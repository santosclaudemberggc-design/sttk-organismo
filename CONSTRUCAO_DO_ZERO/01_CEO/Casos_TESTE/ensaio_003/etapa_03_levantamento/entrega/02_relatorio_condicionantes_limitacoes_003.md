# Peça 2 — Relatório de Condicionantes e Limitações
## Ensaio Sombra 003, Etapa 03: Levantamento. Família Montenegro Prates (100% FICTÍCIO)

**Executor:** Oscar (Agente, Arquitetura, nível Assisted) | **Auditoria:** Lúcio
**Data:** 06/10/2026 | **Natureza:** ANÁLISE PRELIMINAR. Não é projeto: não há layout, partido nem posição de cômodos. Em caso real, depende do Gate do Maurício.
**Etiquetas:** **(a)** dado do dossiê; **(b)** premissa ou mecanismo do Legal/Viabilidade aprovados ou de Skill (seção citada); **(c)** pendente/lacuna, com quem fornece e quem decide.
**Referencial e aproximação retangular (14,29 × 40,00 m):** os mesmos da Peça 1, §1. Ferramenta: `mcp__vitruvius__revit_status` retornou `Error: No such tool available: mcp__vitruvius__revit_status`. Por isso a peça sai em texto, sem desenho simulado.

**Premissas que herdo e não reinterpreto** (parecer da Etapa 01, §2.2 e §5.2; Kelsen R1–R5) **(b)**: área de cálculo de 571,80 m²; TO de 40%, com projeção máxima de **228,72 m²**; afastamentos de 6,00 m na frente, 2,50 m nas laterais e 5,00 m nos fundos, medidos a partir do muro do Lote 16; 2 pavimentos; altura de 8,50 m da soleira; teto computável de **457,44 m²**; área permeável de **142,95 m²**, em porções de no mínimo 4 m² e 2 m de lado, sem subsolo embaixo; sem subsolo, sem rooftop e escavação de no máximo 1,20 m (piscina até 1,60 m); a edícula computa na ATE e na TO por conservadorismo; só 1 vaga coberta fica fora da TO; preservar as árvores no desenho do acesso; edícula com premissa de demolição; cenários H0/H1.

Uma observação sobre a ERRATA 4.1 do Kelsen: ela registra que o Dec. 3.046 VII (sem balanço de varanda sobre o recuo frontal) vale para multifamiliar e que, na casa unifamiliar, remete ao XI. O ponto "continua em aberto". Até decisão do Kelsen, mantenho a leitura conservadora da R4. A Skill `decreto3046-...` §6 M3 (o XI permite varanda e abrigo de carro no afastamento lateral do térreo) é regra **municipal**. Os 2,50 m do condomínio (5.4 Art. 6º) continuam prevalecendo como o mais restritivo (parecer, regra de comparação e linha 17). **Não uso o M3** **(b)/(c: Kelsen)**.

---

## 1. Acessibilidade do lote e canteiro

- **Único acesso documentado: a frente**, pela Rua das Garças. O lote é de meio de quadra e os fundos dão para a faixa verde **comum** (caso §3; 5.5) **(a)**. Usar a faixa verde para obra ou canteiro exige autorização do condomínio, e nenhum documento a dá **(c: condomínio)**.
- **Entrada de carros.** Tem de atravessar o afastamento frontal (y 0–6,00), onde estão as 3 árvores (caso §3) **(a)**. A locação delas **não consta** (Peça 1, §5). Por isso **não consigo dizer hoje por onde o carro entra**. Só digo a regra: o acesso se posiciona entre as árvores e os elementos da testada (postes, PVs, passeio), que também não constam. O rebaixo de meio-fio só é admitido onde for estritamente necessário, e não se admite rampa ou portão fora do alinhamento (COE Art. 35 §§2º-3º, via Skill de levantamento §4) **(b)**.
- **O que o afastamento frontal admite** (LC 270 Art. 363 §2º I, XII e §3º, no parecer P6): estacionamento descoberto de unifamiliar e rampa com inclinação de até 10% e altura de até 0,50 m **(b)**.
- **Canteiro e garagem de obra.** Depois da demolição da casa e da edícula, o canteiro cabe dentro do lote. A posição depende de três coisas que não constam: (i) a proteção das árvores e de suas raízes no frontal; (ii) a passagem do equipamento de estaca hélice contínua, que é a fundação provável (Skill de fundações §3.3; Villaça v9 §6) e entra pela frente, entre as árvores; (iii) em H1, o uso da faixa de 22–40 m como canteiro **não pode ser presumido**, porque seria ocupação temporária de área em suspenso (parecer §5.2, "NÃO pode assumir") **(c: Kelsen/SMAC)**.
- **Ordem demolição × obra nova.** A demolição da casa tem processo próprio (LC 270 Art. 278 VI; POP-LEGAL-03; parecer T6). Se ela precede a licença da obra nova ou corre junto com ela é a TRAVA aberta do POP-LEGAL-03 §5 (Kelsen R4) **(c: Kelsen)**. A casa nunca foi averbada (5.1), e o parecer §5.4 encaminha a averbação antes da demolição a advogado ou cartório **(c: cliente/advogado)**.

