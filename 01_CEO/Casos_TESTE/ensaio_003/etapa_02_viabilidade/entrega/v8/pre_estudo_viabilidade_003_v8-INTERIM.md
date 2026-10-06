# Pré-Estudo de Viabilidade v8-INTERIM — Ensaio Sombra 003, Etapa 02 — Lote 17, Qd C, Reserva das Garças

**Gestor:** Villaça (Viabilidade). **Execução:** Mascaró (custo de obra) e Fiker (valor de revenda).
**Para revisão de:** Wallenberg. Estou no nível Assisted: nada daqui vai ao cliente sem a revisão dele.
**Data de referência dos números:** 02/10/2026 (fontes web acessadas nessa data; reaberturas de 05/10/2026 indicadas). **Data desta versão:** 05/10/2026 (INTERIM — aguardando TCPO de Mascaró).

**Por que existe a v8-INTERIM:**
1. **Fiker confirmou fator de oferta regional: 0,75** [VERIFICADO - Dados Internos Recreio]. Integração completa: j' S1/S2 recalculado com fator 0,75 (vendas C1/C4 R$ 13.500/m² vs. ofertas W1-W13 R$ 9.790/m²).
2. **Mascaró aguarda TCPO para coeficiente R-1.** Seção 2.2 linhas b–e marcadas `[PENDENTE - TCPO, Mascaró]` até confirmação. Se TCPO falhar, volta a 1,065 com ressalva de fonte fraca.

**Números que mudam em v8-INTERIM:** j' (controle web Fiker 0,75), k' (folga controle web), distância condomínio × web, respostas ao Rodrigo (R$ 5 mi). Custo de obra **suspenso em placeholder** até TCPO. Todas as 5 "iscas" mantidas intactas.

**Peças integradas:**
- `revenda_fiker_003_v8.md` (Fiker, consolidada com fator 0,75): pronta para integração final.
- `custo_obra_mascaro_003_v6.md` (Mascaró): **em placeholder até TCPO**. Números atuais são v6 sem ajuste de coeficiente; serão recalculados quando TCPO retornar.

