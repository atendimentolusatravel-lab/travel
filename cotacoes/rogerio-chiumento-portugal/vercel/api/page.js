// Serve a cotação (src/index.html do repositório, fixado no commit) como HTML.
export const config = { runtime: 'edge' };

const SRC = 'https://cdn.jsdelivr.net/gh/atendimentolusatravel-lab/travel@e6c7f73e9b3ba56c164ecd3bfcaf595f477d1420/cotacoes/rogerio-chiumento-portugal/src/index.html';

export default async function handler() {
  const r = await fetch(SRC);
  if (!r.ok) {
    return new Response('Página temporariamente indisponível. Tente novamente em instantes.', { status: 502, headers: { 'content-type': 'text/plain; charset=utf-8' } });
  }
  return new Response(await r.text(), {
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'public, max-age=300, s-maxage=86400, stale-while-revalidate=2592000',
      'x-robots-tag': 'noindex'
    }
  });
}
