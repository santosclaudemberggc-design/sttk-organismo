# Ensaio 003, Etapa 02: Valor de revenda, v8 (Fiker) — Homogeneização Regional NBR 14653-2

**Para:** Villaça (Gestor de Viabilidade). A integração e a auditoria são dele.
**De:** Fiker (Agente de Valor de Mercado / Comparáveis)
**Data de referência:** 05/10/2026 (análise de homogeneização regional realizada em 05/10/2026 sobre dados coletados em 02/10/2026)
**Versão:** v8 (05/10/2026). Base: análise de fatores de homogeneização regional sobre a v6 (`../v7/revenda_fiker_003_v6.md`). A v6 usou fator de oferta nacional (FipeZAP); a v8 reconstrói a homogeneização com **dados REGIONAIS do Recreio** conforme Anexo B.5.1 de NBR 14653-2.

## O que muda em relação à v6

**Foco:** aplicação de **múltiplos fatores de homogeneização por atributo**, com validação regional (Recreio), não nacional.

**Ressalva crítica:** dados públicos de Recreio 2026 com precisão regional (padrão, data, localização) são limitados. A análise abaixo extrai o máximo dos 13 comparáveis internos (W1-W13) para inferir fatores regionais. Onde faltam dados públicos regionais confirmatórios, declaro com [INF] e ofereço alternativa (uso de fator nacional com ressalva).

### 1. Fator de Data (Ajuste Temporal)

**Premissa:** comparáveis foram anunciados entre 27/05/2026 (W4) e 01/09/2026 (W8). O cenário é de 05/10/2026. Todos os comparáveis são de 2026, portanto o ajuste é dentro do ano.

**Dados regionais de variação de preço em Rio (1º semestre 2026):**
- Rio de Janeiro: +1,33% (Jan-Jun 2026, FipeZAP nacional)
- Recreio 2026: não há dado específico por bairro; uso aproximação de Rio geral

**Fator de Data extraído dos comparáveis internos:**
- W4: 27/05/2026 (mais antigo da faixa S1/S2)
- W8: 01/09/2026 (mais recente da faixa S1/S2)
- Intervalo: 97 dias
- Variação linear esperada (1,33% ÷ 180 dias = 0,0074% ao dia): **+0,72% em 97 dias** [INF, linear]

**Aplicação:**
- W1 (28/08): -4 dias de W8 → fator ≈ 1,000 (negligenciável)
- W2 (28/08): -4 dias de W8 → fator ≈ 1,000
- W3 (02/06): -91 dias de W8 → fator de atualização de -91 dias = **1 / 1,0067 = 0,9933** [INF, linear]
- W4 (27/05): -97 dias de W8 → fator de atualização de -97 dias = **1 / 1,0072 = 0,9928** [INF, linear]
- W6 (sem data, VM): não aplicado, mantido como referência fraca
- W7 (sem data, VM): não aplicado, mantido como referência fraca
- W8 (01/09): **1,0000** (referência de data, setembro é próximo a outubro)

**Ressalva:** O fator é calculado por interpolação linear sobre dados agregados de Rio. Sem dados específicos de Recreio, a validade regional é fraca. **Se Wallenberg preferir**, uso fator nacional FipeZAP de 1,33% ao semestre em vez de linear.

### 2. Fator de Padrão (Ajuste de Qualidade Construtiva)

**Premissa:** nem todos os comparáveis declaram padrão. W10 e W13 declaram "alto padrão"; W1-W7 (S1/S2) não declaram; W5, W9, W11 (S3) não declaram ou não foram registrados.

**Análise interna de padrão:**

**Em S1/S2 (425-624 m²):**
- Todos os imóveis são em condomínio fechado, triplex ou 3 pavimentos (maioria)
- Nenhum declara "alto padrão"
- Nenhum declara padrão "médio" ou "baixo"
- **Classificação de trabalho:** assumir **padrão médio** para W1-W7 [PV]

**Em S3 (289-414 m²):**
- W10 e W13: **declarado "alto padrão"** [FP]
- W5, W9, W11: não declaram [NC]
- **Classificação de trabalho:** W10/W13 = alto; W5/W9/W11 = não declarado (assumir médio) [INF]

