# Pré-Estudo de Viabilidade v7 — Ensaio Sombra 003, Etapa 02 — Lote 17, Qd C, Reserva das Garças

**Gestor:** Villaça (Viabilidade). **Execução:** Mascaró (custo de obra) e Fiker (valor de revenda).
**Para revisão de:** Wallenberg. Estou no nível Assisted: nada daqui vai ao cliente sem a revisão dele.
**Data de referência dos números:** 02/10/2026 (fontes web acessadas nessa data; reaberturas de 05/10/2026 indicadas). **Data desta versão:** 05/10/2026.
**Por que existe a v7:** Claudemberg reprovou a v6 em 05/10/2026, sob tolerância zero, e Bardi (`../../parecer_bardi_v6.md`) apontou 4 itens a corrigir:
1. o controle web de revenda foi filtrado por metragem na área **computável** (faixas 430 a 520 m² e 280 a 330 m², vindas da v1), enquanto o avaliando está na área **construída** de trabalho. Agora o filtro está na construída de trabalho, com tolerância declarada (±15%), e tudo o que dependia dele foi refeito: j', k', §2.4, j' de S3, recomendação 7 e respostas ao Rodrigo;
2. a "Limitação de tipo" de Fiker (§2.2 dele) deixava de fora W1 ("Área total" 450). Corrigido;
3. a Skill não dizia que o **filtro** de metragem usa a mesma base de área do avaliando. Agora diz (v1.5, §3.1 e §3.2), e ganhou um checklist de erros de alto impacto ao cliente (§4.1);
4. a 3ª cópia da Skill (`.agents/skills/`, espelho) estava na v1.3. Agora as 3 cópias estão na v1.5, com backup integral de cada uma antes da edição.

**Números que mudaram:** só os do controle web (j', k', distância condomínio × mercado). Custo de obra, revenda pela faixa do condomínio (j), lago, divisa, aluguel e Helena **não mudam**; conferi de novo (seção 6). As v1 a v6 ficam intactas.

**Peças integradas (nesta pasta `v7/`):**
- `custo_obra_mascaro_003_v6.md` (Mascaró): **cópia sem alteração** da peça da v6. Mascaró não foi acionado, porque nada do custo depende do filtro de revenda. Reli a peça inteira contra o checklist da Skill v1.5 §4.1 (seção 6.1). Ela cita a Skill v1.4, que era a vigente quando foi feita; as partes de custo (§2) não mudaram na v1.5;
- `revenda_fiker_003_v6.md` (Fiker, refeito: filtro na construída de trabalho, ±15%; R$/m² sobre preço e área exatos; W1 na "Limitação de tipo"; 4 ajustes meus de auditoria, seção 6.2).

