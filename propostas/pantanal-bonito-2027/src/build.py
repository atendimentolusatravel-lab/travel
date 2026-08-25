# -*- coding: utf-8 -*-
import io, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import SCENES
import content as C

FONTS = io.open("fonts.css", encoding="utf-8").read()
GOLD, DEST = "#da8d00", "#2d5e3a"          # ouro fixo · Verde Tropical (América Latina tropical)
MAIL = "atendimentolusatravel@gmail.com"
WA_T, WA_L = "+55 41 99189-6076", "https://wa.me/5541991896076"
ADDR = "Alameda Princesa Izabel, 1700 · Bigorrilho · Curitiba – PR"

def t(x):  # normaliza whitespace do texto editorial
    return re.sub(r"\s+", " ", x).strip()

CSS = """
%(fonts)s
:root{ --gold:%(gold)s; --dest:%(dest)s; --ink:#1a1510; --char:#333131; --mut:#9a8d80; --line:#e4ddd2;
       --sans:'Poppins',system-ui,-apple-system,'Segoe UI',sans-serif; --con:'Montserrat',var(--sans); }
@page{ size:A3 portrait; margin:0; }
*{ box-sizing:border-box; margin:0; padding:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
html,body{ font-family:var(--sans); color:var(--char); }
.page{ width:297mm; height:420mm; position:relative; overflow:hidden; background:#fff;
       page-break-after:always; display:flex; flex-direction:column; }
.page:last-child{ page-break-after:auto; }
.hd{ background:var(--ink); height:26mm; display:flex; align-items:center; justify-content:space-between;
     padding:0 22mm; flex-shrink:0; }
.hd .logo{ font-size:15pt; font-weight:800; letter-spacing:.08em; color:var(--gold); }
.hd .tag{ font-size:8pt; letter-spacing:.24em; text-transform:uppercase; color:rgba(255,255,255,.4); }
.goldbar{ height:2.6mm; background:var(--gold); flex-shrink:0; }
.ft{ margin-top:auto; background:var(--ink); height:14mm; display:flex; align-items:center;
     justify-content:center; gap:14px; flex-shrink:0; }
.ft a{ font-family:var(--con); font-size:8.5pt; color:rgba(255,255,255,.45); text-decoration:none; }
.ft .sep{ color:rgba(255,255,255,.2); }
.body{ padding:16mm 22mm; flex:1; }
.eyebrow{ font-size:8pt; letter-spacing:.22em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.h2{ font-size:22pt; font-weight:700; color:var(--ink); letter-spacing:-.01em; margin:4mm 0 8mm; }
.lead{ font-size:11pt; font-weight:300; line-height:1.7; color:var(--mut); margin:-4mm 0 9mm; max-width:200mm; }

/* CAPA */
.cover-hd{ position:absolute; top:0; left:0; right:0; height:26mm; background:var(--ink);
  display:flex; align-items:center; justify-content:space-between; padding:0 22mm; z-index:3; }
.cover-hd .logo{ font-size:16pt; font-weight:800; letter-spacing:.08em; color:var(--gold); }
.cover-hd .tag{ font-size:8pt; letter-spacing:.24em; text-transform:uppercase; color:rgba(255,255,255,.4); }
.cover-bar{ position:absolute; top:26mm; left:0; right:0; height:2.6mm; background:var(--gold); z-index:3; }
.cover-photo{ position:absolute; inset:0; background:url('%(capa)s') center/cover no-repeat; }
.cover-scrim{ position:absolute; inset:0;
  background:linear-gradient(to bottom, rgba(0,0,0,.35) 0%%, transparent 30%%, rgba(0,0,0,.78) 78%%); z-index:2; }
.cover-cnt{ position:absolute; left:22mm; right:22mm; bottom:34mm; z-index:3; color:#fff; }
.cover-kicker{ font-size:9pt; letter-spacing:.2em; text-transform:uppercase; color:rgba(255,255,255,.55); }
.cover-basis{ font-size:10pt; color:rgba(255,255,255,.6); margin:2mm 0 9mm; }
.cover-to{ font-size:9pt; letter-spacing:.18em; text-transform:uppercase; color:rgba(255,255,255,.5); }
.cover-name{ font-size:34pt; font-weight:800; letter-spacing:.02em; text-transform:uppercase; line-height:1.1; margin-top:1mm; }
.cover-dest{ font-size:18pt; font-weight:600; color:var(--gold); margin-top:2mm; letter-spacing:.04em; }
.cover-tagline{ font-size:10.5pt; font-weight:300; color:rgba(255,255,255,.72); margin-top:4mm; max-width:180mm; line-height:1.6; }
.stats{ display:flex; gap:14mm; margin-top:11mm; }
.stat b{ display:block; font-size:26pt; font-weight:800; color:var(--gold); line-height:1; }
.stat span{ font-size:8.5pt; color:rgba(255,255,255,.6); letter-spacing:.06em; }
.cover-sig{ position:absolute; left:22mm; right:22mm; bottom:16mm; z-index:3;
  font-family:var(--con); font-size:9pt; color:rgba(255,255,255,.55); line-height:1.7; }

/* ITINERÁRIO */
.tl{ display:flex; flex-direction:column; }
.tl-item{ display:flex; align-items:flex-start; gap:6mm; }
.tl-badge{ width:11mm; height:11mm; border-radius:50%%; background:var(--dest); color:#fff;
  font-weight:800; font-size:13pt; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.tl-line{ width:2px; height:14mm; background:var(--line); margin-left:5.4mm; }
.tl-city{ font-size:14pt; font-weight:700; color:var(--ink); }
.tl-meta{ font-size:10pt; color:var(--mut); margin-top:1mm; }
.tl-note{ font-size:10pt; font-weight:300; color:var(--char); margin-top:2mm; max-width:170mm; line-height:1.6; }

.info-grid{ display:grid; grid-template-columns:1fr 1fr; gap:8mm 14mm; margin-top:14mm;
  border-top:1px solid var(--line); padding-top:9mm; }
.info-k{ font-size:8pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.info-v{ font-size:10.5pt; font-weight:300; line-height:1.65; color:var(--char); margin-top:1.5mm; }
.closing{ margin-top:12mm; border-left:3px solid var(--gold); padding:3mm 0 3mm 7mm;
  font-size:10.5pt; font-weight:300; line-height:1.8; color:var(--mut); }
.incl{ margin-top:11mm; border-top:1px solid var(--line); padding-top:8mm; }
.incl-h{ font-size:8pt; letter-spacing:.14em; text-transform:uppercase; color:var(--gold); font-weight:700; margin-bottom:4mm; }
.incl li{ list-style:none; font-size:10.5pt; font-weight:300; line-height:1.55; color:var(--char);
  padding-left:8mm; position:relative; margin-bottom:3.4mm; }
.incl li::before{ content:'—'; position:absolute; left:0; color:var(--gold); font-weight:700; }

/* DESTINO + HOTEL */
.dest-hd{ background:var(--dest); padding:5mm 22mm; display:flex; align-items:center;
  justify-content:space-between; flex-shrink:0; }
.dest-hd .city{ font-size:12pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:rgba(255,255,255,.85); }
.dest-hd .no{ width:12mm; height:12mm; border-radius:50%%; border:2px solid rgba(218,141,0,.9);
  color:var(--gold); font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; }
.dest-photo{ height:120mm; background:#33402e center/cover no-repeat; position:relative; flex-shrink:0; }
.dest-photo .cap{ position:absolute; bottom:6mm; left:22mm; font-size:13pt; font-weight:800;
  letter-spacing:.08em; text-transform:uppercase; color:#fff; text-shadow:0 1px 8px rgba(0,0,0,.6); }
.dest-text{ font-size:12pt; font-weight:400; line-height:1.7; color:var(--char); }
.hotel-card{ margin-top:10mm; border:1px solid var(--line); border-radius:6px; overflow:hidden; }
.hotel-card .top{ background:#faf7f2; padding:6mm 8mm; border-bottom:1px solid var(--line); }
.hotel-card .name{ font-size:15pt; font-weight:700; color:var(--ink); }
.hotel-card .stars{ font-size:14pt; color:var(--gold); letter-spacing:2px; margin-top:1mm; }
.hotel-card .rows{ padding:6mm 8mm; display:grid; grid-template-columns:1fr 1fr; gap:4mm 10mm; }
.hotel-card .k{ font-size:8pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut); font-weight:700; }
.hotel-card .v{ font-size:11pt; font-weight:300; color:var(--char); margin-top:1mm; }

/* ROTEIRO */
.day{ margin-bottom:7mm; }
.day-h{ font-size:11pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--gold); }
.day-t{ font-size:11pt; line-height:1.7; color:var(--char); margin-top:2mm; }

/* SERVIÇOS */
.svc{ margin-bottom:9mm; }
.svc-h{ font-size:11pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--gold); margin-bottom:2mm; }
.svc-row{ display:flex; justify-content:space-between; align-items:baseline; gap:10mm;
          padding:2.8mm 0; border-bottom:1px solid var(--line); }
.svc-row .n{ font-size:11pt; color:var(--char); }
.svc-row .m{ font-size:9.5pt; font-weight:300; color:var(--mut); white-space:nowrap; }
.svc-note{ font-size:9.5pt; font-weight:300; color:var(--mut); line-height:1.7; margin-top:3mm; }

/* VALORES */
.val-note{ font-size:9pt; color:var(--mut); margin-bottom:5mm; }
.val-row{ display:flex; justify-content:space-between; padding:4mm 0; border-bottom:1px solid var(--line); }
.val-row .lbl{ font-size:12pt; color:var(--char); }
.val-row .amt{ font-size:12pt; font-weight:700; color:var(--ink); font-variant-numeric:tabular-nums; }
.val-row .amt.tbd{ font-weight:300; color:var(--mut); font-style:italic; }
.val-total{ display:flex; justify-content:space-between; align-items:center; background:var(--ink);
  border-radius:5px; padding:6mm 8mm; margin-top:6mm; }
.val-total .lbl{ font-size:11pt; font-weight:700; letter-spacing:.08em; color:rgba(255,255,255,.7); }
.val-total .amt{ font-size:16pt; font-weight:800; color:var(--gold); }
.val-fx{ font-size:9pt; color:var(--mut); margin-top:5mm; line-height:1.6; }

/* CONDIÇÕES */
.cond{ margin-bottom:7mm; }
.cond-h{ font-size:11pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--gold); margin-bottom:2mm; }
.cond-t{ font-size:11pt; line-height:1.8; color:var(--char); }
""" % dict(fonts=FONTS, gold=GOLD, dest=DEST, capa=SCENES["capa"])

