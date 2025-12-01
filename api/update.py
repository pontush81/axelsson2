"""
API endpoint för att trigga dokumentationsuppdatering
Körs som Vercel Serverless Function

Säkerhetsfunktioner:
- Rate limiting (max 3 updates/timme)
- Queue system (endast en update åt gången)
- API-nyckel autentisering
- Audit logging
"""

from http.server import BaseHTTPRequestHandler
import json
import subprocess
import os
from datetime import datetime
import hashlib

# Import våra säkerhetsmoduler
try:
    from .rate_limiter import UpdateRateLimiter
    from .update_queue import UpdateQueue
    from .auth import SecureAuth
    from .config import Config
except:
    # Fallback för lokal testning
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from rate_limiter import UpdateRateLimiter
    from update_queue import UpdateQueue
    from auth import SecureAuth
    from config import Config

# Initialize säkerhetsmoduler
rate_limiter = UpdateRateLimiter(
    max_requests=Config.MAX_UPDATES_PER_HOUR,
    window_minutes=60,
    cooldown_minutes=Config.COOLDOWN_MINUTES
)
update_queue = UpdateQueue()
secure_auth = SecureAuth()

def get_client_ip(request):
    """Hämta klientens IP-adress"""
    # Vercel sätter X-Forwarded-For
    ip = request.headers.get('X-Forwarded-For', '').split(',')[0].strip()
    if not ip:
        ip = request.headers.get('X-Real-IP', 'unknown')
    return ip

def get_client_id(ip):
    """Hash IP för anonymisering i logs"""
    return hashlib.sha256(ip.encode()).hexdigest()[:16]

def verify_request(request):
    """
    Säker verifiering med flera lager
    
    1. IP-whitelist (om konfigurerad)
    2. Token-baserad auth (HMAC, ingen synlig nyckel)
    3. Eller session-baserad auth (för admin-panel)
    
    Returns:
        (bool, str, str): (authorized, reason, client_id)
    """
    client_ip = get_client_ip(request)
    client_id = get_client_id(client_ip)
    
    # Layer 1: IP Whitelist (om konfigurerad)
    ip_allowed, ip_message = secure_auth.verify_ip(client_ip)
    if not ip_allowed:
        return False, ip_message, client_id
    
    # Layer 2: Token-baserad auth
    update_token = request.headers.get('X-Update-Token')
    if update_token:
        token_valid, token_message = secure_auth.verify_update_token(update_token, client_ip)
        if token_valid:
            return True, "Token verified", client_id
        else:
            return False, token_message, client_id
    
    # Layer 3: Session-baserad auth (för admin)
    session_token = request.headers.get('X-Session-Token')
    if session_token:
        session_valid, session_message = secure_auth.verify_session(session_token)
        if session_valid:
            return True, "Session verified", client_id
        else:
            return False, session_message, client_id
    
    # Ingen giltig auth
    return False, "Ingen giltig autentisering (token eller session saknas)", client_id

def log_update_attempt(client_id, success, message, changes=None):
    """Logga update-försök för audit"""
    log_file = Path('/tmp/update_audit.log')
    
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'client_id': client_id,
        'success': success,
        'message': message,
        'changes': changes
    }
    
    try:
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    except:
        pass

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Trigga en inkrementell scraping"""
        client_ip = get_client_ip(self)
        client_id = get_client_id(client_ip)
        
        try:
            # 1. Säker autentisering (IP + Token)
            authorized, auth_message, _ = verify_request(self)
            
            if not authorized:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    'success': False,
                    'message': auth_message,
                    'code': 'UNAUTHORIZED'
                }
                
                log_update_attempt(client_id, False, f'Unauthorized: {auth_message}')
                self.wfile.write(json.dumps(response).encode())
                return
            
            # 2. Kontrollera rate limiting
            allowed, rate_message = rate_limiter.is_allowed(client_id)
            if not allowed:
                self.send_response(429)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Retry-After', '300')  # 5 minutes
                self.end_headers()
                
                response = {
                    'success': False,
                    'message': rate_message,
                    'code': 'RATE_LIMITED',
                    'stats': rate_limiter.get_stats(client_id)
                }
                
                log_update_attempt(client_id, False, rate_message)
                self.wfile.write(json.dumps(response).encode())
                return
            
            # 3. Kontrollera om update redan körs
            is_running, lock_info = update_queue.is_update_running()
            if is_running:
                # Lägg till i kö
                position = update_queue.add_to_queue(client_id)
                
                self.send_response(202)  # Accepted
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    'success': False,
                    'message': f'En uppdatering pågår redan. Du är nummer {position} i kön.',
                    'code': 'QUEUED',
                    'queue_position': position,
                    'queue_status': update_queue.get_queue_status()
                }
                
                self.wfile.write(json.dumps(response).encode())
                return
            
            # 4. Acquire lock
            acquired, lock_message = update_queue.acquire_lock(client_id)
            if not acquired:
                self.send_response(409)  # Conflict
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    'success': False,
                    'message': lock_message,
                    'code': 'LOCKED'
                }
                
                self.wfile.write(json.dumps(response).encode())
                return
            
            # CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-API-Key, Authorization')
            self.end_headers()
            
            # 5. Kör scraper i inkrementellt läge
            try:
                result = subprocess.run(
                    ['python3', 'scraper_incremental.py', '--incremental'],
                    capture_output=True,
                    text=True,
                    timeout=300,  # 5 minuter timeout
                    cwd=os.path.dirname(os.path.dirname(__file__))
                )
                
                if result.returncode == 0:
                    # Parse output för att hitta antal ändringar
                    output = result.stdout
                    changes = {
                        'new': 0,
                        'updated': 0,
                        'deleted': 0
                    }
                    
                    # Leta efter mönster som "✓ 5 nya artiklar", "✓ 3 uppdaterade", etc.
                    import re
                    new_match = re.search(r'(\d+)\s+nya', output)
                    updated_match = re.search(r'(\d+)\s+uppdaterade', output)
                    deleted_match = re.search(r'(\d+)\s+raderade', output)
                    
                    if new_match:
                        changes['new'] = int(new_match.group(1))
                    if updated_match:
                        changes['updated'] = int(updated_match.group(1))
                    if deleted_match:
                        changes['deleted'] = int(deleted_match.group(1))
                    
                    # Log success
                    log_update_attempt(client_id, True, 'Update completed', changes)
                    
                    response = {
                        'success': True,
                        'message': 'Dokumentation uppdaterad',
                        'timestamp': datetime.now().isoformat(),
                        'changes': changes,
                        'output': output if os.getenv('DEBUG') else None
                    }
                else:
                    # Log failure
                    log_update_attempt(client_id, False, f'Scraper failed: {result.stderr}')
                    
                    response = {
                        'success': False,
                        'message': 'Fel vid uppdatering',
                        'error': result.stderr if os.getenv('DEBUG') else 'Se serverloggar'
                    }
                
            finally:
                # 6. Release lock oavsett resultat
                update_queue.release_lock()
            
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'success': False,
                'message': 'Serverfel',
                'error': str(e)
            }
            
            self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

