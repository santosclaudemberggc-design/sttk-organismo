# Custo de Obra v2 — Ensaio 003, Etapa 02 (Viabilidade) — Lote 17, Reserva das Garças

**Agente:** Mascaró (Custo de Obra), equipe de Villaça
**Pedido de:** Villaça, 02/10/2026 (correção após reprovação da v1 por Claudemberg)
**Data de acesso de todas as fontes web:** 02/10/2026.
**Situação:** entrega de Agente para auditoria de Villaça. Não é orçamento, não é custo fechado, não vai a cliente.

> **ENSAIO — 100% FICTÍCIO.** Ninguém foi contatado. `_gabaritos_LACRADO/` não foi aberto. Perguntas que eu faria num caso real estão na seção 10.

**O que muda em relação à v1** (`../custo_obra_mascaro_003.md`, mantida intacta): (1) a base do CUB deixa de ser a área computável e passa a ser a **área equivalente da NBR 12721**, em faixa; (2) o **elevador/plataforma de D. Lourdes** entra nos itens fora do CUB; (3) checklist completo da Skill §2.4, item a item; (4) demolição com piso mecanizado (R$ 25.200); (5) preço SINAPI de hélice contínua achado (média nacional, não RJ); (6) efeito da garagem coberta na TO. Tudo o que a v1 acertou (CUB, INCC, BDI, leitura da proposta 5.12, conta do Rodrigo) está mantido aqui, refeito sobre a nova base.

**Skill aplicada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.0 (ativa-com-ressalva: NBR 12721 não lida no oficial; coeficientes vêm de fonte secundária — herdo essa ressalva).

**Rótulos:** **[FP]** fonte primária lida por mim; **[ECF]** estimativa com fonte (conta minha, fragilidade dita); **[NC]** não calculável (digo o que faltaria); **[DOC]** número do Dossiê do caso.

---

## 1. Premissas de área (fixadas por Villaça, porque Lúcio ainda não desenhou)

| Cenário | Área computável [DOC/Legal] | Não computável (varandas + garagem coberta) | Área construída de trabalho |
|---|---|---|---|
| **S1 / H0** (adotado) | 457,44 m² | 42,56 a 62,56 m² | **500,00 a 520,00 m²** |
| S2 (divisa regularizada) | 480,00 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **522,56 a 542,56 m²** |
| S3 / H1 (APP do lago) | 297,28 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **339,84 a 359,84 m²** |

- A linha **520 m² do programa só existe em H0** (é o teto da faixa do S1). Em H1/S3 o programa de 520 m² **não cabe**: o teto de trabalho é 359,84 m² (faltam 160,16 m²).
- CAB = CAM = 1,0: não há cenário com outorga (OODC R$ 0, v1 e Etapa 01). Não recalculei nenhum parâmetro legal.
- Padrão: alto. Casa de 2 pavimentos. Obra prevista para mai/2027.
- Premissa minha, declarada: a não computável é toda "varanda/garagem coberta". O piso usa o menor coeficiente provável (0,50, garagem por analogia, Skill §2.3); o teto trata tudo como 1,00 (Skill §2.2). Varanda pura teria 0,75–1,00, então o piso real tende a ficar um pouco acima do piso daqui.

---

## 2. Benchmark — CUB/m² Sinduscon-Rio, setembro/2026 [FP] (igual à v1)

- **R-1 Padrão Alto: R$ 3.691,68/m²** (emitido em 29/09/2026). https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
- R-1 Normal R$ 2.990,86 e R-1 Baixo R$ 2.476,02 ficam só como referência. Pela Skill §2.5 / macete M3, **não aplico padrão Normal a casa de alto padrão**; a linha "R-1 Normal" da v1 sai da conta principal.
- Tendência 2026 (Relatório 14, R8-N): +4,0% no ano até set, salto em maio (+2,54%; mão de obra +4,42%) [FP, conta minha] — v1 §2.

---

## 3. Tratamento da casa de 2 pavimentos (Skill §2.5)

