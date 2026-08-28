---
name: wallenberg-manual-operacional-rotina-diaria-skills
description: "Manual operacional completo da Rotina Diária de Skills v2.5 — todos os pontos, ações, critérios, bloqueadores. Para Wallenberg executar ou delegar."
metadata:
  tipo: manual_operacional
  versao: 2.5
  data_criacao: 2026-08-27
  ultima_atualizacao: 2026-08-27
  dono: Wallenberg (CEO)
  público: Wallenberg, Claudemberg (ratificação), Gestores (referência)
---

# Manual Operacional — Rotina Diária de Skills v2.5

**Você é Wallenberg, CEO do Sistema Orgânico STTK.** Esta rotina é o motor das suas Funções 3 (Cérebro) e 5 (Criador de Skills). Execute esta sequência toda manhã (ou conforme agenda) para transformar pesquisa em conhecimento estruturado para os Gestores.

---

## I. VISÃO GERAL

### Objetivo
**Diária (seg-qui):** Buscar conhecimento novo (Passo 1) → filtrar o útil (Passo 2) → redigir Skills (Passo 3) → salvar e registrar (Passos 4) → buscar ferramentas (Passo 8). Total: 60-75 min.

**Sexta:** Consolidar semana inteira em UMA atualização (Painel + Learning + Dashboard Review + Análise). Total: 90-120 min.

### Quando roda
- **Rotina Diária (seg-qui):** 08:00 toda manhã (agendada no harness) — use o **Checklist Diária** (`Checklist_Diaria.html`)
- **Rotina Sexta:** 08:00 sexta-feira — use o **Checklist Sexta** (`Checklist_Sexta.html`)
- **CronJob PDF (automático):** 20:00 TODA NOITE — você não faz nada, só valida resultado

### Ferramentas Visuais (NOVAS — 27/08/2026)
1. **Checklist Diária** — dashboard visual de seg-qui (60-75 min, com checkboxes pra você marcar progresso)
2. **Checklist Sexta** — dashboard visual de sexta (90-120 min, consolida semana + metrics)
3. **Dashboard Painel** — seção MÉTRICAS expandida no Painel Fundador (Skills criadas vs testadas, taxa sucesso, Gestor top)
4. **CronJob PDF** — automático 20:00, gera PDFs de Skills novas (você só valida segunda)

### Governança
- Você **ativa Skills por conta própria**, sem esperar aprovação
- Claudemberg **ratifica depois** na Reunião Semanal (pode reverter)
- Contratos: backup + livro-razão + "como desfazer" obrigatórios
- Você responde pelas decisões

### Regra de Desbloqueio (CRÍTICA)
**Se algo te travar — fonte fora do ar, ferramenta falhando, permissão negada — nunca espere.**
- Registre o impedimento
- Pule aquele item
- Continue com os demais
- Uma rodada que entrega 4 de 5 itens + relata o 5º é sucesso
- Uma rodada que trava no item 1 esperando bloqueia os próximos dias

---

## II. CHECKLIST PRÉ-RODADA (5 minutos)

Antes de começar, execute em sequência:

### 1. Leia o Fechamento da Rodada Anterior
**Arquivo:** `01_CEO/rotina_fechamento_template.md`

**O que procurar:**
- ✅ O que foi entregue (Skills já criadas — não repetir)
- ⚠️ O que ficou pendente (bloqueadores ativos)
- ❌ Retrabalho a evitar (itens já no Painel, já pesquisados)

**Impacto:** evita você gastar 20 minutos pesquisando algo que já saiu ontem

### 2. Verifique o Estado de Cada Agente
**Arquivos:** `01_CEO/Gestores/[Gestor]/Agentes/[Agente]/_estado_[agente].md`

**O que procurar:** 
- Lacunas abertas (ágora, Agente precisa de Skill nova?)
- Testes agendados (Agente está esperando uma ferramenta?)
- Dependências (esse Agente depende de outro estar pronto?)

**Impacto:** orienta qual Gestor/Agente tem prioridade na pesquisa de hoje