FT = ('<div class="ft"><a href="mailto:%s">%s</a><span class="sep">·</span>'
      '<a href="%s">%s</a></div>' % (MAIL, MAIL, WA_L, WA_T))

def hd(tag):
    return ('<div class="hd"><div class="logo">LUSA TRAVEL</div><div class="tag">%s</div></div>'
            '<div class="goldbar"></div>' % tag)

def page_capa(v):
    return f"""<section class="page cover">
  <div class="cover-hd"><div class="logo">LUSA TRAVEL</div><div class="tag">Glossário</div></div>
  <div class="cover-bar"></div><div class="cover-photo"></div><div class="cover-scrim"></div>
  <div class="cover-cnt">
    <div class="cover-kicker">Cotação para sua viagem</div>
    <div class="cover-basis">Baseado em {C.PAX} · {v['periodo']}</div>
    <div class="cover-to">{C.CLIENTE_LABEL}</div>
    <div class="cover-name">{C.CLIENTE}</div>
    <div class="cover-dest">{C.DESTINO}</div>
    <div class="cover-tagline">{v['tagline']}</div>
    <div class="stats">
      <div class="stat"><b>2</b><span>Destinos</span></div>
      <div class="stat"><b>{v['noites']}</b><span>Noites</span></div>
      <div class="stat"><b>2</b><span>Hotéis</span></div>
      <div class="stat"><b>1</b><span>Seguro</span></div>
    </div>
  </div>
  <div class="cover-sig">
    <a href="mailto:{MAIL}" style="color:inherit;text-decoration:none">{MAIL}</a><br>
    <a href="{WA_L}" style="color:inherit;text-decoration:none">{WA_T}</a><br>
    <span style="opacity:.7">{ADDR}</span>
  </div>
</section>"""