---

## 2. Implantação teórica × real: o envelope

### 2.1 Cenário adotado: H0, 571,80 m²

Conta do parecer §2.3, refeita **(b)**:
- Largura útil = menor largura medida − 2 × afastamento lateral = 14,29 − 2 × 2,50 = **9,29 m**
- Profundidade útil = menor lateral − frontal − fundos = 40,00 − 6,00 − 5,00 = **29,00 m**
- **Envelope = 9,29 × 29,00 = 269,41 m²** (x 2,50–11,79; y 6,00–35,00)
- **Folga de desenho = 269,41 − 228,72 = 40,69 m²**. Equivale a 15,1% do envelope; a projeção máxima ocupa 228,72 / 269,41 = 84,9% dele.
- **Ressalva de aproximação.** O lote não é retângulo (14,30 / 14,29 / 40,00 / 40,02, conforme o 5.2) e não temos os ângulos. O envelope real sai do polígono medido com os vértices locados (complementação T5 da Peça 1). A diferença de área entre o retângulo e o lote real é de 0,20 m² (§5.1 abaixo), mas a forma pode deslocar as linhas de afastamento em centímetros. **Antes do EP, o envelope precisa ser redesenhado sobre o polígono real** **(c)**.

**Conclusão:** em H0, **a projeção máxima de 228,72 m² cabe no envelope** dos afastamentos do condomínio, com **40,69 m² de folga**. Isso deixa margem para variar a forma no EP, mas não para crescer: o teto é a TO, não o envelope (parecer §2.2) **(b)**.

**O que consome os 228,72 m²** (premissas do parecer §5.2, que não reinterpreto) **(b)**:
- tudo o que for coberto, inclusive a garagem;
- a garagem coberta, exceto 1 vaga (LC 270 Art. 350 III): consome (n_vagas_cobertas − 1) × área por vaga. A área por vaga é decisão do EP e não a fixo;
- a edícula, se for mantida: a área dela **não consta no dossiê** (Peça 1, §4). O "~20–30 m²" do exemplo do enunciado é estimativa não documental e não serve de base. A conclusão (§4.1) não depende desse número.

### 2.2 Cenário título: 600,00 m² (só com a divisa regularizada)

- Largura de 15,00 → útil (15,00 − 5,00) × 29,00 = **290,00 m²**. Projeção máxima 0,40 × 600,00 = 240,00 m². Folga 290,00 − 240,00 = **50,00 m²** (parecer §2.2 e §2.3) **(b)**.
- Depende de acordo com o vizinho, retirada do muro ou retificação. **Decisão do cliente com advogado** (Kelsen R1). E falta saber se o condomínio mede a TO sobre 600 ou sobre 571,80 m² (parecer §5.3, item 6) **(c)**.

### 2.3 Cenário H1: APP de 30 m da margem (contingente, não confirmado)

