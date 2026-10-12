// Portão com senha na frente do servidor do open-slide, para revisão remota pelos sócios.
// Uso: node portao.mjs            (lê a senha de ./senha.txt; ouve em 127.0.0.1:5180 e repassa para 127.0.0.1:5173)
// Quem acerta a senha recebe um cookie e passa a ver o open-slide normalmente (inclusive comentários e a conexão ao vivo).
import http from 'node:http';
import net from 'node:net';
import { readFileSync } from 'node:fs';
import { randomBytes, timingSafeEqual } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const PASTA = dirname(fileURLToPath(import.meta.url));
const SENHA = readFileSync(join(PASTA, 'senha.txt'), 'utf8').trim();
const PORTA_PORTAO = 5180;
const PORTA_SLIDE = 5173;
const COOKIE = 'sttk_revisao';
const SESSAO = randomBytes(24).toString('hex'); // muda a cada vez que o portão liga
const MAX_TENTATIVAS = 10;
const tentativas = new Map(); // ip -> erros

if (SENHA.length < 8) throw new Error('senha.txt precisa ter pelo menos 8 caracteres');

const igual = (a, b) => {
  const x = Buffer.from(a);
  const y = Buffer.from(b);
  return x.length === y.length && timingSafeEqual(x, y);
};

const autorizado = (req) =>
  (req.headers.cookie || '').split(';').some((c) => igual(c.trim(), `${COOKIE}=${SESSAO}`));

// Segunda trava: arquivo pedido direto do disco (/@fs/) só se estiver dentro da pasta do open-slide.
const PASTA_DECK = '/' + join(PASTA, '..', 'adriana-iraja').replace(/\\/g, '/').toLowerCase() + '/';
const caminhoPermitido = (url) => {
  let caminho;
  try { caminho = decodeURIComponent(url.split('?')[0]).replace(/\\/g, '/'); } catch { return false; }
  if (caminho.includes('..')) return false;
  if (!caminho.toLowerCase().startsWith('/@fs/')) return true;
  return ('/' + caminho.slice(5).replace(/^\/+/, '')).toLowerCase().startsWith(PASTA_DECK);
};

const ipDe = (req) => String(req.headers['cf-connecting-ip'] || req.socket.remoteAddress);

const telaSenha = (erro) => `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Revisão Sttickler</title>
<style>body{font:16px system-ui,sans-serif;background:#f3f1ec;color:#22231f;display:grid;place-items:center;min-height:100vh;margin:0}
form{background:#fff;padding:32px;border-radius:12px;display:grid;gap:12px;width:min(340px,90vw);box-shadow:0 2px 12px #0001}
input,button{font:inherit;padding:10px 12px;border-radius:8px;border:1px solid #ccc}button{background:#3f5a4a;color:#fff;border:0;cursor:pointer}
.e{color:#9a3b1f;margin:0}</style></head><body>
<form method="post" action="/__entrar"><b>Revisão da apresentação</b><label for="s">Senha</label>
<input id="s" name="senha" type="password" autofocus required>${erro ? `<p class="e">${erro}</p>` : ''}
<button>Entrar</button></form></body></html>`;

const repassar = (req, res) => {
  const p = http.request(
    { host: 'localhost', port: PORTA_SLIDE, path: req.url, method: req.method,
      headers: { ...req.headers, host: `localhost:${PORTA_SLIDE}` } },
    (r) => { res.writeHead(r.statusCode, r.headers); r.pipe(res); },
  );
  p.on('error', () => { res.writeHead(502); res.end('O open-slide não está ligado no computador do escritório.'); });
  req.pipe(p);
};

const servidor = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/__entrar') {
    const ip = ipDe(req);
    if ((tentativas.get(ip) || 0) >= MAX_TENTATIVAS) { res.writeHead(429); res.end('Muitas tentativas. Peça a senha de novo a Claudemberg.'); return; }
    let corpo = '';
    req.on('data', (d) => { corpo += d; if (corpo.length > 2000) req.destroy(); });
    req.on('end', () => {
      const senha = new URLSearchParams(corpo).get('senha') || '';
      if (igual(senha, SENHA)) {
        tentativas.delete(ip);
        res.writeHead(303, { 'Set-Cookie': `${COOKIE}=${SESSAO}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=43200`, Location: '/s/adriana-proposta' });
        res.end();
      } else {
        tentativas.set(ip, (tentativas.get(ip) || 0) + 1);
        res.writeHead(401, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(telaSenha('Senha errada. Tente de novo.'));
      }
    });
    return;
  }
  if (!autorizado(req)) { res.writeHead(401, { 'Content-Type': 'text/html; charset=utf-8' }); res.end(telaSenha()); return; }
  if (!caminhoPermitido(req.url)) { res.writeHead(403); res.end('Fora da apresentação.'); return; }
  repassar(req, res);
});

// Conexão ao vivo do open-slide (websocket): só passa com o cookie.
servidor.on('upgrade', (req, socket, cabeca) => {
  if (!autorizado(req)) { socket.end('HTTP/1.1 401 Unauthorized\r\n\r\n'); return; }
  const destino = net.connect(PORTA_SLIDE, 'localhost', () => {
    const linhas = [`${req.method} ${req.url} HTTP/1.1`];
    for (const [k, v] of Object.entries({ ...req.headers, host: `localhost:${PORTA_SLIDE}`, origin: `http://localhost:${PORTA_SLIDE}` })) linhas.push(`${k}: ${v}`);
    destino.write(linhas.join('\r\n') + '\r\n\r\n');
    destino.write(cabeca);
    socket.pipe(destino).pipe(socket);
  });
  destino.on('error', () => socket.destroy());
  socket.on('error', () => destino.destroy());
});

servidor.listen(PORTA_PORTAO, '127.0.0.1', () => console.log(`portão ligado em http://127.0.0.1:${PORTA_PORTAO}`));
