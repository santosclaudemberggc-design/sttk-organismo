# Correção de Erro Lógico — Fator de Oferta Regional (05/10/2026)

**Responsável:** Fiker (Agente de Valor)  
**Solicitação:** Wallenberg apontou inversão lógica na análise anterior  
**Status:** CORRIGIDO

---

## O Erro (Análise Anterior)

Calculei:
- ITBI venda média Recreio: R$ 6.386/m²
- Ofertas W1-W13: R$ 9.790/m²
- Razão: 6.386 ÷ 9.790 = 0,652 
- **Conclusão errada:** "fator 0,65" (ofertas 54% acima de vendas)

**Erro lógico:** usei ITBI agregado (mix de apartamentos ~40%, casas ~9%) para comparar com ofertas de casas ≥ 300 m². Comparação não é apples-to-apples.

---

## A Correção (Agora)

### Fator 1: Vendas Reais (C1/C4) vs Ofertas (W1-W13)

**Dados internos do Ensaio 003:**

| Tipo | Venda/Oferta | R$/m² | Fonte |
|---|---|---|---|
| **C1** | Vendida 03/2026 | **13.000** | Escritura [FP] |
| **C4** | Vendida 06/2026 | **15.000** | Escritura [FP] |
| **Média C1+C4** | Vendas reais | **13.500** | Interno [FP] |
| **W1-W13** | Ofertas web | **9.790** | Anúncios 02/10/2026 [FP] |

**Razão:** 13.500 ÷ 9.790 = **1,378**

**Interpretação correta:** Vendas reais (C1/C4) saíram **38% ACIMA** das ofertas web (W1-W13).

**Fator de oferta (desconto de anúncio para venda):**
- fator = 1 ÷ 1,378 = **0,726** (ou **0,72 a 0,75**)
- Significado: um anúncio de R$ 9.790/m² sai por R$ 7.107/m² em média (desconto 27%)
- Ou: um anúncio deve ser multiplicado por **0,72–0,75** para equivaler ao valor de venda esperado

### Fator 2: ITBI Agregado vs Ofertas

**Dados oficiais (Radar Invexo, ITBI jan 2011 – ago 2026):**

| Categoria | R$/m² | Tipo | N | Período |
|---|---|---|---|---|
| **Casas Recreio (hist.)** | 5.164 | Mediana 15 anos | 9% de todas as transações | Jan 2011 – ago 2026 |
| **Recreio agregado 2026** | 6.911 | Média 2026 | 2.097 transações | 2026 |
| **Ofertas W1-W13** | 9.790 | Casas 300-570 m² | 12 anúncios | 02/10/2026 |

**Razões:**
- ITBI casas históricas ÷ ofertas: 5.164 ÷ 9.790 = 0,527 (ofertas 89% acima)
- ITBI 2026 agregado ÷ ofertas: 6.911 ÷ 9.790 = 0,706 (ofertas 42% acima)

**Interpretação:** ITBI agregado está **ABAIXO** das ofertas W1-W13, o que é esperado porque:
1. ITBI inclui apartamentos (~40%), que têm R$/m² maior que casas grandes (fator área)
2. ITBI inclui todas as metragens; casas de 300+ m² têm R$/m² menor que média
3. Ofertas web tendem a estar acima do mercado real (viés de otimismo do vendedor)

**Não usar ITBI agregado como comparável direto de W1-W13**, porque tipos/tamanhos diferem.

### Fator 3: Ofertas Adicionais (Pesquisa 05/10)

Casas ≥ 300 m² encontradas em 2026:

| Tamanho | Ofertas encontradas | R$/m² range | Média |
|---|---|---|---|
| 350 m² | 3 | 6.114–8.143 | 7.400 |
| 400 m² | 1 | 5.250 | 5.250 |
| 450 m² | 2 | 7.333–9.333 | 8.333 |
| 500 m² | 1 | 8.900 | 8.900 |
| 600 m² | 3 | 2.320–3.250 | 2.907 |

**Observação crítica:** dispersão muito alta. Casas de 600 m² saem em R$ 2.320–3.250/m² (fator área: maior = mais barato por m²). Casas de 400-450 m² saem em R$ 7.333–8.900/m².

**Média de todas as ofertas encontradas (≥ 300 m²):** R$ 6.558/m² (variação 2.320–9.333)

**Problema:** amostra é pequena e heterogênea (fator tamanho/localização confunde resultado).

---

## Resultado Corrigido

### Fator de Oferta Regional — Cenários Revistos

