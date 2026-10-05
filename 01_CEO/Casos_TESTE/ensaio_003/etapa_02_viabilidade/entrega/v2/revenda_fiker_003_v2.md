# Ensaio 003, Etapa 02: Valor de revenda, v2 (Fiker)

**Para:** Villaça (Gestor de Viabilidade). A integração e a auditoria são dele.
**De:** Fiker (Agente de Valor de Mercado / Comparáveis)
**Data de referência:** 02/10/2026. Pesquisa web e acessos em 02/10/2026.
**Versão:** v2. Corrige a v1 (`../revenda_fiker_003.md`, mantida intacta), que foi reprovada por Claudemberg por três motivos: (1) aplicou R$/m² de área construída sobre a área computável; (2) não aplicou fator de oferta aos anúncios; (3) deixou S3 sem ordem de grandeza em R$.
**Skill aplicada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.0, §3 (base de área igual, fator de oferta, fator área, restrição nova, ordem de grandeza). A Skill tem ressalva de fonte: a NBR 14653-2 não foi lida no texto oficial (R1), e o fator de oferta foi calibrado com dado nacional (R2).

**Rótulos:**
- **[FP]** fonte primária: documento do dossiê ou anúncio aberto individualmente.
- **[EF]** estimativa com fonte: conta minha sobre números [FP].
- **[PV]** premissa fixada por Villaça.
- **[NC]** não calculável.

---

## 0. Premissas de área (fixadas por Villaça, porque Lúcio ainda não desenhou) [PV]

| Cenário | Área computável (Legal) | Área construída de trabalho (base da revenda) | Diferença construída − computável |
|---|---|---|---|
| S1 / H0 | 457,44 m² | 500,00 a 520,00 m² | 42,56 a 62,56 m² |
| S2 | 480,00 m² | 522,56 a 542,56 m² | 42,56 a 62,56 m² |
| S3 / H1 | 297,28 m² | 339,84 a 359,84 m² | 42,56 a 62,56 m² |

- A faixa não computável (42,56 a 62,56 m²) é a mesma nos três cenários: varanda, garagem, área técnica etc. É premissa de Villaça, não é desenho.
- **Premissa de base dos comparáveis:**
  - Os "m² construídos" de C1, C2 e C4 são **área construída total**, como informado pelo corretor.
  - Em W1 a W13, a área usada é a **área construída anunciada**.
- **Sentido do erro se a premissa falhar:**
  - **C1, C2 e C4.** Se os 450, 480 e 500 m² forem, na verdade, área computável (ou averbada sem varanda e garagem), o R$/m² real sobre a construída total seria menor. Nesse caso, a v2 **superestima** o valor, e a conta certa voltaria a ser a da v1: R$/m² × computável. O tamanho do erro é exatamente a diferença da seção 3.2, de R$ 553.280 a R$ 938.400 por cenário.
  - **Anúncios W.** Se a área anunciada for área útil ou privativa (menor que a construída), o R$/m² real sobre a construída seria menor, e o controle web cairia ainda mais. Se a área anunciada incluir área descoberta (terraço), o R$/m² real sobre a construída coberta seria maior.

---

## 1. Resumo para Villaça

| Cenário | Construída de trabalho | **Faixa principal**: C1/C4 × construída | Controle web com fator de oferta (× construída) | Peso do lago (S1 − S3, mesma base) | Confiança |
|---|---|---|---|---|---|
| S1 | 500 a 520 m² | **R$ 6.500.000 a R$ 7.800.000** [EF] | R$ 3.545.500 a R$ 5.100.160 [EF] | n/a | média-baixa |
| S2 | 522,56 a 542,56 m² | **R$ 6.793.280 a R$ 8.138.400** [EF] | R$ 3.705.473 a R$ 5.321.428 [EF] | n/a | média-baixa (depende da divisa) |
| S3 | 339,84 a 359,84 m² | **R$ 4.417.920 a R$ 5.397.600** [EF], ordem de grandeza com faixa larga e risco para baixo | R$ 3.943.164 a R$ 4.418.116 (só W10), ou R$ 1.979.908 a R$ 4.418.116 (W10 + W11) [EF] | **R$ 2.082.080 a R$ 2.402.400** (mesmo R$/m²); faixa larga de R$ 1,10 mi a R$ 3,38 mi [EF] | baixa |