- A faixa entra 30,00 − 12,00 = 18,00 m no lote. Profundidade útil = 40,00 − 18,00 − 6,00 = **16,00 m**, e os 5,00 m de fundos ficam dentro da faixa (parecer §2.4) **(b)**.
- **Envelope H1 = 9,29 × 16,00 = 148,64 m²** (y 6,00–22,00).
- **Contra a projeção máxima:** 228,72 − 148,64 = **80,08 m² a menos**. Em H1, a projeção deixa de ser limitada pela TO e passa a ser limitada pelo envelope.
- **Teto computável:** 2 × 148,64 = **297,28 m²** (parecer §2.4 e §5.1), contra 457,44 em H0: **−160,16 m²**.
- **Redução do envelope:** 269,41 − 148,64 = **120,77 m²**.
- **Contradição do enunciado.** A matriz-exemplo diz "H1 reduz ~150 m² de envelope". As contas aprovadas dão **−120,77 m² de envelope**, **−80,08 m² de projeção possível** e **−160,16 m² de teto computável**. Nenhuma delas é ~150. Uso os três números exatos.
- **Teste do programa (sem redimensionar).** O programa de cerca de 520 m² construídos vem da Etapa 02: 457,44 m² computáveis mais 42,56–62,56 m² não computáveis, uma premissa do Villaça (Mascaró v8 §1) **(b)**. **Em H0, cabe na conta**, desde que no mínimo 520 − 457,44 = 62,56 m² sejam de fato não computáveis. Quem confirma o enquadramento de varanda e garagem é o Kelsen; quem confirma como o condomínio mede é o condomínio (parecer §2.2) **(c)**. **Em H1, não cabe:** faltam **160,16 m²** (Mascaró v8 §1; Villaça v9 §8.3) **(b)**. A redefinição do programa em H1 é decisão do cliente no Briefing, com Lúcio. Eu não a faço.
- H2 (marinha, SPU) e H3 (FMP, INEA) **não são estimáveis** (parecer §2.4) e podem ser maiores ou menores que H1 **(c)**.

---

## 3. Faixas fora do envelope e área permeável

### 3.1 Faixas (H0, aproximação 14,29 × 40,00)

| Faixa | Coordenadas | Conta | Área |
|---|---|---|---|
| Afastamento frontal | x 0–14,29; y 0–6,00 | 14,29 × 6,00 | **85,74 m²** |
| Lateral esquerda | x 0–2,50; y 6,00–35,00 | 2,50 × 29,00 | **72,50 m²** |
| Lateral direita | x 11,79–14,29; y 6,00–35,00 | 2,50 × 29,00 | **72,50 m²** |
| Afastamento de fundos | x 0–14,29; y 35,00–40,00 | 14,29 × 5,00 | **71,45 m²** |
| **Soma fora do envelope** | | | **302,19 m²** |
| Envelope | | 9,29 × 29,00 | 269,41 m² |
| **Total da aproximação** | | 14,29 × 40,00 | **571,60 m²** |

**Fechamento:** 571,60 contra os 571,80 do levantamento dá diferença de **−0,20 m² (0,035%)**. A diferença vem de usar a menor largura (14,29) e a menor lateral (40,00), e é desprezível para conclusões. Área livre se a projeção for máxima: 571,80 − 228,72 = **343,08 m²** (parecer §2.2) **(b)**.

### 3.2 Locação CONCEITUAL dos 142,95 m² permeáveis (H0)

Regras do Legal (parecer §5.2; LC 270 Art. 353 III) **(b)**: porções de **no mínimo 4 m² e 2,00 m de lado**, sem subsolo embaixo. O Art. 353 I recomenda a superfície drenante preferencialmente onde há vegetação (parecer P6) **(b)**.

| Faixa | Aptidão (só regra, sem desenho) |
|---|---|
| Frontal (85,74 m²) | É a área **preferencial** (Art. 353 I), porque tem as árvores. Concorre com a entrada de carros, o caminho de pedestres e, se houver, vagas descobertas (Art. 363 §2º XII) |
| Laterais (2 × 72,50 m²) | Largura de 2,50 m, maior que os 2,00 m mínimos, então as porções são aptas. Concorrem com circulação de serviço |
| Fundos (71,45 m²) | Aptos. Concorrem com piscina e deck (§4.2) |
| Sobra do envelope (40,69 m², se a projeção for máxima) | Pode ser permeável se as porções respeitarem 4 m² e 2 m de lado |

**Folga declarada (H0):** fora do envelope há 302,19 m² e o mínimo é 142,95 m². Portanto **até 302,19 − 142,95 = 159,24 m²** fora do envelope podem ser impermeáveis (acessos, caminhos, piscina, deck, vagas descobertas) sem ferir o mínimo. Ainda há os 40,69 m² do envelope não ocupados como reserva. **Em H0, a permeabilidade não é condicionante crítica.**

