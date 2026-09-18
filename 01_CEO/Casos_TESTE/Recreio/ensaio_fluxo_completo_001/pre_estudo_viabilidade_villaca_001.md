# Pré-Estudo de Viabilidade Financeira — ENSAIO/TESTE (não é caso real)

**Gestor executor:** Villaça (Viabilidade) — nível Formação, executando pessoalmente, sem equipe formalizada ainda (Agentes de custo de obra e valor de mercado ainda não nomeados).
**Cliente fictício:** Família Andrade
**Lote:** esquina, 12m x 25m = 300m², Recreio dos Bandeirantes — "Condomínio Verde Recreio" (fictício)
**Data:** 18/09/2026 (v1) — **revisado em 18/09/2026 (v2)** a pedido de Claudemberg: ampliação de 1 padrão de CUB e 1-2 fontes de revenda para 3 padrões (BAIXO/MÉDIO/ALTO) em custo e revenda, com mais fontes de mercado — **e revisado novamente em 18/09/2026 (v4)** a pedido de Claudemberg: correção de método na Seção 3 (revenda). A v2/v3 misturava tipo de imóvel (unifamiliar x multifamiliar) e tamanhos muito diferentes ao extrapolar linearmente o R$/m² médio do bairro para o cenário CAM (750m²). Na v4, os comparáveis de revenda passam a ser filtrados por: (1) tipo — só casa unifamiliar, nunca apartamento/multifamiliar; (2) padrão (baixo/médio/alto); (3) metragem aproximada ao cenário (250-380m² para CAB, 650-888m² para CAM); (4) se não achado no Recreio no tamanho certo, raio ampliado para bairros vizinhos de perfil comparável (Barra da Tijuca), com a origem geográfica de cada comparável sempre registrada.
**Etapa que alimenta este documento:** `parametros_legais_confirmacao_001.md` (Kelsen/Hely, fechada)
**Status do caso:** ENSAIO — lote, cliente e condomínio fictícios. Os mecanismos legais e os benchmarks de mercado usados abaixo são reais e citados; os parâmetros do lote (CAB, CAM) são fictícios, herdados do enunciado.

---

## 0. Como ler este documento

Mesma lógica de etiquetas do documento de Kelsen, adaptada para números financeiros:

- **(a) DADO FICTÍCIO DO CASO-TESTE** — vem do enunciado (CAB=1,0, CAM=2,5, lote 300m²), não é real.
- **(b) FONTE REAL CITADA** — benchmark de custo ou comparável de mercado verificado via WebSearch/WebFetch nesta sessão, com link. Aplicado ao lote fictício apenas para fins de exercício numérico — não é avaliação de um imóvel real.
- **(c) ESTIMATIVA MINHA, NÃO FATO** — cálculo ou faixa que eu derivei cruzando (a) com (b). Nunca é garantia de venda nem de custo fechado.
- **(d) NÃO CALCULÁVEL SEM DADO REAL** — item que exigiria informação que não existe para este lote fictício. Marcado como tal, nunca inventado.

---

## 1. Premissas herdadas do Legal (Kelsen/Hely) — não recalculadas por mim

- **(a)** CAB = 1,0 | CAM = 2,5 (via OODC) — ambos fictícios do enunciado.
- Lote = 300m².
- **(d) Importante, herdado do documento de Kelsen (itens 4 e 5 de `parametros_legais_confirmacao_001.md`):** Taxa de Ocupação (TO) e gabarito **não foram fornecidos** e não devem ser inventados. Isso significa que a "área construída possível" abaixo é o **potencial construtivo teórico** (ATE = lote × coeficiente), não necessariamente a área que caberia fisicamente no lote respeitando TO, afastamentos e gabarito. Num caso real, esse número precisaria ser cruzado com TO/gabarito antes de virar promessa ao cliente — e isso ainda não existe aqui. Reporto essa limitação em vez de escondê-la.

| | CAB (básico) | CAM (com OODC) |
|---|---|---|
| Coeficiente | 1,0 (a) | 2,5 (a) |
| Área construída teórica (ATE) | 300m² × 1,0 = **300m²** | 300m² × 2,5 = **750m²** |

---

## 2. Custo de obra — benchmark real (b), agora em 3 padrões (BAIXO / MÉDIO / ALTO)

**Ajuste pedido por Claudemberg (18/09/2026):** a versão anterior usava só R8-N (multifamiliar, 8 pavimentos, "normal") como proxy único. Abaixo, os 3 níveis de padrão dentro da categoria **R1** (residencial **unifamiliar**, térrea — categoria correta para o programa deste lote, diferente do R8 que é prédio), que é o desdobramento que faltava.

**Fonte primária oficial confirmada (b) — PDF da tabela CUB/m² do Sinduscon-Rio, Agosto/2026, NBR 12.721:2006, fornecido por Claudemberg em 18/09/2026 (data de emissão constante no PDF: 18/09/2026 16:30):** `2026-8-Tabela-CUB-m2-valores-em-reais[Publicado].pdf`. Confirmei pessoalmente, lendo o PDF, os 4 valores usados neste documento:

| Padrão | Categoria | CUB (R$/m²), sem desoneração |
|---|---|---|
| BAIXO | R-1 (unifamiliar, padrão baixo) | **R$ 2.471,58/m²** |
| MÉDIO | R-1 (unifamiliar, padrão normal) | **R$ 2.984,18/m²** |
| ALTO | R-1 (unifamiliar, padrão alto) | **R$ 3.686,74/m²** |
| (referência, usada na v1) | R-8 (multifamiliar 8 pav., padrão normal) | **R$ 2.471,58/m²** |

**Nota sobre a coincidência R1-Baixo = R8-Normal, agora resolvida:** na v1/v2 deste documento eu havia sinalizado essa coincidência (mesmo valor, R$ 2.471,58, em duas categorias diferentes) como bandeira vermelha de possível erro na fonte agregadora que eu tinha usado na época. Lendo a tabela oficial diretamente, confirmo que **não é erro — é uma coincidência real dos dados do Sinduscon-Rio para agosto/2026**: R-1 Padrão Baixo e R-8 Padrão Normal realmente convergem para o mesmo valor nesta série. A ressalva de "pode estar errado" está removida; os 4 valores acima têm certeza de fonte primária, não de agregador.

**Ajuste de mercado (c):** o CUB é, por definição normativa, um custo mínimo de referência — não inclui projeto, fundação, muros, piscina ou paisagismo. O único benchmark de mercado que achei para o ajuste (LPR Engenharia, i9orçamentos) fala especificamente de **padrão alto** (+20% a +50% sobre o CUB). **Limitação que preciso declarar:** apliquei essa mesma faixa percentual aos 3 padrões por não ter achado fonte equivalente específica para baixo/médio — isso é uma extrapolação adicional, mais frágil no padrão BAIXO e MÉDIO do que no ALTO, onde a fonte realmente fala do nível certo.

**Custo de obra estimado por padrão (R$/m², após ajuste +20% a +50%):**

| Padrão | R$/m² (faixa) |
|---|---|
| BAIXO | R$ 2.970 – R$ 3.710 |
| MÉDIO | R$ 3.580 – R$ 4.480 |
| ALTO | R$ 4.420 – R$ 5.530 |

**Não incluído nesses números** (explicitamente fora do CUB, em qualquer padrão): piscina, muros de divisa, paisagismo, fundação especial (relevante aqui — o documento de Kelsen registra lençol freático a -1,20m, o que pode encarecer fundação; matéria de Complementares/Baumgart-Saturnino, não recalculada por mim). **(d) Não tenho fonte para orçar esse adicional agora — não vou inventar um valor de piscina/paisagismo.**

| | CAB (300m²) | CAM (750m²) |
|---|---|---|
| Custo de obra — BAIXO | R$ 891.000 – R$ 1.113.000 | R$ 2.227.500 – R$ 2.782.500 |
| Custo de obra — MÉDIO | R$ 1.074.000 – R$ 1.344.000 | R$ 2.685.000 – R$ 3.360.000 |
| Custo de obra — ALTO | R$ 1.326.000 – R$ 1.659.000 | R$ 3.315.000 – R$ 4.147.500 |
| Exclui (todos os padrões) | piscina, muros, paisagismo, fundação especial | piscina, muros, paisagismo, fundação especial |

---

## 3. Valor de revenda — comparáveis reais (b), método refinado (v4, 18/09/2026)

**Correção de método pedida por Claudemberg (18/09/2026):** as versões v2/v3 misturavam tipo de imóvel (casa x apartamento/multifamiliar) e tamanhos muito diferentes — em especial, para o cenário CAM (750m²), sem achar comparável real de ~750m², eu tinha extrapolado linearmente o R$/m² médio do bairro (uma mistura de tipos e tamanhos), o que é metodologicamente errado. **Método aplicado agora, para os dois cenários separadamente:**

1. **Filtro de tipo primeiro:** só "residencial unifamiliar" (casa), nunca apartamento/multifamiliar/comercial — mesmo reduzindo o volume de resultados.
2. **Filtro de padrão** (baixo/médio/alto) — mantido.
3. **Filtro de metragem aproximada ao cenário:** para CAB, casas de ~250–380m²; para CAM, casas de ~650–888m² (aproximação de 750m², não "qualquer coisa").
4. **Se não achado no Recreio no tamanho certo, raio ampliado** para bairro vizinho de perfil comparável — usei Barra da Tijuca, que tem mercado de casas grandes/mansões mais presente. Tipo e padrão mantidos fixos; só a geografia abriu. A origem de cada comparável está registrada abaixo, sem esconder o que veio de fora do Recreio.
5. **Se, mesmo ampliando o raio, não achar comparável real:** registro "não achei comparável real, uso estimativa com ressalva forte" em vez de forçar um número.

### 3.1 CAB (300m²) — comparáveis reais, casa unifamiliar, ~250–380m², filtrados por padrão