**Os quatro achados que mais pesam:**

1. **Na base certa, a revenda sobe em relação à v1.** Em todos os cenários, a faixa sobe de R$ 553.280 (piso) a R$ 938.400 (topo). A causa é a área de 42,56 a 62,56 m² que a v1 deixava fora da multiplicação. O número só vale se os "m² construídos" do corretor forem área total. Se não forem, o certo é o número da v1 (seção 0).
2. **Com o fator de oferta, a distância até o mercado web aumenta, em vez de diminuir.**
   - Sem fator, o piso do condomínio (R$ 13.000/m²) ficava cerca de 21% acima do maior anúncio web. Com o fator, fica 33% acima (13.000 / 9.808 = 1,325).
   - Na comparação em reais, para S1 com 520 m²: o piso do condomínio é R$ 6.760.000 e o topo do controle web é R$ 5.100.160. A distância é de R$ 1.659.840.
   - Por isso, as escrituras C1 e C4 precisam ser conferidas antes de qualquer uso diante do banco.
3. **C2 homogeneizado fica dentro da faixa das vendas.** Com o fator de oferta: 15.000 × 0,86 a 0,91 = R$ 12.900 a R$ 13.650/m². Isso confirma C2 como dado coerente com C1 e C4, e não só como teto.
4. **O lago pesa cerca de R$ 2,1 a 2,4 milhões na revenda** (de S1 para S3, mesmo R$/m², mesma base). A faixa larga vai de R$ 1,1 a 3,4 milhões, com as premissas na seção 5.3. O sentido provável do erro é o de o peso ser maior, porque a APP também desvaloriza o terreno.

---

## 2. Comparáveis, com a base de área em cada linha

### 2.1 Planilha do corretor (5.13), tratamento linha a linha (mantido da v1, com base e fator acrescentados)

| Ref | Situação / data | Área informada | **Base de área** | Preço | R$/m² bruto | Fator de oferta | R$/m² homogeneizado | Decisão |
|---|---|---|---|---|---|---|---|---|
| C1 | venda (escritura) 03/2026, Lote 04 Qd A, 2 pav., frente para rua interna | 450 m² | **construída total [PV, informada pelo corretor]** | R$ 5.850.000 | 13.000 (5.850.000 / 450) [FP] | **nenhum** (venda) | **13.000** | **ACEITA**: núcleo e piso; não tem o efeito do lago |
| C2 | anúncio 09/2026, Lote 11 Qd B, 2 pav. | 480 m² | **construída total [PV]** | R$ 7.200.000 | 15.000 (7.200.000 / 480) [FP, anúncio] | 0,86 a 0,91 | **12.900 a 13.650** [EF] | **ACEITA COM AJUSTE**: entra homogeneizada como confirmação; fica fora da faixa principal, que usa só vendas |
| C3 | anúncio 08/2026, Lotes 22 + 23 Qd C | "1.200 m²" | **área de terreno** (1.200 = 2 × 600) | R$ 9.600.000 | 8.000 de **terreno**, não comparável | não se aplica | não se aplica | **REJEITA**: área de terreno; lote duplo; área construída não informada |
| C4 | venda (escritura) 06/2026, Lote 09 Qd C, fundos para o lago | 500 m² | **construída total [PV]** | R$ 7.500.000 | 15.000 (7.500.000 / 500) [FP] | **nenhum** (venda) | **15.000** | **ACEITA COM RESSALVA**: pavimentos não informados; vendida antes da questão da APP (seção 5) |
| C5 | anúncio 09/2026, Jardim dos Socós, 2 pav. + subsolo + rooftop | 680 m² | construída (como informado) | R$ 11.560.000 | 17.000 | não aplicado | não se aplica | **REJEITA**: atributos vedados aqui (Art. 7 e 8 do Regramento); fora da metragem; outro condomínio |
| C6 | venda 11/2021, Lote 31 Qd B | "420 m²" | **desconhecida** (construída ou terreno) | R$ 3.780.000 | 9.000 | não se aplica | não se aplica | **REJEITA**: quase 5 anos; não há índice de casa (o FipeZAP mede apartamento); base de área desconhecida |

