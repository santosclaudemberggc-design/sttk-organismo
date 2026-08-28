---
name: playbook-rotinas-automaticas-sttk
versao: 1.0.0
criado: 2026-08-27
autor: Wallenberg (CEO)
---

# Playbook — Rotinas Automáticas STTK

Documento permanente de referência operacional. Cobre as duas rotinas automáticas do organismo,
como elas se relacionam, o que cada passo exige, e as lacunas identificadas em 27/08/2026.
Atualizar sempre que uma rotina mudar de forma que afete o comportamento esperado.

---

## MAPA GERAL DAS ROTINAS

| Rotina | Arquivo | Frequencia | Papel |
|--------|---------|------------|-------|
| Diaria Skills | `wallenberg-rotina-diaria-skills-v2_SKILL.md` | Todo dia (08:00) | Descobrir e documentar ferramentas e conhecimento novo |
| Drenagem Continua | `wallenberg-drenagem-continua-v2_SKILL.md` | Sob demanda / agendada | Drenar fila de pendencias, acionar Gestores, implantar Skills |

### Como as rotinas se relacionam

```
Diaria Skills  ->  produz Skills com Status: proposta
Drenagem       ->  le Skills com Status: proposta  ->  implanta  ->  atualiza Status
```

Regra fundamental: a Drenagem nao busca ferramenta. A Diaria Skills nao implanta.
Qualquer cruzamento desses papeis gera desalinhamento (ja aconteceu em 25/08/2026 e exigiu 3 correcoes no mesmo dia).

---

## ROTINA 1: DIARIA SKILLS

### Objetivo

Transformar pesquisa externa (GitHub, YouTube, Instagram, normas tecnicas) em Skills documentadas,
prontas para implantacao pela Drenagem Continua.

### Quando roda

Todo dia as 08:00. Disparo automatico agendado.

### Fronteira — o que nao faz

- Nao implanta ferramenta (nao clona, nao instala, nao executa codigo de terceiro)
- Nao produz documento de cliente (DULI, memorial, prancha)
- Nao aciona Gestores operacionalmente (registra achado para eles, nao os direciona)
- Nao passa por Gates 13/16
- Nao elimina Agente nem Gestor

---

### PASSO 0 — Leia o estado atual

**O que:** Ler `rotina_fechamento_template.md` e `_estado_wallenberg.md` Secao 1.

**Por que:** Evitar retrabalho. A rodada anterior pode ter deixado Skills parcialmente escritas,
buscas exauridas documentadas, ou itens explicitamente marcados para evitar.

**Quando:** Primeiro passo obrigatorio, antes de qualquer busca.

**Como:**
1. `Read` em `01_CEO/rotina_fechamento_template.md`
2. `Read` em `01_CEO/_estado_wallenberg.md` (Secao 1 — Onde parei)
3. Anotar o que nao fazer antes de comecar

**Criterio de sucesso:** Sabe exatamente o que ja foi feito na rodada anterior e o que evitar.

**Bloqueadores:** Arquivo nao existe (primeira rodada ever) -> criar estado inicial vazio e continuar.

---

### PASSO 1 — Pesquisa externa: Trilha A (Inteligencia)

**O que:** Buscar conhecimento tecnico novo — normas, tecnicas de projetar, regras de projeto, legislacao,
tendencias. Esta trilha gera Skill de conhecimento (nao de ferramenta — ferramenta e Passo 8).

**Por que:** Os Agentes precisam de base tecnica atualizada para executar com qualidade. Sem inteligencia
nova, o organismo estagna no que ja sabia.

**Quando:** Logo apos Passo 0, antes da consolidacao.

**Como — frentes de busca (paralelas):**

| Frente | Fontes priorizadas | Exemplos de termos |
|--------|-------------------|-------------------|
| Legal/RJ | CAU-RJ, SMDU, RIU, normas municipais RJ | LICIN 2.0, CAU-RJ, RDT, PRPA, PREO |
| Arquitetura | SobreArquitetura (YT), sobre.arq (IG), blogs tecnicos | BIM, metodologia de projeto, entregaveis |
| Complementares Trilha A | ABNT, concessionarias, livros tecnicos, YT tecnico | NBR 6118, NBR 5410, hidrossanitario, paisagismo |
| Tendencias | IG: maxcarrau.ia, 99hud, seanaiux, goxyvi | IA arquitetura, produtividade em obra |
| Claude/IA | YT: peaceofcode; Anthropic blog | Claude Code, agentes, automacao |

