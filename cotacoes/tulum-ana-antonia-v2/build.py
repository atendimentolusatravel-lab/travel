import re
src = open('index.html', encoding='utf-8').read()

# ---------- split CSS ----------
m = re.search(r'<style>\n(.*?)</style>\n', src, re.S)
css = m.group(1)
src = src.replace(m.group(0), '<link rel="stylesheet" href="style.css">\n')
# alternate backgrounds: valores section becomes cream (new passeios section is white)
css += '.sec-cream{background:var(--cream)}\n'

def rep(old, new, count=1):
    global src
    assert src.count(old) == count, (old[:60], src.count(old))
    src = src.replace(old, new)

# ---------- title / hero ----------
rep('<title>Lusa Travel · Tulum — Ana e Antonia</title>', '<title>Lusa Travel · Tulum — Ana e Antonia · revisão</title>')
rep('Cotação emitida em <b>29/09/2026</b>', 'Cotação emitida em <b>29/09/2026</b> · revisada em <b>26/10/2026</b>')
rep('<b>2</b>&nbsp;Excursões</div>', '<b>5</b>&nbsp;Passeios</div>')

# ---------- transfers ----------
rep('Valor total do conjunto: <b>R$ 6.622</b>. Parcelável em <b>até 5x</b>', 'Valor total do conjunto: <b>R$ 6.338</b>. Parcelável em <b>até 5x</b>')
rep('R$ 3.542</span>', 'R$ 3.393</span>')
rep('R$ 3.080</span>', 'R$ 2.945</span>')
rep('Os dois transfers somam <b>R$ 6.622</b>', 'Os dois transfers somam <b>R$ 6.338</b>')

# ---------- seguro ----------
rep('R$ 930</span>', 'R$ 980</span>')

# ---------- excursões: rename section ----------
rep('<h2>Excursões</h2>', '<h2>Excursões de barco</h2>')

# ---------- new section: passeios ----------
ICO_RUINS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20h18M5 20v-4h14v4M7 16v-4h10v4M9 12V8h6v4M11 8V5h2v3"/></svg>'
ICO_CENOTE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3s6 7 6 11a6 6 0 01-12 0c0-4 6-11 6-11z"/><path d="M9 14a3 3 0 003 3"/></svg>'
ICO_SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20h18M6 20l6-13 6 13"/><path d="M9 20l3-6 3 6"/><circle cx="18" cy="6" r="2.5"/></svg>'

def card(ico, title, d, sub, p, fine, price):
    return f'''    <div class="expcard">
      <div class="svc"><div class="ic">{ico}</div>
        <div><div class="t">{title}</div><div class="d">{d}
          <div class="sub">{sub}</div>
          <p>{p}</p>
          <div class="fine">{fine}</div>
        </div></div><div class="dt">Data a definir<br><span style="color:var(--green);font-size:1.05rem">R$ {price}</span></div></div>
    </div>
'''

passeios = '''  <!-- ================= PASSEIOS ================= -->
  <section class="section sh">
    <span class="eyebrow">Experiências</span>
    <h2>Passeios em Tulum e Cancún</h2>
    <div class="accent-line"></div>
    <p class="note" style="margin-top:16px">Três passeios em terra — ruínas maias, cenotes e Chichén Itzá — com <b>datas a definir</b> dentro da janela da viagem. Valores para <b>4 adultos</b>. Valor total do conjunto: <b>R$ 9.446</b>.</p>

''' + card(ICO_RUINS,
    'Tulum: ruínas, 2 cenotes secretos e almoço mexicano',
    '<b>Dia inteiro</b> · <b>grupo pequeno</b> · guia especializado · almoço incluso · <b>4 adultos</b>',
    'Ruínas maias de frente para o Caribe e cenotes escondidos na selva',
    'Explore as famosas ruínas maias de <b>Tulum</b>, de frente para o Mar do Caribe. Nade em <b>cenotes secretos</b> escondidos na selva e aproveite um <b>almoço mexicano tradicional</b>. Aprenda sobre a história maia com um guia especializado e viva uma experiência mais exclusiva, em pequenos grupos.',
    'Data e horário a definir junto com vocês. Confirmação sujeita à disponibilidade na data escolhida.',
    '4.464') + '\n' + card(ICO_CENOTE,
    'Cenote Triple Adventure Tour (Grand Cenote Tour)',
    '<b>Meio dia</b> · saída de <b>Tulum</b> · visita guiada · <b>três cenotes</b> · <b>4 adultos</b>',
    'Três cenotes em meio período: mergulho, snorkel e salto do penhasco',
    'Mergulhe livremente, faça <b>snorkel</b> e pule de um penhasco em <b>três cenotes diferentes</b> nesta visita guiada de meio dia saindo de Tulum. Pule de plataformas em níveis no <b>Cenote Zemway</b>, explore o <b>Gran Cenote</b> e os manguezais do <b>Cenote Casa</b>.',
    'Data e horário a definir junto com vocês. Confirmação sujeita à disponibilidade na data escolhida.',
    '3.492') + '\n' + card(ICO_SUN,
    'Cancún: Tour Chichén Itzá, Cenote e Valladolid com almoço',
    '<b>Dia inteiro</b> · <b>Chichén Itzá</b> · cenote · Valladolid · almoço incluso · <b>4 adultos</b>',
    'Uma das sete maravilhas do mundo moderno, um cenote e a Valladolid colonial',
    'Desvende os mistérios dos maias neste passeio de dia inteiro. Visite <b>Chichén Itzá</b>, dê um mergulho refrescante em um <b>cenote</b> e descubra a cidade colonial de <b>Valladolid</b>. Desfrute de uma <b>degustação de tequila</b> incluída!',
    'Data a definir junto com vocês. Passeio operado a partir da região de Cancún — o ponto de encontro a partir de Tulum é confirmado na reserva.',
    '1.490') + '''
    <div class="pkg-note">🏛️ Os três passeios somam <b>R$ 9.446</b> para os <b>4 adultos</b>. As datas ficam em aberto para encaixar com as excursões de barco já cotadas para 02/01 e 04/01.</div>
  </section>

'''
rep('  <!-- ================= VALORES ================= -->\n  <section class="section sh">', passeios + '  <!-- ================= VALORES ================= -->\n  <section class="section sh sec-cream">')

