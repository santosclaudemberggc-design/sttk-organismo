# Peça 1 — Levantamento Planialtimétrico Cadastral orientado ao DULI
## Ensaio Sombra 003, Etapa 03: Levantamento. Família Montenegro Prates (100% FICTÍCIO)

**Executor:** Oscar (Agente, Arquitetura, nível Assisted) | **Auditoria:** Lúcio (Gestor de Arquitetura)
**Data:** 06/10/2026 | **Natureza:** ANÁLISE PRELIMINAR. Num caso real, não é entregável final sem a conferência de Lúcio e o Gate do Maurício.
**Lote:** Rua das Garças, Lote 17, Quadra C, Condomínio Reserva das Garças, Recreio dos Bandeirantes (AP4). Fonte: caso §3.

**Etiquetas**
- **(a)** dado do dossiê (caso §1–§4 e 5.1 a 5.10). Dentro do ensaio, vale como verdade.
- **(b)** premissa ou mecanismo do Legal aprovado (Etapa 01: parecer do Hely e auditoria do Kelsen, incluindo a ERRATA 4.1), da Viabilidade aprovada (Etapa 02) ou de uma Skill, com a seção citada.
- **(c)** pendente ou lacuna: o que falta, quem fornece e quem decide.

---

## 0. Bloqueio de ferramenta e limite desta peça

