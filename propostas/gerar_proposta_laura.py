#!/usr/bin/env python3
"""Gera proposta-laura-dalcanale-toquio.html a partir dos dados abaixo.
Uso: python3 gerar_proposta_laura.py && chromium --headless --print-to-pdf=... """
import base64, pathlib

HERE = pathlib.Path(__file__).parent
LOGO = base64.b64encode((HERE/'assets/lusatravel-logo-dourado.png').read_bytes()).decode()
LOGO_DARK = base64.b64encode((HERE/'assets/lusatravel-logo-original.png').read_bytes()).decode()

CLIENTE = 'Sra. Laura Dalcanale'
COTACAO = '15/10/2026'
CAMBIO = 'USD 1 = R$ 5,04'

# ── helpers de linhas ───────────────────────────────────────────
def R(voo, leg, sub, d1, t1, d2, t2, dur, ac):
    return dict(k='r', voo=voo, leg=leg, sub=sub, d1=d1, t1=t1, d2=d2, t2=t2, dur=dur, ac=ac)
def C(txt): return dict(k='c', txt=txt)
def D(txt): return dict(k='d', txt=txt)
def S(txt): return dict(k='s', txt=txt)
def P(cab, brl, usd, bag): return dict(cab=cab, brl=brl, usd=usd, bag=bag)