# ---------- resumo ----------
rep('<td class="v">R$ 3.542</td>', '<td class="v">R$ 3.393</td>')
rep('<td class="v">R$ 3.080</td>', '<td class="v">R$ 2.945</td>')
rep('<tr class="total-row"><td>Total transfers</td><td></td><td class="v">R$ 6.622</td></tr>', '<tr class="total-row"><td>Total transfers</td><td></td><td class="v">R$ 6.338</td></tr>')
rep('<td class="v">R$ 930</td>', '<td class="v">R$ 980</td>')
rep('<tr class="sec-row"><td colspan="3">Excurs&otilde;es</td></tr>', '<tr class="sec-row"><td colspan="3">Excurs&otilde;es de barco</td></tr>')
rep('<tr class="total-row"><td>Total excurs&otilde;es</td><td></td><td class="v">R$ 6.160</td></tr>',
    '''<tr class="total-row"><td>Total excurs&otilde;es de barco</td><td></td><td class="v">R$ 6.160</td></tr>

        <tr class="sec-row"><td colspan="3">Passeios em Tulum e Canc&uacute;n</td></tr>
        <tr><td>Tulum: ru&iacute;nas, 2 cenotes secretos e almo&ccedil;o mexicano<div class="rm">dia inteiro &middot; grupo pequeno &middot; 4 adultos</div></td><td>a definir</td><td class="v">R$ 4.464</td></tr>
        <tr><td>Cenote Triple Adventure Tour (Grand Cenote Tour)<div class="rm">meio dia &middot; saída de Tulum &middot; 4 adultos</div></td><td>a definir</td><td class="v">R$ 3.492</td></tr>
        <tr><td>Canc&uacute;n: Chich&eacute;n Itz&aacute;, Cenote e Valladolid com almo&ccedil;o<div class="rm">dia inteiro &middot; 4 adultos</div></td><td>a definir</td><td class="v">R$ 1.490</td></tr>
        <tr class="total-row"><td>Total passeios</td><td></td><td class="v">R$ 9.446</td></tr>''')
rep('<tr class="total-row"><td>Transfers + seguro + excurs&otilde;es</td><td>4 adultos</td><td class="v">R$ 13.712</td></tr>',
    '<tr class="total-row"><td>Transfers + seguro + excurs&otilde;es + passeios</td><td>4 adultos</td><td class="v">R$ 22.924</td></tr>')

# ---------- pagamento / obs ----------
rep('<p><b>Excursões</b> — em até <b>3x</b></p>', '<p><b>Excursões de barco</b> — em até <b>3x</b></p>\n        <p><b>Passeios em Tulum e Cancún</b> — condições confirmadas na reserva</p>')
rep('<li>Hospedagem, aéreo, refeições fora das excursões, gorjetas e despesas pessoais</li>',
    '<li>Hospedagem, aéreo, refeições fora dos passeios, gorjetas e despesas pessoais</li>')
rep('<li>Horários das excursões sujeitos às condições do mar e do tempo.</li>',
    '<li>Horários das excursões sujeitos às condições do mar e do tempo.</li>\n        <li>Os três passeios em Tulum e Cancún estão com <b>data a definir</b> — escolhemos os dias juntos antes de reservar.</li>')

# ---------- light minify of HTML (keep readable) ----------
src = re.sub(r'\n[ \t]+', '\n', src)
src = re.sub(r'\n{2,}', '\n', src)
src = re.sub(r'<!-- =+ [A-ZÇÕÃ ]+ =+ -->\n', '', src)
open('src/index.html', 'w', encoding='utf-8').write(src)
open('src/style.css', 'w', encoding='utf-8').write(css)
print(len(src.encode()), len(css.encode()))
