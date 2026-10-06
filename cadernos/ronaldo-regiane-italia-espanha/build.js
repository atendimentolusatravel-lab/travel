// Decifra caderno.enc (AES-256-GCM) com a chave CADERNO_KEY e gera public/index.html.
// Formato do arquivo: iv (12 bytes) | tag (16 bytes) | texto cifrado.
const fs = require('fs');
const crypto = require('crypto');
const key = Buffer.from((process.env.CADERNO_KEY || '').trim(), 'hex');
if (key.length !== 32) { console.error('CADERNO_KEY ausente ou inválida'); process.exit(1); }
const buf = fs.readFileSync('caderno.enc');
const iv = buf.subarray(0, 12), tag = buf.subarray(12, 28), data = buf.subarray(28);
const d = crypto.createDecipheriv('aes-256-gcm', key, iv);
d.setAuthTag(tag);
const html = Buffer.concat([d.update(data), d.final()]);
fs.mkdirSync('public', { recursive: true });
fs.writeFileSync('public/index.html', html);
fs.copyFileSync('robots.txt', 'public/robots.txt');
console.log('caderno gerado:', html.length, 'bytes');
