---
name: fundacoes-solos-moles-lencol-freatico-barra-recreio
description: "Critérios de projeto de fundações em solos moles e com lençol freático alto — condicionantes geotécnicos da Barra da Tijuca, Recreio dos Bandeirantes e Jacarepaguá: SPT, tipos de estaca e soluções recomendadas."
version: "1.3"
status: ativa-com-ressalva
created: 2026-09-21
updated: 2026-10-01 (v1.3 — seção "Macetes de quem faz", M1-M4, Rotina de Macetes v1.2)
author: Rotina Diária Skills v3.2
gestor_validador: cardozo
agente_principal: baumgart
cross_disciplina:
  - saturnino
  - glaziou
fonte_primaria_lida: "não — dados de fontes técnicas secundárias verificadas (AECweb, APL Engenharia, USF, blog.apl.eng.br)"
metadata:
  tipo: Inteligência (Trilha A)
  norma_base: "NBR 6122:2019+Em.1/2022 (Fundações) + NBR 6484/2020 (SPT)"
  zona_geografica: "Barra da Tijuca, Recreio dos Bandeirantes, Jacarepaguá — Rio de Janeiro"
  tags:
    - fundacoes-profundas
    - solos-moles
    - lencol-freatico
    - estaca-helice-continua
    - barra-tijuca
    - recreio
    - spt
    - baumgart
---

# Fundações em Solos Moles e Lençol Freático Alto
## Barra da Tijuca, Recreio dos Bandeirantes e Jacarepaguá — RJ

> **Relação com outras Skills (harmonizado em 28/09/2026):** esta Skill **complementa** `nbr6122-2019-fundacoes`. A regra geral (norma, tipos de fundação, nº mínimo de furos pela NBR 8036) está lá; aqui fica só o que muda no solo mole da Zona Oeste: densificação de furos, escolha de estaca e lençol freático. Se as duas parecerem divergir, vale a regra geral da NBR 8036 como piso e esta Skill como reforço local.

---

## POR QUE ESTA SKILL

A Barra da Tijuca, o Recreio dos Bandeirantes e a Baixada de Jacarepaguá têm perfil geotécnico distinto do restante da cidade: **solo mole**, **aterro sobre banhados** e **lençol freático muito próximo ou na superfície** em grande parte dos lotes. Projetar fundação para esses terrenos como se fosse um lote no Flamengo ou na Tijuca é erro técnico comum que leva a recalques diferenciais, erosão de base e falha de fundação. Esta Skill reúne o diagnóstico e as soluções recomendadas.

---

## 1. CONDICIONANTES GEOTÉCNICOS DA REGIÃO

### Perfil típico do solo

| Camada | Característica | Implicação |
|---|---|---|
| 0–3 m | Aterro antrópico (anos 1970–1980) ou argila orgânica mole | SPT N ≤ 5, baixa capacidade de carga |
| 3–10 m | Areia fina fofa ou argila mole a média | SPT N 3–10, compressível |
| 10–20 m | Argila a areia de densidade média | SPT N 10–20 |
| > 20 m | Areia densa ou rocha alterada | SPT N > 20, capacidade de carga viável |

**Lençol freático:** frequentemente entre 0,5 m e 2,0 m de profundidade, especialmente em lotes próximos às lagoas (Lagoa de Jacarepaguá, Lagoa da Tijuca, Lagoa de Marapendi).

### Consequência para projeto

- **Solo raso incompetente** → fundação direta (sapata, radier em solo) é inviável na maioria dos casos
- **Lençol freático alto** → perfuração seca (tradagem) não funciona para profundidades > lençol
- **Aterro irregular** → sondagem SPT **obrigatória antes de qualquer dimensionamento** (programação de furos pela **NBR 8036** — 1 furo/200 m² de projeção até 1.200 m²; mín. 2 furos até 200 m², mín. 3 entre 200–400 m² — ver R7)

---

## 2. TIPOS DE SONDAGEM RECOMENDADA

### SPT (Standard Penetration Test) — NBR 6484/2020

- Fornece perfil estratigráfico + resistência N por metro
- **Identifica nível do lençol freático** quando interceptado
- Mínimo de furos pela NBR 8036 — em Barra/Recreio, ampliar para 1 furo a cada 100–150 m² (solos heterogêneos por aterro)
- Solicitar análise granulométrica nas amostras de camadas moles (argila × silte × areia) para aferir coesão