**Média do corretor (R$ 12.833/m²):** a conta está certa, (13.000 + 15.000 + 8.000 + 15.000 + 17.000 + 9.000) / 6 = 12.833. **O método é inválido**:
- mistura 3 vendas e 3 anúncios, sem fator de oferta;
- mistura R$/m² de terreno (C3) com R$/m² construído;
- inclui um condomínio com atributos vedados aqui (C5);
- inclui um dado de 2021 (C6).

A coincidência com C1 é acaso: os erros para baixo (C3, C6) compensam o erro para cima (C5).

**Números do rodapé, recusados (mantido da v1):**
- **"R$ 7,67 mi para 590 m²"** (13.000 × 590 = 7.670.000, conta conferida). Os 590 m² vêm do estudo de massa de 2024, que o Legal descartou. **Não usar.** Na base certa, o número comparável é o de S1 na construída: R$ 6,50 a 7,80 mi. O topo coincide com a ordem de grandeza do corretor só porque usa R$ 15.000 sobre 520 m², e não pelo método dele.
- **"R$ 8,8 mi com rooftop":** atribui cerca de R$ 1,13 mi (8,8 − 7,67) a um rooftop vedado (Art. 7). Não tem comparável. **Não usar.**
- **Outorga de R$ 380 mil (Lote 5, Jardim dos Socós, CAM 1,5):** não muda a revenda, porque o CAM aqui é 1,0 e não há área adicional. O custo da OODC é com Villaça.

### 2.2 Anúncios web. Todos foram abertos individualmente em 02/10/2026; todos são anúncio; todos estão no Recreio dos Bandeirantes

Fator de oferta 0,86 a 0,91 (Skill §3.3, macete M6; referência nacional, não local). As contas de R$/m² foram conferidas duas vezes. Os valores estão arredondados ao real.

**Faixa S1/S2 (430 a 520 m²): entram no controle**

| # | Imóvel | Área | **Base de área** | Terreno | Pav. | Preço pedido | R$/m² bruto | × 0,86 | × 0,91 | Publicado | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Bothanica Nature, CA2947 | 450 | construída anunciada | n/d | triplex, terraço | 4.850.000 | 10.778 | 9.269 | 9.808 | 28/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7810eaef-b251-4404-a57c-fb28d465e929) | boa (a listagem dizia "Del Lago"; vale a página individual) |
| W2 | Artlife, CA2948 (2020) | 485 | construída anunciada | 485 | 3 pav. | 3.999.000 | 8.245 | 7.091 | 7.503 | 28/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-485m2/5e1e83bc-6979-496c-a913-2b1a88ae8610) | boa |
| W3 | Riviera Del Sol, CA0159 | 450 | construída anunciada | **600** | triplex, terraço | 4.800.000 | 10.667 | 9.174 | 9.707 | 02/06/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7a59356d-c5f1-4f0a-9fce-952f5c41fb76) | boa; o mais parecido em lote |
| W4 | condomínio não informado, CA2879 | 450 | construída anunciada | 275 | 3 níveis | 3.900.000 | 8.667 | 7.454 | 7.887 | 27/05/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/3f4cd0dd-1fbf-4af4-a6f6-f137107e5556) | média |
| W6 | Riviera Del Sol, VM 001867 | 500 | construída anunciada | 800 | n/i | 4.450.000 | 8.900 | 7.654 | 8.099 | **sem data** | [VM](https://consultoriaimobiliariavm.com.br/imovel/casa-a-venda-5-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-500m2-id-364) | fraca |
| W7 | Riviera Del Sol, VM 002243 | 469 | construída anunciada | 263 | triplex | 4.200.000 | 8.955 | 7.701 | 8.149 | **sem data** | [VM](https://consultoriaimobiliariavm.com.br/imovel/casa-de-condominio-a-venda-4-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-469m2-id-732) | média |

Resultado do controle S1/S2:
- **Faixa homogeneizada (n = 6): R$ 7.091 a R$ 9.808/m²** [EF]. Os extremos são W2 × 0,86 e W1 × 0,91.
- A mediana bruta, R$ 8.928, fica em R$ 7.678 a R$ 8.124 depois do fator.
- Sem W6 e W7, que não têm data, a faixa não muda.

**Fora da metragem: só tendência, não entram em conta**

| # | Imóvel | Área | Base | Preço | R$/m² bruto | × 0,86 a 0,91 | Publicado | Link |
|---|---|---|---|---|---|---|---|---|
| W5 | Parque das Palmeiras, CA0465, **2 pav.** | 400 | construída anunciada | 4.200.000 | 10.500 | 9.030 a 9.555 | 02/06/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-400m2/f4e2f578-514a-43c5-8375-c65a034f6114) |
| W8 | Del Lago, CA0121 | 570 | construída anunciada | 7.000.000 | 12.281 | 10.562 a 11.176 | 01/09/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-ou-aluguel-5-quartos-avenida-guilherme-de-almeida-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-570m2/bb5b5494-0b0d-49a2-b7c2-d112b5680511) |
| W9 | não informado | 392 | construída anunciada | 2.939.000 | 7.497 | 6.447 a 6.822 | 27/05/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-392m2/d7db5acb-d6d4-4204-9133-84a1e3aa02b5) |