# ── dados ───────────────────────────────────────────────────────
CARDS = [
 dict(id='aa-eco', air='American Airlines', sub='Ida via Dallas · volta via Nova York', gold=False,
  prices=[P('Econômica','R$ 37.443,44','USD 7.423,20','1 mala')],
  rows=[D('Ida · 29 dez → 31 dez · tempo total 31h50'),
   R('AA 962','GRU → DFW','São Paulo → Dallas','29 dez','22:35','30 dez','05:55','10h20','Boeing 787-9'),
   C('Conexão em Dallas · <b>7h45</b>'),
   R('AA 175','DFW → HND','Dallas → Tóquio Haneda','30 dez','13:40','31 dez','18:25','13h45','Boeing 777-200'),
   D('Volta · 29 jan → 30 jan · tempo total 24h55'),
   R('AA 168','HND → JFK','Tóquio Haneda → Nova York','29 jan','17:10','29 jan','16:15','13h05','Boeing 787-9'),
   C('Conexão em Nova York · <b>2h20</b>'),
   R('AA 951','JFK → GRU','Nova York → São Paulo','29 jan','18:35','30 jan','06:05','09h30','Boeing 787-9')],
  ft=['<b>Chegada e retorno</b> por Haneda (mais próximo do centro)','<b>Permanência:</b> 29 noites no Japão']),

 dict(id='aa-exec', air='American Airlines', sub='Via Nova York', gold=False,
  prices=[P('Executiva','R$ 43.902,86','USD 8.703,80','2 malas')],
  rows=[D('Ida · 28 dez → 30 dez · tempo total 27h35'),
   R('AA 950','GRU → JFK','São Paulo → Nova York','28 dez','23:00','29 dez','06:50','09h50','Boeing 787-9'),
   C('Conexão em Nova York · <b>3h10</b>'),
   R('AA 167','JFK → HND','Nova York → Tóquio Haneda','29 dez','10:00','30 dez','14:35','14h35','Boeing 787-9'),
   D('Volta · 26 jan → 27 jan · tempo total 31h00'),
   R('AA 8403','HND → JFK','Tóquio Haneda → Nova York · código compartilhado','26 jan','11:05','26 jan','10:00','12h55','Airbus A350-1000'),
   C('Conexão em Nova York · <b>8h35</b> (conexão longa)'),
   R('AA 951','JFK → GRU','Nova York → São Paulo','26 jan','18:35','27 jan','06:05','09h30','Boeing 787-9')],
  ft=['<b>Chegada e retorno</b> por Haneda (mais próximo do centro)','<b>Permanência:</b> 27 noites no Japão']),

 dict(id='ac', air='Air Canada', sub='Ida via Toronto · volta via Montreal', gold=False,
  prices=[P('Econômica','R$ 61.799,48','USD 12.251,84','1 mala'), P('Executiva','R$ 37.060,20','USD 7.347,24','2 malas')],
  rows=[D('Ida · 27 dez → 29 dez · tempo total 31h10'),
   R('AC 91','GRU → YYZ','São Paulo → Toronto','27 dez','21:30','28 dez','05:50','10h20','Boeing 787-9'),
   C('Conexão em Toronto · <b>6h50</b>'),
   R('AC 1','YYZ → HND','Toronto → Tóquio Haneda','28 dez','12:40','29 dez','16:40','14h00','Boeing 777-300ER'),
   D('Volta · 26 jan → 27 jan · tempo total 26h15'),
   R('AC 6','NRT → YUL','Tóquio Narita → Montreal','26 jan','18:45','26 jan','17:00','12h15','Boeing 777-300ER'),
   C('Conexão em Montreal · <b>3h55</b>'),
   R('AC 96','YUL → GRU','Montreal → São Paulo','26 jan','20:55','27 jan','09:00','10h05','Boeing 787-9')],
  ft=['<b>Chegada</b> por Haneda · <b>retorno</b> por Narita','<b>Permanência:</b> 28 noites no Japão']),

 dict(id='am-27', air='Aeroméxico', sub='Via Cidade do México · saída 27 dez', gold=False,
  prices=[P('Econômica Premium','R$ 54.714,92','USD 10.847,32','2 malas'), P('Executiva','R$ 53.262,11','USD 10.559,29','2 malas')],
  rows=[D('Ida · 27 dez → 29 dez · tempo total 30h30'),
   R('AM 15','GRU → MEX','São Paulo → Cidade do México','27 dez','12:00','27 dez','18:35','09h35','Boeing 787-9'),
   C('Conexão na Cidade do México · <b>3h10</b>'),
   R('AM 58','MEX → NRT','Cidade do México → Tóquio Narita · 1 escala intermediária','27 dez','21:45','29 dez','06:30','17h45','Boeing 787-8'),
   D('Volta · 25 jan → 26 jan · tempo total 36h20'),
   R('AM 57','NRT → MEX','Tóquio Narita → Cidade do México','25 jan','09:35','25 jan','07:30','12h55','Boeing 787-8'),
   C('Conexão na Cidade do México · <b>13h25</b> (conexão longa)'),
   R('AM 14','MEX → GRU','Cidade do México → São Paulo','25 jan','20:55','26 jan','09:55','10h00','Boeing 787-9')],
  ft=['<b>Chegada e retorno</b> por Narita','<b>Permanência:</b> 27 noites no Japão']),

 dict(id='am-28', air='Aeroméxico', sub='Via Cidade do México · saída 28 dez', gold=False,
  prices=[P('Econômica','R$ 51.001,68','USD 10.111,16','2 malas'), P('Executiva','R$ 39.331,97','USD 7.797,62','2 malas')],
  rows=[D('Ida · 28 dez → 30 dez · tempo total 30h30'),
   R('AM 15','GRU → MEX','São Paulo → Cidade do México','28 dez','12:00','28 dez','18:35','09h35','Boeing 787-9'),
   C('Conexão na Cidade do México · <b>3h10</b>'),
   R('AM 58','MEX → NRT','Cidade do México → Tóquio Narita · 1 escala intermediária','28 dez','21:45','30 dez','06:30','17h45','Boeing 787-8'),
   D('Volta · 26 jan → 27 jan · tempo total 36h20'),
   R('AM 57','NRT → MEX','Tóquio Narita → Cidade do México','26 jan','09:35','26 jan','07:30','12h55','Boeing 787-9'),
   C('Conexão na Cidade do México · <b>13h25</b> (conexão longa)'),
   R('AM 14','MEX → GRU','Cidade do México → São Paulo','26 jan','20:55','27 jan','09:55','10h00','Boeing 787-9')],
  ft=['<b>Chegada e retorno</b> por Narita','<b>Permanência:</b> 27 noites no Japão']),

 dict(id='ita', air='ITA Airways', sub='Via Roma · Airbus A350 em todos os trechos', gold=False,
  prices=[P('Econômica','R$ 55.858,36','USD 11.074,00','2 malas'), P('Executiva','R$ 41.767,67','USD 8.280,50','2 malas')],
  rows=[D('Ida · 28 dez → 30 dez · tempo total 26h40'),
   R('AZ 679','GRU → FCO','São Paulo → Roma','28 dez','20:40','29 dez','11:35','10h55','Airbus A350'),
   C('Conexão em Roma · <b>3h30</b>'),
   R('AZ 792','FCO → HND','Roma → Tóquio Haneda','29 dez','15:05','30 dez','11:20','12h15','Airbus A350'),
   D('Volta · 28 jan → 29 jan · tempo total 41h20'),
   R('AZ 793','HND → FCO','Tóquio Haneda → Roma','28 jan','13:20','28 jan','20:25','15h05','Airbus A350'),
   C('Conexão em Roma · <b>14h10</b> (pernoite em trânsito)'),
   R('AZ 678','FCO → GRU','Roma → São Paulo','29 jan','10:35','29 jan','18:40','12h05','Airbus A350')],
  ft=['<b>Chegada e retorno</b> por Haneda (mais próximo do centro)','<b>Permanência:</b> 29 noites no Japão']),

 dict(id='lh', air='Lufthansa + Swiss', sub='Ida via Frankfurt · volta via Zurique', gold=False,
  prices=[P('Executiva','R$ 41.903,34','USD 8.307,40','2 malas')],
  rows=[D('Ida · 28 dez → 30 dez · tempo total 28h00'),
   R('LH 507','GRU → FRA','São Paulo → Frankfurt','28 dez','18:45','29 dez','10:15','11h30','Boeing 747-8'),
   C('Conexão em Frankfurt · <b>3h45</b>'),
   R('LH 716','FRA → HND','Frankfurt → Tóquio Haneda','29 dez','14:00','30 dez','10:45','12h45','Boeing 747-8'),
   D('Volta · 28 jan → 29 jan · tempo total 30h30'),
   R('LX 161','NRT → ZRH','Tóquio Narita → Zurique','28 jan','12:10','28 jan','18:40','14h30','Boeing 777-300ER'),
   C('Conexão em Zurique · <b>3h55</b>'),
   R('LX 92','ZRH → GRU','Zurique → São Paulo','28 jan','22:35','29 jan','06:40','12h05','Boeing 777-300ER')],
  ft=['<b>Chegada</b> por Haneda · <b>retorno</b> por Narita','<b>Permanência:</b> 29 noites no Japão']),
]