**Skill usada (dono: Villaça):** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` **v1.5** (§2.4 literal; §2.6 reajuste; §2.8 citação e regra de rótulo; §3.1 e §3.2 filtro na mesma base; §4.1 checklist de erros), ativa-com-ressalva.

**Rótulos de confiança (este arquivo):**
- **[FP] fonte primária:** só o que está **literal** no documento oficial ou do Dossiê/caso base (no ensaio, vale como real). Dedução, cálculo ou interpretação sobre ele nunca leva [FP].
- **[PL] premissa recebida do Legal:** número ou conclusão do parecer da Etapa 01 (Hely/Kelsen, aprovado por Claudemberg em 01/10/2026). Está literal no parecer, mas é cálculo/leitura do Legal, não texto do Dossiê nem da lei. Não reabro.
- **[ECF] estimativa com fonte:** conta sobre fonte citada, com a fragilidade declarada.
- **[PV] premissa de Villaça:** área de trabalho, cronograma, tolerância do filtro e tudo o que eu deduzo de um documento sem que ele o diga.
- **[NC] não calculável:** a seção diz o que faltaria.

**Equivalência com os rótulos das peças dos Agentes:** [DOC] de Mascaró (texto literal do Dossiê ou do caso base) = [FP] aqui; [FP] de Mascaró e de Fiker = [FP] aqui; [EF] de Fiker = [ECF] aqui; [INF] de Fiker (inferência dele) = premissa, tratada como [PV] aqui; [PL], [PV] e [NC] têm o mesmo sentido nas três peças. A mesma área tem o mesmo rótulo nas três: computáveis 457,44 / 480,00 / 297,28 m² = [PL]; construída de trabalho e faixa não computável = [PV].

> ENSAIO, 100% FICTÍCIO. Nada sai desta pasta. Ninguém foi contatado.

---

## 0. Resumo em uma página

1. **Não existe cenário CAM neste lote.** O RIU (5.3) dá CAB 1,0 e CAM "1,0 (a subzona não prevê outorga onerosa acima do CAB)" [FP]. **A OODC é R$ 0, porque não se aplica** [PL], e a diferença "CAM − CAB" é **zero** (LC 270 Art. 345 §3º, conforme a Etapa 01). A outorga de "R$ 380 mil para 300 m² a mais" do corretor foi simulada "no Lote 5 do Jardim dos Socós, aqui do lado, que tem CAM 1,5" (5.13): não vale aqui. O que muda o resultado é a **área**: a divisa com o Lote 16 e, sobretudo, o lago.
2. **Base de área.** Custo sobre a **área equivalente da NBR 12721**; revenda sobre a **área construída**, a mesma base dos comparáveis, **e o filtro que escolhe os comparáveis também na construída**. Nunca sobre a área computável. Área construída de trabalho [PV]: **S1 500 a 520 m²** (457,44 computáveis [PL] + 42,56 a 62,56 não computáveis [PV]).
3. **Cronograma [PV]:** início em mai/2027 (o caso base diz "Querem iniciar a obra em maio/2027") e fim em dez/2028, que é premissa minha tirada do prazo de mudança ("mudar até dezembro/2028"); o documento não diz quando a obra termina.
4. **Custo de obra no S1, pago ao longo da obra, com reajuste pelo INCC em todo o desembolso:**
   - **R$ 2,34 a 2,83 milhões** pela via do CUB (área equivalente 478,72 a 520,00 m² × CUB R-1 Alto + BDI + INCC-M no cronograma + demolição da casa reajustada) [ECF];
   - **R$ 3,42 a 3,78 milhões** pela via do preço da construtora 5.12 sobre a área construída [ECF], com índice-base set/2026 [PV]; se o índice-base for o de ago/2026, **+R$ 8,6 a 9,5 mil** [ECF];
   - **mais a plataforma (ou elevador) de D. Lourdes, com obra civil, reajustada**: plataforma R$ 46.754 a 196.337; elevador R$ 122.864 a 311.829 [ECF, fonte fraca];
   - e, sem número ainda, fundação profunda, rebaixamento, piscina, paisagismo, AC, automação, projetos, ligações, sondagem, impostos, efeito 2 pavimentos [NC].
   - **Não dá para afirmar que o S1 cabe no teto de R$ 4,2 milhões, nem que não cabe.** Pela via da proposta, com a plataforma, a parcela calculável já ocupa 83% a 95% do teto.
5. **Custo de moradia:** a família paga R$ 18.000/mês de aluguel. De out/2026 até a mudança prevista (dez/2028) são 27 meses [PV: contagem] = **R$ 486.000**, fora do teto de obra.
6. **Revenda no S1:** **R$ 6,50 a 7,80 milhões** pelas 2 vendas do condomínio (C1, C4) × área construída [ECF, média-baixa]; o controle de mercado (7 anúncios do Recreio de 450 a 570 m², com fator de oferta) dá **R$ 3,55 a 5,81 milhões**. A distância (16% no R$/m², entre o piso do condomínio e o maior anúncio homogeneizado) **não está resolvida**, e o topo do controle depende de um anúncio só (W8).
7. **O programa de 520 m² não cabe em H1 (lago), pela premissa de área de trabalho.** Se a APP de 30 m for confirmada, o teto computável é 297,28 m² [PL] e o construído de trabalho, 339,84 a 359,84 m² [PV]. Faltam no mínimo 160 m².
8. **Se a APP for confirmada, o lago pesa cerca de R$ 2,1 a 2,4 milhões na revenda** (faixa larga R$ 1,1 a 3,4 mi), ou **R$ 1,2 a 1,6 milhão líquido** depois da economia de obra [ECF, baixa].
9. **Garagem coberta come a TO.** Só 1 vaga coberta fica fora da taxa de ocupação (Etapa 01) [PL]. Cada 10 m² de garagem coberta dentro da projeção tiram 10 m² computáveis da casa [PV: mecanismo]: até R$ 130 a 150 mil de revenda [ECF].
10. **Recomendação:** projetar sobre S1 com variante H1; não fechar com a construtora agora; não contar com R$ 5 milhões do banco; a divisa vale cerca de R$ 0,17 a 0,23 milhão líquido em revenda, menos o custo de regularizar [NC]; o caminho jurídico é do Legal.

---

## 1. Premissas recebidas do Legal e como as usei

Fonte: `parecer_legal_base_003.md` (Hely), seção 5.1, e `auditoria_kelsen_003.md` (libera com ressalva), aprovadas por Claudemberg em 01/10/2026. **Não reabro nenhuma.** Todas levam [PL].

| Premissa [PL] | Valor | Como usei |
|---|---|---|
| CAB / CAM | 1,0 / 1,0 | Não há cenário CAM nem OODC. A coluna "CAM" aparece só para mostrar que é zero. |
| Área de cálculo | 571,80 m² medidos (5.2, literal [FP]); 600,00 m² na escritura (5.11) e na matrícula (5.1), hipótese condicionada | S1 sobre 571,80. S2 sobre 600, só como hipótese. |
| Limite real | TO 40% do condomínio (5.4, Art. 5º: "Taxa de ocupação máxima: 40% da área do lote" [FP]) × 2 pavimentos: **457,44 m² computáveis** (S1); 480 (S2). Projeção máxima 228,72 m² (contas do Legal) | Teto **computável**. |
| Lago (H1, APP de 30 m) | Envelope 148,64 m²; teto **297,28 m² computáveis** (S3) | Cenário de risco, não de projeto. |
| Vagas | Fora da ATE (LC 270 Art. 347 II); **só 1 vaga coberta fora da TO** em unifamiliar (Art. 350 III), na leitura do Legal | Efeito da garagem na TO (seção 2.5). |
| Vedados | subsolo, rooftop, escavação > 1,20 m (piscina até 1,60 m), Mais-Valerá/LC 281 para área | Nenhum valor atribuído. |
| Edícula e casa | premissa de demolição (Etapa 01: "Edícula existente: premissa de demolição (decisão final do cliente)"; o cliente queria manter edícula e piscina, caso base §4) | Demolição da casa no custo; edícula e piscina [NC]. |

**Premissas do caso base [FP, citação literal]:** "Querem iniciar a obra em maio/2027 e mudar até dezembro/2028."; "Moram de aluguel (R$ 18.000/mês) desde a venda do apartamento anterior."; "Orçamento-teto declarado para a obra: R$ 4,2 milhões (sem terreno)." O fim da obra em dez/2028 é **premissa minha [PV]** derivada do prazo de mudança.

**Premissa de área de trabalho** (a mesma nos dois Agentes; é também a base do filtro de comparáveis):

| Cenário | Computável [PL] | Não computável (varandas, garagem coberta) [PV] | Construída de trabalho [PV] | Faixa de busca dos anúncios (±15% [PV]) |
|---|---|---|---|---|
| S1 / H0 | 457,44 | 42,56 a 62,56 | **500,00 a 520,00** | 425 a 598 m² |
| S2 | 480,00 | 42,56 a 62,56 | **522,56 a 542,56** | 444 a 624 m² |
| S3 / H1 | 297,28 | 42,56 a 62,56 | **339,84 a 359,84** | 289 a 414 m² |

A faixa vem do programa ("cerca de 520 m² construídos", caso base §4). A tolerância de ±15% sobre os extremos da construída de trabalho (mínimo × 0,85; máximo × 1,15, arredondado ao m²) é premissa minha, declarada. S1 e S2 usam o mesmo conjunto de anúncios (os 7 de 450 a 570 m² cabem nas duas faixas), por isso a faixa conjunta S1/S2 é 425 a 624 m². Quando Lúcio der o quadro de áreas por tipo, custo, revenda **e o filtro** são refeitos.

**Risco residual registrado (não reabro):** CAB = CAM vem da LC 270 Arts. 345 a 354, mantida por Kelsen "no grau declarado pelo Hely, sem releitura". Se mudar, a seção 2.1 muda inteira.

---

## 2. Matriz CAB x CAM e cenários de área

### 2.1 CAB x CAM

| Item | Cenário CAB | Cenário CAM | Diferença | Rótulo |
|---|---|---|---|---|
| Coeficiente | 1,0 | 1,0 | 0 | [FP] RIU 5.3 (valores literais); [PL] LC 270 Art. 345 §§3º e 5º (leitura do Legal) |
| Área computável (S1) | 457,44 m² | 457,44 m² | 0 m² | [PL] Etapa 01 |
| Custo da OODC | não se aplica | **R$ 0** | R$ 0 | [PL] conclusão da Etapa 01 (CAB = CAM); Skill OODC v1.1 |
| Custo de obra | ver 2.2 | igual ao CAB | 0 | — |
| Revenda | ver 2.2 | igual ao CAB | 0 | — |

### 2.2 Matriz real: cenários de área (contas abertas; base de área em cada linha)

**Fatores (Mascaró v6, seção 5; sem alteração):**
- CUB R-1 Alto set/2026 R$ 3.691,68 [FP, PDF Sinduscon-Rio, data de emissão 29/09/2026 15:21]; BDI TCU 20,34% a 25,00% [ECF, obra pública].
- **INCC-M no cronograma** [ECF, extrapolação do passado], taxa mensal de 0,4794% (piso) e 0,5349% (teto), aplicada de set/2026 a todo o desembolso mai/2027 a dez/2028 [PV no fim]:
  - **piso:** desembolso linear em 20 parcelas, reajustado pelo **fator no mês médio da obra** (9,5 meses depois de mai/2027): 1,046480. É uma **aproximação, por baixo**, da média exata dos 20 fatores, ((1,0047938^20 − 1) / (20 × 0,0047938)) ≈ **1,04687** (Bardi: ≈ 1,04686). Diferença ≈ 0,04 p.p., ≈ R$ 855 no piso de S1; não aplicada, declarada. Fator total desde set/2026 = 1,039 × 1,046480 = **1,087293**;
  - **teto:** tudo reajustado até dez/2028 (limite superior; sem cronograma físico-financeiro): **1,154922**;
  - dissídio de mai/2028 diluído na taxa média, declarado.
- **Demolição da casa:** Cronoshare, página datada de 02/01/2026 [FP, fonte fraca], faixa "mecanizada" de R$ 140 a 300/m² [FP, fonte fraca] × 180 m² = R$ 25.200 a 54.000 [ECF, fraca]. A página não diz quando os preços foram levantados, e por isso o mês-base fica na faixa [PV]: piso base jan/2026, teto base dez/2025. Reajuste até mai/2027 pelo INCC-M de 2026 (taxas mensais da FGV [FP], compostas por Mascaró [ECF]) × a extrapolação set/26→mai/27: piso (fev→set = 1,051913) × 1,039 = **1,092938** → **R$ 27.542**; teto (jan→set = 1,058540) × 1,0436 = **1,104692** → **R$ 59.653**.
- Piso = CUB × 1,2034 × 1,087293 + 27.542; teto = CUB × 1,25 × 1,154922 + 59.653.

| Linha | Base de área | S1 (adotado) | S2 (divisa) | S3 (APP) | Rótulo |
|---|---|---|---|---|---|
| a. Área computável | computável | 457,44 | 480,00 | 297,28 | [PL] Etapa 01 |
| a'. Área construída de trabalho | construída | 500,00 a 520,00 | 522,56 a 542,56 | 339,84 a 359,84 | [PV] |
| a''. Área equivalente NBR 12721 | equivalente | 478,72 a 520,00 | 501,28 a 542,56 | 318,56 a 359,84 | [ECF] |
| b. CUB puro (a'' × 3.691,68) | equivalente | R$ 1.767.281 a 1.919.674 | R$ 1.850.565 a 2.002.958 | R$ 1.176.022 a 1.328.414 | [FP] índice; [ECF] conta |
| c. + BDI | equivalente | R$ 2.126.746 a 2.399.592 | R$ 2.226.970 a 2.503.697 | R$ 1.415.224 a 1.660.518 | [ECF] |
| d. × INCC-M set/26 → cronograma | equivalente | R$ 2.312.396 a 2.771.342 | R$ 2.421.369 a 2.891.575 | R$ 1.538.764 a 1.917.768 | [ECF] |
| e. **+ demolição reajustada = parcela calculável** | equivalente | **R$ 2.339.938 a 2.830.995** | R$ 2.448.911 a 2.951.229 | R$ 1.566.306 a 1.977.422 | [ECF] |
| e'. Plataforma de D. Lourdes, com obra civil, **reajustada**. Fonte: artigo do Monitor do Mercado datado de 24/08/2026, faixas literais de plataforma (R$ 25 a 80 mil), elevador compacto (R$ 95 a 180 mil) e obra civil (R$ 18 a 90 mil) [FP, fonte fraca]; a soma equipamento + obra civil (plataforma R$ 43 a 170 mil; elevador R$ 113 a 270 mil) é de Mascaró [ECF]; valores do artigo tratados como de set/2026 [PV]; × 1,087293 a × 1,154922 | — | R$ 46.754 a 196.337 (elevador: R$ 122.864 a 311.829) | idem | idem | [ECF] fonte fraca |
| f. Via construtora: R$ 6.300 × construída × INCC-M no cronograma. Cláusula literal da 5.12 [FP]: "INCC-M mensal a partir da data desta proposta"; data da proposta 29/09/2026 [FP]. **Índice-base adotado: INCC-M set/2026 [PV]** (a cláusula não diz qual número-índice corresponde à data). Alternativa [PV]: INCC-M ago/2026, índice do mês anterior ao da proposta, leitura usada em alguns contratos (sem fonte lida; por isso é pergunta à construtora, seção 5) → a via f sobe 0,25% (variação de set/26 [FP]) = **+R$ 8.562 a 9.459** no S1 [ECF] | construída | R$ 3.424.973 a 3.783.524 (base set/26 [PV]) | R$ 3.579.508 a 3.947.671 | R$ 2.327.886 a 2.618.199 | [ECF] n = 1; inclui radier provavelmente inválido |
| g. Fora das linhas e e f | — | fundação profunda (provável hélice contínua [PV]; SINAPI R$ 139,38/m Ø 30 e R$ 255,98/m Ø 50, média nacional; sem nº de estacas); rebaixamento; piscina; paisagismo; AC; automação; projetos e aprovações; ligações; sondagem; impostos e taxas; demolição de edícula, piscina e entulho; acabamento acima do R-1 Alto; efeito 2 pavimentos. Todos sofrerão reajuste quando tiverem valor | idem | idem | **[NC]** (Mascaró v6, seção 6) |
| h. OODC | — | R$ 0 | R$ 0 | R$ 0 | [PL] |
| i. Terreno (preço pago, 5.11: "R$ 3.300.000,00, à vista") | — | R$ 3.300.000 | R$ 3.300.000 | R$ 3.300.000 | [FP] valor literal; uso como custo afundado, só para ler k |
| j. Revenda, faixa principal (vendas C1 e C4, R$ 13.000 a 15.000/m² **construída** [PV: "construídos" do corretor lidos como total]) | construída | **R$ 6.500.000 a 7.800.000** | R$ 6.793.280 a 8.138.400 | R$ 4.417.920 a 5.397.600 (ordem de grandeza; só C1: R$ 4.417.920 a 4.677.920) | [ECF] média-baixa (S1, S2); baixa (S3) |
| j'. Revenda, controle web (anúncios × fator de oferta 0,86 a 0,91; área dos anúncios tratada como construída [PV]; **filtro de metragem na construída de trabalho ±15% [PV]**). S1/S2: n = 7 (W1, W2, W3, W4, W6, W7, W8), R$ 7.091 a 11.175/m². S3: n = 5 (W10, W11, W13, W9, W5); linha principal = alto padrão declarado (W10 + W13), R$ 9.274 a 12.278/m² | construída | **R$ 3.545.500 a 5.811.000** | R$ 3.705.473 a 6.063.108 | R$ 3.151.676 a 4.418.116 (W10 + W13); referências: amostra inteira R$ 1.979.908 a 4.418.116; W5 (único de 2 pavimentos confirmado) R$ 3.068.755 a 3.438.271 | [ECF] |
| k. j − i − e ("folga antes de g, e' e moradia") | — | +R$ 369.005 a +R$ 2.160.062 | +R$ 542.051 a +R$ 2.389.489 | −R$ 859.502 a +R$ 531.294 | [ECF]. **Não é margem** |
| k'. j' − i − e (controle web) | — | **−R$ 2.585.495 a +R$ 171.062** | −R$ 2.545.756 a +R$ 314.197 | −R$ 2.125.746 a −R$ 448.190 | [ECF] |

Revenda (j, j') a preço de hoje, sem projeção a 2028 (não há fonte): a comparação k mistura custo reajustado com revenda de hoje, o que é conservador para k.

**Contas refeitas na v7:**
- **R$/m² dos anúncios sobre preço e área exatos** (Skill v1.5 §3.2): extremos S1/S2 = W2 × 0,86 = 3.439.140 / 485 = 7.091,01 → 7.091; W8 × 0,91 = 6.370.000 / 570 = 11.175,44 → 11.175. S3: W13 × 0,86 = 3.431.400 / 370 = 9.274,05 → 9.274; W10 × 0,91 = 3.867.500 / 315 = 12.277,78 → 12.278; W11 × 0,86 = 1.806.000 / 310 = 5.825,81 → 5.826; W5 × 0,86 = 3.612.000 / 400 = 9.030; × 0,91 = 3.822.000 / 400 = 9.555.
- **j' S1:** 500 × 7.091 = 3.545.500; 520 × 11.175 = 5.811.000. **S2:** 522,56 × 7.091 = 3.705.472,96; 542,56 × 11.175 = 6.063.108,00. **S3:** 339,84 × 9.274 = 3.151.676,16; 359,84 × 12.278 = 4.418.115,52; 339,84 × 5.826 = 1.979.907,84; 339,84 × 9.030 = 3.068.755,20; 359,84 × 9.555 = 3.438.271,20.
- **k' S1:** 3.545.500 − 3.300.000 − 2.830.994,99 = −2.585.494,99 → −2.585.495; 5.811.000 − 3.300.000 − 2.339.938,10 = 171.061,90 → +171.062. **S2:** 3.705.472,96 − 3.300.000 − 2.951.228,58 = −2.545.755,62 → −2.545.756; 6.063.108,00 − 3.300.000 − 2.448.911,30 = 314.196,70 → +314.197. **S3:** 3.151.676,16 − 3.300.000 − 1.977.421,78 = −2.125.745,62 → −2.125.746; 4.418.115,52 − 3.300.000 − 1.566.305,58 = −448.190,06 → −448.190.
- **k (sem mudança):** S1 6.500.000 − 3.300.000 − 2.830.994,99 = 369.005,01; 7.800.000 − 3.300.000 − 2.339.938,10 = 2.160.061,90. S2 6.793.280 − 3.300.000 − 2.951.228,58 = 542.051,42; 8.138.400 − 3.300.000 − 2.448.911,30 = 2.389.488,70. S3 4.417.920 − 3.300.000 − 1.977.421,78 = −859.501,78; 5.397.600 − 3.300.000 − 1.566.305,58 = 531.294,42.
- **Custo (sem mudança, conferido):** fatores 1,039 × 1,046480 = 1,087293 e 1,0436 × 1,106670 = 1,154922; e S1 2.312.396,07 + 27.542,03 = 2.339.938,10 e 2.771.341,59 + 59.653,40 = 2.830.994,99; S2 2.448.911,30 e 2.951.228,58; S3 1.566.305,58 e 1.977.421,78. Plataforma 43.000 × 1,087293 = 46.753,60; 170.000 × 1,154922 = 196.336,74; elevador 113.000 × 1,087293 = 122.864,11; 270.000 × 1,154922 = 311.828,94. Via f 3.150.000 × 1,087293 = 3.424.972,95; 3.276.000 × 1,154922 = 3.783.524,47; alternativa ago/26: × 0,0025 = 8.562,43 e 9.458,81; nos 520 m² do Rodrigo: 3.561.971,87 × 0,0025 = 8.904,93.

### 2.3 Diferenças entre cenários

| Comparação | Revenda (construída) | Custo de obra (linha e) | Líquido | Rótulo |
|---|---|---|---|---|
| **CAM − CAB** | 0 | 0 (OODC = R$ 0) | **0** | [PL] |
| **S2 − S1** (regularizar a divisa) | +22,56 m² × 13.000 a 15.000 = +R$ 293.280 a 338.400 | +R$ 108.973 a 120.234 | **+R$ 173.046 a 229.427**, menos o custo da regularização [NC] | [ECF] média-baixa |
| **S1 − S3 = peso do lago, se a APP for confirmada** | central: 160,16 m² × 13.000 a 15.000 = **R$ 2.082.080 a 2.402.400**; faixa larga R$ 1.102.400 a 3.382.080 | economia de R$ 773.632 a 853.573 | **perda líquida central R$ 1.228.507 a 1.628.768**; faixa larga R$ 248.827 a 2.608.448 | [ECF] baixa; sentido provável: peso **maior** |

Contas: 2.448.911 − 2.339.938 = 108.973; 2.951.229 − 2.830.995 = 120.234; 293.280 − 120.234 = 173.046; 338.400 − 108.973 = 229.427. Lago: 2.339.938 − 1.566.306 = 773.632; 2.830.995 − 1.977.422 = 853.573; 2.082.080 − 853.573 = 1.228.507; 2.402.400 − 773.632 = 1.628.768; 1.102.400 − 853.573 = 248.827; 3.382.080 − 773.632 = 2.608.448. Pelo controle web (mesmo R$/m² homogeneizado S1/S2), o peso do lago na revenda seria 160,16 × 7.091 a 11.175 = R$ 1.135.695 a 1.789.788 (Fiker v6 §5.3), dentro da faixa larga.

### 2.4 O ponto não resolvido da revenda

Com o filtro na base certa (construída de trabalho ±15%) e o fator de oferta, o piso do condomínio (R$ 13.000/m²) fica **16% acima** do maior anúncio homogeneizado da faixa S1/S2 (W8, R$ 11.175/m²; 13.000 / 11.175 = 1,163). Em S1 com 520 m², R$ 949 mil (6.760.000 − 5.811.000); com 500 m², R$ 912,5 mil (6.500.000 − 5.587.500). Na v6, com o filtro errado (na computável), eram 33% e R$ 1,66 milhão: o erro de filtro **dobrava** a distância.

Cuidados com esse número:
- o topo do controle depende de **um anúncio só** (W8, anúncio de "venda ou aluguel" pelo próprio link; lote e pavimentos não registrados na coleta de 02/10/2026). Sem W8, o topo volta a R$ 9.808/m² (W1) e a distância a 33%;
- duas hipóteses continuam sem separação: (a) prêmio real do condomínio (2 pavimentos, lago; o tamanho dos lotes do condomínio não é informado no Dossiê, só o do Lote 17) [PV]; (b) as escrituras C1 e C4 precisam ser conferidas (a planilha diz "m² construídos", sem dizer se é total, computável ou averbada). Se forem computáveis, a faixa j cai para a da v1 (R$ 5,95 a 6,86 mi).

**Por isso a linha k não é margem nem promessa**, e para o banco vale o lado do controle web (j').

### 2.5 Efeito da garagem coberta na TO

- Programa: "Garagem para 4 carros" (caso base §4) [FP]. Só **1 vaga coberta fica fora da TO** (LC 270 Art. 350 III, Etapa 01) [PL].
- **Cada 10 m² de garagem coberta dentro da projeção tiram 10 m² computáveis da casa** (457,44 → 447,44) [PV: mecanismo].
- Custo: o CUB puro (set/2026) cai R$ 9.229 a 18.458 por 10 m² [ECF].
- Revenda: perde-se até **R$ 130.000 a 150.000 por 10 m²** de área nobre, menos o que o mercado paga pela garagem [NC] [ECF].
- A área da vaga é de Lúcio; aqui só o peso em dinheiro.

### 2.6 Custo de moradia (da família, fora do teto de obra) — Skill §2.7

- Caso base: "Moram de aluguel (R$ 18.000/mês) desde a venda do apartamento anterior." [FP]. O custo conta **de hoje até a mudança**.
- Período: out/2026 a dez/2028 (caso base: "mudar até dezembro/2028") = 3 + 12 + 12 = **27 meses** [PV: contagem inclusiva].
- **27 × 18.000 = R$ 486.000** [ECF]. Pré-obra out/2026 a abr/2027 = 7 meses = R$ 126.000; obra mai/2027 a dez/2028 = 20 meses = R$ 360.000.
- **Cada mês de atraso custa R$ 18.000.** Pesa a favor de cumprir a condição do banco: licença de obras emitida até 30/06/2027 (5.14).
- Sem informação de reajuste do aluguel no Dossiê: valor constante [PV].

---

## 3. Triagem dos documentos 5.11 a 5.14

| Doc | Aceito | Devolvo / não uso | Por quê |
|---|---|---|---|
| **5.11 Escritura** ("Lote 17 da Quadra C do PAL nº 40.112, com área de 600,00 m², e as benfeitorias nele existentes"; preço "R$ 3.300.000,00, à vista") [FP] | O preço pago, como custo do terreno (linha i) | Os 600,00 m² como área de cálculo. Os R$ 5.500/m² como valor de mercado do terreno | Área medida 571,80 m² (5.2). O preço inclui as benfeitorias (casa, edícula e piscina, caso base §3) e é transação única. O único anúncio de lote achado (R$ 3.371/m², R$ 2.899 a 3.068/m² com fator de oferta) não permite falar em sobrepreço com 1 dado. |
| **5.12 Proposta Alicerce Prime** (29/09/2026, validade 30 dias) | R$ 6.300,00/m² [FP] como **um ponto** de preço de construtora, aplicado à **área construída** (linha f). A lista de "Não inclusos" como checklist. **A cláusula de reajuste, literal [FP]: "INCC-M mensal a partir da data desta proposta"**: índice (INCC-M) e periodicidade (mensal) estão no texto; o marco é "a data desta proposta" (29/09/2026). **Qual número-índice corresponde a esse marco (set ou ago/2026) não está no texto: [PV] set/2026** | Área de 590 m² (inviável [PL]). Total de R$ 3.717.000,00. "Chave na mão" como "tudo incluso". "Fundação em radier de concreto armado" como premissa. Validade de 30 dias como prazo de decisão | 8 itens "Não inclusos" por escrito ("demolição de construções existentes; piscina; paisagismo; ar-condicionado; automação; projetos complementares e aprovações; ligações definitivas de concessionárias; sondagem complementar"); a plataforma de D. Lourdes não é mencionada. Sondagem 5.7: NA 0,90 m e "Argila orgânica mole de 2,5 m a 9,0 m"; Skill de fundações v1.3: radier "inviável na maioria dos casos" → risco de aditivo [NC]. Vence ~29/10/2026 [ECF: 29/09 + 30 dias]. A proposta não abre o BDI, não diz o número-índice-base e não diz se o reajuste mensal incide por medição ou sobre o saldo (perguntas, seção 5). 6.300 ÷ 3.691,68 = 1,707. |
| **5.13 Planilha do corretor** | **C1** (vendida, escritura, 03/2026, "450 m² construídos"; base total [PV]). **C4** (vendida, escritura, 06/2026, "fundos para o lago", "500 m² construídos"; pavimentos não informados). **C2** (anúncio, 09/2026, "480 m² construídos") homogeneizado pela oferta: R$ 12.900 a 13.650/m² [ECF], só como confirmação | **C3** ("Lotes 22 + 23 Qd C (unificados)", "1.200 m²", anúncio): base de área **não declarada**; provavelmente terreno (1.200 = 2 × 600) [PV]; rejeitada pelos dois lados. **C5**: "2 pav. + subsolo + rooftop com piscina", outro condomínio, 680 m², anúncio; subsolo vedado (Art. 8º) e rooftop vedado (Art. 7º) [PV: enquadramento]. **C6**: 11/2021, "420 m²", base não declarada. A média de R$ 12.833. Os R$ 7,67 milhões (590 m²). Os R$ 8,8 milhões ("com o rooftop pela Mais-Valerá"). A outorga de "R$ 380 mil para 300 m² a mais" | A média mistura venda e anúncio sem fator de oferta, provável área de terreno com área construída, atributos vedados e dado velho. Fiker v6, seção 2.1. |
| **5.14 Carta do banco** (15/09/2026) | "Crédito aprovado: até R$ 3.000.000,00, liberado em parcelas conforme medição de obra". "Cada liberação limitada a 60% do valor do imóvel (terreno + obra executada), apurado por vistoria e laudo de avaliação do próprio banco". "Condição: licença de obras emitida até 30/06/2027" [FP] | Qualquer leitura de que os 60% ampliam o crédito ou incidem sobre o valor futuro da casa pronta | Laudo do banco [NC]; pode cair perto do controle web (j'). Ressalva R3 de Kelsen: a licença do LICIN Art. 4º §2º vale 3 meses [PL]; se atende à condição do banco é pergunta ao Legal/banco. |

---

## 4. Respostas às mensagens 5.15 (texto para revisão de Wallenberg; não é enviado)

### Rodrigo: "A construtora fecha em R$ 6.300 o m², tudo incluso. 520 m² dá R$ 3,28 milhões, sobra quase R$ 1 milhão do teto. Já dá pra fechar com eles?"

**Resposta:** Rodrigo, ainda não dá para fechar. A conta está certa como multiplicação, mas a sobra não é de R$ 1 milhão.
- **Área:** os 520 m² só existem se uns 63 m² vierem de varandas e garagem, que não contam no limite da lei. Isso o arquiteto ainda vai ver. E se a faixa de proteção do lago for confirmada, o limite cai para perto de 340 a 360 m², e os 520 m² não cabem.
- **"Tudo incluso":** a própria proposta lista como não inclusos a demolição, a piscina, o paisagismo, o ar-condicionado, a automação, os projetos complementares e aprovações, as ligações definitivas e a sondagem complementar. Também **não menciona a plataforma (ou elevador) da D. Lourdes**, que, com a obra e o reajuste até a instalação, pode custar algo entre R$ 47 mil e R$ 196 mil (elevador: R$ 123 a 312 mil).
- **Fundação:** a proposta prevê radier. A sondagem mostra água a 90 cm e argila mole até 9 m. Se o engenheiro de estrutura pedir estacas, vem um custo extra que hoje ninguém consegue calcular. Essa definição é do projeto de fundação, não minha.
- **Tempo:** a proposta diz que o preço é reajustado pelo INCC-M todo mês, a partir da data dela (29/09/2026). A obra deve ir de maio/2027 até perto de dezembro/2028, então os R$ 3,28 milhões viram algo entre R$ 3,56 e 3,78 milhões ao longo dos pagamentos. **A sobra cai para R$ 420 a 640 mil; tirando a plataforma, R$ 220 a 590 mil**, e é dela que ainda saem os itens não inclusos. Essa conta parte do índice de setembro/2026; se a construtora usar o de agosto, o custo sobe mais uns R$ 9 mil. A proposta vence no fim de outubro, antes de existir projeto.
- **Fora da obra:** o aluguel de vocês, de hoje até a mudança em dezembro/2028, soma cerca de R$ 486 mil. Não sai do teto de obra, mas sai do caixa da família.

O caminho é pedir o preço de novo com anteprojeto e projeto de fundação, a pelo menos duas construtoras, com o BDI aberto, a plataforma incluída e, por escrito, qual índice do INCC-M é a base e se o reajuste mensal incide por medição ou sobre o saldo.

**Fundamento:** Mascaró v6, seções 5 e 8.1: 520 × 6.300 = 3.276.000; × 1,087293 = 3.561.972; × 1,154922 = 3.783.524; 4.200.000 − 3.783.524 = 416.476 e − 3.561.972 = 638.028; menos plataforma: 416.476 − 196.337 = 220.139; 638.028 − 46.754 = 591.274 [ECF; taxa extrapolada; índice-base set/26 [PV]]. Alternativa ago/26: +R$ 8.905 a 9.459 [ECF]. Cláusula de reajuste, literal: "INCC-M mensal a partir da data desta proposta" (5.12, 29/09/2026) [FP]. Não inclusos: 5.12 [FP]. Plataforma: artigo do Monitor do Mercado datado de 24/08/2026 (fonte fraca), soma com obra civil de Mascaró [ECF], reajustada. Solo: 5.7; Skill fundações v1.3 §3.1. H1: seção 2.2, a'. Aluguel: seção 2.6.

### Rodrigo: "O Marcelo mandou a planilha: a casa pronta vale R$ 7,7 milhões, e com o rooftop R$ 8,8. O banco libera 60% do valor do imóvel, então dá pra pedir uns R$ 5 milhões em vez de 3. Pode usar esse número?"

**Resposta:** Não, Rodrigo. Esse número não existe, por três razões.
- **O crédito aprovado é de até R$ 3 milhões.** Pela carta do banco, os 60% não aumentam esse teto; eles limitam cada liberação.
- **Os 60% incidem sobre o terreno mais a obra já executada**, não sobre a casa pronta. E quem avalia é o banco, com laudo próprio.
- **Os R$ 7,7 e 8,8 milhões não se sustentam.** O primeiro usa 590 m², que não cabem no lote. O segundo põe preço num rooftop que o regulamento do condomínio veda. Pelas vendas no próprio condomínio, uma casa de 500 a 520 m² construídos ficaria entre R$ 6,5 e 7,8 milhões; mas os anúncios de casas do mesmo porte no resto do Recreio, já descontada a margem de negociação, apontam R$ 3,5 a 5,8 milhões, e o laudo do banco pode ficar mais perto desse lado. Esse número também depende de conferir as escrituras das vendas.

Para planejar, o número é o que já temos: R$ 4,2 milhões (R$ 3 milhões do banco e R$ 1,2 milhão de recursos próprios).

**Fundamento:** carta 5.14 [FP, literal na seção 3]; "os 60% não aumentam o teto" é leitura minha da carta [PV], coerente com o texto literal. 60% × 8,8 mi = R$ 5,28 mi é a conta implícita no pedido [PV]. Só como ilustração: se o laudo desse ao terreno o preço pago, o limite antes de obra seria 60% × 3,3 mi = R$ 1,98 mi; o laudo real é [NC]. 590 m² fora do limite: Etapa 01 [PL]. Rooftop: Regramento Art. 7º, "Vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje de cobertura" (5.4) [FP]. Revenda: seção 2.2, linhas j e j' (R$ 3.545.500 a 5.811.000; 7 anúncios de 450 a 570 m², filtro na construída ±15%); Fiker v6, seções 3 e 4.

### Helena: "Pagamos R$ 3,3 milhões num terreno que a escritura diz ter 600 m² e que, pelo que entendi, mede menos. Quero saber quanto isso pesa em dinheiro. E queremos o comparativo CAB x CAM que o corretor falou, com o valor da outorga."

**Resposta:** Helena, aqui vai o peso em dinheiro, por duas medidas. Nenhuma delas é "o prejuízo".
- **Rateio pelo preço pago:** faltam 28,20 m² dos 600 m². Pelo preço pago, isso equivale a cerca de **R$ 155 mil**. É proporção; terreno não vale proporcionalmente à área.
- **Efeito no que dá para construir e vender:** com 571,80 m², a casa pode ter cerca de 457 m² "contáveis"; com 600 m², 480 m². Essa diferença vale entre **R$ 170 e 230 mil líquidos** em revenda, já descontado o custo de construir os 22,56 m² a mais. Estimativa com amostra pequena, sem descontar o custo de uma eventual regularização.
- **A causa da diferença e o que fazer a respeito são questões jurídicas.** Não tenho resposta sobre elas e não vou antecipar nenhuma. Já encaminhamos a pergunta ao nosso Legal, que vai responder com base na lei lida. Até lá, o que posso dar é só o peso em dinheiro acima.
- **Comparativo CAB x CAM:** no lote de vocês os dois coeficientes são iguais (1,0), segundo o levantamento do nosso Legal. Não há outorga para comprar: **o valor da outorga é zero**. A simulação de R$ 380 mil do corretor foi feita em outro condomínio, com outra regra. O comparativo que importa é **com ou sem a faixa de proteção do lago**: se ela for confirmada, a área "contável" cai de cerca de 457 para cerca de 297 m², o programa de 520 m² deixa de caber, e a casa pronta perde algo como **R$ 2 milhões** de valor de mercado (entre R$ 1,1 e 3,4 milhões, conforme as premissas), ou R$ 1,2 a 1,6 milhão depois de descontar a obra menor.

**Fundamento:** 3.300.000 × 28,20 / 600 = R$ 155.100 [ECF] (Fiker v6, seção 8). S2 − S1 e lago: seção 2.3 [ECF]. CAB = CAM: RIU 5.3 [FP]; LC 270 Art. 345 §3º (Etapa 01) [PL]. **Nenhuma conclusão jurídica nesta resposta**: causa, responsável, direito e prazos estão com Kelsen (seção 5, pergunta 1). Código Civil Arts. 500 e 501 não lidos no primário por mim e não citados ao cliente.

---

## 5. Recomendação e encaminhamentos

### Recomendação (condicional ao que está aberto)

1. **Não há decisão CAB x CAM a tomar.** Base de projeto: **S1** (457,44 m² computáveis [PL]; 500 a 520 m² construídos de trabalho [PV]), com variante **H1** (297,28 computáveis [PL]) até SPU, INEA e SMAC responderem.
2. **O lago é a incerteza que mais vale:** se a APP for confirmada, cerca de R$ 2,1 a 2,4 mi de revenda (R$ 1,2 a 1,6 mi líquidos). As consultas do Legal (Etapa 01, seção 4.2) são caminho crítico também da viabilidade.
3. **A divisa:** regularizar vale cerca de R$ 0,17 a 0,23 mi líquidos em revenda [ECF, média-baixa], menos custo e tempo da regularização [NC]. Se e como regularizar é questão jurídica, com Kelsen.
4. **Construtora:** não fechar agora. Recotar com anteprojeto e projeto de fundação, ao menos duas propostas, BDI aberto, plataforma incluída, e por escrito: **qual número-índice do INCC-M é a base** (set/2026 ou ago/2026; adotei set/2026 [PV], diferença ≈ R$ 8,6 a 9,5 mil) e se o reajuste mensal incide por medição ou sobre o saldo. O índice (INCC-M), a periodicidade (mensal) e o marco ("a data desta proposta") já estão na 5.12.
5. **Teto de R$ 4,2 mi (com reajuste em todo o cronograma):** a parcela calculável do S1 ocupa **56% a 67%** pela via do CUB (2.339.938 / 4.200.000 = 0,557; 2.830.995 / 4.200.000 = 0,674) e **82% a 90%** pela via da proposta (3.424.973 / 4.200.000 = 0,815; 3.783.524 / 4.200.000 = 0,901). Somando a plataforma **reajustada** (R$ 46.754 a 196.337): **57% a 72%** (0,568; 0,721) e **83% a 95%** (0,827; 0,948). Com a alternativa ago/26, a via da proposta muda menos de 0,3 ponto percentual. Sobra contra o teto, via CUB, depois da plataforma: R$ 1.172.668 a 1.813.308 (Mascaró v6, §5.3). O resto paga itens sem número; o maior é a fundação em solo mole. **Não afirmo que cabe.**
6. **Caixa da família, à parte do teto:** aluguel de R$ 486 mil de out/2026 a dez/2028 (seção 2.6).
7. **Revenda:** não usar nenhum número como valor esperado antes de conferir C1 e C4. Com o filtro na base certa, o controle web de S1 é **R$ 3,55 a 5,81 mi** e a distância até o piso do condomínio é de **16%** (R$ 0,91 a 0,95 mi), mas o topo depende de um anúncio só (W8); sem ele, a distância volta a 33%. Para o banco, considerar que o laudo pode cair perto da faixa web. Em S3, o controle web de alto padrão declarado dá R$ 3,2 a 4,4 mi, e o único anúncio de 2 pavimentos confirmado (W5), R$ 3,1 a 3,4 mi: reforça que o risco de S3 é para baixo.

### Para Lúcio (Arquitetura), via Wallenberg

- **Pela premissa de área de trabalho, o programa de 520 m² não cabe em H1.** Com a APP de 30 m, o teto computável é 297,28 m² [PL]; os 520 m² exigiriam 222,72 m² não computáveis, muito acima dos 42,56 a 62,56 m² que usei como premissa. Se H1 se confirmar, a redução ou reorganização do programa é decisão de Lúcio com a família; a suíte térrea acessível de D. Lourdes é item do programa.
- Em H0 (S1), os 520 m² dependem de cerca de 63 m² não computáveis: Lúcio confirma se isso é possível.
- **Garagem coberta:** só 1 vaga coberta fica fora da TO [PL]; cada 10 m² a mais de garagem coberta na projeção tiram 10 m² computáveis da casa (até R$ 130 a 150 mil de revenda).
- **Plataforma ou elevador para D. Lourdes:** definir o tipo. NA a 0,90 m e Art. 8º ("Vedado subsolo e qualquer escavação com profundidade superior a 1,20 m, salvo piscina com profundidade máxima de 1,60 m"); se o poço é compatível é pergunta a Kelsen e Baumgart.
- Entregar o **quadro de áreas por tipo** e, se possível, um **cronograma físico-financeiro** preliminar (estreita a faixa do reajuste e confirma ou corrige a premissa de fim em dez/2028). Com o quadro, o filtro de comparáveis também é refeito.
- Dimensão e número de vagas cobertas; dimensão da piscina nova.
- Cada m² de **área equivalente** (área interna com acabamento, coeficiente 1,00) custa cerca de R$ 3.692 só de CUB (set/2026), antes de BDI e reajuste; varanda e garagem entram com coeficiente menor (Skill §2.3).

### Para Kelsen (Legal), via Wallenberg

1. **Diferença de área (28,20 m², 4,70% de 600 m²; compra e venda registrada em 07/2026, 5.1):** causa, contra quem e por qual caminho a família pode agir, e se há prazo correndo. Precisa da leitura no primário do Código Civil (Arts. 500 e 501 vistos por mim só em fonte secundária) e do que a Etapa 01 levantou sobre a divisa com o Lote 16. **Nada disso foi dito ao cliente.**
2. **Regramento Art. 8º:** a vedação alcança blocos de coroamento, baldrames, estacas e o **poço da plataforma/elevador**?
3. **Vaga coberta e TO:** confirmar que só 1 vaga coberta sai da TO (Art. 350 III) e como o condomínio mede a TO.
4. **CAB = CAM (LC 270 Art. 345 §§3º e 5º):** confirmação, sem reabrir.

### Para Wallenberg

1. **Cardozo/Baumgart (entre Gestores, decide Wallenberg):** radier × SPT 5.7; quantitativo preliminar de estacas (destrava o maior [NC]); profundidade dos furos de 2024; atrito negativo, se houver aterro até a cota de soleira prevista (5.2: "Cota de soleira prevista: +3,20 m (referência do condomínio)"; a altura do aterro não é conhecida [PV]); poço da plataforma × NA 0,90 m. Saturnino: esgotamento.
2. **Banco:** a licença do Art. 4º §2º (3 meses) atende à condição (R3 de Kelsen)? Que comparáveis e que fator de oferta o laudo usa?
3. **Lista de compra do acervo:** ABNT NBR 12721:2006 e NBR 14653-2:2011.
4. **Num caso real, eu perguntaria (não feito; é ensaio):** ao corretor, escrituras de C1 e C4, se a área é total, computável ou averbada, e a base dos 1.200 m² de C3; à construtora, composição do preço, BDI, **qual número-índice do INCC-M é a base ("mês da proposta ou mês anterior?")**, **se o reajuste mensal incide sobre cada medição ou sobre o saldo**, e se a plataforma entra; a 3 fabricantes do RJ, preço da plataforma instalada com e sem poço; à Comissão de Obras, a taxa de análise do Art. 9º; à família, se o aluguel tem reajuste contratual; ao topógrafo, a altura do aterro até a cota de soleira; à imobiliária de W8, se o anúncio é de venda e qual o lote e os pavimentos. Listas completas: Mascaró v6 seção 10; Fiker v6 seção 9.
5. **Processo:** Skill v1.5 nas **3 cópias** (`.claude/skills/.../SKILL.md`, `01_CEO/Skills_Propostas/2026/Outubro/villaca_viabilidade-...md` e o espelho `.agents/skills/.../SKILL.md`, que estava na v1.3), com backup integral de cada uma em `01_CEO/Decisoes_Autonomas/_backups/2026-10-05/*_INTEGRAL_ANTES_v1.5.md`. Grep confirmou "version: v1.5" nas 3. O espelho `.agents` recebeu o mesmo conteúdo da cópia viva; só a cópia de registro de Skills_Propostas tem, a mais, a linha "CÓPIA DE REGISTRO". **Fica com você** definir quem sincroniza o espelho a cada versão de Skill (item 4 do parecer v6); até lá, eu sincronizo as 3 cópias a cada versão desta Skill.
6. **Nada vai ao cliente sem a sua revisão.** A seção 4 é rascunho.

---

## 6. Auditoria de Villaça sobre Mascaró e Fiker, e revisão completa (v7)

**Método:** Fiker acionado com delegação **bloqueante** (correção do filtro); Mascaró não acionado, porque nada do custo depende do filtro. Refiz as contas de Fiker (seção 2.2, "Contas refeitas na v7") antes de integrar. Depois reli as 3 peças inteiras contra o enunciado e contra o checklist da Skill v1.5 §4.1. A auditoria da v6 (seções 6.1 a 6.3 da v6) fica como histórico na pasta dela.

### 6.1 Mascaró (`custo_obra_mascaro_003_v6.md`, cópia sem alteração)

| Item | Decisão | Observação |
|---|---|---|
| Peça copiada da `v6/` sem alteração de texto nem de número | **Declarado** | Mascaró não foi acionado. |
| Releitura integral contra o checklist §4.1 (base de área; rótulos [DOC]/[PL]/[PV]; datas da Cronoshare, do Monitor do Mercado, do CUB e da FGV; nota do CUB com a condição do playground; reajuste até cada pagamento; números com fonte; 520 m² não cabe em H1) | **Sem achado** | Todas as somas e produtos da §5.1.1, §5.3, §6 item 3 e §8 conferem com a §2.2 daqui. |
| A peça cita a Skill **v1.4** | **Mantido, declarado** | Era a versão vigente quando a peça foi feita; a v1.5 muda só a revenda (§3.1, §3.2), o roteiro item 3, o M5 e acrescenta a §4.1. A §2 (custo) é igual. |
| A peça cita "Fiker" só na §9 (base de custo ≠ valor de mercado) | **Coerente** | Não cita número de revenda; nada depende do filtro. |

### 6.2 Fiker (`revenda_fiker_003_v6.md`)

| Item | Decisão | Observação |
|---|---|---|
| Filtro de metragem refeito na construída de trabalho, ±15% sobre os extremos (S1 425–598; S2 444–624; S1/S2 425–624; S3 289–414), anúncio a anúncio | **Integrado** | Conferi: 500 × 0,85 = 425; 520 × 1,15 = 598; 522,56 × 0,85 = 444,18; 542,56 × 1,15 = 623,94; 339,84 × 0,85 = 288,86; 359,84 × 1,15 = 413,82. W1–W4, W6, W7, W8 (450 a 570) em S1/S2; W10, W11, W13, W9, W5 (310 a 400) em S3; W12 (267) fora. |
| R$/m² homogeneizado sobre preço e área exatos; correções de arredondamento em W8, W9, W3 × 0,86, W4 × 0,86 e W11 × 0,91 | **Integrado** | Conferi as 5. Nenhuma das 3 que Fiker achou a mais (W3, W4, W11) é extremo de faixa nem mediana. |
| j', distância, S3 e linha "controle web" do lago | **Integrado** | Batem com as minhas contas (seção 2.2 e 2.3 daqui). |
| W1 na "Limitação de tipo"; campos não registrados em 02/10 para W5, W8, W9, W10, W11, W13 declarados | **Integrado** | Conferi a lista contra a tabela dele. |
| **Ajuste meu 1:** "ordem de grandeza de S3 para o cliente" dizia "R$ 3,2 a 5,4 milhões" e, na mesma frase, "R$ 3,1 a 3,4 mi pelo W5" (abaixo do piso) | **Corrigido por mim** | Agora R$ 3,1 a 5,4 milhões, no §5.2 e no "O que muda" dele. |
| **Ajuste meu 2 e 3:** "W11 e W9 (padrão não declarado)" e "W11 e W9, por exemplo, não declaram", quando a tabela diz que em W9 o padrão "não foi registrado" | **Corrigido por mim** | Texto alinhado à tabela (W11 não declara; W9 e W5 não registrados em 02/10). |
| **Ajuste meu 4:** a frase da §5.2 sobre S3 cita o W5; conferida contra a tabela da §2.2 dele ("2 pav.", 9.030 a 9.555) | **Conferido** | Sem mudança. |

### 6.3 Revisão completa das 3 peças contra o enunciado e o checklist da Skill v1.5 §4.1

| # do checklist | O que conferi | Resultado |
|---|---|---|
| 1. Base de área | Toda linha da matriz (§2.2) diz a base; custo sobre equivalente (b–e), via construtora e revenda sobre construída (f, j, j'); computável só em a | OK |
| 2. Filtro de comparáveis | Faixas na construída de trabalho ±15%, declaradas na §1 daqui e na §2.2 de Fiker; anúncio por anúncio | **Corrigido nesta versão** |
| 3. Rótulos | Áreas [PL]/[PV] iguais nas 3 peças; tolerância do filtro [PV]; área dos anúncios como construída [PV] aqui e [INF] em Fiker (equivalentes pela legenda); citações literais do Dossiê com [FP] | OK |
| 4. Datas e coerência interna | 33% / R$ 1,66 mi / R$ 5,10 mi / "só W10" / "faixas serão refeitas" procurados por Grep nas peças v7: aparecem só como histórico da v6 ou como "sem W8"; datas da página (Cronoshare), do artigo (Monitor), da emissão (CUB), da divulgação (FGV) e da publicação dos anúncios ditas como tal; o mesmo número em dois lugares conferido (j' na §0, §2.2, §4 e §5; distância na §0, §2.4 e §5) | OK |
| 5. Nota do CUB | Mascaró §6 transcreve a nota com "playground (quando não classificado como área construída)" | OK |
| 6. Reajuste | INCC até cada pagamento (piso no mês médio, teto no fim), índice-base [PV] com alternativa ago/26 | OK |
| 7. Conclusão jurídica | Helena: só o peso em R$ e "está com o Legal"; CC 500/501 não citados ao cliente | OK |
| 8. Número sem fonte | Todo número tem fonte ou é [NC]; tolerância de ±15% é premissa declarada | OK |
| 9. Programa que não cabe | 520 m² × H1 dito na §0, na §5 (Lúcio) e na resposta ao Rodrigo | OK |
| 10. Conta sobre valor arredondado | R$/m² dos anúncios refeitos sobre preço e área exatos; k' refeito com e exato (2.339.938,10 etc.) | **Corrigido nesta versão** |
| Enunciado §3.3 itens 1 a 8 | Premissas do Legal (§1), matriz (§2), triagem 5.11 a 5.14 (§3), respostas 5.15 (§4), recomendação e encaminhamentos (§5), auditoria (§6), fontes e Skills (§7), declaração (§8) | OK |

**Resultado:** mudaram j', k', a distância (33% → 16%), a linha S3 do controle web, a resposta ao Rodrigo sobre a casa pronta e a recomendação 7. Custo, j, k, lago, divisa, aluguel, Helena e plataforma foram reconferidos e não mudaram.

---

## 7. Fontes e Skills usadas

| Fonte | Data-base | Acesso | Uso |
|---|---|---|---|
| Sinduscon-Rio, CUB/m² set/2026 (NBR 12.721), data de emissão 29/09/2026 15:21 | set/2026 | 02/10/2026; reaberto em 05/10/2026 (Mascaró, PDF; nota de exclusões transcrita) | linha b; exclusões |
| FGV IBRE, INCC-M set/2026 (divulgado em 25/09/2026), com as variações mensais de 2026 | jan a set/2026 | 02/10/2026; reconferido em 05/10/2026 (Mascaró) | linha d (taxa extrapolada); reajuste da demolição; variação de set/26 (0,25%) na alternativa ago/26 |
| Dossiê 5.12, cláusula de reajuste | 29/09/2026 | — | fonte primária do índice (INCC-M), da periodicidade (mensal) e do marco ("a data desta proposta"); o número-índice-base é [PV] |
| Polícia Federal/MJSP, Minuta de Contrato de obra, Proc. 08400.007001/2018-11, cláusula 3.3 | 2018 | 02/10/2026 | Skill M7, só apoio |
| TCU, Acórdão 2622/2013-Plenário (BDI) | 2013 | 02/10/2026 | linha c [ECF] |
| Cronoshare, demolição (página datada de 02/01/2026; mês-base do preço incerto) | dez/2025 ou jan/2026 [PV] | 02/10/2026; reconferida em 05/10/2026 (Mascaró) | linha e, fraca |
| SINAPI 100651 e 100652 via orcamentor.com | 07/2026 | 02/10/2026 | linha g, só unitário |
| Monitor do Mercado, elevador/plataforma residencial (artigo datado de 24/08/2026) | tratado como set/2026 [PV] | 02/10/2026; reconferido em 05/10/2026 (Mascaró) | linha e', fraca |
| Raio-X FipeZAP 2T2026 via Portas | reportagem de 18/08/2026 | 02/10/2026 | fator de oferta 0,86 a 0,91 |
| Attria e Consultoria VM, anúncios W1 a W13 (links em Fiker v6) | publicados de 05 a 09/2026 (W6 e W7 sem data) | 02/10/2026; relidos em 05/10/2026 só para texto e rótulo (Fiker v5); na v6 de Fiker nenhuma página foi aberta | linha j' |
| Dossiê 5.1 a 5.15 e caso base (fictícios) | — | — | áreas, preços, C1 a C6, cronograma, aluguel |
| Etapa 01: Hely e Kelsen | aprovada em 01/10/2026 | — | premissas [PL] |

**Skills:**
- `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` **v1.5** (dono Villaça). Ressalva: NBR 12721 e 14653-2 não lidas no oficial.
- `legal-oodc-mais-valera-mais-valia` v1.1: CAB = CAM → sem OODC.
- `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3: risco do radier.
- `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`: poço da plataforma e esgotamento.

**Divergências Skill x fonte primária:** nenhuma aberta. A da v1.3 (playground sem a condição) foi resolvida na v1.4. A v1.5 não toca em texto de fonte primária: acrescenta regra de método (filtro na mesma base) e o checklist §4.1. A tolerância de ±15% é exemplo de método, declarado como premissa, não citação da NBR 14653-2 (não lida no oficial). Macete alterado: M5 (fator área medido na mesma base de área).

**Bloqueios de ferramenta (mantidos):** Planalto (ECONNRESET); DataZAP 404; Loft 410; ImóvelWeb e CasaMineira 403; SINAPI 100650 404; PDF do MPF 404. Nenhum número veio de página bloqueada.

---

## 8. Declaração de ensaio

Pré-Estudo v7 do **Ensaio Sombra 003, Etapa 02**. Cliente, lote, condomínio, documentos e números do Dossiê são **100% fictícios**. Índices, normas e dados de mercado da web são reais, com fonte e data de acesso.

- Nada foi enviado a ninguém; ninguém foi contatado.
- Não abri, listei nem citei nada em `_gabaritos_LACRADO/`. O `parecer_bardi_v6.md` foi lido por ordem de Wallenberg.
- A v1 a v6 foram mantidas intactas.
- Nenhum número aqui é valor de venda prometido nem custo fechado. As respostas ao cliente são rascunho para revisão de Wallenberg.

— Villaça, Gestor Viabilidade, 05/10/2026
