# Custo de Obra v3 — Ensaio 003, Etapa 02 (Viabilidade) — Lote 17, Reserva das Garças

**Agente:** Mascaró (Custo de Obra), equipe de Villaça
**Pedido de:** Villaça, 02/10/2026 (correção v3, tolerância zero, após parecer de Bardi sobre a v2)
**Data de acesso de todas as fontes web:** 02/10/2026.
**Situação:** entrega de Agente para auditoria de Villaça. Não é orçamento, não é custo fechado, não vai a cliente.

> **ENSAIO — 100% FICTÍCIO.** Ninguém foi contatado. `_gabaritos_LACRADO/` não foi aberto. As perguntas que eu faria num caso real estão na seção 10.

**O que muda em relação à v2** (`../v2/custo_obra_mascaro_003_v2.md`, mantida intacta). **Só o reajuste.** A v2 reajustava pelo INCC-M de set/2026 até mai/2027 (início da obra) e parava aí. Mas a obra vai de mai/2027 a dez/2028 (caso base: "iniciar a obra em maio/2027 e mudar até dezembro/2028"), e a proposta 5.12 reajusta pelo INCC-M durante toda a execução. A v3 reajusta também ao longo dos ~20 meses de desembolso (nova seção 5.1) e refaz as seções 4.3 (só a frase final), 5, 5.2, 5.3, 8 e 8.1. Áreas, CUB, BDI, demolição, checklist de 15 itens, plataforma, SINAPI, garagem × TO, leitura da 5.12, sinalizações e perguntas ficam **idênticos à v2**. Aluguel da família: fora do meu arquivo, não tratado.

**Skill aplicada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.0 (ativa-com-ressalva: a NBR 12721 não foi lida no texto oficial; os coeficientes vêm de fonte secundária, e herdo essa ressalva).

**Rótulos:** **[FP]** fonte primária lida por mim; **[ECF]** estimativa com fonte (conta minha, fragilidade declarada); **[NC]** não calculável (digo o que faltaria); **[DOC]** número do Dossiê do caso.

---

## 1. Premissas de área (fixadas por Villaça, porque Lúcio ainda não desenhou) — igual à v2

| Cenário | Área computável [DOC/Legal] | Não computável (varandas + garagem coberta) | Área construída de trabalho |
|---|---|---|---|
| **S1 / H0** (adotado) | 457,44 m² | 42,56 a 62,56 m² | **500,00 a 520,00 m²** |
| S2 (divisa regularizada) | 480,00 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **522,56 a 542,56 m²** |
| S3 / H1 (APP do lago) | 297,28 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **339,84 a 359,84 m²** |

- A linha **520 m² do programa só existe em H0** (é o teto da faixa do S1). Em H1/S3 o programa de 520 m² **não cabe**: o teto de trabalho é 359,84 m² (faltam 160,16 m²).
- CAB = CAM = 1,0: nenhum cenário tem outorga (OODC R$ 0, v1 e Etapa 01). Não recalculei parâmetro legal.
- Padrão alto. Casa de 2 pavimentos. **Obra de mai/2027 a dez/2028 (20 meses de desembolso)** [DOC, caso base].
- Premissa minha, declarada: toda a não computável é "varanda/garagem coberta". O piso usa o menor coeficiente provável (0,50, garagem por analogia, Skill §2.3); o teto trata tudo como 1,00 (Skill §2.2).

---

## 2. Benchmark — CUB/m² Sinduscon-Rio, setembro/2026 [FP] — igual à v2

- **R-1 Padrão Alto: R$ 3.691,68/m²** (emitido em 29/09/2026). https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
- R-1 Normal (R$ 2.990,86) e Baixo (R$ 2.476,02) ficam só como referência. Pela Skill §2.5 / macete M3, não aplico padrão Normal a casa de alto padrão.
- Tendência em 2026 (Relatório 14, R8-N): +4,0% no ano até setembro, com salto em maio (+2,54%; mão de obra +4,42%) [FP, conta minha].

---

## 3. Casa de 2 pavimentos (Skill §2.5) — igual à v2

- R-1 é residência **térrea**. Uso **R-1 Alto como proxy declarado** (extrapolação). Não uso R8-N como base de casa.
- **[NC] "efeito 2 pavimentos"** (escada, laje de piso, estrutura mais carregada): o custo real tende a ser **MAIOR**. Não achei percentual citável e não inventei acréscimo.

