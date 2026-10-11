# Peça 1 (v2) — Levantamento Planialtimétrico Cadastral orientado ao DULI
## Ensaio Sombra 003, Etapa 03: Levantamento. Família Montenegro Prates (100% FICTÍCIO)

**Executor:** Oscar (Agente, Arquitetura, nível Assisted) | **Auditoria:** Lúcio (Gestor de Arquitetura)
**Data:** 06/10/2026 (v2, depois da reprovação da v1 por Claudemberg) | **Natureza:** ANÁLISE PRELIMINAR. Num caso real, não é entregável final sem a conferência de Lúcio e o Gate do Maurício.
**Lote:** Rua das Garças, Lote 17, Quadra C, Condomínio Reserva das Garças, Recreio dos Bandeirantes (AP4). Fonte: caso §3.
**Peça autossuficiente.** Substitui a v1 (`entrega/01_...003.md`, que fica intocada para rastreio). Tudo o que muda em relação à v1 está marcado **[v2]**.

**Etiquetas**
- **(a)** dado do dossiê (caso §1–§4, 5.1 a 5.10 e, **[v2]**, 5.11 a 5.15 do enunciado da Etapa 02). Dentro do ensaio, vale como verdade.
- **(b)** premissa ou mecanismo do Legal aprovado (Etapa 01: parecer do Hely e auditoria do Kelsen, com a ERRATA 4.1), da Viabilidade aprovada (Etapa 02) ou de uma Skill, com a seção citada.
- **(c)** pendente ou lacuna: o que falta, quem fornece e quem decide.

**[v2] O que mudou nesta peça:** §0 com o retorno literal da ferramenta nesta execução; §3 com a cota do piso térreo respondida até onde é possível afirmar e as curvas de nível a cada 1,00 m; T1 corrigido (curvas a cada 1,00 m pela NBR 6492:2021 5.1.1 b); T15 desdobrado; itens novos T18 a T25; nova §7.1, com a tabela "item exigido pela NBR 6492:2021 5.1 × situação no dossiê"; §8 corrigida (a Skill `nbr6492-2021-memoriais-por-etapa-projeto` foi usada; a frase da v1 que dizia o contrário foi retirada); §9 com a declaração atualizada (nesta rodada li o `parecer_bardi.md` por ordem de Lúcio).

---

## 0. Bloqueio de ferramenta e limite desta peça

