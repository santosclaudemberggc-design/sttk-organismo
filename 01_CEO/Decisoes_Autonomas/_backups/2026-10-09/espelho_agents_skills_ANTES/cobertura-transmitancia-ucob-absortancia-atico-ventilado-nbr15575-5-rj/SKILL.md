---
name: cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj
description: Desempenho térmico da cobertura (laje, telhado, ático) em residência no Rio, pelo procedimento simplificado da NBR 15575-5. Cobre o limite de transmitância (Ucob) em função da cor/absortância da telha, o fator de correção FT que premia o ático ventilado pelos beirais (e pune abertura pequena demais), a exigência de emitância para telha metálica, a ponderação de coberturas mistas e o aviso do IPT de que, no clima quente, cobertura sem isolante tende a reprovar na simulação mesmo passando no simplificado. Use sempre que Lúcio/Oscar for definir tipo de cobertura, cor de telha, laje impermeabilizada exposta, beiral, forro ou isolamento no Estudo Preliminar/Anteprojeto, mesmo que o pedido só mencione "telhado", "laje de cobertura", "calor no último andar", "telha sanduíche", "manta térmica" ou "ático", sem citar a norma pelo nome.
version: v1.1
status: ativa-com-ressalva
fonte_primaria_lida: "Projeto de Emenda ABNT NBR 15575-5 (CB-002, mar/2021, sem valor normativo), item 11, Tabela 5 e equação de FT; artigo IPT (Revista IPT v.1 n.6, dez/2017) lido inteiro"
data: 2026-10-01
validacao: "Lúcio (Gestor dono), 01/10/2026, Passo 4.2: PROCEDE COM RESSALVA (R1-R5, seção 9). Tabela 5, FT, emitância, ponderação e tabela de FT conferidas contra o texto: corretas. Corrigido: IPT dizia que U 2,02 'passa no simplificado' (o artigo diz o contrário); envelope das duas colunas anula o FT fora de 0,4 < α ≤ 0,6; macetes sem fonte lida retirados. Coerência: complementa nbr15575-4-emenda2025, nbr15220-3 e nbr9575; diferente de vidro-fachada-poente. Sem contradição real com a 15220-3 (prescrição × desempenho)."
changelog:
  - "v1.0 (01/10/2026, Wallenberg): proposta."
  - "v1.1 (01/10/2026, Lúcio): §4 corrigido (cobertura I do IPT já não atende no simplificado; cidade da simulação não explicitada); §3 ganhou o efeito do envelope sobre o FT; §5 sem os 2 macetes sem fonte lida; §1 e §7 ajustados; seção 9 de ressalvas."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar (projeto arquitetônico)
agentes_cross: Baumgart (laje e peso do isolante), Glaziou (cobertura verde como alternativa), Tenreiro (forro), Saturnino (impermeabilização sobre isolante — ver nbr9575)
---

# Skill: Cobertura no Rio: transmitância (Ucob), cor da telha e ático ventilado (NBR 15575-5, procedimento simplificado)

> ⚠️ RESSALVA DE FONTE. (1) **Texto lido:** o **Projeto de Emenda 1 da ABNT NBR 15575-5** (CB-002, março/2021), publicado pelo LabEEE/UFSC. O cabeçalho do documento diz "**NÃO TEM VALOR NORMATIVO**". O texto final publicado da NBR 15575-5:2021 (paga) **não foi lido**. Trate a Tabela 5 e a equação do FT como "texto provável da norma, a confirmar". (2) **Zona bioclimática:** a Tabela 5 usa as **8 zonas antigas**, e nelas o Rio era **ZB 8**. A NBR 15220-3:2024 passou a 12 zonas (Rio: indício de 4A, não confirmado, ver `nbr15220-3-bioclimatica-rj`). **Não se sabe** se a Emenda 2025 da NBR 15575 reescreveu esta tabela para 12 zonas nem em qual coluna o Rio cai agora. Até confirmar, Oscar calcula **pelas duas colunas** (seção 3) e adota a mais exigente. Isso é **premissa conservadora de projeto, não comprovação de conformidade**: a Emenda 2025 pode ter números diferentes para a zona nova. (3) O estudo do IPT simulou clima de **ZB 8** com a NBR 15575 versão **2013** (a seção 2.2 do artigo não nomeia a cidade; a única cidade de ZB 8 citada no artigo é Manaus). Serve como alerta de tendência, não como número para o Rio. (4) A Skill `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj` (§4, fonte secundária, a confirmar) diz que a Emenda 2025 tornou a simulação obrigatória para obra nova. Se isso se confirmar, o simplificado desta Skill vira **pré-dimensionamento**, não verificação final.

