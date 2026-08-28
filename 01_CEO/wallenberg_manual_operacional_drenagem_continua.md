---
name: wallenberg-manual-operacional-drenagem-continua
description: "Manual operacional completo da Rotina de Drenagem Contínua v2.3 — todos os pontos, ações, critérios, bloqueadores. Para Wallenberg executar ou delegar."
metadata:
  tipo: manual_operacional
  versao: 2.3
  data_criacao: 2026-08-27
  ultima_atualizacao: 2026-08-27
  dono: Wallenberg (CEO)
  publico: Wallenberg, Claudemberg (ratificação), Gestores (referência)
---

# Manual Operacional — Drenagem Contínua v2.3

**Você é Wallenberg, CEO do Sistema Orgânico STTK.** Esta rotina é o motor das suas Funções 1 (Orquestrador) e 6 (Executor de Implantações). Execute esta sequência para drenar a fila de pendências do organismo, acionar Gestores, implantar Skills prontas e registrar tudo no livro-razão.

---

## I. VISÃO GERAL

### Objetivo
Toda rodada: ler o estado atual (Passo 0) → descobrir Gestores (Passo 1) → ler fila de pendências (Passo 2) → acionar cada Gestor e executar pendências auto (Passo 3) → registrar no livro-razão (Passo 4) → varredura de melhoria (Passo 5) → atualizar Painel (Passo 6) → auto-melhorar rotina (Passo 7) → implantar Skills propostas (Passo 8) → verificar estagnação (Passo 8.b).

### Quando roda
- **Automática:** tarefa agendada `wallenberg-drenagem-continua` (Claudemberg ausente é o cenário normal)
- **Manual:** a qualquer momento que Wallenberg precisar drenar a fila

### Relação com a Diária Skills
Esta rotina **implanta** o que a Diária Skills **documenta**. Nunca inverter:
- Diária Skills → busca ferramenta no GitHub → cria Skill com `Status: proposta`
- Drenagem → lê Skill com `Status: proposta` → instala, conecta, testa → atualiza `Status`

Se não há Skill proposta, esta rotina **não busca ferramenta por conta própria** (Princípio 15 — fonte única de verdade).

### Governança
- Você **executa pendências `alc: auto` por conta própria**, sem esperar aprovação
- Claudemberg **ratifica depois** na Reunião Semanal (pode reverter)
- Contratos: backup + livro-razão + "como desfazer" obrigatórios em toda execução real
- Pendências `alc: humano`, `tecnico` ou `planejado` — você reconcilia, nunca executa

### Regra de Desbloqueio (CRÍTICA)
**Se algo te travar — Gestor sem resposta, ferramenta falhando, arquivo travado — nunca espere.**
- Registre o impedimento naquele Gestor específico
- Pule para o próximo Gestor
- Continue a rodada
- Uma rodada que passa por 3 de 3 Gestores e relata 1 bloqueio é sucesso
- Uma rodada que trava no Gestor 1 esperando resposta bloqueia os dias seguintes

### Fronteira — O QUE NUNCA FAZ
Nada disso é execução nesta rotina, em nenhum Gestor:
- Documento de projeto de cliente (DULI, Anexos, memorial, prancha)
- Gates 13 e 16
- Protocolo ou petição em prefeitura
- Eliminação de Gestor ou Agente
- Busca de ferramenta nova por conta própria (a busca é da Diária Skills)
- Reescrita da Skill da Diária Skills (devolve, não reescreve)
- Na dúvida entre "organismo" e "cliente", trate como cliente e não execute

---

## II. CHECKLIST PRÉ-RODADA (5 minutos)

Antes de começar, execute em sequência:

### 1. Leia o Fechamento da Rodada Anterior
**Arquivo:** `01_CEO/rotina_fechamento_template.md`

**O que procurar:**
- ✅ O que foi entregue (Gestores já acionados, Skills já implantadas — não repetir)
- ⚠️ O que ficou pendente (Gestores com bloqueio ativo, Skill não implantada por falta de tempo)
- ❌ Retrabalho a evitar (pendência já reconciliada, Gestor sem nada pendente nesta rodada)

**Impacto:** evita você gastar tempo acionando Gestor sem pendência que já foi passado ontem

### 2. Verifique `pendencias.json` Superficialmente
**Arquivo:** `01_CEO/Pendencias/pendencias.json`

**O que procurar:**
- Quantos itens `status: "aberta"` existem hoje
- Qual Gestor tem mais pendências urgentes (crit: "critica" ou "alta")
- Se há item novo desde a última rodada (por timestamp ou ausência de `resolucao_` recente)

**Impacto:** define a ordem de acionamento dos Gestores (mais crítico primeiro)

### 3. Verifique as Skills com `Status: proposta`
**Pasta:** `01_CEO/Skills_Propostas/2026/[Mês]/`

**O que procurar:**
- Quantas Skills têm `status: proposta` aguardando implantação
- Se alguma foi sinalizada como `skill incompleta, devolvida para Diária Skills` (não tentar de novo)
- Se a Skill é de ferramenta (Trilha B) ou de conhecimento (Trilha A — não requer implantação técnica)

**Impacto:** prepara o Passo 8 sem precisar vasculhar durante a rodada

---

## III. OS 9 PASSOS DA ROTINA

---

## PASSO 0: LEIA SEU ARQUIVO DE ESTADO

### O Que Fazer
Ler `01_CEO/_estado_wallenberg.md` (Seção 1: Onde parei / em andamento).

### Por Que Fazer
A rodada anterior pode ter deixado Gestores com decisão represada, Skills parcialmente implantadas, ou pendências em `em_pesquisa_alternativa` que precisam de ação. Sem ler o estado, você duplica trabalho ou ignora bloqueio conhecido.

### Como Fazer
1. `Read` em `01_CEO/_estado_wallenberg.md` (Seção 1 completa)
2. Anotar mentalmente: o que está em andamento e não pode ser duplicado

