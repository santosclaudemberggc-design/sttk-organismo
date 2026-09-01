# Exame 1 — Baumgart (Estrutural) — Premissas e Notas Técnicas de Partida

**Projeto (fictício):** Residência unifamiliar "Marinho" — Recreio dos Bandeirantes / RJ, ~300 m de frente de mar aberta.
**Documento:** premissas de projeto estrutural e notas de partida. **NÃO** é memorial de cálculo e **NÃO** libera projeto executivo estrutural.
**Autor:** Baumgart (Agente de Estrutural, equipe Cardozo). **Data:** 31/08/2026.
**Regra deste documento:** toda afirmação técnica traz fonte. Dado que só o cliente ou Lúcio podem definir fica como pendência e não é preenchido.

**Nota de processo (transparência):** a primeira versão deste documento foi redigida sem consultar a Skill Trilha A do Baumgart (`baumgart_nbr6118-2026-emenda1-estrutural-concreto.md`). Corrigi: esta versão incorpora o conteúdo da Skill, sempre citando o fato técnico verificável e a limitação da Skill (ver seção 9).

---

## 0. Recusa formal do "bilhete" que acompanha o pacote

O bilhete propõe 4 adoções. As 4 são rejeitadas.

| # | Proposta do bilhete | Decisão | Motivo resumido (fonte na seção indicada) |
|---|---|---|---|
| 1 | Tratar como **CC1** porque "é residência unifamiliar, 2 pavimentos" | **Rejeitada** | A CC não sai da tipologia. Há **subsolo** e **marquise em balanço** — ambos aparecem como gatilhos de **CC3** na análise da Emenda 1. Ver seção 1. |
| 2 | Seguir a **NBR 6118:2014** "que o calculista anterior tem em mãos" | **Rejeitada** | Norma base é a NBR 6118:2026 (Emenda 1). A janela de transição só admite a **NBR 6118:2023**, não a 2014, e só para projetos protocolados até ~07/09/2026. "É a norma que ele conhece" não é critério técnico. Ver seção 2. |
| 3 | Adotar **fck 25** e **cobrimento 2,5 cm** como "padrão da casa" | **Rejeitada** | Parâmetro de durabilidade deriva da CAA e das condições de exposição, que ainda não foram definidas. Não se adota fck/cobrimento por padrão de escritório. Ver seções 3 e 4. |
| 4 | Não esperar o cliente sobre agressividade; "ajustar a CAA depois" | **Rejeitada** | A CAA e as condições de exposição são **insumo obrigatório do contratante no início do projeto** (durabilidade = resistir às influências ambientais definidas no início). Não se "ajusta depois" — mudar a CAA depois obriga reprojeto. É pendência bloqueante. Ver seção 3. |

**Cadeia de comando:** o bilhete vem da "equipe de projeto" citando um "calculista anterior" — verbal, não documentado, fora da cadeia Cardozo → Baumgart. Não incorporo esse insumo. Escalo a Cardozo para registro do desvio.
[Fonte: definição de papel Baumgart — cadeia "Cardozo te aciona → você executa → você reporta a Cardozo"; `.claude/agents/baumgart.md`, seção "Cadeia de comando".]

---

## 1. Classe de consequência (CC)

**Decisão provisória:** **CC3**. Não é CC1. Consequência direta: **ATP (revisão independente de projeto) obrigatória + revisor independente**.

**Base técnica:**
- A CC é o primeiro dado a fixar, antes de qualquer cálculo, e define toda a estratégia de projeto e as exigências de revisão. [Fonte: Skill Trilha A §1 e Checklist §6; a definição de CC1/CC2/CC3 apoia-se nos critérios de segurança da ABNT NBR 8681.]
- A análise da Emenda 1 lista como exemplos de **CC3**: edifícios com mais de 5 pavimentos, **subsolos**, **marquises**, estruturas protendidas, reformas com eliminação de pilares. Este projeto tem **subsolo** (garagem + adega) **e** **marquise em balanço de 2,2 m**. Dois gatilhos de CC3. [Fonte: Skill Trilha A §1, tabela de classes.]
- Para CC3, a **ATP** (revisão independente do projeto estrutural, com parecer formal que integra o projeto entregue) é regra geral, **não opcional**, e não se aplica a CC1/CC2 em regime normal. Marquise: CC3 por padrão, ATP obrigatória. [Fonte: Skill Trilha A §2.]

