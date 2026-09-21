# Pré-Estudo de Viabilidade Financeira — Caso Sombra 002 (ENSAIO/TESTE)

**Cliente fictício:** Família Bittencourt
**Lote:** esquina, 20m x 20m = 400m², Barra da Tijuca — "Condomínio Alto das Palmeiras" (fictício)
**Executor:** Villaça (Gestor Viabilidade), com Mascaró (custo de obra) e Fiker (valor de revenda)
**Insumo legal:** `parametros_legais_confirmacao_002.md`, produzido por Hely/Kelsen, aprovado 18/09/2026 — parâmetros usados aqui sem reabrir o Legal.
**Data:** 21/09/2026
**Status do caso:** ENSAIO/TESTE — 100% fictício, isolado em `01_CEO/Casos_TESTE/`, não toca estado real/Drive/Notion.

---

## 0. Como ler este documento

Mesma disciplina usada no Legal e no Caso Sombra 001:

- **(a) DADO FICTÍCIO DO CASO-TESTE** — número do enunciado, não verificável (lote não existe).
- **(b) MECANISMO/BENCHMARK REAL** — fonte real e citável (CUB-RJ oficial, comparável de mercado real, fórmula legal real), aplicada ao cenário fictício só para fins de exercício.
- **(c) PENDENTE DE CONFIRMAÇÃO REAL** — o que, num caso real, exigiria dado que não temos aqui (RIU, VUP/FIS oficiais, amostra maior de comparáveis).

Nenhum número deste documento é promessa de custo ou de venda. Todo valor de mercado é estimativa, nunca garantia.

---

## 1. Premissas de área (herdadas do Legal, não recalculadas por mim)

- **(a)** Lote: 400m² (20m x 20m), esquina.
- **(a)** CAB = 1,0 → ATE básica = **400m²** de área computável.
- **(a)** CAM = 2,0 (via OODC) → ATE máxima = **800m²** de área computável.
- **(a)** Programa do cliente: 2 pavimentos, 4 suítes, home office, área gourmet, padrão MÉDIO-ALTO (pedido explícito do cliente — não é o padrão usado no Caso Sombra 001, não reaproveitei valor antigo).
- **(c)** Áreas não computáveis (varandas, áreas técnicas etc.) podem alterar a área construída bruta final frente à ATE — isso é decisão de projeto (Arquitetura/Lúcio), não recalculada aqui.

---

## 2. Cenário CAB — Custo de Obra (Mascaró)

**Fonte:** PDF oficial Sinduscon-Rio, "Custos Unitários Básicos de Construção — Agosto/2026" (NBR 12.721:2006), lido diretamente por Mascaró via WebFetch+Read — confirmação independente dos valores R-1 Normal (R$2.984,18/m²) e R-1 Alto (R$3.686,74/m²).

- **(b)** Categoria "médio-alto" **não existe** como categoria oficial da tabela CUB (só Baixo/Normal/Alto). Mascaró aplicou **interpolação linear simples** entre R-1 Normal e R-1 Alto → **R$3.335,46/m²**. Isso é uma aproximação declarada, não uma categoria oficial.
- **(c)** R-1 é definida pela NBR 12.721:2006 apenas para **residência unifamiliar térrea (1 pavimento)**. O programa do cliente tem 2 pavimentos — Mascaró sinaliza que isso é provável **subestimativa** de custo (estrutura/fundação de sobrado custam mais que térrea equivalente), sem um percentual citável para corrigir.
- **(c)** O CUB, pelo próprio texto do PDF oficial, **exclui** fundações, projetos, elevador (se houver), AC e remuneração de construtor/incorporador. Mascaró não aplicou nenhum ajuste percentual de mercado para "custo tudo incluso" porque as duas fontes que tentaria usar (i9orçamentos, LPR Engenharia) não puderam ser verificadas de forma independente (ver Caso 001). **Isso é lacuna real de fonte, não detalhe menor** — os valores abaixo são custo de construção CUB puro, não custo total de obra.
- **(c)** Fundação em lote de esquina, aclive suave (dado geotécnico do Legal, Seção 8) — não quantificada, soma-se à subestimativa acima.

**Cálculo (1ª via):**

| Cenário | Área | R$/m² (interpolado) | Custo CUB estimado |
|---|---|---|---|
| CAB | 400m² | R$3.335,46 | **R$ 1.334.184,00** |