**Faixa S3 (280 a 330 m²)**

| # | Imóvel | Área | Base | Preço | R$/m² bruto | × 0,86 | × 0,91 | Publicado | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|
| W10 | Riviera Del Sol, CA0291, alto padrão, triplex | 315 | construída anunciada | 4.250.000 | 13.492 | 11.603 | 12.278 | 05/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-315m2/8be15c9f-e2bf-4959-9e8d-e22685e5ec48) | boa |
| W11 | não informado, CA0467, triplex | 310 | construída anunciada | 2.100.000 | 6.774 | 5.826 | 6.164 | 03/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-310m2/7a22c151-ec29-4686-9a3b-65a53bbcb317) | fraca: padrão não declarado |
| W12 | Vivendas do Sol, 2 pav. (aparente); fora da faixa | 267 | construída anunciada | 3.000.000 | 11.236 | 9.663 | 10.225 | 01/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-267m2/01f107e3-ac64-420c-9dd1-7aed1a173b78) | referência |
| W13 | CA2932, triplex, alto padrão; fora da faixa | 370 | construída anunciada | 3.990.000 | 10.784 | 9.274 | 9.813 | 28/07/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-370m2/0aa2d877-00ad-48ed-92ea-b857288ff261) | referência |

**Limitação de tipo (mantida da v1):** quase todos os anúncios são triplex com terraço, em lote de 250 a 300 m². O Reserva das Garças proíbe terraço na cobertura e tem lotes de cerca de 600 m². Só W5 é de 2 pavimentos confirmado.

**Tentativas sem sucesso (nenhum número delas foi usado):**
- Loft: HTTP 410 nos anúncios individuais. Os números que apareceram só no resumo da busca foram descartados.
- ImóvelWeb: HTTP 403.
- CasaMineira: HTTP 403.
- Roberto Almeida Imóveis: 404.
- Barra e Vargens: a busca caiu em portais bloqueados.

### 2.3 Fonte do fator de oferta

- Raio-X FipeZAP do 2º trimestre de 2026, via reportagem do Portas de 18/08/2026: https://portas.com.br/noticias/desconto-medio-venda-imoveis-fipezap/ (acesso em 02/10/2026).
  - Desconto de 9% considerando todas as transações (fator 0,91).
  - Desconto de cerca de 14% considerando só as que tiveram desconto (fator 0,86).
- Referência anterior, 3º trimestre de 2025, desconto de cerca de 8%: InfoMoney, 14/11/2025, https://www.infomoney.com.br/?p=3103082 (acesso em 02/10/2026).
- **Ressalvas:**
  - O PDF primário não foi lido (o DataZAP deu 404).
  - O dado é nacional, sem recorte de casa em condomínio nem do Rio.
  - Na v1 eu recusei aplicar o fator. A v2 o aplica porque a Skill §3.3 o torna obrigatório, e a faixa 0,86 a 0,91 está declarada como referência nacional.

---