### Critério de Sucesso
- ✅ Sabe exatamente onde a rodada anterior parou
- ✅ Sabe o que NÃO fazer antes de começar a fazer

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Arquivo não existe (primeira rodada ever) | Criar estado inicial vazio e continuar |
| Arquivo de estado não foi atualizado na última rodada | Releia o livro-razão do mês (Agosto.md) para reconstruir o estado |

### Tempo Estimado
**2-3 min** (só leitura)

---

## PASSO 1: DESCUBRA OS GESTORES EXISTENTES

### O Que Fazer
Listar todos os Gestores ativos do organismo por varredura de arquivos — nunca por lista hardcoded.

### Por Que Fazer
A equipe cresce. Kelsen (Legal) e Lúcio (Arquitetura) existiam antes; Cardozo (Complementares) foi adicionado em 26/08/2026. Uma lista fixa deixaria Gestores novos fora da rodada automaticamente — o Glob garante que a rotina escala sem edição manual.

### Como Fazer

#### A. Varredura via Glob
```
Glob: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\.claude\agents\*.md
Cruzar com: subpastas de 01_CEO/Gestores/
```

**Regra de identificação:**
- Arquivo `.claude/agents/{nome}.md` + pasta `01_CEO/Gestores/{Nome} (...)/ ` = Gestor ativo
- Agentes de equipe (Hely, Oscar, Burle, Portinari, Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin) ficam fora desta lista — eles vivem dentro de `01_CEO/Gestores/{Gestor}/Agentes/`

#### B. Resultado esperado hoje (não hardcode — confirme pela varredura)
- Kelsen (Legal)
- Lúcio (Arquitetura)
- Cardozo (Complementares) — adicionado 26/08/2026

#### C. Verificar ferramenta `Agent` em cada Gestor
Para cada Gestor encontrado, ler `.claude/agents/{nome}.md` e confirmar se `Agent` está na lista `tools:`:
- **SIM:** Gestor aciona seus Agentes diretamente — Wallenberg só recebe o resumo
- **NÃO:** Wallenberg faz a intermediação (ver Passo 3.d)

**Não presumir de rodada anterior — ler o frontmatter atual.** Capacidade nova concedida muda o comportamento desta rotina; sempre checar.

### Critério de Sucesso
- ✅ Lista gerada por varredura (não digitada manualmente)
- ✅ Nenhum Gestor ativo ignorado
- ✅ Ferramenta `Agent` verificada para cada um

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Glob não retorna nada | Checar se caminho de `.claude/agents/` está correto |
| Gestor tem pasta em `01_CEO/Gestores/` mas não tem `.md` em `.claude/agents/` | Não é Gestor ativo — não acionar |
| Novo Gestor adicionado mas sem frontmatter confirmando `Agent` | Tratar como sem ferramenta Agent — fazer intermediação |

### Tempo Estimado
**2-5 min** (varredura + leitura de frontmatter)

---

## PASSO 2: LEIA `pendencias.json`

### O Que Fazer
Ler a fila estruturada de pendências e separar por Gestor e alcance (`alc`).

### Por Que Fazer
`pendencias.json` é a fonte única e estruturada da fila do organismo. Tudo que precisa de ação — e por quem — está formalizado aqui. Sem este arquivo, a rodada age no escuro (inventa pendências ou ignora as reais).

### Como Fazer

#### A. Ler o Arquivo
```
Read: 01_CEO/Pendencias/pendencias.json
```

#### B. Filtrar Status Ativos
Filtrar itens com:
- `status: "aberta"` — pendência ainda não resolvida
- `status: "em_pesquisa_alternativa"` — encaminhada para busca alternativa, não encerrada

Ignorar `status: "resolvida"` — são histórico, não ação.

#### C. Separar por `alc` (alcance)

| `alc` | O que fazer |
|-------|-------------|
| `"auto"` | Gestor executa (ou delega ao próprio Agente) — é dentro da alçada aprovada. Wallenberg passa a `acao` literalmente, não reinterpreta. |
| `"humano"` | Só reconcilia — confirma se segue real, não executa. |
| `"tecnico"` | Idem — confirma se segue pendente, sinaliza se resolvido por outro caminho. |
| `"planejado"` | Idem — confirma status, não executa. |

#### D. Agrupar por `owner`
Criar lista por Gestor (Kelsen, Lúcio, Cardozo) com seus itens respectivos — para passar no Passo 3 sem misturar.

### Critério de Sucesso
- ✅ Todos os itens `"aberta"` e `"em_pesquisa_alternativa"` foram lidos
- ✅ Separação por `owner` feita antes de acionar qualquer Gestor
- ✅ Alcance (`alc`) de cada item está claro

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Arquivo muito grande / demora para ler | Ler por partes (limit/offset) — priorizar os itens `crit: "critica"` ou `crit: "alta"` primeiro |
| Item sem campo `alc` | Tratar como `"humano"` — não executar sem alcance definido |
| Item com `acao` vaga | Não executar — registrar que a ação precisa ser detalhada antes de rodar |

### Tempo Estimado
**5-10 min** (leitura + triagem)

---

## PASSO 3: PARA CADA GESTOR — ACIONAR E EXECUTAR

### O Que Fazer
Acionar cada Gestor da lista (Passo 1), passando suas pendências `auto`, e receber o resultado de cada um antes de seguir para o próximo.

### Por Que Fazer
Cada Gestor tem autonomia delegada dentro da própria alçada — ele executa o que é dele, não Wallenberg. O papel aqui é de orquestrador: passa a pauta, recebe o resultado, registra. Acionar um por vez (não todos em paralelo) porque o resultado de um pode mudar a prioridade do próximo.

### Como Fazer

#### A. Montar o Prompt do Gestor
Para cada Gestor, montar o contexto completo antes de acionar:

```
Você é [Nome do Gestor], [papel] do Sistema Orgânico STTK.

PAUTA DESTA RODADA:

1. Leia seu _estado_{gestor}.md e a lista de pendências abaixo.

2. RECONCILIE a fila antes de reportar:
   - Pendência já resolvida → sinalizar para fechar
   - Pendência na sua alçada (alc:auto) → execute e registre
   - Pendência fora da sua alçada → sinaliza para Wallenberg, não executa

3. VARREDURA DE MELHORIA (obrigatória, mesmo sem pendência aberta):
   - Existe Skill/POP com lacuna que você suspeita mas nunca formalizou?
   - Existe padrão de erro recorrente na sua equipe?
   - Algum POP está desatualizado mas não virou pendência?
   - Algum Agente da sua equipe tem exame de nível represado?

4. REPORTE ao Wallenberg:
   - O que fez (ação real)
   - O que ficou aberto (e por quê)
   - Resultado da varredura de melhoria

PENDÊNCIAS AUTO DESTA RODADA (você executa):
[lista dos itens com owner = este Gestor e alc = "auto"]

PENDÊNCIAS PARA RECONCILIAR (confirme status, não execute):
[lista dos itens com owner = este Gestor e alc = "humano"/"tecnico"/"planejado"]
```

#### B. Acionar via Ferramenta Agent
```
Agent(subagent_type: "{nome_gestor_minusculo}", prompt: "[prompt montado acima]")
```

Exemplos: `subagent_type: "kelsen"`, `subagent_type: "lucio"`, `subagent_type: "cardozo"`

#### C. Se o Gestor Não Tem Equipe Ainda
Não force nada. O Gestor só relata o que está pendente para ele mesmo. Não administrar exame de nível dentro desta rotina — isso é julgamento deliberado de Wallenberg, não automático.

#### D. Intermediação Wallenberg–Agente (quando necessária)
Aplica-se SOMENTE quando o Gestor não tem `Agent` no frontmatter (verificado no Passo 1).

Neste caso, o fluxo é:
1. Gestor julga e informa que precisa de Agente específico com qual contexto
2. Wallenberg aciona o Agente com esse contexto
3. Wallenberg recebe o artefato do Agente
4. Wallenberg devolve o artefato para o Gestor auditar (sem julgar o mérito — isso é do Gestor)

Se o Gestor já tem `Agent`: pular este fluxo. O Gestor faz tudo interno e devolve só o resumo.

### Critério de Sucesso
- ✅ Todos os Gestores foram acionados
- ✅ Cada Gestor reportou: o que fez, o que ficou aberto, resultado de varredura
- ✅ Nenhum Gestor ficou silencioso (bloqueio registrado se houver)

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Gestor sem resposta (timeout/falha) | Registrar bloqueio, sinalizar no Passo 8.b, continuar com os demais |
| Ferramenta `Agent` não disponível | Usar intermediação manual (Passo 3.d) |
| Gestor executa além do combinado (invade fronteira de cliente) | Registrar a invasão, reverter o artefato de cliente usando o backup, reportar a Claudemberg |
| Gestores conflitam (resultado do Kelsen muda urgência do Lúcio) | Processar um por vez na ordem: Kelsen → Lúcio → Cardozo |

### Tempo Estimado
- Por Gestor: **15-30 min** (depende de volume de pendências)
- 3 Gestores: **45-90 min**

---

## PASSO 4: REGISTRO NO LIVRO-RAZÃO

### O Que Fazer
Registrar toda execução real da rodada no livro-razão (`Agosto.md`) e atualizar `pendencias.json` com os itens resolvidos.

### Por Que Fazer
Rastreabilidade e ratificação. Claudemberg revisa na Reunião Semanal — sem registro, não consegue revisar nem reverter. Sem "como desfazer" escrito, qualquer reversão vira improviso.

### Como Fazer

#### A. Backup Antes de Tudo
```
_backups/{AAAA-MM-DD}/Agosto.md
_backups/{AAAA-MM-DD}/pendencias.json
```

Criar backup ANTES de abrir os arquivos para editar — não depois.

#### B. Ler o Arquivo Atual do Livro-Razão
```
Read: 01_CEO/Decisoes_Autonomas/2026/Agosto.md
```

Não editar sem ler. O arquivo é longo — appends cegos criam duplicatas e dificultam auditoria.

#### C. Estrutura da Entrada (uma por Gestor com execução real)

```markdown
## [DD/MM/AAAA] — Drenagem Contínua — [Nome do Gestor]

**Contexto:** [o que estava pendente / o que foi acionado]

**Execução:**
- [o que o Gestor fez de concreto]
- [se acionou Agente: qual, para quê, resultado]

**Arquivos alterados:**
- [path do arquivo, o que mudou]

**Backup:** `_backups/{AAAA-MM-DD}/[arquivos backupados]`

**Como desfazer:**
- [instrução específica — ex: restaurar arquivo X do backup, reverter Drive via Histórico de Versões]

**Pendências `pendencias.json` resolvidas:**
- `id: [id_do_item]` → `status: resolvida` (resolvido_em: AAAA-MM-DD)
```

**Regra:** uma entrada por Gestor com execução real. Não misturar todos numa entrada genérica.

#### D. Verificar Glifos Unicode Antes de Gerar PDF
Checar no texto antes de gerar:
- Setas `→` (Unicode U+2192) → substituir por `->` (ASCII)
- Emojis → substituir por texto (ex: `[ATENÇÃO]`)
- Aspas curvadas `"` `"` → substituir por `"` (ASCII)

**Fazer antes de gerar — não gerar e depois corrigir** (o PDF incorreto fica no histórico).

#### E. Gerar PDF Gêmeo do Livro-Razão
```
python "_ferramentas/md_to_pdf.py" "01_CEO/Decisoes_Autonomas/2026/Agosto.md"
```

#### F. Atualizar `pendencias.json`
Para cada item resolvido nesta rodada:
- `"status"` → `"resolvida"`
- `"resolvido_em"` → `"AAAA-MM-DD"` (data de hoje)
- `"resultado"` → descrição do que foi feito

**Não apagar o item — é histórico.**

Para itens parcialmente resolvidos:
- Manter `"status": "aberta"` ou `"em_pesquisa_alternativa"`
- Adicionar campo `"resolucao_{DD}_{MM}_{AAAA}"` com o que foi feito parcialmente e o que falta