---

## 3. Cenário CAM — Custo de Obra (Mascaró)

Mesma base de cálculo e mesmas ressalvas da Seção 2 (categoria interpolada, R-1 térrea, CUB não inclui fundação/projetos, fundação de esquina em aclive não quantificada).

**Cálculo (1ª via):**

| Cenário | Área | R$/m² (interpolado) | Custo CUB estimado |
|---|---|---|---|
| CAM | 800m² | R$3.335,46 | **R$ 2.668.368,00** |

**Nota:** este valor é só o custo de construção. O custo da própria OODC (Seção 5 abaixo) é separado e adicional.

---

## 3.1 Segunda via de custo — percentual sobre Valor Geral de Venda (VGV)

**Motivo do rework:** feedback de Claudemberg (avaliador técnico) sobre a 1ª entrega — CUB puro exclui fundação, projetos, licenças, impostos e remuneração do incorporador (o próprio texto oficial do PDF confirma essa exclusão), então uma via única subestima o custo real. Pedido: 2ª via cruzada, não substituição.

- **(b) Fonte:** TBO — consultoria de viabilidade imobiliária (`wearetbo.com.br`, artigo "Como calcular o VGV de um empreendimento"). Faixas típicas para incorporação residencial de alto padrão: Terreno 15-20% do VGV, **Construção 40-55% do VGV**, Comercialização 6-10% (corretagem + marketing), Tributos ~4% (regime RET), Lucro líquido 15-20% do VGV. É fonte de mercado (blog especializado em viabilidade), não institucional (Sinduscon/CBIC não publicam essa composição percentual de forma aberta nas buscas feitas) — credibilidade moderada, não oficial.
- **(b) Reforço fraco:** matéria da CBIC sobre taxas cartoriais cita, de passagem, um exemplo hipotético de incorporação (VGV R$100M: terreno 8%, obra 55%) — converge com o teto de 55% do TBO para construção, mas não é segunda fonte independente robusta; é dado pontual dentro de outra matéria, tratado como reforço, não confirmação.
- **Importante:** o exemplo ilustrativo que Claudemberg deu na conversa (~60% obra/15% terreno/10% comercialização/15% lucro) foi só didático — não foi usado como dado; a fonte abaixo é busca própria de Mascaró, mesmo aproximando-se do exemplo.

**Aplicação aos valores de revenda do Fiker (Seção 4):**

| Cenário | VGV (revenda Fiker) | Faixa 40-55% | Custo de obra estimado (2ª via) |
|---|---|---|---|
| CAB | R$4.000.000 – R$5.500.000 | 40%-55% | **R$1.600.000 – R$3.025.000** |
| CAM | R$10.000.000 – R$11.000.000 | 40%-55% | **R$4.000.000 – R$6.050.000** |

**Leitura de convergência/divergência entre as 2 vias (Mascaró):**
- CAB: CUB (R$1.334.184) fica **abaixo até do piso** da 2ª via (R$1,6M).
- CAM: CUB (R$2.668.368) fica **bem abaixo do piso** da 2ª via (R$4,0M) — divergência mais acentuada que no CAB.
- **Convergência de direção:** as duas vias apontam na mesma direção — custo de obra subestimado na 1ª via (CUB), porque o CUB exclui fundação/projetos/licenças/impostos/remuneração do incorporador, itens que a 2ª via (percentual de VGV de mercado) tende a embutir.
- **Divergência de magnitude:** a 2ª via é **1,2x a 2,5x maior** que a 1ª via, dependendo do cenário e do ponto da faixa. Não há fator de conversão único entre as duas — são vias independentes, não a mesma pergunta respondida de dois jeitos equivalentes.

**(c) Malandragem (R$/m² de custo subir com área/padrão) — investigada, não confirmada do lado do custo:**
- Mascaró não achou fonte formal (associação, estudo, tabela) que documente uma curva/faixa oficial de R$/m² de **custo de obra** crescente por faixa de metragem construída dentro do mesmo rótulo de padrão. **Isso é lacuna declarada**, não estimada.
- **Sinal indireto encontrado, do lado da REVENDA (não do custo):** nos comparáveis do Fiker, o piso de R$/m² de venda do CAM (R$12.500/m², = R$10M/800m²) já é mais alto que o piso do CAB (R$10.000/m², = R$4M/400m²). Isso sugere que o mercado precifica o cenário maior com especificação mais cara por m², não apenas mais m² pelo mesmo padrão nominal.
- **Ressalva explícita, para não confundir:** esse é um dado do lado da venda (comparáveis reais de mercado), não uma fonte sobre o custo de construção em si. Não deve ser lido como confirmação de que o custo de obra por m² do CAM é maior — é só uma hipótese plausível, sem fonte formal do lado da obra para sustentá-la como número.