TURKISH = [
 dict(id='tk-1', air='Turkish Airlines', sub='Volta de Narita pela manhã · dois horários de saída de São Paulo, mesma tarifa', gold=True,
  prices=[P('Econômica','R$ 61.806,96','USD 12.253,32','1 mala')],
  rows=[D('Ida · 26 dez → 30 dez · escolha um dos dois voos de saída'),
   R('TK 16<i>Opção A</i>','GRU → IST','São Paulo → Istambul · saída de madrugada','26 dez','04:10','26 dez','22:35','12h25','Airbus A350'),
   R('TK 216<i>Opção B</i>','GRU → IST','São Paulo → Istambul · saída à tarde','26 dez','17:10','27 dez','11:45','12h35','Airbus A350'),
   S('✦ <b>Stopover em Istambul</b> · <b>3 noites</b> com a Opção A (26, 27 e 28 dez) ou <b>2 noites</b> com a Opção B (27 e 28 dez) · hospedagem não inclusa'),
   R('TK 50','IST → NRT','Istambul → Tóquio Narita','29 dez','15:25','30 dez','08:40','11h15','Boeing 787-9'),
   D('Volta · 26 jan → 27 jan · tempo total 30h10'),
   R('TK 51','NRT → IST','Tóquio Narita → Istambul','26 jan','10:10','26 jan','18:00','13h50','Boeing 787-9'),
   C('Conexão em Istambul · <b>2h35</b>'),
   R('TK 215','IST → GRU','Istambul → São Paulo','26 jan','20:35','27 jan','04:20','13h45','Airbus A350')],
  ft=['<b>Chegada e retorno</b> por Narita','<b>Permanência:</b> 2 ou 3 noites em Istambul + 27 noites no Japão']),

 dict(id='tk-2', air='Turkish Airlines', sub='Volta de Haneda à noite · 2 noites em Istambul', gold=True,
  prices=[P('Econômica','R$ 69.509,16','USD 13.780,28','1 mala'), P('Executiva','R$ 79.967,15','USD 15.853,60','2 malas')],
  rows=[D('Ida · 26 dez → 30 dez'),
   R('TK 216','GRU → IST','São Paulo → Istambul','26 dez','17:10','27 dez','11:45','12h35','Airbus A350'),
   S('✦ <b>Stopover em Istambul · 2 noites</b> (27 e 28 dez) · hospedagem não inclusa'),
   R('TK 50','IST → NRT','Istambul → Tóquio Narita','29 dez','15:25','30 dez','08:40','11h15','Boeing 787-9'),
   D('Volta · 26 jan → 27 jan · tempo total 31h40'),
   R('TK 199','HND → IST','Tóquio Haneda → Istambul','26 jan','22:05','27 jan','05:45','13h40','Boeing 777-300ER'),
   C('Conexão em Istambul · <b>4h10</b>'),
   R('TK 15','IST → GRU','Istambul → São Paulo','27 jan','09:55','27 jan','17:45','13h50','Airbus A350')],
  ft=['<b>Chegada</b> por Narita · <b>retorno</b> por Haneda','<b>Permanência:</b> 2 noites em Istambul + 27 noites no Japão']),
]