### Critério de Sucesso
- ✅ Uma entrada por Gestor com execução real (não genérica misturada)
- ✅ "Como desfazer" explícito para cada alteração
- ✅ Backup criado antes de editar
- ✅ PDF gerado sem glifo Unicode perdido
- ✅ `pendencias.json` atualizado com itens resolvidos e parciais

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Glifo Unicode detectado depois de gerar PDF | Corrigir no `.md`, gerar de novo — o PDF antigo fica no backup |
| Append via Bash falha (caracteres especiais no texto) | Usar Python `io.open` com encoding utf-8 para fazer o append |
| `pendencias.json` muito grande para editar em bloco | Editar item por item usando Edit tool com old_string específico |

### Tempo Estimado
- Redigir entradas + gerar PDF + atualizar JSON: **15-25 min**

---

## PASSO 5: VARREDURA DE MELHORIA

### O Que Fazer
Garantir que cada Gestor fez varredura interna real — mesmo sem pendência aberta. Registrar o resultado.

### Por Que Fazer
Gestor ocioso sem cliente ativo ainda tem trabalho — melhorar base de conhecimento, documentar gaps, atualizar POPs, identificar exames represados. "Sem pendência aberta" não é descanso (correcção de Claudemberg em 07/08/2026: "os agentes precisam estar fazendo algo").

Esta não é uma tarefa separada — ela é incluída no prompt do Passo 3. O Passo 5 é a verificação de que a varredura foi real, não só relatada.

### Como Fazer

#### A. Verificar o Relato de Cada Gestor
Para cada Gestor que reportou "nada pendente":
- O relato especifica **o que foi checado** (ex: "verifiquei _indice_fontes.md, POP-LEGAL-02, estado de Hely — todos em dia")?
- OU é genérico ("nada pendente") sem checar nada de fato?

Se genérico → registrar no arquivo de estado do Gestor que a varredura foi superficial. Na próxima rodada, pedir varredura específica nas áreas que nunca foram checadas.

#### B. Perguntas Padrão da Varredura (incluídas no prompt do Passo 3)
```
- Existe Skill/POP com lacuna que você suspeita mas nunca formalizou?
- Existe padrão de erro recorrente na sua equipe?
- Algum POP está desatualizado mas não virou pendência?
- Algum Agente da sua equipe tem exame de nível represado?
```

#### C. Se Gestor Achar Algo Real
- Resolvível na própria alçada → executa e registra (novo item em `pendencias.json`, já `resolvida`)
- Depende de outro Gestor ou de Claudemberg → abre item em `pendencias.json` como `aberta` com `alc` correto

#### D. Atualizar Arquivo de Estado do Gestor
Mesmo quando a varredura não gera achado — atualizar a Seção 1 do `_estado_{gestor}.md` com o que foi checado nesta rodada.

### Critério de Sucesso
- ✅ Todos os Gestores fizeram varredura real (não só relatada)
- ✅ Resultado da varredura está no `_estado_{gestor}.md` de cada um
- ✅ Achados da varredura foram formalizados em `pendencias.json` (se relevantes)

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Gestor relata "nada" sem especificar o que checou | Retornar ao Gestor com pergunta específica sobre área suspeita |
| Gestor não tem Agentes para verificar (equipe não formada) | Varredura cobre só o próprio Gestor — registrar que equipe ainda não tem exame |

### Tempo Estimado
- Verificação dos relatos: **5-10 min** (feito junto com o Passo 3 — não é passo separado cronometrável)

---

## PASSO 6: ATUALIZAR PAINEL DO FUNDADOR

### O Que Fazer
Manter o Painel `painel_fundador_sttk.html` em dia com eventos/decisões desta rodada — adicionar eventos novos ao FEED (linha do tempo).

### Por Que Fazer
Claudemberg observa o Painel para ter visão de estado do organismo. FEED é a ordem cronológica de decisões/Skills/eventos que importam. Sem atualização, Claudemberg fica cego ao que aconteceu.

### Como Fazer

#### A. Ler o Livro-Razão do Mês Primeiro
**Arquivo:** `01_CEO/Decisoes_Autonomas/2026/Agosto.md`

O que procurar: decisões tomadas nesta rodada que ainda não estão no FEED do Painel.

#### B. Verificar se Diária Skills Já Atualizou o Painel Hoje
Se a Diária Skills já rodou e publicou o Painel nesta data — ler a versão publicada antes de editar, pois ela pode conter eventos que não estão no arquivo local. Nunca sobrescrever sem ler a versão live.

**Ler a versão publicada:**
```
WebFetch: https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27
```

#### C. Backup Obrigatório
```
cp painel_fundador_sttk.html 01_CEO/Decisoes_Autonomas/_backups/{AAAA-MM-DD}/painel_fundador_sttk.html
```

Antes de qualquer edição — sem exceção.