def page_itinerario(v):
    a, b = v["etapas"]
    info = "".join(f'<div><div class="info-k">{k}</div><div class="info-v">{t(x)}</div></div>'
                   for k, x in v["info"])
    return f"""<section class="page">{hd('Itinerário')}
  <div class="body">
    <div class="eyebrow">Sua rota</div><h2 class="h2">Itinerário</h2>
    <p class="lead">{t(v['rota_lead'])}</p>
    <div class="tl">
      <div class="tl-item"><div class="tl-badge">1</div><div>
        <div class="tl-city">PANTANAL SUL · MIRANDA – MS</div>
        <div class="tl-meta">{a['datas']} · {a['noites']} noites</div>
        <div class="tl-note">{t(a['nota'])}</div></div></div>
      <div class="tl-line"></div>
      <div class="tl-item"><div class="tl-badge">2</div><div>
        <div class="tl-city">BONITO · SERRA DA BODOQUENA – MS</div>
        <div class="tl-meta">{b['datas']} · {b['noites']} noites</div>
        <div class="tl-note">{t(b['nota'])}</div></div></div>
    </div>
    <div class="info-grid">{info}</div>
  </div>{FT}</section>"""

def page_roteiro(dias, closing):
    ds = "".join(f'<div class="day"><div class="day-h">{n} | {cid} | {dt}</div>'
                 f'<div class="day-t">{t(tx)}</div></div>' for n, cid, dt, tx in dias)
    return f"""<section class="page">{hd('Roteiro')}
  <div class="body"><div class="eyebrow">Dia a dia</div><h2 class="h2">Roteiro</h2>{ds}
    <div class="closing">{t(closing)}</div></div>{FT}</section>"""