**Locação conceitual dos 142,95 m² (H0) — zoneamento, não desenho** *[acrescentado por Lúcio na auditoria, 06/10: o critério 6 do enunciado pede a locação, e a versão de Oscar dava só a aptidão e a folga]*. Duas alternativas, porque a posição da piscina não consta (T10):

| Alternativa | Faixas permeáveis (inteiras, jardim sobre solo natural) | Conta | Total | Folga sobre 142,95 |
|---|---|---|---|---|
| **A** — piscina fora dos fundos (ou demolida) | fundos + lateral esquerda | 71,45 + 72,50 | **143,95 m²** | +1,00 m² |
| **B** — piscina nos fundos | lateral esquerda + lateral direita | 72,50 + 72,50 | **145,00 m²** | +2,05 m² |

- As duas fecham o mínimo **só com faixas inteiras** e folga pequena (1,00 e 2,05 m²). Por isso, **em qualquer alternativa, o frontal precisa manter jardim em torno das 3 árvores** como reserva (Art. 353 I, vegetação preferencial), com área a definir no EP depois da locação (T11).
- Cada faixa lateral tem 2,50 m de largura. Se uma parte dela for pavimentada no sentido do comprimento, a parte permeável restante só conta se mantiver **≥ 2,00 m de lado** (Art. 353 III): no máximo **0,50 m** pavimentado ao longo da faixa. Uma circulação de serviço de 1,20 m numa lateral **desqualifica a faixa inteira** (2,50 − 1,20 = 1,30 m < 2,00 m) e o que ela perder tem de sair do frontal ou da sobra do envelope.
- Todas as porções sem subsolo embaixo (parecer §5.2). Jardim de chuva **não** entra nesta conta até a análise do §3.4. Em H1, ver §3.3: a Alternativa A deixa de existir (fundos dentro da faixa H1).

**Efeito do acesso de veículos no frontal:** consome (largura do acesso) × 6,00 m². Mesmo que o frontal inteiro (85,74 m²) fosse impermeável, ainda sobrariam 159,24 − 85,74 = 73,50 m² de folga. Não fixo a largura do acesso: é EP.

**Efeito da piscina nos fundos:** a piscina **não é área permeável**. A área dela (não consta) sai dos 71,45 m², e as sobras dos fundos só contam se tiverem 2,00 m de lado. Exemplo de regra: se a piscina deixar uma faixa de 1,50 m até a divisa, essa faixa **não conta**.

**Padrão de superfície.** Jardim e gramado sobre solo natural atendem à regra sem dúvida aparente. Se **brita, piso drenante ou grelha de concreto com grama** contam como superfície drenante para a SMDU e para o condomínio, eu não decido **(c: Kelsen)**. Até lá, conto como permeável só o jardim sobre solo natural.

### 3.3 O que muda em H1

| Zona | Conta | Área |
|---|---|---|
| Faixa H1 (y 22,00–40,00) | 14,29 × 18,00 | **257,22 m²** |
| Frontal | 14,29 × 6,00 | 85,74 m² |
| Laterais até y 22,00 | 2 × 2,50 × 16,00 | 80,00 m² |
| Envelope H1 | 9,29 × 16,00 | 148,64 m² |
| Soma | | 571,60 m² |

- **Se a APP vegetada contar como permeável:** só a faixa H1 (257,22 m²) já supera os 142,95 m².
- **Se não contar:** fora do envelope, até y 22,00, sobram 85,74 + 80,00 = **165,74 m²**. Folga de 165,74 − 142,95 = **22,79 m²** para **todos** os acessos e caminhos, com o envelope H1 inteiramente ocupado. Um acesso de veículos que atravesse o frontal consome largura × 6,00 m², e com **largura ≥ 22,79 / 6,00 = 3,80 m a folga acaba**. A partir daí, a projeção teria de ficar abaixo do envelope H1 para abrir área permeável. **É risco real de desenho em H1.**
- **Quem decide se APP vegetada conta como permeável: Kelsen**, à luz da resposta da SMAC. **Não decido.**
- Piscina ou deck na faixa H1: **não pode ser presumido**. Seria intervenção em área de proteção (LC 281 Art. 22 III, no parecer P2; parecer §5.2) **(c: Kelsen/SMAC)**.