## 1. POR QUE ESSA SKILL EXISTE

A Skill `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj` deixou a linha "U cobertura ≤ x — **Confirmar na Emenda ABNT 2025**" em aberto (§ Coberturas) e afirma que a cobertura é o elemento de maior ganho de calor no Rio. Esta Skill preenche esse "x" **provisoriamente** com o texto do projeto de emenda (ressalva 1). Também mostra uma brecha pouco usada, válida só em parte enquanto a zona não for confirmada (seção 3): **a abertura do beiral pode aumentar o limite permitido de Ucob**.

## 2. A REGRA (Projeto de Emenda NBR 15575-5, item 11)

- O procedimento simplificado da cobertura só verifica o **nível Mínimo** (obrigatório). Os níveis **Intermediário e Superior** exigem **simulação** (NBR 15575-1:2021, item 11.4).
- A avaliação é feita **por ambiente de permanência prolongada (APP)**: sala e quartos. Se um APP falhar, a unidade vai para simulação.
- O simplificado da cobertura é **complementado** pela avaliação das paredes (NBR 15575-4:2021, Seção 11), as duas juntas.

**Tabela 5 (Ucob de referência, W/(m²·K)):**

| Zonas | Condição | Ucob máximo |
|---|---|---|
| ZB 1 e 2 | qualquer | ≤ 2,30 |
| ZB 3 a 6 | αcob ≤ 0,6 | ≤ 2,3 |
| ZB 3 a 6 | αcob > 0,6 | ≤ 1,5 |
| **ZB 7 e 8** | **αcob ≤ 0,4** | **≤ 2,3 × FT** |
| **ZB 7 e 8** | **αcob > 0,4** | **≤ 1,5 × FT** |

- **αcob** = absortância solar da face externa da cobertura. A norma recomenda considerar a **degradação** da superfície (NBR 15575-1:2021, item 11.2): telha clara que escurece com o tempo perde a vantagem.
- **Telha metálica** (com ou sem pintura), ZB 3 a 8: a face externa precisa de **emitância térmica > 0,7**, comprovada por **laudo técnico**.
- Passou do limite → **simulação** obrigatória (NBR 15575-1:2021, item 11.4).
- **Cobertura mista:** a Ucob equivalente é a média das Ucob ponderada pela **área de projeção horizontal** de cada trecho. A absortância equivalente é ponderada pela área de cada pintura ou telha.

## 3. O FATOR FT: A BRECHA DO ÁTICO VENTILADO (e a armadilha)

**FT = 1,17 − 1,07 · h^(−1,04)**, onde **h** é a **altura da abertura em dois beirais opostos, em centímetros**. Para **cobertura sem forro ou ático não ventilado, FT = 1**.

Valores calculados pela fórmula (conta de Wallenberg, refeita por Lúcio em 01/10/2026: confere em todas as linhas; FT = 1 em h ≈ 5,86 cm):

| h (cm) | FT | Efeito no limite |
|---|---|---|
| 2 | 0,65 | **piora 35%** |
| 4 | 0,92 | piora 8% |
| **≈ 5,9** | **1,00** | **neutro** |
| 10 | 1,07 | +7% |
| 20 | 1,12 | +12% |
| 30 | 1,14 | +14% (o teto é 1,17) |

- **Brecha válida (na coluna ZB 7-8):** ático ventilado com abertura de beiral de 10 a 20 cm em **dois lados opostos** dá de 7% a 12% de folga no limite de Ucob.
- **Armadilha:** abertura **menor que ~6 cm** dá FT < 1. Na conta, "ventilar pouco" fica **pior** do que declarar ático fechado. Oscar desenha a fresta do beiral **com cota**, nunca "beiral ventilado" genérico.
- O FT **só existe na coluna ZB 7-8**. Enquanto a zona não for confirmada, vale o **envelope** (menor limite entre as colunas ZB 3-6 e ZB 7-8), e nele o FT **só ajuda numa faixa de cor**:

| Absortância αcob | Limite pelo envelope | O FT ajuda? |
|---|---|---|
| ≤ 0,4 | 2,3 × FT se FT < 1; senão 2,3 | **Não**, só pune fresta < 6 cm |
| > 0,4 e ≤ 0,6 | 1,5 × FT (h = 10 cm → 1,61; h = 20 cm → 1,68) | **Sim** |
| > 0,6 | 1,5 × FT se FT < 1; senão 1,5 | **Não**, só pune fresta < 6 cm |

  Em memorial, não conte com a folga do FT fora da faixa 0,4-0,6 até a zona sair confirmada (ressalva 2).

## 4. O AVISO DO IPT: PASSAR NO SIMPLIFICADO NÃO É GARANTIA

Brito, Salles, Vittorino, Aquilino e Akutsu (IPT, Revista IPT v.1 n.6, dez/2017) simularam 21 sistemas construtivos (7 paredes × 3 coberturas) em clima de ZB 8, pela NBR 15575:2013, com janelas sombreadas e 5 renovações de ar por hora. A cobertura base era telha cerâmica + ático de ~40 cm + forro de gesso, com α = 0,65:

- **Sem isolante na cobertura (U = 2,02):** **nenhuma** das paredes testadas atingiu o nível Mínimo **na simulação**. (Essa cobertura, com α = 0,65, **já não atendia o simplificado**, segundo o próprio artigo, p. 28.)
- **O desencontro simplificado × simulação** que o IPT aponta é nas **paredes**: os sistemas H, I, J, K, O e R passam no simplificado e falham na simulação (Tabela 3 do artigo). A lição vale para a cobertura também: o simplificado é um filtro grosso.
- **Com 5 cm de isolante (U = 0,57):** atende o Mínimo com paredes de **capacidade térmica de 140 a 200 kJ/(m²·K)**.
- **Com 10 cm de isolante:** atende também com paredes leves mais isolantes (U = 0,68).
- Os autores **propõem** (proposta de aprimoramento, não texto de norma), para ZB 8, Ucob máximo **da ordem de 0,6**, e que o método simplificado só valha para ambientes com até **15% de área envidraçada sobre a área de piso**.
- O mesmo artigo (p. 23) avisa que, em clima quente, isolante usado sem critério também **segura o calor interno**. O resultado favorável veio com isolante **na cobertura**, junto com paredes adequadas, não de "isolar tudo".

**Consequência para Oscar:** em casa de alto padrão na Barra/Recreio (pano de vidro maior que 15% e laje exposta), o simplificado tende a **não ser o caminho real**. Planeje a simulação e trate o isolante de cobertura como **premissa recomendada do partido**, não como item de corte de orçamento. **Não é exigência prescritiva**: nem o texto lido da NBR 15575-5 nem a Skill `nbr15220-3-bioclimatica-rj` (linha 30, "isolamento em cobertura não obrigatório") obrigam isolante; o que obriga é passar no limite de Ucob e, se for o caso, na simulação. Não há contradição: lá é prescrição, aqui é desempenho.

## 5. MACETES DE QUEM FAZ

- **O FT é conta, o isolante é desempenho.** O FT premia a ventilação do ático **no simplificado**. Na simulação do IPT, o que levou ao Mínimo foi o **isolante** (5 a 10 cm sobre o forro); o ático de ~40 cm sem isolante não bastou com nenhuma parede (Brito et al., 2017, p. 28). E com cobertura bem isolada, a cor da telha pesa pouco (mesmo artigo, p. 31). Use o FT para o simplificado **e** planeje o isolante para a simulação.
- **Cor: número, não nome.** O IPT **propõe** (não é norma) usar **α = 0,5** como "cor média" nas ZB 1 a 7, e classifica clara α ≤ 0,3, média 0,3-0,7, escura α ≥ 0,7 (Brito et al., 2017, p. 30-31). Como a Tabela 5 muda de linha em 0,4 e 0,6, o memorial traz a absortância de catálogo ou laudo, nunca "telha cinza claro".

## 6. CHECKLIST DE OSCAR