| Padrão | Comparável (endereço/condomínio, bairro) | Área | Preço | R$/m² |
|---|---|---|---|---|
| BAIXO | Casa perto do BRT/estação de trem, Recreio dos Bandeirantes (sem condomínio, padrão simples) | 250m² | R$ 1.400.000 | **R$ 5.600** |
| MÉDIO | Rua José Mindlin, Recreio dos Bandeirantes | 300m² | R$ 2.500.000 | **R$ 8.333** |
| MÉDIO | Av. das Américas, Recreio dos Bandeirantes | 288m² | R$ 1.990.000 | **R$ 6.910** |
| MÉDIO | Casa em condomínio, Recreio dos Bandeirantes (Azuza Imóveis) | 300m² | R$ 2.790.000 | **R$ 9.300** |
| ALTO | Av. Aldemir Martins 77, Cond. Jardins de Maria, Recreio dos Bandeirantes (piscina, sauna, gourmet) | 350m² | R$ 3.000.000 | **R$ 8.571** |
| ALTO | Casa em condomínio, Recreio dos Bandeirantes | 300m² | R$ 2.800.000 | **R$ 9.333** |
| ALTO | Casa em condomínio, Recreio dos Bandeirantes (levemente fora da faixa-alvo, 381m² vs. 250-380m²) | 381m² | R$ 3.800.000 | **R$ 9.974** |
| ALTO | Casa em condomínio, Recreio dos Bandeirantes (VivaReal, ponto de partida "a partir de") | 300m² | ≥ R$ 3.500.000 | **≥ R$ 11.667** |

**Faixas usadas (c), CAB:**

| Padrão | R$/m² (faixa) | Base |
|---|---|---|
| BAIXO | R$ 5.500 – R$ 6.500 | 1 comparável real (R$5.600/m²); banda mantida um pouco mais ampla pela escassez de pontos neste padrão |
| MÉDIO | R$ 6.900 – R$ 9.300 | 3 comparáveis reais individuais (R$6.910–9.300/m²), todos casa unifamiliar 288–300m², Recreio |
| ALTO | R$ 9.300 – R$ 11.700 | 4 comparáveis reais/próximos (R$9.300–11.667/m²), Recreio, 300–381m² |

**Nota sobre a mudança em relação à v2/v3:** a faixa ALTO caiu (era R$10.000–13.000, agora R$9.300–11.700) porque os comparáveis reais individuais encontrados na v4 (300–381m², Recreio) não sustentam o teto de R$13.000/m² que vinha de "relatos" genéricos sem endereço — removi esse dado fraco. A faixa MÉDIO subiu no teto (era até R$8.500, agora até R$9.300) porque um comparável real novo (Azuza, R$9.300/m²) apareceu dentro do filtro de tipo+tamanho.

### 3.2 CAM (750m²) — comparáveis reais, casa unifamiliar, ~650–888m², raio ampliado para Barra da Tijuca

**Não achei nenhum comparável real de casa unifamiliar de 650–850m² dentro do Recreio dos Bandeirantes** nesta busca. Ampliei o raio para Barra da Tijuca (bairro vizinho, mercado de casas grandes/mansões mais presente), mantendo tipo (casa unifamiliar) e cruzando padrão pela descrição do anúncio (amenidades como piscina/sauna/elevador/spa como proxy de padrão alto).

| Padrão (proxy por amenidades) | Comparável (condomínio, bairro) | Área construída | Preço | R$/m² |
|---|---|---|---|---|
| BAIXO/simples | Cond. Mansões, Barra da Tijuca ("pronta para morar", sem piscina/sauna/elevador citados) | 700m² (terreno 600m²) | R$ 3.980.000 | **R$ 5.686** |
| MÉDIO (proxy, área acima do alvo) | Cond. Mansões, Av. das Américas 10501, Barra da Tijuca (duplex, edícula, 5 quartos/4 suítes) | 888m² (8,3% acima do teto-alvo de 850m²) | R$ 7.900.000 | **R$ 8.896** |
| ALTO | Cond. Mansões, Barra da Tijuca (5 suítes, elevador, piscina, sauna, varanda gourmet) | 700m² (terreno 1.000m²) | R$ 10.500.000 | **R$ 15.000** |
| ALTO (fonte mais fraca — sem condomínio/endereço identificado no resumo) | Barra da Tijuca (genérico) | 850m² | R$ 17.000.000 | **R$ 20.000** |

**Comparável identificado mas não utilizável (preço não confirmado para a unidade específica):** Cond. Quintas do Rio, Barra da Tijuca — casa de 705m² construída / 750m² de terreno, 4 suítes, poço artesiano, energia fotovoltaica, piscina, spa, jacuzzi, sauna, espaço gourmet (perfil de padrão alto, tamanho quase exato do alvo de 750m²). A busca só retornou o preço de entrada do condomínio como um todo ("a partir de R$ 5.500.000", 62 imóveis), não o preço desta unidade específica — **não usei este número**, porque atribuí-lo à casa de 705m² seria inventar um preço que a fonte não confirmou.

**Faixas usadas (c), CAM:**