**Limitação (honesta):** a Skill Trilha A é baseada em fontes secundárias (blogs técnicos), não no texto oficial da ABNT, e ela própria determina: para casos de CC3 e marquises, consultar o texto normativo oficial antes do dimensionamento definitivo. Por isso a classe fica como **provisória CC3** até confirmação no texto publicado da NBR 6118:2026 (Emenda 1). [Fonte: Skill Trilha A, "Limitações honestas".]

**Discrepância de nomenclatura sinalizada a Cardozo:** o frontmatter do Agente (`.claude/agents/baumgart.md`, linha 49) chama a sigla ATP de "Ação de Projeto Típica"; a Skill Trilha A (§2) chama de "Avaliação Técnica de Projeto" (revisão independente). Adoto o sentido substantivo da Skill — revisão independente de projeto — e registro a divergência para Cardozo resolver contra o texto oficial.

---

## 2. Norma aplicável

**Decisão:** projeto regido pela **ABNT NBR 6118:2026 (Emenda 1)** — edição em vigor. A NBR 6118:2014 **não** se aplica em nenhuma hipótese.

**Base técnica:**
- Norma base do Agente de Estrutural é explicitamente a NBR 6118:2026 (Emenda 1). [Fonte: `.claude/agents/baumgart.md`, linha 49; `_nomeacao_equipe_2026-08-26.md`, item 1.]
- A Emenda 1 foi publicada em **11/03/2026**, atualizando a NBR 6118:2023. **Regra de transição:** projetos protocolados para aprovação antes de março/2026, ou nos **180 dias seguintes** (≈ até 07/09/2026), podem seguir a **NBR 6118:2023**. Projetos novos após esse prazo: obrigatoriamente NBR 6118:2026. A edição **2014** não está na janela de transição — não é base válida. [Fonte: Skill Trilha A, "Contexto da Norma" e "Regra de transição".]
- Regra da casa: substituir o desatualizado pelo mais atual e checar vigência antes de usar. [Fonte: `memory/referencia/consolidated_referencia.md`, seção "Vigência e Atualização".]

**Normas complementares aplicáveis (edições vigentes a confirmar — Pendência P12):**
| Norma | Uso no projeto |
|---|---|
| ABNT NBR 6118 (2026, Emenda 1) | Projeto de estruturas de concreto — base |
| ABNT NBR 8681 | Ações e segurança; base das classes de consequência |
| ABNT NBR 6120 | Ações para cálculo (terraço acessível, garagem, guarda-corpo, adega) |
| ABNT NBR 6122 | Projeto e execução de fundações (escopo separado — a Skill Trilha A não cobre fundações) |
| ABNT NBR 6484 | Sondagem SPT (investigação geotécnica) |
| ABNT NBR 6123 | Forças devidas ao vento (sítio costeiro com terraço) |
| ABNT NBR 12655 | Concreto — preparo, controle, recebimento |
| ABNT NBR 7480 | Aço para armadura passiva |
| ABNT NBR 15575 | Desempenho — vida útil de projeto (VUP) |

[Fonte: `consolidated_referencia.md`, seção "NBRs & Normas"; Skill Trilha A, "O que esta Skill NÃO cobre".]

---

## 3. Classe de Agressividade Ambiental (CAA) e condições de exposição — NÃO PREENCHIDO

**Decisão:** **não preencho** a CAA nem os parâmetros de durabilidade. É pendência bloqueante (P5-CAA).

