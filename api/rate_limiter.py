"""
Rate Limiter för Update API
Förhindrar spam och överbelastning
"""

import time
import json
import os
from pathlib import Path

class UpdateRateLimiter:
    def __init__(self, max_requests=3, window_minutes=60, cooldown_minutes=5):
        """
        Args:
            max_requests: Max antal updates per window
            window_minutes: Tidsfönster i minuter
            cooldown_minutes: Min tid mellan updates
        """
        self.max_requests = max_requests
        self.window_seconds = window_minutes * 60
        self.cooldown_seconds = cooldown_minutes * 60
        
        # Storage file för rate limit data
        self.storage_file = Path('/tmp/update_rate_limits.json')
        self.requests = self._load_requests()
    
    def _load_requests(self):
        """Ladda tidigare requests från disk"""
        if self.storage_file.exists():
            try:
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def _save_requests(self):
        """Spara requests till disk"""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.requests, f)
        except:
            pass
    
    def _cleanup_old_requests(self, client_id):
        """Ta bort gamla requests utanför window"""
        now = time.time()
        if client_id in self.requests:
            self.requests[client_id] = [
                ts for ts in self.requests[client_id]
                if now - ts < self.window_seconds
            ]
    
    def is_allowed(self, client_id):
        """
        Kontrollera om client får göra en update
        
        Returns:
            (bool, str): (allowed, reason/message)
        """
        now = time.time()
        
        # Initiera om ny client
        if client_id not in self.requests:
            self.requests[client_id] = []
        
        # Rensa gamla requests
        self._cleanup_old_requests(client_id)
        
        # Kontrollera cooldown (senaste request)
        if self.requests[client_id]:
            last_request = max(self.requests[client_id])
            time_since_last = now - last_request
            
            if time_since_last < self.cooldown_seconds:
                wait_minutes = int((self.cooldown_seconds - time_since_last) / 60)
                return False, f"Vänta {wait_minutes} minuter innan nästa uppdatering"
        
        # Kontrollera max requests per window
        if len(self.requests[client_id]) >= self.max_requests:
            oldest_request = min(self.requests[client_id])
            time_until_reset = int((self.window_seconds - (now - oldest_request)) / 60)
            return False, f"För många uppdateringar. Försök igen om {time_until_reset} minuter"
        
        # Tillåt request
        self.requests[client_id].append(now)
        self._save_requests()
        return True, "OK"
    
    def get_stats(self, client_id):
        """Hämta statistik för en client"""
        self._cleanup_old_requests(client_id)
        
        requests_count = len(self.requests.get(client_id, []))
        remaining = self.max_requests - requests_count
        
        return {
            'requests_used': requests_count,
            'requests_remaining': remaining,
            'requests_max': self.max_requests,
            'window_minutes': self.window_seconds / 60
        }