**Regras:**
- So fontes verificaveis: URL + data + autoria identificavel
- Traduzir ingles -> portugues (Gestores nao tem barreira de idioma eliminada)
- Nao clonar, nao instalar nada — so leitura
- Para Vitruvius: qualquer achado BIM/Revit -> registrar em
  `Gestores/Lucio (Arquitetura)/Agentes/Oscar/vitruvius_achados_candidatos.md`
  ANTES (ou junto) de virar Skill isolada — nunca descartar por omissao

**Criterio de sucesso:** Ao menos 1 achado de substancia por frente relevante.
"Nada novo" e resultado valido — nunca inventar.

**Bloqueadores:**
- Site fora do ar -> registrar, pular, tentar na proxima rodada
- Conteudo so em video -> usar `/watch:watch <URL>` para transcricao
- Instagram bloqueado -> tentar WebFetch no link direto do post

---

### PASSO 2 — Consolidacao

**O que:** Separar sinal de ruido. Classificar cada achado por Gestor/Agente beneficiado.
Decidir o que vira Skill e o que e descartado.

**Por que:** Pesquisa bruta nao vira Skill automaticamente. Sem este filtro, cria-se Skill generica
que ninguem usa (Principio 15 — redundancia zero).

**Quando:** Apos Passo 1, antes de redigir Skills.

**Como:** Para cada achado, responder:
1. E norma/tecnica/ferramenta real ou e opiniao/tendencia vaga?
2. Qual Agente usaria hoje? (Oscar, Hely, Burle, Portinari, Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin)
3. Ja existe Skill cobrindo isso? (checar `01_CEO/Skills_Propostas/2026/{Mes}/` e meses anteriores)
4. E Trilha A (conhecimento -> fica aqui) ou Trilha B (ferramenta -> vai para Passo 8)?

Descartar: conteudo generico sem aplicacao concreta no fluxo atual do organismo.

**Criterio de sucesso:** Lista de achados validados, cada um com Agente-alvo identificado e Trilha definida.

**Bloqueadores:** Achado ambiguo -> errar para o lado conservador, nao criar Skill desnecessaria.

---

### PASSO 3 — Redacao de Skills

**O que:** Transformar cada achado validado (Trilha A) em um arquivo `.md` de Skill.

**Por que:** Conhecimento so e util se esta documentado de forma que o Agente consiga usar
sem precisar de contexto adicional ou da presenca de Wallenberg.

**Quando:** Apos Passo 2.

**Como:**

Estrutura obrigatoria para Skill de Conhecimento (Trilha A):
```
# [Nome do Conhecimento/Norma] — Skill de Conhecimento

## Para qual Agente serve
[nome do Agente e funcao especifica que cobre]

## Status
proposta | implantada

## O que ensina / entrega
[conteudo tecnico operacional — o Agente le isso e sabe o que fazer]

## Fontes
[URL/norma/data de verificacao]

## Limitacoes / o que nao cobre
[honesto sobre o que a Skill nao resolve]
```

Nomenclatura dos arquivos: `{agente}_{assunto-kebab-case}.md`

Regras:
- Checar se ja existe Skill semelhante antes de criar (Principio 15)
- Se existir desatualizada -> atualizar, nao criar nova
- Teste de completude: se o Agente precisar de contexto oral para entender a Skill, ela esta incompleta

**Criterio de sucesso:** Arquivo `.md` autonomo — qualquer um (humano ou Agente) le e entende
sem precisar perguntar nada.

**Bloqueadores:** Achado insuficiente para Skill completa -> criar rascunho com marcador
`[INCOMPLETA — falta: X]` e registrar como pendencia para proxima rodada.
Nunca publicar Skill incompleta como `Status: proposta`.

---

### PASSO 4 — Salvamento local

**O que:** Salvar Skills em `01_CEO/Skills_Propostas/2026/{Mes}/` e atualizar `indice.md` do mes.

**Por que:** Localizacao unica e previsivel — a Drenagem sabe onde procurar.
O indice alimenta a Reuniao Mensal.

**Quando:** Apos Passo 3.