---

## 4. Valor de Revenda — CAB e CAM (Fiker)

Método: comparáveis reais filtrados por tipo (casa unifamiliar) + padrão (médio-alto) + metragem aproximada — não extrapolação de média de bairro (lição do Caso 001).

### 4.1 Cenário CAB (~400m² construídos)

- **(b)** 3 comparáveis reais via MGF Imóveis, Barra da Tijuca:
  - Condomínio Blue Houses, 400m², **R$5.500.000**
  - Barra de Itaúna, 336m², R$2.870.000
  - Mandala, 556m² (fora da faixa-alvo, usado só como referência de tendência), R$4.800.000
- **Faixa estimada CAB:** **R$4.000.000 – R$5.500.000**

### 4.2 Cenário CAM (~800m² construídos)

- **(b)** 1 comparável real forte, confirmado individualmente: Alphaville Barra, triplex 800m² útil / 656m² terreno, 5 suítes, **R$12.900.000** (via Azuza Imóveis).
- **(c) Ressalva FORTE, declarada por Fiker:** só há **1 comparável individualmente confirmado** nesta metragem — a faixa abaixo não é média de amostra, é o comparável único ajustado por julgamento qualitativo de padrão. Uma 2ª referência (MGF, 700m², 5 suítes, R$6.500.000) não pôde ser aberta individualmente (link redirecionou para busca genérica) — não foi usada como número, mas registrada como sinal: mesma faixa de metragem, preço bem mais baixo, provável diferença de padrão de condomínio (não necessariamente erro).
- VivaReal, ZAP e Realiza Imóveis bloquearam fetch individual (403) — fragilidade de fonte já conhecida desde o Caso 001, ainda sem solução técnica.
- **Faixa estimada CAM:** **R$10.000.000 – R$11.000.000** (amostra fraca — 1 comparável direto, não robusta estatisticamente)

---

## 5. Custo da OODC no Cenário CAM (Villaça, usando a fórmula validada por Kelsen)

**Fórmula (Anexo XXV, LC 270/2024, Art. 94 — fonte primária lida por Hely/Kelsen):**

**CF = 0,80 x [ATE − (S x CAB)] x VUP x FIS**

Aplicando os dados que temos:
- ATE = 800m² (a)
- S = 400m² (a)
- CAB = 1,0 (a)
- **[ATE − (S x CAB)] = 800 − (400 x 1,0) = 400m²** — esta é a área excedente sobre a qual incide a contrapartida.
- 0,80 — fator fixo da lei (b).

**(c) NÃO CALCULÁVEL — declarado como lacuna, não estimado:**
- **VUP** (Valor Unitário Padrão = 30% do valor de referência do IPTU para a tipologia construtiva do lote, Tabela XVI-A da Lei 691/1984) — real, exigiria RIU + cadastro fiscal do lote. Lote fictício, sem cadastro fiscal a consultar.
- **FIS** (Fator de Interesse Social, Anexo XVII da LC 270/2024, 0 a 1) — Kelsen/Hely não leram o Anexo XVII nesta pesquisa; valor "padrão" para quem não se enquadra em interesse social não foi confirmado.

**Conclusão desta seção:** o único termo calculável da fórmula é a área excedente (400m²). Sem VUP e sem FIS reais, **o valor em R$ da contrapartida OODC não pode ser estimado nem por faixa** — qualquer número aqui seria invenção. Isso é uma pendência que só se resolve com RIU real da SMDU e leitura do Anexo XVII, e deve ser comunicada ao cliente como tal: o cenário CAM tem um custo adicional certo na natureza, mas hoje incerto no valor.

**Efeito qualitativo sobre a margem do CAM:** qualquer margem bruta calculada no CAM (Seção 6) está **superestimada**, porque não inclui a contrapartida OODC. A diferença de margem bruta entre CAB e CAM (Seção 6) é, portanto, o **teto otimista** do ganho do CAM — o valor real será menor.