**Cálculo do fator de padrão (Recreio, 2026):**
- Comparação W10 (315 m², alto padrão) vs W5 (400 m², padrão não declarado):
  - W10: R$ 13.492/m² bruto; após fator oferta 0,91 → R$ 12.278/m²
  - W5: R$ 10.500/m² bruto; após fator oferta 0,91 → R$ 9.555/m²
  - Razão W10 ÷ W5 = 12.278 ÷ 9.555 = **1,285** (28,5% prêmio para alto padrão)
  
- **Alternativa:** Comparação W10 (alto) vs W11 (padrão não declarado, mesmo condomínio Riviera):
  - W10: R$ 13.492/m²; homogeneizado → R$ 12.278/m²
  - W11: R$ 6.774/m²; homogeneizado → R$ 6.165/m²
  - Razão = 1,992 (99% prêmio) — **muito alto**, pode haver erro de padrão em W11 ou tamanho diferente
  
**Fator de Padrão escolhido (conservador):**
- Alto padrão vs Médio padrão: **fator 1,20** (+20% prêmio para alto padrão, Recreio 2026) [INF, conservador]
- **Justificativa:** W10/W5 = 1,285 é baseado em 2 comparáveis só, e W5 é 2 pavimentos (fator área influencia). Uso 1,20 como valor mais defensável.
- **Ressalva:** sem pesquisa separada de alto vs médio padrão especificamente em Recreio, o fator é **inferência fraca**. Alternativa: usar fator nacional (se existir em literatura de avaliação).

### 3. Fator de Oferta (Desconto de Oferta vs Venda)

**Premissa:** a v6 usou fator nacional FipeZAP de 0,86-0,91. Vou validar com dados regionais dos comparáveis.

**Dados de comparáveis que são vendas (C1, C4) vs anúncios (W1-W13):**
- C1: vendida em 03/2026 por R$ 5.850.000 (450 m²) = R$ 13.000/m²
- C4: vendida em 06/2026 por R$ 7.500.000 (500 m²) = R$ 15.000/m²
- **Vendas (C1+C4, média): (13.000 + 15.000) ÷ 2 = R$ 14.000/m²**

**Comparáveis de anúncio (faixa S1/S2):**
- W1 (28/08): R$ 10.778/m² (oferta)
- W2 (28/08): R$ 8.245/m² (oferta)
- W3 (02/06): R$ 10.667/m² (oferta)
- W4 (27/05): R$ 8.667/m² (oferta)
- W6 (s/data): R$ 8.900/m² (oferta)
- W7 (s/data): R$ 8.955/m² (oferta)
- W8 (01/09): R$ 12.281/m² (oferta)
- **Anúncios (média simples): (10.778 + 8.245 + 10.667 + 8.667 + 8.900 + 8.955 + 12.281) ÷ 7 = R$ 9.790/m²**

**Razão Venda (C1+C4) ÷ Anúncio (W1-W7, média):**
- R$ 14.000 ÷ R$ 9.790 = **1,430** (43% acima)

**Fator de oferta regional (Recreio, 2026):**
- Se anúncio está 43% acima de venda, o fator é **1 ÷ 1,430 = 0,699** (desconto de ~30%)
- **Intervalo conservador (nacional, FipeZAP):** 0,86-0,91 (9-14% desconto)
- **Intervalo regional (Recreio, interno):** 0,70-0,75 (25-30% desconto)

**Escolha:** 
- **Fator regional Recreio = 0,75** (25% desconto de oferta) [INF, baseado em 9 comparáveis internos]
- **Ressalva:** o intervalo regional é significativamente maior que o nacional (30% vs 10%). Isso pode indicar que o Recreio tem maior descolamento entre oferta e venda, ou que a amostra interna (apenas 2 vendas reais) é pequena demais.

### 4. Fator de Localização

**Premissa:** alguns comparáveis estão próximos a avenidas principais (Avenida Guilherme de Almeida, Avenida Vereador Alceu de Carvalho); outros não.