### 3.4 Jardim de chuva com NA a 0,90 m

- A Skill `paisagismo-jardim-de-chuva` apresenta a técnica como solução de infiltração ("recarrega o lençol"; "até 30% do escoamento") e declara que **não há NBR específica** (seção "Limitações honestas") **(b)**. **A Skill é silente sobre a separação entre o fundo do jardim e o lençol freático.** Registro a lacuna para Cardozo (seção "Escopo, crescimento e manutenção" da própria Skill).
- A Skill de fundações §5 (parceria com Glaziou) manda verificar se o lençol já não está saturado na cota de infiltração **(b)**. O NA da sondagem é de **0,90 m** (5.7) **(a)**. O NA máximo provável (chuva forte, lago cheio) **não é conhecido** (Skill `rebaixamento-...` §6) **(c)**.
- **Parecer:** **não recomendo** jardim de chuva como solução de infiltração neste lote sem análise de Glaziou e Saturnino sobre a folga entre o fundo e o NA máximo. Pode virar acúmulo de água. Se o jardim de chuva conta como superfície drenante para fins legais, quem decide é o Kelsen **(c)**.

---

## 4. Conflitos percebidos

### 4.1 Edícula: parecer de Oscar

| Regra | Exigido | Existente (5.2) | Falta |
|---|---|---|---|
| Condomínio, 5.4 Art. 6º (prevalece) | 2,50 m | 0,80 m | **1,70 m** |
| COES, unifamiliar (parecer, linha 12; Art. 31 p.ú.) | 1,50 m | 0,80 m | **0,70 m** |
| Código Civil Art. 1.301 (janela) | 1,50 m | 0,80 m, **com janela** | 0,70 m (risco civil: Kelsen R5) |
| Vão de iluminação ou ventilação | Uma faixa de 0,80 m não é afastamento nem prisma (parecer P2). Um PV, só para ventilação, já exige lado de **no mínimo 1,00 m**, e um PVI, **no mínimo 3,00 m** (Skill `coe-lc198-...` §2) | 0,80 m | não atende nem como PV |

- **Habite-se:** a edícula **não aparece** na planta aprovada (5.8) **(a)**. Não há direito adquirido, e o "Art. 38 da LC 274" do estudo anterior está revogado (parecer P2) **(b)**.
- **TO:** a edícula computa por conservadorismo (parecer, linha 17; D3046 XV × LC 270 Arts. 347 V / 350 IV, tensão aberta na R4 do Kelsen) **(b)**. **Quanto da projeção de 228,72 m² ela consome: não consta**, porque a área dela não é documentada **(c: topógrafo, T9)**.
- **Manter "como está":** **inviável dentro das premissas.** Viola o Art. 6º do condomínio independentemente do que a Prefeitura decida (parecer P2) e consome TO.
- **Demolição parcial** (cortar a faixa de 1,70 m junto à divisa e ficar com o resto): na prática, é obra nova sobre uma construção nunca licenciada. O enquadramento seria o híbrido que o parecer P2 descreve como "sem caminho limpo" **(c: Kelsen, rito)**. Também não se sabe se o resto, depois do corte, tem largura útil (as dimensões não constam).
- **Parecer:** **prever a demolição total**, alinhado com a recomendação do Legal. A **decisão final é do cliente** (parecer §5.2). Se a família quiser uma edícula, ela entra no projeto novo, dentro do envelope e contando na projeção.

### 4.2 Piscina: parecer de Oscar