# resumo: (companhia, rota, cabine, ida, volta, bag, brl, usd, destaque)
SUMMARY = [
 ('American Airlines','via Dallas / Nova York','Econômica','29 dez','29 jan','1 mala','R$ 37.443,44','USD 7.423,20',False),
 ('American Airlines','via Nova York','Executiva','28 dez','26 jan','2 malas','R$ 43.902,86','USD 8.703,80',False),
 ('Air Canada','via Toronto / Montreal','Econômica','27 dez','26 jan','1 mala','R$ 61.799,48','USD 12.251,84',False),
 ('Air Canada','via Toronto / Montreal','Executiva','27 dez','26 jan','2 malas','R$ 37.060,20','USD 7.347,24',False),
 ('Aeroméxico','via Cidade do México','Econômica Premium','27 dez','25 jan','2 malas','R$ 54.714,92','USD 10.847,32',False),
 ('Aeroméxico','via Cidade do México','Executiva','27 dez','25 jan','2 malas','R$ 53.262,11','USD 10.559,29',False),
 ('Aeroméxico','via Cidade do México','Econômica','28 dez','26 jan','2 malas','R$ 51.001,68','USD 10.111,16',False),
 ('Aeroméxico','via Cidade do México','Executiva','28 dez','26 jan','2 malas','R$ 39.331,97','USD 7.797,62',False),
 ('ITA Airways','via Roma','Econômica','28 dez','28 jan','2 malas','R$ 55.858,36','USD 11.074,00',False),
 ('ITA Airways','via Roma','Executiva','28 dez','28 jan','2 malas','R$ 41.767,67','USD 8.280,50',False),
 ('Lufthansa + Swiss','via Frankfurt / Zurique','Executiva','28 dez','28 jan','2 malas','R$ 41.903,34','USD 8.307,40',False),
 ('Turkish Airlines','stopover Istambul · volta Narita (TK 51/215)','Econômica','26 dez','26 jan','1 mala','R$ 61.806,96','USD 12.253,32',True),
 ('Turkish Airlines','stopover Istambul · volta Haneda (TK 199/15)','Econômica','26 dez','26 jan','1 mala','R$ 69.509,16','USD 13.780,28',True),
 ('Turkish Airlines','stopover Istambul · volta Haneda (TK 199/15)','Executiva','26 dez','26 jan','2 malas','R$ 79.967,15','USD 15.853,60',True),
]

# ── render ──────────────────────────────────────────────────────
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Montserrat:wght@400;500;600&display=swap');
:root{ --gold:#da8d00; --green:#414625; --green-soft:#eef0e6; --gold-soft:#fbf3e3;
  --ink:#1a1510; --char:#333131; --mut:#8a8178; --line:#e2ddd3;
  --sans:'Poppins',system-ui,-apple-system,'Segoe UI',sans-serif; --con:'Montserrat',var(--sans); }