def page_destino(no, cidade, img, texto, hotel, ci, co):
    return f"""<section class="page">
  <div class="dest-hd"><div class="city">{cidade}</div><div class="no">{no}</div></div>
  <div class="goldbar"></div>
  <div class="dest-photo" style="background-image:url('{img}')"><div class="cap">{cidade.split(' · ')[0]}</div></div>
  <div class="body">
    <p class="dest-text">{t(texto)}</p>
    <div class="hotel-card">
      <div class="top"><div class="name">{hotel['nome']}</div><div class="stars">{hotel['stars']}</div></div>
      <div class="rows">
        <div><div class="k">Quarto</div><div class="v">{hotel['quarto']}</div></div>
        <div><div class="k">Plano</div><div class="v">{hotel['plano']}</div></div>
        <div><div class="k">Endereço</div><div class="v">{hotel['endereco']}</div></div>
        <div><div class="k">Check-in / out</div><div class="v">{ci} → {co}</div></div>
      </div>
    </div>
  </div>{FT}</section>"""

def _rows(items):
    return "".join(f'<div class="svc-row"><span class="n">{n}</span><span class="m">{m}</span></div>'
                   for n, m in items)

def page_servicos(completa):
    tr, inc, pas = C.servicos(completa)
    return f"""<section class="page">{hd('Serviços')}
  <div class="body">
    <div class="eyebrow">O que está incluído</div><h2 class="h2">Serviços Adicionais</h2>
    <div class="svc"><div class="svc-h">Seguro de viagem</div>
      {_rows([C.SEGURO])}</div>
    <div class="svc"><div class="svc-h">Traslados privativos</div>{_rows(tr)}</div>
    <div class="svc"><div class="svc-h">Experiências inclusas no Pantanal</div>{_rows(inc)}
      <div class="svc-note">Todas as atividades do lodge são conduzidas por guias bilíngues e já estão
      contempladas no regime all-inclusive, sem cobrança à parte.</div></div>
    <div class="svc"><div class="svc-h">Passeios em Bonito</div>{_rows(pas)}
      <div class="svc-note">Os atrativos de Bonito operam por voucher com vaga e horário marcados.
      Durações são estimadas e não incluem o tempo de deslocamento entre a cidade e a atração.</div></div>
  </div>{FT}</section>"""

