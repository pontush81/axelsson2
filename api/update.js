/**
 * Update Endpoint
 * Triggar inkrementell scraping med säker autentisering
 */

const crypto = require('crypto');
const { exec } = require('child_process');
const { promisify } = require('util');
const execAsync = promisify(exec);

// Rate limiter (in-memory för enkelhetens skull)
const rateLimits = new Map();
const updateLocks = new Map();

function getClientIp(req) {
    const forwarded = req.headers['x-forwarded-for'];
    if (forwarded) {
        return forwarded.split(',')[0].trim();
    }
    return req.headers['x-real-ip'] || 'unknown';
}

function verifyToken(token, clientIp) {
    if (!token) {
        return { valid: false, message: 'Token saknas' };
    }
    
    try {
        const parts = token.split(':');
        if (parts.length !== 2) {
            return { valid: false, message: 'Ogiltigt token-format' };
        }
        
        const [timestampStr, providedHash] = parts;
        const timestamp = parseInt(timestampStr);
        
        // Check token age (max 1 timme)
        const now = Math.floor(Date.now() / 1000);
        const ageSeconds = now - timestamp;
        
        if (ageSeconds > 3600) {
            return { valid: false, message: 'Token har gått ut. Ladda om sidan.' };
        }
        
        if (ageSeconds < 0) {
            return { valid: false, message: 'Ogiltigt token' };
        }
        
        // Verifiera HMAC
        const secret = process.env.UPDATE_API_KEY || 'dev-key-change-in-production';
        const message = `${clientIp}:${timestamp}`;
        const hmac = crypto.createHmac('sha256', secret);
        hmac.update(message);
        const expectedHash = hmac.digest('hex');
        
        if (crypto.timingSafeEqual(Buffer.from(providedHash), Buffer.from(expectedHash))) {
            return { valid: true, message: 'Token verified' };
        }
        
        return { valid: false, message: 'Ogiltigt token' };
        
    } catch (error) {
        return { valid: false, message: `Token verification error: ${error.message}` };
    }
}

function checkRateLimit(clientIp) {
    const maxRequests = parseInt(process.env.MAX_UPDATES_PER_HOUR || '3');
    const cooldownMinutes = parseInt(process.env.COOLDOWN_MINUTES || '5');
    const cooldownSeconds = cooldownMinutes * 60;
    const windowSeconds = 3600; // 1 timme
    
    const now = Date.now() / 1000;
    const clientKey = crypto.createHash('sha256').update(clientIp).digest('hex').substring(0, 16);
    
    if (!rateLimits.has(clientKey)) {
        rateLimits.set(clientKey, []);
    }
    
    const requests = rateLimits.get(clientKey);
    
    // Rensa gamla requests
    const validRequests = requests.filter(ts => now - ts < windowSeconds);
    rateLimits.set(clientKey, validRequests);
    
    // Kolla cooldown
    if (validRequests.length > 0) {
        const lastRequest = Math.max(...validRequests);
        const timeSinceLast = now - lastRequest;
        
        if (timeSinceLast < cooldownSeconds) {
            const waitMinutes = Math.ceil((cooldownSeconds - timeSinceLast) / 60);
            return {
                allowed: false,
                message: `Vänta ${waitMinutes} minuter innan nästa uppdatering`
            };
        }
    }
    
    // Kolla max requests
    if (validRequests.length >= maxRequests) {
        const oldestRequest = Math.min(...validRequests);
        const timeUntilReset = Math.ceil((windowSeconds - (now - oldestRequest)) / 60);
        return {
            allowed: false,
            message: `För många uppdateringar. Försök igen om ${timeUntilReset} minuter`
        };
    }
    
    // Tillåt och lägg till timestamp
    validRequests.push(now);
    rateLimits.set(clientKey, validRequests);
    
    return { allowed: true, message: 'OK' };
}

