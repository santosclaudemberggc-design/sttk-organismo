# Custo de Obra v4 — Ensaio 003, Etapa 02 (Viabilidade) — Lote 17, Reserva das Garças

**Agente:** Mascaró (Custo de Obra), equipe de Villaça
**Pedido de:** Villaça, 02/10/2026 (correção v4, tolerância zero, após parecer de Bardi sobre a v3)
**Data de acesso de todas as fontes web:** 02/10/2026.
**Situação:** entrega de Agente para auditoria de Villaça. Não é orçamento, não é custo fechado, não vai a cliente.

> **ENSAIO — 100% FICTÍCIO.** Ninguém foi contatado. `_gabaritos_LACRADO/` não foi aberto. As perguntas que eu faria num caso real estão na seção 10.

**O que muda em relação à v3** (`../v3/custo_obra_mascaro_003_v3.md`, mantida intacta):
1. **Leitura da 5.12 corrigida.** A proposta diz, literalmente: Reajuste: "INCC-M mensal a partir da data desta proposta", e a proposta é de 29/09/2026. Logo ela **declara** a data-base (29/09/2026) e a periodicidade (mensal). A v1, a v2 e a v3 afirmavam o contrário: estava errado. Corrigido nas §§ 8, 10, 11 e 12. Também tirei a frase "a proposta reajusta durante toda a execução": o texto da 5.12 não diz isso. O que ele diz é "mensal a partir da data desta proposta".
2. **Datas da obra.** O início em mai/2027 é o desejo declarado pelo cliente [DOC]. O fim em dez/2028 é **premissa minha [PV]**: o caso base diz "mudar até dezembro/2028", não que a obra termina aí.
3. **Plataforma e elevador de D. Lourdes reajustados** pelos fatores do cronograma (Skill §2.6), §6 item 3.
4. **Demolição reajustada** da data-base da fonte (Cronoshare, 02/01/2026) até mai/2027, com o INCC-M mês a mês lido na FGV, §5.
5. **Fator do piso:** a frase "< 0,03 p.p." estava errada. A diferença é ≈ 0,04 p.p. (≈ R$ 855 no piso de S1), §5.1.
6. Refeitos: §5.1.1, §5.2 (agora contra a v3), §5.3, §8.1, §6 itens 3 e 12. A via 5.12 (§8) não muda de valor.

Áreas, CUB, BDI, checklist, SINAPI, garagem × TO e sinalizações ficam iguais à v3.

