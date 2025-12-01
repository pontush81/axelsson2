"""
Säker autentisering för update endpoint
Flera säkerhetslager utan att exponera API-nyckel i frontend
"""

import os
import hashlib
import hmac
import time
import json
from pathlib import Path

class SecureAuth:
    """Säker autentisering utan synlig API-nyckel i frontend"""
    
    def __init__(self):
        self.allowed_ips_file = Path('/tmp/allowed_ips.json')
        self.sessions_file = Path('/tmp/admin_sessions.json')
        
    def _load_allowed_ips(self):
        """Ladda tillåtna IP-adresser"""
        # Från environment (komma-separerad lista)
        env_ips = os.getenv('ALLOWED_UPDATE_IPS', '')
        if env_ips:
            return [ip.strip() for ip in env_ips.split(',') if ip.strip()]
        
        # Från fil
        if self.allowed_ips_file.exists():
            try:
                with open(self.allowed_ips_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return []
    
    def verify_ip(self, client_ip):
        """
        Verifiera att IP är tillåten
        
        Returns:
            (bool, str): (allowed, message)
        """
        allowed_ips = self._load_allowed_ips()
        
        # Om ingen IP-lista finns, tillåt alla (development mode)
        if not allowed_ips:
            if os.getenv('VERCEL_ENV') == 'production':
                return False, "IP-whitelist ej konfigurerad i produktion"
            return True, "Development mode - alla IPs tillåtna"
        
        if client_ip in allowed_ips:
            return True, "IP verified"
        
        return False, f"IP {client_ip} är inte tillåten att uppdatera"
    
    def generate_update_token(self, client_ip):
        """
        Generera en tidsbegränsad token för client
        Token är giltig i 1 timme
        
        Args:
            client_ip: Klientens IP-adress
            
        Returns:
            str: Säker token
        """
        secret = os.getenv('UPDATE_API_KEY', 'dev-key-change-in-production')
        timestamp = int(time.time())
        
        # Token = HMAC(secret, client_ip + timestamp)
        message = f"{client_ip}:{timestamp}"
        token = hmac.new(
            secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return f"{timestamp}:{token}"
    
    def verify_update_token(self, token, client_ip):
        """
        Verifiera en update token
        
        Args:
            token: Token från client (format: "timestamp:hash")
            client_ip: Klientens IP-adress
            
        Returns:
            (bool, str): (valid, message)
        """
        if not token:
            return False, "Token saknas"
        
        try:
            parts = token.split(':')
            if len(parts) != 2:
                return False, "Ogiltigt token-format"
            
            timestamp_str, provided_hash = parts
            timestamp = int(timestamp_str)
            
            # Check token age (max 1 timme)
            now = int(time.time())
            age_seconds = now - timestamp
            
            if age_seconds > 3600:  # 1 timme
                return False, "Token har gått ut. Ladda om sidan."
            
            if age_seconds < 0:
                return False, "Ogiltigt token (framtida timestamp)"
            
            # Verifiera token
            secret = os.getenv('UPDATE_API_KEY', 'dev-key-change-in-production')
            message = f"{client_ip}:{timestamp}"
            expected_hash = hmac.new(
                secret.encode(),
                message.encode(),
                hashlib.sha256
            ).hexdigest()
            
            if hmac.compare_digest(provided_hash, expected_hash):
                return True, "Token verified"
            else:
                return False, "Ogiltigt token"
                
        except Exception as e:
            return False, f"Token verification error: {str(e)}"
    
    def create_session(self, username, password):
        """
        Skapa admin session (för framtida admin-panel)
        
        Args:
            username: Admin användarnamn
            password: Admin lösenord
            
        Returns:
            (bool, str|None): (success, session_token)
        """
        # Kolla credentials
        admin_user = os.getenv('ADMIN_USERNAME', 'admin')
        admin_pass_hash = os.getenv('ADMIN_PASSWORD_HASH', '')
        
        # Hash lösenordet
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if username == admin_user and password_hash == admin_pass_hash:
            # Skapa session token
            session_token = hashlib.sha256(
                f"{username}:{time.time()}:{os.urandom(16).hex()}".encode()
            ).hexdigest()
            
            # Spara session
            sessions = self._load_sessions()
            sessions[session_token] = {
                'username': username,
                'created_at': time.time(),
                'expires_at': time.time() + 86400  # 24 timmar
            }
            self._save_sessions(sessions)
            
            return True, session_token
        
        return False, None
    
    def verify_session(self, session_token):
        """
        Verifiera admin session
        
        Returns:
            (bool, str): (valid, message)
        """
        if not session_token:
            return False, "Session token saknas"
        
        sessions = self._load_sessions()
        session = sessions.get(session_token)
        
        if not session:
            return False, "Ogiltig session"
        
        # Check expiration
        if time.time() > session['expires_at']:
            return False, "Session har gått ut"
        
        return True, f"Session verified för {session['username']}"
    
    def _load_sessions(self):
        """Ladda sessions från disk"""
        if self.sessions_file.exists():
            try:
                with open(self.sessions_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def _save_sessions(self, sessions):
        """Spara sessions till disk"""
        # Cleanup gamla sessions
        now = time.time()
        sessions = {
            token: data for token, data in sessions.items()
            if data['expires_at'] > now
        }
        
        with open(self.sessions_file, 'w') as f:
            json.dump(sessions, f)