- **Revit/Vitruvius.** Chamei `mcp__vitruvius__revit_status` antes de qualquer outra coisa. Retorno literal: `Error: No such tool available: mcp__vitruvius__revit_status`. Não há modelo nem ferramenta BIM nesta sessão, e **não simulei desenho**. Esta peça sai em texto, tabelas e um croqui descritivo com coordenadas em metros, a partir de um referencial declarado (§1).
- **Sem visita.** O POP-PROJ-01 proíbe iniciar o traço sem conferência física presencial, e o ensaio não tem visita. Tudo o que está abaixo vem do dossiê ou é conta sobre ele. Onde o dossiê não traz o dado, escrevo **"não consta no dossiê"** e o item entra na lista de complementação (§7).
- **O levantamento 5.2 não basta para o DULI.** Pela Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` §3 e §5, o DULI exige RN do meio-fio na testada, curvas de nível, perfil natural do terreno, PAA/alinhamento com número, passeio com largura, PVs/PVIs, postes, árvores e construções existentes. O 5.2 traz só o perímetro, a área, a nota sobre o muro, a distância da edícula à divisa e a cota de soleira **prevista**. O próprio topógrafo escreveu que o levantamento ficou "restrito ao perímetro do lote; espelho d'água do lago não levantado" (5.2) **(a)**. Conclusão: **o 5.2 serve de base de área e perímetro, mas não serve de base de DULI.** É preciso encomendar a complementação do §7 **(c)**.
- **Destino do DULI.** O enunciado diz que o DULI "será anexado ao projeto executivo (Etapa 15)". Não confere: o DULI é peça do Projeto Legal/LICIN (LICIN Anexo I, citado no parecer da Etapa 01, §2.1 e T8), cuja etapa é a **07 (Legal: entrada na Prefeitura e no condomínio, Kelsen/Hely)**, conforme o caso §6. Este levantamento **alimenta** o DULI da Etapa 07. Não é o DULI.

---

## 1. Referencial e croqui descritivo (aproximação retangular)

**Referencial adotado (declarado por mim, Oscar):**
- Origem **O = (0,00; 0,00)**: vértice frente-esquerda, no encontro do alinhamento com a face do **muro existente do Lote 16**. Os afastamentos se medem a partir desse muro (premissa da Etapa 01, parecer §2.1 e §5.2) **(b)**.
- Eixo **x**: ao longo da testada, da esquerda (Lote 16) para a direita. Eixo **y**: perpendicular à testada, da rua para os fundos.
- **Aproximação:** retângulo de **14,29 m × 40,00 m**, a menor largura medida pela menor lateral medida (mesmo critério do parecer §2.3) **(b)**. O lote real **não é retângulo**: frente 14,30, fundos 14,29, lateral esquerda 40,00, lateral direita 40,02 (5.2) **(a)**. O 5.2 não traz ângulos nem coordenadas dos vértices **(c)**. Por isso, toda área abaixo é aproximação. A área oficial do lote é a do topógrafo, **571,80 m²**.
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
        | A  |   9,29 × 29,00 = 269,41 m²                          |  A  x≈13,49 0,80 m da divisa
        | T  |                                                    |  T       |     direita (5.2); y e
 22,00  |-E--|- - - - - linha H1 (30 m da margem = y 22,00) - - - -|--D-------|     dimensões: não
        | S  |   ENVELOPE H1: y 6,00–22,00 → 9,29 × 16,00 = 148,64 |  I       |     constam
        | Q  |                                                    |  R       |
  6,00  |----+----------------------------------------------------+----------|
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
| Envelope H0 | x 2,50–11,79; y 6,00–35,00 | parecer §2.3; 5.4 Art. 6º | (b) |
| Linha de H1 (APP de 30 m da margem) | y = 22,00 (40,00 − 18,00) | parecer §2.4 e §5.2 ("faixa entre 22 m e 40 m da frente") | (b)/(c) |
| Margem do lago | y ≈ 52,00 (40,00 + 12,00) | 5.5, planta anexa | (a) |
| Face da edícula voltada à divisa direita | x ≈ 14,29 − 0,80 = 13,49 | 5.2 | (a) + conta |
| Casa de 1998 | **posição e dimensões: não constam no dossiê** (só "cerca de 180 m²", caso §3) | caso §3 | (a)/(c) |
| Piscina | **posição, dimensões, profundidade e cota: não constam no dossiê** | caso §3, §4 | (c) |
| Árvores (3) | "no afastamento frontal", ou seja, y entre 0 e 6,00; **x, DAP, copa e estado: não constam** | caso §3 | (a)/(c) |

> O "EXEMPLO" do enunciado ("casa de ~180 m² no meio do lote", "edícula de ~20–30 m²", "piscina talvez ~4 × 8 m nos fundos") **não é documento do dossiê**. Não uso esses valores em nenhuma conclusão. Onde aparecem, aparecem como estimativa não documental.

---

## 2. Dimensões do lote: título × medida local

| Lado | Matrícula 5.1 | Levantamento 5.2 | Diferença |
|---|---|---|---|
| Frente | 15,00 | 14,30 | −0,70 |
| Fundos | 15,00 | 14,29 | −0,71 |
| Lateral esquerda (Lote 16) | 40,00 | 40,00 | 0,00 |
| Lateral direita | 40,00 | 40,02 | +0,02 |
| **Área** | **600,00 m²** | **571,80 m²** | **−28,20 m²** |

Fontes: 5.1 e 5.2 **(a)**. O RIU (5.3) também registra 600,00 m² no cadastro **(a)**.

**Conferência das contas:**
- Retângulo pelas médias: ((14,30 + 14,29) / 2) × ((40,00 + 40,02) / 2) = 14,295 × 40,01 = **571,94 m²**. Fica 0,14 m² acima do valor do topógrafo, uma diferença compatível com o polígono não retangular. Prevalece **571,80 m²**, que é o valor medido **(a)**.
- Perda atribuída ao muro (parecer §2.1): 0,70 × 40,00 = **28,00 m²** contra 28,20 m² de diferença real **(b)**. O enunciado escreve "~0,70 m × 40 m = 28 m²". O número exato da diferença é **28,20 m²**.

**Motivo da divergência.** O topógrafo registra que o "muro da divisa lateral esquerda do vizinho (Lote 16) avança sobre a linha de projeto do PAL" (5.2) **(a)**. Ele **não mediu quanto o muro avança**. A atribuição dos 28,20 m² ao muro é inferência do Legal ("muito provavelmente", parecer §2.1) **(b)**. Para provar isso, é preciso locar a linha do PAL no terreno e cotar o muro em relação a ela **(c: topógrafo; ver §7)**.

**Área adotada: 571,80 m²**, com os afastamentos medidos a partir do muro existente. É premissa da Etapa 01 (parecer §2.1 e §5.2; Kelsen R1) e **não a reinterpreto** **(b)**. O cenário de 600,00 m² só entra se a divisa for regularizada. Essa regularização é matéria civil e registral e é **decisão do cliente com advogado** (Kelsen R1) **(c)**.

**O que vai ao DULI:** as dimensões do título **e** as medidas locais, porque há divergência (LICIN Anexo I, III, Planta de situação, item 1, citado no parecer §2.1; Skill de levantamento §3) **(b)**.

---

## 3. Altimetria e topografia

| Item | Situação no dossiê | Etiq. |
|---|---|---|
| Cota de soleira | **+3,20 m "prevista"**, referência do condomínio (5.2). **Não é cota atual.** O enunciado chama de "atual": não confere com o 5.2 | (a) |
| Referencial do +3,20 | Condominial. A amarração ao referencial oficial **não foi confirmada** (parecer, quadro linha 19) | (c) |
| Efeito legal da cota | LC 270 Art. 458 caput: cota de soleira < 3 m, ou área frágil de baixada, exige avaliação técnica do Município (parecer, linha 19 e T9). Se o +3,20 condominial corresponder a menos de 3 m no referencial oficial, o Art. 458 entra em jogo. **Quem decide: Kelsen/Hely** | (b)/(c) |
| Teto de altura com a soleira prevista | 5.4 Art. 7º: 8,50 m medidos da cota de soleira ao ponto mais alto. Conta: +3,20 + 8,50 = **+11,70 m** (referencial do condomínio), **se** a soleira ficar em +3,20 | (a)+(b) |
| Cota do terreno atual, curvas de nível, aclives e depressões | **Não constam no dossiê** | (c) |
| RN do meio-fio na testada | **Não consta** (exigido pelo DULI: Skill de levantamento §3, Planta de situação item 8; Cortes item 4) | (c) |
| Perfil natural do terreno e sinais de aterro | **Não constam** (exigidos: Skill de levantamento §3, Cortes itens 3 e 6, e §4 "terreno natural × aterro"). Qual cota vale como "natural" é decisão do Hely (Skill de levantamento, R2) | (c) |
| Aterro necessário até +3,20 | **Não calculável** sem a cota do terreno atual | (c) |
| Nível d'água | **0,90 m** abaixo da superfície, na sondagem de 2024. **Vem do 5.7, não do 5.2.** O enunciado atribui o NA ao 5.2, e isso não confere | (a) |
| Cota de piso do térreo da casa nova | É decisão de projeto (Etapa 05), amarrada à soleira. Não a fixo aqui | — |

---

## 4. Edificações existentes

| Edificação | O que o dossiê diz | O que não consta | Etiq. |
|---|---|---|---|
| **Casa de 1998** | Térrea, "cerca de 180 m²", **existente e a demolir** (caso §3). Nunca averbada (5.1). Tem Habite-se de 1999 (5.8). A demolição de ~180 m² está orçada no Mascaró v8 §6.4 | Posição, dimensões, projeção exata, cota do piso | (a)/(c) |
| **Edícula** | Churrasqueira e depósito (caso §3). Fica a **0,80 m** da divisa lateral direita, com janela voltada para a divisa (5.2). **Não consta** da planta do Habite-se (5.8) | Área, dimensões, posição em y, altura, cota | (a)/(c) |
| **Piscina** | Existe, e o cliente quer mantê-la (caso §3, §4) | Posição, dimensões, profundidade, cota da borda, estado, se aparece no Habite-se | (a)/(c) |

**Contradição do enunciado.** O resumo de entrada diz "Casa demolida (térrea 180 m²)". As fontes dizem o contrário: a casa **existe** e está **a demolir**. O caso §3 diz "para demolir a casa e construir", o 5.8 registra o Habite-se da casa e o Mascaró v8 §6.4 orça a demolição. Adoto: **casa existente, a demolir.**

**Cores do DULI para o que existe** (Skill de levantamento §5; LICIN Anexo I, IV.2): amarelo para demolir, vermelho para novo ou a legalizar, preto para existente a manter. Na premissa da Etapa 01, casa e edícula vão a amarelo **(b)**. A piscina fica **indefinida** até ser levantada (Peça 2, §4.2).

---

## 5. Vegetação de porte

| Item | Dossiê | Não consta | Etiq. |
|---|---|---|---|
| 1 ipê-amarelo + 2 amendoeiras | Ficam no afastamento frontal (caso §3; o enunciado repete) | Locação (x, y), DAP, diâmetro de copa, altura, estado fitossanitário, laudo | (a)/(c) |

O levantamento cadastral precisa trazer a posição, a espécie e o DAP de cada árvore (Skill de levantamento §4 "Árvore na testada" e §5; Skill `remocao-arvores-...` §4: "planta/croqui com localização das árvores", com responsável Glaziou/Oscar) **(b)**. A **arborização do passeio** também precisa ser levantada, porque o COE Art. 35 §4º a exige em edificação nova (via Skill de levantamento §4) **(b)/(c)**.

---

## 6. Acessos, vizinhança e corpo hídrico

**Acessos**
- O lote é de **meio de quadra**, com frente para a Rua das Garças e fundos para a faixa verde comum do condomínio (caso §3) **(a)**. O único acesso documentado é pela frente. O acesso pelos fundos atravessaria área comum do condomínio. **Não há documento que o autorize**, então não o presumo **(c: condomínio)**.
- Portão, rebaixo de meio-fio, passeio, postes e PVs existentes: **não constam no dossiê** **(c)**. O COE Art. 35 §§2º-3º proíbe degrau, rampa e portão fora do alinhamento e só admite rebaixo de meio-fio onde for estritamente necessário (via Skill de levantamento §4) **(b)**. Por isso o levantamento da testada é condição para posicionar o acesso de veículos (Peça 2, §1).
- Acesso de pedestres e de serviço: **não constam** **(c)**.

**Vizinhança imediata**
- **Esquerda: Lote 16.** O muro dele avança sobre a linha do PAL (5.2) **(a)**. Os afastamentos e as construções do vizinho em relação à divisa **não constam** **(c)**.
- **Direita:** o confrontante **não é identificado no dossiê** (número, construções, muro) **(c)**. O DULI exige os confrontantes com numeração (Skill de levantamento §3, item 5) **(b)**.
- **Fundos:** faixa verde comum do condomínio, com 12 m de largura (5.5) **(a)**.
- Muros de divisa (tipo, altura, cota) e afastamentos das casas vizinhas: **não constam** **(c)**. Também interessam a Baumgart, para o risco de recalque nos vizinhos durante o estaqueamento (Skill `rebaixamento-...` §6) **(b)**.

**Corpo hídrico**
- Lago "aproximadamente 1 ha", contornado por faixa verde de 12 m. A margem fica a **12,00 m** da divisa de fundos (5.5 e planta anexa) **(a)**.
- O memorial de 2009 diz "**sem ligação** com o sistema lagunar" (5.5). O caseiro relata que o lago "enche e baixa duas vezes por dia" e que uma "manilha grande" o liga ao canal (5.9) **(a)**. **As duas fontes se contradizem.** O memorial é peça de venda de 2009 e o relato é observação recente, mas não prova. Não decido entre elas. Isso se resolve com medição (régua ou marégrafo para oscilação ≥ 5 cm, DL 9.760 Art. 2º p.ú.) e com resposta da SPU e da SMAC. Se a ligação ao canal se confirmar, entra também a LC 270 Art. 216, V (lagoas do sistema da Barra/Recreio, "seus canais, suas APPs e faixas marginais"), que é o achado do Kelsen na R2 **(b)/(c)**.
- O **espelho d'água não foi levantado** (5.2) **(a)**. A área medida é o que decide a dispensa de APP (< 10.000 m²: LC 270 Art. 215 §2º; Lei 12.651 Art. 4º §4º; parecer P5). "Aproximadamente 1 ha" não prova "inferior a" **(b)**. A Skill `decreto3046-...` §6 diz que M1 e M2 "nunca se presumem" **(b)**.
- APP (SMAC), FMP (INEA) e terreno de marinha (SPU) são **três questões diferentes, com três donos diferentes** (parecer §2.4 H1/H2/H3). Este levantamento **não resolve nenhuma delas** **(c)**.

---

## 7. Complementação do levantamento: encomenda ao topógrafo e vistoria

Checklist da Skill de levantamento §5, aplicado ao que falta no 5.2. **Quem fornece:** topógrafo contratado pelo cliente. **Quem encomenda e confere:** Oscar, via Lúcio. **Quem assina:** o responsável técnico do topógrafo.

| # | Item a levantar | Por quê (fonte) |
|---|---|---|
| T1 | Planialtimétrico **cadastral** com curvas de nível (o intervalo fica com o topógrafo, pela NBR 13133, que não li: Skill de levantamento R1) | DULI, Planta de situação item 8 (Skill §3) |
| T2 | **RN do meio-fio** na testada, com a cota escrita na planta | DULI, Planta de situação item 8 e Cortes item 4 (Skill §3) |
| T3 | Amarração da referência do condomínio (+3,20 m) ao referencial oficial | LC 270 Art. 458 (parecer, linha 19) |
| T4 | Cota do terreno atual em malha, **perfil natural** e sinais de aterro | DULI, Cortes itens 3 e 6; Skill §4; atrito negativo (Skill de fundações, M4) |
| T5 | Coordenadas dos 4 vértices e ângulos; locação da **linha do PAL** e posição do muro do Lote 16 em relação a ela | Prova da perda de 28,20 m² (§2) |
| T6 | Alinhamento com **nº do PAA** (o cliente fornece, se tiver) e **largura do passeio** | DULI, Planta de situação item 2 (Skill §3; R3: o canal oficial do PAA/PAL não foi verificado) |
| T7 | Postes (anotar se estão na mesma calçada ou do outro lado), PVs, PVIs, rebaixos e portões existentes, árvores do passeio | DULI, Planta de situação item 6; COE Art. 35 (Skill §4) |
| T8 | **Casa:** contorno, projeção, cota de piso | Demolição; DULI em amarelo |
| T9 | **Edícula:** contorno, área, altura, vãos, distância a cada divisa | Peça 2, §4.1 |
| T10 | **Piscina:** contorno, dimensões, **profundidade**, cota da borda e do fundo, estado | Peça 2, §4.2 |
| T11 | **Árvores:** locação, espécie, DAP, copa, altura (o estado fitossanitário vem do laudo de profissional habilitado, pela Skill `remocao-...` §4) | Peça 2, §4.3 |
| T12 | Confrontantes com número; muros de divisa e construções vizinhas encostadas ou próximas | DULI, Planta de situação item 5; vistoria cautelar (Skill `rebaixamento-...` §6) |
| T13 | **Espelho d'água do lago:** contorno e área medida; margem em relação à divisa de fundos; manilha (posição e cota). Depende de autorização do condomínio, porque é área comum | Lei 12.651 Art. 4º §4º; LC 270 Art. 215 §2º (parecer P5 e §5.4) |
| T14 | Régua/marégrafo no lago, para provar ou afastar oscilação ≥ 5 cm | DL 9.760 Art. 2º p.ú. (parecer P5) |
| T15 | **Norte verdadeiro** no levantamento. Insolação, ventos dominantes, ruído e calçamento ficam para a vistoria. O dossiê não traz nada disso, e o escopo do POP-PROJ-01 exige | POP-PROJ-01, Seção 3 (patch de 27/08) |
| T16 | Arquivo DWG/DXF georreferenciado, para entrar no Revit sem redesenho | Skill de levantamento §5 |
| T17 | **Sondagem:** posição dos 3 furos de 2024 em relação ao lote; data da medição do NA; verificar se 3 furos bastam e onde ficam frente à projeção futura. A decisão é de Baumgart/Cardozo | Skill de fundações §6 e R7 (NBR 8036: no mínimo 3 furos para projeção entre 200 e 400 m²; reforço local de 1 furo a cada 100–150 m²); 5.7 |

---

## 8. Skills e fontes usadas nesta peça

- `levantamento-topografico-cadastral-orientado-duli-licin-rj`: §2 (os 13 parâmetros do Art. 3º contra o dado de campo), §3 (o que o DULI exige), §4 (aterro, título × medida, passeio, árvore), §5 (checklist, base da tabela do §7), R1/R2/R3.
- `decreto3046-81-lc270-2024-licin-barra-recreio`: §4 (APP e marinha), §6 (M1/M2 nunca se presumem).
- `remocao-arvores-smac-fpj-autorizacao-compensacao-rj`: §4.
- `fundacoes-solos-moles-lencol-freatico-barra-recreio`: §6, R7, M4.
- `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`: §6.
- Etapa 01: parecer do Hely (§§1, 2.1–2.4, 5.2, 5.4) e auditoria do Kelsen (R1, R2, ERRATA 4.1). Etapa 02: Mascaró v8 §6.4.
- Não usei nenhuma Skill de NBR 6492 "memoriais por etapa".

## 9. Declaração

Ensaio Sombra 003, caso 100% fictício. Nada foi protocolado, enviado ou consultado em órgão nenhum. **Não abri, não listei, não li e não citei nada em `_gabaritos_LACRADO\` nem qualquer arquivo `parecer_bardi*.md`.** Esta peça é análise preliminar, sujeita à auditoria de Lúcio.

— Oscar, 06/10/2026