## 3. Faixa principal por cenário: vendas C1–C4 (R$ 13.000 a 15.000/m², base construída) × área CONSTRUÍDA de trabalho

### 3.1 Contas abertas (cada multiplicação foi conferida duas vezes)

| Cenário | Área (base) | × R$ 13.000 (C1, construída) | × R$ 15.000 (C4, construída) |
|---|---|---|---|
| S1 | 500,00 m² **construída [PV]** | 6.500.000 | 7.500.000 |
| S1 | 520,00 m² **construída [PV]** | 6.760.000 | 7.800.000 |
| **S1, faixa** | | **R$ 6.500.000 (piso)** | **R$ 7.800.000 (topo)** |
| S2 | 522,56 m² **construída [PV]** | 6.793.280 | 7.838.400 |
| S2 | 542,56 m² **construída [PV]** | 7.053.280 | 8.138.400 |
| **S2, faixa** | | **R$ 6.793.280** | **R$ 8.138.400** |
| S3 | 339,84 m² **construída [PV]** | 4.417.920 | 5.097.600 |
| S3 | 359,84 m² **construída [PV]** | 4.677.920 | 5.397.600 |
| **S3, faixa** (ordem de grandeza, seção 5) | | **R$ 4.417.920** | **R$ 5.397.600** |

Conferência pela diferença de área: o topo de S2 menos o topo de S1 é 22,56 × 15.000 = 338.400, e 7.800.000 + 338.400 = 8.138.400 ✓. O piso de S3 é o piso de S1 menos 160,16 × 13.000 = 2.082.080, e 6.500.000 − 2.082.080 = 4.417.920 ✓.

### 3.2 O que dava a v1 (base computável, ERRADA) e a diferença. Mostrado separado, não usar

| Cenário | v1: R$ 13.000 a 15.000 × **computável** | v2: × **construída** | Diferença no piso (42,56 × 13.000) | Diferença no topo (62,56 × 15.000) |
|---|---|---|---|---|
| S1 | 457,44 → 5.946.720 a 6.861.600 | 6.500.000 a 7.800.000 | +553.280 | +938.400 |
| S2 | 480,00 → 6.240.000 a 7.200.000 | 6.793.280 a 8.138.400 | +553.280 | +938.400 |
| S3 | 297,28 → 3.864.640 a 4.459.200 | 4.417.920 a 5.397.600 | +553.280 | +938.400 |

A diferença é a mesma nos três cenários porque a parcela não computável de trabalho [PV] é a mesma. A v1 subestimava; esse foi o erro de base.

### 3.3 Posição dentro da faixa e confiança
- **S1 e S2:** confiança média-baixa.
  - A favor: o tipo, o condomínio e a data batem. C2, depois do fator de oferta (12.900 a 13.650), fica dentro da faixa.
  - Contra: só 2 vendas; escrituras não conferidas; a base de área é premissa [PV]; e a distância até o mercado web é de 33% (seção 4).
  - **Não escolho um ponto dentro da faixa.** C4 (o lago) puxaria para o topo, mas a APP em aberto puxa para baixo (seção 5).
- **S2** só existe se a divisa com o Lote 16 for regularizada. O topo de S2 (R$ 8,14 mi) já passa o preço pedido de C2 sem fator (R$ 7,2 mi para 480 m²). Isso é sinal de que o topo de S2 é otimista.

---

## 4. Controle web (j'), com fator de oferta, sobre a área construída de trabalho

Faixa homogeneizada: S1/S2 de **R$ 7.091 a 9.808/m²** (n = 6) [EF]. Para S3, ver a seção 5.

| Cenário | Área (base) | × 7.091 | × 9.808 | Controle web [EF] |
|---|---|---|---|---|
| S1 | 500 / 520 **construída** | 500 × 7.091 = 3.545.500 | 520 × 9.808 = 5.100.160 | **R$ 3.545.500 a R$ 5.100.160** |
| S2 | 522,56 / 542,56 **construída** | 522,56 × 7.091 = 3.705.472,96 | 542,56 × 9.808 = 5.321.428,48 | **R$ 3.705.473 a R$ 5.321.428** |