- R-1 da NBR 12721 é residência **térrea**. Não há projeto-padrão CUB de sobrado unifamiliar. Uso **R-1 Alto como proxy declarado** (extrapolação).
- Não uso R8-N como base de casa.
- **Item [NC] "efeito 2 pavimentos":** escada, laje de piso entre pavimentos e estrutura mais carregada não estão no R-1. **Sentido: o custo real tende a ser MAIOR** que o calculado aqui. Não achei percentual citável; não apliquei acréscimo inventado.

---

## 4. Área equivalente (NBR 12721) × CUB R-1 Alto — conta aberta por linha

Fórmula (Skill §2.2): piso = computável × 1,00 + não computável mínima (42,56) × 0,50; teto = construída máxima × 1,00. Linha de comparação: construída de trabalho × 1,00.

### 4.1 Áreas

| Cenário | Linha | Base de área declarada | Conta | Área (m²) |
|---|---|---|---|---|
| S1/H0 | **Piso equivalente** | computável ×1,00 + não comp. mín. ×0,50 | 457,44 + 42,56 × 0,50 = 457,44 + 21,28 | **478,72** |
| S1/H0 | **Teto equivalente** | construída máxima ×1,00 | 520,00 × 1,00 | **520,00** |
| S1/H0 | Comparação | construída de trabalho ×1,00 | 500,00 a 520,00 | 500,00 a 520,00 |
| S2 | **Piso equivalente** | idem | 480,00 + 21,28 | **501,28** |
| S2 | **Teto equivalente** | construída máxima ×1,00 | 542,56 × 1,00 | **542,56** |
| S2 | Comparação | construída de trabalho ×1,00 | 522,56 a 542,56 | 522,56 a 542,56 |
| S3/H1 | **Piso equivalente** | idem | 297,28 + 21,28 | **318,56** |
| S3/H1 | **Teto equivalente** | construída máxima ×1,00 | 359,84 × 1,00 | **359,84** |
| S3/H1 | Comparação | construída de trabalho ×1,00 | 339,84 a 359,84 | 339,84 a 359,84 |

### 4.2 Custo CUB puro (set/2026) — área × R$ 3.691,68 [FP no índice; ECF na base de área]

| Cenário | Linha | Conta | R$ | Conferência (2ª via) |
|---|---|---|---|---|
| S1 | Piso equiv. | 478,72 × 3.691,68 | **1.767.281,05** | 480 × 3.691,68 = 1.772.006,40 − 1,28 × 3.691,68 (4.725,35) = 1.767.281,05 ✔ |
| S1 | Teto equiv. | 520,00 × 3.691,68 | **1.919.673,60** | 500 × 3.691,68 = 1.845.840,00 + 20 × 3.691,68 (73.833,60) ✔ |
| S1 | Comparação (construída 500) | 500,00 × 3.691,68 | 1.845.840,00 | ✔ |
| S2 | Piso equiv. | 501,28 × 3.691,68 | **1.850.565,35** | 1.845.840,00 + 4.725,35 ✔ |
| S2 | Teto equiv. | 542,56 × 3.691,68 | **2.002.957,90** | 1.919.673,60 + 22,56 × 3.691,68 (83.284,30) ✔ |
| S2 | Comparação (construída 522,56) | 522,56 × 3.691,68 | 1.929.124,30 | 1.919.673,60 + 2,56 × 3.691,68 (9.450,70) ✔ |
| S3 | Piso equiv. | 318,56 × 3.691,68 | **1.176.021,58** | 300 × 3.691,68 (1.107.504,00) + 18,56 × 3.691,68 (68.517,58) ✔ |
| S3 | Teto equiv. | 359,84 × 3.691,68 | **1.328.414,13** | 60 × 3.691,68 (221.500,80) − 0,16 × 3.691,68 (590,67) = 220.910,13 + 1.107.504,00 ✔ |
| S3 | Comparação (construída 339,84) | 339,84 × 3.691,68 | 1.254.580,53 | 1.328.414,13 − 73.833,60 ✔ |

### 4.3 Quanto a v1 subestimava (S1)