**Atenção:** em lotes que eram banhado ou lagoa até décadas recentes, a sondagem pode revelar turfas (matéria orgânica decomposta) com N = 0 — camada que exige tratamento especial ou transposição total.

### Critério de paralisação do SPT — NBR 6484:2020 (v1.1, 24/09/2026)

A NBR 6484:2020 **cancela e substitui** a NBR 6484:2001. O critério de paralisação é responsabilidade técnica do **contratante** (Baumgart/Cardozo, na especificação da sondagem) — se nada for especificado, a norma manda avançar até atingir um destes:

| Trecho contínuo | NSPT em todos os metros do trecho |
|---|---|
| 10 m | ≥ 25 golpes/30 cm |
| 8 m | ≥ 30 golpes/30 cm |
| 6 m | ≥ 35 golpes/30 cm |

**Brecha/armadilha na Barra/Recreio:** paralisação normativa **não é rocha nem garantia de camada competente contínua** — só atesta que o ensaio terminou. Se a estaca prevista (hélice 12–20 m) precisar ir abaixo do fundo do furo, ou se houver dúvida de continuidade, matacão ou embutimento em rocha, **especificar sondagem mista/rotativa** complementar. Regra prática: na especificação da sondagem, Baumgart fixa profundidade mínima ≥ ponta estimada da estaca + margem, em vez de deixar o critério default da norma decidir.

---

## 3. FUNDAÇÕES RECOMENDADAS POR CONDIÇÃO

### 3.1 Solo mole + lençol freático próximo à superfície (situação mais comum na Barra/Recreio)

| Solução | Quando usar | Vantagem | Limitação |
|---|---|---|---|
| **Estaca hélice contínua** | Qualquer profundidade com água | Atravessa areia fofa e lençol freático sem desmoronar; concreto bombeado pelo eixo da broca antes da extração | Barulho e vibração limitados; equipe especializada |
| **Estaca pré-moldada de concreto** | Solo não coesivo + lençol freático | Controle de qualidade da fábrica; boa para grandes cargas pontuais | Cravação por percussão pode ser restrita em área residencial |
| **Estaca escavada com camisa metálica** | Quando lençol freático pode invadir o furo | Camisa avança durante escavação e impede colapso | Custo maior; deixar camisa ou retirar após concretagem |
| **Radier rígido** | Solo superficial razoável (N ≥ 5–8) + carga bem distribuída | Simples, sem equipamento de percussão | Requer solo superficial minimamente competente |

### 3.2 Solo com turfa ou matéria orgânica (N ≈ 0)

- **Pilotar sem apoio nesta camada** — a estaca deve transpor até camada competente (N ≥ 10–15 para carga leve; N ≥ 20+ para carga alta)
- Turfa não pode servir como solo de apoio, mesmo para radier
- Verificar recalque diferencial no tempo — turfa continua adensando mesmo após a obra

### 3.3 Carga leve (casas térreas, sobrados)

- Estaca hélice contínua Ø 30 cm ou Ø 40 cm com profundidade de 12–20 m é a solução padrão na Barra/Recreio
- Capacidade de carga típica: 60–120 kN/estaca (hélice Ø 30–40 cm em areia média)

---

## 4. ERROS MAIS COMUNS NA REGIÃO

1. **Usar sapata em aterro:** o aterro original da Barra (anos 1970–1980) não tem compactação controlada. SPT baixo (N < 5). Sapata recalca.

2. **Jogar concreto na água:** em furo cheio de água, o concreto convencional fica contaminado e perde resistência. Solução: hélice contínua (concreto bombeado pela broca) ou camisa metálica + concreto autoadensável.

3. **Não considerar a turfa:** laudos geotécnicos antigos podem não ter identificado camadas orgânicas — pedir laudo novo se o lote era área alagada até recentemente.

4. **Dimensionar pelo valor médio de N:** em solos heterogêneos, um furo com N médio bom pode mascarar uma camada mole. Usar o critério da camada mais fraca no trecho de apoio.

5. **Desconsiderar recalques futuros:** solos moles de Jacarepaguá/Recreio têm recalques por adensamento que podem levar anos. Prever juntas de dilatação e não apoiar estrutura em fundação diferente numa mesma planta.

---

## 5. PARCERIA COM OUTROS AGENTES