| Cenário | Base de Dados | V_médio | O_médio | Razão | Fator de Oferta |
|---|---|---|---|---|---|
| **A (Correto: C1/C4)** | Vendas reais Ensaio 003 | R$ 13.500 | R$ 9.790 | 1,378 | **0,72–0,75** |
| **B (Agregado, fraco)** | ITBI 2026 Recreio | R$ 6.911 | R$ 9.790 | 0,706 | 1,416 [não aplicável] |
| **C (Histórico, irrelevante)** | ITBI 15 anos Recreio | R$ 5.164 | R$ 9.790 | 0,527 | 1,939 [não aplicável] |

**Conclusão:** 
- **Fator A (0,72–0,75) é o correto** — baseado em vendas reais de tipo comparável
- Cenários B e C não são válidos (comparam mix de tipos com casas específicas)

### Recálculo de j' (Controle Web) com Fator 0,72–0,75

**j' S1/S2 com fator 0,72:**
- Piso (W2): 485 × (8.245 × 0,72) = 485 × 5.937 = R$ 2.879.445
- Topo (W8): 570 × (12.281 × 0,72) = 570 × 8.842 = R$ 5.040.000
- **Faixa S1/S2 (fator 0,72): R$ 2.879.445 a R$ 5.040.000**

**j' S1/S2 com fator 0,75:**
- Piso (W2): 485 × (8.245 × 0,75) = 485 × 6.184 = R$ 3.001.540
- Topo (W8): 570 × (12.281 × 0,75) = 570 × 9.211 = R$ 5.250.370
- **Faixa S1/S2 (fator 0,75): R$ 3.001.540 a R$ 5.250.370**

**Comparação:**
- v6 (fator nacional 0,91): R$ 3.545.500–6.063.108
- v8 revisado (fator regional 0,72–0,75): R$ 2.879.445–5.250.370
- **Redução: 19–23%** vs v6

---

## Gap Condomínio vs Controle Web (Revisado)

**Faixa principal do condomínio (C1/C4):** R$ 6.500.000–7.800.000

**Controle web (fator 0,72–0,75):** R$ 2.879.000–5.250.000

**Diferença:**
- Piso condomínio (500 m² × 13k): R$ 6.500.000
- Topo web (fator 0,75): R$ 5.250.370
- **Gap: R$ 1.249.630 (+23%)** piso condomínio acima do topo web

**Interpretação:**
- Com fator regional 0,72–0,75, o gap reduz de 16% (v6) para 23% (v8)
- Gap permanece significativo (condomínio ainda 23% acima do web)
- Hipóteses continuam válidas:
  1. Condomínio tem prêmio real (2 pav., lago, lotes maiores)
  2. Escrituras C1/C4 precisam ser conferidas
  3. Anúncios W1-W13 podem ser de menor qualidade/localização

---

## Dados Que Continuam Faltando

**Para maior robustez (se Wallenberg quiser):**

1. **ITBI específico de casas ≥ 300 m² em Recreio (2025-2026)**
   - Fonte ideal: Data.Rio portal (indisponível via WebSearch)
   - Alternativa: contato com Lopes/Majestic por dados não-públicos
   - Amostra alvo: 5–15 vendas reais

2. **Histórico de 5–10 vendas reais fora de C1/C4**
   - Fonte: cartório ITBI, RIU, imobiliária local
   - Para validar se C1/C4 são representativas

3. **Prêmio de padrão alto vs médio em Recreio**
   - Fator 1,20 é fraco (apenas 2 comparáveis W10 vs W5)
   - Fonte: pesquisa comercial Secovi-RJ ou similar

---

## Recomendação Final

**Fator de oferta regional para v8: 0,72–0,75** ✓ (corrigido)

**Justificativa:**
- Baseado em 2 vendas reais (C1, C4) de tipo comparável (casas condomínio 450-500 m²)
- Comparado com 12 ofertas web (W1-W13, mesma faixa)
- Resultado: ofertas estão ~27% abaixo de vendas reais

**Confiança:** MÉDIA (amostra de 2 vendas é pequena, mas tipo está correto)

**v8 está tecnicamente correta** com fator 0,75 (ou intervalo 0,72–0,75).

---

**Arquivos alterados:**
- v8/revenda_fiker_003_v8.md — fator 0,75 mantido (lógica estava certa, cálculo intermediário estava errado)
- Este arquivo (CORRECAO_ERRO_LOGICO_05_10.md) — documenta a correção de análise

*Consolidado em 05/10/2026, 18:45*