- **Posição, dimensões, profundidade e cota: não constam no dossiê.** O "~4 × 8 m nos fundos" do enunciado é estimativa não documental **(c: T10)**.
- **Quem fixa o limite de 1,60 m:** o **Regramento do condomínio**, Art. 8º (5.4), que é norma privada e não lei. Pela lei municipal, piscina descoberta **não depende de licença** (LC 270 Art. 278 §1º II, no parecer P2) **(a)+(b)**. O enunciado diz "a Lei permite até 1,60 m", o que não confere.
- **NA a 0,90 m (5.7)** contra o fundo de até 1,60 m: se a profundidade for contada da mesma superfície em que o NA foi medido, o fundo fica até **1,60 − 0,90 = 0,70 m abaixo do NA**. A amarração altimétrica entre a borda, o terreno atual e a soleira de +3,20 **não consta**, e um aterro até +3,20 muda essa conta **(c)**. Riscos, pelas Skills **(b)**:
  - **subpressão e flutuação com a piscina vazia** (manutenção), verificadas com o NA máximo (Skill `rebaixamento-...` §6, verificação acrescentada em 29/09, e §4.3);
  - **estanqueidade e impermeabilização** sob pressão de água externa (Skill `rebaixamento-...` §4.3, remetendo à NBR 9575);
  - **esgotamento na obra**: escavar abaixo do NA é extração de água subterrânea. Acima de 5.000 L/dia, cai fora do uso insignificante, e a outorga ou certidão do INEA tem de sair **antes** da escavação (Skill `rebaixamento-...` §2; R1 da Skill ainda aberta) **(c: Hely via Kelsen)**;
  - **recalque em vizinho** se houver bombeamento em argila mole (Skill `rebaixamento-...` §1 e §3; argila mole de 2,5 a 9,0 m, conforme 5.7).
  - O mesmo raciocínio vale para blocos e baldrames, que já podem passar o NA mesmo dentro do limite de 1,20 m do Art. 8º (Mascaró v8 §6.1, pergunta a Baumgart) **(c: Baumgart/Cardozo)**.
- **Posição × H1:** se a piscina estiver nos últimos 18 m (y 22–40), **cai em H1** e não pode ser presumida mantida **(c: Kelsen/SMAC)**.
- **Posição × afastamento de fundos:** se estiver em y 35–40, o Regramento não diz se piscina pode ocupar o afastamento de fundos **(c: condomínio/Kelsen)**.
- **Não é área permeável** (§3.2).
- **Parecer:** **não dá para dizer hoje se a piscina pode ser mantida.** Pode-se manter **somente se**, depois de levantada, ela (i) estiver fora da faixa H1 ou H0 for confirmado, (ii) tiver profundidade ≤ 1,60 m, (iii) estiver em estado estrutural e de estanqueidade compatível com NA de 0,90 m (laudo de Baumgart/Cardozo) e (iv) não ocupar área necessária ao envelope ou à permeabilidade. Até lá, o EP **não usa a piscina existente como premissa**. A decisão final é do cliente, com o laudo.

### 4.3 Árvores: parecer de Oscar

- Ficam no afastamento frontal (caso §3) **(a)**. **Locação, DAP e estado não constam** (Peça 1, §5) **(c: T11 + laudo de profissional habilitado)**.
- **O motivo do pedido de remoção caiu.** A cliente quer tirar as árvores "pra fazer a rampa da garagem" (5.10), mas sem subsolo não há rampa para descer (parecer P6) **(b)**. O afastamento frontal admite estacionamento descoberto de unifamiliar e rampa de até 10% e 0,50 m (LC 270 Art. 363 §2º, no parecer P6) **(b)**.
- **Remoção** exige licença municipal (LC 270 Art. 278 XIV) **e** autorização do condomínio (5.4 Art. 12) (parecer, linha 23) **(a)+(b)**. Quando vinculada a obra, o pedido segue pela SMAC/SISARV junto com o licenciamento (Skill `remocao-...` §3), com compensação (§5). Árvore sadia sem risco documentado raramente sai (Skill `remocao-...` §6). Essa regra prática é de fonte secundária (R3 da Skill) **(b)/(c)**. A espécie de cada árvore vem do laudo; se for exótica, o tratamento muda, mas a lista da SMAC não foi levantada (Skill `remocao-...` §6 item 3 e §10) **(c: Glaziou)**.
- **Ganho de espaço com a remoção:** não muda a projeção nem o envelope, porque as árvores estão fora do envelope, no frontal. Só liberaria posição para o acesso no frontal e reduziria a vegetação preferencial para a superfície drenante (Art. 353 I).
- **Parecer:** **preservar as 3 árvores e posicionar o acesso de veículos conforme a locação a levantar.** Remoção de uma delas só se, com a locação em mãos, não houver acesso viável, e mesmo assim com laudo, licença e autorização do condomínio. **Decisão do cliente**, sujeita à SMAC e ao condomínio.