def page_valores(v):
    linhas = [("Hotelaria", "Sob consulta"), ("Aéreo Nacional", "Sob consulta"),
              ("Seguro de Viagem", "Sob consulta"), ("Traslados e Passeios", "Sob consulta")]
    rs = "".join(f'<div class="val-row"><span class="lbl">{l}</span>'
                 f'<span class="amt tbd">{a}</span></div>' for l, a in linhas)
    itens = "".join(f'<li>{t(i)}</li>' for i in v["contempla"])
    return f"""<section class="page">{hd('Valores')}
  <div class="body">
    <div class="eyebrow">Investimento</div><h2 class="h2">Valores</h2>
    <div class="val-note">*Valores em BRL para {C.PAX} — {v['periodo']}</div>
    {rs}
    <div class="val-total"><span class="lbl">TOTAL / FAMÍLIA</span><span class="amt">Sob consulta</span></div>
    <div class="incl"><div class="incl-h">Esta cotação contempla</div><ul>{itens}</ul></div>
    <div class="val-fx">Cotação de referência 25/08/2026 · Valores em BRL (viagem nacional, sem conversão cambial).<br>
      Os fornecedores ainda não publicaram tarifário para março de 2027; os valores serão preenchidos na
      cotação formal, com validade e câmbio datados.<br>
      <strong>*Nada reservado, apenas cotado</strong></div>
  </div>{FT}</section>"""

def page_condicoes():
    cs = "".join(f'<div class="cond"><div class="cond-h">{h}</div><div class="cond-t">{x}</div></div>'
                 for h, x in C.CONDICOES)
    return f"""<section class="page">{hd('Condições')}
  <div class="body"><div class="eyebrow">Importante</div>
    <h2 class="h2">Condições e Observações</h2>{cs}</div>{FT}</section>"""

DIAG = """<script>
window.addEventListener('load',function(){
 var r=[],ps=document.querySelectorAll('.page');
 ps.forEach(function(p,i){
   var over=p.scrollHeight-p.clientHeight, b=p.querySelector('.body'), bo=b?b.scrollHeight-b.clientHeight:0;
   r.push('P'+(i+1)+':page='+over+',body='+bo+(over>1||bo>1?' <<OVERFLOW>>':''));
 });
 var d=document.createElement('div'); d.id='__diag'; d.textContent='PAGES='+ps.length+' | '+r.join(' | ');
 document.body.appendChild(d);
});</script>"""

