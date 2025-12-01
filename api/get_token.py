"""
Token Generator Endpoint
Genererar säkra tokens för update-funktionen
Tokens är IP-bundna och tidsbegränsade (1 timme)
"""

from http.server import BaseHTTPRequestHandler
import json
import hashlib

try:
    from .auth import SecureAuth
except:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from auth import SecureAuth

secure_auth = SecureAuth()

def get_client_ip(request):
    """Hämta klientens IP-adress"""
    ip = request.headers.get('X-Forwarded-For', '').split(',')[0].strip()
    if not ip:
        ip = request.headers.get('X-Real-IP', 'unknown')
    return ip

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Generera en update token för denna klient"""
        try:
            client_ip = get_client_ip(self)
            
            # Verifiera IP först
            ip_allowed, ip_message = secure_auth.verify_ip(client_ip)
            
            if not ip_allowed:
                self.send_response(403)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    'success': False,
                    'message': ip_message,
                    'code': 'IP_NOT_ALLOWED'
                }
                
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Generera token
            token = secure_auth.generate_update_token(client_ip)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.end_headers()
            
            response = {
                'success': True,
                'token': token,
                'expires_in': 3600,  # 1 timme
                'message': 'Token genererad'
            }
            
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': False,
                'message': f'Serverfel: {str(e)}',
                'code': 'SERVER_ERROR'
            }
            
            self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