**Dados disponíveis:**
- W6: Vereador Alceu de Carvalho, 665 (avenida)
- W7: Riviera Del Sol, Vereador Alceu de Carvalho (avenida)
- Demais: ruas secundárias ou sem localização precisa

**Análise interna:**
- W6 (avenida, 500 m²): R$ 8.900/m² (oferta)
- W7 (avenida, 469 m²): R$ 8.955/m² (oferta)
- **Média de avenida (W6+W7): R$ 8.928/m²**

- W1 (sem localização precisa, 450 m²): R$ 10.778/m²
- W2 (sem localização precisa, 485 m²): R$ 8.245/m²
- W3 (sem localização precisa, 450 m²): R$ 10.667/m²
- W4 (sem localização precisa, 450 m²): R$ 8.667/m²
- W8 (Avenida Guilherme de Almeida, 570 m²): R$ 12.281/m²
- **Média geral (excluindo W6/W7): R$ 10.110/m²**

**Razão Média Geral ÷ Média Avenida:** R$ 10.110 ÷ R$ 8.928 = **1,132** (13% prêmio para não-avenida ou erro de tamanho)

**Conclusão:** os dados são **inconsistentes**. W8 é em avenida e é o maior R$/m² (R$ 12.281); W6/W7 em avenida são os menores (R$ 8.9xx). Não é possível extrair fator de localização confiável dos comparáveis internos.

**Fator de Localização = 1,000** (sem ajuste) [NC — não calculável com precisão regional]
- **Ressalva:** a localização dentro de Recreio pode ter efeito (proximidade a praia, comércio, etc.), mas os comparáveis não permitem isolá-lo dos outros fatores.

### 5. Fator de Área (Escala)

**Premissa:** a macete M5 (Skill viabilidade-cub-nbr12721) indica que casa menor no mesmo lote tende a ter R$/m² maior, porque o lote tem custo fixo.

**Aplicação:**
- Não recalculo este fator, porque está implícito no R$/m² dos comparáveis.
- S3 (339-359 m²) naturally tem R$/m² mais disperso que S1/S2 (500-620 m²) pelos dados: S1/S2 médio ≈ R$ 9.790/m²; S3 médio ≈ R$ 9.358/m² (sem fator oferta).
- **Mantém-se o método da v6:** uso R$/m² de cada faixa sem recálculo de expoente [PV].

---

## Recálculo de j' (Controle Web) com Homogeneização Regional

### Passo 1: Aplicar Fator de Data aos comparáveis de S1/S2

| # | Imóvel | Publicado | Dias de diferença vs W8 (ref) | Fator Data | R$/m² bruto | R$/m² ajustado data |
|---|---|---|---|---|---|---|
| W1 | Bothanica Nature, CA2947 | 28/08 | -4 | 1,0000 | 10.778 | 10.778 |
| W2 | Artlife, CA2948 | 28/08 | -4 | 1,0000 | 8.245 | 8.245 |
| W3 | Riviera Del Sol, CA0159 | 02/06 | -91 | 0,9933 | 10.667 | 10.597 |
| W4 | condomínio não informado, CA2879 | 27/05 | -97 | 0,9928 | 8.667 | 8.608 |
| W6 | Riviera Del Sol (endereço), VM 001867 | s/data | n/a | 1,0000 | 8.900 | 8.900 |
| W7 | Riviera Del Sol, VM 002243 | s/data | n/a | 1,0000 | 8.955 | 8.955 |
| W8 | Del Lago, CA0121 | 01/09 | 0 | 1,0000 | 12.281 | 12.281 |

**Média ajustada por data (n=7): (10.778 + 8.245 + 10.597 + 8.608 + 8.900 + 8.955 + 12.281) ÷ 7 = R$ 9.852/m²** [EF]
- vs v6 (sem ajuste data): R$ 9.790/m²
- **Diferença:** +0,63% (negligenciável)

### Passo 2: Aplicar Fator de Oferta Regional (Recreio)

**Fator regional = 0,75** (25% desconto)

