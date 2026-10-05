# Ensaio 003, Etapa 02: Valor de revenda, v5 (Fiker)

**Para:** Villaça (Gestor de Viabilidade). A integração e a auditoria são dele.
**De:** Fiker (Agente de Valor de Mercado / Comparáveis)
**Data de referência:** 02/10/2026. Pesquisa web e acessos em 02/10/2026. Na varredura da v5 (05/10/2026), reli as mesmas páginas só para conferir texto e rótulo: nenhuma fonte nova, nenhum número novo.
**Versão:** v5 (05/10/2026). Base: cópia integral da v4 (`../v5/revenda_fiker_003_v4.md`, com cópia em `../v4/`, as duas mantidas intactas). A v4 copiou a v2 (`../v3/revenda_fiker_003_v2.md`, mantida intacta), que corrigiu a v1 (`../revenda_fiker_003.md`, mantida intacta). A v1 foi reprovada por Claudemberg por três motivos: (1) aplicou R$/m² de área construída sobre a área computável; (2) não aplicou fator de oferta aos anúncios; (3) deixou S3 sem ordem de grandeza em R$.
**Skill aplicada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj`, §3 (base de área igual, fator de oferta, fator área, restrição nova, ordem de grandeza) e §4, item 5. A v4 foi feita com a v1.2. A v5 foi conferida contra a §3 e o §4, item 5, lidos na v1.3 em 05/10/2026; a v1.4, gravada por Villaça no mesmo dia, só muda a §2.4 (custo), e essas partes são iguais na v1.3 e na v1.4 (e, pelo changelog, desde a v1.0). Nenhuma regra de revenda mudou. A Skill tem ressalva de fonte: a NBR 14653-2 não foi lida no texto oficial (R1), e o fator de oferta foi calibrado com dado nacional (R2).

## O que muda em relação à v4

**Nenhum número muda.** Só rótulo e texto.

1. **Rótulo [PL].** As áreas computáveis 457,44 / 480,00 / 297,28 m² e as conclusões do Legal (hipótese H1 da APP de 30 m; "os 590 m² não cabem"; S2 depende de regularizar a divisa com o Lote 16; vaga coberta fora da área computável) passam a levar [PL], com a legenda nova. Na v4, o título da §0 levava [PV] e cobria a tabela inteira, inclusive a coluna do Legal: a mesma área ficava com dois rótulos na mesma entrega. Agora o título da §0 não tem rótulo; a coluna do Legal leva [PL]; a construída de trabalho e a faixa não computável levam [PV].
2. **Varredura do arquivo inteiro** (rótulos, "literal", datas). Achei e corrigi mais estes pontos, todos de texto:
   - a. **C5:** "[enquadramento meu]" não é rótulo da legenda. Virou [INF].
   - b. **Base de área dos anúncios da Attria.** A v4 dizia "construída anunciada". A Attria mostra só o campo "Área", sem dizer a base. Agora: área do anúncio ("Área"); tratá-la como construída é [INF]. Nos da VM (W6, W7), a página diz "área construída", e isso se mantém.
   - c. **Coluna "Terreno" (W1 a W7).** A v4 tratava como terreno o campo "Área total" dos anúncios. Só W2 ("Terreno com 485m2") e W7 (263 m², no texto) dizem que é terreno. W3 (600), W4 (275) e W6 (800) dizem só "Área total". W1 mostra "Área total" de 450, igual à área, e estava "n/d". A coluna agora diz o que cada anúncio diz.
   - d. **W3, "o mais parecido em lote com o Lote 17".** Isso dependia de "Área total" = terreno. Agora está marcado como [INF].
   - e. **W6, "Riviera Del Sol".** Na releitura de 05/10/2026, a página da VM não nomeia o condomínio; dá só o endereço (Vereador Alceu de Carvalho, 665). O nome virou [INF], tirado do endereço.
   - f. **Limitação de tipo (§2.2) e leitura da §4.** A v4 dizia "quase todos os anúncios são triplex com terraço, em lote de 250 a 300 m²" e "lotes maiores que os dos anúncios". Isso contradizia a própria tabela: terraço só está declarado em W1 e W3; e, dos anúncios com "Área total" ou terreno informado, dois (W3 com 600 e W6 com 800) não são menores que o Lote 17. Reescrito pela tabela.
   - g. **"Únicas metragens informadas no condomínio" (§5.1 e item 8 do histórico da v2).** C3 (1.200 m²) e C6 (420 m²) também têm área informada, só que sem base declarada. Agora: "metragens informadas como construídas".
   - h. **Título da §3, "vendas C1–C4".** Lia-se como C1 a C4, o que incluiria C2 (anúncio) e C3 (rejeitado). Agora: "vendas C1 e C4".
   - i. **§10, "filtrei por padrão (alto)".** Contradizia "W11 (padrão não declarado)". Agora: o alvo foi o alto padrão, mas nem todo anúncio o declara.
   - j. **Faixas de busca da §2.2.** As faixas 430 a 520 m² e 280 a 330 m² vêm da v1, que trabalhava sobre a área computável. Não tinham sido refeitas para a construída de trabalho, e isso não estava declarado. Agora está, na §2.2. Reajustar mudaria o controle web; fica para Villaça decidir, e aqui nenhum número muda.
   - k. **§1, achado 2, "maior anúncio web".** W8 (fora da metragem) tem R$/m² maior que W1. Agora: "maior anúncio web da faixa S1/S2 (W1)".
3. **Conferido sem mudança:** datas de C1 a C6 (5.13); RIU de 22/09/2026 (5.3); reportagem do Portas de 18/08/2026 e InfoMoney de 14/11/2025; datas de publicação de W1 a W5 e W8 a W13 e do TE0307 (iguais nas páginas em 05/10/2026); W6 e W7 sem data; todas as citações do Dossiê entre aspas; preços dos anúncios; "cerca de R$ 2 mi" do `parecer_bardi.md`.

## O que muda em relação à v2 (histórico da v4)

Só texto. **Nenhum número de revenda muda.** Toda citação do Dossiê (5.1 a 5.15) e do caso base foi conferida contra o texto literal de `enunciado.md` e `caso_sombra_003.md`.

1. **C3 (5.13).** A planilha diz só "1.200 m²", sem declarar a base. A v2 afirmava que era área de terreno. Agora: base não declarada pelo corretor; **provavelmente terreno (1.200 = 2 × 600, lotes unificados), por inferência minha**. A rejeição se mantém pelos dois lados: se for terreno, não se compara com R$/m² construído; se for construída, 1.200 m² em lote duplo está muito fora da metragem.
2. **Tamanho dos lotes do condomínio.** A v2 dizia que o Reserva das Garças "tem lotes de cerca de 600 m²". O Dossiê não informa isso. Ele informa só o Lote 17: 600,00 m² na matrícula (5.1) e 571,80 m² medidos (5.2). Corrigido na §2.2 e na §4.
3. **Art. 7º do Regramento (5.4).** A v2 resumia como "proíbe terraço na cobertura". O texto literal é: "Vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje de cobertura". Corrigido na §2.2 e na linha de C5.
4. **Rodapé do corretor (5.13).** As frases entre aspas não eram literais ("R$ 7,67 mi para 590 m²", "R$ 8,8 mi com rooftop"). Substituídas pelo texto literal. A conta 13.000 × 590 é reconstrução minha; o corretor não a escreve.
5. **"m² construídos" de C1, C2 e C4.** A planilha diz "450 m² construídos" (e 480, 500). Ela não diz "total". A v2 dizia "construída total, informada pelo corretor". Agora: "construídos" é do corretor; "total" é a premissa [PV].
6. **APP.** A v2 dizia "APP de 30 m confirmada" na §5.3. A APP não está confirmada: é a hipótese H1 do parecer do Legal (Etapa 01). Agora: "se a APP de 30 m for confirmada (H1)".
7. **C4 "vendida antes da questão da APP".** O Dossiê não diz isso. Ele diz só que C4 foi vendida em 06/2026, e o RIU (5.3, 22/09/2026) traz a observação sobre APP. Agora está marcado como inferência minha.
8. **"Condomínio de casas de 450 a 500 m²"** (§5.1). O Dossiê não descreve as casas do condomínio. Só C1, C2 e C4 têm área informada como construída (450 a 500 m²); C3 e C6 têm área sem base declarada. Corrigido. (Texto deste item ajustado na v5.)
9. **§9:** a citação composta "450/500/480 m² construídos" virou texto sem aspas, e "área construída de C3" virou "base dos 1.200 m² de C3".

**Rótulos:**
- **[FP]** fonte primária: documento do dossiê ou anúncio aberto individualmente.
- **[EF]** estimativa com fonte: conta minha sobre números [FP].
- **[PL]** premissa recebida do Legal: número ou conclusão do parecer da Etapa 01 (Hely/Kelsen, aprovado por Claudemberg em 01/10/2026). Está literal no parecer, mas é cálculo/leitura do Legal, não texto do Dossiê nem da lei.
- **[PV]** premissa fixada por Villaça.
- **[NC]** não calculável.
- **[INF]** inferência minha, que o documento não diz.

---

## 0. Premissas de área (porque Lúcio ainda não desenhou)

| Cenário | Área computável [PL] (Legal, Etapa 01) | Área construída de trabalho [PV] (base da revenda) | Diferença construída − computável [PV] |
|---|---|---|---|
| S1 / H0 | 457,44 m² | 500,00 a 520,00 m² | 42,56 a 62,56 m² |
| S2 | 480,00 m² | 522,56 a 542,56 m² | 42,56 a 62,56 m² |
| S3 / H1 | 297,28 m² | 339,84 a 359,84 m² | 42,56 a 62,56 m² |

- A faixa não computável (42,56 a 62,56 m²) é a mesma nos três cenários: varanda, garagem, área técnica etc. É premissa de Villaça, não é desenho.
- **Premissa de base dos comparáveis:**
  - A planilha diz "450 m² construídos", "480 m² construídos" e "500 m² construídos" (C1, C2, C4). Que sejam **área construída total** é premissa [PV]; o corretor não diz "total".
  - Em W1 a W13, a área usada é a **área do anúncio**. Nos anúncios da Attria, o campo se chama só "Área", sem base declarada; tratá-la como área construída é [INF]. Nos da VM (W6, W7), a página diz "área construída".
- **Sentido do erro se a premissa falhar:**
  - **C1, C2 e C4.** Se os 450, 480 e 500 m² forem, na verdade, área computável (ou averbada sem varanda e garagem), o R$/m² real sobre a construída total seria menor. Nesse caso, a v5 **superestima** o valor, e a conta certa voltaria a ser a da v1: R$/m² × computável [PL]. O tamanho do erro é exatamente a diferença da seção 3.2, de R$ 553.280 a R$ 938.400 por cenário.
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
   - Sem fator, o piso do condomínio (R$ 13.000/m²) ficava cerca de 21% acima do maior anúncio web da faixa S1/S2 (W1). Com o fator, fica 33% acima (13.000 / 9.808 = 1,325).
   - Na comparação em reais, para S1 com 520 m²: o piso do condomínio é R$ 6.760.000 e o topo do controle web é R$ 5.100.160. A distância é de R$ 1.659.840.
   - Por isso, as escrituras C1 e C4 precisam ser conferidas antes de qualquer uso diante do banco.
3. **C2 homogeneizado fica dentro da faixa das vendas.** Com o fator de oferta: 15.000 × 0,86 a 0,91 = R$ 12.900 a R$ 13.650/m². Isso confirma C2 como dado coerente com C1 e C4, e não só como teto.
4. **O lago pesa cerca de R$ 2,1 a 2,4 milhões na revenda** (de S1 para S3, mesmo R$/m², mesma base), se a APP for confirmada (hipótese H1 do Legal [PL]). A faixa larga vai de R$ 1,1 a 3,4 milhões, com as premissas na seção 5.3. O sentido provável do erro é o de o peso ser maior, porque a APP também desvaloriza o terreno.

---

## 2. Comparáveis, com a base de área em cada linha

### 2.1 Planilha do corretor (5.13), tratamento linha a linha (mantido da v1, com base e fator acrescentados)

| Ref | Situação / data | Área informada | **Base de área** | Preço | R$/m² bruto | Fator de oferta | R$/m² homogeneizado | Decisão |
|---|---|---|---|---|---|---|---|---|
| C1 | vendida (escritura) 03/2026, Lote 04 Qd A, 2 pav., frente para rua interna | "450 m² construídos" | **construídos (corretor); total = [PV]** | R$ 5.850.000 | 13.000 (5.850.000 / 450) [FP] | **nenhum** (venda) | **13.000** | **ACEITA**: núcleo e piso; não tem o efeito do lago |
| C2 | anúncio 09/2026, Lote 11 Qd B, 2 pav. | "480 m² construídos" | **construídos (corretor); total = [PV]** | R$ 7.200.000 | 15.000 (7.200.000 / 480) [FP, anúncio] | 0,86 a 0,91 | **12.900 a 13.650** [EF] | **ACEITA COM AJUSTE**: entra homogeneizada como confirmação; fica fora da faixa principal, que usa só vendas |
| C3 | anúncio 08/2026, Lotes 22 + 23 Qd C (unificados) | "1.200 m²" | **não declarada pelo corretor**; provavelmente terreno (1.200 = 2 × 600, lotes unificados) [INF] | R$ 9.600.000 | 8.000 sobre base não declarada; provável R$/m² de terreno [INF] | não se aplica | não se aplica | **REJEITA pelos dois lados**: se for terreno, não se compara com R$/m² construído; se for construída, 1.200 m² em lote duplo está muito fora da metragem |
| C4 | vendida (escritura) 06/2026, Lote 09 Qd C, fundos para o lago | "500 m² construídos" | **construídos (corretor); total = [PV]** | R$ 7.500.000 | 15.000 (7.500.000 / 500) [FP] | **nenhum** (venda) | **15.000** | **ACEITA COM RESSALVA**: pavimentos não informados; venda de 06/2026, provavelmente sem a APP no preço [INF] (seção 5) |
| C5 | anúncio 09/2026, Condomínio Jardim dos Socós (vizinho, fictício), 2 pav. + subsolo + rooftop com piscina | "680 m² construídos" | construídos (como informado) | R$ 11.560.000 | 17.000 | não aplicado | não se aplica | **REJEITA**: subsolo é vedado pelo Art. 8º; rooftop com piscina se enquadra em "área de lazer sobre a laje de cobertura", vedada pelo Art. 7º [INF]; fora da metragem; outro condomínio |
| C6 | vendida (escritura) 11/2021, Lote 31 Qd B | "420 m²" | **não declarada** (construída ou terreno) | R$ 3.780.000 | 9.000 | não se aplica | não se aplica | **REJEITA**: quase 5 anos; não há índice de casa (o FipeZAP mede apartamento); base de área desconhecida |

**Média do corretor (R$ 12.833/m²):** a conta está certa, (13.000 + 15.000 + 8.000 + 15.000 + 17.000 + 9.000) / 6 = 12.833. **O método é inválido**:
- mistura 3 vendas e 3 anúncios, sem fator de oferta;
- mistura um provável R$/m² de terreno (C3, base não declarada) com R$/m² construído;
- inclui um condomínio com atributos vedados aqui (C5);
- inclui um dado de 2021 (C6).

A coincidência com C1 é acaso: os erros para baixo (C3, C6) compensam o erro para cima (C5).

**Números do rodapé, recusados (mantido da v1):**
- Texto literal: "Terreno de 600 m², projeto do arquiteto anterior com 590 m²: a casa pronta vale **R$ 7,67 milhões**". A conta que reproduz o número é 13.000 × 590 = 7.670.000 (reconstrução minha; o corretor não a escreve). Os 590 m² vêm do estudo de massa de 2024 (5.6), que o parecer do Legal da Etapa 01 recusou ("os 590 m² não cabem") [PL]. **Não usar.** Na base certa, o número comparável é o de S1 na construída: R$ 6,50 a 7,80 mi. O topo coincide com a ordem de grandeza do corretor só porque usa R$ 15.000 sobre 520 m², e não pelo método dele.
- Texto literal: "com o rooftop pela Mais-Valerá, **R$ 8,8 milhões**". Atribui cerca de R$ 1,13 mi (8,8 − 7,67) a um rooftop que o Art. 7º veda ("Vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje de cobertura"). Não tem comparável. **Não usar.**
- Outorga: "simulei no Lote 5 do Jardim dos Socós, aqui do lado, que tem CAM 1,5 — deu R$ 380 mil para 300 m² a mais". Não muda a revenda, porque aqui o CAM é 1,0 (RIU 5.3: "a subzona não prevê outorga onerosa acima do CAB") e não há área adicional. O custo da OODC é com Villaça.

### 2.2 Anúncios web. Todos foram abertos individualmente em 02/10/2026; todos são anúncio; todos estão no Recreio dos Bandeirantes

Fator de oferta 0,86 a 0,91 (Skill §3.3, macete M6; referência nacional, não local). As contas de R$/m² foram conferidas duas vezes. Os valores estão arredondados ao real.

**Base de área dos anúncios:** na Attria, o campo se chama só "Área" (base não declarada); tratá-lo como construída é [INF]. Na VM (W6, W7), a página diz "área construída". A coluna "Lote / Área total" repete o que cada anúncio diz; "Área total" sem a palavra terreno não prova que seja o lote.

**Faixas de busca (declaração da v5):** as faixas 430 a 520 m² (S1/S2) e 280 a 330 m² (S3) vêm da v1, que trabalhava sobre a área computável (457,44, 480,00 e 297,28 m² [PL]). Elas não foram refeitas para a construída de trabalho [PV] (500,00 a 542,56 m² e 339,84 a 359,84 m²). Por isso W8 (570 m²) e W13 (370 m²) ficaram fora, embora estejam mais perto da construída de trabalho que parte dos incluídos. Reajustar as faixas mudaria o controle web; a decisão é de Villaça. Nesta versão, nenhum número muda.

**Faixa S1/S2 (430 a 520 m²): entram no controle**

| # | Imóvel | Área | **Base de área** | Lote / Área total (como o anúncio diz) | Pav. | Preço pedido | R$/m² bruto | × 0,86 | × 0,91 | Publicado | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | Bothanica Nature, CA2947 | 450 | "Área" (Attria); construída [INF] | lote n/d ("Área total" 450, igual à área) | triplex, terraço | 4.850.000 | 10.778 | 9.269 | 9.808 | 28/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7810eaef-b251-4404-a57c-fb28d465e929) | boa (a listagem dizia "Del Lago"; vale a página individual) |
| W2 | Artlife, CA2948 (2020) | 485 | "Área" (Attria); construída [INF] | 485 ("Terreno com 485m2") | 3 pav. | 3.999.000 | 8.245 | 7.091 | 7.503 | 28/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-485m2/5e1e83bc-6979-496c-a913-2b1a88ae8610) | boa |
| W3 | Riviera Del Sol, CA0159 | 450 | "Área" (Attria); construída [INF] | "Área total" 600 (não diz terreno) | triplex, terraço | 4.800.000 | 10.667 | 9.174 | 9.707 | 02/06/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-5-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/7a59356d-c5f1-4f0a-9fce-952f5c41fb76) | boa; se a "Área total" de 600 for o lote [INF], é o mais parecido em lote com o Lote 17 (600,00 m² na matrícula) |
| W4 | condomínio não informado, CA2879 | 450 | "Área" (Attria); construída [INF] | "Área total" 275 (não diz terreno) | 3 níveis | 3.900.000 | 8.667 | 7.454 | 7.887 | 27/05/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-450m2/3f4cd0dd-1fbf-4af4-a6f6-f137107e5556) | média |
| W6 | condomínio não nomeado na página (Vereador Alceu de Carvalho, 665); Riviera Del Sol pelo endereço [INF], VM 001867 | 500 | construída anunciada ("área construída", VM) | "área total" 800 (não diz terreno) | n/i | 4.450.000 | 8.900 | 7.654 | 8.099 | **sem data** | [VM](https://consultoriaimobiliariavm.com.br/imovel/casa-a-venda-5-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-500m2-id-364) | fraca |
| W7 | Riviera Del Sol, VM 002243 | 469 | construída anunciada ("área construída", VM) | 263 (terreno, no texto do anúncio) | triplex | 4.200.000 | 8.955 | 7.701 | 8.149 | **sem data** | [VM](https://consultoriaimobiliariavm.com.br/imovel/casa-de-condominio-a-venda-4-quartos-recreio-dos-bandeirantes-rio-de-janeiro-rj-469m2-id-732) | média |

Resultado do controle S1/S2:
- **Faixa homogeneizada (n = 6): R$ 7.091 a R$ 9.808/m²** [EF]. Os extremos são W2 × 0,86 e W1 × 0,91.
- A mediana bruta, R$ 8.928, fica em R$ 7.678 a R$ 8.124 depois do fator.
- Sem W6 e W7, que não têm data, a faixa não muda.

**Fora da metragem: só tendência, não entram em conta**

| # | Imóvel | Área | Base | Preço | R$/m² bruto | × 0,86 a 0,91 | Publicado | Link |
|---|---|---|---|---|---|---|---|---|
| W5 | Parque das Palmeiras, CA0465, **2 pav.** | 400 | "Área" (Attria); construída [INF] | 4.200.000 | 10.500 | 9.030 a 9.555 | 02/06/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-400m2/f4e2f578-514a-43c5-8375-c65a034f6114) |
| W8 | Del Lago, CA0121 | 570 | "Área" (Attria); construída [INF] | 7.000.000 | 12.281 | 10.562 a 11.176 | 01/09/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-ou-aluguel-5-quartos-avenida-guilherme-de-almeida-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-570m2/bb5b5494-0b0d-49a2-b7c2-d112b5680511) |
| W9 | não informado | 392 | "Área" (Attria); construída [INF] | 2.939.000 | 7.497 | 6.447 a 6.822 | 27/05/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-392m2/d7db5acb-d6d4-4204-9133-84a1e3aa02b5) |

**Faixa S3 (280 a 330 m²)**

| # | Imóvel | Área | Base | Preço | R$/m² bruto | × 0,86 | × 0,91 | Publicado | Link | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|
| W10 | Riviera Del Sol, CA0291, alto padrão, triplex | 315 | "Área" (Attria); construída [INF] | 4.250.000 | 13.492 | 11.603 | 12.278 | 05/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-estrada-vereador-alceu-de-carvalho-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-315m2/8be15c9f-e2bf-4959-9e8d-e22685e5ec48) | boa |
| W11 | não informado, CA0467, triplex | 310 | "Área" (Attria); construída [INF] | 2.100.000 | 6.774 | 5.826 | 6.164 | 03/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-310m2/7a22c151-ec29-4686-9a3b-65a53bbcb317) | fraca: padrão não declarado |
| W12 | Vivendas do Sol, 2 pav. (aparente); fora da faixa | 267 | "Área" (Attria); construída [INF] | 3.000.000 | 11.236 | 9.663 | 10.225 | 01/08/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-267m2/01f107e3-ac64-420c-9dd1-7aed1a173b78) | referência |
| W13 | CA2932, triplex, alto padrão; fora da faixa | 370 | "Área" (Attria); construída [INF] | 3.990.000 | 10.784 | 9.274 | 9.813 | 28/07/2026 | [Attria](https://www.attria.com.br/imovel/casa-em-condominio-a-venda-4-quartos-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-com-garagem-370m2/0aa2d877-00ad-48ed-92ea-b857288ff261) | referência |

**Limitação de tipo (mantida da v1, texto corrigido na v4 e na v5):** a maioria dos anúncios é triplex ou de 3 pavimentos (W1, W2, W3, W4, W7, W10, W11, W13); terraço está declarado em W1 e W3. No Reserva das Garças, o Art. 7º do Regramento (5.4) diz: "Vedado pavimento de cobertura, terraço habitável ou área de lazer sobre a laje de cobertura"; e o gabarito é de 2 pavimentos. Onde o anúncio informa lote ou "Área total", o número vai de 263 a 800 m² (W7 263; W4 275; W2 485; W3 600; W6 800); só W2 e W7 dizem que é terreno. O Dossiê não informa o tamanho dos lotes do condomínio; informa só o do Lote 17: 600,00 m² na matrícula (5.1) e 571,80 m² medidos (5.2). Que os outros lotes sejam parecidos é inferência minha [INF]. Só W5 é de 2 pavimentos confirmado.

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
  - Na v1 eu recusei aplicar o fator. A partir da v2 ele é aplicado, porque a Skill §3.3 o torna obrigatório, e a faixa 0,86 a 0,91 está declarada como referência nacional.

---

## 3. Faixa principal por cenário: vendas C1 e C4 (R$ 13.000 a 15.000/m², base construída) × área CONSTRUÍDA de trabalho

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

| Cenário | v1: R$ 13.000 a 15.000 × **computável [PL]** | v2/v4/v5: × **construída [PV]** | Diferença no piso (42,56 × 13.000) | Diferença no topo (62,56 × 15.000) |
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
- **S2** só existe se a divisa com o Lote 16 for regularizada [PL] (5.2: "Muro da divisa lateral esquerda do vizinho (Lote 16) avança sobre a linha de projeto do PAL"). O topo de S2 (R$ 8,14 mi) já passa o preço pedido de C2 sem fator (R$ 7,2 mi para 480 m²). Isso é sinal de que o topo de S2 é otimista.

---

## 4. Controle web (j'), com fator de oferta, sobre a área construída de trabalho

Faixa homogeneizada: S1/S2 de **R$ 7.091 a 9.808/m²** (n = 6) [EF]. Para S3, ver a seção 5.

| Cenário | Área (base) | × 7.091 | × 9.808 | Controle web [EF] |
|---|---|---|---|---|
| S1 | 500 / 520 **construída** | 500 × 7.091 = 3.545.500 | 520 × 9.808 = 5.100.160 | **R$ 3.545.500 a R$ 5.100.160** |
| S2 | 522,56 / 542,56 **construída** | 522,56 × 7.091 = 3.705.472,96 | 542,56 × 9.808 = 5.321.428,48 | **R$ 3.705.473 a R$ 5.321.428** |

(Contas intermediárias: 520 × 7.091 = 3.687.320; 500 × 9.808 = 4.904.000; 542,56 × 7.091 = 3.847.292,96; 522,56 × 9.808 = 5.125.268,48.)

**Distância entre a faixa do condomínio e o controle web depois do fator:**

| Comparação | Antes do fator (v1) | Depois do fator (v2/v4/v5) |
|---|---|---|
| Piso do condomínio (13.000) ÷ topo web | 13.000 / 10.778 = 1,206 (**+21%**) | 13.000 / 9.808 = 1,325 (**+33%**) |
| C2 ÷ topo web | 15.000 / 10.778 = 1,392 | 12.900 / 9.808 = 1,315 (a 13.650 / 9.808 = 1,392) |
| S1 com 520 m²: piso do condomínio − topo web | 6.760.000 − 5.604.560 = 1.155.440 | 6.760.000 − 5.100.160 = **1.659.840** |
| S1 com 500 m²: piso do condomínio − topo web | 6.500.000 − 5.389.000 = 1.111.000 | 6.500.000 − 4.904.000 = **1.596.000** |

(No "antes": 520 × 10.778 = 5.604.560 e 500 × 10.778 = 5.389.000.)

**Leitura:**
- O fator de oferta aumenta a distância, porque só os anúncios descem. As vendas C1 e C4 não recebem fator.
- Há duas hipóteses, que continuam sem separação possível:
  1. o Reserva das Garças tem um prêmio real: 2 pavimentos sem terraço (Art. 7º), o lago (5.5) e, possivelmente, lotes maiores que os da maioria dos anúncios. Só o Lote 17 tem área conhecida (600,00 m² na matrícula); que os outros lotes sejam parecidos é [INF]. Entre os anúncios com lote ou "Área total" informado, W3 (600) e W6 (800) não são menores que o Lote 17 (§2.2);
  2. as escrituras C1 e C4 precisam ser conferidas.
- Para o laudo do banco (5.14: "laudo de avaliação do próprio banco"), o risco é de cair perto do controle web, e não da faixa do condomínio.

---

## 5. S3 (lago / APP): ordem de grandeza em R$, sem [NC] puro

### 5.1 (i) Faixa do condomínio × construída S3
- Base: R$ 13.000 a 15.000/m² (construída) × 339,84 a 359,84 m² (construída [PV]) = **R$ 4.417.920 a R$ 5.397.600** [EF] (contas na seção 3.1).
- **Não há comparável real nessa metragem**, nem no condomínio nem nas vendas. É **interpolação declarada, com ressalva forte**.
- **Efeitos para cima:**
  - **Fator área (macete M5):** casa menor no mesmo lote tende a ter R$/m² maior. O lote pesa muito (pago a R$ 3,3 mi, 5.11).
  - Não quantifico o expoente, porque o M5 é um estudo de apartamentos e só indica o sentido.
- **Efeitos para baixo:**
  1. **APP visível, se confirmada (hipótese H1 do Legal [PL]):** a faixa de fundo fica inutilizável e aparece na diligência de qualquer comprador e de qualquer banco.
  2. **Produto fora do padrão:** uma casa de cerca de 340 a 360 m², abaixo das metragens informadas como construídas no condomínio (C1, C2 e C4: 450 a 500 m² construídos; C3 e C6 têm área sem base declarada). O Dossiê não descreve as demais casas.
  3. **C4 perde a âncora:** C4 foi vendida em 06/2026, antes do RIU de 22/09/2026 que traz a observação "verificar APP". Que o preço tenha sido formado sem a restrição é inferência minha [INF]; se for assim, não serve para precificar depois dela. Sem C4, sobra só C1: 13.000 × 339,84 a 359,84 = **R$ 4.417.920 a R$ 4.677.920**.
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

- **Premissa:** se a APP de 30 m for confirmada (hipótese H1 do parecer do Legal, Etapa 01 [PL]), o lago reduz a área possível de S1 para S3. A diferença de área construída [PV] é 500 − 339,84 = **160,16 m²** (= 520 − 359,84), igual à diferença de área computável [PL] (457,44 − 297,28 = 160,16), porque a parcela não computável [PV] é a mesma.

| Variante | Conta | Peso do lago [EF] |
|---|---|---|
| **Central: mesmo R$/m² nos dois cenários** | 160,16 × 13.000 = 2.082.080; 160,16 × 15.000 = 2.402.400 | **R$ 2.082.080 a R$ 2.402.400** |
| Alta: S1 mantém C4 (sem APP), S3 perde C4 | 7.800.000 − 4.417.920 | R$ 3.382.080 |
| Baixa: S1 no piso, S3 no topo (fator área a favor de S3) | 6.500.000 − 5.397.600 | R$ 1.102.400 |
| Controle web, mesmo R$/m² homogeneizado | 160,16 × 7.091 = 1.135.694,56; 160,16 × 9.808 = 1.570.849,28 | R$ 1.135.695 a R$ 1.570.849 |

- **Faixa larga declarada: R$ 1,10 a 3,38 mi. Central: R$ 2,08 a 2,40 mi.** Bate com a ordem de grandeza "cerca de R$ 2 mi" do primeiro parecer de Bardi (`parecer_bardi.md`).
- **Sentido do erro:** a conta central mede só a perda de área. Ela não inclui a desvalorização do próprio terreno pela APP, nem o desconto de produto fora do padrão (seção 5.1), que aumentam o peso. A tendência é de o peso real ser **maior** que o central.
- O peso é só de revenda. A economia de custo de obra em S3 é do Mascaró, e Villaça integra.

---

## 6. S2 − S1, refeito na base construída

- Diferença de área construída [PV]: 522,56 − 500,00 = 542,56 − 520,00 = **22,56 m²**. É igual à diferença de área computável [PL] (480,00 − 457,44), porque a parcela não computável [PV] é a mesma nos dois cenários.
- 22,56 × 13.000 = **293.280**; 22,56 × 15.000 = **338.400** [EF].
- Conferência por diferença das faixas: 6.793.280 − 6.500.000 = 293.280 ✓; 8.138.400 − 7.800.000 = 338.400 ✓.
- **O valor em R$ não muda em relação à v1.** O que muda é a base declarada. Usar o mesmo R$/m² é aceitável, porque a diferença de área é de cerca de 4%.

---

## 7. Efeito da garagem coberta na TO, em revenda

- **Mecanismo (Skill §4, item 5):** a vaga coberta não é computável [PL], mas pode ocupar a projeção, e a TO é limitada pelo Regramento (Art. 5º: "Taxa de ocupação máxima: 40% da área do lote"). Cada 10 m² de garagem coberta dentro da projeção tiram 10 m² de área computável do térreo.
- **A área construída total pode não mudar,** porque a garagem continua construída. O que cai é a **área de uso nobre** (sala, suíte, cozinha), trocada por garagem.
- **Por isso a conta "R$/m² × construída" não capta o efeito.** O R$/m² dos comparáveis já embute uma mistura de área nobre e garagem. Trocar área nobre por garagem reduz o valor da casa mesmo com a mesma área total.
- **Em R$, pela faixa do condomínio:** cada 10 m² de área nobre perdida = 10 × 13.000 a 15.000 = **R$ 130.000 a R$ 150.000** [EF].
  - Esse é o **teto** da perda. A perda líquida é esse valor menos o que o mercado paga pela garagem a mais, que é [NC], porque não há comparável que separe o R$/m² de garagem.
  - A perda é proporcional: 20 m² dão R$ 260 a 300 mil, e assim por diante.
- **Não informo a área da garagem.** O programa (caso base, §4) pede "Garagem para 4 carros", mas a área e a posição da vaga são de Lúcio. Quando ele desenhar, Villaça multiplica a área da vaga dentro da projeção por esses R$ 13.000 a 15.000/m².

---

## 8. Terreno e a pergunta de Helena (mantido da v1)

- Preço pago (5.11): R$ 3.300.000 [FP].
  - Sobre 600,00 m²: R$ 5.500/m².
  - Sobre 571,80 m²: R$ 5.771/m² [EF].
- Esse preço não é valor de mercado do terreno: é uma transação só e inclui benfeitorias (5.11: "e as benfeitorias nele existentes"). O valor de mercado do terreno fica **[NC]**.
- Controle: lote de 525 m² no Jardim de Maria, anúncio de R$ 1.770.000, ou R$ 3.371/m², publicado em 28/08/2026 ([Attria TE0307](https://www.attria.com.br/imovel/terreno-em-condominio-a-venda-rio-de-janeiro-rj-no-bairro-recreio-dos-bandeirantes-525m2/d53ed614-6a87-42ee-833c-25d11dc09e26), acesso em 02/10/2026).
  - Sem fator de oferta, o preço pago fica 63% a 71% acima desse anúncio.
  - Com fator de oferta, o anúncio cai para R$ 2.899 a 3.068/m² (3.371 × 0,86 = 2.899,06; × 0,91 = 3.067,61). O preço pago fica então de 1,79 a 1,99 vez acima (5.500 / 3.068 = 1,79; 5.771 / 2.899 = 1,99) [EF].
- **Helena:** 28,20 m² (600,00 − 571,80) × R$ 5.500 = **R$ 155.100** [EF].
  - É aritmética sobre o preço pago, e não perda de mercado.
  - O efeito real está no potencial construtivo: S2 − S1 = R$ 293.280 a R$ 338.400 de revenda (seção 6).

---

## 9. O que eu perguntaria num caso real (não contatei ninguém)

| A quem | O quê | Por quê |
|---|---|---|
| Marcelo (corretor) | Matrícula e escrituras de C1, C4 e C6; se os m² construídos de C1, C2 e C4 (450, 480 e 500) são área total, computável ou averbada; padrão, idade e pavimentos de C1 e C4; há quanto tempo C2 está anunciado; a base dos 1.200 m² de C3 (terreno ou construída) e, se terreno, a área construída | A premissa de base (seção 0) e a distância de 33% até o mercado web dependem disso |
| Cartório de RI (certidão de inteiro teor) | Preço e área declarados nas escrituras de C1 e C4 | Conferência independente do corretor |
| Administradora / síndico | Vendas de 2025 e 2026; área dos lotes do condomínio; se algum lote de fundos para o lago já teve exigência de APP ou FMP | Aumentar a amostra; confirmar o tamanho dos lotes (hoje [INF]); saber se o mercado já desconta a APP (C4) |
| Banco (via Villaça e Wallenberg) | Que comparáveis e que fator de oferta o laudo do banco usa | O limite de 60% (5.14) segue o laudo do banco |
| Lúcio (via Villaça) | Quadro de áreas por tipo, inclusive a área da garagem dentro da projeção | Substituir a premissa [PV] e fechar a seção 7 |

---

## 10. Ressalvas finais

- Nenhum número é promessa de valor de venda. São faixas, com a base de área declarada em cada linha.
- Não usei média de bairro. Filtrei por tipo (casa em condomínio) e por metragem; o alvo de padrão foi o alto, mas nem todo anúncio declara o padrão (W11, por exemplo, não declara e está marcado como fraco). Todos os comparáveis são do Recreio; não foi preciso ampliar o raio.
- **Qualidade desigual:** as 2 vendas do dossiê valem mais que os anúncios para dizer o valor neste condomínio. Os anúncios mostram que esse valor está acima do resto do Recreio. W6 e W7 (sem data) e W11 (padrão não declarado) são os dados mais fracos.
- A Skill e o fator de oferta trazem as ressalvas R1 e R2. As áreas construídas são premissa de Villaça [PV], não desenho. As áreas computáveis são do Legal [PL].
- Legal, custo de obra e OODC estão fora do meu escopo.

*Declaração: ENSAIO 003, caso 100% fictício. Os dados do dossiê (5.1 a 5.15) foram tratados como reais dentro do ensaio. Os dados de mercado da web são reais, com link e acesso em 02/10/2026; na varredura da v5, as mesmas páginas foram relidas em 05/10/2026 só para conferir texto e rótulo. Ninguém foi contatado. A pasta `_gabaritos_LACRADO/` não foi aberta.*