(Contas intermediárias: 520 × 7.091 = 3.687.320; 500 × 9.808 = 4.904.000; 542,56 × 7.091 = 3.847.292,96; 522,56 × 9.808 = 5.125.268,48.)

**Distância entre a faixa do condomínio e o controle web depois do fator:**

| Comparação | Antes do fator (v1) | Depois do fator (v2) |
|---|---|---|
| Piso do condomínio (13.000) ÷ topo web | 13.000 / 10.778 = 1,206 (**+21%**) | 13.000 / 9.808 = 1,325 (**+33%**) |
| C2 ÷ topo web | 15.000 / 10.778 = 1,392 | 12.900 / 9.808 = 1,315 (a 13.650 / 9.808 = 1,392) |
| S1 com 520 m²: piso do condomínio − topo web | 6.760.000 − 5.604.560 = 1.155.440 | 6.760.000 − 5.100.160 = **1.659.840** |
| S1 com 500 m²: piso do condomínio − topo web | 6.500.000 − 5.389.000 = 1.111.000 | 6.500.000 − 4.904.000 = **1.596.000** |

(No "antes": 520 × 10.778 = 5.604.560 e 500 × 10.778 = 5.389.000.)

**Leitura:**
- O fator de oferta aumenta a distância, porque só os anúncios descem. As vendas C1 e C4 não recebem fator.
- Há duas hipóteses, que continuam sem separação possível:
  1. o Reserva das Garças tem um prêmio real (lote de 600 m², 2 pavimentos, lago);
  2. as escrituras C1 e C4 precisam ser conferidas.
- Para o laudo do banco (5.14), o risco é de cair perto do controle web, e não da faixa do condomínio.

---

## 5. S3 (lago / APP): ordem de grandeza em R$, sem [NC] puro

### 5.1 (i) Faixa do condomínio × construída S3
- Base: R$ 13.000 a 15.000/m² (construída) × 339,84 a 359,84 m² (construída [PV]) = **R$ 4.417.920 a R$ 5.397.600** [EF] (contas na seção 3.1).
- **Não há comparável real nessa metragem**, nem no condomínio nem nas vendas. É **interpolação declarada, com ressalva forte**.
- **Efeitos para cima:**
  - **Fator área (macete M5):** casa menor no mesmo lote tende a ter R$/m² maior. O lote pesa muito (pago a R$ 3,3 mi).
  - Não quantifico o expoente, porque o M5 é um estudo de apartamentos e só indica o sentido.
- **Efeitos para baixo:**
  1. **APP visível:** a faixa de fundo fica inutilizável e aparece na diligência de qualquer comprador e de qualquer banco.
  2. **Produto fora do padrão:** uma casa de cerca de 340 a 360 m² num condomínio de casas de 450 a 500 m².
  3. **C4 perde a âncora:** C4 foi vendida antes de a APP ser conhecida, e preço formado sem a restrição não serve para precificar depois dela. Sem C4, sobra só C1: 13.000 × 339,84 a 359,84 = **R$ 4.417.920 a R$ 4.677.920**.
- **Leitura:** os três efeitos para baixo vêm de fatos já identificados, e o para cima é só um sentido geral (M5). O risco é para baixo. O centro mais defensável é o piso da faixa (só C1), cerca de **R$ 4,4 a 4,7 mi**, e o topo de R$ 5,4 mi é otimista.

### 5.2 (ii) Controle web com fator de oferta, sobre a construída S3

| Amostra | R$/m² homogeneizado | × 339,84 | × 359,84 | Faixa [EF] |
|---|---|---|---|---|
| W10 (único na faixa com alto padrão declarado) | 11.603 a 12.278 | 339,84 × 11.603 = 3.943.163,52 | 359,84 × 12.278 = 4.418.115,52 | **R$ 3.943.164 a R$ 4.418.116** |
| W10 + W11 (W11 é fraco: padrão não declarado) | 5.826 a 12.278 | 339,84 × 5.826 = 1.979.907,84 | 359,84 × 12.278 = 4.418.115,52 | R$ 1.979.908 a R$ 4.418.116 (dispersão de 2 vezes, só referência) |
| W10 + W12 + W13 (alto padrão; W12 e W13 fora da metragem) | 9.274 a 12.278 | 339,84 × 9.274 = 3.151.676,16 | 4.418.115,52 | R$ 3.151.676 a R$ 4.418.116 (referência) |