- [ ] Zona do projeto confirmada? (até confirmar: calcular pelas colunas ZB 7-8 e ZB 3-6 e adotar a mais exigente)
- [ ] Absortância da telha ou laje com fonte (catálogo/laudo), considerando o envelhecimento
- [ ] Telha metálica? → laudo de emitância > 0,7
- [ ] Ático ventilado? → cota da abertura **h** nos **dois beirais opostos**, h ≥ 10 cm (nunca < 6 cm)
- [ ] Ucob calculada (NBR 15220-2) e ponderada por área se a cobertura for mista
- [ ] Área envidraçada > 15% do piso, ou laje exposta sem isolante? → planejar **simulação** (NBR 15575-1, item 11.4) desde o Estudo Preliminar
- [ ] Isolante na cobertura: espessura e posição compatíveis com a impermeabilização (Skill `nbr9575-impermeabilizacao`) e com a carga da laje (Baumgart)

## 7. RELAÇÃO COM OUTRAS SKILLS

- **`nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj`**: **complementa**. Lá ficam as paredes, a regra geral da Emenda 2025 e a simulação. Aqui fica o número da cobertura que lá estava "a confirmar". **Leitura correta da absortância de lá (linhas 79-80):** na Tabela 5, αcob **não é limite isolado**; ela escolhe a linha do limite de Ucob (α > 0,6 é permitido com Ucob ≤ 1,5). Remissão de volta a ser gravada lá.
- **`nbr15220-3-bioclimatica-rj`**: **complementa**, e é a dona da zona do Rio (ressalva 2). A linha 30 de lá ("isolamento não obrigatório") é prescrição; o aviso do IPT aqui é desempenho (seção 4). Não se contradizem.
- **`vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj`**: **diferente**. Vidro e INI-R lá, cobertura e NBR 15575-5 aqui. O limite de 15% de vidro do IPT (proposta, NBR 15575) **não é** a referência de ~17% da INI-R de lá: métodos distintos, não somar.
- **`nbr9575-impermeabilizacao`**: **complementa**. Lá fica a sequência de camadas da cobertura plana com "isolamento térmico (se aplicável)" (linha 29) e o peso do sistema (linha 39); aqui fica quando o isolante é aplicável e por quê.

## 8. FONTES

- ABNT/CB-002, Projeto de Emenda 1 ABNT NBR 15575-5 (mar/2021), sem valor normativo, item 11, Tabela 5 e equação do FT: https://labeee.ufsc.br/sites/default/files/documents/P_ABNTNBR15575_5_2020CNGPR_PosCN_SiteLabEEE.pdf (texto extraído com pypdf em 01/10/2026)
- Brito, A. C.; Salles, E. M.; Vittorino, F.; Aquilino, M. M.; Akutsu, M. "Avaliação de desempenho térmico de habitações segundo a norma ABNT NBR 15575: proposta para aprimoramento do método simplificado". Revista IPT, v.1, n.6, dez/2017: https://revista.ipt.br/revistaIPT/pt_BR/article/view/49/54
- Retirados na v1.1 (sem leitura do original, regra "macete sem fonte não entra"): síntese de busca sobre ventilação de ático sem isolante (revista.ipt.br, artigo 64/75) e vídeo da arq. Talita Catelani citado pelo TNH1 (não assistido). Se alguém ler/assistir, podem voltar como macete.

## 9. RESSALVAS DE ATIVAÇÃO (validação Lúcio, 01/10/2026)

- **R1.** Fonte é projeto de emenda sem valor normativo. Antes de memorial de cliente, confirmar Tabela 5 e FT no texto publicado da NBR 15575-5 e na Emenda 2025 (Hely, via Kelsen, ou norma comprada).
- **R2.** Zona: o envelope das duas colunas é premissa de projeto, não prova de conformidade. Fora de 0,4 < α ≤ 0,6, não usar folga de FT (seção 3).
- **R3.** Se a Emenda 2025 exigir simulação para obra nova (Skill 15575-4, §4, a confirmar), esta Skill é pré-dimensionamento.
- **R4.** Números do IPT: ZB 8, NBR 15575:2013, proposta dos autores. Tendência, não limite.
- **R5.** Isolante: premissa recomendada, não exigência prescritiva. Espessura e posição passam por Saturnino/nbr9575 (camadas) e Baumgart (carga).