function checkUpdateLock() {
    const now = Date.now() / 1000;
    
    // Cleanup gamla locks (timeout efter 10 minuter)
    for (const [key, lock] of updateLocks.entries()) {
        if (now - lock.timestamp > 600) {
            updateLocks.delete(key);
        }
    }
    
    // Kolla om något lock finns
    if (updateLocks.size > 0) {
        const lock = Array.from(updateLocks.values())[0];
        return {
            locked: true,
            message: `En uppdatering pågår redan (startad ${new Date(lock.timestamp * 1000).toLocaleTimeString('sv-SE')})`
        };
    }
    
    return { locked: false };
}

function acquireLock(clientId) {
    const lockCheck = checkUpdateLock();
    
    if (lockCheck.locked) {
        return { acquired: false, message: lockCheck.message };
    }
    
    updateLocks.set(clientId, {
        timestamp: Date.now() / 1000,
        clientId: clientId
    });
    
    return { acquired: true };
}

function releaseLock(clientId) {
    updateLocks.delete(clientId);
}

module.exports = async (req, res) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Update-Token');
    
    // Handle OPTIONS
    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }
    
    const clientIp = getClientIp(req);
    const clientId = crypto.createHash('sha256').update(clientIp).digest('hex').substring(0, 16);
    
    try {
        // 1. Verifiera token
        const token = req.headers['x-update-token'];
        const tokenCheck = verifyToken(token, clientIp);
        
        if (!tokenCheck.valid) {
            return res.status(401).json({
                success: false,
                message: tokenCheck.message,
                code: 'UNAUTHORIZED'
            });
        }
        
        // 2. Rate limiting
        const rateCheck = checkRateLimit(clientIp);
        if (!rateCheck.allowed) {
            return res.status(429).json({
                success: false,
                message: rateCheck.message,
                code: 'RATE_LIMITED'
            });
        }
        
        // 3. Check lock
        const lockCheck = checkUpdateLock();
        if (lockCheck.locked) {
            return res.status(409).json({
                success: false,
                message: lockCheck.message,
                code: 'LOCKED'
            });
        }
        
        // 4. Acquire lock
        const lock = acquireLock(clientId);
        if (!lock.acquired) {
            return res.status(409).json({
                success: false,
                message: lock.message,
                code: 'LOCKED'
            });
        }
        
        try {
            // 5. Kör scraper (Python)
            const { stdout, stderr } = await execAsync(
                'python3 scraper_incremental.py --incremental',
                { 
                    timeout: 300000, // 5 minuter
                    maxBuffer: 10 * 1024 * 1024 // 10MB
                }
            );
            
            // Parse output för ändringar
            const changes = {
                new: 0,
                updated: 0,
                deleted: 0
            };
            
            const newMatch = stdout.match(/(\d+)\s+nya/);
            const updatedMatch = stdout.match(/(\d+)\s+uppdaterade/);
            const deletedMatch = stdout.match(/(\d+)\s+raderade/);
            
            if (newMatch) changes.new = parseInt(newMatch[1]);
            if (updatedMatch) changes.updated = parseInt(updatedMatch[1]);
            if (deletedMatch) changes.deleted = parseInt(deletedMatch[1]);
            
            return res.status(200).json({
                success: true,
                message: 'Dokumentation uppdaterad',
                changes: changes,
                timestamp: new Date().toISOString()
            });
            
        } catch (error) {
            console.error('Scraper error:', error);
            
            return res.status(500).json({
                success: false,
                message: 'Fel vid uppdatering',
                error: process.env.DEBUG === 'true' ? error.message : 'Se serverloggar'
            });
            
        } finally {
            // Release lock
            releaseLock(clientId);
        }
        
    } catch (error) {
        console.error('Update endpoint error:', error);
        
        return res.status(500).json({
            success: false,
            message: `Serverfel: ${error.message}`,
            code: 'SERVER_ERROR'
        });
    }
};