**Skill aplicada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` **v1.2** (ativa-com-ressalva: a NBR 12721 não foi lida no texto oficial; os coeficientes vêm de fonte secundária, e herdo essa ressalva). A v1.2 manda ler e citar literalmente a cláusula de reajuste da proposta.

**Rótulos:** **[FP]** fonte primária lida por mim; **[ECF]** estimativa com fonte (conta minha, fragilidade declarada); **[NC]** não calculável (digo o que faltaria); **[DOC]** dado do Dossiê ou do caso base; **[PV]** premissa minha, declarada.

---

## 1. Premissas de área (fixadas por Villaça, porque Lúcio ainda não desenhou)

| Cenário | Área computável [DOC/Legal] | Não computável (varandas + garagem coberta) | Área construída de trabalho |
|---|---|---|---|
| **S1 / H0** (adotado) | 457,44 m² | 42,56 a 62,56 m² | **500,00 a 520,00 m²** |
| S2 (divisa regularizada) | 480,00 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **522,56 a 542,56 m²** |
| S3 / H1 (APP do lago) | 297,28 m² | 42,56 a 62,56 m² (mesmo acréscimo absoluto) | **339,84 a 359,84 m²** |

- A linha de **520 m² do programa** (caso base §4: "cerca de 520 m² construídos") **só existe em H0** (é o teto da faixa do S1). Em H1/S3 esse programa **não cabe**: o teto de trabalho é 359,84 m² (faltam 160,16 m²).
- CAB = CAM = 1,0: nenhum cenário tem outorga (OODC R$ 0, v1 e Etapa 01). Não recalculei parâmetro legal.
- Padrão alto. Casa de 2 pavimentos.
- **Datas da obra:** o caso base (§2) diz literalmente: "Querem iniciar a obra em maio/2027 e mudar até dezembro/2028."
  - **Início mai/2027** = desejo declarado pelo cliente **[DOC]**.
  - **Fim dez/2028** = **[PV]**: adoto o fim da obra igual ao prazo de mudança. O documento não diz que a obra termina em dez/2028. Com isso, o desembolso tem 20 meses (mai/2027 a dez/2028), **premissa**. Se a obra acabar antes (para dar tempo de mudança), o teto da §5.1 cai.
- [PV] Toda a não computável é "varanda/garagem coberta". O piso usa o menor coeficiente provável (0,50, garagem por analogia, Skill §2.3); o teto trata tudo como 1,00 (Skill §2.2).

---

## 2. Benchmark — CUB/m² Sinduscon-Rio, setembro/2026 [FP]

- **R-1 Padrão Alto: R$ 3.691,68/m²** (emitido em 29/09/2026). https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
- R-1 Normal (R$ 2.990,86) e Baixo (R$ 2.476,02) ficam só como referência. Pela Skill §2.5 / macete M3, não aplico padrão Normal a casa de alto padrão.
- Tendência em 2026 (Relatório 14, R8-N): +4,0% no ano até setembro, com salto em maio (+2,54%; mão de obra +4,42%) [FP, conta minha]. Atenção: isso é o CUB R8-N do Rio; o INCC-M nacional (FGV) subiu mais no mesmo período (≈ 5,85%, §5).

---

## 3. Casa de 2 pavimentos (Skill §2.5)

- R-1 é residência **térrea**. Uso **R-1 Alto como proxy declarado** (extrapolação). Não uso R8-N como base de casa.
- **[NC] "efeito 2 pavimentos"** (escada, laje de piso, estrutura mais carregada): o custo real tende a ser **MAIOR**. Não achei percentual citável e não inventei acréscimo.

---

## 4. Área equivalente (NBR 12721) × CUB R-1 Alto

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

## 5. Cadeia completa: CUB → BDI → INCC-M (até o início e ao longo da obra) → + demolição reajustada

Parâmetros:
- **BDI** TCU, Acórdão 2622/2013-Plenário, "Construção de Edifícios": 20,34% (1º quartil) a 25,00% (3º quartil) [ECF, extrapolação: obra pública, 2013].
- **INCC-M de set/2026 a mai/2027 (8 meses): +3,9% a +4,4%** (dois métodos, v1 §5.2) [ECF, extrapolação do passado]. Fatores: 1,039 (piso) e 1,0436 (teto).
- **Demolição só da casa (~180 m², mecanizada): R$ 25.200 a R$ 54.000 em preço de 02/01/2026** [ECF, fonte fraca, Cronoshare]. **Novo na v4: reajustada até mai/2027** (é gasto do início da obra; por isso não a reajusto ao longo do cronograma, [PV]).

### 5.0 NOVO — Reajuste da demolição (02/01/2026 → mai/2027)

**Trecho 1: data da fonte → set/2026, INCC-M FGV [FP].** Fonte: FGV, "INCC-M setembro 2026" (divulgado em 25/09/2026), https://portal.fgv.br/noticias/incc-m-setembro-2026. **A matéria não traz o "acumulado no ano"** (traz a variação mensal e o acumulado em 12 meses: set/26 = 0,25%; 12 meses = 6,61%). Por isso compus o acumulado com as variações mensais da tabela da própria matéria [FP nas taxas; conta minha]:

| Mês | jan/26 | fev/26 | mar/26 | abr/26 | mai/26 | jun/26 | jul/26 | ago/26 | set/26 |
|---|---|---|---|---|---|---|---|---|---|
| Variação mensal | 0,63% | 0,34% | 0,36% | 1,04% | 0,77% | 0,85% | 0,62% | 0,85% | 0,25% |

- Produto jan→set/2026 (9 meses) = 1,0063 × 1,0034 × 1,0036 × 1,0104 × 1,0077 × 1,0085 × 1,0062 × 1,0085 × 1,0025 = **1,058540** (+5,854%). Cobre de dez/2025 (base) a set/2026.
- Produto fev→set/2026 (8 meses) = 1,058540 ÷ 1,0063 = **1,051913** (+5,191%). Cobre de jan/2026 (base) a set/2026.

**A que mês corresponde o preço de 02/01/2026?** Não dá para saber com certeza. A página da Cronoshare traz a data de 02/01/2026, mas não diz quando os preços foram levantados. O dia 02/01 cai no começo de janeiro, antes de quase toda a alta de jan/2026 (0,63%). Por isso:
- **Teto: base dez/2025** → × 1,058540 (conta toda a alta de janeiro).
- **Piso: base jan/2026** → × 1,051913 (supõe que a alta de janeiro já estava no preço).
A diferença entre as duas leituras é de 0,63%, e eu a deixo dentro da faixa.

**Trecho 2: set/2026 → mai/2027:** os mesmos fatores da cadeia, × 1,039 (piso) e × 1,0436 (teto) [ECF].

**Fatores totais da demolição:**
- Piso: 1,051913 × 1,039 = **1,092938**
- Teto: 1,058540 × 1,0436 = **1,104692**

**Demolição reajustada (mai/2027):**
- Piso: 25.200 × 1,051913 = 26.508,21; × 1,039 = **R$ 27.542,03**
- Teto: 54.000 × 1,058540 = 57.161,17; × 1,0436 = **R$ 59.653,40**

**Divergência registrada:** o CUB R8-N do Sinduscon-Rio subiu +4,0% no ano até set/2026 (Relatório 14), menos que o INCC-M nacional (+5,85%). Usei o INCC-M porque é o índice da cadeia e da 5.12. Com o CUB do Rio, a demolição reajustada sairia um pouco menor (≈ −R$ 0,5 mil no piso e ≈ −R$ 1 mil no teto). Não é material.

### 5.1 Reajuste ao longo do desembolso (mai/2027 → dez/2028, fim = [PV])

**Taxa mensal: a mesma que já estava implícita na v2. Não criei taxa nova.**
- Piso: 1,039 em 8 meses → taxa mensal = 1,039^(1/8) − 1. ln(1,039) = 0,0382587; ÷ 8 = 0,0047823 → **0,4794% a.m.**
- Teto: 1,0436 em 8 meses → 1,0436^(1/8) − 1. ln(1,0436) = 0,0426763; ÷ 8 = 0,0053345 → **0,5349% a.m.**

**Cronograma [PV]:** 20 parcelas mensais, de mai/2027 (mês 0) a dez/2028 (mês 19). O fim em dez/2028 é premissa (§1). O reajuste é contado a partir de mai/2027, sobre o valor que já foi reajustado até o início.

**Piso: desembolso linear. O fator 1,046480 é o fator no MÊS MÉDIO da obra, não a média dos 20 fatores.**
- Mês médio = (0 + 19) ÷ 2 = 9,5 meses depois de mai/2027 (~meados de fev/2028).
- Fator no mês médio = e^(0,0047823 × 9,5) = e^0,0454318 = **1,046480**.
- **Média exata dos 20 fatores**, com r = 0,0047938: ((1 + r)^20 − 1) ÷ (20 r). (1 + r)^20 = e^(0,0956460) = 1,100369; (1,100369 − 1) ÷ 0,095876 = **≈ 1,046867** (Bardi: ≈ 1,04686).
- Diferença: 1,046867 − 1,046480 = 0,000387 → **≈ 0,04 p.p.** (a v3 dizia "< 0,03 p.p.": **estava errado**).
- **Mantenho 1,046480 como aproximação declarada, por baixo.** No piso de S1 ela deixa de fora ≈ 2.209.689,11 × 0,000387 ≈ **R$ 855** (com 0,0004 arredondado, ≈ R$ 884). Em S2 ≈ R$ 895; em S3 ≈ R$ 569. Valores pequenos diante das outras incertezas, mas o piso fica um pouco baixo.
- **Fator INCC total do piso** = 1,039 × 1,046480 = **1,087293** (equivale a 1,039^(17,5/8): e^(0,0382587 × 2,1875) = e^0,0836909 = 1,087293 ✔).

**Teto: reajuste até o fim da obra (dez/2028, mês 19, [PV]).** É o limite superior possível: nenhuma parcela é paga depois do último mês. Uma curva em S ficaria entre o piso e este teto. Não tenho cronograma físico-financeiro para situar a curva, e inventar o formato seria inventar número.
- Fator na obra = e^(0,0053345 × 19) = e^0,1013555 = **1,106670**.
- **Fator INCC total do teto** = 1,0436 × 1,106670 = **1,154921** (conferência: 1,0436^(27/8) = e^0,1440325 = 1,154922; uso 1,154922).

**Dissídio de maio/2028:** não modelado como degrau. O Relatório 14 sustenta o salto de maio/2026 (mão de obra +4,42%), mas não o valor de 2028. A taxa mensal é uma média que já dilui um dissídio por ano (a janela set→mai contém o salto de maio/2026). Aproximação declarada.

**Fatores únicos da cadeia (sobre o CUB puro):**
- Piso: 1,2034 × 1,087293 = **1,3084484**
- Teto: 1,25 × 1,154922 = **1,4436525**

### 5.1.1 Tabela — linhas d/e por cenário (contas abertas)

Piso = CUB piso × 1,2034 × 1,039 × 1,046480 + 27.542,03. Teto = CUB teto × 1,25 × 1,0436 × 1,106670 + 59.653,40.

| Cenário | Linha | CUB puro | × BDI | × INCC até mai/27 | × INCC na obra | + demolição reajustada | **Total (desembolso mai/27–dez/28)** |
|---|---|---|---|---|---|---|---|
| S1/H0 | Piso | 1.767.281,05 | 2.126.746,02 | 2.209.689,11 | × 1,046480 = 2.312.396,07 | + 27.542,03 | **2.339.938,10** |
| S1/H0 | Teto | 1.919.673,60 | 2.399.592,00 | 2.504.214,21 | × 1,106670 = 2.771.341,59 | + 59.653,40 | **2.830.994,99** |
| S2 | Piso | 1.850.565,35 | 2.226.970,34 | 2.313.822,18 | × 1,046480 = 2.421.369,27 | + 27.542,03 | **2.448.911,30** |
| S2 | Teto | 2.002.957,90 | 2.503.697,38 | 2.612.858,59 | × 1,106670 = 2.891.575,18 | + 59.653,40 | **2.951.228,58** |
| S3/H1 | Piso | 1.176.021,58 | 1.415.224,37 | 1.470.418,12 | × 1,046480 = 1.538.763,55 | + 27.542,03 | **1.566.305,58** |
| S3/H1 | Teto | 1.328.414,13 | 1.660.517,66 | 1.732.916,23 | × 1,106670 = 1.917.768,38 | + 59.653,40 | **1.977.421,78** |

Conferência pelo fator único (CUB × 1,3084484 ou × 1,4436525), igual à v3:
- S1 piso: 1.767.281,05 × 1,3084484 = 2.312.396,07 ✔; S1 teto: 1.919.673,60 × 1,4436525 = 2.771.341,59 ✔
- S2 piso: 2.421.369,27 ✔; S2 teto: 2.891.575,18 ✔; S3 piso: 1.538.763,55 ✔; S3 teto: 1.917.768,38 ✔

### 5.2 Quanto mudou em relação à v3

| Cenário | v3 | v4 | Diferença |
|---|---|---|---|
| S1 piso | 2.337.596,07 | 2.339.938,10 | **+2.342,03** |
| S1 teto | 2.825.341,59 | 2.830.994,99 | **+5.653,40** |
| S2 piso | 2.446.569,27 | 2.448.911,30 | **+2.342,03** |
| S2 teto | 2.945.575,18 | 2.951.228,58 | **+5.653,40** |
| S3 piso | 1.563.963,55 | 1.566.305,58 | **+2.342,03** |
| S3 teto | 1.971.768,38 | 1.977.421,78 | **+5.653,40** |

A diferença é só a demolição reajustada: piso 27.542,03 − 25.200 = 2.342,03; teto 59.653,40 − 54.000 = 5.653,40.

### 5.3 Contra o teto da família (R$ 4,2 milhões) — só S1
- 4.200.000 − 2.830.994,99 = **R$ 1.369.005,01** (contra o teto de custo)
- 4.200.000 − 2.339.938,10 = **R$ 1.860.061,90** (contra o piso de custo)
- **Depois da plataforma reajustada** (§6 item 3; piso com piso, teto com teto):
  - 1.860.061,90 − 46.753,60 = **R$ 1.813.308,30**
  - 1.369.005,01 − 196.336,74 = **R$ 1.172.668,27**
- **Se for elevador** (reajustado): 1.860.061,90 − 122.864,11 = R$ 1.737.197,79; 1.369.005,01 − 311.828,94 = R$ 1.057.176,07.
- **Sobram R$ 1,17 mi a R$ 1,81 mi** (com plataforma) para todos os outros itens da seção 6 ainda sem valor. **Continuo sem poder afirmar se cabe ou não cabe**: o maior item aberto (fundação em argila mole com NA a 0,90 m) é o que mais varia. Os itens da seção 6, quando tiverem valor, **também** vão sofrer reajuste.

---

## 6. Itens fora do CUB — checklist completo (Skill §2.4)

| # | Item | Valor | Rótulo | Fonte / o que faltaria |
|---|---|---|---|---|
| 1 | **Fundação profunda** (provável hélice contínua; sondagem 5.7: NA a 0,90 m, argila orgânica mole de 2,5 m a 9,0 m, areia compacta abaixo de 11 m) | Total: — . Unitário: **SINAPI 100651 Ø 30: R$ 139,38/m; 100652 Ø 50: R$ 255,98/m** (07/2026, média nacional, não desonerado, sem mobilização) | **[NC]** total; **[ECF]** unitário | orcamentor.com: https://orcamentor.com/composicao/100651/ e /100652/. Teste contra concreto Sinduscon-Rio (R$ 587,50/m³) ✔. Não é preço RJ; Ø 40 não localizado (100650 = 404). Sem nº de estacas, não multiplico. Pergunta (Art. 8º): blocos e baldrames cabem em 1,20 m? |
| 2 | **Rebaixamento de lençol / esgotamento** | — | **[NC]** | Excluído do CUB [FP]. Depende das cotas (blocos, poço, piscina). Skill de Saturnino. |
| 3 | **Plataforma / elevador para D. Lourdes** (81 anos, usa cadeira de rodas; 2 paradas = [PV] pela casa de 2 pavimentos) | Preço da fonte, com obra civil: plataforma R$ 43.000–170.000; elevador R$ 113.000–270.000. **Reajustado no cronograma: plataforma R$ 46.753,60–196.336,74; elevador R$ 122.864,11–311.828,94** | **[ECF], fonte FRACA** | Monitor do Mercado, 24/08/2026 (faixas "ilustrativas", sem região/fabricante). **[PV]: trato o preço de 24/08/2026 como preço de set/2026** (diferença de ~1 mês; o INCC-M de set/26 foi 0,25%). Reajuste (Skill §2.6) pelos fatores da §5.1: piso × 1,087293; teto × 1,154922. Contas: 43.000 × 1,087293 = 46.753,60; 170.000 × 1,154922 = 196.336,74; 113.000 × 1,087293 = 122.864,11; 270.000 × 1,154922 = 311.828,94. Risco: poço × NA 0,90 m × Art. 8º (Baumgart/Kelsen). |
| 4 | **Piscina nova** | — | **[NC]** | Dimensão não definida; NA raso pede piscina estanque. |
| 5 | **Paisagismo** | — | **[NC]** | Sem projeto (Glaziou). |
| 6 | **Ar-condicionado** | — | **[NC]** | Sem projeto nem carga térmica. |
| 7 | **Automação** | — | **[NC]** | Sem escopo. |
| 8 | **Projetos e aprovações** | — | **[NC]** | Tabela CAU/BR não lida; taxa de análise da Comissão de Obras (Art. 9º) sem valor. |
| 9 | **Ligações definitivas** | — | **[NC]** | Sem carga nem orçamento de concessionária. |
| 10 | **Sondagem complementar** | — | **[NC]** | Profundidade dos furos de 2024 não informada. |
| 11 | **Impostos, taxas, emolumentos** | — | **[NC]** | Excluídos do CUB [FP]. |
| 12 | **Demolição — casa (cerca de 180 m²)** | Fonte (02/01/2026): R$ 25.200–54.000. **Reajustada até mai/2027: R$ 27.542,03–59.653,40** | **[ECF], fraca** | Somada na seção 5. Cronoshare, 02/01/2026. Fatores na §5.0: 1,092938 (piso) e 1,104692 (teto). |
| 12b | Demolição — edícula, piscina, entulho | — | **[NC]** | Faltam área, volume e cotação. |
| 13 | **Acabamento acima do memorial R-1 Alto** | — | **[NC]** | Sem fonte. Sentido: aumenta. |
| 14 | **Efeito 2 pavimentos** | — | **[NC]** | Seção 3. Sentido: aumenta. |
| 15 | **BDI** | 20,34%–25,00% | **[ECF]** | Somado na seção 5 (TCU). |
| — | Equipamentos, playground, urbanização | — | **[NC]** | Excluídos do CUB [FP]; sem projeto. |

Detalhamento de cada item (textos, URLs, testes): v2 §6, que continua valendo, salvo os valores dos itens 3 e 12 acima.

---

## 7. Efeito da garagem coberta na TO, em custo

Por 10 m² de garagem coberta dentro da projeção: −10 m² computáveis; −R$ 36.916,80 de área útil + R$ 18.458,40 a R$ 27.687,60 de garagem = **−R$ 18.458,40 a −R$ 9.229,20 no CUB puro (set/26)**. O custo cai um pouco, mas **a família perde 10 m² de casa**. O coeficiente 0,50–0,75 é analogia com garagem de subsolo (Skill §2.3), declarada. **Pedido:** dimensão e nº de vagas cobertas (Lúcio); regra de TO para vaga coberta (Kelsen).

---

## 8. Proposta 5.12 (Alicerce Prime, R$ 6.300/m²) na área construída

**Texto literal da 5.12 [DOC]:** proposta de 29/09/2026, "validade 30 dias"; preço "R$ 6.300,00/m², 'chave na mão', sobre a área total construída de 590 m² = R$ 3.717.000,00"; **Reajuste: "INCC-M mensal a partir da data desta proposta".**

Leitura:
- 590 × 6.300 = 3.717.000 ✔ [DOC], mas 590 m² não cabe na lei.
- "Chave na mão" exclui 8 itens (lista de "Não inclusos" da 5.12).
- Fundação "em radier de concreto armado" contra a sondagem 5.7 (risco alto de aditivo, [NC]).
- 6.300 ÷ 3.691,68 = 1,7066 (70,7% acima do CUB Alto). n = 1, não é benchmark.
- **Reajuste: a proposta declara a data-base (a data da proposta, 29/09/2026) e a periodicidade (mensal).** O que ela não diz: se o reajuste incide por medição ou sobre o saldo, e qual número-índice usa. Isso fica para a pergunta (§10).
- Validade: 30 dias a partir de 29/09/2026 → vence ~29/10/2026.

**Premissas do reajuste:**
(a) **[DOC, 5.12]** reajuste mensal pelo INCC-M, com base na data da proposta (29/09/2026).
(b) **Leitura do índice, não premissa por falta de declaração:** o número-índice que corresponde à data declarada (29/09/2026) é o INCC-M de set/2026, divulgado pela FGV em 25/09/2026. Por isso o preço de 6.300/m² está em moeda de set/2026, a mesma base do CUB.
(c) **[PV]** pagamento por medição mensal ao longo da obra, mai/2027 a dez/2028 (fim = premissa, §1), com os fatores da §5.1: piso 1,087293 (linear), teto 1,154922 (tudo até dez/2028).

| Cenário | Base (construída) | Preço set/26 [DOC × premissa de área] | Piso: × 1,087293 | Teto: × 1,154922 |
|---|---|---|---|---|
| S1/H0 | 500–520 | 3.150.000 a 3.276.000 | **3.424.972,95** | **3.783.524,47** |
| S2 | 522,56–542,56 | 3.292.128 a 3.418.128 | **3.579.507,73** | **3.947.671,23** |
| S3/H1 | 339,84–359,84 | 2.140.992 a 2.266.992 | **2.327.885,61** | **2.618.198,94** |

Contas: 3.150.000 × 0,087293 = 274.972,95; 3.276.000 × 0,154922 = 507.524,47; 3.292.128 × 0,087293 = 287.379,73; 3.418.128 × 0,154922 = 529.543,23; 2.140.992 × 0,087293 = 186.893,61; 2.266.992 × 0,154922 = 351.206,94. **Valores iguais aos da v3; só o texto mudou.**

As duas vias no S1, no cronograma: CUB + BDI + INCC + demolição **R$ 2,34–2,83 mi** × proposta **R$ 3,42–3,78 mi**. Divergem ~R$ 0,95–1,09 mi (piso com piso: 3.424.972,95 − 2.339.938,10 = 1.085.034,85; teto com teto: 3.783.524,47 − 2.830.994,99 = 952.529,48). É esperado: a proposta inclui fundação (radier) e acabamento "de alto padrão" que o CUB não mede, e eu ainda não somei fundação etc.

### 8.1 Conta do Rodrigo (5.15)
Mensagem literal: "A construtora fecha em R$ 6.300 o m², tudo incluso. 520 m² dá R$ 3,28 milhões, sobra quase R$ 1 milhão do teto."
- Aritmética ✔: 520 × 6.300 = 3.276.000 (≈ R$ 3,28 mi); 4.200.000 − 3.276.000 = 924.000.
- "Tudo incluso" não confere com a própria 5.12, que tem 8 "Não inclusos".
- **Reajustado no cronograma:** 3.276.000 × 1,087293 = **3.561.971,87** (piso); 3.276.000 × 1,154922 = **3.783.524,47** (teto).
- **Sobra: R$ 416.475,53 (4.200.000 − 3.783.524,47) a R$ 638.028,13 (4.200.000 − 3.561.971,87).** Igual à v3.
- **Depois da plataforma reajustada:** 638.028,13 − 46.753,60 = **R$ 591.274,53**; 416.475,53 − 196.336,74 = **R$ 220.138,79**. **Se for elevador:** 638.028,13 − 122.864,11 = R$ 515.164,02; 416.475,53 − 311.828,94 = R$ 104.646,59.
- Continua não sendo custo da obra: (1) 520 m² só existe em H0 e se 62,56 m² entrarem como não computáveis (decisão de Lúcio); em H1, 520 m² não cabe; (2) a sobra de R$ 220–591 mil (com plataforma) ainda precisa pagar os 8 não inclusos (a demolição sozinha leva R$ 27,5–59,7 mil); (3) radier → estacas vira aditivo, e aditivo também é reajustado; (4) a validade vence antes de existir projeto.

---

## 9. Sinalizações para Villaça encaminhar

| Para | O quê |
|---|---|
| **Baumgart / Cardozo** | Radier × sondagem; quantitativo de estacas; profundidade dos furos de 2024; blocos/baldrames × Art. 8º (1,20 m); poço da plataforma/elevador × NA 0,90 m × Art. 8º; atrito negativo com aterro de +3,20 m. |
| **Kelsen** | Poço de elevador/plataforma conta como "escavação" do Art. 8º? Vaga coberta na projeção: efeito na TO. |
| **Saturnino (via Cardozo)** | Esgotamento/rebaixamento na obra e no poço. |
| **Lúcio** | Quadro de áreas por tipo; vagas cobertas; tipo de plataforma; piscina. Avisar que o programa de 520 m² não cabe em H1. Um cronograma físico-financeiro (mesmo preliminar) estreitaria a faixa e diria se a obra termina antes de dez/2028 (hoje premissa). |
| **Fiker** | A base de custo é a área construída/equivalente; preço de construtora é custo, não valor de mercado. Os totais estão em moeda do desembolso (mai/27–dez/28, fim = premissa). |
| **Villaça** | A 5.12 declara data-base e periodicidade do reajuste: corrigir a triagem e a resposta ao Rodrigo onde pedem "mês-base". |

## 10. Perguntas que eu faria num caso real (NÃO enviadas)

| A quem | Pergunta |
|---|---|
| Alicerce Prime | Composição do R$ 6.300/m² e BDI aberto; o reajuste "mensal a partir da data desta proposta" incide sobre cada medição ou sobre o saldo, e com qual número-índice do INCC-M (mês da proposta ou mês anterior)?; sobre qual área cobra; preço refeito com estacas e área legal; plataforma inclusa? Cronograma físico-financeiro previsto e prazo de obra. |
| Família | A obra precisa terminar quantos meses antes de dez/2028 para a mudança? |
| 3 fabricantes de plataforma/elevador (RJ) | Preço instalado, 2 paradas, cadeira de rodas, com e sem poço. |
| Cronoshare / 3 demolidoras (RJ) | Data de levantamento do preço; cotação para casa de ~180 m² + edícula + piscina. |
| Topógrafo/caseiro | Área da edícula, volume da piscina existente. |
| Empresa de sondagem | Profundidade final dos furos de 2024. |
| Comissão de Obras | Taxa de análise do Art. 9º. |

## 11. Lacunas e bloqueios desta execução

- NBR 12721 não lida no oficial; hélice contínua sem preço RJ e sem Ø 40; plataforma/elevador só com fonte fraca; sem % para sobrado; sem fonte de acabamento acima do memorial; BDI de obra pública; CAU/BR não lida.
- Taxa mensal do INCC é extrapolação do passado; sem cronograma físico-financeiro (teto = "tudo até o fim"); **fim da obra em dez/2028 é premissa**; dissídio de mai/2028 não modelado como degrau; fator do piso é o do mês médio (≈ R$ 855 abaixo da média exata em S1).
- Demolição: a FGV não publica o "acumulado no ano" na matéria de set/2026; compus com as taxas mensais. O mês-base do preço da Cronoshare (dez/2025 ou jan/2026) é incerto e ficou dentro da faixa.
- A 5.12 declara data-base e periodicidade; **não** declara se o reajuste é por medição ou sobre o saldo (premissa (c) da §8).

## 12. Fontes (acesso 02/10/2026)

1. Sinduscon-Rio, CUB/m² set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-setembro-de-2026.pdf
2. Sinduscon-Rio, Relatório 14, set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Evolucao-e-composicao-setembro-de-2026.pdf
3. Sinduscon-Rio, Preços medianos set/2026 [FP]: https://www.sinduscon-rio.com.br/wp/wp-content/uploads/2021/01/Precos-medianos-setembro-de-2026.pdf
4. FGV, INCC-M set/2026 (divulgado em 25/09/2026) [FP], incluindo a tabela de variações mensais set/25 a set/26 usada na §5.0: https://portal.fgv.br/noticias/incc-m-setembro-2026 ; VRI: https://www.vriconsulting.com.br/indices/incc-m.php ; Brasil Indicadores: https://www.brasilindicadores.com.br/incc-m
5. TCU, Acórdão 2622/2013-Plenário (BDI): https://www.mpf.mp.br/o-mpf/unidades/pr-to/transparencia/licitacoes-novo/2016/12Acordao26222013BDI.pdf
6. Cronoshare, demolição (02/01/2026), fraca: https://www.cronoshare.com.br/quanto-custa/demolir-casa
7. SINAPI 100651/100652 via orcamentor.com: https://orcamentor.com/composicao/100651/ ; https://orcamentor.com/composicao/100652/
8. Monitor do Mercado, elevador residencial (24/08/2026), fraca: https://monitordomercado.com.br/economia-2/420300-quanto-custa-instalar-um-elevador-residencial-para-ligar-2-andares-de-uma-casa-em-2026-e-o-que-precisa-ser-preparado-antes-da-montagem/
9. Skills `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.2; `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3.
10. **Reajuste — periodicidade e data-base:**
    - **Fonte primária: a própria proposta 5.12 [DOC]**, citada literalmente: Reajuste: "INCC-M mensal a partir da data desta proposta" (proposta de 29/09/2026). É ela que dá a periodicidade (mensal) e a data-base (29/09/2026).
    - **Apoio (macete M7), não fonte da periodicidade:** PF/MJSP, CPL/SELOG/SR/PF/PE, *Minuta de Contrato — Obra de Engenharia*, Processo 08400.007001/2018-11, Cláusula 3.3: *"O valor consignado neste Termo de Contrato é fixo e irreajustável, porém poderá ser corrigido anualmente mediante requerimento da contratada, observado o interregno mínimo de um ano, contado a partir da data limite para a apresentação da proposta, pela variação do Índice Nacional de Custo da Construção – INCC, coluna 35, calculado pela Fundação Getúlio Vargas"*. https://www.gov.br/pf/pt-br/assuntos/licitacoes/2018/pernambuco/concorrencias/licitacao-para-reforma-da-sede-da-sr-pe/anexo-ii-minuta-do-contrato.pdf . Mostra só que contrato de obra se reajusta pelo INCC/FGV; é obra pública e o reajuste é anual, diferente da 5.12.
    - A forma de aplicar o reajuste mensal às medições (curva de desembolso) é aritmética minha [ECF] sobre a premissa (c) da §8.

---

*Declaração: ensaio 100% fictício (Ensaio Sombra 003, Etapa 02, v4). Ninguém contatado; gabarito lacrado não aberto. Nenhum número é custo fechado ou garantia. Mascaró, 02/10/2026.*