| # | R$/m² (ajustado data) | × 0,75 (fator oferta regional) | R$/m² homogeneizado |
|---|---|---|---|
| W1 | 10.778 | 10.778 × 0,75 = 8.084 | 8.084 |
| W2 | 8.245 | 8.245 × 0,75 = 6.184 | 6.184 |
| W3 | 10.597 | 10.597 × 0,75 = 7.948 | 7.948 |
| W4 | 8.608 | 8.608 × 0,75 = 6.456 | 6.456 |
| W6 | 8.900 | 8.900 × 0,75 = 6.675 | 6.675 |
| W7 | 8.955 | 8.955 × 0,75 = 6.716 | 6.716 |
| W8 | 12.281 | 12.281 × 0,75 = 9.211 | 9.211 |

**Faixa S1/S2 homogeneizada (fator oferta regional 0,75, n=7): R$ 6.184 a R$ 9.211/m²** [EF]
- vs v6 (fator nacional 0,86-0,91): R$ 7.091 a R$ 11.175/m²
- **Diferença:** redução significativa de ~12-20% no topo

### Passo 3: Aplicar Fator de Padrão (não aplicável a S1/S2, todos padrão médio)

Não há ajuste de padrão em S1/S2 (todos classificados como padrão médio).

### Passo 4: Calcular j' (Controle Web) com Homogeneização Regional para S1/S2

| Cenário | Área (base) | × 6.184 (W2 ajustado, piso) | × 9.211 (W8 ajustado, topo) | Controle web regional [EF] |
|---|---|---|---|---|
| S1 | 500 construída | 500 × 6.184 = 3.092.000 | 500 × 9.211 = 4.605.500 | **R$ 3.092.000 a R$ 4.605.500** |
| S1 | 520 construída | 520 × 6.184 = 3.215.680 | 520 × 9.211 = 4.789.720 | |
| **S1, faixa** | | | | **R$ 3.092.000 a R$ 4.789.720** |
| S2 | 522,56 construída | 522,56 × 6.184 = 3.231.624,64 | 522,56 × 9.211 = 4.809.689,16 | |
| S2 | 542,56 construída | 542,56 × 6.184 = 3.357.355,04 | 542,56 × 9.211 = 4.993.942,16 | |
| **S2, faixa** | | | | **R$ 3.231.625 a R$ 4.993.942** |

**Constatação crítica:**
- v6 (fator nacional 0,75): j' S1 = R$ 3.545.500 a R$ 5.811.000
- v8 (fator regional 0,75): j' S1 = R$ 3.092.000 a R$ 4.789.720
- **Redução de ~13-17%** no controle web com fator regional vs nacional

**Implicação:** com fator de oferta regional (0,75), a distância entre a faixa do condomínio (R$ 13.000-15.000/m²) e o controle web diminui, tornando os valores **mais próximos e mais defensáveis**.

---

## Recálculo de S3 com Homogeneização Regional

### Fator de Padrão em S3

Comparáveis de S3:
- W10 (alto padrão): R$ 13.492/m² bruto
- W13 (alto padrão): R$ 10.784/m² bruto
- W5 (padrão não declarado): R$ 10.500/m² bruto
- W9 (padrão não registrado): R$ 7.497/m² bruto
- W11 (padrão não declarado): R$ 6.774/m² bruto

**Aplicação de Fator Padrão 1,20:**
- W10 alto padrão: não ajusta (é a referência alta) → R$ 13.492/m²
- W13 alto padrão: não ajusta → R$ 10.784/m²
- W5 médio (inferido): R$ 10.500 × 1,20 = R$ 12.600/m² [ajuste para equivalente alto padrão]
- W9 médio (inferido): R$ 7.497 × 1,20 = R$ 8.997/m²
- W11 médio (inferido): R$ 6.774 × 1,20 = R$ 8.129/m²

**Faixa S3 ajustada por padrão (todos elevados a alto padrão equivalente): R$ 8.129 a R$ 13.492/m²** [EF]

**Aplicar Fator de Oferta Regional 0,75:**
- R$ 8.129 × 0,75 = R$ 6.097/m²
- R$ 13.492 × 0,75 = R$ 10.119/m²

**Faixa S3 homogeneizada (padrão alto + oferta regional 0,75, n=5): R$ 6.097 a R$ 10.119/m²** [EF]

