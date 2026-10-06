// Uso: CADERNO_KEY=<hex de 64 chars> node encrypt.js <index.html>  →  caderno.enc
const fs = require('fs');
const crypto = require('crypto');
const key = Buffer.from((process.env.CADERNO_KEY || '').trim(), 'hex');
if (key.length !== 32) { console.error('CADERNO_KEY ausente ou inválida'); process.exit(1); }
const html = fs.readFileSync(process.argv[2]);
const iv = crypto.randomBytes(12);
const c = crypto.createCipheriv('aes-256-gcm', key, iv);
const enc = Buffer.concat([c.update(html), c.final()]);
fs.writeFileSync('caderno.enc', Buffer.concat([iv, c.getAuthTag(), enc]));
console.log('caderno.enc:', 28 + enc.length, 'bytes');