---

## 4. Área equivalente (NBR 12721) × CUB R-1 Alto — igual à v2

Fórmula (Skill §2.2): piso = computável × 1,00 + não computável mínima (42,56) × 0,50; teto = construída máxima × 1,00.

### 4.1 Áreas

| Cenário | Linha | Conta | Área (m²) |
|---|---|---|---|
| S1/H0 | Piso equivalente | 457,44 + 42,56 × 0,50 | **478,72** |
| S1/H0 | Teto equivalente | 520,00 × 1,00 | **520,00** |
| S2 | Piso equivalente | 480,00 + 21,28 | **501,28** |
| S2 | Teto equivalente | 542,56 × 1,00 | **542,56** |
| S3/H1 | Piso equivalente | 297,28 + 21,28 | **318,56** |
| S3/H1 | Teto equivalente | 359,84 × 1,00 | **359,84** |

Linha de comparação (construída × 1,00): S1 500–520; S2 522,56–542,56; S3 339,84–359,84.

### 4.2 CUB puro (set/2026) = área × R$ 3.691,68 [FP no índice; ECF na base de área]

| Cenário | Piso | Teto |
|---|---|---|
| S1 | 478,72 × 3.691,68 = **1.767.281,05** | 520,00 × 3.691,68 = **1.919.673,60** |
| S2 | 501,28 × 3.691,68 = **1.850.565,35** | 542,56 × 3.691,68 = **2.002.957,90** |
| S3 | 318,56 × 3.691,68 = **1.176.021,58** | 359,84 × 3.691,68 = **1.328.414,13** |

As conferências por segunda via estão na v2 §4.2 e continuam valendo.

### 4.3 Quanto a v1 subestimava (S1)
A v1 usava 457,44 × 3.691,68 = R$ 1.688.722,10. No CUB puro, a diferença é de +R$ 78.558,95 (piso) a +R$ 230.951,50 (teto). Depois de BDI e INCC no cronograma, fica em ~R$ 102,8 mil (78.558,95 × 1,3084484) a ~R$ 333,4 mil (230.951,50 × 1,4436525) só pela base de área.

---

## 5. Cadeia completa: CUB → BDI → INCC-M (até o início **e ao longo da obra**) → + demolição

Parâmetros:
- **BDI** TCU, Acórdão 2622/2013-Plenário, "Construção de Edifícios": 20,34% (1º quartil) a 25,00% (3º quartil) [ECF, extrapolação: obra pública, 2013]. Igual à v2.
- **INCC-M de set/2026 a mai/2027 (8 meses): +3,9% a +4,4%** (dois métodos, v1 §5.2) [ECF, extrapolação do passado]. Fatores usados: 1,039 (piso) e 1,0436 (teto). Igual à v2.
- **Demolição só da casa (~180 m², mecanizada): R$ 25.200 a R$ 54.000** [ECF, fonte fraca, Cronoshare]. Igual à v2. É gasto do início da obra, por isso **não reajusto a demolição no cronograma** (premissa declarada).

### 5.1 NOVO — reajuste ao longo do desembolso (mai/2027 → dez/2028)

**Taxa mensal: a mesma que já estava implícita na v2. Não criei taxa nova.**
- Piso: 1,039 em 8 meses → taxa mensal = 1,039^(1/8) − 1. ln(1,039) = 0,0382587; ÷ 8 = 0,0047823 → **0,4794% a.m.**
- Teto: 1,0436 em 8 meses → 1,0436^(1/8) − 1. ln(1,0436) = 0,0426763; ÷ 8 = 0,0053345 → **0,5349% a.m.**

**Cronograma:** 20 parcelas mensais, de mai/2027 (mês 0) a dez/2028 (mês 19). O reajuste é contado a partir de mai/2027, sobre o valor que já foi reajustado até o início.

**Piso: desembolso linear.** Com parcelas iguais, o fator médio de reajuste é praticamente o fator no mês médio da obra, (0 + 19) ÷ 2 = **9,5 meses depois de mai/2027 (~meados de fev/2028)**. A diferença entre a média dos fatores e o fator no mês médio é de segunda ordem (< 0,03 p.p.); declaro a aproximação.
- Fator na obra = e^(0,0047823 × 9,5) = e^0,0454318 = **1,046480**.
- **Fator INCC total do piso** = 1,039 × 1,046480 = **1,087293** (equivale a 1,039^(17,5/8): e^(0,0382587 × 2,1875) = e^0,0836909 = 1,087293 ✔).