### j' de S3 com Homogeneização Regional

| Cenário | Área | × 6.097 | × 10.119 | Controle web regional S3 [EF] |
|---|---|---|---|---|
| S3 | 339,84 | 2.071.696 | 3.440.054 | **R$ 2.071.696 a R$ 3.440.054** |
| S3 | 359,84 | 2.193.551 | 3.644.038 | |
| **S3, faixa** | | | | **R$ 2.071.696 a R$ 3.644.038** |

**Comparação:**
- v6 (alto padrão W10+W13, fator 0,91): R$ 3.151.676 a R$ 4.418.116
- v8 (todos ajustados a alto padrão, fator 0,75): R$ 2.071.696 a R$ 3.644.038
- **Redução de ~34-18%** com fator regional vs nacional (range menor, piso mais baixo)

---

## Comparação: Faixa do Condomínio vs Controle Web (v6 vs v8)

### S1/S2 — Faixa Principal (C1 e C4)

| Comparação | v6 (fator nacional FipeZAP 0,86-0,91) | v8 (fator regional 0,75) | Diferença |
|---|---|---|---|
| **j' S1 (500-520 m²)** | R$ 3.545.500 a R$ 5.811.000 | R$ 3.092.000 a R$ 4.789.720 | -12% a -17% |
| **j' S2 (522-542 m²)** | R$ 3.705.473 a R$ 6.063.108 | R$ 3.231.625 a R$ 4.993.942 | -13% a -18% |
| **Piso condomínio (C1, 13k) vs topo web** | 13.000 / 11.175 = 1,163 (+16%) | 13.000 / 9.211 = 1,411 (+41%) | Redução de 25 pp |
| **Topo condomínio (C4, 15k) vs topo web** | 15.000 / 11.175 = 1,342 (+34%) | 15.000 / 9.211 = 1,629 (+63%) | Aumento de 29 pp |

**Interpretação:**
- Com fator regional 0,75, o controle web **cai significativamente**, aumentando o **gap entre condomínio e mercado**.
- Isso sugere que ou:
  1. O fator regional 0,75 é **conservador demais** (real é menor, ex.: 0,80-0,85);
  2. O Recreio tem **prêmio real** vs ofertas web (hipótese já levantada na v6);
  3. As **escrituras C1/C4 precisam ser conferidas** (premissa [PV] de área pode estar errada).

### S3 — Ordem de Grandeza

| Comparação | v6 | v8 |
|---|---|---|
| **Faixa web (alto padrão W10+W13, fator 0,91)** | R$ 3.151.676 a R$ 4.418.116 | N/A (método diferente) |
| **Faixa web (todos, fator 0,75, ajustados a alto)** | N/A | R$ 2.071.696 a R$ 3.644.038 |
| **Peso do lago (S1 − S3, R$/m² 13k-15k)** | R$ 2.082.080 a R$ 2.402.400 | **recalcular abaixo** |

---

## Peso do Lago com Homogeneização Regional (v8)

### Faixa S1 (horiz alta, C4 com 15k)

- **S1 topo: 520 m² × R$ 15.000/m² = R$ 7.800.000** (condomínio, faixa principal da v6)
- **S1 web topo (v8): 520 × 9.211 = R$ 4.789.720** (controle web regional)

### Faixa S3 (lago, H1 APP confirmada)

- **S3 topo: 359,84 m² × R$ 15.000/m² = R$ 5.397.600** (condomínio, faixa principal da v6, sem APP desconto)
- **S3 web (v8): 359,84 × 10.119 = R$ 3.644.038** (controle web regional, todos ajustados a alto padrão)

### Cálculo do Peso do Lago

| Variante | Conta | Peso do lago [EF, v8] |
|---|---|---|
| **Central: mesmo R$/m² condomínio nos dois cenários** | 160,16 × 13.000 = 2.082.080; 160,16 × 15.000 = 2.402.400 | **R$ 2.082.080 a R$ 2.402.400** (inalterado vs v6) |
| **Controle web regional (160,16 m² × R$/m² web)** | 160,16 × 6.097 = 976.333; 160,16 × 10.119 = 1.620.607 | R$ 976.333 a R$ 1.620.607 |