**Como:**
1. Backup: se for atualizacao de Skill existente, copiar antes para `_backups/{AAAA-MM-DD}/`
2. Salvar: `01_CEO/Skills_Propostas/2026/{Mes}/{nome}.md`
3. Atualizar `indice.md`: adicionar linha com `| data | nome | Agente-alvo | resumo 1 linha | status |`

**Criterio de sucesso:** Skill salva no caminho correto. Indice atualizado refletindo estado real.

**Bloqueadores:** Pasta do mes nao existe -> criar antes de salvar.

---

### PASSO 5 — Gerar PDFs

**O que:** Gerar PDF gemeo de cada `.md` criado ou alterado nesta rodada (Skill e indice).

**Por que:** Regra do organismo — todo `.md` de conteudo tem PDF gemeo.
E o formato que vai para externo/cliente se necessario.

**Quando:** Apos Passo 4.

**Como:**
```
python "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\_ferramentas\md_to_pdf.py" "{caminho_do_md}"
```

Gerar um por um. Antes de gerar: checar glifos Unicode no `.md` (setas ->, aspas especiais,
emojis) — viram problema silencioso no PDF (caractere simplesmente some, sem aviso de erro).
Substituir por ASCII antes de gerar.

**Criterio de sucesso:** PDF existe no mesmo diretorio, mesmo nome. Nenhum glifo perdido visivel
por rasterizacao (abrir o PDF e ler o trecho que tinha o caractere suspeito).

**Bloqueadores:**
- Script nao encontrado -> verificar caminho em `_ferramentas/`
- Glifo perdido detectado -> corrigir no `.md` primeiro, gerar de novo

---

### PASSO 6 — Atualizar Painel do Fundador

**O que:** Adicionar ao feed do Painel qualquer evento de hoje que ainda nao esteja la.

**Por que:** O Painel e a interface de Claudemberg com o organismo — se algo aconteceu e nao
esta no Painel, para ele nao aconteceu.

**Quando:** Apos Passo 5. So se houve algo real para registrar.

**Como:**
1. Backup do HTML: `_backups/{AAAA-MM-DD}/painel_fundador_sttk.html`
2. Ler o arquivo publicado ANTES de editar — nunca editar sem ver a versao live
   (causa conflito de merge no Artifact; exige releitura de todas as 600+ linhas do HTML publicado)
3. Para cada evento novo: adicionar objeto no array do feed logo abaixo do marcador `FEED-AUTO`,
   no topo (mais recente primeiro):
   `{d:"DD/MM",et:"TIPO",t:"titulo curto",who:"quem fez",p:"uma frase."}`
   Tipos validos: `decisao`, `promocao`, `agente`, `skill`, `sistema`, `correcao`, `marco`, `capacidade`
4. Atualizar `<span class="updated" id="updated">Atualizado DD/MM/AAAA</span>`
5. Republicar no MESMO URL: `url: https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`
6. Registrar no livro-razao o que atualizou no painel

Se nada aconteceu hoje que mude o painel -> nao publicar, nao inventar evento (Principio 15).

**Criterio de sucesso:** Feed reflete exatamente o que aconteceu. URL permanente inalterado.
Versao publicada bate com o arquivo local (nao ficou pendente de merge).

**Bloqueadores:**
- Conflito de versao no Artifact -> ler a versao publicada completa (WebFetch no URL),
  fazer merge manual, republicar — nunca forcear sem ler a versao mais recente
- HTML corrompido -> restaurar do backup, editar, republicar

---

### PASSO 7 — Learning Agent (auto-melhoria)

**O que:** Buscar 1-3 fontes sobre como melhorar o processo de criacao automatica de conhecimento
e propor (nao executar) melhoria concreta nesta rotina.

**Por que:** A rotina precisa evoluir com a experiencia — sem esse passo, ela estagna
na versao de quando foi escrita.

**Quando:** Apos Passo 6.

**Como:**

Termos de busca:
- "How to automate knowledge base creation"
- "AI creating documentation automatically"
- "Research to skill conversion workflows"
- "Building skills documentation systems automatically"

Para cada fonte encontrada:
1. Ler via WebFetch ou `/watch:watch` (se video)
2. Perguntar: "Qual passo desta rotina seria otimizado com essa tecnica?"
3. Se achar oportunidade real: documentar como proposta — NAO executa, NAO altera o SKILL.md.
   A execucao e Claudemberg quem aprova.