def doc(v, diag=False):
    pages = [
        page_capa(v),
        page_itinerario(v),
        page_roteiro(v["dias"], v["closing"]),
        page_destino(1, "PANTANAL SUL · MIRANDA – MS", SCENES["pantanal"], C.TXT_PANTANAL,
                     C.HOTEL_PANTANAL, v["ci1"], v["co1"]),
        page_destino(2, "BONITO · SERRA DA BODOQUENA – MS", SCENES["bonito"], C.TXT_BONITO,
                     C.HOTEL_BONITO, v["ci2"], v["co2"]),
        page_servicos(v["completa"]),
        page_valores(v),
        page_condicoes(),
    ]
    sheet = ("<style>@media screen{body{display:flex;flex-wrap:wrap;gap:8px;background:#6b6b6b;padding:8px}"
             ".page{zoom:.30;box-shadow:0 0 0 3px #111}}</style>") if diag == "sheet" else ""
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<title>{C.CLIENTE_LABEL[:-1]} {C.CLIENTE.title()} | Pantanal e Bonito — Lusa Travel</title>'
            f'<style>{CSS}</style>{sheet}</head><body>' + "".join(pages)
            + (DIAG if diag == "diag" else "") + "</body></html>")


# ── Blocos complementares ─────────────────────────────────────────────────────
INFO_COMPLETA = [
   ('Aéreo sugerido',
    'Chegada em Campo Grande (CGR) e retorno por Bonito (BYO), cotado à parte e sujeito à abertura de venda das companhias para março de 2027.'),
   ('Deslocamento interno',
    '≈ 5h30 de estrada no total, em traslado privativo. Sair por Bonito evita as 4h de retorno a Campo Grande.'),
   ('Ritmo',
    'Três dias de campo no Pantanal e três de água em Bonito, com uma tarde inteiramente livre no resort para descanso.'),
   ('Perfil do roteiro',
    'Desenhado para crianças de 7 a 12 anos: deslocamentos curtos, atividades de meio período e fauna visível em todas as saídas.'),
   ('Clima previsto',
    'Fim da estação chuvosa: 24 °C a 33 °C, umidade alta e pancadas de chuva no fim da tarde. Nenhuma atividade do roteiro depende de tempo firme o dia inteiro.'),
   ('Documentação',
    'Viagem nacional: RG ou certidão de nascimento para os menores, acompanhados dos pais. Sem exigência de passaporte ou visto.'),
]
INFO_COMPACTA = [
   ('Aéreo sugerido',
    'Chegada em Campo Grande (CGR) e retorno por Bonito (BYO), cotado à parte e sujeito à abertura de venda das companhias para março de 2027.'),
   ('Deslocamento interno',
    '≈ 5h30 de estrada no total, em traslado privativo. Se o voo de Bonito não encaixar, o retorno por Campo Grande acrescenta ≈ 3h30.'),
   ('Ritmo',
    'Dois dias de campo e dois de água, sem tarde ociosa. Roteiro cheio, indicado para famílias que já viajam bem com crianças.'),
   ('Perfil do roteiro',
    'Desenhado para crianças de 7 a 12 anos: deslocamentos curtos, atividades de meio período e fauna visível em todas as saídas.'),
   ('Clima previsto',
    'Fim da estação chuvosa: 24 °C a 33 °C, umidade alta e pancadas de chuva no fim da tarde. Nenhuma atividade do roteiro depende de tempo firme o dia inteiro.'),
   ('Documentação',
    'Viagem nacional: RG ou certidão de nascimento para os menores, acompanhados dos pais. Sem exigência de passaporte ou visto.'),
]
CLOSE_COMPLETA = 'A ordem dos passeios pode ser ajustada no destino conforme o nível dos rios e a previsão de chuva. Em março, convém manter um dia de folga entre a flutuação e o retorno para permitir remarcação — este roteiro já foi montado assim.'
CLOSE_COMPACTA = 'A ordem dos passeios pode ser ajustada no destino conforme o nível dos rios. Esta versão não tem folga entre a flutuação e o retorno: em caso de chuva forte no sábado, a flutuação no Rio da Prata é remanejada para a manhã de segunda, trocando de lugar com as cachoeiras.'
CONTEMPLA_COMPLETA = ['6 noites de hospedagem nos hotéis indicados, com os planos de refeição descritos', 'Todas as atividades guiadas do Refúgio Ecológico Caiman, em regime all-inclusive', 'Traslados privativos entre aeroporto, Pantanal e Bonito', 'Vouchers dos passeios de Bonito listados na página de Serviços Adicionais', 'Seguro de viagem para os quatro passageiros', 'Acompanhamento da Lusa Travel antes e durante a viagem']
CONTEMPLA_COMPACTA = ['4 noites de hospedagem nos hotéis indicados, com os planos de refeição descritos', 'Todas as atividades guiadas do Refúgio Ecológico Caiman, em regime all-inclusive', 'Traslados privativos entre aeroporto, Pantanal e Bonito', 'Vouchers dos passeios de Bonito listados na página de Serviços Adicionais', 'Seguro de viagem para os quatro passageiros', 'Acompanhamento da Lusa Travel antes e durante a viagem']

