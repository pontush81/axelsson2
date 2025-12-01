"""
Update Queue System
Endast en scraping åt gången, övriga köas
"""

import json
import time
import os
from pathlib import Path
from datetime import datetime

class UpdateQueue:
    def __init__(self):
        """Initialize queue system"""
        self.lock_file = Path('/tmp/update_lock.json')
        self.queue_file = Path('/tmp/update_queue.json')
    
    def _read_lock(self):
        """Läs lock-fil"""
        if self.lock_file.exists():
            try:
                with open(self.lock_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return None
    
    def _write_lock(self, data):
        """Skriv lock-fil"""
        with open(self.lock_file, 'w') as f:
            json.dump(data, f)
    
    def _remove_lock(self):
        """Ta bort lock"""
        if self.lock_file.exists():
            self.lock_file.unlink()
    
    def _read_queue(self):
        """Läs kö"""
        if self.queue_file.exists():
            try:
                with open(self.queue_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def _write_queue(self, queue):
        """Skriv kö"""
        with open(self.queue_file, 'w') as f:
            json.dump(queue, f)
    
    def is_update_running(self):
        """
        Kontrollera om en update redan körs
        
        Returns:
            (bool, dict|None): (is_running, lock_info)
        """
        lock = self._read_lock()
        
        if not lock:
            return False, None
        
        # Kontrollera om lock är för gammal (timeout efter 10 minuter)
        lock_age = time.time() - lock.get('timestamp', 0)
        if lock_age > 600:  # 10 minuter timeout
            # Lock är för gammal, ta bort den
            self._remove_lock()
            return False, None
        
        return True, lock
    
    def acquire_lock(self, client_id):
        """
        Försök ta lock för att köra update
        
        Returns:
            (bool, str): (acquired, message)
        """
        is_running, lock_info = self.is_update_running()
        
        if is_running:
            started_at = datetime.fromtimestamp(lock_info['timestamp']).strftime('%H:%M:%S')
            return False, f"En uppdatering pågår redan (startad {started_at})"
        
        # Skapa lock
        lock_data = {
            'client_id': client_id,
            'timestamp': time.time(),
            'started_at': datetime.now().isoformat()
        }
        self._write_lock(lock_data)
        
        return True, "Lock acquired"
    
    def release_lock(self):
        """Släpp lock efter update"""
        self._remove_lock()
    
    def add_to_queue(self, client_id):
        """
        Lägg till client i kö
        
        Returns:
            int: Position i kön
        """
        queue = self._read_queue()
        
        # Kontrollera om client redan är i kön
        if client_id in [item['client_id'] for item in queue]:
            position = [item['client_id'] for item in queue].index(client_id) + 1
            return position
        
        # Lägg till i kö
        queue.append({
            'client_id': client_id,
            'timestamp': time.time(),
            'added_at': datetime.now().isoformat()
        })
        
        self._write_queue(queue)
        return len(queue)
    
    def get_queue_status(self):
        """Hämta status för kön"""
        queue = self._read_queue()
        is_running, lock_info = self.is_update_running()
        
        return {
            'is_running': is_running,
            'current_update': lock_info,
            'queue_length': len(queue),
            'queue': queue
        }
    
    def cleanup_old_queue_items(self, max_age_minutes=30):
        """Ta bort gamla items från kön"""
        queue = self._read_queue()
        now = time.time()
        max_age_seconds = max_age_minutes * 60
        
        cleaned_queue = [
            item for item in queue
            if now - item.get('timestamp', 0) < max_age_seconds
        ]
        
        self._write_queue(cleaned_queue)
        return len(queue) - len(cleaned_queue)

