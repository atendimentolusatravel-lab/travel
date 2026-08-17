# Cartografia Silenciosa — filosofia visual

*Movimento estético aplicado à peça de recrutamento da Lusa Travel.*

## Manifesto

**Cartografia Silenciosa** trata a superfície como um instrumento de medição, não como
um cartaz. Parte da convicção de que uma ideia humana — o desejo de partir, de pertencer
a um time, de atravessar o mundo — pode ser registrada com o mesmo rigor com que se
registra uma rota náutica. O plano é um papel creme, quente e limpo, como uma folha de
atlas guardada há décadas; sobre ele não há trama, nem grafismo, nem ilustração — apenas
tipografia, quatro filetes e uma barra de ouro de dois pixels. Nada mais acontece. Essa
contenção é deliberada e cara: cada milímetro de vazio foi calculado com paciência de
artesão, e é no vazio que a peça respira.

## Espaço e forma

A composição obedece a uma malha rigorosa que permanece invisível: ela ordena, mas nunca
aparece. A moldura de um pixel apenas insinua o limite do papel, e quatro marcas de ouro
nos cantos — do tamanho de uma unha — funcionam como cruzes de registro de uma prova
gráfica. Elas não decoram: provam que alguém mediu. Todo o resto é distância calculada
entre blocos, e é essa distância que o olho lê como elegância. Nada encosta em nada,
nada transborda, nada é acidental.

## Cor e matéria

A paleta é reduzida a três estados: papel creme (`#f7f2ea`), verde savana (`#404525`) e
ouro (`#da8d00`). O verde é a tinta — títulos, rótulos, numerais e o único
bloco sólido da peça, o selo da vaga — e desce a `#2f3319` quando precisa de peso. O ouro nunca é usado como enfeite:
ele indica, mede, separa. Aparece em três lugares e só neles: o filete sob a marca, a barra
vertical que sustenta o claim e as cruzes de registro dos cantos — nunca em texto pequeno
sobre o creme, onde perderia legibilidade. Nenhuma dessas duas cores tem
variante inventada: o mesmo verde, o mesmo ouro, apenas em opacidades calibradas até que a
hierarquia se resolvesse sozinha — sem contorno, sem sombra, sem truque.

## Escala e ritmo

A tipografia funciona por contraste extremo de peso e tamanho: uma manchete em Poppins
Light, aberta e serena, contra micro-rótulos em Montserrat com tracking largo, tratados
como legendas de catálogo científico. Entre os dois extremos, quase nada — a ausência
de tamanhos intermediários é o que produz a sensação de precisão. Os numerais `01–04`
funcionam como índices de espécime: ordenam sem hierarquizar, e sua repetição constrói
o ritmo da leitura.

## Hierarquia e execução

A informação é lida em três tempos: a manchete (afirmação), a barra de ouro com o claim
(anúncio), as colunas indexadas (evidência). O rodapé fecha o instrumento com um filete e um endereço,
como a assinatura de um cartógrafo no canto da folha. O resultado deve parecer trabalhado
por muitas horas, por alguém no topo do ofício — não um layout preenchido, mas um objeto
impresso que sobrevive à ampliação: filetes de espessura exata, alinhamentos ópticos
corrigidos à mão, e um silêncio geral que só se consegue removendo, nunca acrescentando.

---

## Texto de apoio (legenda / WhatsApp / grupos)

> **Nosso time está crescendo — e estamos recrutando.** 🌍✈️
>
> A Lusa Travel abre uma vaga para atuar com:
> • Atendimento aos passageiros
> • Orçamentos
> • Contato com fornecedores
> • Rotinas administrativas
>
> **Requisitos:** inglês intermediário · Excel básico · gostar de viajar
> **Vaga presencial** — Curitiba/PR
>
> Envie seu currículo para **atendimentolusatravel@gmail.com**
> ou WhatsApp **+55 41 99189-6076**.

## Arquivos gerados

| Arquivo | Uso |
|---|---|
| `anuncio-recrutamento.html` | fonte editável (texto, cores, itens) |
| `anuncio-recrutamento.png` | 1080 × 1350 px — feed Instagram / LinkedIn / WhatsApp |
| `anuncio-recrutamento.pdf` | A4 retrato — impressão em vitrine, mural, balcão |

Para regerar após editar o HTML:

```bash
# headless_shell (headless real): o modo --headless legado desconta a altura
# da barra do navegador e corta ~85px do canvas no screenshot.
CH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
$CH --no-sandbox --hide-scrollbars --force-device-scale-factor=1 \
    --screenshot=anuncio-recrutamento.png --window-size=1080,1350 \
    file://$PWD/anuncio-recrutamento.html
$CH --no-sandbox --no-pdf-header-footer \
    --print-to-pdf=anuncio-recrutamento.pdf file://$PWD/anuncio-recrutamento.html
```