VERSOES = {
 "completa": dict(
   completa=True, noites=6, periodo="24 a 30 de março de 2027",
   tagline="Sete dias entre o Pantanal na cheia e as águas cristalinas da Serra da Bodoquena — "
           "roteiro desenhado para dois meninos de 9 e 10 anos.",
   rota_lead="Chegada por Campo Grande e saída por Bonito, evitando quatro horas de estrada no retorno. "
             "Todos os deslocamentos internos em traslado privativo.",
   etapas=[dict(datas="24 a 27 mar", noites=3,
                nota="Refúgio Ecológico Caiman · Cordilheira Lodge — regime all-inclusive com safáris, "
                     "focagem noturna, cavalgada, barco e pescaria de piranha."),
           dict(datas="27 a 30 mar", noites=3,
                nota="Zagaia Eco Resort — base para flutuação no Rio da Prata, Buraco das Araras e um dia "
                     "inteiro de cachoeiras, com piscinas e recreação no hotel.")],
   ci1="24/03/2027", co1="27/03/2027", ci2="27/03/2027", co2="30/03/2027",
   info=INFO_COMPLETA, closing=CLOSE_COMPLETA, contempla=CONTEMPLA_COMPLETA,
   dias=C.DIAS_COMPLETA),
 "compacta": dict(
   completa=False, noites=4, periodo="25 a 29 de março de 2027",
   tagline="Cinco dias aproveitando o feriado da Semana Santa — o essencial do Pantanal e de Bonito, "
           "sem dias de aula além do feriado.",
   rota_lead="Versão enxuta para quem não quer estender além do feriado: mesma sequência da viagem "
             "completa, com uma noite a menos em cada base e traslados privativos entre elas.",
   etapas=[dict(datas="25 a 27 mar", noites=2,
                nota="Refúgio Ecológico Caiman · Cordilheira Lodge — all-inclusive, com safári, focagem "
                     "noturna, pescaria de piranha e cavalgada concentrados em dois dias cheios."),
           dict(datas="27 a 29 mar", noites=2,
                nota="Zagaia Eco Resort — flutuação no Rio da Prata no Domingo de Páscoa e circuito curto "
                     "de cachoeiras na manhã do retorno.")],
   ci1="25/03/2027", co1="27/03/2027", ci2="27/03/2027", co2="29/03/2027",
   info=INFO_COMPACTA, closing=CLOSE_COMPACTA, contempla=CONTEMPLA_COMPACTA,
   dias=C.DIAS_COMPACTA),
}

if __name__ == "__main__":
    for k, v in VERSOES.items():
        for mode, suf in ((False, ""), ("diag", ".diag"), ("sheet", ".sheet")):
            fn = f"proposta-{k}{suf}.html"
            io.open(fn, "w", encoding="utf-8").write(doc(v, mode))
        print(f"  proposta-{k}.html  ({v['noites']} noites, {len(v['dias'])} dias)")