- **Saturnino:** lençol freático alto impacta sistema de drenagem de águas servidas. Verificar cota de saída do esgoto — pode ser necessária elevatória ou rebaixamento do lençol durante a obra. **Rebaixamento (outorga INEA, recalque de vizinhos, alternativas sem bombear): ver `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` (29/09/2026, complementa).**
- **Glaziou:** jardins de chuva e jardins de infiltração na Barra/Recreio devem verificar se o lençol não está já saturado na cota de infiltração — paisagismo superficial pode acumular água se o subsolo estiver impermeável.
- **NBR 6122:2019 + Em.1/2022 (Skill existente de Baumgart):** esta Skill é complemento geográfico da Skill de fundações geral. Aqui o foco é o solo específico da Barra/Recreio, não os cálculos gerais da norma.

---

## 6. O QUE FAZER ANTES DE QUALQUER LANÇAMENTO ESTRUTURAL

**Checklist mínimo para projetos na Barra/Recreio:**

- [ ] Contratar sondagem SPT — **mínimo normativo pela NBR 8036** (contado pela área de projeção da edificação, não do lote): 1 furo a cada 200 m² de projeção até 1.200 m²; mínimo 2 furos até 200 m² e mínimo 3 entre 200 e 400 m² (ver R7). **Reforço local Barra/Recreio:** 1 furo a cada 100–150 m² de projeção — recomendação de projeto desta Skill, acima do mínimo normativo, não exigência da norma
- [ ] Verificar se o histórico do lote inclui aterro, banhado ou lagoa (mapa histórico ou vizinhança)
- [ ] Identificar nível do lençol freático médio anual (pode ser diferente da profundidade no dia da sondagem)
- [ ] Checar se há camada de turfa (N ≈ 0 com cores escuras/cheiro orgânico na amostra)
- [ ] Cotizar hélice contínua como opção padrão e escavada com camisa como alternativa
- [ ] Comunicar a Kelsen se SPT revelar condição que altere viabilidade da obra (ART de fundações pode mudar custo substancialmente)

---

## Macetes de quem faz

> Entrou na v1.3 (01/10/2026, Rotina de Macetes v1.2), conferido por Cardozo contra esta Skill, a `nbr6122-2019-fundacoes` e a norma (até onde ela foi lida). Macete **não é norma**: é como o profissional experiente resolve. Os números citados vêm da fonte e precisam ser conferidos no texto da NBR antes de entrar em memorial.

**M1 — Monitoramento não é controle: calibrar o equipamento num furo de sondagem**
- **O que fazer:** no início do estaqueamento, fazer um teste de introdução do trado ao lado de um furo de sondagem, sem concretar (retirar girando ao contrário), anotando a cada metro rotação, velocidade de avanço e pressão de torque. Se o gráfico não se parecer com o NSPT, pedir nova sondagem a empresa qualificada. Se parecer, a parada das demais estacas daquela obra pode ser controlada pela pressão de torque daquele equipamento.
- **Por que funciona:** o computador de bordo só registra; a hélice contínua é de "controle pouco abrangente". A qualidade do SPT caiu (Alonso cita Menezes 2013 e Medeiros Silva 2014), e na Barra o aterro heterogêneo já é o erro nº 4 desta Skill. O teste cruza duas medições independentes do mesmo solo.
- **Quem disse / onde:** Eng. Urbano Rodriguez Alonso, Instituto de Engenharia, 2023 (F1, slides 26-27).
- **Tipo:** A (profissional/autor técnico).
- **Limite:** vale só para aquele equipamento e aquela obra. Não substitui a profundidade de projeto (§2, Baumgart fixa) nem prova de carga (NBR 16903:2020). O furo de teste fica fora da posição das estacas definitivas.

**M2 — Ler o "perfil" da estaca como % de consumo, não como forma**
- **O que fazer:** no relatório da hélice, olhar em que trechos houve sobreconsumo de concreto. Esses trechos têm de coincidir com as camadas moles da sondagem. Se não coincidirem, questionar a sondagem.
- **Por que funciona:** o software desenha a estaca supondo um cilindro simétrico; a "forma" desenhada é ficção, o consumo por trecho é dado medido.
- **Quem disse / onde:** Alonso (F1, slide 28).
- **Tipo:** A.
- **Limite:** não prova a integridade do fuste.

**M3 — Erros de execução que Baumgart proíbe na especificação de hélice contínua**
- **O que fazer:** escrever na especificação:
  - (a) limitar a "prolonga" do trado em argila muito mole abaixo do NA. Exemplo de Alonso: prolonga de 6 m num equipamento de trado de 18 m; em trado menor, prolonga ≤ 10% do comprimento;
  - (b) não parar a concretagem na cota de arrasamento quando ela fica abaixo do terreno, e não deixar a cabeça da estaca sem armadura depois do arrasamento;
  - (c) armadura com no mínimo 4 m, e concha da escavadeira com no máximo 50% do espaço entre as estacas do bloco (evita quebra por impacto na escavação);
  - (d) armadura longa: espaçadores tipo rolete no pé e no topo; concreto dosado com tecnólogo. Slump acima de 26 cm não resolve: em areia acima do NA, usar aditivo modificador de viscosidade/antissegregante (Alonso: ≤ 1% do cimento).