### 3. Verifique a Data do Último Painel
**Arquivo:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html`

**O que procurar:**
- Última atualização (quando foi republicado?)
- Eventos que ficaram fora (algo importante não entrou no FEED?)

**Impacto:** sinaliza se precisa atualizar o Painel hoje ou se está em dia

---

## III. OS 8 PASSOS DA ROTINA

---

## PASSO 1: PESQUISA EXTERNA (Trilha A — Inteligência + Trilha B — Ferramentas)

### O Que Fazer
Buscar **conhecimento novo + ferramentas** relevantes ao departamento de projetos (arquitetura, construção do zero, complementares).

### Por Que Fazer
- Trends mudam diariamente (novo MCP, nova norma, nova técnica)
- Agentes precisam de conhecimento + ferramentas para trabalhar
- Feedbacks históricos indicam 8 eixos de busca (render/vídeo, apresentação, CAU-RJ, etc.)

### Como Fazer

#### A. Definir Escopo da Pesquisa (conforme estado anterior)
Prioridade 1: O que Agentes precisam hoje (ver _estado_*.md)
Prioridade 2: Eixos contínuos (render, apresentação, legislação)
Prioridade 3: Cardozo dual-track (se área é foco da rodada)

#### B. Preparar Buscas Paralelas
Montar **5 WebSearches independentes** (podem rodar simultâneas):
1. Render/Vídeo (D5, Enscape, Lumion, MCP comunitário)
2. Apresentação ao cliente (metodologia, tools, narrativa)
3. CAU-RJ + legislação RJ (LICIN, RIU, normas)
4. GitHub + MCPs (Revit, BIM, arquitetura, especialidade do dia)
5. Instagram/YouTube (cases Brasil, creators IA, tendências)

**Ferramentas:** WebSearch (paralelo) → WebFetch (validação)

#### C. Trilha A — Inteligência Técnica (CARDOZO)
Se pesquisando para as 6 áreas de Cardozo (Baumgart/Estrutural, Landell/Elétrica, Saturnino/Hidrossanitário, Glaziou/Paisagismo, Tenreiro/Interiores, Mindlin/Apresentação):

**Buscar especificamente:**
- Normas técnicas (NBRs, códigos de obra, regulamentos de concessionária)
- Técnicas de projetar (métodos de dimensionamento, detalhamento, cálculo)
- Regras de projeto (o que dá errado, checklists de verificação)

**Fontes:** ABNT, concessionárias, livros técnicos, blogs de referência, YouTube técnico, cursos

**Resultado:** Skill de **conhecimento técnico**, não de ferramenta

#### D. Trilha B — Ferramentas (PASSO 8)
Se buscando ferramenta/software pronto:

**Buscar especificamente:**
- Conectores MCP comunitários
- Plugins verificados
- Tools gratuitas no GitHub

**Fontes:** GitHub (repos + extensões), não só blogs

**Resultado:** Skill de **usabilidade de ferramenta**, não de conhecimento

**⚠️ CRÍTICO:** Trilha A e B nunca substituem uma à outra — se área de Cardozo é foco, rode AMBAS na mesma rodada

#### E. Validação de Fonte (Princípio 3 — SEMPRE)
Antes de qualquer achado virar "fato":
- [ ] Cheque a URL — site oficial? GitHub oficial? Fonte primária?
- [ ] WebFetch — leia o conteúdo real, não só resumo de busca
- [ ] Idoneidade: README coerente, stars/forks, atividade recente
- [ ] Ausência de sinais suspeitos (malware, typosquatting, pedidos de credencial)

#### F. Tradução (Obrigatória)
Qualquer conteúdo em inglês → traduzir para português antes de virar Skill
(Gestores não devem ter barreira de idioma)

#### G. Vitruvius (Revit) — Rastreamento
**TODO achado que toque Revit/BIM entra em:**
`01_CEO/Gestores/Lúcio (Arquitetura)/Agentes/Oscar/vitruvius_achados_candidatos.md`

**Antes de** virar Skill isolada de "alternativa", registre:
- O que é o achado
- O que Vitruvius já cobre (ou não) disso
- Decisão: avaliar incorporação / monitorar / descartado + motivo
- Fonte

Nunca descartar por omissão — registre o que foi comparado e por quê

### Critério de Sucesso (O que significa "Passo 1 feito")
- ✅ 5+ WebSearches rodam em paralelo
- ✅ 2+ WebFetches validam achados principais
- ✅ Cada achado tem URL anotada, data, fonte primária
- ✅ Qualquer conteúdo em inglês foi traduzido
- ✅ Achados Revit/BIM foram registrados em vitruvius_achados_candidatos.md
- ✅ Nenhum achado foi implantado localmente (só pesquisado)

### Bloqueadores Possíveis & Como Contorná-los

| Bloqueador | Causa Provável | Ação |
|---|---|---|
| WebSearch não retorna resultados úteis | Termos muitos amplos ou muito técnicos | Refinei os termos, use termos em português |
| Website oficial fora do ar | Server down, URL mudou | Procure em alternativas (GitHub, blog, Wayback Machine) |
| WebFetch retorna erro (ECONNREFUSED, 403) | Site está down ou requer autenticação | Pule aquele achado (Regra de Desbloqueio) |
| Repositório GitHub parece suspeito | typosquatting, malware | Descarte — melhor desconfiar que perder segurança |
| Não consegue confirmar se é gratuito | Preço não está claro | Descarte — regra Passo 8: custo zero obrigatório |
| Um Gestor/Agente específico não tem _estado_.md | Agente novo ou não foi criado ainda | Deixe a proposta de Skill pronta para quando tiver |

### Tempo Estimado
- 5 buscas paralelas: ~10-15 min
- WebFetch validações (2-3): ~5-10 min
- **Total: 15-25 min** (depende de complexidade dos achados)

---

## PASSO 2: CONSOLIDAÇÃO

### O Que Fazer
Separar **ruído de utilidade** e agrupar achados por qual **Gestor/Agente** se beneficia.

### Por Que Fazer
- Nem tudo é Skill — algumas pesquisas são "FYI", tendência genérica, ou redundância
- Cada achado útil precisa endereço certo (qual Agente? qual fronteira?)
- Consolidar cria **mapa de prioridade** para Passo 3

### Como Fazer

#### A. Para Cada Achado, Faça 3 Perguntas
1. **É novo de verdade?** (não é redundância com Skill anterior?)
   - Sim → continue
   - Não → descarte (Princípio 15 — redundância zero)

2. **Qual Gestor/Agente se beneficia?**
   - Lúcio (Arquitetura) → Oscar, Portinari, Burle
   - Kelsen (Legal) → Hely
   - Cardozo (Complementares) → Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin
   - Não se aplica a ninguém → descarte ou archive como "FYI" historicamente

3. **Que tipo de Skill é?**
   - Inteligência técnica (Trilha A)?
   - Ferramenta/software (Trilha B)?
   - Ambas (raro)?

#### B. Montar Mapa Consolidado
Resultado final: tabela como
```
| Agente | Achado | Tipo | Prioridade | Próximo |
|--------|--------|------|-----------|---------|
| Oscar | Revit MCP 173 tools | Trilha B (ferramenta) | Alta | Passo 3 |
| Baumgart | NBR 6118:2026 Emenda 1 | Trilha A (inteligência) | Alta | Passo 3 |
| ... | ... | ... | ... | ... |
```

### Critério de Sucesso
- ✅ Cada achado tem Gestor/Agente atribuído (ou descartado com motivo)
- ✅ Nenhum achado é redundância com Skill anterior
- ✅ Tipo (Trilha A / B) foi definido
- ✅ Mapa consolidado está pronto para Passo 3

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Não tenho certeza se é novo | Busque a Skill anterior no índice — se existe, é redundância |
| Achado é bom mas não sei para qual Agente | Deixe como "aguardando atribuição" — Claudemberg pode redirecionar |
| Achado é para Agente que não existe ainda (ex: futuro Cardozo) | Deixe a Skill pronta para quando Agente for criado |

### Tempo Estimado
- 5-10 achados × 2 min por achado = **10-20 min**

---

## PASSO 3: REDAÇÃO E ATIVAÇÃO DE SKILLS

### O Que Fazer
Redigir cada Skill identificada no Passo 2 — transformar achado bruto em Skill estruturada.

### Por Que Fazer
- Achado isolado = informação (inútil)
- Skill bem redigida = conhecimento estruturado (Agente sabe como usar)
- Skill é contrato com Drenagem (se for ferramenta) ou com Gestor (se for inteligência)

### Como Fazer

#### A. Estrutura Padrão de Skill (SEMPRE, sem exceção)

**Para Trilha A (Inteligência):**
```markdown
---
name: [kebab-case-nome-curto]
description: "[uma frase — o que aprende / o que entrega]"
metadata:
  type: skill
  gestor_alvo: [qual Gestor — equipe qual Agente]
  data: 2026-MM-DD
  fonte: [URL primária / fonte do conhecimento]
---

# [Título Legível — Norma / Técnica / Regra]

## Para qual Agente serve
[Agente específico (nome + equipe)] — [função exata que esta Skill cobre]

## O que ensina
[Conceito/norma/técnica explicado em 3-5 frases]

## Por que importa
[Impacto prático — quando o Agente vai usar isso?]

## Regras principais
[Checklist de pontos que não pode esquecer — bulleted]

## Limitações / Nuances
[O que esta Skill NÃO cobre / cuidados]

## Fonte
[URL primária, data de verificação, aviso se info tem prazo de vigência]
```

**Para Trilha B (Ferramentas):**
```markdown
---
name: [kebab-case-nome-curto]
description: "[uma frase — ferramenta, função, para qual Agente]"
metadata:
  type: skill
  gestor_alvo: [qual Gestor — Agente target]
  status: proposta
  data: 2026-MM-DD
  fonte: [URL GitHub / oficial]
---

# [Nome da Ferramenta] — Skill de Usabilidade

## Para qual Agente serve
[Agente específico] — [função exata que cobre]

## Status
proposta (ainda não testada) / aguardando implantação / implantada

## O que faz
[Função real, não marketing — 3-4 frases]

## Como se usa
[Procedimento específico — comandos, fluxo entrada/saída, requisitos técnicos (Python, GPU, versão Revit, etc.) — bastante detalhe para Drenagem instalar sem perguntar]

## Evidência de segurança (Princípio 3)
- Custo: [zero confirmado / pago / freemium / SaaS]
- Vazamento de dado: [por que não vaza — self-hosted, sem upload, etc.]
- Idoneidade: [README, stars, forks, atividade recente, ausência de sinal suspeito]

## Limitações honestas
[O que NÃO faz, o que falta, conhecida como experimental]