**Teto: reajuste até o fim da obra (dez/2028, mês 19).** Justificativa: é o limite superior possível. Nenhuma parcela é paga depois do último mês, então reajustar 100% do valor até dez/2028 dá o maior reajuste que o cronograma admite. Uma curva em S, com desembolso concentrado no meio e no fim, ficaria entre o piso e este teto. Escolhi o fim, e não um ponto da curva em S, porque **não tenho cronograma físico-financeiro** para situar esse ponto, e inventar o formato da curva seria inventar número.
- Fator na obra = e^(0,0053345 × 19) = e^0,1013555 = **1,106670**.
- **Fator INCC total do teto** = 1,0436 × 1,106670 = **1,154921** (conferência: 1,0436^(27/8) = e^(0,0426763 × 3,375) = e^0,1440325 = 1,154922 ✔; uso 1,154922).

**Dissídio de maio/2028:** **não modelado separadamente.** A minha fonte (Sinduscon-Rio, Relatório 14) sustenta que houve salto em maio/2026 (mão de obra +4,42%), mas não sustenta o valor do dissídio de 2028. A taxa mensal que uso é uma média e já "dilui" um dissídio por ano: o método "mesma janela do ano anterior" (set→mai) contém o salto de maio/2026. Por isso o fator dos meses mai/27→dez/28 inclui o efeito de um dissídio na média, mas não reproduz o degrau no mês certo. Na prática, num desembolso linear, o degrau concentrado em mai/2028 pesa menos sobre o valor do que a mesma alta espalhada pelo ano, então o erro tende a ser pequeno e para cima. Declaro como aproximação.

**Fatores únicos da cadeia (sobre o CUB puro):**
- Piso: 1,2034 × 1,087293 = **1,3084484**
- Teto: 1,25 × 1,154922 = **1,4436525**

### 5.1.1 Tabela — linhas d/e por cenário (contas abertas)

Piso = CUB piso × 1,2034 × 1,039 × 1,046480 + 25.200. Teto = CUB teto × 1,25 × 1,0436 × 1,106670 + 54.000.

| Cenário | Linha | CUB puro | × BDI | × INCC até mai/27 (= v2) | × INCC na obra | + demolição | **Total (desembolso mai/27–dez/28)** |
|---|---|---|---|---|---|---|---|
| S1/H0 | Piso | 1.767.281,05 | 2.126.746,02 | 2.209.689,11 | × 1,046480 = 2.312.396,07 | + 25.200 | **2.337.596,07** |
| S1/H0 | Teto | 1.919.673,60 | 2.399.592,00 | 2.504.214,21 | × 1,106670 = 2.771.341,59 | + 54.000 | **2.825.341,59** |
| S2 | Piso | 1.850.565,35 | 2.226.970,34 | 2.313.822,18 | × 1,046480 = 2.421.369,27 | + 25.200 | **2.446.569,27** |
| S2 | Teto | 2.002.957,90 | 2.503.697,38 | 2.612.858,59 | × 1,106670 = 2.891.575,18 | + 54.000 | **2.945.575,18** |
| S3/H1 | Piso | 1.176.021,58 | 1.415.224,37 | 1.470.418,12 | × 1,046480 = 1.538.763,55 | + 25.200 | **1.563.963,55** |
| S3/H1 | Teto | 1.328.414,13 | 1.660.517,66 | 1.732.916,23 | × 1,106670 = 1.917.768,38 | + 54.000 | **1.971.768,38** |

Conferência pelo fator único (CUB × 1,3084484 ou × 1,4436525):
- S1 piso: 1.767.281,05 × 1,3 = 2.297.465,37; × 0,0084484 = 14.930,70 → 2.312.396,07 ✔
- S1 teto: 1.919.673,60 × 1,4 = 2.687.543,04; × 0,0436525 = 83.798,55 → 2.771.341,59 ✔
- S2 piso: 2.405.734,96 + 15.634,31 = 2.421.369,27 ✔
- S2 teto: 2.804.141,06 + 87.434,12 = 2.891.575,18 ✔
- S3 piso: 1.528.828,05 + 9.935,50 = 1.538.763,55 ✔
- S3 teto: 1.859.779,78 + 57.988,60 = 1.917.768,38 ✔
(Diferenças de centavo entre multiplicar em cadeia e pelo fator único são arredondamento.)

