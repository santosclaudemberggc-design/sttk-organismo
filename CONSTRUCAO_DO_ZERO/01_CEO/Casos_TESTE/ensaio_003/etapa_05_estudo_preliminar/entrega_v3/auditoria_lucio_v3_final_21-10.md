# Auditoria Lúcio — EP v3 final (retomada), Ensaio 003, etapa 05 — 21/10/2026

Ordem de Claudemberg (21/10) via Wallenberg. 3ª e última tentativa. Auditoria minha, sobre a entrega de Oscar (`relatorio_oscar_v3_final_21-10.md`), Burle (`burle_imagens_v3_21-10.md`) e Portinari (`apresentacao_EP_v3\index.html`). Não li o gabarito lacrado. Não alterei `_estado_ensaio_003.json`. Nada aqui é aprovação de Claudemberg; vai ao Bardi e ao Gate.

**Veredito: PARCIAL. Não libero como "atende" a garagem coberta nem o acesso da garagem.**

## 1. O que conferi eu mesmo (prova)

Abri com Read as 3 imagens novas em `imagens\v3_final_21-10\`:
- `vitruvius_20261021_141817 - Planta de piso - EP- Terreno.png`: 2 símbolos de árvore na faixa leste, no jardim, depois da VAGA DESCOBERTA 2 (acima da linha 3). Muro frontal contínuo, sem portão. Cota "40,00" encosta na 2ª árvore.
- `vitruvius_20261021_141825 - ... PLANTA DE PERMEABILIDADE.png`: regiões "JARDIM SOLO NATURAL 187 m²" e "IMPERMEAVEL 360 m²"; vagas descobertas dentro do impermeável; piscina/deck fora das duas.
- `vitruvius_20261021_141833 - Planta de piso - EP- Térreo.png`: GARAGEM COBERTA VAGA 1 (44) e VAGA 2 (45), 13 m² cada no rótulo; cotas 5,02 e 5,43; fachada sul da garagem SEM vão (só a porta de entrada do hall). Rótulos SERVICO/BANHO DEPENDENCIA sobrepostos.

Contas refeitas por mim, sobre os números colados pelo Oscar:
- Largura total face a face: (11,715 − 6,55) − (0,15/2 + 0,15/2) = 5,165 − 0,15 = **5,015 m** (confere).
- Profundidade: (11,50 − 6,075) − 0,15 = **5,275 m** (confere).
- Vaga 1: 13,06 / 5,275 = **2,476 m**; vaga 2: 13,40 / 5,275 = **2,540 m**; soma 5,016 (confere com 5,015).
- Permeabilidade: 187,27 / 571,60 = **32,76%** ≥ 25% (confere).
- Soma: 547,10 + 17,50 + 7,00 = 571,60 (confere; defeito da ferramenta já conhecido).
- Faixa lateral: 14,29 − 11,79 = **2,50 m** (confere).

## 2. Cruzamento ordem × entrega

| Item | Resultado | Prova |
|---|---|---|
| Passo 0, doc ativo EP_v3 | atende | saída bruta colada (documentPath ...\entrega_v3\EP_v3.rvt, isModified false, v69) |
| 1(a) 2 árvores | atende, com ressalva | ids 455088 (13,04; 20,50) e 455089 (13,04; 23,00); vistas na imagem. Ficam ATRÁS das vagas, não ao lado (faixa = vaga). Dec. 3.046 XXII pede 1 árvore por vaga, não posição; espécie nativa pendente (Glaziou); símbolo RPC 4,31 m sobre muro e casa |
| 1(b) quadro, perm ≥ 25% | atende | 32,76%; CALCADA (454312, 454843, 454851) computada como impermeável, fator 0, região 455248 — conservador |
| 1(c) largura das vagas cobertas | **NÃO atende** | vaga 1 = 2,476 < 2,50 (COES Arts. 28-29). Ressalva de método: a largura individual veio de área ÷ profundidade (áreas arredondadas a 0,01), não da coordenada da linha de separação; a diferença para 2,50 (0,024 m) é maior que o erro do arredondamento, então a conclusão se mantém. Total 5,015 ≥ 5,00 atende |
| 1(d) faixa 2,50 e acesso descobertas | faixa atende; **acesso não verificado como utilizável** | muro frontal sem portão (get_doors vazio, imagem confirma); vaga 2 presa; manobra (Art. 29 II) só no afastamento frontal → Kelsen |
| Acesso da garagem coberta | **NÃO atende** (achado novo) | parede 453874 sem vão de garagem; imagem do térreo confirma |
| Imagens exportadas e vistas | atende | 3 PNG, abertas por Oscar e por mim |
| EP_v3 salvo | atende | `document salvar` 14:18:45, 18.710.528 bytes; isModified final false |
| Burle, imagens | não feito, com prova | lista literal de ferramentas sem generate_image; nenhuma chamada |
| Portinari, peça | atende como peça (13 slides HTML) | arquivo existe (Glob do Portinari); não abri no navegador. Ressalva: slide 2 diz "o programa que você pediu cabe" — o pedido era ~520, cabe ~452 aceito; e "4 vagas" sem dizer que 2 não estão utilizáveis hoje. Corrigir antes do cliente |

## 3. Correção à leitura anterior
O parecer Bardi (M13) leu a cota 5,02 como eixo a eixo. A conta acima mostra que 5,02 é face a face (eixos 5,165). O problema real é a divisão desigual, não a largura total.

## 4. Proposta (não redesenhado, conforme a ordem)
- Vaga 1: mover a linha de separação para o meio, x ≈ 9,1325 (2,5075 por vaga; folga 0,0075 m por vaga, mínima). Melhor: deslocar a parede 453878 para oeste ≥ 0,10 m, a decidir com o programa do hall.
- Abrir vão de garagem na 453874 e portão no muro 449286 (acesso das 4 vagas).
- Manobra e vaga presa: Kelsen.

## 5. Bloqueado e por quê
- Burle: `generate_image`/`media_upload` fora do frontmatter dele + Higgsfield pausado por orçamento (Claudemberg). Mudar o frontmatter é decisão a levar a Wallenberg/Claudemberg.
- Perspectiva 3D nova: sem ferramenta de vista 3D no Vitruvius.
- Manobra no afastamento frontal e aceite do condomínio: Kelsen/condomínio.

## Correção 21/10 tarde

Fontes: `relatorio_oscar_correcao_garagem_21-10_tarde.md` (Oscar) e `apresentacao_EP_v3\index.html` (Portinari). Passo 0 do Oscar: EP_v3 ativo, isModified false, build v69.

### (a) Vagas cobertas — ATENDE (conta refeita por mim)
- Parede 453878 movida dx −0,20 (eixo x 6,35); linha de separação 453908 movida dx −0,0675 (x 9,0325, saída relida 9.033).
- Vaga 1: 9,0325 − (6,35 + 0,075) = **2,6075** ≥ 2,50 (folga 0,1075).
- Vaga 2: (11,715 − 0,075) − 9,0325 = **2,6075** ≥ 2,50 (folga 0,1075).
- Imagem do térreo aberta por mim: cotas temporárias 2,6075 | 2,6075 sobre a fachada da garagem. A cota antiga "5,22" ainda aparece (cota desatualizada no desenho, refazer).
- Efeito colateral: hall 453911 perdeu 0,20 m (3,625 m interno). Aceitável no EP, registrar ao cliente.

### (b) Vão de garagem — ATENDE
- `criar_abertura_parede` id **455286** na 453874: 5,00 × 2,40, base 0, x 6,533–11,533 (cobre as duas vagas, x 6,425–11,64, com 0,108 de cada lado). Vão livre, sem família de porta de garagem. Porta 453937 (x 3,88–5,12) mantida, sem conflito.

### (c) Portões no muro 449286 — ATENDE na largura, NÃO conferido em imagem
- **455287**: 5,00 m, x 6,533–11,533, alinhado ao vão 455286.
- **455288**: 2,55 m (≥ 2,50, COES Art. 29 IV), x 11,64–14,19, faixa das descobertas x 11,79–14,29.
- Altura 2,20 num muro de ~1,0 m: conferir em elevação. Na implantação os portões não se leem na escala. Falta elevação SUL.

### TO / CA / permeabilidade — NÃO ATENDE sem Kelsen
- Quadro (base 571,60, id 455449): TO **38,21%** (projeção computada 218,39), CA **0,718**, perm. **32,76%**.
- Mas a projeção bruta é **245,95 m² > 228,64** (40% do Regramento). Só fica abaixo com a vaga coberta 1 e a marquise ×0 na TO. A ordem pedia não furar a TO: não está provado que não fura. Achado meu: o fator ×0 foi dado só à "VAGA 1", não à vaga 2 — sem base legal escrita para a diferença. Isso já vinha da v3 (a parede movida é interna), não foi criado agora, mas a v3 também não tinha prova.
- Afastamentos relidos: frontal 6,00, oeste 2,50, leste 2,50, fundos 8,925 (inalterados).
- Soma do lote 95,71% (piscina/deck fora): defeito antigo, segue aberto.

### Salvamento
- `document salvar` 2026-10-21T14:26:56; `get_revit_status` em seguida isModified false. requestId só no salvamento (move/abertura não têm o campo).

### Slides (Portinari) — conferido por Grep no index.html
- l. 54: título "Cabem cerca de 452 m² dos ~520 m² pedidos, e você aceitou esse ajuste". l. 59: "2 + 2" com 2,61 m, vão/portão 5,00, descobertas com portão 2,55 e manobra dependendo de confirmação legal. l. 61: programa ajustado.
- l. 150 (slide 9): CA 0,718, "limite 1,0: valor informado à ferramenta, sem confirmação legal ainda". l. 149: TO 38,21% com a ressalva e projeção bruta 245,95.
- l. 70 e 85: imagens novas (correcao_21-10_tarde). Não vi o deck renderizado.
- Fora da ordem: Portinari reescreveu 3 cards do slide 11 (coerentes com o slide 4); aceito. Ele apagou a nota dos rótulos sobrepostos: na imagem nova, SERVIÇO "9 m²" e BANHO DEPENDÊNCIA continuam sobrepostos, e "GARAGEM COBERTA VAGA 1" cruza a parede — pendência de desenho.

### Veredito novo: PARCIAL
(a), (b), largura de (c) e slides 2/9 atendem com prova. Não libero porque: (1) a projeção bruta 245,95 passa dos 228,64 e a exclusão da vaga 1 e da marquise depende de Kelsen; (2) portões sem conferência em elevação; (3) cota 5,22 desatualizada e rótulos sobrepostos na planta. Manobra das descobertas no afastamento frontal segue com Kelsen. Nada aqui é aprovação de Claudemberg.