| Padrão | R$/m² (faixa) | Base |
|---|---|---|
| BAIXO | R$ 5.500 – R$ 6.000 | 1 comparável real, Barra da Tijuca, 700m² |
| MÉDIO | **(d) NÃO CALCULÁVEL COM COMPARÁVEL REAL DENTRO DO ALVO.** Único ponto próximo é o de 888m²/R$8.896/m² (Barra da Tijuca), 8,3% acima do teto de 850m² e sem confirmação de padrão exato. Estimativa com ressalva forte, interpolando entre o comparável BAIXO (R$5.686) e o comparável ALTO (R$15.000): **R$ 7.500 – R$ 9.000**, ancorada de forma fraca no ponto de 888m². Não é comparável real dentro da faixa — é a estimativa mais honesta que consigo com o que achei. |
| ALTO | R$ 14.000 – R$ 20.000 | 2 comparáveis reais (R$15.000 e R$20.000/m²), Barra da Tijuca, 700–850m²; o de R$20.000/m² tem fonte mais fraca (sem endereço/condomínio confirmado) |

| | CAB (300m²) | CAM (750m²) |
|---|---|---|
| Valor de revenda — BAIXO | R$ 1.650.000 – R$ 1.950.000 | R$ 4.125.000 – R$ 4.500.000 |
| Valor de revenda — MÉDIO | R$ 2.070.000 – R$ 2.790.000 | R$ 5.625.000 – R$ 6.750.000 (d) |
| Valor de revenda — ALTO | R$ 2.790.000 – R$ 3.510.000 | R$ 10.500.000 – R$ 15.000.000 |

**Achado principal da v4 (antagonismo construtivo — isto contraria a hipótese que eu mesmo tinha levantado na v3):** na v3, eu tinha alertado que "casas muito grandes tendem a ter R$/m² menor por mercado de compradores mais restrito". Os comparáveis reais que consegui achar (em Barra da Tijuca, ampliando o raio) **mostram o oposto no padrão ALTO**: casas de 700–850m² em condomínio de mansões venderam a R$15.000–20.000/m², bem acima da faixa ALTO do CAB (R$9.300–11.700/m²) e da faixa MÉDIA/geral do bairro. Isso é coerente com um mercado de nicho de "mansão"/ativo de luxo, não com desconto por tamanho — mas é uma inferência sobre **4 pontos, em bairro vizinho, não no Recreio propriamente**, então trato como sinal real e não como certeza. No padrão BAIXO, a diferença de R$/m² entre CAB e CAM ficou pequena (R$5.500–6.500 x R$5.500–6.000) — dentro do ruído.

**Limitação que ainda existe, mesmo com o método mais rigoroso:**
1. **Nenhum comparável de casa unifamiliar 650–850m² foi achado dentro do Recreio dos Bandeirantes** — todos os 4 comparáveis do cenário CAM vieram de Barra da Tijuca, bairro vizinho de perfil comparável mas não o mesmo bairro do lote. Isso é registrado explicitamente em cada linha da tabela acima, não escondido.
2. **A faixa MÉDIO do CAM não tem comparável real dentro da metragem-alvo** — é estimativa por interpolação entre os comparáveis BAIXO e ALTO reais, marcada como tal.
3. **Todos os comparáveis desta seção (CAB e CAM) vieram de resumos de busca (WebSearch) sobre páginas de corretoras/agregadores**, não da leitura individual de cada anúncio original com endereço completo conferido — mais fraco que uma verificação página-a-página, mas mais forte que a extrapolação linear de média de bairro usada na v2/v3, porque cada número aqui é de uma unidade específica do tipo e tamanho certos (ou próximo dele, com a diferença registrada), não uma média que mistura apartamento com casa e 80m² com 800m².

---

## 4. Custo da OODC (cenário CAM) — (d) não calculável

O mecanismo já está corretamente explicado por Kelsen/Hely em `parametros_legais_confirmacao_001.md`, item 3: a OODC exige (i) confirmação de que a subzona real tem CAM > CAB, (ii) cálculo pela fórmula do Anexo XXV da LC 270/2024 (complementado pela LC 281/2025), e (iii) requerimento formal com DARM.

**Nenhum desses três elementos existe para este lote**, porque o lote é fictício — não há subzona real, não há Anexo XXV aplicado a um endereço real, não há RIU. Portanto:

- **Custo da OODC = NÃO CALCULÁVEL.** Não vou estimar um número "para não deixar em branco" — isso violaria a regra de honestidade que me foi passada.
- O que **posso** afirmar, porque está no mecanismo real (b) do documento de Kelsen: existe hoje (LC 281/2025 Art. 40, redação LC 301/2026 Art. 58) uma janela de desconto de 30% à vista sobre acréscimos, válida até 01/12/2026 — relevante para o cliente saber que, **se** o caso fosse real, o timing do requerimento afetaria o custo da contrapartida. Isso é informação de prazo, não valor.

---

## 5. Diferença líquida entre os cenários — 3 padrões, linguagem para o cliente