Formato da proposta (registrar no livro-razao ou em nota de rodape do arquivo de estado):
```
Proposta Learning Agent — [data]
Tecnica: [nome]
Fonte: [URL]
Passo afetado: [qual]
Mudanca: [exatamente o que muda]
Impacto esperado: [resultado]
```

Se nao achar nada util -> registrar "learning agent rodou, nenhuma proposta gerada" — nao inventar melhoria.

**Criterio de sucesso:** Proposta documentada com fonte verificavel, ou registro honesto de "nenhuma proposta".

**Bloqueadores:**
- Video inacessivel por JavaScript -> tentar proxima fonte; se todas falharem, registrar e pular

---

### PASSO 8 — Busca de ferramenta (Trilha B) + Skill de Usabilidade

**O que:** Para os Agentes com lacuna de ferramenta conhecida, buscar no GitHub (e equivalentes)
uma ferramenta gratuita, segura, self-hosted, ja funcionando. Documentar como Skill de Usabilidade.
NAO implanta — a implantacao e da Drenagem.

**Por que:** Completar a capacidade tecnica dos Agentes sem depender de SaaS pago.
A Skill de Usabilidade e o contrato que a Drenagem segue para implantar.

**Quando:** Apos Passo 7.

**Como:**

1. Verificar `_estado_{agente}.md` de cada Agente com lacuna conhecida ANTES de buscar
   (nunca copiar mapa de rodada anterior sem checar — estado muda)

Mapa atual (validar antes de usar — atualizado em 27/08/2026):

| Agente | Lacuna | Situacao |
|--------|--------|----------|
| Burle | Render + video self-hosted | WAN 2.2 em andamento — NAO repetir busca |
| Portinari | Apresentacao automatica (slides) | Aberta — PPTAgent descartado 27/08 (fasttext requer Build Tools) |
| Oscar | Automacao BIM/Revit alem do Vitruvius | Aberta — nenhum candidato confirmado |
| Times Cardozo | Ferramentas para 6 areas complementares | Aberta — zero busca feita; prioridade proxima rodada |

2. Criterios obrigatorios (todos ou descarta):
   - Custo zero (sem freemium com trava, sem SaaS com cartao)
   - Sem vazamento de dado de cliente
   - Sem malware (checar por leitura: README, estrelas, forks, atividade recente)
   - Ja funcionando (nao "vamos programar do zero")

3. Se achar candidato valido: redigir Skill de Usabilidade no formato abaixo
   (e o contrato com a Drenagem — precisa bastar sozinha, sem precisar de contexto adicional)

```
# {Nome da Ferramenta} — Skill de Usabilidade

## Para qual Agente serve
[nome e funcao especifica que cobre]

## Status
proposta

## O que faz
[funcao real, nao descricao de marketing]

## Como usar
[comandos, entrada/saida, requisitos tecnicos — GPU, Python, versao, etc. — especifico o bastante
para a Drenagem instalar sem perguntar de volta]

## Evidencia de segurança (Principio 3)
- Custo: [confirmado zero]
- Vazamento de dado: [por que nao vaza — self-hosted, sem upload externo, etc.]
- Idoneidade: [README, estrelas, forks, atividade recente, sem sinal suspeito]

## Limitacoes honestas
[o que nao faz, o que falta]

## Fonte
[link GitHub/oficial, data de verificacao]
```

Esta Skill NAO inclui: confirmacao de que a instalacao funcionou, resultado de teste real,
ou registro de que o Agente ja usa a ferramenta — isso a Drenagem escreve de volta
no campo `Status`.

**Criterio de sucesso:** Skill de Usabilidade completa o suficiente para a Drenagem implantar
sem precisar voltar para perguntar.

**Bloqueadores:**
- Nenhum candidato passa nos criterios -> registrar "busca exaurida, nenhum achado" — nao criar Skill vazia
- Skill incompleta por requisito tecnico desconhecido -> marcar `[INCOMPLETA — falta: X]`,
  nao publicar como `proposta`

---

### SAIDA: Resumo final