### 5.2 Quanto mudou em relação à v2

| Cenário | v2 (só até mai/27) | v3 (no cronograma) | Diferença |
|---|---|---|---|
| S1 piso | 2.234.889,11 | 2.337.596,07 | **+102.706,96** (+4,6%) |
| S1 teto | 2.558.214,21 | 2.825.341,59 | **+267.127,38** (+10,4%) |
| S2 piso | 2.339.022,18 | 2.446.569,27 | **+107.547,09** |
| S2 teto | 2.666.858,59 | 2.945.575,18 | **+278.716,59** |
| S3 piso | 1.495.618,12 | 1.563.963,55 | **+68.345,43** |
| S3 teto | 1.786.916,23 | 1.971.768,38 | **+184.852,15** |

A diferença é toda do reajuste na obra (a demolição não muda): piso = (fator 1,046480 − 1) sobre o valor de mai/27; teto = (1,106670 − 1). Ex.: S1 piso 2.209.689,11 × 0,046480 = 102.706,95 ✔; S1 teto 2.504.214,21 × 0,106670 = 267.124,5 (a diferença de ~R$ 3 é arredondamento do fator).

A faixa abriu: no S1, a distância entre piso e teto passa de R$ 323 mil (v2) para R$ 488 mil. Isso vem da premissa de teto (todo o valor reajustado até dez/2028), que é deliberadamente conservadora.

### 5.3 Contra o teto da família (R$ 4,2 milhões) — só S1
- 4.200.000 − 2.825.341,59 = **R$ 1.374.658,41** (contra o teto de custo)
- 4.200.000 − 2.337.596,07 = **R$ 1.862.403,93** (contra o piso de custo)
- **Sobram R$ 1,37 mi a R$ 1,86 mi** (na v2 eram R$ 1,64 mi a R$ 1,97 mi: −R$ 267 mil a −R$ 103 mil) para TODOS os itens da seção 6 ainda sem valor. **Continuo sem poder afirmar se cabe ou não cabe**: o maior item aberto (fundação em argila mole com NA a 0,90 m) é o que mais varia. Atenção: os itens da seção 6, quando tiverem valor, **também** vão sofrer o reajuste no cronograma.

---

## 6. Itens fora do CUB — checklist completo (Skill §2.4) — igual à v2

| # | Item | Valor | Rótulo | Fonte / o que faltaria |
|---|---|---|---|---|
| 1 | **Fundação profunda** (provável hélice contínua: sondagem 5.7, NA 0,90 m, argila mole de 2,5 a 9 m, areia compacta só abaixo de 11 m) | Total: — . Unitário: **SINAPI 100651 Ø 30: R$ 139,38/m; 100652 Ø 50: R$ 255,98/m** (07/2026, média nacional, não desonerado, sem mobilização) | **[NC]** total; **[ECF]** unitário | orcamentor.com: https://orcamentor.com/composicao/100651/ e /100652/. Teste de consistência contra concreto Sinduscon-Rio (R$ 587,50/m³) ✔. Não é preço RJ; Ø 40 não localizado (100650 = 404). Sem nº de estacas, não multiplico. Pergunta (Art. 8º): blocos e baldrames cabem em 1,20 m? |
| 2 | **Rebaixamento de lençol / esgotamento** | — | **[NC]** | Excluído do CUB [FP]. Depende das cotas (blocos, poço, piscina). Skill de Saturnino. |
| 3 | **Elevador / plataforma para D. Lourdes** (81 anos, cadeirante, 2 paradas) | Com obra civil: **plataforma R$ 43.000–170.000; elevador R$ 113.000–270.000** | **[ECF], fonte FRACA** | Monitor do Mercado, 24/08/2026 (faixas "ilustrativas", sem região/fabricante). Risco: poço × NA 0,90 m × Art. 8º (Baumgart/Kelsen). |
| 4 | **Piscina nova** | — | **[NC]** | Dimensão não definida; NA raso pede piscina estanque. |
| 5 | **Paisagismo** | — | **[NC]** | Sem projeto (Glaziou). |
| 6 | **Ar-condicionado** | — | **[NC]** | Sem projeto nem carga térmica. |
| 7 | **Automação** | — | **[NC]** | Sem escopo. |
| 8 | **Projetos e aprovações** | — | **[NC]** | Tabela CAU/BR não lida; taxa da Comissão de Obras (Art. 9º) sem valor. |
| 9 | **Ligações definitivas** | — | **[NC]** | Sem carga nem orçamento de concessionária. |
| 10 | **Sondagem complementar** | — | **[NC]** | Profundidade dos furos de 2024 não informada. |
| 11 | **Impostos, taxas, emolumentos** | — | **[NC]** | Excluídos do CUB [FP]. |
| 12 | **Demolição — casa** | **R$ 25.200–54.000** | **[ECF], fraca** | Somada na seção 5. Cronoshare, 02/01/2026. |
| 12b | Demolição — edícula, piscina, entulho | — | **[NC]** | Faltam área, volume e cotação. |
| 13 | **Acabamento acima do memorial R-1 Alto** | — | **[NC]** | Sem fonte. Sentido: aumenta. |
| 14 | **Efeito 2 pavimentos** | — | **[NC]** | Seção 3. Sentido: aumenta. |
| 15 | **BDI** | 20,34%–25,00% | **[ECF]** | Somado na seção 5 (TCU). |
| — | Equipamentos, playground, urbanização | — | **[NC]** | Excluídos do CUB [FP]; sem projeto. |