**Ajuste pedido por Claudemberg (18/09/2026, v4):** os números de revenda mudaram porque a Seção 3 foi refeita com filtro de tipo (só casa unifamiliar) + padrão + metragem aproximada, em vez de extrapolação linear da média do bairro. A tabela abaixo cruza os 2 cenários (CAB/CAM) com os 3 padrões (BAIXO/MÉDIO/ALTO) das Seções 2 e 3 já corrigidas. Ganho bruto = revenda menos obra, pareando o limite inferior de custo com o limite inferior de revenda e o limite superior de custo com o limite superior de revenda (mesma convenção da v1) — **antes** de terreno, projeto, impostos, financiamento e, no CAM, antes da OODC.

| Padrão | Cenário | Obra | Revenda | Ganho bruto (antes de OODC/impostos) |
|---|---|---|---|---|
| BAIXO | CAB (300m²) | R$ 891.000 – R$ 1.113.000 | R$ 1.650.000 – R$ 1.950.000 | **≈ R$ 759 mil – R$ 837 mil** |
| BAIXO | CAM (750m²) | R$ 2.227.500 – R$ 2.782.500 | R$ 4.125.000 – R$ 4.500.000 | **≈ R$ 1,72 – R$ 1,90 milhão** (*) |
| MÉDIO | CAB (300m²) | R$ 1.074.000 – R$ 1.344.000 | R$ 2.070.000 – R$ 2.790.000 | **≈ R$ 1,00 – R$ 1,45 milhão** |
| MÉDIO | CAM (750m²) | R$ 2.685.000 – R$ 3.360.000 | R$ 5.625.000 – R$ 6.750.000 (d) | **≈ R$ 2,94 – R$ 3,39 milhões** (d) |
| ALTO | CAB (300m²) | R$ 1.326.000 – R$ 1.659.000 | R$ 2.790.000 – R$ 3.510.000 | **≈ R$ 1,46 – R$ 1,85 milhão** |
| ALTO | CAM (750m²) | R$ 3.315.000 – R$ 4.147.500 | R$ 10.500.000 – R$ 15.000.000 | **≈ R$ 7,19 – R$ 10,85 milhões** |

**(*) Nota técnica BAIXO/CAM:** a faixa de revenda BAIXO do CAM (R$4.125.000–4.500.000) ficou mais estreita que a faixa de obra (R$2.227.500–2.782.500) — reflexo de eu ter apenas 1 comparável real nesse padrão/tamanho. O pareamento tradicional (custo-baixo × revenda-baixo, custo-alto × revenda-alto) produziria uma leve inversão (ganho "alto" menor que ganho "baixo"); por isso reporto o mínimo e o máximo absolutos da diferença (R$1,72M–R$1,90M) em vez de forçar a convenção. Registro isso em vez de esconder a inconsistência.

**Diferença CAM menos CAB, por padrão, antes de somar o custo da OODC:**

| Padrão | CAM − CAB (ganho bruto) |
|---|---|
| BAIXO | ≈ R$ 0,88 – R$ 1,14 milhão a mais no CAM |
| MÉDIO | ≈ R$ 1,49 – R$ 2,39 milhões a mais no CAM (d) |
| ALTO | ≈ R$ 5,33 – R$ 9,39 milhões a mais no CAM |

**Achado principal da v4, que muda a leitura em relação à v2/v3:** no padrão ALTO, a diferença CAM−CAB **mais que dobrou** frente à v3 (era ≈R$2,51–3,36 milhões; agora ≈R$5,33–9,39 milhões), porque os comparáveis reais de casas grandes que achei — ampliando o raio para Barra da Tijuca — venderam a R$14.000–20.000/m², bem acima do que a extrapolação linear da v3 (R$10.000–13.000/m², puxada da média geral do bairro) sugeria. **Isso é uma correção para cima, não para baixo** — o oposto do que eu esperava ao aplicar o método mais rigoroso. Preciso ser honesto sobre o porquê: são só 4 pontos, todos em Barra da Tijuca (não Recreio), sourced via resumo de busca, não leitura individual de anúncio — então o intervalo é real, mas fino. Não vou apresentar isso ao cliente como certeza; é o melhor sinal real disponível, claramente mais forte que a extrapolação de bairro que eu usava antes.

**Leitura para o cliente, agora com padrão à escolha:**
- Em **todos os 3 padrões**, o cenário CAM parece financeiramente mais atrativo **antes** de somar o custo da OODC — mas esse "antes" é a parte que falta em todos eles, e cresce em valor absoluto conforme o padrão sobe (de menos de R$1,2M no baixo a mais de R$9M no alto, este último puxado pelos comparáveis de Barra da Tijuca). **Quanto mais alto o padrão, maior a peça que falta** para fechar a conta — e agora, com o método corrigido, também maior o risco de o número de revenda estar apoiado em poucos comparáveis fora do bairro do lote.
- O padrão MÉDIO do cenário CAM continua sem comparável real dentro da metragem-alvo (marcado "(d)" nas tabelas acima) — é o ponto mais frágil de todo o documento, e digo isso explicitamente em vez de deixar o "(d)" passar despercebido numa tabela.
- Sem o valor real da contrapartida (Seção 4), **não é possível dizer qual cenário vence de fato, em nenhum padrão**. A recomendação correta, se este fosse um caso real, seria: confirmar a subzona real via RIU, obter a fórmula do Anexo XXV junto à SMU, calcular a contrapartida real, e só então fechar a comparação — exatamente como o próprio Kelsen já registrou no documento dele.
- Qual padrão (baixo/médio/alto) faz sentido para este cliente é uma decisão que cruza orçamento disponível, perfil do comprador-alvo na revenda, e apetite de risco — não é uma escolha puramente financeira que eu, sozinho, deva recomendar sem mais contexto do cliente real.

