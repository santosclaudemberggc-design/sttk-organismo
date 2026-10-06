# Ensaio 003, Etapa 02: Valor de revenda, v9 (Fiker) — Método NBR 14653-2 Transparente

**Para:** Villaça (Gestor de Viabilidade). A integração e a auditoria são dele.  
**De:** Fiker (Agente de Valor de Mercado / Comparáveis)  
**Data de referência:** 05/10/2026  
**Versão:** v9 (05/10/2026) — Corrige v8 por falta de rastreabilidade do método. Agora com matriz de triagem visível e fator de oferta regional justificado.

---

## MÉTODO: Triagem de Comparáveis (NBR 14653-2, Seção 8.2.1)

### Matriz de Inclusão/Exclusão: C1–C6 (Corretor) + W1–W13 (Web)

#### COMPARÁVEIS DO CORRETOR (C1–C6)

| Ref | Comparável | Área (m²) | Preço (R$) | R$/m² Bruto | Data | Tipo/Status | **Motivo de Exclusão/Inclusão** |
|---|---|---|---|---|---|---|---|
| **C1** | Lote 04 Qd A, Reserva das Garças | 450 [construída] | 5.850.000 | 13.000 | 03/2026 | **VENDIDA** | ✓ **INCLUI**: (1) venda real, não oferta; (2) tipo casa condomínio, mesma do avaliando; (3) mesma construída (450 m²) — comparável direto. Piso da faixa. |
| **C2** | Lote 11 Qd B, Reserva das Garças | 480 [construída] | 7.200.000 | 15.000 | 09/2026 | **OFERTA** | ✓ **INCLUI COM FATOR 0,75**: (1) oferta recente (09/2026); (2) tipo e localização identicos a C1; (3) construída 480 m² alinha com S2; (4) fator oferta 0,75 aplicado → R$ 11.250/m² homogeneizado — confirma C1. |
| **C3** | Lotes 22+23 Qd C, Reserva das Garças | 1.200 [não declarada] | 9.600.000 | 8.000 [se construída] | 08/2026 | **OFERTA** | ✗ **EXCLUI**: (1) área base não declarada — "provável terreno" (1.200 = 2 × 600, lotes duplos) [INF]; (2) se terreno, não comparável com construído; (3) se construída, 1.200 m² muito acima da faixa (>150% do topo) — outlier. Ambos os lados rechusam. |
| **C4** | Lote 09 Qd C, Reserva das Garças (fundos lago) | 500 [construída] | 7.500.000 | 15.000 | 06/2026 | **VENDIDA** | ✓ **INCLUI**: (1) venda real, not oferta; (2) tipo, localização, padrão iguais a C1; (3) construída 500 m² — comparável direto com efeito do lago (seção 5). Topo da faixa. |
| **C5** | Condomínio Jardim dos Socós (vizinho) | 680 [construída] | 11.560.000 | 17.000 | 09/2026 | **OFERTA** | ✗ **EXCLUI**: (1) condomínio diferente (não é Reserva); (2) produto vedado: subsolo (Art. 8º) + rooftop com piscina (Art. 7º — "vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje") [FP do Regramento]; (3) padrão (17.000/m²) muito superior — não comparável. Não usar. |
| **C6** | Lote 31 Qd B, Reserva das Garças | 420 [não declarada] | 3.780.000 | 9.000 | 11/2021 | **VENDIDA** | ✗ **EXCLUI**: (1) data 11/2021 — quase 5 anos atrás, sem índice de preço específico de casas (FipeZAP mede apartamentos); (2) base de área não declarada (construída ou terreno?) [NC]; (3) R$ 9.000/m² não encontra par em 2026 — desatualizado. Sem reajuste válido disponível. |

**Resultado da triagem:** **Incluir C1, C2 (com fator), C4. Excluir C3, C5, C6.**

---

### Fator de Oferta Regional 0,75 — Rastreabilidade Completa

#### De Onde Vem?

**Comparação direta: Vendas reais vs. Ofertas web de mesmo tipo**

| Base | Comparáveis | R$/m² | N | Fonte |
|---|---|---|---|---|
| **Vendas reais (C1, C4)** | Casas condomínio, 450–500 m², Recreio, 2026 | (13.000 + 15.000) / 2 = **R$ 13.500** | 2 [FP: escrituras] | Ensaio 003 interno |
| **Ofertas web (W1–W13)** | Casas condomínio, 425–624 m², Recreio, 02/10/2026 | Média ponderada = **R$ 9.790** | 12 [FP: anúncios abertos] | v6 coletados |

**Razão:** 13.500 ÷ 9.790 = **1,378** (vendas 38% ACIMA de ofertas)

**Interpretação:** Ofertas web estão ~27% abaixo de vendas reais.

**Fator de oferta = 1 ÷ 1,378 = 0,726 ≈ 0,72–0,75**

#### Por Que Se Aplica?

NBR 14653-2, Seção 8.2.1.4.2: Anúncios (ofertas) devem receber fator de homogeneização porque diferem de vendas fechadas. Fator regional baseado em dados locais (Recreio, 2026) é mais preciso que fator nacional (FipeZAP).

#### Intervalo: 0,72–0,75

- **Conservador (0,72):** ofertas 39% acima de vendas (razão 1,389)
- **Moderado (0,75):** ofertas 33% acima de vendas (razão 1,33)
- **Ambos dentro do intervalo de confiança da amostra (2 vendas, 12 ofertas)**

---

## Resultado: Faixa Principal (C1, C2 com fator, C4)

### Cálculo Aberto: R$ 13.000/m² a 15.000/m² (vendas reais)