Detalhamento completo de cada item (textos, URLs, testes): v2 §6, que continua valendo integralmente.

---

## 7. Efeito da garagem coberta na TO, em custo — igual à v2

Por 10 m² de garagem coberta dentro da projeção: −10 m² computáveis; −R$ 36.916,80 de área útil + R$ 18.458,40 a R$ 27.687,60 de garagem = **−R$ 18.458,40 a −R$ 9.229,20 no CUB puro (set/26)**. O custo cai um pouco, mas **a família perde 10 m² de casa**. O coeficiente 0,50–0,75 é analogia com garagem de subsolo (Skill §2.3), declarada. **Pedido:** dimensão e nº de vagas cobertas (Lúcio); regra de TO para vaga coberta (Kelsen).

---

## 8. Proposta 5.12 (Alicerce Prime, R$ 6.300/m²) na área construída — reajuste refeito

Leitura igual à v1/v2: 590 × 6.300 = 3.717.000 ✔ [DOC], mas 590 m² não cabe na lei; "chave na mão" exclui 8 itens; radier contra a sondagem (risco alto de aditivo, [NC]); 6.300 ÷ 3.691,68 = 1,7066 (70,7% acima do CUB Alto); n = 1, não é benchmark; reajuste INCC-M sem mês-base declarado; validade vence ~29/10/2026.

**Premissas do reajuste:** (a) a proposta reajusta pelo INCC-M durante toda a execução [DOC, 5.12]; (b) adoto set/2026 como mês-base, porque a proposta não declara mês-base (premissa minha); (c) pagamento por medição mensal, com os mesmos fatores da seção 5.1: piso 1,087293 (linear), teto 1,154922 (tudo até dez/2028).

| Cenário | Base (construída) | Preço set/26 [DOC × premissa] | Piso: × 1,087293 | Teto: × 1,154922 | v2 (só até mai/27) | Diferença |
|---|---|---|---|---|---|---|
| S1/H0 | 500–520 | 3.150.000 a 3.276.000 | **3.424.972,95** | **3.783.524,47** | 3.272.850 a 3.418.834 | +152.123 / +364.690 |
| S2 | 522,56–542,56 | 3.292.128 a 3.418.128 | **3.579.507,73** | **3.947.671,23** | 3.420.521 a 3.567.158 | +158.987 / +380.513 |
| S3/H1 | 339,84–359,84 | 2.140.992 a 2.266.992 | **2.327.885,61** | **2.618.198,94** | 2.224.491 a 2.365.833 | +103.395 / +252.366 |

Contas: 3.150.000 × 0,087293 = 274.972,95; 3.276.000 × 0,154922 = 507.524,47; 3.292.128 × 0,087293 = 287.379,73; 3.418.128 × 0,154922 = 529.543,23; 2.140.992 × 0,087293 = 186.893,61; 2.266.992 × 0,154922 = 351.206,94.

