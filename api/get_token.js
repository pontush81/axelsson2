/**
 * Token Generator Endpoint
 * Genererar säkra tokens för update-funktionen
 */

const crypto = require('crypto');

function generateUpdateToken(clientIp) {
    const secret = process.env.UPDATE_API_KEY || 'dev-key-change-in-production';
    const timestamp = Math.floor(Date.now() / 1000);
    
    // Create HMAC signature
    const message = `${clientIp}:${timestamp}`;
    const hmac = crypto.createHmac('sha256', secret);
    hmac.update(message);
    const hash = hmac.digest('hex');
    
    return `${timestamp}:${hash}`;
}

function getClientIp(req) {
    const forwarded = req.headers['x-forwarded-for'];
    if (forwarded) {
        return forwarded.split(',')[0].trim();
    }
    return req.headers['x-real-ip'] || 'unknown';
}

function checkIpWhitelist(clientIp) {
    const allowedIps = process.env.ALLOWED_UPDATE_IPS;
    
    // Om ingen IP-lista finns, tillåt alla
    if (!allowedIps) {
        return { allowed: true, message: 'IP-whitelist disabled - all IPs allowed' };
    }
    
    // Kolla om IP är i listan
    const ipList = allowedIps.split(',').map(ip => ip.trim());
    
    if (ipList.includes(clientIp)) {
        return { allowed: true, message: 'IP verified' };
    }
    
    return { allowed: false, message: `IP ${clientIp} är inte tillåten att uppdatera` };
}

module.exports = async (req, res) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate');
    
    // Handle OPTIONS (CORS preflight)
    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }
    
    try {
        const clientIp = getClientIp(req);
        
        // Verifiera IP (om whitelist konfigurerad)
        const ipCheck = checkIpWhitelist(clientIp);
        
        if (!ipCheck.allowed) {
            return res.status(403).json({
                success: false,
                message: ipCheck.message,
                code: 'IP_NOT_ALLOWED'
            });
        }
        
        // Generera token
        const token = generateUpdateToken(clientIp);
        
        return res.status(200).json({
            success: true,
            token: token,
            expires_in: 3600,
            message: 'Token genererad'
        });
        
    } catch (error) {
        console.error('Token generation error:', error);
        
        return res.status(500).json({
            success: false,
            message: `Serverfel: ${error.message}`,
            code: 'SERVER_ERROR'
        });
    }
};