O controle web de S3 fica entre R$ 3,2 e 4,4 mi, abaixo da faixa do condomínio, pelo mesmo motivo de S1/S2 (seção 4).

**Ordem de grandeza de S3 para o cliente:** cerca de **R$ 3,2 a 5,4 milhões**, mais provável na metade de baixo (R$ 4,4 a 4,7 mi pelo condomínio só com C1; R$ 3,9 a 4,4 mi pelo W10). Confiança baixa.

### 5.3 (iii) Peso do lago = revenda S1 − revenda S3, mesma base (construída)

- **Premissa:** o lago (APP de 30 m confirmada) reduz a área possível de S1 para S3. A diferença de área construída é 500 − 339,84 = **160,16 m²** (= 520 − 359,84), igual à diferença de área computável (457,44 − 297,28 = 160,16), porque a parcela não computável [PV] é a mesma.

| Variante | Conta | Peso do lago [EF] |
|---|---|---|
| **Central: mesmo R$/m² nos dois cenários** | 160,16 × 13.000 = 2.082.080; 160,16 × 15.000 = 2.402.400 | **R$ 2.082.080 a R$ 2.402.400** |
| Alta: S1 mantém C4 (sem APP), S3 perde C4 | 7.800.000 − 4.417.920 | R$ 3.382.080 |
| Baixa: S1 no piso, S3 no topo (fator área a favor de S3) | 6.500.000 − 5.397.600 | R$ 1.102.400 |
| Controle web, mesmo R$/m² homogeneizado | 160,16 × 7.091 = 1.135.694,56; 160,16 × 9.808 = 1.570.849,28 | R$ 1.135.695 a R$ 1.570.849 |

- **Faixa larga declarada: R$ 1,10 a 3,38 mi. Central: R$ 2,08 a 2,40 mi.** Bate com a ordem de grandeza de cerca de R$ 2 mi do parecer de Bardi.
- **Sentido do erro:** a conta central mede só a perda de área. Ela não inclui a desvalorização do próprio terreno pela APP, nem o desconto de produto fora do padrão (seção 5.1), que aumentam o peso. A tendência é de o peso real ser **maior** que o central.
- O peso é só de revenda. A economia de custo de obra em S3 é do Mascaró, e Villaça integra.

---

## 6. S2 − S1, refeito na base construída

- Diferença de área construída: 522,56 − 500,00 = 542,56 − 520,00 = **22,56 m²**. É igual à diferença de área computável (480,00 − 457,44), porque a parcela não computável [PV] é a mesma nos dois cenários.
- 22,56 × 13.000 = **293.280**; 22,56 × 15.000 = **338.400** [EF].
- Conferência por diferença das faixas: 6.793.280 − 6.500.000 = 293.280 ✓; 8.138.400 − 7.800.000 = 338.400 ✓.
- **O valor em R$ não muda em relação à v1.** O que muda é a base declarada. Usar o mesmo R$/m² é aceitável, porque a diferença de área é de cerca de 4%.

---

## 7. Efeito da garagem coberta na TO, em revenda

- **Mecanismo (Skill §4, item 5):** a vaga coberta não é computável, mas pode ocupar a projeção, e a TO é limitada pelo Regramento (Art. 5, 40%). Cada 10 m² de garagem coberta dentro da projeção tiram 10 m² de área computável do térreo.
- **A área construída total pode não mudar,** porque a garagem continua construída. O que cai é a **área de uso nobre** (sala, suíte, cozinha), trocada por garagem.
- **Por isso a conta "R$/m² × construída" não capta o efeito.** O R$/m² dos comparáveis já embute uma mistura de área nobre e garagem. Trocar área nobre por garagem reduz o valor da casa mesmo com a mesma área total.
- **Em R$, pela faixa do condomínio:** cada 10 m² de área nobre perdida = 10 × 13.000 a 15.000 = **R$ 130.000 a R$ 150.000** [EF].
  - Esse é o **teto** da perda. A perda líquida é esse valor menos o que o mercado paga pela garagem a mais, que é [NC], porque não há comparável que separe o R$/m² de garagem.
  - A perda é proporcional: 20 m² dão R$ 260 a 300 mil, e assim por diante.