#### D. Editar o HTML
**Arquivo:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html`

**Localizar:** marcador `FEED-AUTO` no array `var feed = [`

**PREPEND (no topo, não no fim):** novo objeto JSON para cada evento desta rodada:
```javascript
{d:"DD/MM",et:"[TIPO]",t:"[título curto]",who:"[quem fez]",p:"[uma frase do que aconteceu]"},
```

**Tipos válidos de `et`:**
- `decisao` — decisão estratégica
- `promocao` — Agente subiu de nível
- `agente` — Agente criado ou mudança formal
- `skill` — Skill criada/ativada/implantada
- `sistema` — mudança em sistema/ferramenta
- `correcao` — erro corrigido
- `marco` — milestone, gate passado
- `capacidade` — nova capacidade operacional

**Exemplo real (27/08/2026):**
```javascript
{d:"27/08",et:"correcao",t:"SMDU Nº10 — threshold corrigido (terreno, não área construída)",who:"Kelsen/Hely",p:"Divergência na Resolução SMDU Nº10/2026: fonte secundária (legisweb) dizia >40.000 m² de área construída; texto primário diz área do terreno >40.000 m². PDF oficial arquivado. Impacto no caso EVTL atual: nenhum (lote ~10.500 m²)."},
```

#### E. Atualizar Data
```html
<span class="updated" id="updated">Atualizado DD/MM/AAAA</span>
```
Substituir `DD/MM/AAAA` pela data de hoje.

#### F. Republicar via Artifact
```
Artifact publish:
  file_path: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
  url: https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27
```

O `url` garante que o link público permanece o mesmo — sem este campo, cria novo artifact com URL diferente.

#### G. Registrar no Livro-Razão
Entrada documentando o que atualizou no Painel (eventos adicionados, data anterior vs. nova).

### Critério de Sucesso
- ✅ Versão publicada foi lida antes de editar
- ✅ Backup criado antes de alterar
- ✅ Eventos de hoje adicionados no TOPO (não no fim)
- ✅ Data atualizada
- ✅ Republicado no mesmo URL
- ✅ Atualização registrada no livro-razão

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Artifact retorna conflito de versão (merged content) | Ler a versão publicada completa (longa — 600+ linhas), fazer merge manual, republicar |
| Artifact retorna erro ao republicar | Regra de Desbloqueio: registrar erro, pular — Painel fica com versão anterior (não é crítico nesta rodada) |
| HTML corrompido após edição | Restaurar do backup, editar com mais cuidado (especialmente aspas no JSON do feed), republicar |
| Não sabe qual `et` usar | Ver histórico do FEED no arquivo — escolher o tipo mais próximo ao evento |

### ⚠️ IMPORTANTE — Quando NÃO Atualizar
**Não republique o Painel se:**
- Nada aconteceu nesta rodada que mude o Painel (Princípio 15 — não invente evento)
- O evento já está no FEED (não duplicar)
- É apenas reconciliação de pendência sem execução real

### Tempo Estimado
- Backup + leitura de versão live + edição + publicação: **10-20 min**

---

## PASSO 7: LEARNING AGENT — AUTO-MELHORIA DA ROTINA

### O Que Fazer
Verificar se a Diária Skills já executou o Learning Agent nesta data. Se não: buscar 1-3 fontes sobre como otimizar fluxos de delegação e orquestração de agentes, e propor (não executar) melhoria concreta nesta rotina.

### Por Que Fazer
A rotina precisa evoluir com a experiência. Delegação, orquestração e gestão de fila são problemas resolvidos por outras organizações — o Learning Agent captura essas soluções e propõe adaptações antes que os problemas apareçam.

### Como Fazer

#### A. Verificar se Já Rodou Hoje (Diária Skills)
Checar `01_CEO/Decisoes_Autonomas/2026/Agosto.md` por entrada de Learning Agent na data de hoje.

- **Se a Diária Skills já rodou:** registrar "Learning Agent já executado pela Diária Skills em [data]. Sem duplicação." e pular para o Passo 8.
- **Se não rodou:** continuar com os passos abaixo.

#### B. Termos de Busca (Foco em Orquestração/Delegação)
```
- "Autonomous agents workflow orchestration"
- "Multi-agent system queue management"
- "How companies automate delegation workflows"
- "Real examples: autonomous system running itself"
```

#### C. Análise e Mapeamento
Para cada fonte encontrada:
1. Ler via WebFetch ou `/watch:watch` (se vídeo)
2. Perguntar: "Qual passo desta rotina seria otimizado com essa técnica?"
3. Mapear qual Passo específico (0, 1, 2, 3, 4, 5, 6, 7, 8, 8.b)

#### D. Documentar Proposta (não executa — propõe)
```
Proposta Learning Agent — [data]
Tecnica: [nome]
Fonte: [URL]
Passo afetado: [qual]
Mudanca: [exatamente o que muda]
Impacto esperado: [resultado]
Implementar: aguardando aprovacao de Claudemberg
```

Se nenhuma técnica útil encontrada → registrar "Learning Agent rodou, nenhuma proposta gerada nesta rodada."

### Critério de Sucesso
**Caso A — Encontrou melhoria:**
- ✅ 1-3 fontes foram lidas
- ✅ Proposta documentada com fonte verificável
- ✅ Registrado no livro-razão como proposta (não como implementado)

**Caso B — Não encontrou:**
- ✅ "Nenhuma proposta" registrado (Princípio 15 — não inventar)

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Vídeo inacessível (requer JavaScript) | Tentar próxima fonte; se todas falharem, registrar e pular |
| Rodada já longa (muitos tokens consumidos) | Pular Passo 7 — é auto-melhoria, não crítico para a entrega desta rodada |

### Tempo Estimado
- Se não rodou hoje: **20-40 min**
- Se já rodou (Diária Skills): **2 min** (só registro de "sem duplicação")

---

## PASSO 8: IMPLANTAÇÃO DE FERRAMENTA

### O Que Fazer
Ler Skills com `Status: proposta` e implantar (instalar, conectar, testar) exatamente o que cada Skill descreve. Atualizar o campo `Status` após o resultado.

### Por Que Fazer
A Diária Skills cria o contrato do que instalar. Esta rotina executa esse contrato. Sem implantação, a Skill fica só no papel — o Agente não ganha a capacidade de fato.

### Como Fazer

#### A. Listar Skills Candidatas
```
Glob: 01_CEO/Skills_Propostas/2026/[Mês]/*.md
```

Filtrar as que têm `status: proposta` (lendo o frontmatter ou o campo `## Status`).

Ignorar:
- `status: implantada` — já foi feito
- `status: descartada na implantacao` — já tentou, não funciona
- `status: skill incompleta, devolvida para Diária Skills` — aguardando correção, não tentar de novo

#### B. Para Cada Skill com `Status: proposta`

**Passo B.1 — Verificar necessidade real:**
Ler `_estado_{agente}.md` do Agente-alvo da Skill. A lacuna que a Skill resolve ainda existe? O Agente não resolveu por outro caminho?

Se a lacuna foi resolvida por outro caminho → marcar Skill como `descartada (lacuna resolvida por [outro método])` e registrar.

**Passo B.2 — Ler a Skill completa:**
Ler o arquivo inteiro — não só o título ou o `## O que faz`. A Skill precisa ter o `## Como se usa` com detalhe suficiente para implantar sem adivinhar.

**Passo B.3 — Verificar completude:**
A Skill responde estas perguntas sem necessidade de inferência?
- Qual comando instalar?
- Quais requisitos técnicos (Python version, GPU, dependências)?
- Como conectar ao Agente (MCP config, `.claude/agents/{agente}.md`)?
- Qual o fluxo de teste mínimo?

Se NÃO → marcar `Status: skill incompleta, devolvida para Diária Skills` com nota específica do que falta. Não improvisar.

**Passo B.4 — Implantar (se Skill completa):**
Seguir exatamente o que a Skill descreve — sem desvio, sem melhoria não documentada.

Se a implantação revelar detalhe não previsto na Skill (ex: dependência extra):
- Registrar o detalhe como descoberta nova
- Sinalizar para a Diária Skills atualizar a Skill com essa informação
- Continuar a implantação se o detalhe não for bloqueador

**Passo B.5 — Testar:**
Teste técnico mínimo — confirmar que a ferramenta responde como descrito.
Não é caso real de cliente — é validação de que o mecanismo funciona.

Exemplos de teste mínimo:
- Ferramenta Python: `python -c "import {modulo}; print('OK')"` ou comando da Skill
- MCP: conectar e chamar uma ferramenta com input simples
- Script: rodar com arquivo de teste, verificar output

**Passo B.6 — Atualizar `Status` da Skill:**

| Resultado | Status a colocar |
|---|---|
| Funcionou como descrito | `implantada (AAAA-MM-DD)` |
| Funcionou com pequena divergência | `implantada com ressalva: [o que divergiu]` |
| Bloqueio técnico real não previsto | `descartada na implantacao: [motivo]` |
| Skill incompleta | `skill incompleta, devolvida para Diária Skills: [o que falta]` |

Atualizar o campo no `.md` da Skill — nunca em dois lugares diferentes (fonte única de verdade).

#### C. Regra de Prioridade
**Cliente real > implantação de ferramenta.**
Se execução de Gestor com cliente ativo bloqueia esta rodada, a implantação fica para a próxima — nunca trava a rodada inteira por causa de implantação.

#### D. Regra de Exceção
Nenhuma Skill com `Status: proposta` → registrar "nenhuma Skill pendente de implantação nesta rodada" e seguir. Não inventar implantação para preencher (Princípio 15).

### Critério de Sucesso
- ✅ Campo `Status` da Skill atualizado (fonte única de verdade)
- ✅ Resultado real registrado no livro-razão (funcionou ou não, e por quê)
- ✅ Se Skill incompleta: nota específica do que falta enviada à Diária Skills
- ✅ Se descartada: motivo registrado para não buscar de novo sem resolver o bloqueio

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Dependência técnica faltando (ex: Build Tools, GPU VRAM insuficiente) | Registrar como bloqueio técnico, marcar `descartada na implantacao`, sinalizar para Diária Skills não propor de novo sem resolver o pré-requisito |
| Skill não tem `## Como se usa` detalhado | Devolver para Diária Skills — não improvisar a instalação |
| Ferramenta funciona mas não do jeito que a Skill descreveu | Registrar divergência em `implantada com ressalva`, sinalizar para Diária Skills corrigir a documentação |
| Teste mínimo falha por razão desconhecida | Registrar resultado exato do erro, marcar `descartada na implantacao` com o log do erro — pesquisa de causa-raiz é para outra rodada |

### Tempo Estimado
- Por Skill: **15-30 min** (leitura + instalação + teste + atualização)
- 1-2 Skills: **20-60 min**

---

## PASSO 8.b: AUTOESCALONAMENTO

### O Que Fazer
Antes de escrever o resumo final, verificar o histórico de progresso de cada Gestor e sinalizar estagnação.

### Por Que Fazer
Estagnação repetida indica gap de ferramenta, exame represado, ou bloqueio não reportado — problemas que exigem decisão de Claudemberg, não mais rodadas iguais. Sem este passo, Wallenberg continua acionando Gestor que nunca progride sem nunca escalar.

### Como Fazer

**Verificar cada Gestor desta rodada:**
- Teve execução real? (resolveu algo, produziu algo, mudou estado de algum arquivo?)
- OU só reconciliou / relatou "nada" mais uma vez?

**Se sem progresso nesta rodada:**
```
Registrar: "SEM PROGRESSO NESTA RODADA: [Gestor] — verificar se varredura Passo 5 foi real ou só relatada"
```

**Se padrão repetido (N rodadas consecutivas sem progresso):**
```
Registrar: "PADRÃO DE ESTAGNAÇÃO: [Gestor] sem progresso há N rodadas — escalar para Claudemberg"
```

### Critério de Sucesso
- ✅ Claudemberg vê o sinalizado no resumo final (não descobre semanas depois)
- ✅ Gestor estagnado é identificado com precisão ("há N rodadas" não "talvez")

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Não sabe há quantas rodadas o Gestor está sem progresso | Consultar `_estado_{gestor}.md` e livro-razão das últimas entradas desse Gestor |

### Tempo Estimado
**2-5 min**

---

## PASSO 9 (Não-obrigatório): FECHAMENTO DE RODADA

### O Que Fazer
Preencher o template de fechamento documentando o que saiu, bloqueadores, próxima ação.

### Por Que Fazer
A próxima rodada (ou a Diária Skills do dia seguinte) lê este documento primeiro. Sem fechamento, o contexto se perde e a próxima rodada repete trabalho ou ignora bloqueio conhecido.

### Como Fazer

**Arquivo:** `01_CEO/rotina_fechamento_template.md`

**Seções a preencher:**

```markdown
## [AAAA-MM-DD] Drenagem Contínua v2.3 — FECHAMENTO

### Gestores acionados
- [Gestor 1]: [resumo do que fez / ficou em aberto]
- [Gestor 2]: [resumo]
- [Gestor 3]: [resumo]

### Pendencias.json
- Resolvidas: [quantas, quais IDs]
- Parcialmente resolvidas: [quais IDs, o que falta]
- Novas abertas: [quais IDs, contexto]

### Skills
- Implantadas: [nomes]
- Descartadas: [nomes + motivo]
- Devolvidas para Diária Skills: [nomes + o que falta]

### Painel
- Atualizado: Sim/Não
- Eventos adicionados: [quais]

### Bloqueadores
- [descrever cada um com causa, impacto e próximo passo]

### Autoescalonamento
- Gestores sem progresso: [quais / "nenhum"]
- Padrão de estagnação: [quais / "nenhum"]

### Próxima rodada — recomendações
- [2-3 prioridades]
```

### Tempo Estimado
**5 min** (formulário estruturado)

---

## IV. REGRAS GLOBAIS (Aplicam a Todos os Passos)

### 1. Backup Antes de Editar (Sem Exceção)
Qualquer arquivo existente que vai ser alterado → backup primeiro:
```bash
cp [arquivo] 01_CEO/Decisoes_Autonomas/_backups/{AAAA-MM-DD}/[arquivo]
```

### 2. Livro-Razão Obrigatório com "Como Desfazer"
Toda execução real vai ao livro-razão:
```
"[DD/MM] [Tipo]: [resumo 1-2 linhas].
Arquivo: [path]. Backup: [path backup].
Como desfazer: [instruções explícitas]."
```

Sem "como desfazer" → Claudemberg não consegue reverter → não publique sem ele.

### 3. Unicode Proibido em Arquivos com PDF
Nenhum caractere Unicode (setas →, emojis, aspas curvadas) em `.md` que gera PDF. Substituir por ASCII antes de salvar. Fazer grep antes de gerar:
```bash
grep -P '[\x80-\xFF]' arquivo.md
```

### 4. Versão Publicada Primeiro (Painel)
Nunca republicar o Painel sem ler a versão publicada antes. Merge sem leitura = conflito com versão mais nova.

### 5. Fronteira Cliente é Absoluta
Dúvida entre "organismo" e "cliente" → trata como cliente → não executa → sinaliza para Reunião Semanal. A fronteira protege a responsabilidade técnica de Claudemberg (CAU/RRT).

### 6. Fonte Única de Verdade para Status de Skill
O campo `Status` no `.md` da Skill em `Skills_Propostas/` é o único lugar que diz se a ferramenta está implantada. Nunca atualizar em dois lugares — o outro inevitavelmente fica desatualizado.

### 7. Pense por Gestor, Execute por Agente
Wallenberg é orquestrador — não executor dos projetos dos Gestores. Cada Gestor é responsável pelo mérito do que sua equipe produz. Wallenberg só orbita em torno de pendências e implantações do organismo.

---

## V. COMO DESFAZER (Se Algo Sair Errado)

### Desfazer Execução de Pendência
Depende do que o Gestor fez:
- Edição de arquivo `.md` local → restaurar do backup: `cp _backups/{data}/{arquivo} {destino}`
- Edição de documento no Google Drive → usar Histórico de Versões do Google Docs (Arquivo → Histórico de versões)
- Não há ação de cliente que esta rotina possa executar — a fronteira garante isso

### Desfazer Implantação de Ferramenta
- Desconectar do `.claude/agents/{agente}.md` (remover da lista `tools:`)
- Se `pip install` foi feito: `pip uninstall {pacote}` — mas esta rotina não deve ter feito pip install sem documentar o comando exato
- Registrar no livro-razão que foi desfeito

### Desfazer Atualização do Painel
```
cp 01_CEO/Decisoes_Autonomas/_backups/{data}/painel_fundador_sttk.html 01_CEO/Painel_Fundador/painel_fundador_sttk.html
Artifact publish(file_path=..., url=3c28ec0d...)
```

### Desfazer Atualização de `pendencias.json`
```
cp 01_CEO/Decisoes_Autonomas/_backups/{data}/pendencias.json 01_CEO/Pendencias/pendencias.json
```

---

## VI. CHECKLIST PÓS-RODADA (Antes de Declarar "Concluído")

- [ ] **Passo 0 (Estado):** Arquivo de estado lido, contexto da rodada anterior incorporado
- [ ] **Passo 1 (Gestores):** Lista gerada por Glob (não hardcoded), ferramenta `Agent` verificada por frontmatter
- [ ] **Passo 2 (Pendências):** `pendencias.json` lido, itens separados por Gestor e alcance
- [ ] **Passo 3 (Gestores):** Todos os Gestores acionados, todos reportaram (ou bloqueio registrado)
- [ ] **Passo 4 (Livro-razão):** Uma entrada por Gestor com execução real, "como desfazer" explícito, PDF gerado sem glifo, `pendencias.json` atualizado
- [ ] **Passo 5 (Varredura):** Varredura de melhoria feita e resultado registrado no `_estado_{gestor}.md`
- [ ] **Passo 6 (Painel):** Versão publicada lida antes de editar, backup criado, republicado no mesmo URL (ou "nada novo" registrado)
- [ ] **Passo 7 (Learning Agent):** Rodou ou registrou "Diária Skills já rodou hoje"
- [ ] **Passo 8 (Implantação):** Skills candidatas avaliadas, `Status` atualizado (ou "nenhuma pendente")
- [ ] **Passo 8.b (Escalon.):** Gestores sem progresso identificados e sinalizados
- [ ] **Governança:** Backup criado antes de qualquer edição ✅
- [ ] **Livro-razão:** Entrada com "como desfazer" ✅
- [ ] **Fechamento:** Template preenchido (ou impedimento registrado) ✅

---

## VII. EXEMPLOS REAIS

### Exemplo 1 — Rodada Padrão (27/08/2026)
```
PASSO 0: Leu _estado_wallenberg.md — Items 4-8 pausados, WAN 2.2 em aberto
PASSO 1: Glob → Kelsen, Lúcio, Cardozo (3 Gestores). Kelsen e Lúcio têm Agent. Cardozo novo — verificado.
PASSO 2: pendencias.json — 3 itens abertos: b14 (Kelsen, humano), wallenberg-integracao (auto), lucio-render (Lúcio, tecnico)
PASSO 3:
  → Kelsen: reconciliou b14 (sem resposta SMDU 10 dias). Hely arquivou PDF SMDU Nº10 com correção de divergência.
  → Lúcio: decidiu 5 pontos da auditoria Oscar (represada 16 dias). Achou WAN 2.2 bloqueado (Burle sem Bash).
  → Cardozo: corrigiu _estado_cardozo.md divergente. Sinalizou 2 Skills BIM sem Agente dono.
PASSO 4: 3 entradas no livro-razão (uma por Gestor). PDF gerado. pendencias.json atualizado (2 parciais, 1 novo aberto).
PASSO 5: Varredura: Kelsen checou fontes, Lúcio checou POPs de Oscar, Cardozo checou exame do Caso 2.
PASSO 6: Painel atualizado — 3 eventos adicionados. Republicado.
PASSO 7: Diária Skills não tinha rodado hoje. Learning Agent buscou 2 vídeos — nenhuma proposta viável.
PASSO 8: 2 Skills propostas: RDT → implantada (só conhecimento). PPTAgent → descartada (fasttext sem Build Tools).
PASSO 8.b: Todos os 3 Gestores com execução real. Sem estagnação.
STATUS: ✅ Completa (8/9 passos + Fechamento)
```

### Exemplo 2 — Rodada com Bloqueio (hipotético)
```
PASSO 0: OK
PASSO 1: Glob → 3 Gestores
PASSO 2: pendencias.json — 2 itens auto, 1 humano
PASSO 3: ❌ Bloqueio — Lúcio não responde (timeout)
  → Aplicar Regra de Desbloqueio: registra bloqueio, continua com Kelsen e Cardozo
PASSO 4: 2 entradas (Kelsen e Cardozo). Lúcio: registrado como bloqueado.
PASSO 5: Varredura: Kelsen e Cardozo fizeram. Lúcio: bloqueado (sem varredura).
PASSO 6: Painel — 2 eventos (sem eventos de Lúcio).
PASSO 7: Pular — rodada já longa.
PASSO 8: 1 Skill pendente → implantada.
PASSO 8.b: Lúcio sem progresso (1ª rodada) → sinalizado no resumo.
STATUS: ⚠️ Parcial (7/9 passos + Lúcio bloqueado)
PRÓXIMA: Investigar o que travou Lúcio — verificar _estado_lucio.md
```

---

## VIII. TABELA RÁPIDA DE REFERÊNCIA

| Passo | Objetivo | Tempo Est. | Resultado | Bloqueador Comum |
|---|---|---|---|---|
| 0 | Ler estado atual | 2-3 min | Contexto da rodada anterior | Arquivo não existe |
| 1 | Descobrir Gestores | 2-5 min | Lista por Glob + ferramenta verificada | Glob retorna vazio |
| 2 | Ler fila pendências | 5-10 min | Itens separados por Gestor/alcance | JSON muito grande |
| 3 | Acionar Gestores | 45-90 min | Resultado de cada Gestor | Timeout / fronteira cliente invadida |
| 4 | Livro-razão + JSON | 15-25 min | Entradas + PDF + JSON atualizado | Glifo Unicode |
| 5 | Varredura melhoria | 5-10 min | Relato do que foi checado | Gestor relata "nada" sem checar |
| 6 | Painel | 10-20 min | Painel republicado | Conflito de versão |
| 7 | Learning Agent | 2-40 min | Proposta ou "sem proposta" | Vídeos inacessíveis |
| 8 | Implantar Skills | 20-60 min | Status atualizado | Skill incompleta / dependência faltando |
| 8.b | Autoescalonamento | 2-5 min | Estagnação sinalizada | Não sabe histórico do Gestor |
| Fech. | Fechamento | 5 min | Template preenchido | Sem tempo (registrar para depois) |

---

## IX. REFERÊNCIAS RÁPIDAS

### Arquivos Principais
- **Rotina v2.3 (regras):** `wallenberg-drenagem-continua-v2_SKILL.md`
- **Este manual:** `wallenberg_manual_operacional_drenagem_continua.md`
- **Fechamento anterior:** `01_CEO/rotina_fechamento_template.md`
- **Estado Wallenberg:** `01_CEO/_estado_wallenberg.md`
- **Fila estruturada:** `01_CEO/Pendencias/pendencias.json`
- **Livro-razão:** `01_CEO/Decisoes_Autonomas/2026/Agosto.md`
- **Skills:** `01_CEO/Skills_Propostas/2026/[Mês]/`
- **Painel:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html`
- **Script PDFs:** `_ferramentas/md_to_pdf.py`

### URL Permanente do Painel
```
https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27
```

### Comandos Comuns (PowerShell)
```powershell
# Backup antes de alterar
cp "[arquivo]" "01_CEO\Decisoes_Autonomas\_backups\$(Get-Date -f 'yyyy-MM-dd')\[arquivo]"

# Gerar PDF
python "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\_ferramentas\md_to_pdf.py" "[caminho_do_md]"

# Checar glifos Unicode num .md
python -c "import re,sys; [print(f'L{i+1}: {l.rstrip()}') for i,l in enumerate(open(sys.argv[1],'r',encoding='utf-8')) if re.search(r'[^\x00-\x7F]',l)]" "[arquivo.md]"
```

### Agentes Disponíveis
| Agente | Acionar com | Tem `Agent`? |
|--------|-------------|--------------|
| Kelsen | `subagent_type: "kelsen"` | Sim (desde 03/08) |
| Lúcio | `subagent_type: "lucio"` | Sim (desde 03/08) |
| Cardozo | `subagent_type: "cardozo"` | Sim (verificar frontmatter) |

---

**VERSÃO:** 2.3 (27/08/2026)
**PRONTO PARA:** Wallenberg executar em toda rodada da Drenagem Contínua
**PRÓXIMA REVISÃO:** quando uma das regras da rotina mudar — atualizar na mesma sessão