As duas vias no S1, no cronograma: CUB + BDI + INCC + demolição **R$ 2,34–2,83 mi** × proposta **R$ 3,42–3,78 mi**. Divergem ~R$ 0,96–1,09 mi (piso com piso, teto com teto). É esperado: a proposta inclui fundação (radier) e acabamento "alto padrão" que o CUB não mede, e eu ainda não somei fundação, elevador etc.

### 8.1 Conta do Rodrigo (5.15): 520 × 6.300 = R$ 3.276.000; "sobra quase R$ 1 milhão"
- Aritmética ✔: 520 × 6.300 = 3.276.000; 4.200.000 − 3.276.000 = 924.000.
- **Reajustado no cronograma:** 3.276.000 × 1,087293 = **3.561.971,87** (piso); 3.276.000 × 1,154922 = **3.783.524,47** (teto).
- **Sobra: 4.200.000 − 3.783.524,47 = R$ 416.475,53 a 4.200.000 − 3.561.971,87 = R$ 638.028,13.** Na v2 eram R$ 781–796 mil; agora cai **R$ 158–380 mil**.
- Continua não sendo custo da obra: (1) 520 m² só existe em H0 e se 62,56 m² entrarem como não computáveis (decisão de Lúcio); em H1, 520 m² não cabe; (2) os R$ 416–638 mil precisam pagar os 8 não inclusos **e a plataforma/elevador de D. Lourdes** (R$ 43–170 mil de plataforma, fonte fraca); (3) radier → estacas vira aditivo, e aditivo também é reajustado; (4) a validade vence antes de existir projeto.

---

## 9. Sinalizações para Villaça encaminhar — igual à v2

| Para | O quê |
|---|---|
| **Baumgart / Cardozo** | Radier × sondagem; quantitativo de estacas; profundidade dos furos de 2024; blocos/baldrames × Art. 8º (1,20 m); poço da plataforma/elevador × NA 0,90 m × Art. 8º; atrito negativo com aterro de +3,20 m. |
| **Kelsen** | Poço de elevador/plataforma conta como "escavação" do Art. 8º? Vaga coberta na projeção: efeito na TO. |
| **Saturnino (via Cardozo)** | Esgotamento/rebaixamento na obra e no poço. |
| **Lúcio** | Quadro de áreas por tipo; vagas cobertas; tipo de plataforma; piscina. Avisar que o programa de 520 m² não cabe em H1. **Novo:** um cronograma físico-financeiro (mesmo preliminar) permitiria trocar o teto "tudo até dez/2028" por uma curva real e estreitar a faixa. |
| **Fiker** | A base de custo é a área construída/equivalente; preço de construtora é custo, não valor de mercado. **Novo:** os totais agora são em moeda do desembolso (mai/27–dez/28), não de mai/27. |

## 10. Perguntas que eu faria num caso real (NÃO enviadas)

| A quem | Pergunta |
|---|---|
| Alicerce Prime | Composição do R$ 6.300/m²; **mês-base do INCC e periodicidade do reajuste (por medição mensal ou anual?)**; sobre qual área cobra; preço refeito com estacas e área legal; plataforma inclusa? Cronograma físico-financeiro previsto. |
| 3 fabricantes de plataforma/elevador (RJ) | Preço instalado, 2 paradas, cadeira de rodas, com e sem poço. |
| Topógrafo/caseiro | Área da edícula, volume da piscina existente. |
| Empresa de sondagem | Profundidade final dos furos de 2024. |
| Comissão de Obras | Taxa do Art. 9º. |

## 11. Lacunas e bloqueios desta execução

- Igual à v2: NBR 12721 não lida no oficial; hélice contínua sem preço RJ e sem Ø 40; plataforma só com fonte fraca; sem % para sobrado; sem fonte de acabamento acima do memorial; BDI de obra pública; CAU/BR não lida.
- **Novo:** taxa mensal do INCC é extrapolação do passado; sem cronograma físico-financeiro (por isso o teto é "tudo até o fim"); dissídio de mai/2028 não modelado como degrau; mês-base da proposta 5.12 assumido como set/2026.
- **Fonte sobre reajuste no cronograma (item 4 do pedido): não achei** uma fonte lida na íntegra que diga literalmente que cada parcela/medição é reajustada pelo INCC do mês da sua execução. Detalhe na seção 12, fonte 10.