- **Não informo a área da garagem.** O programa pede 4 carros, mas a área e a posição da vaga são de Lúcio. Quando ele desenhar, Villaça multiplica a área da vaga dentro da projeção por esses R$ 13.000 a 15.000/m².

---

## 8. Terreno e a pergunta de Helena (mantido da v1)

- Preço pago (5.11): R$ 3.300.000 [FP].
  - Sobre 600,00 m²: R$ 5.500/m².
  - Sobre 571,80 m²: R$ 5.771/m² [EF].
- Esse preço não é valor de mercado do terreno: é uma transação só e inclui benfeitorias. O valor de mercado do terreno fica **[NC]**.
- Controle: lote de 525 m² no Jardim de Maria, anúncio de R$ 1.770.000, ou R$ 3.371/m², publicado em 28/08/2026 ([Attria TE0307](https://www.attria.com.br/imovel/terreno-em-condominio-a-venda-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-525m2/d53ed614-6a87-42ee-833c-25d11dc09e26), acesso em 02/10/2026).
  - Sem fator de oferta, o preço pago fica 63% a 71% acima desse anúncio.
  - Com fator de oferta, o anúncio cai para R$ 2.899 a 3.068/m² (3.371 × 0,86 = 2.899,06; × 0,91 = 3.067,61). O preço pago fica então de 1,79 a 1,99 vez acima (5.500 / 3.068 = 1,79; 5.771 / 2.899 = 1,99) [EF].
- **Helena:** 28,20 m² × R$ 5.500 = **R$ 155.100** [EF].
  - É aritmética sobre o preço pago, e não perda de mercado.
  - O efeito real está no potencial construtivo: S2 − S1 = R$ 293.280 a R$ 338.400 de revenda (seção 6).

---

## 9. O que eu perguntaria num caso real (não contatei ninguém)

| A quem | O quê | Por quê |
|---|---|---|
| Marcelo (corretor) | Matrícula e escrituras de C1, C4 e C6; **se os "450/500/480 m² construídos" são área total, computável ou averbada**; padrão, idade e pavimentos de C1 e C4; há quanto tempo C2 está anunciado; área construída de C3 | A premissa de base (seção 0) e a distância de 33% até o mercado web dependem disso |
| Cartório de RI (certidão de inteiro teor) | Preço e área declarados nas escrituras de C1 e C4 | Conferência independente do corretor |
| Administradora / síndico | Vendas de 2025 e 2026; se algum lote de fundos para o lago já teve exigência de APP ou FMP | Aumentar a amostra; saber se o mercado já desconta a APP (C4) |
| Banco (via Villaça e Wallenberg) | Que comparáveis e que fator de oferta o laudo do banco usa | O limite de 60% (5.14) segue o laudo do banco |
| Lúcio (via Villaça) | Quadro de áreas por tipo, inclusive a área da garagem dentro da projeção | Substituir a premissa [PV] e fechar a seção 7 |

---

## 10. Ressalvas finais

- Nenhum número é promessa de valor de venda. São faixas, com a base de área declarada em cada linha.
- Não usei média de bairro. Filtrei por tipo (casa em condomínio), padrão (alto) e metragem. Todos os comparáveis são do Recreio; não foi preciso ampliar o raio.
- **Qualidade desigual:** as 2 vendas do dossiê valem mais que os anúncios para dizer o valor neste condomínio. Os anúncios mostram que esse valor está acima do resto do Recreio. W6 e W7 (sem data) e W11 (padrão não declarado) são os dados mais fracos.
- A Skill e o fator de oferta trazem as ressalvas R1 e R2. As áreas construídas são premissa de Villaça [PV], não desenho.
- Legal, custo de obra e OODC estão fora do meu escopo.

*Declaração: ENSAIO 003, caso 100% fictício. Os dados do dossiê (5.11 a 5.15) foram tratados como reais dentro do ensaio. Os dados de mercado da web são reais, com link e acesso em 02/10/2026. Ninguém foi contatado. A pasta `_gabaritos_LACRADO/` não foi aberta.*