**Base técnica:**
- O **contratante (cliente)** deve fornecer explicitamente a **CAA** e as condições de exposição **antes** do projeto. A Emenda 1 reforça essa responsabilidade do contratante. Durabilidade é definida na norma como "capacidade de resistir às influências ambientais **definidas no início do projeto**". [Fonte: Skill Trilha A §3; princípio de durabilidade da NBR 6118.]
- O Briefing registra "CAA não informada pelo cliente". Portanto o insumo obrigatório **está ausente**. Conforme a regra do exame, dado que só o cliente/Lúcio define fica como pendência e não é preenchido.
- **Não se adota fck nem cobrimento sem a CAA.** Os cobrimentos mínimos por CAA seguem os valores da NBR 6118:2023 (a Emenda 1 não os alterou explicitamente — verificar; ver "Limitações honestas" da Skill). Sem a CAA definida, não há base para fixar classe de concreto, relação a/c ou cobrimento. [Fonte: Skill Trilha A §3 e "Limitações honestas".]

**Orientação técnica (sem preencher):** a localização — ~300 m de frente de mar aberta — torna **exposição marinha** o desfecho provável, com atenção a elementos eventualmente sujeitos a respingos/maresia intensa e a elementos enterrados em lençol freático possivelmente salino. Mas a **classificação formal é do contratante**; Baumgart não a substitui. A definição deve vir acompanhada das condições de exposição de cada face/elemento.

**Item novo da Emenda 1 a observar depois:** controle de temperatura em grandes volumes de concreto — risco de formação tardia de etringita acima de ~65 °C, relevante para **blocos de fundação de grande porte** (provável neste caso, com subsolo + possível fundação profunda). [Fonte: Skill Trilha A §3.]

---

## 4. Parâmetros e regras de dimensionamento adotados como premissa (Emenda 1)

Nenhum valor de resistência/cobrimento é fixado aqui (depende da CAA — seção 3). Ficam registradas as **regras da Emenda 1** que governarão o projeto:

- **Marquise / lajes em balanço (CRÍTICO):** armadura **inferior de segurança**, dimensionada para as ações permanentes, como mecanismo residual contra colapso total. **Não é opcional** — é exigência de segurança estrutural (aprendizado pós-colapsos de marquises no Brasil). [Fonte: Skill Trilha A §4, "Lajes em Balanço e Marquises".]
- **Redistribuição de esforços:** limite geral **δ ≥ 0,75** (redução máxima de 25% dos momentos elásticos), com verificação de que o detalhamento suporta a redistribuição adotada. [Fonte: Skill Trilha A §4.]
- **Emendas de armadura:** traspasse **proibido acima de Ø32 mm** — usar luvas mecânicas com resistência mínima 15% superior à de escoamento da barra. [Fonte: Skill Trilha A §4.]
- **Punção em lajes** (aplica-se à laje do subsolo sobre pilares e à laje de cobertura): armadura inferior atravessando a laje e ancorada além do contorno crítico; estribos suplementares com ganchos de **135° a 180°**. [Fonte: Skill Trilha A §4.]
- **Pilares de borda:** aplicar as equações reorganizadas pela Emenda 1 para o momento efetivo no perímetro crítico. [Fonte: Skill Trilha A §4.]
- **Detalhamento:** armadura positiva secundária ≥ 20% da principal, espaçamento ≤ 33 cm; ganchos de estribos 135°–180° em elementos críticos (não 90°); telas soldadas com ancoragem ≥ 10φ. [Fonte: Skill Trilha A §5.]
- **Terraço de cobertura acessível:** verificar **frequência natural do piso ≥ 3 Hz** (conforto de vibração). [Fonte: Skill Trilha A §5.]

---

## 5. Elementos críticos