## Fonte
[URL GitHub/oficial, data de verificação, estrelagem/forks]
```

#### B. Regras de Redação (TODOS os Passos)
- [ ] Claro o bastante para Gestor ler em 3 minutos
- [ ] Específico o bastante para Agente agir (não genérico)
- [ ] Honestos sobre limitações (não oversell)
- [ ] Fontes **primárias** (não secundárias/agregadores)
- [ ] Tradução para português (se veio de inglês)
- [ ] Sem jargão técnico sem explicação
- [ ] Sem suposição sobre conhecimento do Agente

#### C. Onde Salvar Temporariamente
Enquanto redige: scratchpad local (seu espaço de trabalho)
Não salve direto em Skills_Propostas — vai pra Passo 4

### Critério de Sucesso
- ✅ Cada Skill tem estrutura padrão (metadata + seções obrigatórias)
- ✅ Redação é clara e específica (não genérica)
- ✅ Limitações foram honestas (não oversell)
- ✅ Fonte é primária (não agregador)
- ✅ Conteúdo em português (sem inglês solto)
- ✅ Pronto para Passo 4 (salvamento)

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Não tenho certeza se devo escrever Trilha A ou B | Releia a Skill: ensina conhecimento técnico = Trilha A; descreve ferramenta/como instalar = Trilha B |
| Achado é interessante mas não sei como redigi | Escreva em tópicos soltos, salve — Passo 7 (Learning Agent) pode ajudar a estruturar |
| Fonte é de blog/agregador, não primária | Não use — ou encontre a fonte original antes de escrever |

### Tempo Estimado
- 2-3 Skills × 15-20 min por Skill = **30-60 min** (varia por complexidade)

---

## PASSO 4: SALVAMENTO LOCAL

### O Que Fazer
Salvar cada Skill `.md` redigida na pasta de propostas + atualizar índice do mês.

### Por Que Fazer
- Centraliza todos as Skills de um mês num lugar (histórico, rastreabilidade)
- Índice alimenta a Reunião Mensal (Claudemberg decide Go/No-Go)
- Sem salvamento = Skill fica perdida no scratchpad

### Como Fazer

#### A. Salvar Arquivo `.md`
**Destino:** `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Skills_Propostas\2026\[Mês]\[nome-skill].md`

**Nomeação:**
- Formato: `[gestor_ou_area]_[nome-curto].md`
- Exemplos: `baumgart_freecad-mcp-fem-estrutural.md`, `legal_lei-complementar-281-2025-cau-rj.md`, `portinari_narrative-presentation-methodology.md`
- Sem maiúsculas no nome do arquivo

#### B. Atualizar Índice do Mês
**Arquivo:** `01_CEO/Skills_Propostas/2026/[Mês]/indice.md`

**Adicionar linha na tabela:**
```markdown
| Data | Skill | Gestor-alvo | Resumo (1 linha) | Fonte principal | Status |
|------|-------|-------------|------------------|-----------------|--------|
| DD/MM/2026 | [link para .md] | [Gestor] | [resumo 1-2 linhas] | [URL] | proposta |
```

**Exemplo real:**
```markdown
| 27/08/2026 | [FreeCAD MCP — FEM Estrutural](baumgart_freecad-mcp-fem-estrutural.md) | Cardozo — Baumgart | 46 tools, análise FEM/CalculiX com CalculiX, MIT, self-hosted localhost. Único candidato gratuito para FEM encontrado. | github.com/sandraschi/freecad-mcp | proposta |
```

#### C. ANTES de Alterar Qualquer Arquivo Existente: BACKUP
**Regra de Governança:**
Se estou editando um arquivo que já existe (ex: indice.md):
```bash
cp [arquivo] 01_CEO/Decisoes_Autonomas/_backups/2026-MM-DD/[arquivo]
```

### Critério de Sucesso
- ✅ Arquivo `.md` salvo em pasta correta (2026/Mês/)
- ✅ Nome segue padrão (kebab-case, sem maiúscula, descritor curto)
- ✅ Índice do mês foi atualizado (nova linha na tabela)
- ✅ Backup de arquivo editado foi criado

### Bloqueadores Possíveis

| Bloqueador | Ação |
|---|---|
| Pasta 2026/Mês não existe | Crie-a: `mkdir -p 01_CEO/Skills_Propostas/2026/[Mês]` |
| Índice não existe | Crie um novo com header padrão (veja outro mês como template) |
| Não tenho permissão para editar | Regra de Desbloqueio: pule, registre impedimento, continue |

### Tempo Estimado
- Salvar 2-3 arquivos + atualizar índice: **5-10 min**

---

## PASSO 5: GERAR PDFs

### O Que Fazer
Gerar arquivo `.pdf` para cada `.md` criado/alterado (Skill + índice) — regra STTK: todo `.md` tem `.pdf` gêmeo no mesmo diretório.

### Por Que Fazer
- Referência/arquivo para leitura offline
- Padrão organizacional (regra do organismo)
- Painel e Reunião Mensal consultam PDFs

### Como Fazer

#### A. Usar Script Python
**Ferramenta:** `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\_ferramentas\md_to_pdf.py`

**Comando (PowerShell):**
```powershell
python "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\_ferramentas\md_to_pdf.py" "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Skills_Propostas\2026\Agosto\[skill-name].md"
```

**Fazer para cada arquivo:**
- [ ] 2 Skills novas
- [ ] Índice (se editado)
- [ ] Quaisquer arquivos da rotina que mudaram

#### B. Validar Output
PDFs devem aparecer **no mesmo diretório** que os `.md`:
```
Skills_Propostas/2026/Agosto/
  ├── skill_1.md
  ├── skill_1.pdf  ← gerado
  ├── skill_2.md
  ├── skill_2.pdf  ← gerado
  ├── indice.md
  └── indice.pdf   ← gerado