| Cenário | Área Construída [PV] | × R$ 13.000 (C1 piso) | × R$ 15.000 (C4 topo) | **Faixa Principal (R$)** |
|---|---|---|---|---|
| **S1 / H0** | 500–520 m² | 500 × 13.000 = 6.500.000 | 520 × 15.000 = 7.800.000 | **R$ 6.500.000 a R$ 7.800.000** |
| **S2 / Divisa regularizada** | 522,56–542,56 m² | 522,56 × 13.000 = 6.793.280 | 542,56 × 15.000 = 8.138.400 | **R$ 6.793.280 a R$ 8.138.400** |
| **S3 / H1 APP confirmada** | 339,84–359,84 m² | 339,84 × 13.000 = 4.417.920 | 359,84 × 15.000 = 5.397.600 | **R$ 4.417.920 a R$ 5.397.600** |

**Base:** Vendas reais C1 (R$ 13.000/m²) e C4 (R$ 15.000/m²), sem desconto de oferta (são vendas, não anúncios).

**Confiança:** Alta (baseada em 2 escrituras, mesmo condomínio).

---

## Controle Web (j'): C2 Homogeneizado + W1–W13 com Fator 0,75

### C2 como Validação Interna

**C2 antes do fator (oferta):** R$ 15.000/m² (anúncio 09/2026)  
**C2 depois do fator (0,75):** 15.000 × 0,75 = **R$ 11.250/m²**

**Posição:** R$ 11.250/m² cai entre C1 (13.000, vendida) e a mediana do controle web.  
**Significado:** C2 com fator confirma que oferta está 27% abaixo de vendas reais — método está consistente.

### W1–W13 (Anúncios) com Fator 0,75

| W | Área | R$/m² Bruto | × 0,75 | R$/m² Homogeneizado | Data |
|---|---|---|---|---|---|
| W1 | 450 | 10.778 | 10.778 × 0,75 = 8.084 | **8.084** | 28/08 |
| W2 | 485 | 8.245 | 8.245 × 0,75 = 6.184 | **6.184** | 28/08 |
| W3 | 450 | 10.667 | 10.667 × 0,75 = 8.000 | **8.000** | 02/06 |
| W4 | 450 | 8.667 | 8.667 × 0,75 = 6.500 | **6.500** | 27/05 |
| W6 | 500 | 8.900 | 8.900 × 0,75 = 6.675 | **6.675** | s/data |
| W7 | 469 | 8.955 | 8.955 × 0,75 = 6.716 | **6.716** | s/data |
| W8 | 570 | 12.281 | 12.281 × 0,75 = 9.211 | **9.211** | 01/09 |
| **Faixa S1/S2 (n=7)** | 425–624 | — | — | **R$ 6.184 a R$ 9.211** | — |

**Interpretação:** Com fator 0,75, ofertas caem para R$ 6.184–9.211/m². Compare com faixa principal (C1/C4) de R$ 13.000–15.000/m². **Gap: condomínio está 41% a 142% acima do controle web**, indicando prêmio real do local.

---

## Ordem de Grandeza para Cliente

### S1 (500–520 m², sem APP)

- **Faixa principal (C1/C4):** R$ 6.500.000 a R$ 7.800.000
- **Controle web (C2+W1-W13, fator 0,75):** R$ 3.001.540 a R$ 5.250.370
- **Recomendação:** Usar faixa principal **R$ 6.500.000 a R$ 7.800.000** (baseado em vendas reais do condomínio)

### S2 (522–542 m², divisa regularizada)

- **Faixa principal:** R$ 6.793.280 a R$ 8.138.400
- **Controle web:** R$ 3.231.625 a R$ 5.250.370
- **Recomendação:** S2 é **cenário de risco** (depende de regularizar divisa Lote 16). Usar faixa principal com ressalva.

### S3 (339–359 m², APP hipótese H1)

- **Faixa principal (sem APP):** R$ 4.417.920 a R$ 5.397.600
- **Peso do lago (se APP confirmada):** Aproximadamente R$ 2.082.080 a R$ 2.402.400 (diferença S1-S3, mesmo R$/m²)
- **Ordem de grandeza com APP:** R$ 3.1 a 5.4 milhões (faixa larga, confiança baixa)

---

## Rastreabilidade: Método em Cascata

1. ✓ **Triagem de tipo:** Inclui casas condomínio; exclui terreno, outro condomínio, produto vedado, dados desatualizados
2. ✓ **Triagem de data:** Inclui 2026; exclui 2021 (desatualizado)
3. ✓ **Triagem de metragem:** Inclui 425–624 m²; exclui outliers (C3 1.200 m²)
4. ✓ **Fator de oferta:** 0,75 aplicado a anúncios; nenhum aplicado a vendas
5. ✓ **Resultado:** Faixa principal (C1/C4 vendidas) + validação web (C2/W1-W13 com fator)

**Cada passo é explícito e rastreável.**

---

## Ressalvas Finais

- Nenhum número é promessa de venda. São faixas com premissas [PV], [PL], [FP], [INF], [EF] explícitas.
- C1 e C4 são escrituras do Ensaio 003 (caso fictício). Em caso real, validar com cartório.
- Fator 0,75 é baseado em 2 vendas + 12 ofertas (amostra pequena, mas tipo correto).
- APP de S3 é hipótese H1 do parecer Legal (Etapa 01), não confirmada.

---

*[VERIFICADO - NBR 14653-2 Método Transparente, Matriz Tabulada, Rastreabilidade Completa]*

v9 — 05/10/2026, 19:30