### 4.4 APP / FMP / marinha nos fundos

- O levantamento **não resolve** nenhuma das três questões, que exigem demarcação oficial (parecer §2.4). Alerta: **se H1 se confirmar, os últimos 18 m (y 22–40) ficam fora do desenho**, com os efeitos numéricos do §2.3 e do §3.3 **(b)**.
- A contradição entre 5.5 ("sem ligação com o sistema lagunar") e 5.9 (maré, manilha ligando ao canal) **reforça** o risco. O caseiro não prova nada, mas também não pode ser descartado. Se a ligação se confirmar, entra a LC 270 Art. 216 V (Kelsen R2) **(b)/(c)**.
- O levantamento ajuda com três medições: área do espelho d'água (T13), régua de maré (T14) e posição da manilha (T13). Ver a Peça 1, §7, e o §9 abaixo.

---

## 5. Permeabilidade: o que o enunciado pede e o que confere

- Mínimo de **142,95 m²** (25% × 571,80) (parecer, linha 14) **(b)**. Locação conceitual no §3.
- O enunciado associa a "LC270 Art. 353 III" a um "valor mínimo de lote por zona". **Não confere.** No parecer aprovado, o Art. 353 III é a regra das **porções de superfície drenante com no mínimo 4 m² e 2 m de lado** (parecer, linha 14 e §5.2). Lote mínimo não é condicionante deste caso: o lote existe e está registrado (5.1).

---

## 6. Cotas e referenciais

| Item | Situação | Quem decide ou fornece |
|---|---|---|
| Cota de soleira | +3,20 m **prevista** (5.2), não "atual" como diz o enunciado; referência do condomínio | Topógrafo (T3), Kelsen/Hely (Art. 458) |
| Ponto mais alto da edificação | ≤ +11,70 m no referencial do condomínio, se a soleira for +3,20 (5.4 Art. 7º) | conta (a)+(b) |
| Cota do terreno atual e aterro até +3,20 | **Não consta**. Sem ela não se sabe o volume de aterro | Topógrafo (T4) |
| Efeito do aterro na fundação | Aterro sobre argila mole gera **atrito negativo** nas estacas (Skill de fundações M4); pergunta já registrada pelo Mascaró v8 §10 | Baumgart/Cardozo (**não dimensiono**) |
| Cota do piso térreo da casa nova | Decisão do EP, amarrada à soleira; aqui não a fixo | Lúcio/Oscar na Etapa 05 |
| Cota da piscina (se mantida) | Não consta | Topógrafo (T10) |
| Regra numérica de soleira contra o meio-fio e de "terreno natural" para gabarito | Não está nas Skills legais (Skill de levantamento R2) | Hely/Kelsen |

---

## 7. Fundações: só o condicionante de levantamento

A sondagem 5.7 dá NA de 0,90 m, argila orgânica mole de 2,5 a 9,0 m e areia compacta abaixo de 11 m **(a)**. O Mascaró v8 §6.1 e o Villaça v9 §6 já apontaram estacas (hélice contínua) e radier inadequado **(b)**. **Não dimensiono nada.** O que o levantamento precisa entregar a Baumgart: cota do terreno atual e aterro previsto (atrito negativo, M4); posição dos 3 furos em relação à projeção futura (NBR 8036 pela Skill de fundações R7: no mínimo 3 furos entre 200 e 400 m² de projeção; reforço local de 1 furo a cada 100–150 m²); data e condição da medição do NA (o NA médio anual e o NA máximo podem ser diferentes, conforme a Skill de fundações §6 e a Skill `rebaixamento-...` §6); vizinhos para vistoria cautelar **(c: Baumgart/Cardozo)**.

---

## 8. Acessibilidade de D. Lourdes