v1 = 457,44 × 3.691,68 = **R$ 1.688.722,10** (área computável).
- Contra o piso equivalente: 1.767.281,05 − 1.688.722,10 = **R$ 78.558,95** (= 21,28 × 3.691,68 ✔).
- Contra o teto equivalente: 1.919.673,60 − 1.688.722,10 = **R$ 230.951,50** (= 62,56 × 3.691,68 ✔).
- Ou seja, só no CUB puro a v1 subestimava o S1 em **R$ 78,6 mil a R$ 231,0 mil (4,7% a 13,7%)**; depois de BDI e INCC, em ~R$ 98 mil a ~R$ 301 mil (ver 5.2).

---

## 5. Cadeia completa: CUB → BDI → INCC-M → + demolição

Parâmetros (mesmos da v1):
- **BDI** TCU, Acórdão 2622/2013-Plenário, "Construção de Edifícios": 20,34% (1º quartil) a 25,00% (3º quartil) [ECF, extrapolação: obra pública, 2013].
- **INCC-M** set/2026 → mai/2027: **+3,9% a +4,4%** (dois métodos, v1 §5.2) [ECF, extrapolação do passado]. Fator usado no teto: 1,0436.
- **Demolição só da casa** (~180 m²), faixa mecanizada: 180 × R$ 140–300/m² = **R$ 25.200 a R$ 54.000** [ECF, fonte fraca — Cronoshare, média nacional]. Corrijo o piso da v1 (R$ 5.400, manual) para R$ 25.200: a própria fonte separa manual (R$ 30–90/m²) e mecanizada (R$ 140–300/m²), e uma casa de ~180 m² + edícula + piscina, num lote de condomínio com prazo, é demolição mecanizada. A fonte sustenta a faixa; não sustenta a escolha do método (é leitura minha).

Piso = CUB piso × 1,2034 × 1,039 + 25.200. Teto = CUB teto × 1,25 × 1,0436 + 54.000.

| Cenário | Linha | CUB puro | × BDI | × INCC | + demolição | **Total (mai/27)** |
|---|---|---|---|---|---|---|
| S1/H0 | Piso | 1.767.281,05 | 2.126.746,02 | 2.209.689,11 | + 25.200 | **2.234.889,11** |
| S1/H0 | Teto | 1.919.673,60 | 2.399.592,00 | 2.504.214,21 | + 54.000 | **2.558.214,21** |
| S2 | Piso | 1.850.565,35 | 2.226.970,34 | 2.313.822,18 | + 25.200 | **2.339.022,18** |
| S2 | Teto | 2.002.957,90 | 2.503.697,38 | 2.612.858,59 | + 54.000 | **2.666.858,59** |
| S3/H1 | Piso | 1.176.021,58 | 1.415.224,37 | 1.470.418,12 | + 25.200 | **1.495.618,12** |
| S3/H1 | Teto | 1.328.414,13 | 1.660.517,66 | 1.732.916,23 | + 54.000 | **1.786.916,23** |

Conferência por fator único: piso 1,2034 × 1,039 = 1,2503326; teto 1,25 × 1,0436 = 1,3045.
S1 piso 1.767.281,05 × 1,2503326 = 2.209.689,11 ✔; S1 teto 1.919.673,60 × 1,3045 = 2.504.214,21 ✔; S2 teto 2.002.957,90 × 1,3045 = 2.612.858,58 ✔ (dif. de centavo de arredondamento); S3 teto 1.328.414,13 × 1,3045 = 1.732.916,23 ✔; S3 piso 1.176.021,58 × 1,2503326 = 1.470.418,13 ✔.

### 5.2 Comparação com a v1 (S1)
v1: R$ 2.116.864 a R$ 2.256.938. v2: **R$ 2.234.889 a R$ 2.558.214**. Diferença: +R$ 118.025 no piso (base de área +R$ 98,2 mil após BDI/INCC, demolição +R$ 19.800) e +R$ 301.276 no teto.