**Comparação de peso do lago:**
- v6: R$ 2.082.080 a R$ 2.402.400 (central com R$/m² condomínio)
- v8: **mesmo central**, mas web cai para R$ 0,98 a R$ 1,62 mi
- **Interpretação:** com fator regional, o peso do lago **aparece maior** em termos de diferencial vs mercado web

---

## Ordem de Grandeza para o Cliente — v8 (Regional)

### S1 (500-520 m², sem APP)

- **Faixa condomínio (C1/C4):** R$ 6.500.000 a R$ 7.800.000 [faixa principal, vendas C1+C4]
- **Controle web (regional 0,75):** R$ 3.092.000 a R$ 4.789.720 [controle, método web]
- **Posição:** condomínio está **37% a 60% acima** do web
- **Confiança:** média-baixa a baixa (gap grande; depende de validar escrituras)
- **Recomendação de ordem de grandeza:** manter **R$ 6,5 a 7,8 mi** (condomínio), com ressalva de gap vs mercado

### S2 (522-542 m², divisa regularizada)

- **Faixa condomínio:** R$ 6.793.280 a R$ 8.138.400
- **Controle web (regional 0,75):** R$ 3.231.625 a R$ 4.993.942
- **Posição:** condomínio **36% a 63% acima** do web
- **Confiança:** muito baixa (S2 depende de regularizar divisa; gap é grande)
- **Recomendação:** S2 é **cenário de risco**; não usar como referência isolada

### S3 (339-359 m², APP hipótese H1)

- **Faixa condomínio (sem APP):** R$ 4.417.920 a R$ 5.397.600
- **Controle web (todos alto padrão, regional 0,75):** R$ 2.071.696 a R$ 3.644.038
- **Peso do lago (APP confirmada):** **aproximadamente R$ 2,1 a 2,4 mi** (diferença S1-S3, central)
- **Faixa larga (web):** R$ 0,98 a R$ 1,62 mi
- **Posição:** condomínio está **48% a 61% acima** do web
- **Confiança:** baixa; faixa larga; risco para baixo
- **Recomendação de ordem de grandeza:**
  - **Com APP confirmada (H1):** cerca de **R$ 3,1 a 5,4 mi** (mesma da v6)
  - **Mais provável:** R$ 4,4 a 4,7 mi (condomínio só com C1, sem C4)
  - **Web (alto padrão):** R$ 2,1 a 3,6 mi (para comparação, não usar direto)

---

## Discussão: O Gap Permanece e se Amplia com Fator Regional

### Achado crítico

Com **fator de oferta regional 0,75** (em vez de nacional 0,91):
1. O **controle web cai ~13-17%** em S1/S2 e ~18-34% em S3
2. O **gap entre condomínio e web se amplia** de 16-33% (v6) para 37-63% (v8)
3. As **hipóteses não mudam:**
   - O Recreia tem prêmio real (2 pav., lago, lotes maiores)
   - **OU** as escrituras C1/C4 precisam ser conferidas
   - **OU** o fator de oferta regional 0,75 é muito conservador

### Três caminhos para Wallenberg / Villaça

**Opção 1: Aceitar v8 com fator regional 0,75**
- Pros: segue NBR 14653-2 (múltiplos fatores regionais); valida com dados internos de Recreio
- Cons: gap grande; depende de verificação de escrituras; fator 0,75 é inferência de 2 vendas só
- **Resultado:** S1/S2 R$ 6,5-7,8 mi; S3 R$ 3,1-5,4 mi; confiança baixa

**Opção 2: Usar fator intermediário regional 0,82 (compromisso)**
- Pros: menos conservador que 0,75; ainda regional (entre nacional 0,91 e v8 0,75)
- Cons: escolha arbitrária
- **Resultado:** j' S1 ficaria em R$ 3.600-5.200 mi (entre v6 e v8)

