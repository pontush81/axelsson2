/**
 * Test endpoint - Verifiera att API fungerar
 */

module.exports = async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Content-Type', 'application/json');
    
    return res.status(200).json({
        success: true,
        message: 'API fungerar! Node.js runtime OK ✅',
        timestamp: new Date().toISOString(),
        env: process.env.VERCEL_ENV || 'development'
    });
};