### 5.3 Contra o teto da família (R$ 4,2 milhões) — só S1
Sobram **R$ 1.641.786 a R$ 1.965.111** (4.200.000 − 2.558.214,21; 4.200.000 − 2.234.889,11) para TODOS os itens da seção 6 que não têm valor somado. **Continuo sem poder afirmar que cabe ou não cabe**: o maior item aberto (fundação em argila mole com NA a 0,90 m) é o que mais varia.

---

## 6. Itens fora do CUB — checklist completo (Skill §2.4)

| # | Item | Valor | Rótulo | Fonte / o que faltaria |
|---|---|---|---|---|
| 1 | **Fundação profunda** (estaca hélice contínua, provável pela sondagem 5.7: NA 0,90 m, argila mole 2,5–9 m, areia compacta só abaixo de 11 m) | Total: — . Preço unitário achado: **SINAPI 100651, hélice contínua Ø 30 cm: R$ 139,38/m; SINAPI 100652, Ø 50 cm: R$ 255,98/m** (07/2026, média nacional, não desonerado, inclui concreto fck 30, bombeamento e armadura mínima; **exclui mobilização/desmobilização**; 100651 válida até 24 m) | **[NC]** no total; **[ECF]** no unitário | orcamentor.com (agregador do SINAPI): https://orcamentor.com/composicao/100651/ e https://orcamentor.com/composicao/100652/. **Teste de consistência (aprendizado da v1):** concreto Ø 30 = 0,0707 m³/m × R$ 587,50 (Sinduscon-Rio, preços medianos set/26) = R$ 41,5/m < R$ 139,38 ✔; Ø 50 = 0,1963 m³/m × 587,50 = R$ 115,3/m < R$ 255,98 ✔. Consistente — ao contrário do ORSE descartado na v1. **Não é preço RJ** (o agregador só mostra média nacional; preço RJ fica no aplicativo/planilha SINAPI-RJ, não lido). Ø 40 cm não localizada (código 100650 deu 404). Só para ordem de grandeza: 1 estaca de 16 m custaria R$ 2.230 (Ø 30) a R$ 4.096 (Ø 50) sem mobilização — **não multiplico por nº de estacas porque não existe nº**. Faltaria: projeto de Baumgart (nº, Ø, comprimento, blocos, baldrames), mobilização, preço SINAPI-RJ. **Pergunta (Regramento Art. 8º):** blocos de coroamento e baldrames cabem na escavação máxima de 1,20 m? Para Baumgart/Kelsen. |
| 2 | **Rebaixamento de lençol / esgotamento** (NA 0,90 m) | — | **[NC]** | Excluído do CUB [FP]. Depende de cota de blocos, poço do elevador e piscina. Skill `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` (Saturnino). Faltaria projeto de fundação e cotas. |
| 3 | **Elevador / plataforma elevatória para D. Lourdes** (81 anos, cadeirante, casa de 2 pavimentos, 2 paradas) | Plataforma simples **R$ 25.000–45.000**; plataforma estruturada **R$ 45.000–80.000**; elevador compacto **R$ 95.000–180.000**; obra civil à parte **R$ 18.000–90.000**. Faixa de trabalho com obra civil: **plataforma R$ 43.000–170.000; elevador R$ 113.000–270.000** | **[ECF], fonte FRACA** | Monitor do Mercado, "Quanto custa instalar um elevador residencial para ligar 2 andares de uma casa em 2026...", 24/08/2026: https://monitordomercado.com.br/economia-2/420300-quanto-custa-instalar-um-elevador-residencial-para-ligar-2-andares-de-uma-casa-em-2026-e-o-que-precisa-ser-preparado-antes-da-montagem/ . **Fragilidade:** portal de notícias, o próprio texto chama as faixas de "referências ilustrativas", sem região nem fabricante; recomenda 3 cotações. Não achei tabela de fabricante nem fonte institucional. Fora do CUB [FP: "elevador(es)"; plataforma por leitura da Skill §2.4, lado conservador]. **Risco técnico, não decisão minha:** poço/rebaixo da plataforma ou do elevador fica abaixo do piso, com **NA a 0,90 m** (poço estanque, subpressão, esgotamento) e pode esbarrar no **Regramento Art. 8º** (escavação > 1,20 m vedada) — pergunta para Baumgart/Kelsen. Plataforma de rebaixo raso/sem poço reduziria o conflito. Norma da plataforma (NBR ISO 9386-1) não lida. |
| 4 | **Piscina nova** (até 1,60 m) | — | **[NC]** | Dimensão não definida (Lúcio). Faixas de blog sem método não uso. NA 0,90 m pede piscina estanque e verificação de subpressão (Cardozo). |
| 5 | **Paisagismo** | — | **[NC]** | Sem projeto (Glaziou). Pedido da família de remover ipê/amendoeiras não é custo meu (é Legal/ambiental). |
| 6 | **Ar-condicionado** | — | **[NC]** | Sem projeto nem carga térmica. |
| 7 | **Automação** | — | **[NC]** | Sem escopo. |
| 8 | **Projetos e aprovações** (arquitetura, estrutura, fundação, instalações, especiais; Prefeitura; Comissão de Obras) | — | **[NC]** | Tabela de Honorários CAU/BR oficial não lida (de novo, nesta rodada). Taxa da Comissão de Obras (Regramento Art. 9º) sem valor no Dossiê. |
| 9 | **Ligações definitivas** (Light, água/esgoto, gás) | — | **[NC]** | Sem carga nem orçamento de concessionária. |
| 10 | **Sondagem complementar** | — | **[NC]** | Profundidade final dos 3 furos de 2024 não informada; estaca de 12–20 m pede furo até a ponta + margem. Sem cotação citável. |
| 11 | **Impostos, taxas e emolumentos** (ISS da obra, habite-se, averbação) | — | **[NC]** | Excluídos do CUB [FP]. Não levantados. |
| 12 | **Demolição** — casa | **R$ 25.200–54.000** | **[ECF], fonte fraca** | Já somada na seção 5. Cronoshare, 02/01/2026: https://www.cronoshare.com.br/quanto-custa/demolir-casa |
| 12b | Demolição — edícula, piscina existente, caçamba/destinação de entulho | — | **[NC]** | Faltariam área da edícula, volume da piscina e cotação local com destinação de resíduos. |
| 13 | **Acabamento acima do memorial R-1 Alto** | — | **[NC]** | Sem fonte citável. Sentido: aumenta. |
| 14 | **Efeito 2 pavimentos** (escada, laje entre pisos, estrutura) | — | **[NC]** | Seção 3. Sentido: aumenta. |
| 15 | **BDI / remuneração do construtor** | 20,34%–25,00% | **[ECF]** | Já somado na seção 5 (TCU). |
| — | Equipamentos (bombas de recalque, aquecedores), playground, urbanização | — | **[NC]** | Excluídos do CUB [FP]; sem projeto. Terreno: já é da família (não entra). |