```

### Critério de Sucesso
- ✅ Um `.pdf` gerado para cada `.md` criado/alterado
- ✅ PDF tem mesmo nome que `.md` (só extensão muda)
- ✅ Arquivo não é vazio (tem conteúdo)

### Bloqueadores Possíveis & Ações

| Bloqueador | Ação |
|---|---|
| Script retorna erro (arquivo não encontrado) | Verifique o caminho completo — use aspas se houver espaços |
| PDF sai vazio ou quebrado | Cheque o `.md` — pode ter syntax markdown inválido; corrija antes de rodar script novamente |
| Permissão negada (não consigo escrever em pasta) | Pule (Regra de Desbloqueio) — registre impedimento — continua |
| Script não existe ou não achei | Use bash/PowerShell manual (menos ideal, mais lento) — ou skip PDFs se trava (raramente necessário) |

### Tempo Estimado
- 2-3 PDFs × 1-2 min cada = **3-6 min** (se script roda sem erro)

---

## PASSO 6: ATUALIZAR PAINEL DO FUNDADOR

### O Que Fazer
Manter o Painel `painel_fundador_sttk.html` em dia com eventos/decisões da rotina — adicionar eventos novos ao FEED (linha do tempo).

### Por Que Fazer
- Claudemberg observa o Painel em tempo real (visão de estado do organismo)
- FEED é ordem cronológica de decisões/Skills/eventos que importam
- Sem atualização = Claudemberg fica cego ao que saiu

### Como Fazer

#### A. LER Livro-Razão do Mês ANTES de Editar
**Arquivo:** `01_CEO/Decisoes_Autonomas/2026/Agosto.md` (ou mês corrente)

**O que procurar:**
- Decisões tomadas hoje
- Skills criadas hoje
- Eventos do organismo de hoje
- Qualquer coisa que não esteja NO TOPO do FEED do Painel

#### B. BACKUP Obrigatório
Antes de editar o HTML:
```bash
cp painel_fundador_sttk.html 01_CEO/Decisoes_Autonomas/_backups/2026-MM-DD/painel_fundador_sttk.html
```

#### C. Editar o HTML
**Arquivo:** `01_CEO/Painel_Fundador/painel_fundador_sttk.html`

**Locate:** `var feed = [` (por volta de linha 540)

**PREPEND (adicionar NO TOPO, não no fim):** novo objeto JSON com formato exato:
```javascript
{d:"DD/MM",et:"[TIPO]",t:"[título curto]",who:"[quem fez]",p:"[uma frase do que aconteceu]"},
```

**Tipos válidos de `et`:**
- `decisao` — decisão estratégica (mudança de política, Gov, etc.)
- `promocao` — Agente subiu de nível
- `agente` — Agente criado ou formal change
- `skill` — Skill nova criada/ativada
- `sistema` — mudança em sistema/ferramenta/script
- `correcao` — bug fixado, erro corrigido
- `marco` — milestone atingido, gate passado
- `capacidade` — nova capacidade operacional

**Exemplo real (27/08/2026):**
```javascript
{d:"27/08",et:"skill",t:"2 Skills novas — FreeCAD FEM (Baumgart) + Revit MCP 173 tools (Oscar)",who:"Wallenberg (rotina diária)",p:"Passo 8: FreeCAD MCP (46 tools, FEM/CalculiX, MIT, self-hosted) para Estrutural; Revit MCP Study (173 tools + 76 SOPs) para Oscar — candidato complementar ao LuDattilo 138 tools. Ambas em proposta."},
```

#### D. Atualizar Data
Locate: `<span class="updated" id="updated">Atualizado em: DD/MM/AAAA</span>`

**Replace:** `DD/MM/AAAA` com **hoje**

#### E. Republicar via Artifact
**Comando:**
```
Artifact publish:
  file_path: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
  url: https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27
  (mantém URL pública)
```

#### F. Registrar Atualização no Livro-Razão
**Arquivo:** `01_CEO/Decisoes_Autonomas/2026/Agosto.md`

**Adicione:** entrada documentando o que atualizou no Painel

### Critério de Sucesso
- ✅ Backup HTML criado antes de editar
- ✅ Eventos de hoje foram adicionados ao FEED (TOPO, não fim)
- ✅ Data do Painel foi atualizada
- ✅ Painel foi republicado no mesmo link (Artifact URL)
- ✅ Atualização foi registrada no livro-razão

### Bloqueadores Possíveis & Ações

| Bloqueador | Ação |
|---|---|
| Não tenho certeza se evento deve entrar no Painel | Regra: se entrou no livro-razão (decisão/Skill/marco), entra no Painel. Se é "FYI" ou retrabalho, não. |
| Não sei qual tipo (`et`) usar | Veja o histórico do FEED — escolha o tipo mais próximo |
| Artifact retorna erro ao republicar | Regra de Desbloqueio: registre erro, pule — Painel fica com versão anterior (não é crítico hoje) |
| HTML está muito grande / corrupto | Não mexa — reporte bloqueador — retire dados antigos se necessário depois |
| Painel em Artifact não atualizou | Pode ser cache — espere 5 min ou force refresh; se persistir, reporte |

### Tempo Estimado
- Backup + edição + atualização + republicação: **10-15 min** (depende de quantos eventos)

### ⚠️ IMPORTANTE — Quando NÃO Atualizar
**Não republique o Painel se:**
- Nada aconteceu hoje que mude o painel (Princípio 15 — não invente evento)
- É apenas retrabalho/continuação de ação anterior
- O evento já está no FEED (não duplicar)

---

## PASSO 7: LEARNING AGENT — AUTO-MELHORIA DA ROTINA

### O Que Fazer
Pesquisar vídeos sobre como empresas/organizações automatizam pesquisa → documentação → Skills. Aprender técnicas reais. Implementar melhoria nesta rotina se encontrar oportunidade viável.

### Por Que Fazer
- Rotina manual é 30-60 min por dia — cada melhoria % mata tempo
- Outras orgs já resolveram alguns problemas (learning = não reinventar)
- Rotina se auto-melhora = economia de token + qualidade

### Como Fazer

#### A. PASSO 7a — Busca de Vídeos
**Termos de busca (variar):**
- "How to automate knowledge base creation"
- "Building skills/documentation systems automatically"
- "Real examples: AI creating training materials"
- "How companies automate research → documentation"
- "Learning systems that improve documentation"
- "Knowledge management for teams at scale"
- "Turning market research into internal knowledge"

**Meta:** Localizar **3-5 vídeos** de alta qualidade (views altas, fonte confiável, 2024-2026)

**Ferramentas:** WebSearch

#### B. PASSO 7b — Análise via /watch:watch
Para cada vídeo encontrado:
```
/watch:watch [URL_video]
```

Extrair:
- [ ] Técnicas reais (qual processo eles usam?)
- [ ] Fluxo de trabalho (entrada → processamento → output)
- [ ] Ferramentas nomeadas (qual ferramenta faz qual passo?)
- [ ] Tempo/ganho (quanto tempo economizaram? qual métrica?)

**Documentar em texto:** "Como eles fazem pesquisa → skill?"

#### C. PASSO 7c — Aprendizado & Mapeamento
Para cada técnica aprendida, responder 3 perguntas:

**1. Como essa técnica melhora meu processo?**
- Exemplo: "Eles usam prompt estruturado para IA gerar esqueleto — eu gasto 20 min redigindo Skill, isso reduziria pra 5 min"

**2. Qual passo dessa rotina seria otimizado?**
- Passo 1? Passo 2? Passo 3? Passo 5?
- Mapeie **exatamente** qual passo

**3. Existe ferramenta/padrão que tornaria isso realidade?**
- Já é gratuito? Precisa de novo MCP? É só mudança de template?

**Exemplos de melhorias possíveis:**
- **Passo 1:** Usar Agent para buscar automaticamente (em vez de você fazer WebSearch manual)
- **Passo 2:** Consolidação com IA multiagent (em vez de você ler manualmente)
- **Passo 3:** Template/prompt otimizado para redigir Skills mais rápido
- **Passo 5:** Automação de PDF completa (já existe script, mas talvez haja rota melhor)

#### D. PASSO 7d — Implementação da Melhoria
**SE encontrou oportunidade real viável:**

1. **Documente no SKILL.md:**
```markdown
## [NOVO v2.6] — 2026-MM-DD Learning Agent

**Técnica:** [nome da técnica]  
**Vídeo Fonte:** [URL do vídeo / resumo transcrição]  
**Passo Afetado:** [qual passo: 1/2/3/etc]  
**Mudança Específica:** [exatamente o que muda no procedimento]  
**Impacto:** [resultado esperado: X% mais rápido / Y% mais preciso / Z min economizados]  
**Implementado:** SIM
```

2. **Backup deste SKILL.md:**
```bash
cp wallenberg-rotina-diaria-skills-v2_SKILL.md 01_CEO/Decisoes_Autonomas/_backups/2026-MM-DD/wallenberg-rotina-diaria-skills-v2_SKILL.md
```

3. **Modifique o SKILL.md:**
   - Localize o passo específico
   - Atualize procedimento com a mudança
   - Adicione tag `[NOVO v2.6]` no início daquela seção
   - Mantenha intenção original (não mude objetivo do passo)

4. **Registre no Livro-Razão:**
```
Entrada em 01_CEO/Decisoes_Autonomas/2026/Agosto.md:
"Learning Agent: Implementou [técnica] no Passo X (fonte: [vídeo] do [autor]).
Impacto esperado: [% redução de tempo / ganho de qualidade]. SKILL.md v2.5 → v2.6. PDF regenerado."
```

5. **Regenere PDFs:**
   - SKILL.md novo
   - Índice (se relacionado)
   - Livro-razão

6. **Atualize o Painel (se mudança é visível):**
   - Adicione evento `et:"sistema"` relatando a melhoria
   - Republique

#### E. PASSO 7e — Validação Antes de Confirmar
- [ ] Syntax check (Markdown não quebrou?)
- [ ] Semântica preservada (objetivo original intacto?)
- [ ] Backup criado (arquivo anterior está seguro?)
- [ ] Livro-razão registrado (como desfazer está documentado?)
- [ ] PDF regenerado (novo PDF existe?)
- [ ] Painel atualizado (if aplicável)?

### Critério de Sucesso (Ambos os casos)
**Caso A — Encontrou melhoria e implementou:**
- ✅ 3-5 vídeos foram assistidos via /watch:watch
- ✅ Técnica viável foi identificada e documentada
- ✅ SKILL.md foi atualizado (novo v2.X)
- ✅ Backup criado antes de alterar
- ✅ Livro-razão registrado
- ✅ PDFs regenerados
- ✅ Painel atualizado (if mudança visível)

**Caso B — Assistiu vídeos, não encontrou melhoria viável:**
- ✅ 3-5 vídeos foram assistidos
- ✅ Registrado: "Nenhuma técnica nova identificada nesta rodada" (Princípio 15)
- ✅ Documentado: "próximas buscas vão focar em [tema]"

### Bloqueadores Possíveis & Ações

| Bloqueador | Ação |
|---|---|
| WebSearch não acha bons vídeos | Refine termos — busque em YouTube direto — ou pule (Regra Desbloqueio) |
| Vídeo está em inglês / sem transcrição | Assista mesmo assim, tome notas — traduz conceito para português |
| Técnica aprendida é viável mas requer novo MCP/ferramenta | Descarte por agora — anote como "roadmap futuro" — não é melhoria imediata |
| Técnica é viável mas exigiria reescrever metade da rotina | Descarte — muito risco — faça uma melhoria menor em vez disso |
| Painel bloqueado (Artifact error) | Pule atualização do Painel — o SKILL.md mudou, isso é o importante |

### Tempo Estimado
- 3-5 vídeos × 10-15 min cada (assistir + extrair): **30-75 min** (longo!)
- **RECOMENDAÇÃO:** Se rodada já está em 60+ min, pule Passo 7 e faça amanhã (é auto-melhoria, não crítico)

### ⚠️ IMPORTANTE
**Quando NÃO Fazer Passo 7:**
- Se rodada já está consumindo muitos tokens
- Se há bloqueadores pendentes de dias anteriores (Passo 5 travado, Passo 6 bloqueado)
- Se Claudemberg pediu pausa nesta semana
- Se nenhuma melhoria foi encontrada em 2-3 rodadas consecutivas (retome em semana diferente)

---

## PASSO 8: BUSCA DE FERRAMENTA (GITHUB) + SKILL DE USABILIDADE

### O Que Fazer
Buscar **ferramenta/software pronto** no GitHub (ou fonte equivalente) que **algum Agente específico precisa** — com critérios rigorosos de custo/segurança. Redigi Skill de usabilidade para Drenagem Contínua instalar.

### Por Que Fazer
- Ferramenta é diferente de inteligência (Trilha A = conhecimento; Trilha B = tool)
- Drenagem Contínua é responsável por instalar/conectar — você só documenta
- Skill de ferramenta é **contrato** com Drenagem (precisa ser completa e honesta)

### Como Fazer

#### A. Checar Lacunas Abertas (ANTES de buscar)
**Leia:** `01_CEO/Gestores/[Gestor]/Agentes/[Agente]/_estado_[agente].md`

**Responda:**
- [ ] Este Agente tem lacuna aberta? (qual função falta?)
- [ ] A lacuna é "ferramenta não encontrada" ou "conhecimento não estruturado"? (Trilha B ou A?)
- [ ] Outra Skill de ferramenta foi proposta já? (não duplicar)

**Se não há lacuna clara:** pule este Agente nesta rodada

#### B. Definir Busca Precisa
Não busque genérico — busque ESPECÍFICO:

**Ruim:** "render tool MCP"
**Bom:** "Revit MCP conector para automação design linguagem natural + clash detection, gratuito, GitHub"

**Ruim:** "ferramenta IA para projeto"
**Bom:** "FEM structural analysis solver Python open-source CalculiX GitHub MIT license"

#### C. Buscar no GitHub Especificamente
**Ferramentas:** WebSearch + WebFetch + GitHub direto (GitHub topics)

**Critério: TODOS os 4 (sem exceção)**

1. **Custo zero**
   - [ ] Sem freemium com trava ("5 usos grátis, depois pague")
   - [ ] Sem SaaS que exija cartão
   - [ ] Orçamento = só Claude, nada mais
   - Se dúvida: descarte (economize esforço)

2. **Sem vazamento de dado de cliente**
   - [ ] Não exige upload de arquivo de projeto para servidor terceiro
   - [ ] Não retém dados por padrão operação
   - [ ] Se usa API externa: cheque privacy policy
   - Teste: "Se rodo isso localmente com dados sigiloso, saem dados?"

3. **Sem malware / vírus / typosquatting**
   - [ ] README existe e faz sentido
   - [ ] Atividade recente (commits últimos 6 meses)
   - [ ] Stars/forks compatível com tipo projeto (Revit MCP esperado ter 50+, landscape tool esperado 20+)
   - [ ] Sem pedido suspeito de credencial/senha
   - [ ] Sem sinal de typosquatting (nome muito similar a projeto famoso? descarte)
   - **NUNCA clone, instale ou rode código** — só leia README, veja código fonte, cheque issues

4. **Recurso já funcionando, não construção**
   - [ ] Projeto tem releases/tags (não é alpha perpétuo)
   - [ ] README de uso existe (não é só "work in progress")
   - [ ] Exemplos de uso ou demo rodando (prova que funciona)
   - [ ] Time/org atualiza (não é abandonado há anos)

#### D. Estrutura Obrigatória da Skill (Trilha B — Ferramentas)
**NUNCA varie desta estrutura:**

```markdown
---
name: [kebab-case-nome-skill]
description: "[uma frase — ferramenta, para qual Agente]"
metadata:
  type: skill
  gestor_alvo: [qual Gestor] — [qual Agente]
  status: proposta
  data: 2026-MM-DD
  fonte: [URL GitHub oficial]
---

# [Nome da Ferramenta] — Skill de Usabilidade

## Para qual Agente serve
[Agente específico, equipe de qual Gestor] — [função exata que a ferramenta cobre]

## Status
proposta | aguardando implantação | implantada [data]

## O que a ferramenta faz
[Função real, não marketing — 3-5 frases]

## Como se usa
[Procedimento específico bastante para Drenagem instalar sem perguntar:
- Instalação (comando, requisitos)
- Fluxo de entrada/saída (como o Agente vai usar?)
- Requisitos técnicos (Python 3.X, GPU memory, Revit version, etc.)
- Exemplo de uso
]

## Evidência de segurança (Princípio 3)
- Custo: [zero confirmado como / pago / freemium / SaaS]
- Vazamento de dado: [por que não vaza — self-hosted local, sem upload externo, etc.]
- Idoneidade: [README existente, X stars, Y forks, atividade recente (data last commit), ausência de sinal suspeito]

## Limitações honestas
[O que NÃO faz, o que falta, se é experimental, requisitos técnicos complexos]

## Fonte
[URL GitHub/oficial exata, data de verificação, última versão disponível]
```

#### E. Mapa de Busca por Agente (ATUALIZAR a cada rodada)
Não copie rodada anterior — **cheque de novo:**

| Agente | Lacuna Aberta | Buscar Por | Status Atual |
|--------|---|---|---|
| Oscar (Oscar) | Automação BIM além Vitruvius | Revit MCP + clash detection + QTO | Nenhum candidato confirmado ainda |
| Burle (Burle) | Render + vídeo gratuito self-hosted | WAN 2.2 / Blender MCP | WAN 2.2 em Drenagem já (não repetir) |
| Portinari (Portinari) | Apresentação estruturada (slides auto) | GitHub slides gerador gratuito | Nenhum candidato mapeado |
| Baumgart (Cardozo) | FEM estrutural | FreeCAD MCP / Estrutural solver | **ENCONTRADO 27/08 — freecad-mcp** |
| Landell (Cardozo) | Automação elétrica | MEP + elétrica GitHub MCP | Sem candidato gratuito ainda |
| Saturnino (Cardozo) | Hidrossanitário automação | Pipe/plumbing solver GitHub | Sem candidato gratuito ainda |
| Glaziou (Cardozo) | Paisagismo | Landscape design MCP/tool | Sem candidato gratuito ainda |
| Tenreiro (Cardozo) | Interiores | Interior design MCP/tool | Sem candidato gratuito ainda |
| Mindlin (Cardozo) | Apresentação complementares | Presentation gerador auto | Sem candidato gratuito ainda |

#### F. Regra de Exceção (CRÍTICA)
**Se busca não encontrar candidato que passe nos 4 critérios:**
- [ ] **NÃO invente Skill vazia** (Princípio 15 — redundância zero)
- [ ] Registre: "Nenhum achado novo que atenda critérios" no livro-razão
- [ ] Mantenha mapa de busca como está (para próxima rodada lembrar)
- [ ] Avance para próximo Agente/próxima rodada

### Critério de Sucesso

**Se encontrou ferramenta viável:**
- ✅ Todos os 4 critérios foram verificados (não apenas 3)
- ✅ Skill foi redigida conforme estrutura obrigatória
- ✅ "Como se usa" tem detalhe bastante para Drenagem instalar sem perguntar
- ✅ Limitações foram honestas (não oversell)
- ✅ Fonte é URL GitHub/oficial exata (não agregador)

**Se NÃO encontrou:**
- ✅ "Nenhum achado novo" foi registrado (não inventou)
- ✅ Motivo foi documentado ("critério 3 falhou: typosquatting suspeito")
- ✅ Próxima busca foi anotada (roadmap)

### Bloqueadores Possíveis & Ações

| Bloqueador | Ação |
|---|---|
| GitHub não acha nada no termo preciso | Varie os termos — ou descarte (Regra Desbloqueio) |
| Encontrei 2-3 candidatos, não sei qual escolher | Cheque os 4 critérios para cada — o que passa em TODOS? (raro haver empate) |
| Candidato é bom mas custo vago (não claro se é zero) | Descarte — regra é custo zero confirmado, não "provavelmente gratuito" |
| Ferramenta requer GPU/CPU específico (Oscar não tem) | Cheque _estado_oscar.md por hardware — se não tem, descarte |
| Vou encontrar ferramenta melhor se esperar 1 semana | Não espere — Se passa nos 4 critérios HOJE, proponha hoje — Drenagem decide |

### Tempo Estimado
- 1-2 Agentes × 15-20 min cada (busca + validação): **15-40 min** (varia)

---

## PASSO 9 (Não-obrigatório): FECHAMENTO DE ROTINA

### O Que Fazer
Preencher template de fechamento documentando o que saiu, bloqueadores, próxima ação.

### Por Que Fazer
- Próxima rodada lê este documento (não repete trabalho, não inventa evento)
- Claudemberg vê o que foi feito (relatório transparente)
- Arquivo se torna histórico (rastreabilidade)

### Como Fazer

**Arquivo:** `01_CEO/rotina_fechamento_template.md`

**Seções a preencher (ao final da rodada):**

```markdown
## [2026-08-27] Rotina Diária Skills v2.5 — FECHAMENTO

### Entregáveis
- [ ] Skills criadas: [nomes + versão]
- [ ] Skills documentadas: [paths salvas]
- [ ] PDFs regenerados: [quantos]
- [ ] Painel atualizado: Sim/Não (descrever eventos adicionados)
- [ ] Livro-razão registrado: Sim/Não (data/hora entrada)
- [ ] Learning Agent melhorias: [quantas implementadas + resumo]

### Bloqueadores (se houver)
- **Bloqueador 1:** [descrição]
  - Causa: [por quê trava]
  - Impacto: [o que não conseguiu fazer]
  - Próximo passo: [quem resolve, quando]
- (repita para cada bloqueador, ou deixe vazio se nenhum)

### Retrabalho Evitado (se houver)
- **Item 1:** Skill X não recriada (já existe v2 de DD/MM)
- (repita, ou deixe vazio)

### Status Final
- **Rodada:** ✅ Completa (8/8 passos) / ⚠️ Parcial (X de 8 passos)
- **Taxa de sucesso:** [X de Y itens planejados entregues]
- **Próxima rodada recomendação:** [2-3 prioridades baseadas em bloqueadores]
```

### Tempo Estimado
- **5 minutos** (formulário estruturado, copia resposta direta)

---

## IV. REGRAS GLOBAIS (Aplicam a Todos os Passos)

### 1. Princípio 3 — Sempre Validar Fonte
- **Não use:** agregadores, resumos secundários, blogs suspeitos
- **Use:** fonte primária (site oficial, GitHub repo, norma ABNT primária)
- **Teste:** "Se apago este blog amanhã, a informação ainda está disponível?"

### 2. Princípio 15 — Redundância Zero
- **Não crie Skill** se já existe similar no índice anterior
- **Não invente evento** para o Painel se nada de novo aconteceu
- **Se dúvida:** pesquise o índice anterior ou skills históricas antes de escrever

### 3. Governança — Backup Obrigatório
**Antes de alterar qualquer arquivo existente:**
```bash
cp [arquivo] 01_CEO/Decisoes_Autonomas/_backups/AAAA-MM-DD/[arquivo]
```
- Data no nome do backup (AAAA-MM-DD)
- Pasta de backup cria-se automaticamente se não existir
- Sem exceção

### 4. Governança — Livro-Razão Obrigatório
**Toda Skill/mudança vai ao livro-razão:**
```
Entrada em 01_CEO/Decisoes_Autonomas/2026/Agosto.md:
"[DD/MM] [Tipo de evento]: [resumo 1-2 linhas]. 
Arquivo: [path salvo]. Backup: [path backup]. 
Como desfazer: [instruções explícitas]."
```
- Sem "como desfazer" escrito = Claudemberg não consegue reverter = não publique

### 5. Tradução Obrigatória (Português)
- Qualquer conteúdo em inglês → traduzir antes de virar Skill
- Gestores não devem ter barreira de idioma
- Exceção: nomes próprios (ferramenta, autor, URL)

### 6. Segurança — Nunca Execute Código de Terceiro
- **NUNCA:** `npm install`, `pip install`, `git clone` ou rode scripts
- **SEMPRE:** WebFetch + leitura (README, código fonte, documentação)
- Esta fase é só avaliação de idoneidade — instalação é tarefa da Drenagem

### 7. Granularidade — Pense por Agente
- Cada Skill é para um Agente específico consumir
- "Pra quem serve?" deve ter resposta exata
- Não escreva "pra arquitetura geral" — escreva "para Oscar no Estudo Preliminar"

### 8. Veracidade Sobre Limitações
- Toda Skill tem seção "Limitações"
- **Não esconda:** "não testado em produção", "experimental", "requer GPU"
- Drenagem decide se implanta — com informação honesta

---

## V. COMO DESFAZER (Se Algo Sair Errado)

### Desfazer Skills Criadas
```bash
# Delete arquivo e entrada do índice
rm 01_CEO/Skills_Propostas/2026/Agosto/[skill-name].md
rm 01_CEO/Skills_Propostas/2026/Agosto/[skill-name].pdf  # se foi gerado

# Remova a linha do índice (edite indice.md)
# Remova a entrada do livro-razão (edite Agosto.md)
```
**Nenhum impacto em cliente/código** — tudo é só proposta

### Desfazer Atualização do Painel
```bash
# Restore de backup
cp 01_CEO/Decisoes_Autonomas/_backups/2026-MM-DD/painel_fundador_sttk.html 01_CEO/Painel_Fundador/painel_fundador_sttk.html

# Republique via Artifact (url preserva link antigo)
# Artifact.publish(file_path=..., url=3c28ec0d...)
```

### Desfazer Atualização do SKILL.md
```bash
# Restore versão anterior
cp 01_CEO/Decisoes_Autonomas/_backups/2026-MM-DD/wallenberg-rotina-diaria-skills-v2_SKILL.md 01_CEO/wallenberg-rotina-diaria-skills-v2_SKILL.md
```

---

## VI. CHECKLIST PÓS-ROTINA (Antes de Declarar "Concluído")

Marque cada item conforme completa:

- [ ] **Passo 1 (Pesquisa):** 5+ WebSearches rodaram, 2+ WebFetches validaram, achados têm URL/fonte/data
- [ ] **Passo 2 (Consolidação):** Achados foram categorizados por Gestor/Agente
- [ ] **Passo 3 (Redação):** Skills foram redigidas conforme estrutura padrão (ou nenhuma Skill necessária)
- [ ] **Passo 4 (Salvamento):** `.md` salvo em Skills_Propostas/2026/Mês/, índice atualizado
- [ ] **Passo 5 (PDFs):** Cada `.md` tem `.pdf` gêmeo (ou Regra Desbloqueio aplicada com impedimento registrado)
- [ ] **Passo 6 (Painel):** Eventos foram adicionados ao FEED (ou nada novo aconteceu — Princípio 15)
- [ ] **Passo 7 (Learning Agent):** 3-5 vídeos foram assistidos, melhoria foi (ou não) implementada (ou Regra Desbloqueio — pule se tempo)
- [ ] **Passo 8 (Ferramentas):** Busca dirigida rodou para Agentes com lacunas (ou nenhum candidato viável encontrado)
- [ ] **Governa:** Backup criado antes de alterar arquivo existente ✅
- [ ] **Livro-razão:** Entrada foi criada com "como desfazer" ✅
- [ ] **Fechamento:** Template preenchido (ou será feito depois, registrado como bloqueador) ✅

---

## VII. EXEMPLOS REAIS

### Exemplo 1 — Rodada Padrão (27/08/2026)
```
PASSO 1: WebSearch render MCP + Revit MCP + estrutural FEM
  ↓ Encontrou: Revit MCP 173 tools, FreeCAD FEM (CalculiX)
PASSO 2: Consolida → Oscar (Revit), Baumgart (FEM)
PASSO 3: Redação 2 Skills (ferramentas)
PASSO 4: Salva em Skills_Propostas/2026/Agosto/
PASSO 5: Gera 2 PDFs + índice
PASSO 6: Adiciona 2 eventos ao Painel (skills novas)
PASSO 7: [Opcional] Busca vídeo automação, encontra melhoria Consolidação → implementa
PASSO 8: [Já coberto] Revit + FreeCAD foram encontrados no Passo 1
GOVERNANÇA: Backups criados, livro-razão registrado
STATUS: ✅ Completa (7/8 passos + correção estrutural)
```

### Exemplo 2 — Rodada com Bloqueador (hipotético)
```
PASSO 1: Pesquisa OK
PASSO 2: Consolidação OK
PASSO 3: Redação 1 Skill
PASSO 4: Salvamento OK
PASSO 5: ❌ Bloqueador — script PDF retorna erro (permissão negada)
  → Aplicar Regra de Desbloqueio: registra impedimento, continua
PASSO 6: Painel — 1 evento adicionado (Skill de Passo 3)
PASSO 7: [Pula — tempo limitado]
PASSO 8: Nenhum candidato viável encontrado → "nenhum achado novo"
GOVERNANÇA: Backup + livro-razão OK, impedimento de Passo 5 registrado
STATUS: ⚠️ Parcial (6/8 passos + bloqueador em Passo 5)
PRÓXIMA: Tentar Passo 5 novamente amanhã ou resolver permissão
```

---

## VIII. TABELA RÁPIDA DE REFERÊNCIA

| Passo | Objetivo | Tempo Est. | Resultado | Bloqueador Comum |
|---|---|---|---|---|
| 1 | Pesquisa externa | 15-25 min | Achados brutos + URLs | Fonte fora do ar |
| 2 | Consolidação | 10-20 min | Mapa de prioridade | Não conseguir atribuir a Agente |
| 3 | Redação Skills | 30-60 min | Skills .md prontas | Não saber como escrever |
| 4 | Salvamento | 5-10 min | Arquivos em pasta certa | Pasta não existe |
| 5 | Gerar PDFs | 3-6 min | .pdf gêmeo para cada .md | Script erro / permissão negada |
| 6 | Atualizar Painel | 10-15 min | Painel republicado | Artifact error / HTML corrompido |
| 7 | Learning Agent | 30-75 min | Rotina melhorada (ou "nenhuma") | Vídeos não encontrados |
| 8 | Busca de Ferramenta | 15-40 min | Skill de usabilidade (ou "nenhuma") | Nenhum candidato viável |
| Fech. | Fechamento | 5 min | Template preenchido | Não há tempo |

---

## IX. APÊNDICE — CHECKLISTS VISUAIS, DASHBOARD E CRONJON PDF (NOVO — 27/08/2026)

### Checklist Diária (HTML Visual)
**Arquivo:** `01_CEO/Checklist_Diaria.html`

**Como usar:**
- Abra no navegador toda **segunda a quinta**
- Clique nos checkboxes conforme progride (60-75 min total)
- Arquivo automático guarda seu progresso (LocalStorage)
- Referencia Passos 1-4 + 8 do manual completo
- Segue mesmo layout/tema do Painel (integrado visualmente)

**O que você vê:**
- Seção PRÉ: 3 tarefas (leia fechamento, estado, painel) — 12 min
- Seção DURANTE: Passos 1-4 + 8 com tempo estimado cada
- Seção DEPOIS: 3 tarefas de fechamento (registre, backup, pronto pra sexta?)
- Resumo: cards mostrando Skills criadas, Gestores, Bloqueadores, Tempo (você preenche manual)

**Benefício:** Visão consolidada de uma rodada diária (sem necessidade de ler manual completo)

---

### Checklist Sexta (HTML Visual)
**Arquivo:** `01_CEO/Checklist_Sexta.html`

**Como usar:**
- Abra no navegador **toda sexta-feira** (uma única vez por semana)
- Clique nos checkboxes conforme progride (90-120 min total)
- Consolida semana inteira (seg-qui) em uma única atualização
- Referencia Passos 6-10 + Fechamento do manual completo

**O que você vê:**
- Cronograma da sexta (08:00–10:00 PASSOS 6-10, 10:00–10:15 FECHAMENTO)
- Passo 6: Atualizar Painel (40 min, com sub-tarefas)
- Passo 7: Learning Agent opcional (45 min)
- Passo 9 (NOVO): Ler Dashboard (10-15 min)
- Passo 10 (NOVO): Análise Semanal (20 min)
- Fechamento: 4 tarefas (template, métricas, backup, notifique gestores)
- Resumo: Skills semana, Skills testadas, Taxa sucesso, Gestor top (você preenche manual)

**Benefício:** Rotina semanal clara e separada (não é overhead — é consolidação)

---

### Dashboard no Painel (Seção MÉTRICAS — NOVO)
**Local:** Painel Fundador (`01_CEO/Painel_Fundador/painel_fundador_sttk.html`) — seção expandida **antes do footer**

**Cards visíveis (dados que você preenche sexta):**
1. **Skills Criadas** — número da semana (seg-qui)
2. **Skills Testadas** — quantas os Gestores/Agentes reportaram usar
3. **Taxa de Sucesso** — (testadas ÷ criadas × 100)
4. **Gestor Mais Ativo** — quem mais solicitou Skills (top)
5. **Próximas Prioridades** — anotações da sua análise semanal (Passo 10)

**Como preencher (toda sexta — Passo 9/10 do Checklist Sexta):**
- Abra o arquivo `painel_fundador_sttk.html` no Editor de Artifacts
- Localize os `id` de cada métrica: `metric-created`, `metric-tested`, etc.
- Substitua o valor `—` pelo número da semana
- Republicar artifact (mantém URL)

**Quem lê:**
- Claudemberg (sócios) — vê ROI de Skills (quantas foram de fato usadas)
- Gestores — veem se sua área foi top (incentivo)
- Wallenberg — vê taxa de sucesso (se rotina está rendendo)

**Exemplo (semana 27-31/08):**
```
Skills Criadas: 3
Skills Testadas: 2
Taxa de Sucesso: 67%
Gestor Mais Ativo: Kelsen (Legal) — 3 pedidos
Próximas Prioridades: resolver bloqueador Painel, focar em complementares sexta que vem
```

**Benefício:** Visão executiva centralizada (não precisa ler relatório longo)

---

### CronJob PDF (Automático — NOVO)
**O que faz:**
- Script `md_to_pdf.py` roda **toda noite às 20:00**
- Converte qualquer `.md` novo em `Skills_Propostas/2026/[Mês]/` → PDF
- PDFs prontos no mesmo diretório, pronto pra entregar

**Seu papel:**
- **Nada.** Automático.
- Amanhã (sexta 28/08) às 20:00 roda pela primeira vez
- Segunda de manhã (01/09), PDFs de seg-qui estão prontos
- Você só **valida se está tudo certo** (PDF não vazio, nome correto)

**Se der erro:**
- Script publica erro em log
- Você vê segundo/terça e corrige (raramente necessário)
- Nunca deixa Agente esperando — sempre tem `.md` disponível

**Benefício:** Zero overhead manual (PDFs geram sozinhos enquanto dorme)

---

## X. INTEGRAÇÃO — FLUXO VISUAL COMPLETO (NOVO — 27/08/2026)

**SEMANA VISTA COMO WALLENBERG:**

```
SEGUNDA 01/09        TERÇA 02/09          QUARTA 03/09        QUINTA 04/09        SEXTA 05/09
─────────────────    ────────────────     ────────────────    ────────────────    ─────────────
08:00 DIÁRIA         08:00 DIÁRIA         08:00 DIÁRIA        08:00 DIÁRIA        08:00 SEXTA
└─ Checklist_D.html  └─ Checklist_D.html  └─ Checklist_D.html  └─ Checklist_D.html  └─ Checklist_S.html
   60-75 min            60-75 min            60-75 min            60-75 min            90-120 min
   Passo 1-4+8          Passo 1-4+8          Passo 1-4+8          Passo 1-4+8          Passo 6-10
   ✓ Pesquisa           ✓ Pesquisa           ✓ Pesquisa           ✓ Pesquisa           ✓ Painel
   ✓ Consolidação       ✓ Consolidação       ✓ Consolidação       ✓ Consolidação       ✓ Learning (opt)
   ✓ Redação            ✓ Redação            ✓ Redação            ✓ Redação            ✓ Dashboard
   ✓ Salvamento         ✓ Salvamento         ✓ Salvamento         ✓ Salvamento         ✓ Análise
   ✓ Ferramentas        ✓ Ferramentas        ✓ Ferramentas        ✓ Ferramentas        ✓ Fechamento

   ↓ (cada noite)       ↓ (cada noite)       ↓ (cada noite)       ↓ (cada noite)       ↓ (20:00)
20:00 CronJob PDF    20:00 CronJob PDF    20:00 CronJob PDF    20:00 CronJob PDF    20:00 CronJob PDF
   (automático)         (automático)         (automático)         (automático)         (automático)
   ✓ PDFs gerado        ✓ PDFs gerado        ✓ PDFs gerado        ✓ PDFs gerado        ✓ PDFs gerado
     (dormindo)           (dormindo)           (dormindo)           (dormindo)           (dormindo)

           Painel      Painel      Painel      Painel      Painel atualizado
           estático    estático    estático    estático    (consolida seg-qui)
                                                            ✓ Dashboard + métricas
                                                            ✓ Próximas prioridades
```

**O QUE MUDOU (27/08):**
- ✅ Diária agora usa **Checklist_Diaria.html** (antes: arquivo manual gigante)
- ✅ Sexta agora usa **Checklist_Sexta.html** (antes: não tinha visual)
- ✅ Painel tem **seção MÉTRICAS** (antes: sem dados de ROI)
- ✅ CronJob PDF roda **automático** toda noite (antes: manual Passo 5)
- ✅ **Nenhuma rotina separada** — tudo integrado em um fluxo

**IMPORTANTE:** Nada é novo em termos de TRABALHO. Você fazia Passo 5 (PDF) manual — agora é automático. Você não tinha Dashboard — agora tem visibilidade. Os Passos 1-4+8 são os mesmos. Sexta continua sendo a consolidação que já era — só virou visual em um Checklist.

---

## X. REFERÊNCIAS RÁPIDAS

### Arquivos Principais
- **Rotina v2.5 (este doc):** `wallenberg-rotina-diaria-skills-v2_SKILL.md`
- **Checklist Diária (HTML visual):** `01_CEO/Checklist_Diaria.html` ⭐ NOVO
- **Checklist Sexta (HTML visual):** `01_CEO/Checklist_Sexta.html` ⭐ NOVO
- **Fechamento anterior:** `rotina_fechamento_template.md`
- **Livro-razão:** `01_CEO/Decisoes_Autonomas/2026/Agosto.md`
- **Skills:** `01_CEO/Skills_Propostas/2026/Agosto/` (cria novo `.md` por Skill)
- **Painel (com MÉTRICAS):** `01_CEO/Painel_Fundador/painel_fundador_sttk.html` ⭐ EXPANDIDO
- **Script PDFs (automático):** `_ferramentas/md_to_pdf.py`

### Comandos Comuns
```bash
# Backup antes de alterar
cp [arquivo] 01_CEO/Decisoes_Autonomas/_backups/$(date +%Y-%m-%d)/[arquivo]

# Gerar PDF
python "_ferramentas/md_to_pdf.py" "01_CEO/Skills_Propostas/2026/Agosto/[skill].md"

# Checar se Skill já existe (antes de escrever)
ls 01_CEO/Skills_Propostas/2026/*/[palavras-chave]* | head -5
```

### Contatos de Desbloqueio
- **Ferramenta trava:** Claudemberg (ratificação / decisão)
- **Arquivo não existe:** crie conforme template
- **Permissão negada:** Regra de Desbloqueio — pule, registre
- **Dúvida sobre Skill:** releia Passo 3 ou procure exemplo anterior

---

**VERSÃO:** 2.6 (27/08/2026 — Checklists + Dashboard + CronJob integrados)  
**PRONTO PARA:** Wallenberg executar AMANHÃ (sexta 28/08) com rotina sexta nova + CronJob  
**PRÓXIMA IMPLEMENTAÇÃO:** Segunda 01/09/2026 — rotina diária nova com Checklist visual