## 12. Fontes (acesso 02/10/2026)

1. Sinduscon-Rio, CUB/m² set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
2. Sinduscon-Rio, Relatório 14, set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Evolucao-e-composicao-setembro-de-2026.pdf
3. Sinduscon-Rio, Preços medianos set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Precos-medianos-setembro-de-2026.pdf
4. FGV, INCC-M set/2026 [FP]: https://portal.fgv.br/noticias/incc-m-setembro-2026 ; VRI: https://www.vriconsulting.com.br/indices/incc-m.php ; Brasil Indicadores: https://www.brasilindicadores.com.br/incc-m
5. TCU, Acórdão 2622/2013-Plenário (BDI): https://www.mpf.mp.br/o-mpf/unidades/pr-to/transparencia/licitacoes-novo/2016/12Acordao26222013BDI.pdf
6. Cronoshare, demolição (02/01/2026), fraca: https://www.cronoshare.com.br/quanto-custa/demolir-casa
7. SINAPI 100651/100652 via orcamentor.com: https://orcamentor.com/composicao/100651/ ; https://orcamentor.com/composicao/100652/
8. Monitor do Mercado, elevador residencial (24/08/2026), fraca: https://monitordomercado.com.br/economia-2/420300-quanto-custa-instalar-um-elevador-residencial-para-ligar-2-andares-de-uma-casa-em-2026-e-o-que-precisa-ser-preparado-antes-da-montagem/
9. Skills `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.0; `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3.
10. **Reajuste no cronograma — resultado da busca (item 4):**
    - **Lida na íntegra [FP], mas sustenta só parcialmente:** Polícia Federal / MJSP, CPL/SELOG/SR/PF/PE, *Minuta de Contrato — Obra de Engenharia*, Processo 08400.007001/2018-11 (metadado do PDF: 21/09/2018), Cláusula 3.3: *"O valor consignado neste Termo de Contrato é fixo e irreajustável, porém poderá ser corrigido anualmente mediante requerimento da contratada, observado o interregno mínimo de um ano, contado a partir da data limite para a apresentação da proposta, pela variação do Índice Nacional de Custo da Construção – INCC, coluna 35, calculado pela Fundação Getúlio Vargas"*. https://www.gov.br/pf/pt-br/assuntos/licitacoes/2018/pernambuco/concorrencias/licitacao-para-reforma-da-sede-da-sr-pe/anexo-ii-minuta-do-contrato.pdf . **Sustenta** que contrato de obra se reajusta pelo INCC/FGV durante a execução. **Não sustenta** o reajuste mês a mês por medição: em obra pública, o reajuste é anual. Obra pública ≠ contrato privado de casa.
    - **Só vista em resumo de busca, NÃO lida no original:** o resumo do buscador atribui a contratos públicos (MPF, INSS, comprasnet) uma cláusula do tipo "as parcelas do cronograma físico-financeiro que, na data de sua efetiva execução, ultrapassem um ano da data-base do orçamento, serão reajustadas pela variação do INCC/FGV". Tentei abrir a fonte: o PDF do MPF deu 404 e a minuta do INSS (https://www.gov.br/inss/pt-br/acesso-a-informacao/licitacoes-e-contratos/licitacoes-superintendencia-regional-nordeste-regiao-nordeste-do-pais/MINUTADECONTRATOCE.pdf) não teve o trecho localizado nas páginas que li. **Não cito como fonte.**
    - Orçafascio, Hiago Branco, "Saiba o que é o INCC..." (21/09/2021, atualizado em 13/06/2025): https://www.orcafascio.com/papodeengenheiro/incc — **não trata** de reajuste por medição na obra; fala só de parcelas de imóvel na planta. Descartado.
    - **Conclusão: não achei** fonte verificável que sustente literalmente o reajuste por medição mensal ao longo da curva de desembolso. O que sustenta o meu método é o próprio Dossiê (a proposta 5.12 reajusta pelo INCC-M durante a execução [DOC]) mais a aritmética do cronograma, que é minha [ECF].

---

*Declaração: ensaio 100% fictício (Ensaio Sombra 003, Etapa 02, v3). Ninguém contatado; gabarito lacrado não aberto. Nenhum número é custo fechado ou garantia. Mascaró, 02/10/2026.*
