"""
Configuration för API endpoints
Läser från environment variables
"""

import os

class Config:
    # API Security
    UPDATE_API_KEY = os.getenv('UPDATE_API_KEY', 'dev-key-change-in-production')
    
    # Rate Limiting
    MAX_UPDATES_PER_HOUR = int(os.getenv('MAX_UPDATES_PER_HOUR', '3'))
    COOLDOWN_MINUTES = int(os.getenv('COOLDOWN_MINUTES', '5'))
    
    # Timeouts
    SCRAPER_TIMEOUT = int(os.getenv('SCRAPER_TIMEOUT_SECONDS', '300'))
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT_SECONDS', '30'))
    
    # Debugging
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    
    # Monitoring
    SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK_URL', '')
    EMAIL_ALERTS = os.getenv('EMAIL_ALERTS', '')
    
    @classmethod
    def is_production(cls):
        """Check if running in production"""
        return os.getenv('VERCEL_ENV') == 'production'
    
    @classmethod
    def validate(cls):
        """Validera att critical config finns"""
        errors = []
        
        if cls.is_production():
            if cls.UPDATE_API_KEY == 'dev-key-change-in-production':
                errors.append('UPDATE_API_KEY måste sättas i produktion!')
        
        return errors