- **Por que funciona:** são as patologias mais comuns que Alonso relata da execução (Geofix/Sondasa). Proibir na especificação é mais barato que discutir depois com a executora.
- **Quem disse / onde:** Alonso (F1, slides 19-20, 29, 32), citando NBR 6122:2019, Anexo N, itens N4 (prolonga) e N6 (armadura).
- **Tipo:** A.
- **Limite:** conferir os valores no texto da NBR 6122 antes de citar em memorial. Registrar a técnica do aditivo, não a marca que Alonso cita. **Divergência a resolver:** Alonso põe a hélice contínua no Anexo N; a Skill `nbr6122-2019-fundacoes` (tabela da Emenda 1) chama o Anexo N de "escavadas com fluido" e o Anexo J de "hélice contínua". Uma das duas está com a letra trocada. Até conferir na norma, citar "Anexo da hélice contínua (N segundo Alonso)", não a letra seca.

**M4 — Atrito negativo na argila da Baixada de Jacarepaguá**
- **O que fazer:** se o lote vai receber aterro (alteamento de greide para fugir de alagamento, comum na Barra/Recreio) ou recebeu aterro recente, Baumgart considera atrito negativo com ponto neutro conservador (mais baixo) e, se possível, aterra ou pré-carrega antes de estaquear.
- **Por que funciona:** o adensamento da argila sob o aterro "puxa" a estaca para baixo durante anos (ver erro nº 5 desta Skill). O estudo concluiu que, em argila extremamente compressível sob aterro, o ponto neutro fica bem mais baixo que nos métodos usuais, e o atrito negativo calculado pelos métodos correntes pode ficar contra a segurança.
- **Quem disse / onde:** AZEVEDO, R. S., orientação Profªs Bernadete Ragoni Danziger e Denise M. S. Gerscovich, dissertação UERJ, 2017 (F2, Resumo).
- **Tipo:** A (pesquisa acadêmica aplicada a caso real da região).
- **Limite:** caso de estaca metálica sob talude de aterro; é previsão, não medição. A ordem de grandeza exige cálculo por caso. Pré-carga leva meses: entra no cronograma, não é decisão só de Baumgart.

**Tipo B (executora/fabricante) e vídeo:** tentados, nada acessível (manuais de Geofix, Brasfond, Fundesp não localizados; nenhum vídeo). Fica para a próxima rodada.

---

## RESSALVAS

**R1 (CRÍTICA) — Fonte primária:** dados de SPT médio e profundidade de camadas competentes NÃO foram obtidos de laudo geotécnico real da Barra/Recreio — são valores típicos de referência da literatura técnica (AECweb, APL Engenharia). Baumgart DEVE solicitar sondagem real antes de qualquer dimensionamento.

**R2 — Variabilidade por lote:** o perfil geotécnico varia muito dentro do mesmo bairro. Um lote a 200 m do outro pode ter situação completamente diferente (aterro antigo vs. solo natural).

**R3 — Norma vigente:** NBR 6122 vigente é a edição de 2019 + Emenda 1/2022 (cimento: 350 kg/m³ mín.). Verificar se há nova emenda antes de usar.

**R4 — Não substituir Skill NBR 6122:** esta Skill complementa, não substitui, a Skill de fundações NBR 6122:2019 (07/09/2026) que trata de dimensionamento. Aqui o foco é o condicionante geográfico da Barra/Recreio.

**R5 — ✅ FECHADA 24/09/2026:** NBR 6484:2020 existe e **cancela e substitui a NBR 6484:2001** (Target Normas / catálogo ABNT; confirmado por múltiplas fontes técnicas). Citação "NBR 6484:2020" em memorial está correta. Texto integral continua não lido (norma paga).

**R6 ALTA — Capacidade de carga 60-120 kN/estaca sem método declarado (Cardozo, 21/09):** os valores de capacidade de carga citados (60–120 kN para hélice Ø 30–40 cm em areia média) não especificam o método de cálculo utilizado (Aoki-Velloso ou Décourt-Quaresma produzem resultados distintos para o mesmo perfil SPT). Baumgart não pode usar esses valores como referência em memorial de dimensionamento real sem declarar o método — são apenas orientação de ordem de grandeza para estimativa preliminar de viabilidade, não valores de projeto.

