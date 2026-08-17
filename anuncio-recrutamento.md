# Cartografia Silenciosa — filosofia visual

*Movimento estético aplicado à peça de recrutamento da Lusa Travel.*

## Manifesto

**Cartografia Silenciosa** trata a superfície como um instrumento de medição, não como
um cartaz. Parte da convicção de que uma ideia humana — o desejo de partir, de pertencer
a um time, de atravessar o mundo — pode ser registrada com o mesmo rigor com que se
registra uma rota náutica. O plano é um papel creme, quente e levemente envelhecido, como
uma folha de atlas guardada há décadas; sobre ele, uma única linha de ouro descreve um arco
de círculo máximo, e uma placa de verde profundo ancora a afirmação central. Nada mais
acontece. Essa contenção é deliberada e cara: cada milímetro de vazio foi calculado com
paciência de artesão, e é no vazio que a peça respira.

## Espaço e forma

A composição obedece a uma malha invisível de módulos rigorosos. Marcas de registro —
cruzes finíssimas, quase imperceptíveis — pontuam o campo em intervalos regulares,
como as marcações de um instrumento óptico. Elas não decoram: provam que alguém mediu.
O arco atravessa o terço superior sem tocar nenhum bloco de texto, e os nós que o
pontuam (círculos de um pixel e meio de traço) sugerem escalas de uma viagem que ainda
não aconteceu. Toda a estrutura é resultado de refinamento obsessivo: nada encosta em
nada, nada transborda, nada é acidental.

## Cor e matéria

A paleta é reduzida a três estados: papel creme (`#f7f2ea`), verde savana (`#404525`) e
ouro (`#da8d00`). O verde é a tinta — títulos, rótulos, numerais, a placa que carrega o
claim — e desce a `#2f3319` quando precisa de peso. O ouro nunca é usado como enfeite:
ele indica, mede, separa. Aparece no filete de dois pixels sob a marca, no arco pontilhado,
nas cruzes de registro dos cantos e nas palavras que ficam sobre o verde, onde a densidade
do fundo lhe devolve a legibilidade que o creme lhe tira. Nenhuma dessas duas cores tem
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

A informação é lida em três tempos: o arco (respiração), a manchete (afirmação), as
colunas indexadas (evidência). O rodapé fecha o instrumento com um filete e um endereço,
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
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # ou 'chromium'
$CH --headless --no-sandbox --hide-scrollbars --force-device-scale-factor=1 \
    --screenshot=anuncio-recrutamento.png --window-size=1080,1350 \
    file://$PWD/anuncio-recrutamento.html
$CH --headless --no-sandbox --no-pdf-header-footer \
    --print-to-pdf=anuncio-recrutamento.pdf file://$PWD/anuncio-recrutamento.html
```