Ao terminar, escrever resumo em 5-10 linhas:
- Quantas Skills ativadas e para quais Agentes
- O que foi pesquisado (Trilha A e B, por frente)
- Se Painel foi atualizado e por que
- Se Learning Agent encontrou proposta de melhoria
- O que foi pulado (regra de desbloqueio) e por que

---

---

## ROTINA 2: DRENAGEM CONTINUA

### Objetivo

Drenar a fila de pendencias do organismo: acionar Gestores, executar itens `auto` de
`pendencias.json`, implantar Skills com `Status: proposta`, e registrar tudo no livro-razao.

### Quando roda

Sob demanda (tarefa agendada `wallenberg-drenagem-continua`) ou disparada manualmente.
Claudemberg ausente e o cenario normal — Wallenberg executa sozinho.

### Fronteira — o que nao faz

- Nao busca ferramenta nova por conta propria (isso e da Diaria Skills)
- Nao reescreve Skill da Diaria Skills (sinaliza que esta incompleta, nao corrige sozinho)
- Nao produz documento de cliente
- Nao passa por Gates 13/16
- Nao elimina Gestor ou Agente

---

### PASSO 0 — Leia seu estado

**O que:** Ler `01_CEO/_estado_wallenberg.md` (Secao 1) e `rotina_fechamento_template.md`.

**Por que:** A rodada anterior pode ter deixado pendencias parcialmente resolvidas,
Gestores com decisao represada, ou Skill implantada a meias.

**Como:**
1. `Read` de `01_CEO/_estado_wallenberg.md`
2. `Read` de `01_CEO/rotina_fechamento_template.md`
3. Anotar o que esta em andamento para nao duplicar

**Criterio de sucesso:** Sabe exatamente onde a rodada anterior parou.

---

### PASSO 1 — Descubra os Gestores existentes

**O que:** Listar todos os Gestores ativos do organismo por varredura — nunca por lista hardcoded.

**Por que:** A equipe cresce. Lista fixa deixaria de incluir Gestores novos automaticamente.

**Como:**
```
Glob: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\.claude\agents\*.md
Cruzar com: subpastas de 01_CEO/Gestores/
```

Regra: arquivo `.claude/agents/{nome}.md` + pasta `01_CEO/Gestores/{Nome} (...)/` = Gestor ativo.

Gestores hoje (resultado esperado do Glob, nao hardcode):
- Kelsen (Legal)
- Lucio (Arquitetura)
- Cardozo (Complementares) — adicionado 26/08/2026

Agentes de equipe (Hely, Oscar, Burle, Portinari, Baumgart, etc.) ficam fora desta lista.
Eles aparecem dentro de `01_CEO/Gestores/{Gestor}/Agentes/`.

**Criterio de sucesso:** Lista reflete a realidade atual — nenhum Gestor novo ignorado.

---

### PASSO 2 — Leia `pendencias.json`

**O que:** Ler a fila estruturada e separar por Gestor e alcance.

**Por que:** `pendencias.json` e a fonte unica estruturada da fila. Tudo que precisa de acao
esta la — sem ele, a rodada age no escuro.

**Como:**
1. `Read` de `01_CEO/Pendencias/pendencias.json`
2. Filtrar `status: "aberta"` e `status: "em_pesquisa_alternativa"` (nao so "aberta")
3. Separar por `owner` e por `alc`:

| `alc` | O que fazer |
|-------|-------------|
| `"auto"` | Gestor executa (ou delega ao proprio Agente) — e dentro da alçada aprovada |
| `"humano"` | So reconcilia — confirma se segue real, nao executa |
| `"tecnico"` | Idem |
| `"planejado"` | Idem |

**Criterio de sucesso:** Antes de acionar qualquer Gestor, ja sabe quem deve fazer o que.

---

### PASSO 3 — Para cada Gestor: acionar e executar

**O que:** Acionar cada Gestor um de cada vez, passar suas pendencias `auto`, e receber resultado.

**Por que:** Cada Gestor tem autonomia dentro da propria alçada. Papel de Wallenberg aqui
e de orquestrador, nao executor.

**Quando:** Apos Passo 2. Um Gestor por vez (nao em paralelo — o contexto de cada um
depende de ver o resultado do anterior para decidir prioridade).

**Como:**

**3.a. Verificar ferramenta `Agent` no frontmatter do Gestor**