**R7 — Mínimo de furos depende da área (Cardozo, 24/09/2026; harmonizado 28/09/2026):** a atribuição antiga a "NBR 6122 item 6.3" estava errada. A regra é da **NBR 8036** (programação de sondagens): 1 furo/200 m² de projeção até 1.200 m²; mín. 2 furos até 200 m²; mín. 3 entre 200–400 m². Desde a v1.2 esta Skill e `nbr6122-2019-fundacoes` usam a mesma redação (o antigo "mínimo 3 furos" sem condição do checklist §6 foi corrigido). **Ressalva:** valores da NBR 8036 vêm do conhecimento de Cardozo, não de leitura da norma — Baumgart confere antes de citar em memorial. Regra para projeção acima de 1.200 m²: **a confirmar** (não coberta pela fonte). Na Barra/Recreio, manter como recomendação de projeto (acima do mínimo normativo) 1 furo/100–150 m².

---

## FONTES VERIFICADAS

- AECweb — "Solos moles pedem fundações profundas: conheça as principais alternativas" (secundária ✓)
- APL Engenharia — "Lençol Freático: Como a Água no Solo Pode Comprometer Fundações" (secundária ✓)
- APL Engenharia — "Conheça os principais tipos de estacas para fundações" (secundária ✓)
- GF Engenharia SP — "Sondagem de simples reconhecimento do solo com SPT" (secundária ✓)
- TCC UENF 2026 — "Projeto de fundações profundas em solo mole" — PDF binário, não lido na íntegra (mencionado, não citado como fonte de valores)
- **NBR 6484/2020 e NBR 6122:2019+Em.1/2022** — normas de referência (não lidas na íntegra — ABNT pagas)
- Target Normas — ficha ABNT NBR 6484 (edição 2020 substitui 2001) (secundária ✓, 24/09)
- APL Engenharia — "Sondagem SPT paralisada pela NBR 6484: quando avançar para sondagem rotativa?" (secundária ✓ lida, 24/09 — critério 10/8/6 m)
- boletimsondagem.com.br — "NBR 6484:2020: guia prático para boletim de sondagem SPT" (secundária ✓ lida, 24/09)
- YouTube "QUANDO PARAR A SONDAGEM | NBR 6484 2020 ATUALIZADA" — localizado, **não assistido** (/watch bloqueado por HTTP 429/403 do YouTube em 24/09)
- **F1** — ALONSO, Urbano Rodriguez. "Estacas Hélice Contínua — sua história no Brasil... controles da capacidade de carga e patologias mais comuns". Instituto de Engenharia (SP), 2023. https://www.institutodeengenharia.org.br/site/wp-content/uploads/2023/08/Helice-continua.pdf — slides 19, 20, 26-29, 32 (lida por Wallenberg em 01/10/2026; base de M1-M3)
- **F2** — AZEVEDO, R. S. (orient. B. R. Danziger e D. M. S. Gerscovich). "Evolução do atrito negativo no tempo: estudo de um caso de estaca metálica em argila muito compressível". Dissertação UERJ, 2017. https://www.bdtd.uerj.br:8443/bitstream/1/11644/1/Rachel%20da%20Silva%20Azevedo1.pdf — Resumo (lido por Wallenberg em 01/10/2026; base de M4)

---

## HISTÓRICO DE VERSÕES

- **1.0** — 21/09/2026 — criação (Rotina Diária Skills v3.2).
- **1.1** — 24/09/2026 — R5 fechada (NBR 6484:2020 confirmada); critério de paralisação SPT adicionado; R7 nova.
- **1.2** — 28/09/2026 — correções do treino aprovadas por Claudemberg: checklist §6 troca "mínimo 3 furos" sem condição pelo mínimo da NBR 8036 por área de projeção, com o reforço local 1/100–150 m² explicitado como recomendação de projeto; R6 e R7 reordenadas (R6 antes de R7).
- **1.3** — 01/10/2026 — Rotina de Macetes v1.2: seção "Macetes de quem faz" com M1-M4 (F1 Alonso; F2 Azevedo/Danziger/Gerscovich UERJ), todos aprovados por Cardozo. M3 com divergência de letra de anexo (N × J) contra a `nbr6122-2019-fundacoes`, a conferir na norma.