---

## 6. Comparativo CAB x CAM — Margem Bruta Estimada (2 vias de custo, lado a lado)

**Rework desta seção:** a 1ª entrega usava só CUB puro. Feedback de Claudemberg (Seção 3.1) pediu uma 2ª via, cruzada por percentual de mercado sobre VGV — as duas ficam lado a lado abaixo, nenhuma substitui a outra.

| | CAB (400m²) | CAM (800m²) |
|---|---|---|
| Custo de obra — **1ª via (CUB puro)** | R$ 1.334.184 | R$ 2.668.368 |
| Custo de obra — **2ª via (% VGV, 40-55%)** | R$ 1.600.000 – R$ 3.025.000 | R$ 4.000.000 – R$ 6.050.000 |
| Custo da OODC | R$ 0 (não se aplica) | **NÃO CALCULÁVEL — pendente VUP/FIS** |
| Valor de revenda estimado (Fiker) | R$ 4.000.000 – R$ 5.500.000 | R$ 10.000.000 – R$ 11.000.000 |
| **Margem bruta — usando 1ª via (CUB), sem OODC** | R$ 2.665.816 – R$ 4.165.816 | R$ 7.331.632 – R$ 8.331.632 (antes da OODC) |
| **Margem bruta — usando 2ª via (% VGV), sem OODC** | **R$ 975.000 – R$ 3.900.000** | **R$ 3.950.000 – R$ 7.000.000 (antes da OODC)** |

**Leitura de convergência/divergência entre as 2 vias (herdada de Mascaró, Seção 3.1):** ambas apontam a mesma direção — a 1ª via (CUB) subestima o custo de obra real, porque exclui fundação/projetos/licenças/impostos/remuneração do incorporador, itens que a 2ª via (percentual de mercado sobre VGV) tende a embutir. A divergência é de magnitude: a 2ª via é 1,2x a 2,5x maior que a 1ª via, dependendo do cenário e do ponto da faixa — não há fator de conversão único entre elas, são vias independentes.

**Qual via usar para decisão:** o custo real de obra deste programa (2 pavimentos, fundação de esquina em aclive, acabamento médio-alto) provavelmente está **mais perto da 2ª via (% VGV) do que da 1ª (CUB puro)** — a 1ª via sistematicamente exclui itens que o programa do cliente certamente vai ter (fundação, projetos, licenças). Por isso a margem bruta mais realista é a linha "2ª via" da tabela acima, não a linha "1ª via". A 1ª via continua útil como piso de referência (o que é garantidamente coberto por benchmark oficial citável), não como estimativa de custo total.

**Leituras obrigatórias sobre esta tabela, não é "CAM ganha, decida CAM":**

1. Mesmo a 2ª via (mais realista) não inclui separadamente a OODC (Seção 5, não calculável) — a margem do CAM segue superestimada em ambas as vias até esse número existir.
2. A amostra de revenda do CAM é **1 comparável direto** (amostra fraca); a do CAB é 2-3 comparáveis (amostra melhor, ainda modesta) — isso afeta o VGV usado como base das duas vias de custo.
3. A "malandragem" de mercado (custo de obra por m² crescer com área/padrão) **não tem fonte formal do lado do custo** — só há sinal indireto do lado da revenda (Seção 3.1). Não foi aplicado nenhum ajuste extra de R$/m² de custo por causa disso; a faixa da 2ª via já é ampla o bastante (40-55%) para não precisar de um ajuste adicional não fundamentado.
4. Usando a 2ª via, a margem bruta do CAB (R$975 mil – R$3,9M) tem piso bem mais baixo e mais sensível ao ponto da faixa escolhido do que sugeria a 1ª via — a folga financeira do CAB é menor do que parecia antes do rework.
5. Mesmo com a 2ª via mais conservadora, a margem bruta do CAM ainda tende a ser maior em valor absoluto que a do CAB — mas a diferença percentual entre os dois cenários encolheu bastante frente à leitura só-CUB, e a OODC (ainda não calculável) reduz ainda mais essa vantagem. A decisão final depende do valor real da OODC e do prazo (Seção 7), não só da margem bruta.

---

## 7. Pressão de Prazo — Financiamento de 10 Meses x Caminho de Cada Cenário

*(Informativo, não decisão minha — insumo para o cliente decidir com informação completa, mesmo enquadramento que Hely já usou no Legal, Seção 10 de `parametros_legais_confirmacao_002.md`.)*