---

## 7. Efeito da garagem coberta na TO, em custo

Programa: garagem para 4 carros. Pela Etapa 01, só **1 vaga coberta fica fora da TO**; as demais, se cobertas, **entram na projeção de 228,72 m²**. Não sei a área da vaga — **não invento**; mostro o efeito por **10 m² de garagem coberta dentro da projeção**:

| Efeito | Conta | Valor |
|---|---|---|
| Área computável perdida no térreo | 10 m² de projeção viram garagem | **−10,00 m²** computáveis (e −10 m² do teto de 457,44 no S1) |
| CUB da área útil que deixa de existir | 10 × 1,00 × 3.691,68 | −R$ 36.916,80 |
| CUB da garagem que passa a existir | 10 × 0,50 a 0,75 × 3.691,68 | +R$ 18.458,40 a +R$ 27.687,60 |
| Saldo no CUB puro (set/26) | −36.916,80 + 18.458,40 / 27.687,60 | **−R$ 18.458,40 a −R$ 9.229,20** por 10 m² |

Leitura: o custo cai um pouco, mas **a família perde 10 m² de casa** por 10 m² de garagem coberta na projeção. Para 3 vagas cobertas além da primeira (ordem de 12,5 m² por vaga é comum, mas **não uso esse número**: peço a medida), a perda seria de várias dezenas de m² computáveis. Vaga descoberta sobre terreno teria coeficiente 0,05–0,10 (Skill §2.3) e não come TO. Coeficiente 0,50–0,75 é **analogia com garagem de subsolo** (Skill §2.3), declarada.
**Pedido:** dimensão da vaga e quantas cobertas a Lúcio; confirmação da regra de TO para vaga coberta a Kelsen.