Ler `.claude/agents/{nome}.md` — se `Agent` esta na lista `tools:`:
- SIM: Gestor aciona seus Agentes diretamente — Wallenberg so recebe o resumo
- NAO: Wallenberg faz a intermediacao (Gestor julga -> Wallenberg aciona o Agente ->
  Wallenberg devolve para o Gestor auditar)

NAO presumir de rodada anterior — ler o frontmatter atual. Capacidade nova concedida a
um Gestor deve estar documentada aqui na mesma sessao em que for confirmada.

**3.b. Montar o prompt do Gestor:**

```
Leia _estado_{gestor}.md e as pendencias abaixo.
1. Reconcilie sua fila antes de reportar.
2. Execute os itens com alc:auto que couberem na sua propria alçada.
3. Faca varredura de melhoria (ver Passo 5 deste playbook).
4. Reporte o que fez, o que ficou em aberto e por que.

Pendencias auto desta rodada para voce:
[lista dos itens alc:auto com owner = este Gestor]
```

**3.c. Se o Gestor nao tem equipe ainda** — so relata pendencias proprias.
Nao administrar exame de nivel dentro desta rotina.

**3.d. Regra de intermediacao Wallenberg-Agente** — So valida se o Gestor nao tem `Agent` no frontmatter.
Neste caso: Gestor julga e pede contexto -> Wallenberg aciona o Agente -> Wallenberg devolve
o artefato para o Gestor auditar (sem julgar o merito do artefato — isso e do Gestor).

**Criterio de sucesso:** Todo Gestor reportou: o que fez, o que ficou aberto, e por que.
Nenhum Gestor silencioso na rodada.

**Bloqueadores:**
- Gestor sem resposta (timeout/falha tecnica) -> registrar, sinalizar no Passo 8.b, continuar
- Ferramenta `Agent` nao disponivel -> fazer intermediacao manual (3.d)

---

### PASSO 4 — Registro no livro-razao

**O que:** Registrar toda execucao real da rodada no livro-razao e atualizar `pendencias.json`.

**Por que:** Rastreabilidade e ratificacao. Claudemberg revisa na Reuniao Semanal — sem registro,
nao consegue revisar nem reverter.

**Quando:** Apos receber resultado de todos os Gestores.

**Como:**

**4.a. Backup antes de editar:**
```
_backups/{AAAA-MM-DD}/Agosto.md  (ou o mes corrente)
_backups/{AAAA-MM-DD}/pendencias.json
```

**4.b. Ler o arquivo atual do livro-razao** (nao editar sem ler primeiro — arquivo grande,
append cego cria duplicata)

**4.c. Adicionar entrada com:**
- Data e contexto da rodada
- Uma secao por Gestor com execucao real (nao misturar todos numa entrada generica)
- O que foi decidido, por que, o que foi criado/alterado, backup criado, como desfazer

**4.d. Checar glifos Unicode antes de gerar PDF:**
- Setas (->) confirmadas como ASCII hifem-maior, nao Unicode (->)
- Emojis ausentes
- Aspas curvadas ausentes
Substituir antes de gerar — nao gerar e depois corrigir.

**4.e. Gerar PDF gemeo** do livro-razao apos confirmar sem glifo.

**4.f. Atualizar `pendencias.json`:** Para cada item resolvido nesta rodada:
- `status` -> `"resolvida"`
- `resolvido_em` -> data de hoje `AAAA-MM-DD`
- NAO apagar o item — e historico

**Criterio de sucesso:** Entrada legivel, com data, por Gestor, com "como desfazer" explicito.
PDF gerado sem glifo perdido. `pendencias.json` atualizado.

**Bloqueadores:**
- Glifo Unicode no livro-razao -> corrigir no `.md` antes de gerar PDF
- Append via Bash falha (caracteres especiais) -> usar Python `io.open` com encoding utf-8

---

### PASSO 5 — Varredura de melhoria (toda rodada, todo Gestor)

**O que:** Mesmo sem pendencia aberta, cada Gestor faz varredura interna de melhoria.

**Por que:** Gestor ocioso sem cliente ativo ainda tem trabalho — melhorar base de conhecimento,
documentar gaps, atualizar POPs. "Sem pendencia" nao e descanso (correcao de Claudemberg em 07/08/2026:
"os agentes precisam estar fazendo algo, pode ser uma melhoria minima").