- **Revit/Vitruvius [v2].** Chamei `mcp__vitruvius__revit_status` uma vez, antes de qualquer escrita da v2, em 06/10/2026. Retorno literal: `Error: No such tool available: mcp__vitruvius__revit_status`. Não há modelo nem ferramenta BIM nesta sessão, e **não simulei desenho**. A peça sai em texto, tabelas e um croqui descritivo com coordenadas em metros, a partir de um referencial declarado (§1).
- **Sem visita.** O POP-PROJ-01 não admite iniciar o traço sem conferência física presencial, e o ensaio não tem visita. Tudo o que está abaixo vem do dossiê ou é conta sobre ele. Onde o dossiê não traz o dado, escrevo **"não consta no dossiê"** e o item entra na lista de complementação (§7).
- **O levantamento 5.2 não basta para o DULI.** Pela Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` §3 e §5, o DULI exige RN do meio-fio na testada, curvas de nível, perfil natural do terreno, PAA/alinhamento com número, passeio com largura, PVs/PVIs, postes, árvores e construções existentes. O 5.2 traz só o perímetro, a área, a nota sobre o muro, a distância da edícula à divisa e a cota de soleira **prevista**. O próprio topógrafo escreveu que o levantamento ficou "restrito ao perímetro do lote; espelho d'água do lago não levantado" (5.2) **(a)**. Conclusão: **o 5.2 serve de base de área e perímetro, mas não serve de base de DULI.** É preciso encomendar a complementação do §7 **(c)**.
- **[v2] O 5.2 também não basta para o Levantamento pela NBR 6492:2021.** A norma pede, nesta etapa, relatórios com dados ambientais (inclusive regime de ventos e de marés), urbanísticos e legislativos, áreas alagáveis e registro fotográfico com pontos de vista (Skill `nbr6492-2021-memoriais-por-etapa-projeto` §2, linha LV-ARQ, e §3, nota LV). O que existe e o que falta está na §7.1.
- **Destino do DULI.** O enunciado diz que o DULI "será anexado ao projeto executivo (Etapa 15)". Não confere: o DULI é peça do Projeto Legal/LICIN (LICIN Anexo I, citado no parecer da Etapa 01, §2.1 e T8), cuja etapa é a **07 (Legal: entrada na Prefeitura e no condomínio, Kelsen/Hely)**, conforme o caso §6. Este levantamento **alimenta** o DULI da Etapa 07, mas não é o DULI.

---

## 1. Referencial e croqui descritivo (aproximação retangular)

**Referencial adotado (declarado por mim, Oscar):**
- Origem **O = (0,00; 0,00)**: vértice frente-esquerda, no encontro do alinhamento com a face do **muro existente do Lote 16**. Os afastamentos se medem a partir desse muro (premissa da Etapa 01, parecer §2.1 e §5.2) **(b)**.
- Eixo **x**: ao longo da testada, da esquerda (Lote 16) para a direita. Eixo **y**: perpendicular à testada, da rua para os fundos.
- **Aproximação:** retângulo de **14,29 m × 40,00 m**, com a menor largura medida e a menor lateral medida (mesmo critério do parecer §2.3) **(b)**. O lote real **não é retângulo**: frente 14,30, fundos 14,29, lateral esquerda 40,00, lateral direita 40,02 (5.2) **(a)**. O 5.2 não traz ângulos nem coordenadas dos vértices **(c)**. Por isso, toda área abaixo é aproximação. A área oficial do lote é a do topógrafo, **571,80 m²**.
- **Altimetria:** o dossiê só traz a cota de soleira **prevista** de +3,20 m, no referencial do condomínio (5.2) **(a)**. Não há RN do meio-fio, curvas de nível nem cota do terreno atual **(c)**. Por isso, nenhuma coordenada z é atribuída ao terreno.

**Croqui esquemático (sem escala; é diagrama de leitura, não desenho de projeto):**

```
 y (m)
 52,00  ~~~~~~~~ margem do lago (5.5: 12,00 m além da divisa de fundos) ~~~~~~~~
        |         faixa verde comum do condomínio, 12 m (5.5) — fora do lote   |
 40,00  +================= divisa de fundos (14,29 m medidos) ==================+
        |  FAIXA DE FUNDOS 5,00 m  (y 35,00–40,00)                            |
 35,00  |----+----------------------------------------------------+----------|
        |    |                                                    |          |
        | L  |   ENVELOPE H0: x 2,50–11,79 ; y 6,00–35,00          |  L   ed. |  <- edícula: face a
        | A  |   9,29 × 29,00 = 269,41 m²  (zona de implantação   |  A  x≈13,49 0,80 m da divisa
        | T  |   possível; varandas só aqui dentro [v2])          |  T       |     direita (5.2); y e
 22,00  |-E--|- - - - - linha H1 (30 m da margem = y 22,00) - - - -|--D-------|     dimensões: não
        | S  |   ENVELOPE H1: y 6,00–22,00 → 9,29 × 16,00 = 148,64 |  I       |     constam
        | Q  |                                                    |  R       |
  6,00  |----+---- face frontal de qualquer pavimento: y ≥ 6,00 [v2] ------+----------|
  5,60  |    .  .  .  só jardineira/ar-condicionado, acima do térreo (XIV) [v2]    |
        |  AFASTAMENTO FRONTAL 6,00 m (y 0–6,00): ipê + 2 amendoeiras (caso §3);|
        |  locação e DAP: não constam                                          |
  0,00  O================== alinhamento / testada (14,30 m medidos) ==========+
        x=0 (muro Lote 16)  x=2,50                                x=11,79   x=14,29
                            RUA DAS GARÇAS (passeio, meio-fio, postes, PVs: não constam)