@page{ size:A3 portrait; margin:0; }
*{ box-sizing:border-box; margin:0; padding:0; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
html,body{ font-family:var(--sans); color:var(--char); background:#fff; }
.page{ width:297mm; height:420mm; position:relative; overflow:hidden; background:#fff; page-break-after:always; display:flex; flex-direction:column; }
.page:last-child{ page-break-after:auto; }
.hd{ background:var(--green); height:27mm; display:flex; align-items:center; justify-content:space-between; padding:0 20mm; flex-shrink:0; }
.hd img{ height:18mm; display:block; }
.hd .tag{ font-size:8pt; letter-spacing:.24em; text-transform:uppercase; color:rgba(255,255,255,.6); }
.goldbar{ height:2.6mm; background:var(--gold); flex-shrink:0; }
.body{ padding:7mm 20mm 6mm; flex:1; display:flex; flex-direction:column; }
.intro{ display:flex; justify-content:space-between; align-items:flex-end; border-bottom:1px solid var(--line); padding-bottom:4mm; margin-bottom:3mm; }
.eyebrow{ font-size:8pt; letter-spacing:.22em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.h1{ font-size:22pt; font-weight:800; color:var(--ink); letter-spacing:-.01em; line-height:1.1; margin-top:2mm; }
.h1 small{ display:block; font-size:12pt; font-weight:500; color:var(--green); letter-spacing:.04em; margin-top:1.5mm; }
.meta{ text-align:right; font-size:9pt; color:var(--mut); line-height:1.7; } .meta b{ color:var(--ink); font-weight:600; }
.sec{ margin-top:3mm; }
.sec-hd{ display:flex; align-items:center; gap:4mm; margin-bottom:2.5mm; }
.sec-hd .num{ width:9mm; height:9mm; border-radius:50%; background:var(--green); color:#fff; font-weight:800; font-size:11pt; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.sec-hd .num.g{ background:var(--gold); }
.sec-hd h2{ font-size:15pt; font-weight:700; color:var(--ink); } .sec-hd h2 span{ font-weight:400; color:var(--mut); font-size:11pt; }
.sec-hd .cab{ margin-left:auto; font-size:8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--green); font-weight:700; border:1.5px solid var(--green); border-radius:3mm; padding:1.2mm 4mm; }
.sec-hd .cab.g{ color:#8a5a00; border-color:var(--gold); }
.lead{ font-size:9pt; color:var(--char); margin:0 0 3mm; line-height:1.5; } .lead b{ color:var(--ink); font-weight:600; }
.opt{ border:1px solid var(--line); border-left:3mm solid var(--green); border-radius:2mm; margin-bottom:3.5mm; overflow:hidden; }
.opt.gold{ border-left-color:var(--gold); }
.opt-hd{ display:flex; align-items:center; gap:5mm; padding:2.4mm 6mm; background:var(--green-soft); }
.opt.gold .opt-hd{ background:var(--gold-soft); }
.opt-hd .air{ font-size:12.5pt; font-weight:700; color:var(--ink); }
.opt-hd .air small{ display:block; font-size:8.5pt; font-weight:400; color:var(--mut); margin-top:.5mm; }
.prices{ margin-left:auto; display:flex; gap:0; }
.pr{ text-align:right; padding:0 0 0 6mm; margin-left:6mm; border-left:1px solid rgba(0,0,0,.12); }
.pr:first-child{ border-left:none; margin-left:0; padding-left:0; }
.pr .lab{ font-size:7pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.pr .brl{ font-size:14.5pt; font-weight:800; color:var(--ink); line-height:1.05; }
.pr .usd{ font-family:var(--con); font-size:8pt; color:var(--mut); margin-top:.8mm; } .pr .usd b{ color:var(--char); font-weight:600; }
table{ width:100%; border-collapse:collapse; font-size:8.5pt; }
th{ text-align:left; font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:var(--mut); font-weight:600; padding:1.8mm 3mm 1.4mm; border-bottom:1px solid var(--line); }
td{ padding:1.6mm 3mm; border-bottom:1px solid #efebe4; vertical-align:top; color:var(--char); }
tr:last-child td{ border-bottom:none; }
td.voo i{ display:block; font-style:normal; font-size:7pt; color:#8a5a00; font-weight:600; }
td.leg{ font-weight:600; color:var(--ink); } td.leg span{ display:block; font-weight:300; font-size:8pt; color:var(--mut); }
td.dt{ white-space:nowrap; } td.dt b{ color:var(--ink); font-weight:600; } td.dur{ white-space:nowrap; font-family:var(--con); }
tr.conn td{ padding:1mm 3mm; background:#faf8f4; font-size:8pt; color:var(--mut); font-style:italic; } tr.conn td b{ color:var(--green); font-style:normal; font-weight:600; }
tr.stop td{ padding:1.6mm 3mm; background:var(--gold-soft); font-size:8.5pt; color:#6b4600; } tr.stop td b{ color:#8a5a00; }
tr.dir td{ padding:1.8mm 3mm .6mm; border-bottom:none; }
.dirlab{ font-size:7pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); font-weight:700; }
.opt-ft{ display:flex; gap:8mm; padding:2mm 6mm; border-top:1px solid var(--line); font-size:8.5pt; } .opt-ft b{ color:var(--ink); font-weight:600; }
.sum{ margin-top:1mm; border:1px solid var(--line); border-radius:2mm; overflow:hidden; }
.sum table{ font-size:8pt; } .sum table td,.sum table th{ padding:1mm 5mm; }
.sum th{ background:var(--green); color:rgba(255,255,255,.85); border-bottom:none; }
.sum td.leg span{ font-size:7.2pt; line-height:1.15; }
.sum td.r{ text-align:right; font-family:var(--con); white-space:nowrap; } .sum td.r b{ color:var(--ink); }
.sum tr.hl td{ background:var(--gold-soft); }
.note{ font-size:8pt; color:var(--mut); margin-top:2mm; line-height:1.5; } .note b{ color:var(--ink); font-weight:600; }
.sig{ margin-top:auto; padding-top:3mm; border-top:1px solid var(--line); display:flex; justify-content:space-between; align-items:center; font-family:var(--con); font-size:8.5pt; color:var(--mut); }
.sig a{ color:var(--green); text-decoration:none; font-weight:600; } .sig img{ height:11mm; }
"""

def header():
    return f'''  <div class="hd"><img src="data:image/png;base64,{LOGO}" alt="LusaTravel"><div class="tag">Proposta de voos</div></div>
  <div class="goldbar"></div>
'''

def card(c):
    h = [f'      <div class="opt{" gold" if c["gold"] else ""}">',
         f'        <div class="opt-hd"><div class="air">{c["air"]} <small>{c["sub"]}</small></div><div class="prices">']
    for p in c['prices']:
        h.append(f'          <div class="pr"><div class="lab">{p["cab"]}</div><div class="brl">{p["brl"]}</div><div class="usd">{p["usd"]} · <b>{p["bag"]}</b></div></div>')
    h.append('        </div></div>\n        <table>\n          <tr><th>Voo</th><th>Trecho</th><th>Saída</th><th>Chegada</th><th>Duração</th><th>Aeronave</th></tr>')
    for r in c['rows']:
        if r['k']=='r':
            h.append(f'          <tr><td class="voo">{r["voo"]}</td><td class="leg">{r["leg"]}<span>{r["sub"]}</span></td><td class="dt"><b>{r["d1"]}</b> {r["t1"]}</td><td class="dt"><b>{r["d2"]}</b> {r["t2"]}</td><td class="dur">{r["dur"]}</td><td>{r["ac"]}</td></tr>')
        elif r['k']=='c': h.append(f'          <tr class="conn"><td colspan="6">{r["txt"]}</td></tr>')
        elif r['k']=='s': h.append(f'          <tr class="stop"><td colspan="6">{r["txt"]}</td></tr>')
        elif r['k']=='d': h.append(f'          <tr class="dir"><td colspan="6"><span class="dirlab">{r["txt"]}</span></td></tr>')
    h.append('        </table>')
    h.append('        <div class="opt-ft">' + ''.join(f'<span>{x}</span>' for x in c['ft']) + '</div>\n      </div>')
    return '\n'.join(h)+'\n'

def sec_hd(num, title, cab, gold=False, cont=False):
    g=' g' if gold else ''
    t = title + (' <span>· continuação</span>' if cont else '')
    return f'      <div class="sec-hd"><div class="num{g}">{num}</div><h2>{t}</h2><div class="cab{g}">{cab}</div></div>\n'

INTRO = f'''    <div class="intro">
      <div><div class="eyebrow">Cotação para sua viagem</div>
        <div class="h1">{CLIENTE}<small>São Paulo ⇄ Tóquio · Dezembro 2026 – Janeiro 2027</small></div></div>
      <div class="meta">Cotação <b>{COTACAO}</b><br>Câmbio de referência <b>{CAMBIO}</b><br>Valores com taxas de embarque incluídas</div>
    </div>
'''
LEAD1 = '<p class="lead">Quando a mesma companhia oferece mais de uma cabine <b>nas mesmas datas</b>, os valores aparecem lado a lado no mesmo cartão. Franquia de bagagem indicada junto a cada valor.</p>\n'
LEAD2 = '<p class="lead">A conexão da ida vira uma <b>parada em Istambul</b> antes de seguir para Tóquio: 3 noites com a saída de madrugada (TK 16) ou 2 noites com a saída à tarde (TK 216). Hospedagem em Istambul não está incluída.</p>\n'

def summary():
    rows=''
    for air,route,cab,ida,volta,bag,brl,usd,hl in SUMMARY:
        rows+=f'          <tr{" class=\"hl\"" if hl else ""}><td class="leg">{air}<span>{route}</span></td><td>{cab}</td><td>{ida}</td><td>{volta}</td><td>{bag}</td><td class="r"><b>{brl}</b></td><td class="r">{usd}</td></tr>\n'
    return f'''    <div class="sec">
      <div class="sec-hd"><div class="num">✓</div><h2>Resumo comparativo</h2></div>
      <div class="sum"><table>
          <tr><th>Companhia</th><th>Cabine</th><th>Ida</th><th>Volta</th><th>Bagagem</th><th style="text-align:right">Total R$</th><th style="text-align:right">Total USD</th></tr>
{rows}      </table></div>
      <p class="note"><b>*Nada reservado, apenas cotado.</b> Cotação {COTACAO[:5]} · {CAMBIO}. Tarifas sujeitas a alteração e disponibilidade até a emissão. Valores incluem tarifa e taxas de embarque. Hospedagem, seguro-viagem e transporte terrestre não estão incluídos nesta proposta. Horários em hora local de cada aeroporto.</p>
    </div>
'''
SIG = f'''    <div class="sig"><img src="data:image/png;base64,{LOGO_DARK}" alt="LusaTravel"><span><a href="mailto:atendimentolusatravel@gmail.com">atendimentolusatravel@gmail.com</a> &nbsp;·&nbsp; <a href="https://wa.me/5541991896076">+55 41 99189-6076</a></span></div>
'''

def page(inner):
    return f'<section class="page">\n{header()}  <div class="body">\n{inner}  </div>\n</section>\n'

C = {c['id']:c for c in CARDS+TURKISH}
pages = [
  INTRO + '    <div class="sec">\n' + sec_hd(1,'Opções por companhia aérea','Economy · Premium · Business') + LEAD1 + card(C['aa-eco'])+card(C['aa-exec']) + '    </div>\n',
  '    <div class="sec">\n' + sec_hd(1,'Opções por companhia aérea','Economy · Premium · Business',cont=True) + card(C['ac'])+card(C['am-27'])+card(C['am-28']) + '    </div>\n',
  '    <div class="sec">\n' + sec_hd(1,'Opções por companhia aérea','Economy · Business',cont=True) + card(C['ita'])+card(C['lh']) + '    </div>\n',
  '    <div class="sec">\n' + sec_hd(2,'Opção especial · Turkish Airlines com stopover em Istambul','Stopover Istambul',gold=True) + LEAD2 + card(C['tk-1'])+card(C['tk-2']) + '    </div>\n',
  summary() + SIG,
]
html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Laura Dalcanale | Tóquio — LusaTravel</title>
<style>{CSS}</style></head>
<body>
{''.join(page(p) for p in pages)}</body></html>
'''
(HERE/'proposta-laura-dalcanale-toquio.html').write_text(html, encoding='utf-8')
print('ok', len(html))