**Quando:** Incluido no prompt do Passo 3 para cada Gestor.

**Como:** Incluir no prompt:
- "Existe Skill/POP com lacuna que voce ja suspeita mas nunca formalizou?"
- "Existe padrao de erro recorrente na sua equipe?"
- "Algum POP esta desatualizado mas nao virou pendencia?"
- "Algum Agente da sua equipe tem exame de nivel represado?"

Se achar algo real e resolvivel na propria alçada -> executar e registrar.
Se achar algo que depende de outro -> abrir item em `pendencias.json`.
Se varredura for genuinamente vazia -> registrar o que foi checado (nao "nada pendente" seco).

**Criterio de sucesso:** Arquivo de estado do Gestor atualizado com resultado da varredura,
mesmo quando nao ha achado.

---

### PASSO 6 — Atualizar Painel do Fundador

Identico ao Passo 6 da Diaria Skills (mesmo HTML, mesmo URL, mesmo procedimento de merge).

**ATENCAO ao conflito entre rotinas:** Se a Diaria Skills ja atualizou o Painel neste mesmo dia,
ler a versao publicada antes de editar — ela pode ja conter eventos que nao estao no arquivo local.

---

### PASSO 7 — Learning Agent

Se a Diaria Skills ja rodou o Learning Agent nesta data -> pular e registrar:
"Learning Agent ja rodou na Diaria Skills de [data]. Sem duplicacao."

Se nao rodou -> seguir o mesmo procedimento do Passo 7 da Diaria Skills.

---

### PASSO 8 — Implantacao de ferramenta

**O que:** Ler Skills com `Status: proposta` e implantar (instalar, conectar, testar)
exatamente o que cada Skill descreve.

**Por que:** A Diaria Skills cria o contrato do que instalar. Esta rotina executa.
Sem implantacao, a Skill fica so no papel.

**Quando:** Apos Passo 7. Nao bloqueia a rodada se nao houver nada pendente.

**Como:**

1. Listar Skills com `Status: proposta` em `01_CEO/Skills_Propostas/2026/{Mes}/`
2. Para cada uma:

   a. Ler a Skill inteira (nao so o nome)

   b. Verificar se resolve lacuna real hoje (cruzar com `_estado_{agente}.md` — nao instalar
      sem lacuna real confirmada)

   c. Se a Skill estiver incompleta (nao da para instalar sem adivinhar) ->
      marcar `Status: skill incompleta, devolvida para Diaria Skills`
      registrar exatamente o que falta — NAO improvisar

   d. Se suficiente -> implantar seguindo exatamente o que a Skill descreve

3. Testar: confirmar que funciona como descrito (nao em caso de cliente — so validacao tecnica)

4. Atualizar `Status` da Skill:
   - `implantada` (com data e nota do que foi testado)
   - `implantada com ressalva` (algo divergiu — descrever o que)
   - `descartada na implantacao` (bloqueio tecnico real — descrever motivo, para nao buscar de novo)

**Regra de prioridade:** Cliente real > implantacao de ferramenta. Se Gestor com cliente ativo
bloqueou a rodada, implantacao fica para a proxima.

**Regra de excecao:** Nenhuma Skill pendente -> registrar "nenhuma Skill pendente de implantacao"
e seguir — nao inventar implantacao para preencher.

**Criterio de sucesso:** Campo `Status` da Skill atualizado. Registro no livro-razao com resultado
real (funcionou ou nao, e por que).

**Bloqueadores:**
- Dependencia tecnica faltando (ex.: Build Tools ausente, GPU insuficiente) ->
  registrar bloqueio, marcar `descartada na implantacao`, sinalizar para Diaria Skills
  nao propor de novo sem resolver o pre-requisito
- Skill incompleta -> devolver para Diaria Skills com nota especifica do que falta

---

### PASSO 8.b — Autoescalonamento

**O que:** Antes do resumo final, verificar se algum Gestor ficou estagnado nesta rodada ou em varias.

**Por que:** Estagnacao repetida indica gap de ferramenta, exame represado, ou bloqueio nao reportado.
Claudemberg precisa saber — nao descobrir semanas depois.

**Como:**

- Sem progresso nesta rodada ->
  registrar: `"SEM PROGRESSO NESTA RODADA: {Gestor} — verificar se varredura Passo 5 foi real ou so relatada"`