---

## 8. Proposta 5.12 (Alicerce Prime, R$ 6.300/m²) reaplicada na área construída de trabalho

Tudo da v1 §7 permanece válido: 590 × 6.300 = 3.717.000 ✔ [DOC], mas 590 m² não cabe na lei; "chave na mão" exclui 8 itens; radier contra a sondagem (risco alto de aditivo, [NC]); 6.300 ÷ 3.691,68 = 1,7066 (70,7% acima do CUB Alto) e 36,5% acima de CUB × 1,25; n = 1, não é benchmark; reajuste INCC-M sem mês-base declarado; validade vence ~29/10/2026.

Agora aplicada à **área construída de trabalho** (base certa para preço de construtora por m² construído; premissa: a proposta cobra sobre área construída total, como os 590 m² sugerem):

| Cenário | Base de área declarada | Conta | Preço set/26 [DOC × premissa] | Em mai/27 (INCC +3,9%/+4,4%) [ECF] |
|---|---|---|---|---|
| S1/H0 | construída 500,00–520,00 | × 6.300 | **R$ 3.150.000 a 3.276.000** | R$ 3.272.850 a 3.418.834 |
| S2 | construída 522,56–542,56 | × 6.300 | **R$ 3.292.128 a 3.418.128** | R$ 3.420.521 a 3.567.158 |
| S3/H1 | construída 339,84–359,84 | × 6.300 | **R$ 2.140.992 a 2.266.992** | R$ 2.224.491 a 2.365.833 |

Contas: 500 × 6.300 = 3.150.000; 3.150.000 × 1,039 = 3.272.850; 3.276.000 × 1,0436 = 3.418.833,60; 3.292.128 × 1,039 = 3.420.521; 3.418.128 × 1,0436 = 3.567.158; 2.140.992 × 1,039 = 2.224.491; 2.266.992 × 1,0436 = 2.365.833.
A v1 aplicava 6.300 a 457,44 (R$ 2.881.872): subestimava o S1 em R$ 268.128 a R$ 394.128.

As duas vias no S1 (mai/27): CUB + BDI + INCC + demolição **R$ 2,23–2,56 mi** × proposta **R$ 3,27–3,42 mi**: divergem ~R$ 0,86–1,04 mi. Esperado: a proposta inclui fundação (radier) e acabamento "alto padrão" que o CUB não mede, e a v2 ainda não soma fundação, elevador etc.

### 8.1 Conta do Rodrigo (5.15): 520 × 6.300 = R$ 3.276.000; "sobra quase R$ 1 milhão"
- Aritmética ✔: 520 × 6.300 = 3.276.000; 4.200.000 − 3.276.000 = 924.000.
- Agora a **base de área está certa para preço** (520 m² é construída, teto do S1/H0) — **mas só em H0**. Em H1 (lago), 520 m² não cabe (teto 359,84 m²).
- Ainda não é custo da obra: (1) 520 só existe se 62,56 m² entrarem como não computáveis (decisão de Lúcio); (2) os R$ 924 mil precisam pagar os 8 não inclusos **e o elevador/plataforma de D. Lourdes** (R$ 43–170 mil de plataforma, fonte fraca, seção 6 item 3), que a proposta nem menciona; (3) radier → estacas vira aditivo; (4) mai/27: R$ 3,40–3,42 mi (3.276.000 × 1,039 = 3.403.764; × 1,0436 = 3.418.834), o que reduz a sobra para **R$ 781–796 mil**; (5) validade vence antes de existir projeto.

---

## 9. Sinalizações para Villaça encaminhar