- A suíte acessível é **programa, não exigência legal**: o COES dispensa a casa unifamiliar das normas de acessibilidade (Art. 31 V, no parecer §5.2) **(b)**. A Skill `arquitetura-nbr9050-...` ("Brecha válida" item 3 e "Limitações" item 3) aponta a mesma isenção para unifamiliar privada **(b)**.
- **O desnível entre a rua (meio-fio) e a soleira não é conhecido**, porque faltam o RN do meio-fio e a cota do terreno (T2, T4) **(c)**.
- **Impacto, pela Skill NBR 9050 (tabela de rampas):** obra nova com no máximo 8,33%, até 0,80 m de desnível e 9,60 m por segmento, e patamares de 1,20 m. Recomendável 5%. Largura mínima de 1,20 m **(b)**. Conta de ordem de grandeza: comprimento = desnível / inclinação. Exemplo: 0,50 m a 8,33% → 6,00 m, o afastamento frontal inteiro. Um desnível maior ultrapassa o frontal ou exige mais de um segmento com patamar.
- **Interface com o Legal:** no afastamento frontal, a rampa é admitida até 10% e 0,50 m de altura (Art. 363 §2º, no parecer P6) **(b)**. **Se o desnível rua–soleira passar de 0,50 m**, a parte excedente da rampa acessível teria de ficar fora do frontal, ou seja, dentro do envelope ou das laterais, e, se coberta, consome projeção. **Esse é o efeito de desenho a levar ao Briefing.** O valor do desnível depende de T2/T4. A solução fica no EP.
- Os parâmetros numéricos da Skill vêm de fonte secundária, porque a norma não foi lida (Skill, "Limitações" item 1). Antes do anteprojeto, é preciso conferir no texto da NBR 9050 **(c)**.

---

## 9. Análise de riscos: o que o Legal deixou aberto e onde o levantamento ajuda

| # | Aberto no Legal | O levantamento ajuda? | Impacto no desenho |
|---|---|---|---|
| 1 | APP: área do espelho d'água < 10.000 m²? | **Sim:** medir o espelho (T13). A decisão é da SMAC | H0 ou H1 (§2.3) |
| 2 | Marinha: há influência de maré? | **Sim:** régua de maré (T14). A decisão é da SPU | Domínio da União sobre a faixa |
| 3 | FMP (INEA) | Não. Depende da certidão do INEA | Não estimável |
| 4 | Ligação lago–canal (5.5 × 5.9; Art. 216 V) | **Sim:** locar a manilha (T13). A decisão é da SMAC/Kelsen | Reforça H1/H2 |
| 5 | Cota de soleira no referencial oficial (Art. 458) | **Sim:** T3 | Rito (avaliação técnica) e alturas |
| 6 | Divisa com o Lote 16 | **Sim:** linha do PAL e muro (T5). A decisão é do cliente com advogado | 571,80 × 600 |
| 7 | Como o condomínio mede a TO | Não. Pergunta ao condomínio | Projeção disponível |
| 8 | Edícula: rito e cômputo | Parcial: área (T9) | Projeção consumida |
| 9 | Demolição × obra nova (TRAVA do POP-LEGAL-03 §5) | Não | Cronograma |
| 10 | Brita ou piso drenante como superfície drenante; APP como permeável | Não | Folga permeável (§3) |

---

## 10. Skills usadas (seções)

`levantamento-topografico-cadastral-orientado-duli-licin-rj` §2, §3, §4, §5, R2; `decreto3046-81-lc270-2024-licin-barra-recreio` §4 e §6 (M1, M2, M3); `coe-lc198-2019-...` §2 (PV ≥ 1,00 m; PVI ≥ 3,00 m); `fundacoes-solos-moles-...` §3.3, §5, §6, R7, M4; `rebaixamento-lencol-freatico-...` §1–§4, §6; `paisagismo-jardim-de-chuva` (Como usar; Limitações honestas; lacuna registrada); `remocao-arvores-smac-fpj-...` §3, §5, §6, §10; `arquitetura-nbr9050-acessibilidade` (tabela de rampas; Brecha válida item 3; Limitações). A `varandas-nao-computaveis-...` **não foi usada**: nesta etapa não se define varanda. Não usei Skill de NBR 6492 "memoriais por etapa".

## 11. Declaração

Ensaio 100% fictício. Nada foi protocolado nem enviado, e nenhum órgão, condomínio ou cliente foi contatado. **Não abri, listei, li ou citei nada em `_gabaritos_LACRADO\` nem qualquer `parecer_bardi*.md`.** Análise preliminar, sujeita à auditoria de Lúcio.

— Oscar, 06/10/2026