```

**Coordenadas-chave (aproximação):**

| Elemento | Coordenadas / medida | Fonte | Etiq. |
|---|---|---|---|
| Lote (aproximação) | x 0–14,29; y 0–40,00 | 5.2; parecer §2.3 | (a)+(b) |
| Envelope H0 (zona de implantação possível) | x 2,50–11,79; y 6,00–35,00 | parecer §2.3; 5.4 Art. 6º | (b) |
| **[v2]** Limite das varandas (premissa operacional, Peça 2 §2.5) | dentro do envelope: x 2,50–11,79; y 6,00–35,00 | Skill `varandas-...` §4.1; parecer linha 16 e §5.2; COES Art. 8º §2º | (b)/(c) |
| **[v2]** Saliência frontal admitida (Dec. 3.046 XIV) | até y = 5,60 (0,40 m), acima do térreo, só jardineira e ar-condicionado | Skill `decreto3046-...` §6, complemento do M3; Skill `varandas-...` §4.1 | (b) |
| Linha de H1 (APP de 30 m da margem) | y = 22,00 (40,00 − 18,00) | parecer §2.4 e §5.2 ("faixa entre 22 m e 40 m da frente") | (b)/(c) |
| Margem do lago | y ≈ 52,00 (40,00 + 12,00) | 5.5, planta anexa | (a) |
| Face da edícula voltada à divisa direita | x ≈ 14,29 − 0,80 = 13,49 | 5.2 | (a) + conta |
| Casa de 1998 | **posição e dimensões: não constam no dossiê** (só "cerca de 180 m²", caso §3) | caso §3 | (a)/(c) |
| Piscina | **posição, dimensões, profundidade e cota: não constam no dossiê** | caso §3, §4 | (c) |
| Árvores (3) | "no afastamento frontal", ou seja, y entre 0 e 6,00; **x, DAP, copa e estado: não constam** | caso §3 | (a)/(c) |

> O "EXEMPLO" do enunciado ("casa de ~180 m² no meio do lote", "edícula de ~20–30 m²", "piscina talvez ~4 × 8 m nos fundos") **não é documento do dossiê**. Não uso esses valores em nenhuma conclusão.

---

## 2. Dimensões do lote: título × medida local

| Lado | Matrícula 5.1 | Levantamento 5.2 | Diferença |
|---|---|---|---|
| Frente | 15,00 | 14,30 | −0,70 |
| Fundos | 15,00 | 14,29 | −0,71 |
| Lateral esquerda (Lote 16) | 40,00 | 40,00 | 0,00 |
| Lateral direita | 40,00 | 40,02 | +0,02 |
| **Área** | **600,00 m²** | **571,80 m²** | **−28,20 m²** |

Fontes: 5.1 e 5.2 **(a)**. O RIU (5.3) também registra 600,00 m² no cadastro **(a)**. A escritura (5.11) descreve o lote "com área de 600,00 m²" **(a) [v2]**.

**Conferência das contas:**
- Retângulo pelas médias: ((14,30 + 14,29) / 2) × ((40,00 + 40,02) / 2) = 14,295 × 40,01 = **571,94 m²**. Fica 0,14 m² acima do valor do topógrafo, o que é compatível com o polígono não retangular. Prevalece **571,80 m²**, que é o valor medido **(a)**.
- Perda atribuída ao muro (parecer §2.1): 0,70 × 40,00 = **28,00 m²** contra 28,20 m² de diferença real **(b)**. O enunciado escreve "~0,70 m × 40 m = 28 m²". O número exato da diferença é **28,20 m²**.

**Motivo da divergência.** O topógrafo registra que o "muro da divisa lateral esquerda do vizinho (Lote 16) avança sobre a linha de projeto do PAL" (5.2) **(a)**. Ele **não mediu quanto o muro avança**. A atribuição dos 28,20 m² ao muro é inferência do Legal ("muito provavelmente", parecer §2.1) **(b)**. Para provar isso, é preciso locar a linha do PAL no terreno e cotar o muro em relação a ela **(c: topógrafo, T5)**.

**Área adotada: 571,80 m²**, com os afastamentos medidos a partir do muro existente. É premissa recomendada pela Etapa 01 (parecer §2.1 e §5.2) e **não a reinterpreto** **(b)**. A escolha tem efeito patrimonial: quem decide é o **cliente com advogado**, e o Legal só recomenda (Kelsen R1) **(c)**. O cenário de 600,00 m² só entra se a divisa for regularizada.

**O que vai ao DULI:** as dimensões do título **e** as medidas locais, porque há divergência (LICIN Anexo I, III, Planta de situação, item 1, citado no parecer §2.1; Skill de levantamento §3) **(b)**.

---

## 3. Altimetria e topografia

| Item | Situação no dossiê | Etiq. |
|---|---|---|
| Cota de soleira | **+3,20 m "prevista"**, referência do condomínio (5.2). **Não é cota atual.** O enunciado chama de "atual", o que não confere com o 5.2 | (a) |
| Referencial do +3,20 | Condominial. A amarração ao referencial oficial **não foi confirmada** (parecer, quadro linha 19) | (c) |
| Efeito legal da cota | LC 270 Art. 458 caput: cota de soleira < 3 m, ou área frágil de baixada, exige avaliação técnica do Município (parecer, linha 19 e T9). Se o +3,20 condominial corresponder a menos de 3 m no referencial oficial, o Art. 458 entra em jogo. **Quem decide: Kelsen/Hely** | (b)/(c) |
| Teto de altura com a soleira prevista | 5.4 Art. 7º: 8,50 m medidos da cota de soleira ao ponto mais alto. Conta: +3,20 + 8,50 = **+11,70 m** (referencial do condomínio), **se** a soleira ficar em +3,20 | (a)+(b) |
| Cota do terreno atual, curvas de nível, aclives e depressões | **Não constam no dossiê.** **[v2]** As curvas têm de vir **a cada 1,00 m** (NBR 6492:2021 5.1.1 b, via Skill `nbr6492-2021-memoriais-...` §2 e §3) | (c) |
| RN do meio-fio na testada | **Não consta** (exigido pelo DULI: Skill de levantamento §3, Planta de situação item 8; Cortes item 4) | (c) |
| Perfil natural do terreno e sinais de aterro | **Não constam** (exigidos: Skill de levantamento §3, Cortes itens 3 e 6, e §4 "terreno natural × aterro"). Qual cota vale como "natural" é decisão do Hely (Skill de levantamento, R2) | (c) |
| Aterro necessário até +3,20 | **Não calculável** sem a cota do terreno atual | (c) |
| Nível d'água | **0,90 m** abaixo da superfície, na sondagem de 2024. **Vem do 5.7, não do 5.2.** O enunciado atribui o NA ao 5.2, e isso não confere | (a) |
| **[v2] Cota do piso térreo da casa nova** | **O que se pode afirmar hoje:** (1) pelo glossário do COE, a cota de soleira é a cota de implantação da edificação (Skill de levantamento §2, linha III); (2) a cota de soleira **prevista** é +3,20 no referencial do condomínio (5.2); (3) a altura de 8,50 m é medida a partir da soleira (5.4 Art. 7º), de modo que, se o piso térreo ficar acima da soleira, a diferença sai da altura disponível. **O valor final não é afirmável** e depende de T2 (RN do meio-fio), T3 (amarração ao referencial oficial e Art. 458), T4 (terreno natural e aterro) e da regra numérica de soleira e de terreno natural, que é do Hely (Skill de levantamento R2). A fixação é do EP (Etapa 05), sobre esses dados | (a)+(b)/(c) |

---

## 4. Edificações existentes

| Edificação | O que o dossiê diz | O que não consta | Etiq. |
|---|---|---|---|
| **Casa de 1998** | Térrea, "cerca de 180 m²", **existente e a demolir** (caso §3). Nunca averbada (5.1). Tem Habite-se de 1999 (5.8). A demolição de ~180 m² está orçada no Mascaró v8 §6.4 | Posição, dimensões, projeção exata, cota do piso | (a)/(c) |
| **Edícula** | Churrasqueira e depósito (caso §3). Fica a **0,80 m** da divisa lateral direita, com janela voltada para a divisa (5.2). **Não consta** da planta do Habite-se (5.8). **[v2]** O cliente quer **mantê-la**: "já estão prontas, economiza" (caso §4). Resposta na Peça 2 §4.1 | Área, dimensões, posição em y, altura, cota | (a)/(c) |
| **Piscina** | Existe, e o cliente quer mantê-la pelo mesmo motivo ("já estão prontas, economiza", caso §3, §4) **[v2]**. Resposta na Peça 2 §4.2 | Posição, dimensões, profundidade, cota da borda, estado, se aparece no Habite-se | (a)/(c) |

**Contradição do enunciado.** O resumo de entrada diz "Casa demolida (térrea 180 m²)". As fontes dizem o contrário: a casa **existe** e está **a demolir** (caso §3: "para demolir a casa e construir"; 5.8 registra o Habite-se dela; Mascaró v8 §6.4 orça a demolição). Adoto: **casa existente, a demolir.**

**Cores do DULI para o que existe** (Skill de levantamento §5; LICIN Anexo I, IV.2): amarelo para demolir, vermelho para novo ou a legalizar, preto para existente a manter. Na premissa da Etapa 01, casa e edícula vão a amarelo **(b)**. A piscina fica **indefinida** até ser levantada (Peça 2 §4.2).

---

## 5. Vegetação de porte

| Item | Dossiê | Não consta | Etiq. |
|---|---|---|---|
| 1 ipê-amarelo + 2 amendoeiras | Ficam no afastamento frontal (caso §3; o enunciado repete) | Locação (x, y), DAP, diâmetro de copa, altura, estado fitossanitário, laudo | (a)/(c) |

O levantamento cadastral precisa trazer a posição, a espécie e o DAP de cada árvore (Skill de levantamento §4, "Árvore na testada", e §5; Skill `remocao-arvores-...` §4: "planta/croqui com localização das árvores", com responsável Glaziou/Oscar) **(b)**. A **arborização do passeio** também precisa ser levantada, porque o COE Art. 35 §4º a exige em edificação nova (via Skill de levantamento §4) **(b)/(c)**. A NBR 6492:2021 5.1.1 b) também pede as árvores na planta planialtimétrica (Skill `nbr6492-...` §2) **(b) [v2]**.

---

## 6. Acessos, vizinhança e corpo hídrico

**Acessos**
- O lote é de **meio de quadra**, com frente para a Rua das Garças e fundos para a faixa verde comum do condomínio (caso §3) **(a)**. O único acesso documentado é pela frente. O acesso pelos fundos atravessaria área comum do condomínio. **Não há documento que o autorize**, então não o presumo **(c: condomínio)**.
- Portão, rebaixo de meio-fio, passeio, postes e PVs existentes: **não constam no dossiê** **(c)**. O COE Art. 35 §§2º-3º proíbe degrau, rampa e portão fora do alinhamento e só admite rebaixo de meio-fio onde for estritamente necessário (via Skill de levantamento §4) **(b)**. Por isso o levantamento da testada é condição para posicionar o acesso de veículos (Peça 2 §1 e §2.4).
- Acesso de pedestres e de serviço: **não constam** **(c)**.

**Vizinhança imediata**
- **Esquerda: Lote 16.** O muro dele avança sobre a linha do PAL (5.2) **(a)**. Os afastamentos e as construções do vizinho em relação à divisa **não constam** **(c)**.
- **Direita:** o confrontante **não é identificado no dossiê** (número, construções, muro) **(c)**. O DULI exige os confrontantes com numeração (Skill de levantamento §3, item 5) **(b)**.
- **Fundos:** faixa verde comum do condomínio, com 12 m de largura (5.5) **(a)**.
- Muros de divisa (tipo, altura, cota) e afastamentos das casas vizinhas: **não constam** **(c)**. Interessam também a Baumgart, pelo risco de recalque nos vizinhos durante o estaqueamento (Skill `rebaixamento-...` §6) **(b)**. A NBR 6492:2021 5.1.1 a) e c) pede plantas cadastrais da vizinhança e cortes/elevações do terreno com as edificações vizinhas (Skill `nbr6492-...` §2) **(b) [v2]**.

**Corpo hídrico**
- Lago "aproximadamente 1 ha", contornado por faixa verde de 12 m. A margem fica a **12,00 m** da divisa de fundos (5.5 e planta anexa) **(a)**.
- O memorial de 2009 diz "**sem ligação** com o sistema lagunar" (5.5). O caseiro relata que o lago "enche e baixa duas vezes por dia" e que uma "manilha grande" o liga ao canal (5.9) **(a)**. **As duas fontes se contradizem.** O memorial é peça de venda de 2009 e o relato é observação recente, mas não prova. Não decido entre elas. Isso se resolve com medição (régua ou marégrafo para oscilação ≥ 5 cm, DL 9.760 Art. 2º p.ú.) e com resposta da SPU e da SMAC. Se a ligação ao canal se confirmar, entra também a LC 270 Art. 216, V (lagoas do sistema da Barra/Recreio, "seus canais, suas APPs e faixas marginais"), que é o achado do Kelsen na R2 **(b)/(c)**.
- O **espelho d'água não foi levantado** (5.2) **(a)**. A área medida é o que decide a dispensa de APP (< 10.000 m²: LC 270 Art. 215 §2º; Lei 12.651 Art. 4º §4º; parecer P5). "Aproximadamente 1 ha" não prova "inferior a" **(b)**. A Skill `decreto3046-...` §6 diz que M1 e M2 "nunca se presumem" **(b)**.
- **[v2] Regime de marés e áreas alagáveis.** A NBR 6492:2021 pede, no Levantamento, o regime de marés com fonte e as áreas alagáveis na planta (Skill `nbr6492-...` §2, linha LV-ARQ; §3: "em lote lindeiro a lago/lagoa na Barra/Recreio, isso é dado obrigatório do relatório"). **O dossiê não traz nenhum dos dois:** só o relato do caseiro (5.9), que não é medição. Itens T14, T19 e T22 **(c)**.
- APP (SMAC), FMP (INEA) e terreno de marinha (SPU) são **três questões diferentes, com três donos diferentes** (parecer §2.4 H1/H2/H3). Este levantamento **não resolve nenhuma delas** **(c)**.

---

## 7. Complementação do levantamento: encomenda ao topógrafo, vistoria e relatórios

Base: checklist da Skill de levantamento §5 (para o DULI) e **[v2]** jogo do LV-ARQ da NBR 6492:2021 5.1 (Skill `nbr6492-...` §2 e §4). **Quem encomenda e confere:** Oscar, via Lúcio. **Quem contrata:** o cliente. **Quem assina:** o responsável técnico de cada item.

| # | Item a levantar | Quem fornece | Por quê (fonte) |
|---|---|---|---|
| T1 **[v2]** | Planialtimétrico **cadastral** com **curvas de nível a cada 1,00 m**. A classe e a precisão do levantamento ficam pela NBR 13133, que **não li** (Skill de levantamento R1) | Topógrafo | NBR 6492:2021 5.1.1 b) (Skill `nbr6492-...` §2 e §3); DULI, Planta de situação item 8 (Skill de levantamento §3) |
| T2 | **RN do meio-fio** na testada, com a cota escrita na planta | Topógrafo | DULI, Planta de situação item 8 e Cortes item 4 (Skill de levantamento §3) |
| T3 | Amarração da referência do condomínio (+3,20 m) ao referencial oficial | Topógrafo | LC 270 Art. 458 (parecer, linha 19) |
| T4 | Cota do terreno atual em malha, **perfil natural** e sinais de aterro | Topógrafo | DULI, Cortes itens 3 e 6; Skill de levantamento §4; atrito negativo (Skill de fundações, M4) |
| T5 | Coordenadas dos 4 vértices e ângulos; locação da **linha do PAL** e posição do muro do Lote 16 em relação a ela | Topógrafo | Prova da perda de 28,20 m² (§2) |
| T6 | Alinhamento com **nº do PAA** (o cliente fornece, se tiver) e **largura do passeio** | Topógrafo + cliente | DULI, Planta de situação item 2 (Skill §3; R3: o canal oficial do PAA/PAL não foi verificado) |
| T7 | Postes (anotar se estão na mesma calçada ou do outro lado), PVs, PVIs, rebaixos e portões existentes, árvores do passeio, drenagem existente | Topógrafo | DULI, Planta de situação item 6; COE Art. 35 (Skill §4); NBR 6492 5.1.1 b) |
| T8 | **Casa:** contorno, projeção, cota de piso | Topógrafo | Demolição; DULI em amarelo |
| T9 | **Edícula:** contorno, área, altura, vãos, distância a cada divisa | Topógrafo | Peça 2 §4.1 (sem a área não se quantifica o que ela consome da projeção) |
| T10 | **Piscina:** contorno, dimensões, **profundidade**, cota da borda e do fundo, estado | Topógrafo; estado e estanqueidade por laudo de Baumgart/Cardozo | Peça 2 §4.2 |
| T11 | **Árvores:** locação, espécie, DAP, copa, altura (o estado fitossanitário vem do laudo de profissional habilitado, pela Skill `remocao-...` §4) | Topógrafo + profissional habilitado (Glaziou) | Peça 2 §4.3 e §2.4 (alternativa A da garagem) |
| T12 | Confrontantes com número; muros de divisa e construções vizinhas encostadas ou próximas | Topógrafo | DULI, Planta de situação item 5; vistoria cautelar (Skill `rebaixamento-...` §6) |
| T13 | **Espelho d'água do lago:** contorno e área medida; margem em relação à divisa de fundos; manilha (posição e cota). Depende de autorização do condomínio, porque é área comum | Topógrafo, com autorização do condomínio | Lei 12.651 Art. 4º §4º; LC 270 Art. 215 §2º (parecer P5 e §5.4) |
| T14 | Régua/marégrafo no lago, para provar ou afastar oscilação ≥ 5 cm | Topógrafo | DL 9.760 Art. 2º p.ú. (parecer P5) |
| T15 **[v2]** | **Norte verdadeiro** na planta e **calçamento** (tipo e estado do passeio e da via). Insolação, ventos e ruído passaram para T18 e T20 | Topógrafo (norte); vistoria (calçamento) | POP-PROJ-01, Seção 3 (patch de 27/08); NBR 6492 5.1.1 b) (norte) |
| T16 | Arquivo DWG/DXF georreferenciado, para entrar no Revit sem redesenho | Topógrafo | Skill de levantamento §5 |
| T17 | **Sondagem:** posição dos 3 furos de 2024 em relação ao lote; data da medição do NA; verificar se 3 furos bastam e onde ficam frente à projeção futura. A decisão é de Baumgart/Cardozo | Baumgart/Cardozo | Skill de fundações §6 e R7 (NBR 8036: mínimo de 3 furos para projeção entre 200 e 400 m²; reforço local de 1 furo a cada 100–150 m²); 5.7 |
| **T18 [v2]** | **Dados climáticos com fonte citada:** temperaturas, pluviosidade, insolação (trajetória solar sobre o lote, sombras das vizinhas e das 3 árvores) e regime de ventos | Oscar compila de fonte oficial citada, via Lúcio | NBR 6492:2021 5.1.2, dados ambientais (Skill `nbr6492-...` §2) |
| **T19 [v2]** | **Regime de marés** com fonte (régua de T14 + fonte oficial citada), amplitude e cotas máxima e mínima do lago no referencial do levantamento | Topógrafo (medição) + Oscar (fonte) | NBR 6492:2021 5.1.2 (Skill `nbr6492-...` §2 e §3); 5.9 |
| **T20 [v2]** | **Poluição** do ar, do solo, da água e sonora, cada uma com **responsável e método** declarados (ruído: medição; solo: atenção a aterro de origem desconhecida, T4; água: lago e lençol) | Profissional habilitado contratado pelo cliente; Oscar especifica o escopo | NBR 6492:2021 5.1.2, dados ambientais (Skill `nbr6492-...` §2) |
| **T21 [v2]** | **Dados urbanísticos:** uso do entorno (lotes vizinhos, área comum, portaria), infraestrutura existente (água, esgoto, drenagem, energia, gás, telecom) e tráfego (via interna do condomínio, horários de obra admitidos) | Vistoria (Oscar) + concessionárias + condomínio | NBR 6492:2021 5.1.2, dados urbanísticos (Skill `nbr6492-...` §2) |
| **T22 [v2]** | **Áreas alagáveis** do lote e da faixa verde: marcas de cheia, cota máxima atingida pelo lago, pontos de acúmulo, saída da drenagem do lote | Topógrafo + vistoria + condomínio (histórico) | NBR 6492:2021 5.1.1 b) (Skill `nbr6492-...` §2); Peça 2 §4.2 (risco de alagamento) |
| **T23 [v2]** | **Registro fotográfico com pontos de vista locados em planta** (testada, as 3 árvores, edícula e janela, piscina, muro do Lote 16, divisas, faixa verde e lago, manilha) | Oscar, na vistoria | NBR 6492:2021 5.1.2 (Skill `nbr6492-...` §2); critério 1 do enunciado ("cotas/fotos/croquis"); POP-PROJ-01, conclusão do Levantamento (conforme instrução de Lúcio de 06/10; o POP não foi relido nesta rodada) |
| **T24 [v2]** | **Plantas cadastrais da vizinhança** e **cortes/elevações do terreno com as edificações existentes e vizinhas** | Topógrafo | NBR 6492:2021 5.1.1 a) e c) (Skill `nbr6492-...` §2) |
| **T25 [v2]** | **Divisas de matrícula, áreas de preservação e servidões** na planta (a matrícula 5.1 não menciona servidão; confirmar com a certidão atualizada) | Topógrafo + cliente/advogado (certidão) | NBR 6492:2021 5.1.1 b) (Skill `nbr6492-...` §2); 5.1 |

### 7.1 [v2] Jogo do Levantamento pela NBR 6492:2021, 5.1: item exigido × situação no dossiê

Fonte do que é exigido: Skill `nbr6492-2021-memoriais-por-etapa-projeto` §2 (linha LV-ARQ) e §3 (nota LV), lida por Lúcio na norma em 06/10/2026 **(b)**. Fonte do que existe: dossiê 5.1 a 5.15 **(a)**.

| Item exigido (NBR 6492:2021) | Situação no dossiê | Complementação |
|---|---|---|
| 5.1.1 a) Plantas cadastrais da vizinhança | Não consta. Só se sabe que o Lote 16 tem muro que avança (5.2) | T12, T24 |
| 5.1.1 b) Planta planialtimétrica: curvas a cada metro | Não consta (5.2 é só perímetro) | T1 |
| 5.1.1 b) Corpos hídricos | Lago só pelo memorial (5.5); espelho "não levantado" (5.2) | T13 |
| 5.1.1 b) Áreas alagáveis | Não consta | T22 |
| 5.1.1 b) Árvores | Existência e faixa (caso §3); locação não | T11 |
| 5.1.1 b) Construções existentes | Existência (caso §3) e distância da edícula à divisa (5.2); contornos não | T8, T9, T10 |
| 5.1.1 b) Postes, drenagem | Não consta | T7 |
| 5.1.1 b) Divisas de matrícula | Medidas do título (5.1) e locais (5.2); vértices e PAL não | T5 |
| 5.1.1 b) Áreas de preservação e servidão | Preservação: H1/H2/H3 em aberto (parecer §2.4); servidão não mencionada | T13, T14, T25 |
| 5.1.1 b) Norte | Não consta | T15 |
| 5.1.1 c) Plantas, cortes e elevações do terreno com edificações existentes e vizinhas | Não consta | T24 |
| 5.1.2 Relatório de topografia | Parcial: só o 5.2 (perímetro e área) | T1 a T7 |
| 5.1.2 Relatório de sondagem | Existe (5.7: 3 furos, NA 0,90 m, argila mole 2,5–9,0 m, areia abaixo de 11 m); posição dos furos e data do NA não | T17 |
| 5.1.2 Relatório de vizinhança | Não consta | T12, T21, T24 |
| 5.1.2 Dados ambientais: temperaturas, pluviosidade, insolação, ventos | Não consta | T18 |
| 5.1.2 Dados ambientais: **regime de marés, com fonte** | Só relato não técnico (5.9) | T14, T19 |
| 5.1.2 Dados ambientais: poluição do ar, do solo, da água e sonora, com responsável e método | Não consta | T20 |
| 5.1.2 Dados urbanísticos: uso do entorno, infraestrutura, tráfego | Não consta (só que o condomínio tem 46 lotes unifamiliares, 5.4) | T21 |
| 5.1.2 Dados legislativos: TO, CA, gabarito, alinhamento, recuos; prefeitura, bombeiros, concessionárias, patrimônio | **Respondido pela Etapa 01** (parecer §1 linhas 1–24, §2 e §4, incluindo CBMERJ e APAC). Alinhamento com nº do PAA não consta | Remeto à Etapa 01; PAA em T6 |
| 5.1.2 **Registro fotográfico com pontos de vista** | **Não existe** (o ensaio não tem visita) | T23 |

**Conclusão [v2]:** pela NBR 6492:2021, o Levantamento desta etapa está **incompleto**. Só os dados legislativos (Etapa 01) e a sondagem (5.7, com ressalvas) estão cobertos. O resto depende de T1 a T25. Nada disso é inventado aqui.

---

## 8. Skills e fontes usadas nesta peça

- `levantamento-topografico-cadastral-orientado-duli-licin-rj`: §2 (os 13 parâmetros do Art. 3º contra o dado de campo; linha III: cota de soleira = cota de implantação), §3 (o que o DULI exige), §4 (aterro, título × medida, passeio, árvore), §5 (checklist), R1/R2/R3.
- **[v2]** `nbr6492-2021-memoriais-por-etapa-projeto`: §2 (linha LV-ARQ: 5.1.1 a)-c) e 5.1.2), §3 (nota LV: curvas a cada metro, marés e áreas alagáveis obrigatórias em lote lindeiro a lago), §4 (jogo mínimo do LV-ARQ). **A frase da v1 "Não usei nenhuma Skill de NBR 6492 'memoriais por etapa'" foi retirada: a Skill se aplica e foi usada.**
- **[v2]** `varandas-nao-computaveis-ate-to-coes-lc198-rj`: §4.1 (limite das varandas no croqui; detalhe na Peça 2 §2.5).
- `decreto3046-81-lc270-2024-licin-barra-recreio`: §4 (APP e marinha), §6 (M1/M2 nunca se presumem; **[v2]** M3 e complemento XIV).
- `remocao-arvores-smac-fpj-autorizacao-compensacao-rj`: §4.
- `fundacoes-solos-moles-lencol-freatico-barra-recreio`: §6, R7, M4.
- `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`: §6.
- Etapa 01: parecer do Hely (§§1, 2.1–2.4, 5.2, 5.4) e auditoria do Kelsen (R1, R2, ERRATA 4.1). Etapa 02: enunciado (5.11 a 5.15) **[v2]**, Mascaró v8 §1, §6.4 e §8, Villaça v9 §5.

## 9. Declaração [v2]

Ensaio Sombra 003, caso 100% fictício. Nada foi protocolado, enviado ou consultado em órgão nenhum. **Não abri, não listei, não li e não citei nada em `_gabaritos_LACRADO\`.** Nesta rodada li o `etapa_03_levantamento\parecer_bardi.md` por ordem expressa de Lúcio (06/10/2026), para corrigir a v1. Não usei Glob nem Grep na pasta do ensaio: só Read por caminho exato. A v1 não foi apagada nem editada. Esta peça é análise preliminar, sujeita à auditoria de Lúcio.

— Oscar, 06/10/2026 (v2)