| Para | O quê |
|---|---|
| **Baumgart / Cardozo** | Radier × sondagem; quantitativo de estacas (destrava o maior [NC]); profundidade dos furos de 2024; **blocos/baldrames × Art. 8º (1,20 m)**; **poço da plataforma/elevador × NA 0,90 m × Art. 8º**; atrito negativo com aterro da soleira +3,20 m. |
| **Kelsen** | Poço de elevador/plataforma conta como "escavação" do Art. 8º? Vaga coberta na projeção: confirmar efeito na TO. |
| **Saturnino (via Cardozo)** | Esgotamento/rebaixamento na obra e no poço. |
| **Lúcio** | Quadro de áreas por tipo (varanda, garagem, técnica) para trocar a faixa por área equivalente fechada; dimensão e nº de vagas cobertas; tipo de plataforma (com ou sem poço); dimensão da piscina. Avisar: programa de 520 m² não cabe em H1. |
| **Fiker** | Base de custo agora é construída/equivalente; preço de construtora é custo, não valor de mercado. |

## 10. Perguntas que eu faria num caso real (NÃO enviadas)

| A quem | Pergunta |
|---|---|
| Alicerce Prime | Composição do R$ 6.300/m² (BDI, fundação, acabamento), mês-base do INCC, sobre qual área cobra; preço refeito com estacas e área legal; plataforma de acessibilidade inclusa? |
| 3 fabricantes de plataforma/elevador residencial (RJ) | Preço instalado, 2 paradas, cadeira de rodas, com e sem poço, e exigência de poço |
| Topógrafo/caseiro | Área da edícula, volume da piscina existente |
| Empresa de sondagem | Profundidade final dos furos de 2024 |
| Comissão de Obras | Taxa do Art. 9º |

## 11. Lacunas e bloqueios desta execução

- NBR 12721 não lida no oficial (coeficientes secundários, ressalva da Skill).
- Preço de hélice contínua: achado SINAPI média nacional (100651/100652), **não RJ**; Ø 40 não localizado (100650 = 404).
- Elevador/plataforma: só fonte jornalística fraca; nenhuma tabela de fabricante.
- Sem % citável para sobrado sobre R-1; sem fonte para acabamento acima do memorial; BDI de obra pública; CAU/BR não lida.

## 12. Fontes (acesso 02/10/2026)

1. Sinduscon-Rio, CUB/m² set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
2. Sinduscon-Rio, Relatório 14, set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Evolucao-e-composicao-setembro-de-2026.pdf
3. Sinduscon-Rio, Preços medianos set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Precos-medianos-setembro-de-2026.pdf
4. FGV, INCC-M set/2026 [FP]: https://portal.fgv.br/noticias/incc-m-setembro-2026 ; VRI (número-índice): https://www.vriconsulting.com.br/indices/incc-m.php ; Brasil Indicadores: https://www.brasilindicadores.com.br/incc-m
5. TCU, Acórdão 2622/2013-Plenário (BDI): https://www.mpf.mp.br/o-mpf/unidades/pr-to/transparencia/licitacoes-novo/2016/12Acordao26222013BDI.pdf
6. Cronoshare, demolição (02/01/2026), fraca: https://www.cronoshare.com.br/quanto-custa/demolir-casa
7. SINAPI 100651 e 100652 via orcamentor.com (07/2026, média nacional): https://orcamentor.com/composicao/100651/ ; https://orcamentor.com/composicao/100652/
8. Monitor do Mercado, elevador/plataforma residencial 2 andares (24/08/2026), fraca: https://monitordomercado.com.br/economia-2/420300-quanto-custa-instalar-um-elevador-residencial-para-ligar-2-andares-de-uma-casa-em-2026-e-o-que-precisa-ser-preparado-antes-da-montagem/
9. Skill `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.0 (coeficientes NBR 12721 §5.7.3, fonte secundária); Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3.

---

*Declaração: ensaio 100% fictício (Ensaio Sombra 003, Etapa 02, v2). Ninguém contatado; gabarito lacrado não aberto. Nenhum número é custo fechado ou garantia. Mascaró, 02/10/2026.*