- Padrao repetido (N rodadas sem progresso) ->
  escalar: `"PADRAO DE ESTAGNACAO: {Gestor} sem progresso ha N rodadas — escalar para Claudemberg"`

**Criterio de sucesso:** Claudemberg tem visibilidade de estagnacao no resumo da rodada.

---

### SAIDA: Resumo final

Por Gestor (2-4 linhas cada): o que encontrou, o que resolveu, se acionou Agente.

Total da rodada:
- Gestores passados / com execucao real
- Itens `pendencias.json` fechados
- Skills implantadas / descartadas / devolvidas para Diaria Skills
- Autoescalonamento: Gestores sem progresso (se houver)

---

---

## LACUNAS IDENTIFICADAS EM 27/08/2026

| # | Lacuna | Rotina | Severidade | Acao recomendada |
|---|--------|--------|------------|-----------------|
| 1 | Cardozo nao aparecia no exemplo do Passo 1 da Drenagem (texto so citava Kelsen e Lucio) | Drenagem | Baixa (Glob resolve na pratica) | Corrigido neste playbook |
| 2 | Learning Agent duplicado nas duas rotinas — mesmo passo pode rodar duas vezes no mesmo dia | Ambas | Media | Corrigido neste playbook: Drenagem pula se Diaria Skills ja rodou |
| 3 | Painel atualizado nas duas rotinas — conflito de versao se rodarem proximas | Ambas | Media | Corrigido neste playbook: ler versao publicada antes de editar |
| 4 | `pendencias.json` filtrava so `status: "aberta"` — ignorava `"em_pesquisa_alternativa"` | Drenagem | Media | Corrigido neste playbook: Passo 2 filtra os dois |
| 5 | Mapa de busca do Passo 8 da Diaria Skills com status desatualizado (Burle/WAN 2.2) | Diaria Skills | Media | Corrigido neste playbook: mapa atualizado com nota de cada situacao |
| 6 | Passo 0 ausente na Diaria Skills (mencionava template de fechamento mas nao era passo explicito) | Diaria Skills | Baixa | Corrigido neste playbook: Passo 0 explicito |
| 7 | Criterios de sucesso e bloqueadores ausentes em todos os passos de ambas as rotinas | Ambas | Alta | Corrigido neste playbook: cada passo tem criterio e bloqueador |
| 8 | Exame de nivel de Gestores/Agentes nao tem home claro — aparece em varios lugares como "nao fazer aqui" | Ambas | Alta | Pendente: definir em qual momento/rotina administrar exames |
| 9 | Nao ha processo definido para quando um Gestor NOVO e criado — como ele e integrado as rotinas | Ambas | Media | Pendente: criar checklist de onboarding de Gestor novo |
| 10 | PPTAgent descartado em 27/08 (fasttext requer C++ Build Tools) — Diaria Skills deve buscar alternativa | Diaria Skills | Media | Pendente: Diaria Skills proxima rodada avalia alternativa sem fasttext |

---

## GOVERNANCA

| Regra | Descricao |
|-------|-----------|
| Backup antes de editar | Qualquer arquivo existente -> backup em `_backups/{AAAA-MM-DD}/` antes de abrir |
| Ratificacao posterior | Wallenberg ativa Skills por conta propria; Claudemberg ratifica na Reuniao Semanal |
| Fonte unica de verdade | Campo `Status` da Skill em `Skills_Propostas/` e o unico lugar que diz se esta implantada |
| Fronteira cliente | Duvida entre "organismo" e "cliente" -> trata como cliente, sinaliza para Claudemberg |
| Redundancia zero (P15) | Nunca criar Skill, pendencia ou entrada de livro-razao que ja existe |
| Unicode proibido | Nenhum caractere Unicode em `.md` que gera PDF — substituir por ASCII antes de salvar |
| Versao publicada primeiro | Nunca republicar Painel sem ler a versao publicada — causa conflito de merge |

---

**Criado em:** 27/08/2026
**Autor:** Wallenberg (CEO), baseado nas rotinas v2.3 (Drenagem) e v2.5 (Diaria Skills)
**Proxima revisao:** sempre que uma rotina for alterada — este playbook deve ser atualizado na mesma sessao