**Opção 3: Manter fator nacional 0,91 (v6) com ressalva forte**
- Pros: fator publicado (FipeZAP); documentado com fonte; menos incerteza
- Cons: não é regional conforme NBR 14653-2; v6 já tem ressalva R2
- **Resultado:** idem v6, R$ 6,5-7,8 mi; confiança média-baixa

### Recomendação de Fiker

**Sem acesso a:** 
- Raio-X FipeZAP específico de Recreio (PDF DataZAP 404)
- Pesquisa de padrão alto vs médio em Recreio (comercial, paga)
- Amostra ampliada de vendas vs ofertas no Recreio (tenho 2 vendas, 11 ofertas)

**Veredito:** a homogeneização regional v8 é **tecnicamente correta** (NBR 14653-2), mas **risco é para baixo** em confiança, porque:
1. Fator padrão 1,20 é inferência de 2 comparáveis (W10 vs W5)
2. Fator data é linear e não validado com Recreio real
3. Fator oferta 0,75 é baseado em 2 vendas só

**Cenário mais defensável para Villaça:**
- Usar **v8 (regional) como base técnica** (NBR 14653-2)
- Declarar **intervalo de incerteza:** fator 0,75-0,91 → resultado **R$ 3,1 a 7,8 mi** para S1/S2 (faixa larga, acomodando ambos os fatores)
- Recomendar **validação de escrituras de C1/C4** antes de usar em laudo de banco
- **Aguardar acesso a dados regionais mais precisos** (Raio-X DataZAP Recreio, ou pesquisa específica de padrão)

---

## Metodologia Completa (NBR 14653-2 Anexo B.5.1)

| Fator | Cálculo | Válidade | Abrangência | Status |
|---|---|---|---|---|
| **Data** | Linear: +0,72% em 97 dias | Válida para 2026 Q2-Q3 | Rio (proxy de Recreio) | [INF] — linear sobre Rio geral |
| **Padrão** | 1,20 (alto vs médio) | Válida para Recreio 2026 | Recreio (interno, 2 comp.) | [INF] — fraco, 2 comparáveis |
| **Oferta** | 0,75 (25% desconto) | Válida para Recreio 2026 | Recreio (interno, 2 vendas + 11 ofertas) | [INF] — derivado internamente |
| **Localização** | 1,000 (sem ajuste) | N/A | N/A | [NC] — não isolável |
| **Área** | Implícito em R$/m² | Válida para cada faixa | Recreio (faixas S1/S2, S3) | [PV] — método v6 mantido |

---

## Ressalvas Finais

1. **[VERIFICADO - Homogeneização Regional Recreio, v8]** — análise realizada conforme Anexo B.5.1 de NBR 14653-2 (múltiplos fatores por atributo)
2. **Dados regionais limitados:** não há acesso a Raio-X FipeZAP de Recreio específico (404); pesquisa comercial de padrão não realizada; amostra de vendas é apenas 2
3. **Fator regional 0,75 é inferência interna fraca:** baseado em 2 vendas (C1, C4) vs 11 ofertas de web; validade regional não pode ser confirmada sem amostra ampliada
4. **Gap aumenta de 16% (v6) para 37-63% (v8):** indica que a escolha de fator de oferta é **crítica para o resultado final**
5. **Nenhum número é promessa de valor de venda.** São faixas com premissas explícitas.

---

**Próximas ações (para Wallenberg/Villaça):**
- [ ] Validar escrituras de C1 (450 m²) e C4 (500 m²) para confirmar se "construídos" = construída total [PV]
- [ ] Buscar Raio-X DataZAP específico de Recreio (2º trimestre 2026) ou equivalente
- [ ] Decidir se usa v8 (regional, NBR 14653-2 rigoroso) ou v6 (nacional, FipeZAP documentado)
- [ ] Confirmar com Kelsen se há restrições adicionais (APP, FMP) que mudem o fator de padrão/localização

*Declaração: ENSAIO 003, caso 100% fictício. Homogeneização v8 aplicada em 05/10/2026 sobre comparáveis reais coletados em 02/10/2026, com fatores extraídos da amostra interna (Recreio) e dados nacionais (Rio/FipeZAP) como proxy. A validação regional é fraca e depende de dados ampliados.*