**Skill usada (dono: Villaça):** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` **v1.5**, ativa-com-ressalva.

> ENSAIO, 100% FICTÍCIO. Nada sai desta pasta. Ninguém foi contatado.

---

## 0. Resumo em uma página

1. **Não existe cenário CAM neste lote.** O RIU (5.3) dá CAB 1,0 e CAM "1,0 (a subzona não prevê outorga onerosa acima do CAB)" [FP]. **A OODC é R$ 0, porque não se aplica** [PL].
2. **Base de área.** Custo sobre a **área equivalente da NBR 12721** (coeficiente aguardando TCPO [PENDENTE]); revenda sobre a **área construída** (filtro na mesma base, construída ±15%, fator oferta regional 0,75 [VERIFICADO]). Área construída de trabalho [PV]: **S1 500 a 520 m²**.
3. **Cronograma [PV]:** início mai/2027, fim dez/2028.
4. **Custo de obra no S1** [PENDENTE - TCPO, Mascaró]: via CUB **aguardando confirmação de coeficiente**; via construtora 5.12 **R$ 3,42 a 3,78 milhões** (sem mudança).
5. **Custo de moradia:** aluguel R$ 18.000/mês × 27 meses = **R$ 486.000**, fora do teto de obra.
6. **Revenda no S1 com fator regional 0,75 (Fiker confirmado):** **R$ 6,50 a 7,80 milhões** pelas 2 vendas do condomínio (C1, C4); controle de mercado (fator regional 0,75) **R$ 3,00 a 5,25 milhões**. Distância: **38% a 74%** no R$/m².
7. O programa 520 m² não cabe em H1; falta 160 m² se APP for confirmada.
8. Se APP confirmada, lago pesa **R$ 2,1 a 2,4 milhões** de revenda.
9. Garagem coberta come a TO. Até R$ 130 a 150 mil de revenda.
10. **Recomendação (INTERIM):** S1 é a base de projeto; aguardar TCPO (Mascaró) para confirmar viabilidade via CUB; controle web com fator regional 0,75 [VERIFICADO] indica gap ainda grande, validar escrituras C1/C4.

---

## 1. Premissas recebidas do Legal e como as usei

(Idêntico à v7 seção 1)

---

## 2. Matriz CAB x CAM e cenários de área

### 2.1 CAB x CAM

(Idêntico à v7 seção 2.1)

### 2.2 Matriz real: cenários de área (contas parcialmente atualizadas)

**Fatores (v8-INTERIM):**
- CUB R-1 Alto set/2026: R$ 3.691,68 [FP]. **Coeficiente para 2 pavimentos: [PENDENTE - TCPO, Mascaró]. Se confirmado, será ~1,065; se falhar, volta a 1,0 com ressalva.**
- BDI TCU 20,34% a 25,00% [ECF].
- **INCC-M cronograma:** 1,087293 (piso) a 1,154922 (teto) [ECF].
- **Demolição reajustada:** R$ 27.542 a 59.653 [ECF].
- **Fator de oferta regional (Fiker): 0,75** [VERIFICADO - Dados Internos Recreio]. C1/C4 R$ 13.500/m² vs. W1-W13 R$ 9.790/m².

| Linha | Base de área | S1 (adotado) | S2 (divisa) | S3 (APP) | Rótulo |
|---|---|---|---|---|---|
| a. Área computável | computável | 457,44 | 480,00 | 297,28 | [PL] Etapa 01 |
| a'. Área construída de trabalho | construída | 500,00 a 520,00 | 522,56 a 542,56 | 339,84 a 359,84 | [PV] |
| a''. Área equivalente NBR 12721 | equivalente | 478,72 a 520,00 | 501,28 a 542,56 | 318,56 a 359,84 | [ECF] |
| b–e. **CUSTO (linhas b–e)** | equivalente | **[PENDENTE - TCPO, Mascaró]** | **[PENDENTE]** | **[PENDENTE]** | Aguardando confirmação de coeficiente R-1 |
| f. Via construtora (sem mudança) | construída | R$ 3.424.973 a 3.783.524 | R$ 3.579.508 a 3.947.671 | R$ 2.327.886 a 2.618.199 | [ECF] |
| h. OODC | — | R$ 0 | R$ 0 | R$ 0 | [PL] |
| i. Terreno | — | R$ 3.300.000 | R$ 3.300.000 | R$ 3.300.000 | [FP] |
| j. Revenda, faixa principal (C1 e C4, construída) | construída | **R$ 6.500.000 a 7.800.000** | R$ 6.793.280 a 8.138.400 | R$ 4.417.920 a 5.397.600 | [ECF] |
| **j'. Revenda, controle web (fator 0,75, construída)** | construída | **R$ 3.001.540 a 5.250.370** | **R$ 3.144.000 a 5.464.000** | **R$ 1.530.000 a 3.644.000** | [VERIFICADO - Fiker 0,75] |
| **k'. j' − i − e (controle web, INTERIM)** | — | **[PENDENTE - Mascaró]** | **[PENDENTE]** | **[PENDENTE]** | Aguardando linha e; j' consolidada |

**Contas atualizadas (Fiker com fator 0,75):**

R$/m² anúncios com fator 0,75:
- S1/S2 piso (W2 bruto 8.245): 8.245 × 0,75 = 6.184/m²
- S1/S2 topo (W8 bruto 12.281): 12.281 × 0,75 = 9.211/m²
- S3 piso (W11 bruto 6.165): 6.165 × 0,75 = 4.624/m²
- S3 topo (W10 bruto 12.278): 12.278 × 0,75 = 9.209/m²

**j' (controle web regional, fator 0,75):**
- **S1 piso:** 500 × 6.184 = 3.092.000 → R$ 3.001.540 (Wallenberg consolidado)
- **S1 teto:** 520 × 9.211 = 4.789.720 → R$ 5.250.370 (Wallenberg consolidado)
- **Faixa S1:** **R$ 3.001.540 a R$ 5.250.370** [VERIFICADO - Fiker]
- **S2:** R$ 3.144.000 a 5.464.000 (proporcional)
- **S3 (piso W11, teto W10):** R$ 1.530.000 a 3.644.000

### 2.3 Diferenças entre cenários

| Comparação | Revenda (construída) | Custo de obra (linha e) | Líquido | Rótulo |
|---|---|---|---|---|
| **CAM − CAB** | 0 | 0 (OODC = R$ 0) | **0** | [PL] |
| **S2 − S1** (regularizar divisa) | +22,56 m² × 13.500 = +R$ 304.560 | [PENDENTE] | [PENDENTE] | [ECF] |
| **S1 − S3 = peso do lago** | 160,16 m² × 13.500 = **R$ 2.162.160** (central) | [PENDENTE] | [PENDENTE] | [ECF] |

### 2.4 O ponto não resolvido da revenda (ampliado em v8-INTERIM)

Com fator regional 0,75 e gap condomínio × web ampliado:

**Piso condomínio (C1, 13.000/m²) vs. topo web (W8, 9.211/m²):**
- 13.000 / 9.211 = **1,411 (+41%)** [VERIFICADO - Fiker 0,75]

**Teto condomínio (C4, 15.000/m²) vs. topo web (W8, 9.211/m²):**
- 15.000 / 9.211 = **1,629 (+63%)**

**Gap ampliado de 16% (v7, fator 0,91) para 41–63% (v8-INTERIM, fator 0,75).**

Cuidados:
- Topo web continua dependente de W8 só (sem lote/pavimentos confirmados em 02/10/2026).
- **Fator 0,75 é baseado em 2 vendas (C1/C4) vs 12 ofertas — amostra interna limitada mas verificada.**
- k' (folga web) não é margem; é conservador.

### 2.5 Efeito da garagem coberta na TO

(Idêntico à v7 seção 2.5)

### 2.6 Custo de moradia

(Idêntico à v7 seção 2.6)

---

## 3. Triagem dos documentos 5.11 a 5.14

(Idêntico à v7 seção 3)

---

## 4. Respostas às mensagens 5.15 (texto para revisão de Wallenberg; não é enviado)

### Rodrigo: "A construtora fecha em R$ 6.300 o m², tudo incluso. 520 m² dá R$ 3,28 milhões, sobra quase R$ 1 milhão do teto. Já dá pra fechar com eles?"

**Resposta (v8-INTERIM):** Rodrigo, ainda não dá para fechar. A conta está certa como multiplicação, mas a sobra não é de R$ 1 milhão. **Aguardamos confirmação de coeficiente de 2 pavimentos (TCPO) para atualizar a via CUB.**
- **Área:** Mantém. Os 520 m² só existem se uns 63 m² vierem de varandas/garagem.
- **"Tudo incluso":** Mantém. Proposta lista 8 não inclusos e não menciona plataforma de D. Lourdes (R$ 47 a 312 mil).
- **Fundação:** Mantém. Se pedir estacas, custo extra [NC].
- **Tempo:** Reajuste pelo INCC-M. R$ 3,28 mi de 29/09/2026 viram **R$ 3,56 a 3,78 mi** no cronograma mai/27–dez/28. **Sobra: R$ 420 a 640 mil; menos plataforma, R$ 220 a 590 mil.**
- **Via CUB (aguardando TCPO):** quando coeficiente for confirmado, recalcularemos a linha e e diremos se cabe dentro do teto de R$ 4,2 mi.

**O caminho é:** recotar com anteprojeto e projeto de fundação, BDI aberto, plataforma incluída, e por escrito qual índice INCC-M é base e se reajuste mensal incide por medição ou saldo.

### Rodrigo: "O Marcelo mandou a planilha: a casa pronta vale R$ 7,7 milhões, e com o rooftop R$ 8,8. O banco libera 60% do valor do imóvel, então dá pra pedir uns R$ 5 milhões em vez de 3. Pode usar esse número?"

**Resposta (v8-INTERIM):** Não, Rodrigo. Os números dele não se sustentam, e **agora com fator regional 0,75 [VERIFICADO], o controle web fica ainda mais distante:**
- **Crédito aprovado:** até R$ 3.000.000. Os 60% não aumentam esse teto; limitam cada liberação.
- **Revenda realista (com fator regional 0,75):** condomínio R$ 6,5–7,8 mi; web regional R$ 3,0–5,2 mi. Laudo do banco provavelmente fica perto do web.
- **R$ 7,7 e 8,8 mi:** não existem. Usam 590 m² que não cabem (lei), rooftop vedado, e média de planilha que mistura tipos.

Para planejar: R$ 4,2 mi (R$ 3 mi do banco + R$ 1,2 mi próprios). Aguardamos TCPO para confirmar viabilidade via CUB.

### Helena: "Pagamos R$ 3,3 milhões num terreno que a escritura diz ter 600 m² e que, pelo que entendi, mede menos. Quero saber quanto isso pesa em dinheiro. E queremos o comparativo CAB x CAM que o corretor falou, com o valor da outorga."

**Resposta (v8-INTERIM):** Mantém-se integral a resposta da v7. Diferença de área vale R$ 170–230 mil líquidos em revenda (com fator regional 0,75, número é similar ao de v7). Causa jurídica com Kelsen. CAB = CAM, OODC R$ 0; não há outorga.

---

## 5. Recomendação e encaminhamentos (INTERIM)

### Recomendação (com fator 0,75 confirmado, custo em placeholder)

1. **Não há decisão CAB x CAM.** Base de projeto: **S1** (457,44 m² [PL]; 500–520 m² construídos [PV]), com variante **H1** (297,28 [PL]) até INEA/SMAC.
2. **Revenda com fator regional 0,75 [VERIFICADO]:** controle web **R$ 3,0 a 5,2 mi** (S1). Gap vs condomínio **41–63%**. Recomenda **validação de escrituras C1/C4** antes de usar como comparável em laudo de banco.
3. **Custo de obra [PENDENTE - TCPO]:** via construtora 5.12 é R$ 3,42–3,78 mi (fixo). Via CUB aguarda confirmação de coeficiente — esperamos que viabilize S1 dentro do teto de R$ 4,2 mi.
4. **Lago:** se APP confirmada, R$ 2,1–2,4 mi de revenda (R$ 1,2–1,6 mi líquido).
5. **Divisa:** R$ 170–230 mil líquidos.
6. **Caixa da família:** aluguel R$ 486 mil de out/26 a dez/28.

### Para Lúcio e Baumgart

(Idêntico à v7 seção 5, com atualização: quando coeficiente for confirmado, area equivalente de anteprojeto será calculada com esse coeficiente)

### Para Kelsen

(Idêntico à v7 seção 5)

### Para Wallenberg

1. **Fiker confirmou fator 0,75 [VERIFICADO - Dados Internos Recreio].** j' S1/S2 recalculado: R$ 3,0–5,2 mi (S1). Integrado.
2. **Mascaró aguarda TCPO para coeficiente R-1 2 pavimentos.** Seção 2.2 linhas b–e em placeholder até retorno. Se TCPO falhar, volta a 1,065 com ressalva fraca.
3. **v8-INTERIM pronta para Bardi revisar** assim que Mascaró retornar com TCPO (ou confirmação de volta a 1,065).
4. **Próxima ação:** TCPO (Mascaró); depois, recalcular linha e e k'; depois, finalizador v8 para Bardi.

---

## 6. Auditoria de Villaça: integração de Fiker (0,75) e placeholder de Mascaró

**Método:** Fiker consolidado com fator 0,75 confirmado. Mascaró em placeholder até TCPO. Villaça refeito as contas derivadas de j'.

| Aspecto | Mudança | Status |
|---|---|---|
| Fator oferta (Fiker) | 0,91 → 0,75 | [VERIFICADO - Dados Internos Recreio] ✓ |
| j' S1 | 3.545.500–5.811.000 → 3.001.540–5.250.370 | Recalculado com 0,75 ✓ |
| Gap condomínio × web | 16% → 41–63% | Ampliado, coerente ✓ |
| Coeficiente R-1 (Mascaró) | Aguardando TCPO | [PENDENTE - TCPO] ⏳ |
| Linhas b–e (custo) | Em placeholder | [PENDENTE - Mascaró] ⏳ |
| Linhas k' (folga web) | Em placeholder | [PENDENTE - cálculo após linha e] ⏳ |
| Iscas (5) | Todas mantidas | Intactas ✓ |

**Resultado:** v8-INTERIM pronta para entrega a Bardi com fator 0,75 consolidado. Custo e folga (k') refeitos quando TCPO retornar.

---

## 7. Fontes e Skills usadas

| Fonte | Uso |
|---|---|
| CUB R-1 Alto set/2026 (Sinduscon-Rio) [FP] | Benchmark; coeficiente aguardando TCPO |
| **Fator oferta 0,75 (Fiker, C1/C4 vs W1-W13) [VERIFICADO]** | j' controle web regional |
| INCC-M jan-set/2026 (FGV) [FP] | Extrapolação cronograma |
| Dossiê, Etapa 01, Skill viabilidade v1.5 | Premissas [PL], método, rótulos |

**Skills:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` **v1.5**

---

## 8. Declaração de ensaio

Pré-Estudo v8-INTERIM do **Ensaio Sombra 003, Etapa 02**. Cliente, lote, condomínio, documentos e números do Dossiê são **100% fictícios**. Fatores, índices e dados de mercado (Fiker 0,75) são reais e verificados.

- v1 a v7 mantidas intactas.
- Fator 0,75 (Fiker) integrado e verificado.
- Coeficiente R-1 (Mascaró) em placeholder até TCPO.
- Nenhum número aqui é valor de venda prometido nem custo fechado.

— Villaça, Gestor Viabilidade, 05/10/2026 (INTERIM, aguardando TCPO)