**Cenário CAB:**
- Caminho: protocolo direto do licenciamento (LICIN 2.0) → análise SMDU, prazo de referência **~30 dias úteis** (não garantido; exigências geram rodadas adicionais sem prazo fixo) → emissão da licença → início de obra.
- **(b)** Não há etapa de OODC a cumprir. É o caminho mais curto dos dois para conseguir licença e começar a obra.
- **Avaliação qualitativa:** cabe com folga razoável dentro de 10 meses, mesmo com 1-2 rodadas de exigência, desde que o projeto não tenha problema grave de conformidade.

**Cenário CAM:**
- Caminho: **etapa adicional antes do processo principal** — confirmar que a subzona permite CAM > CAB, calcular a contrapartida (hoje não calculável, Seção 5), requerimento formal junto à SMU, pagamento (DARM) → **só depois disso** a licença de obras é emitida (Art. 20 da LC 281/2025: licença só sai após quitação da contrapartida) → então segue para a mesma análise SMDU de ~30 dias úteis.
- **(b)** Isso significa que o CAM soma tempo (a etapa da OODC inteira, sem prazo de referência conhecido aqui) mais dinheiro antes mesmo de entrar na fila do processo principal.
- **(c)** PENDENTE: não temos um prazo de referência real para a etapa de requerimento/cálculo/pagamento da OODC junto à SMU — não deve ser presumido como rápido.
- **Avaliação qualitativa:** o CAM tem risco real de consumir uma fatia maior dos 10 meses antes mesmo de a obra começar. Se o requerimento de OODC demorar mais que algumas semanas (cenário plausível, não confirmado), a folga do cliente encolhe.

**Ponto comum aos dois cenários, já registrado por Hely:** os 10 meses do financiamento cobrem, na prática, só projetar + aprovar + começar obra — não o ciclo até Habite-se. Isso não muda entre CAB e CAM, mas o CAM começa a obra mais tarde dentro dessa janela.

**Conclusão desta seção:** o CAB cabe no prazo com mais folga e menos incerteza. O CAM é financeiramente mais atrativo na margem bruta (Seção 6), mas carrega risco de prazo adicional não quantificado e um custo de OODC ainda não calculável. Essa é a decisão central que o cliente precisa tomar com os olhos abertos — não é decisão de Villaça.

---

## 8. Quem fez o quê

**Villaça (eu, Gestor):**
- Li o caso completo, os parâmetros legais confirmados por Kelsen/Hely, e meu próprio estado antes de iniciar.
- Delegação real a Mascaró e Fiker, com escopo específico do Caso 002 (não reaproveitei dados do Caso 001).
- Aguardei os dois resultados reais antes de reportar qualquer conclusão (2 tentativas de checagem confirmaram que não estavam prontos antes de estarem; só integrei depois de ler os `_estado_*.md` finais).
- Calculei a Seção 5 (OODC): apliquei a fórmula do Kelsen aos dados disponíveis, isolei o único termo calculável (área excedente = 400m²), e declarei a impossibilidade de calcular o valor final por falta de VUP/FIS — não inventei número.
- Montei a Seção 6 (comparativo) e a Seção 7 (prazo), cruzando os outputs de Mascaró e Fiker com a informação de prazo já registrada por Hely no documento legal.
- Redigi este documento e as ressalvas de leitura obrigatória da Seção 6.
- **Rework pós-feedback de Claudemberg (avaliador técnico):** deleguei a Mascaró uma 2ª pesquisa (percentual de custo sobre VGV + investigação da "malandragem" de R$/m² crescente com área/padrão), aguardei o resultado real, conferi contra o resumo do coordenador antes de integrar, e reescrevi as Seções 3.1 (nova) e 6 (comparativo com as 2 vias lado a lado) sem apagar a 1ª via — mantive a leitura de que a via mais realista para decisão é a 2ª (% VGV), com a 1ª (CUB) como piso de referência.