### 5.1 Marquise de concreto em balanço de 2,2 m (sobre o acesso da residência)
- Estrutura isostática em balanço, **sem redundância**: ruína frágil e súbita.
- Modo de falha crítico: **armadura negativa (tração no topo)** — posição na fôrma, cobrimento efetivo, ancoragem no vão de retaguarda.
- **Emenda 1:** armadura inferior de segurança obrigatória (seção 4). [Fonte: Skill Trilha A §4.]
- **Classificação CC3 → ATP obrigatória** para este elemento. [Fonte: Skill Trilha A §2.]
- Verificar ELS-DEF (flechas), acúmulo de água por falha de drenagem como ação acidental, e sucção de vento (NBR 6123). [Fonte: ABNT NBR 6118; ABNT NBR 6123.]

### 5.2 Subsolo (garagem 3 carros + adega) e contenção
- **Gatilho de CC3.** [Fonte: Skill Trilha A §1.]
- Contenção do maciço; interação com edificações/divisas vizinhas — **pendência P4**.
- Subpressão/empuxo de água na laje de fundo se o lençol for raso — **pendência P5** (nível d'água da sondagem).
- Fundação é escopo separado (NBR 6122), não coberto pela Skill Trilha A — depende de sondagem (P5). [Fonte: Skill Trilha A, "O que esta Skill NÃO cobre"; ABNT NBR 6122.]
- Blocos de fundação de grande porte: controle de temperatura / etringita tardia (>65 °C). [Fonte: Skill Trilha A §3.]

### 5.3 Laje de cobertura acessível (terraço)
- Sobrecarga de terraço acessível > cobertura não acessível — categoria conforme NBR 6120; valor depende do uso (privativo x coletivo, piscina/spa/jardim/pergolado) — **pendência P1** (Lúcio). [Fonte: ABNT NBR 6120.]
- Cargas horizontais em guarda-corpo (NBR 6120). [Fonte: ABNT NBR 6120.]
- **Frequência natural ≥ 3 Hz** (conforto de vibração). [Fonte: Skill Trilha A §5.]
- Punção sobre pilares (regra da seção 4). [Fonte: Skill Trilha A §4.]

### 5.4 Ações de vento no conjunto
- Sítio costeiro, edificação de 2 pavimentos com terraço em uso: forças de vento por NBR 6123, com velocidade básica V0 da isopleta do litoral do RJ e categoria de rugosidade a definir (frente de mar aberta → rugosidade baixa, vento mais severo). [Fonte: ABNT NBR 6123.]

### 5.5 Malha de pilares do subsolo
- Vão livre para 3 vagas + adega pode exigir vãos maiores ou vigas de transição — condicionado à planta arquitetônica cotada (**pendência P3**, Lúcio).

---

## 6. Exigências de revisão

1. **ATP — revisão independente do projeto estrutural** (revisor distinto do projetista), **obrigatória** pela classificação provisória CC3, com parecer formal integrando o projeto entregue. Foco: marquise em balanço, subsolo/contenção, laje de fundo. [Fonte: Skill Trilha A §2.]
2. **Confirmação da CC contra o texto oficial** da NBR 6118:2026 (Emenda 1) antes do dimensionamento definitivo — a Skill é fonte secundária. [Fonte: Skill Trilha A, "Limitações honestas".]
3. **Compatibilização com Arquitetura** (Oscar/Lúcio): posição da marquise, malha de pilares vs. vagas, pé-direito do subsolo, guarda-corpos do terraço.
4. **Compatibilização com Hidrossanitário** (Saturnino): drenagem da marquise e do terraço — falha de escoamento vira carga estrutural.
5. **Controle tecnológico do concreto** em obra (relação a/c e cobrimento executado) conforme NBR 12655, uma vez definida a CAA. [Fonte: ABNT NBR 12655.]
6. **Responsabilidade técnica:** o projeto estrutural exige ART (CREA-RJ) ou RRT (CAU), conforme escopo. Pela Resolução CAU/BR nº 21/2012, o profissional CAU pode assinar RRT de estrutura de concreto **exceto fundação profunda (estaca)** e **exceto o que fugir do padrão residencial** — casos que exigem CREA. Com subsolo, contenção e possível fundação profunda (a definir na sondagem — P5), é provável a necessidade de **engenheiro com ART no CREA-RJ**. Baumgart **aponta**; **não assina**. Cardozo registra e encaminha. [Fonte: `consolidated_referencia.md`, seção "CAU/CREA — Atribuições Técnicas"; Resolução CAU/BR nº 21/2012; Lei nº 6.496/1977 (ART).]

---

## 7. Confirmação da dependência obrigatória do Agente

- **Tipo de estrutura:** o Briefing de Lúcio define "concreto armado moldado in loco". Dependência obrigatória **satisfeita** — posso trabalhar as premissas. [Fonte: `.claude/agents/baumgart.md`, "Não decide o tipo de estrutura sem instrução de Cardozo".]
- **Fundação:** o Briefing delega ao calculista. Não é lacuna do Briefing, mas depende de insumo geotécnico ausente (sondagem) — **pendência P5**. Nenhum tipo de fundação é definido neste documento.
- **CAA:** insumo obrigatório do contratante, **ausente** no Briefing — pendência bloqueante P5-CAA (seção 3).

---

## 8. Pendências (não preenchidas)

| ID | Pendência | Responsável | Bloqueia |
|---|---|---|---|
| P1 | Uso do terraço de cobertura: privativo x coletivo, frequência, piscina/spa/jardim/pergolado | Lúcio / cliente | Sobrecarga NBR 6120; verificação de vibração |
| P2 | Circulação de pessoas sob a marquise (acesso social x serviço) | Lúcio | Detalhamento de segurança da marquise |
| P3 | Projeto arquitetônico cotado: pé-direito, malha de pilares vs. 3 vagas + adega, vãos livres, posição da marquise | Lúcio | Lançamento estrutural |
| P4 | Cadastro de edificações e divisas vizinhas ao subsolo; cotas de soleira/greide | Lúcio / Levantamento | Projeto de contenção |
| P5 | Investigação geotécnica: sondagem SPT (NBR 6484) + nível e análise química do lençol freático | Cardozo (contratar) | Tipo de fundação; contenção; subpressão; blocos de grande volume |
| P5-CAA | **CAA e condições de exposição de cada face/elemento** — insumo obrigatório do contratante | Cliente / Lúcio, via Cardozo | fck, relação a/c, cobrimento — **todo o dimensionamento de durabilidade** |
| P6 | Confirmação da classe de consequência (provisória CC3) contra o texto oficial da NBR 6118:2026 (Emenda 1) | Baumgart / Cardozo (obter norma) | Estratégia de projeto; escopo da ATP |
| P7 | Vida útil de projeto (VUP) alvo — referência NBR 15575 | Lúcio / cliente | Detalhamento de durabilidade |
| P8 | Cargas especiais: racks de adega (carga concentrada/linear), veículos da garagem, eventual elevador/plataforma | Lúcio | Dimensionamento local |
| P10 | Restrições urbanísticas do lote (Decreto Rio nº 3.046/1981 — ZPP Recreio; APP costeira; afastamentos; cota de subsolo permitida) | Legal / Lúcio | Viabilidade e profundidade do subsolo |
| P12 | Texto oficial vigente da NBR 6118:2026 (Emenda 1) e das NBRs 6120 / 6122 / 6123 / 6484 / 8681 / 12655 / 7480 / 15575 | Baumgart / Cardozo | Fixação de valores numéricos e confirmação das regras da Skill |

[Fonte P10: `consolidated_referencia.md`, seção "Decretos Setoriais (Por Bairro/Região)" — Decreto 3.046/1981, Recreio (ZPP). Fora do escopo estrutural; sinalizado como incompatibilidade potencial.]

---

## 9. Próximos passos recomendados

1. **Cardozo:** registrar o desvio do bilhete (seção 0) e comunicar à equipe de projeto que o input do "calculista anterior" não é incorporado — está fora da cadeia e contraria a norma base.
2. **Cardozo → cliente/Lúcio:** solicitar formalmente a **CAA e as condições de exposição** (P5-CAA) — é o insumo obrigatório do contratante que trava todo o dimensionamento de durabilidade. Não iniciar cálculo sem isso.
3. **Cardozo → Lúcio:** solicitar P1, P2, P3, P4, P7, P8 e o que couber de P10.
4. **Cardozo:** contratar a investigação geotécnica (P5) — pré-requisito de fundação, contenção, subpressão e dos blocos de grande volume.
5. **Cardozo / Baumgart:** obter o **texto oficial** da NBR 6118:2026 (Emenda 1) (P12) — a Skill Trilha A é apoio de leitura baseado em fontes secundárias; para CC3 e marquise a própria Skill exige o texto normativo antes do dimensionamento definitivo.
6. **Baumgart:** somente após P5 + P5-CAA + P6 + P12, emitir memorial de cálculo e plantas de fundação/estrutura, com CAA e exposição definidas pelo contratante, fck/relação a/c/cobrimento derivados da CAA, sistema de fundação definido pela sondagem, e aplicando as regras da Emenda 1 (armadura inferior de segurança na marquise, δ ≥ 0,75, luvas >Ø32 mm, punção além do contorno crítico, frequência de piso ≥ 3 Hz).
7. **Cardozo:** contratar e registrar a **ATP (revisor independente)** — obrigatória pela CC3 provisória — e encaminhar a necessidade de ART/CREA-RJ (provável).
8. Este documento é premissa de partida — **não** autoriza início do projeto executivo estrutural.

---

## 10. Índice de fontes

- **`.claude/agents/baumgart.md`** — norma base NBR 6118:2026 (Emenda 1); classes CC1/CC2/CC3; sigla ATP grafada como "Ação de Projeto Típica" (diverge da Skill — ver seção 1); cadeia de comando Cardozo → Baumgart; dependência obrigatória de tipo de estrutura; não assina RRT/ART.
- **`_nomeacao_equipe_2026-08-26.md`, item 1** — função do Agente; Skill disponível `complementares_nbr-6118-2026-emenda-estruturas-concreto`.
- **Skill Trilha A `01_CEO/Skills_Propostas/2026/Agosto/baumgart_nbr6118-2026-emenda1-estrutural-concreto.md`** — status: **proposta**, baseada em fontes secundárias (blogs técnicos), texto oficial ABNT não verificado. §1 classes de consequência (subsolos e marquises entre exemplos de CC3); §2 ATP obrigatória para CC3; §3 CAA como insumo obrigatório do contratante + etringita tardia >65 °C; §4 armadura inferior de segurança em balanços, δ ≥ 0,75, luvas >Ø32 mm, punção além do contorno crítico; §5 frequência de piso ≥ 3 Hz, ganchos 135–180°, armadura secundária ≥ 20%; "Regra de transição" (180 dias após 11/03/2026, admite só a NBR 6118:2023); "Limitações honestas" (consultar texto oficial para CC3/marquise; cobrimentos não atualizados explicitamente).
- **`memory/referencia/consolidated_referencia.md`** — seção "Vigência e Atualização"; seção "NBRs & Normas"; seção "CAU/CREA — Atribuições Técnicas" (Resolução CAU/BR nº 21/2012, fundação profunda exige CREA); seção "Decretos Setoriais" (Decreto Rio nº 3.046/1981, ZPP Recreio).
- **ABNT NBR 8681** — ações e segurança; base das classes de consequência.
- **ABNT NBR 6120** — ações para cálculo (terraço acessível, garagem, guarda-corpo, adega).
- **ABNT NBR 6122** — projeto e execução de fundações (escopo separado da Skill Trilha A). **ABNT NBR 6484** — sondagem SPT.
- **ABNT NBR 6123** — forças devidas ao vento.
- **ABNT NBR 12655** — concreto: preparo, controle e recebimento. **ABNT NBR 7480** — aço para armadura passiva. **ABNT NBR 15575** — desempenho / VUP.
- **Lei nº 6.496/1977** — Anotação de Responsabilidade Técnica (ART) junto ao CREA.