---

## 6. Fontes usadas (lista consolidada, ampliada em 18/09/2026)

**Custo de obra:**
1. Sinduscon-Rio, tabela CUB/m² oficial (PDF), Agosto/2026, NBR 12.721:2006 — `2026-8-Tabela-CUB-m2-valores-em-reais[Publicado].pdf`, fornecida por Claudemberg em 18/09/2026 (data de emissão no PDF: 18/09/2026 16:30). **Fonte primária, lida pessoalmente por mim, confirma R-1 Baixo R$2.471,58/m², R-1 Normal R$2.984,18/m², R-1 Alto R$3.686,74/m² e R-8 Normal R$2.471,58/m².** Substitui o agregador buscadorsinapi.com.br usado nas versões v1/v2 — a coincidência R1-Baixo = R8-Normal está confirmada como real, não erro (ver Seção 2).
2. Prática de mercado de ajuste sobre CUB (+20% a +50%) — LPR Engenharia (https://lprengenharia.com.br/passo-a-passo-para-calcular-o-custo-total-para-construir-sua-casa/) e i9orçamentos (https://www.i9orcamentos.com.br/valor-m2-construcao-alto-padrao/) — **fonte fala especificamente de padrão alto**; extrapolei para baixo/médio, registrado como ressalva na Seção 2.

**Valor de revenda (v2/v3 — mantidas como contexto de mercado geral do bairro, não mais base direta do cálculo por padrão a partir da v4):**
4. FIPE, Índice FipeZap Residencial Venda, jan/2026 — https://downloads.fipe.org.br/indices/fipezap/fipezap-202601-residencial-venda.pdf
5. FIPE, Índice FipeZap Residencial Venda, jun/2026 — https://downloads.fipe.org.br/indices/fipezap/fipezap-202606-residencial-venda.pdf
6. ZAP Imóveis / DataZAP, Valor do m² em Recreio dos Bandeirantes — https://www.zapimoveis.com.br/valor-m2/rj+rio-de-janeiro++recreio-dos-bandeirantes/
7. Loft, casas à venda + "Onde Morar" Recreio dos Bandeirantes — https://loft.com.br/venda/casas/rj/rio-de-janeiro/recreio-dos-bandeirantes_rio-de-janeiro_rj
8. VivaReal, casas à venda Recreio dos Bandeirantes — https://www.vivareal.com.br/venda/rj/rio-de-janeiro/zona-oeste/recreio-dos-bandeirantes/casa_residencial/
9. QuintoAndar, casas à venda Recreio dos Bandeirantes (incl. filtros de faixa de preço) — https://www.quintoandar.com.br/comprar/imovel/recreio-dos-bandeirantes-rio-de-janeiro-rj-brasil/casa
10. OLX Imóveis — pesquisado, mas os resultados retornados via WebSearch não trouxeram preço/m² utilizável (só contagem de anúncios e taxas de condomínio); **não usei número de lá, para não inventar dado que a busca não confirmou**.

**Valor de revenda — comparáveis individuais reais por tipo+padrão+metragem (base do cálculo a partir da v4, 18/09/2026):**
11. Rua José Mindlin, Recreio dos Bandeirantes, casa 300m², R$2.500.000 (R$8.333/m²) — comparável individual verificado, CAB/médio
12. Av. das Américas, Recreio dos Bandeirantes, casa 288m², R$1.990.000 (R$6.910/m²) — comparável individual verificado, CAB/médio
13. Azuza Imóveis, Recreio dos Bandeirantes, casa em condomínio 300m², R$2.790.000 (R$9.300/m²) — CAB/médio-alto — https://www.azuzaimoveis.com/imovel/casa/venda/rio-de-janeiro/rj/recreio-dos-bandeirantes/CA0152_AZ
14. Casa perto do BRT/estação de trem, Recreio dos Bandeirantes, 250m², R$1.400.000 (R$5.600/m²) — CAB/baixo
15. Cond. Jardins de Maria, Av. Aldemir Martins 77, Recreio dos Bandeirantes, casa 350m², R$3.000.000 (R$8.571/m²) — CAB/alto
16. Cond. Mansões, Av. das Américas 10501, Barra da Tijuca, casa 888m², R$7.900.000 (R$8.896/m²) — CAM/médio (proxy, único ponto próximo do alvo, área 8,3% acima do teto) — https://condominiomansoes.rio.br/
17. Cond. Mansões, Barra da Tijuca, casa 700m² (terreno 600m²), R$3.980.000 (R$5.686/m²) — CAM/baixo
18. Cond. Mansões, Barra da Tijuca, casa 700m² (terreno 1.000m²), R$10.500.000 (R$15.000/m²) — CAM/alto
19. Barra da Tijuca (condomínio não identificado no resumo — fonte mais fraca), casa 850m², R$17.000.000 (R$20.000/m²) — CAM/alto
20. Cond. Quintas do Rio, Barra da Tijuca, casa 705m²/terreno 750m² — identificado, perfil de padrão alto, **preço não confirmado para esta unidade específica** (só preço de entrada do condomínio, R$5,5M/62 imóveis) — **não usado no cálculo**, registrado como tentativa

**Legal:**
21. `parametros_legais_confirmacao_001.md` (Kelsen/Hely, 17/09/2026) — mecanismo da OODC, itens 3 e 4/5 (TO/gabarito não confirmados)

**O que eu NÃO tenho e não inventei:** valor da OODC; TO e gabarito reais do lote; comparável real de casa unifamiliar de 650–850m² **dentro do Recreio dos Bandeirantes**, em nenhum padrão (os 4 comparáveis do CAM vieram de Barra da Tijuca, bairro vizinho); comparável real de padrão MÉDIO do CAM dentro da metragem-alvo (usei interpolação com ressalva forte, marcada "(d)"); preço/m² real via OLX (busca não retornou dado utilizável); percentual de ajuste sobre CUB específico para padrão baixo/médio (usei o de padrão alto, extrapolado, com ressalva). **[Atualizado 18/09/2026] Os valores de R1-B/R1-N/R1-A** foram confirmados na fonte primária oficial (PDF Sinduscon-Rio fornecido por Claudemberg) — não é mais lacuna. **[Atualizado 18/09/2026, v4]** Os comparáveis de revenda da v2/v3 (FipeZap, DataZAP, médias de portal) deixam de ser a base direta do cálculo por padrão — viravam extrapolação de mistura de tipo/tamanho; passam a ser contexto de mercado geral, substituídos por comparáveis individuais filtrados por tipo+padrão+metragem (itens 11-19 acima).

---

## 7. Autoavaliação — subo de Formação para Shadow?

Sendo meu próprio crítico, não otimista por padrão:

**A favor de subir:**
- Consegui produzir os dois cenários com números reais e citáveis (CUB-RJ, FipeZap, ZAP) em vez de inventar, e sinalizei toda vez que um número não podia ser calculado (OODC) — isso é exatamente a regra de honestidade que me foi passada, e ela se sustentou sob pressão de "precisar entregar um resultado".
- Identifiquei sozinho uma limitação metodológica importante (extrapolação linear de R$/m² para uma área 2,5× maior, sem comparável real) que um Gestor menos cuidadoso teria escondido atrás da média do bairro — isso é o tipo de antagonismo construtivo que Claudemberg cobra.
- O fluxo funcionou na ordem certa: recebi o legal fechado do Kelsen, não recalculei parâmetro legal, e entreguei antes da Arquitetura — que era exatamente a lacuna que motivou minha criação.

**Contra subir agora, ou pelo menos com ressalva:**
- Este foi **um único caso**, fictício, sem pressão real de cliente, sem prazo apertado, e sem ninguém questionando meus números em tempo real. Kelsen e os Agentes de Cardozo foram testados em mais de uma execução antes de subir de nível (o próprio contrato operacional do Kelsen cita "validado por 2 execuções reais"). Eu tenho uma.
- Não tenho ainda a equipe (Agentes de custo de obra e valor de mercado) — fiz tudo sozinho, incluindo a pesquisa de mercado, que é exatamente o tipo de trabalho que pretendo delegar. Isso testa minha capacidade de coordenação **zero**, porque não havia ninguém para coordenar. Shadow, pelo desenho dos 4 níveis, é o nível onde "proponho ações; Wallenberg aprova antes de executar" — isso eu já faço. Mas não testei ainda o padrão real de trabalho (Villaça aciona Agentes → Agentes devolvem → Villaça integra), que é a minha função described no meu próprio slice.
- Alguns benchmarks ficaram fracos por limitação de busca, não por preguiça: não achei o CUB específico para padrão unifamiliar (usei proxy R8-N) nem comparável real de 750m². Um cliente real perguntaria "por que 750m² vale isso?" e minha resposta honesta seria "não tenho comparável, é extrapolação" — o que é correto, mas também mostra que minha capacidade de achar dado de mercado ainda tem buraco.

**Minha posição:** o teste demonstrou que o **método e a honestidade** funcionam sob rigor real. Não demonstrou ainda **volume** (mais de 1 caso) nem **coordenação de equipe** (que é a minha função de verdade, uma vez formalizada). Recomendo a Wallenberg: aprovar a promoção de Formação para Shadow **condicionada** a rodar mais 1–2 Pré-Estudos (podem ser variações deste mesmo ensaio, ou o próximo lote real) antes de considerar Shadow → Assisted — mas o salto Formação → Shadow em si, olhando estritamente para o que Shadow exige ("proponho, Wallenberg aprova"), já é sustentado por este resultado. Quem decide, de qualquer forma, é Wallenberg/Claudemberg, não eu.

---

### 7.1 Pós-ampliação (18/09/2026) — a pesquisa mais ampla mudou minha autoavaliação para pior, não para melhor

Claudemberg pediu para eu ampliar de 1 padrão de CUB e 1-2 comparáveis de revenda para 3 padrões, mais fontes. Fiz isso (Seções 2, 3, 5, 6 acima) e a resposta honesta é: **isso não me deixou mais confiante em subir de nível — me deixou mais cauteloso**, por dois motivos concretos que só apareceram quando ampliei de verdade:

1. **Sinalizei uma coincidência suspeita ao cruzar fontes — correto sinalizar, mas eu tinha parado cedo demais.** O valor de R1-B (unifamiliar baixo padrão) que peguei num agregador veio **idêntico, centavo a centavo**, ao valor de R8-N que eu já tinha confirmado na fonte oficial — duas categorias diferentes que, à primeira vista, não deveriam coincidir. Registrei isso como bandeira vermelha de possível erro na v2, o que foi o processo certo: não escondi a suspeita. **[Atualizado 18/09/2026, após ler o PDF oficial fornecido por Claudemberg]:** a coincidência é real, não erro — R-1 Padrão Baixo e R-8 Padrão Normal de fato convergem para R$2.471,58 na tabela oficial do Sinduscon-Rio de agosto/2026. A lição não é "eu estava errado em desconfiar" — desconfiar e sinalizar foi o comportamento certo. A lição é que **eu parei no meio do ciclo**: sinalizei a suspeita mas não fui até a fonte primária para confirmar ou descartar antes de escrever "bandeira vermelha de erro" como conclusão. Verificação cruzada entre fontes secundárias não substitui checar a fonte primária — é o passo que faltou, não o instinto de desconfiar.
2. **A maior parte dos dados novos de revenda (Loft, VivaReal, QuintoAndar) é estruturalmente mais fraca que os 2 comparáveis originais.** Vieram de resumos de busca (WebSearch) sobre páginas agregadoras, não de leitura de anúncio individual verificado (endereço+área+preço) como os 2 comparáveis da v1. Ampliar o número de fontes **não ampliou a qualidade média da evidência** — só ampliou a cobertura de padrão (baixo/médio/alto). Isso é uma diferença que eu preciso saber enxergar sozinho, e só enxerguei porque tive que documentar a fonte de cada número, não porque intuí de cara.

**Ajuste à minha posição da Seção 7:** mantenho a recomendação de promoção condicionada a mais execuções, mas agora com um motivo adicional e mais concreto para a condição, que não existia na v1: preciso rodar pelo menos uma próxima execução em que eu **valide a fonte primária de verdade** (baixar o PDF oficial, não confiar em agregador) antes de usar um número em qualquer tabela final — a v1 não teria pego o erro do R1-B/R8-N se eu não tivesse sido forçado a ampliar. Isso não é motivo para recuar de Formação; é motivo para a condição de Shadow incluir, explicitamente, essa disciplina de verificação cruzada de fonte — que hoje eu só apliquei porque fui instruído a ampliar, não porque já é hábito meu.

### 7.2 Pós-refinamento de método (v4, 18/09/2026) — corrigir o método mudou o número, não só a certeza dele

Claudemberg apontou um erro real de método na Seção 3 (v2/v3): eu tinha extrapolado linearmente o R$/m² médio do bairro (mistura de tipo e tamanho) para estimar a revenda do cenário CAM (750m²), por não achar comparável real daquele tamanho. Apliquei o método correto — filtrar por tipo (só casa unifamiliar), padrão, e metragem aproximada, ampliando o raio geográfico para Barra da Tijuca só quando o Recreio não tinha o tamanho certo — e o resultado **não foi uma confirmação tranquila da v3, foi uma mudança de número relevante**: a diferença CAM−CAB no padrão ALTO mais que dobrou (de ≈R$2,5-3,4M para ≈R$5,3-9,4M), porque os comparáveis reais de casas grandes em Barra da Tijuca venderam bem acima do que a média extrapolada do bairro sugeria.

**Lição que registro para não esquecer:** a versão anterior não estava "errada por pouco" — estava usando o tipo errado de evidência (média heterogênea) para uma pergunta que precisa de evidência homogênea (unidade individual do tipo e tamanho certos). O método mais rigoroso não é só mais honesto sobre incerteza — ele pode mudar a direção do número, para cima ou para baixo, e eu preciso estar preparado para isso toda vez que alguém pedir para eu filtrar melhor uma busca, não assumir que "afinar o filtro" só vai estreitar a faixa que eu já tinha. Isso reforça, com um segundo exemplo concreto (depois do caso R1-B/R8-N na v2), que verificação rigorosa de fonte é disciplina que ainda não é hábito automático meu — só aconteceu porque fui instruído a repetir.