**Mascaró (Agente, custo de obra):**
- **1ª rodada:** buscou e leu diretamente (WebFetch + Read) o PDF oficial do Sinduscon-Rio, Agosto/2026, confirmando de forma independente R-1 Normal e R-1 Alto. Interpolou linearmente para aproximar "médio-alto" (categoria que não existe oficialmente), declarando isso como aproximação, não categoria oficial. Sinalizou 2 ressalvas fortes por conta própria: R-1 é térrea (programa é sobrado, custo provavelmente subestimado) e o CUB não inclui fundação/projetos/impostos/remuneração. Entregou os 2 valores de custo (1ª via, CAB e CAM) usados nas Seções 2 e 3.
- **2ª rodada (rework):** buscou e achou fonte real (TBO, consultoria de viabilidade imobiliária) para percentual de custo de obra sobre VGV (40-55%), com reforço fraco de uma matéria da CBIC. Aplicou essa faixa aos valores de revenda do Fiker, gerando a 2ª via de custo (Seção 3.1). Investigou a "malandragem" de R$/m² de custo crescente com área/padrão — não achou fonte formal do lado do custo, declarou lacuna explícita, e trouxe apenas um sinal indireto do lado da revenda (não confundido com dado de custo). Comparou as 2 vias e concluiu convergência de direção (1ª via subestima) com divergência de magnitude (2ª via é 1,2x-2,5x maior).

**Fiker (Agente, valor de mercado):**
- Buscou comparáveis reais filtrados por tipo+padrão+metragem para os dois cenários, sem extrapolar média de bairro.
- Confirmou individualmente 3 comparáveis para o CAB (MGF Imóveis) e 1 para o CAM (Azuza Imóveis, Alphaville Barra).
- Declarou com transparência que o comparável do CAM é único (amostra fraca), registrando um 2º sinal de mercado (não usado como número) e as fontes que bloquearam o fetch (VivaReal, ZAP, Realiza).
- Entregou as 2 faixas de valor de revenda usadas na Seção 4.

---

## 9. Achados/Ressalvas que exigem decisão de Claudemberg

1. **OODC não calculável no valor final** (Seção 5) — só é resolvível com RIU real e leitura do Anexo XVII (LC 270/2024). Isso é uma lacuna estrutural do ensaio (lote fictício), não um erro de processo — mas precisa ficar explícito para quem for auditar o documento como se fosse caso real.
2. **Amostra de revenda do cenário CAM é fraca** (1 comparável direto) — se este fosse caso real, eu recomendaria a Fiker buscar mais fontes (outro portal, ou acesso a ferramenta de scraping/API que ele já sinalizou não ter) antes de apresentar a faixa ao cliente como definitiva.
3. **Custo de obra de ambos os cenários usa proxy térrea (R-1) para um programa de sobrado** — subestimativa provável nos dois lados, sem percentual de correção citável hoje. Fica como pendência técnica aberta por Mascaró.
4. **Pressão de prazo do CAM não tem prazo de referência conhecido para a etapa de OODC junto à SMU** — não deve ser presumida rápida; se isso for relevante para a decisão do cliente, vale uma consulta específica a Kelsen/Hely sobre prazo médio real desse trâmite.
5. **Divergência de artigo (Art. 94 vs Art. 106) sobre a base legal da OODC**, já registrada por Hely no documento legal e não resolvida — não é matéria minha, mas repito o sinal para não se perder entre etapas.
6. **2ª via de custo (% sobre VGV) usa fonte de mercado (TBO), não institucional** — Sinduscon-Rio e CBIC não publicam essa composição percentual de forma aberta nas buscas feitas por Mascaró. É fonte citável e coerente com o reforço fraco da CBIC, mas não tem o mesmo peso de fonte primária oficial que o CUB (Seção 2/3). Se este fosse caso real, valeria buscar mais de uma fonte institucional antes de apresentar a faixa 40-55% ao cliente como definitiva.
7. **"Malandragem" (custo de obra por m² crescente com área/padrão) segue sem fonte formal do lado do custo** — só há sinal indireto do lado da revenda (comparáveis do Fiker). Nenhum ajuste extra foi aplicado à 2ª via por causa disso; se Claudemberg quiser testar essa hipótese com mais rigor, precisaria de fonte específica de custo de construção por faixa de metragem, que Mascaró não encontrou nesta pesquisa.
8. **Com a 2ª via, a margem bruta do CAB ficou mais sensível ao ponto da faixa (piso R$975 mil, teto R$3,9M)** — a folga financeira do CAB parecia maior só com CUB; vale o cliente entender que a margem pode ser mais apertada que a 1ª leitura sugeria, dependendo de onde o custo real cair dentro da faixa 40-55%.
