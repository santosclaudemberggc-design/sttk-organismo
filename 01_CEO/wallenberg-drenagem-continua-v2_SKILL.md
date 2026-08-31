---
name: wallenberg-drenagem-continua-v2-3
version: 2.3.0
created: 2026-07-27
recriado: 2026-08-28
based_on: "Especificação completa fornecida por Claudemberg em 28/08/2026 — campos B e C copiados integralmente, sem reescrita, a pedido dele"
---

# 📋 WALLENBERG DRENAGEM CONTÍNUA v2.3 — ESPECIFICAÇÃO COMPLETA

## A. METADADOS (Configuração Básica)

```
Nome da Rotina: Wallenberg drenagem continua v2.3
Status: Ativo
Agendamento: Todos os dias 10:15 (seg-sex) — 1h após Rotina Diária Skills
Duração esperada: 60-90 min (paralelo + validação)
Versão: 2.3.0 (Divisão final 25/08/2026)
Data criação: 27/07/2026 | Última atualização: 25/08/2026
Arquivo de instrução: 01_CEO/wallenberg-drenagem-continua-v2_SKILL.md
```

---

## B. CAMPO: DESCRIÇÃO (Copiar integralmente)

```
Wallenberg Drenagem Contínua v2.3 — Implementação + Gestores + Auto-Melhoria
Agente CEO executa autonomamente 10:15 (após Skills diárias). Lê Skills 
criadas pela Diária (Status: proposta) → Avalia tipo (habilidade vs ferramenta) 
→ Cria Gestores faltantes (respeitando hierarquia) → Testa Gestores → Implanta 
ferramenta (APENAS se Autonomous) → Varredura de melhoria (Gestor sem pendências) 
→ Learning Agent aperfeiçoa rotina → Atualiza Painel. Relatório de execução ao fim. 
Sem interferência humana.
```

---

## C. CAMPO: INSTRUÇÕES (Copiar integralmente)

```
⚠️ WALLENBERG — DRENAGEM CONTÍNUA EXECUTE AUTONOMAMENTE (v2.3)
═══════════════════════════════════════════════════════════════
🎯 TODOS OS DIAS (Seg-Sexta, 10:15 — Após Rotina Diária Skills)
⏱️  Tempo total: 60-90 min | Paralelo onde possível
═══════════════════════════════════════════════════════════════

🔹 FASE 1: PREPARAÇÃO & DESCOBERTA (5-10 min)

✅ Passo 0: Leia arquivo de estado
   └─ 01_CEO/_estado_wallenberg.md (Seção 1: Onde parei / em andamento)
   └─ Contexto: Rodadas anteriores, bloqueios pendentes, progresso

✅ Passo 1: Descubra Gestores existentes
   └─ Rode Glob: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\.claude\agents\*.md
   └─ Cruze com: 01_CEO/Gestores/{Nome} (...)/ 
   └─ Resultado: Lista dinâmica de Gestores (Kelsen, Lúcio, Cardozo, futuro Fechamento)

✅ Passo 2: Leia pendências
   └─ Arquivo: 01_CEO/Pendencias/pendencias.json
   └─ Schema: owner, agente, crit, alc, res, acao, status, resolvido_em
   └─ Separe por owner: Qual pendência é de qual Gestor?
   └─ Reconcilie: Notion "Treinos e Testes" vs pendencias.json

═══════════════════════════════════════════════════════════════
🔹 FASE 2: LEITURA DE SKILLS (5 min)

✅ Passo 3: Leia Skills criadas pela Diária (Status: "proposta")
   └─ Pasta: 01_CEO/Skills_Propostas/2026/Agosto/ (mês corrente)
   └─ Para cada Skill:
      ├─ Tipo? (Habilidade/Inteligência OU Ferramenta/Tool)
      ├─ Para qual Gestor?
      ├─ Gestor existe? (responda: SIM / NÃO)
      └─ Se existe, qual nível? (Formação / Aprendizado / Especialista / Autonomous)

═══════════════════════════════════════════════════════════════
🔹 FASE 3: CRIAÇÃO DE INFRAESTRUTURA — RESPEITANDO HIERARQUIA (10-15 min)

✅ Passo 4: Para cada Skill SEM Gestor
   
   1. VERIFIQUE HIERARQUIA:
      ├─ Legal (Kelsen) é pré-requisito?
      │  └─ Se Skill é sobre legislação → Kelsen DEVE existir antes
      │
      ├─ Arquitetura (Lúcio) depende de Legal?
      │  └─ Se Skill é sobre arquitetura → Lúcio precisa Kelsen existindo
      │
      ├─ Complementares (Cardozo) depende de Arquitetura?
      │  └─ Se Skill é sobre complementares → Cardozo precisa Lúcio existindo
      │
      └─ Fechamento depende de Complementares?
         └─ Se Skill é sobre fechamento → Fechamento precisa Cardozo existindo
   
   2. SE HIERARQUIA BLOQUEADA:
      └─ Skill Status: "bloqueada por hierarquia — aguarda Gestor {pai}"
      └─ Registre no livro-razão: "Skill X bloqueada, aguarda criação Gestor Y"
      └─ Sinalize para Claudemberg (decisão necessária)
   
   3. SE HIERARQUIA OK — CRIE GESTOR:
      ├─ Cria em nível: "Formação" (não Autonomous ainda)
      ├─ Cria estrutura:
      │  ├─ .claude/agents/{gestor}.md (com tools: Agent)
      │  ├─ 01_CEO/Gestores/{Gestor} ({Tipo})/
      │  ├─ 01_CEO/Gestores/{Gestor}/Agentes/ (pasta vazia, aguarda equipe)
      │  └─ _estado_{gestor}.md (arquivo de estado)
      ├─ Registra no livro-razão: Qual Gestor, por quê, hierarquia respeitada
      └─ Skill Status: "Gestor criado em Formação, aguardando Autonomous"

═══════════════════════════════════════════════════════════════
🔹 FASE 4: ACIONAMENTO DE GESTORES (Paralelo, 20-30 min)

✅ Passo 5: Para CADA Gestor encontrado (ação em paralelo):
   
   5.a. ACIONE o Gestor:
        └─ Use Agent tool: subagent_type = "{gestor}" em minúsculas
        
   5.b. PEÇA que ele LEIA e RECONCILIE:
        ├─ Próprio arquivo de estado (_estado_{gestor}.md)
        ├─ Notion "Treinos e Testes" (filtro: Gestor = {nome}, Status = pendente)
        ├─ Reconcilie fila antes de reportar:
        │  ├─ Pendência já resolvida? → Remove
        │  ├─ Pendência em sua alçada (auto)? → Executa + registra
        │  └─ Só o que cruza fronteira → Sinaliza sem executar
        
   5.c. PASSE ITENS DE PENDENCIAS.JSON (seu owner):
        ├─ Para alc:"auto" (autonomia delegada):
        │  └─ Executa a acao descrita literalmente (não é sugestão)
        │  └─ Se bloquear → Registra bloqueio, não fica esperando
        │
        └─ Para alc:"humano"/"tecnico"/"planejado":
           └─ Apenas confirma se segue real (reconcilia contra arquivos)
   
   5.d. SE GESTOR NÃO TEM EQUIPE AINDA:
        └─ Não force nada → Ele relata o que está pendente (ex: exame de nível)
        └─ Não administre exame (é julgamento seu, deliberado, não lote)
   
   5.e. SE GESTOR PRECISA ACIONAR AGENTE DA PRÓPRIA EQUIPE:
        └─ Confira .claude/agents/{gestor}.md → Agent na lista tools?
        └─ SIM: Peça ao Gestor acionar Agente direto (na mesma chamada)
        └─ NÃO (Gestor novo): Você aciona e devolve artefato para Gestor auditar
        └─ Você recebe resumo final (intermediário Gestor↔Agente fica oculto)
   
   RESULTADO: Relatório de cada Gestor (execuções reais, bloqueios, próximas ações)

═══════════════════════════════════════════════════════════════
🔹 FASE 5: IMPLANTAÇÃO DE FERRAMENTA (10-20 min)

✅ Passo 6: Para cada Skill com Status "proposta" (tipo Ferramenta):
   
   1. VERIFICA NÍVEL DO GESTOR:
      
      ├─ Autonomous? (nível máximo)
      │  └─ SIM → Prossiga
      │  └─ NÃO → Pule para "Aguardando Autonomous" abaixo
      
   2. SIM — AUTONOMOUS, IMPLANTE:
      ├─ Leia Skill inteira (verifique se suficiente para instalar)
      ├─ Se incompleta → NÃO invente o que falta
      │  └─ Marque: Status = "skill incompleta, devolvida para Diária Skills"
      │  └─ Registre exatamente o que falta
      │  └─ Não prossegue
      │
      ├─ Se suficiente → Execute implantação:
      │  ├─ Instale exatamente conforme Skill descreve (npm, conexão MCP, etc)
      │  ├─ Conecte ao agente (.claude/agents/{agente}.md se MCP)
      │  ├─ Teste tecnicamente (não é caso cliente, é validação técnica)
      │  └─ Registre resultado real: Funcionou como documentado? Divergiu?
      │
      └─ Atualize Skill Status:
         ├─ "implantada" (funcionou perfeitamente)
         └─ "implantada com ressalva" (divergiu em algo, describe)
   
   3. NÃO — FORMAÇÃO/APRENDIZADO, AGUARDE:
      └─ Skill Status: "pronta, aguardando Gestor atingir Autonomous"
      └─ Ferramenta fica pronta MAS NÃO APLICA à equipe ainda
      └─ Próxima rodada (quando Gestor for Autonomous) → Implanta

═══════════════════════════════════════════════════════════════
🔹 FASE 6: VARREDURA DE MELHORIA (5-15 min — Se Gestor sem pendências)

✅ Passo 7: Se um Gestor NÃO tem pendência (lista limpa):
   
   └─ NUNCA fica parado (correção Claudemberg 07/08)
   └─ Peça varredura concreta na própria área:
      ├─ Skill/POP com lacuna que já suspeita
      ├─ Padrão de erro recorrente na equipe (histórico)
      ├─ POP desatualizado (não está "aberta", mas está desatualizado)
      ├─ Capacidade/ferramenta que falta (nunca foi formalizada como gap)
      ├─ Treino/exame de nível de Agente não administrado
      
   └─ Se encontrar algo real E resolvível na alçada:
      ├─ Executa + Registra (novo item pendencias.json, já "resolvida")
      
   └─ Se varredura não rende nada:
      ├─ AINDA ASSIM registre no arquivo de estado dele: O que foi checado
      └─ (Obrigação é fazer varredura de verdade, não garantir achado)

═══════════════════════════════════════════════════════════════
🔹 FASE 7: LEARNING AGENT & RASTREABILIDADE (15-25 min)

✅ Passo 8a: LEARNING AGENT — Auto-melhoria da rotina
   
   1. PESQUISE VÍDEOS:
      ├─ YouTube: "Autonomous agents workflow", "Multi-agent systems", "Claude AI"
      ├─ Instagram: maxcarrau.ia, 99hud, seanaiux, o.engenheirolider, sobre.arq, goxyvi
      ├─ WebSearch: "automação delegação", "otimização rotinas", "IA arquitetura"
      └─ Localize: 3-5 fontes alta qualidade (views, data recente, confiável)
   
   2. ANALISE VIA /watch:watch:
      └─ Vídeos longos: Transcreva e extraia implementações concretas
      └─ Instagram reels: Leia comentários, não só caption
      └─ Identifique: Padrões de sucesso, problemas resolvidos
   
   3. MAPEIE PARA ESTA ROTINA:
      └─ "Qual passo desta rotina poderia otimizar?"
      └─ "Existe gap entre o que fazemos e o vídeo mostra?"
      └─ Exemplos possíveis:
         ├─ Passo 1: Descobrir Gestores mais eficientemente (caching)
         ├─ Passo 2: Reconciliação paralela de Notion vs JSON
         ├─ Passo 3: Acionar Gestores ainda mais rápido
         └─ Passo 7: Varredura de melhoria com IA (metatask)
   
   4. SE ENCONTRAR OPORTUNIDADE REAL:
      ├─ Documente mudança: [NOVO v2.X] — data, técnica, vídeo fonte, passo afetado
      ├─ Faça backup: 01_CEO/Decisoes_Autonomas/_backups/AAAA-MM-DD/wallenberg-drenagem-continua-v2_SKILL.md
      ├─ Modifique SKILL.md: Atualize passo específico (mantenha intenção original)
      ├─ Registre no livro-razão: "Learning Agent: Implementou [técnica] no Passo Y"
      ├─ Regenere PDF gêmeo
      └─ (NÃO EXECUTA — só propõe para Claudemberg revisar)

✅ Passo 8b: REGISTRO NO LIVRO-RAZÃO
   
   └─ SE houve execução real (Gestor resolveu algo, Agente produziu, item "auto" fechou):
      ├─ Registre em: 01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md
      ├─ Modelo: O que foi decidido, por quê, o que foi criado/alterado, backup, como desfazer
      ├─ Uma entrada por Gestor com execução real (não genérica)
      └─ Gere PDF gêmeo (exceto arquivos de estado)
   
   └─ SE item de pendencias.json foi resolvido:
      ├─ Edite arquivo: Status → "resolvida", resolvido_em → AAAA-MM-DD
      └─ Não apague o item (é histórico)

✅ Passo 8c: ATUALIZAÇÃO DO PAINEL FUNDADOR
   
   └─ SE houve execução real nesta rodada:
      ├─ Leia livro-razão do mês (01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md)
      ├─ Para cada decisão/evento de HOJE ainda não no FEED:
      │  └─ PREPENDE novo objeto abaixo de FEED-AUTO (mais recente no topo)
      │  └─ Formato: {d:"DD/MM",et:"TIPO",t:"título",who:"quem",p:"frase"}
      │  └─ Tipos válidos: decisao, promocao, agente, skill, sistema, correcao, marco, capacidade
      ├─ Atualize data: <span class="updated">DD/MM/AAAA</span>
      ├─ Se card mudou estado (ex: Gestor promovido) → Atualiza só aquele card
      ├─ Republique com Artifact (mesma URL)
      └─ Registre no livro-razão: O que atualizou no painel
   
   └─ SE nada aconteceu hoje: Não republique nem registre (Princípio 15)

═══════════════════════════════════════════════════════════════
🔹 FASE 8: VIGILÂNCIA & RESUMO FINAL (5-10 min)

✅ Passo 9: AUTOESCALONAMENTO — Detecta padrões de estagnação
   
   └─ Após Passos 1-8, confira cada Gestor:
      ├─ SEM execução real NEM varredura real nesta rodada?
      │  └─ Sinalize: "SEM PROGRESSO ESTA RODADA: {Gestor}"
      │
      └─ Padrão de estagnação (N rodadas consecutivas)?
         └─ Sinalize: "PADRÃO ESTAGNAÇÃO: {Gestor} há N rodadas — escalona para Claudemberg"
         └─ Necessita revisão humana (bloqueio real ou desalinhamento?)

✅ Passo 10: RESUMO FINAL
   
   └─ Para CADA Gestor processado (2-4 linhas):
      ├─ O que encontrou
      ├─ O que resolveu sozinho (quantos itens "auto" de pendencias.json fechou)
      ├─ Se acionou Agente da equipe (por quê)
      ├─ O que registrou no livro-razão
      
   └─ Se Gestor não tinha nada: Uma linha, siga para próximo
   
   └─ Fechamento com métricas totais:
      ├─ Quantos Gestores passaram pela rodada
      ├─ Quantos tiveram execução real
      ├─ Quantos itens de pendencias.json foram fechados
      ├─ Quantas melhorias Learning Agent propôs
      ├─ Quanto tempo (início-fim)

═══════════════════════════════════════════════════════════════
🚨 FRONTEIRA CRÍTICA — NUNCA EXECUTE:
❌ Documento de cliente real (DULI, Anexos, memorial, prancha)
❌ Gates 13, 16 (validação de projeto técnico com Maurício)
❌ Protocolo em prefeitura
❌ Eliminação de Gestor ou Agente
❌ Dúvida entre "organismo" vs "cliente"? → Trata como cliente, não executa, sinaliza
═══════════════════════════════════════════════════════════════

📁 Pasta Principal: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\

📄 ARQUIVOS QUE VOCÊ CONSULTA/EDITA:
   • 01_CEO/_estado_wallenberg.md (Seção 1: estado)
   • 01_CEO/Pendencias/pendencias.json (fila estruturada)
   • 01_CEO/Skills_Propostas/2026/{Mês}/*.md (Skills da Diária)
   • 01_CEO/Gestores/{Gestor}/Agentes/ (estrutura de equipe)
   • 01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md (livro-razão)
   • 01_CEO/Painel_Fundador/painel_fundador_sttk.html (Dashboard)
   • Notion: "Treinos e Testes" (data source: collection://7b0728a8-fd57-419c-8a51-d5fe3794d165)

🚀 PRINCÍPIOS QUE GUIAM:
   1, 2, 3, 4, 5, 6, 7, 8 (rastreabilidade)
   13 (autonomia com contas) — Executa, mas documenta tudo
   15 (redundância zero) — Não inventa trabalho fictício
   17 (aprendizado compartilhado) — Learning Agent

CLIENTE > FERRAMENTA: Se execução de Gestor com cliente bloqueia, implantação fica para próxima.

Execute conforme descrito. Relatório ao fim.
```

---

## D. DOCUMENTOS DE SUPORTE (Que criar ou referenciar)

```
Arquivo de Estado

📄 _estado_wallenberg.md
   ├─ Seção 1: Onde parei / em andamento
   │  └─ Última rodada: Data, Gestores processados, bloqueios
   │  └─ Padrões observados: Estagnação em algum Gestor?
   │  └─ Próximo foco: O que fazer na próxima rodada?
   │
   └─ Atualizado ao fim de cada rodada de Drenagem

📄 _estado_{gestor}.md (para cada Gestor)
   ├─ Seção 1: Onde parei / em andamento
   ├─ Nível atual: Formação / Aprendizado / Especialista / Autonomous
   ├─ Pendências em aberto: (linked para pendencias.json)
   └─ Atualizado ao fim de cada acionamento

Bases Externas

📄 01_CEO/Pendencias/pendencias.json
   ├─ Schema único de fila: owner, agente, crit, alc, res, acao, status, resolvido_em
   ├─ Seu arquivo-fonte (não duplicar em outro lugar)
   └─ Editar para marcar itens como "resolvida"

📄 Notion: "Treinos e Testes"
   ├─ Data source: collection://7b0728a8-fd57-419c-8a51-d5fe3794d165
   ├─ Filtros: Gestor = {nome}, Status = pendente
   └─ Reconciliar vs pendencias.json

Livro-Razão

📄 01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md
   ├─ Entrada por Gestor com execução real
   ├─ Cada entrada: O que decidiu, por quê, backup, como desfazer
   └─ Fonte única de verdade para updates do Painel

Painel

📄 01_CEO/Painel_Fundador/painel_fundador_sttk.html
   ├─ FEED-AUTO: Prependa eventos de hoje
   ├─ Cards: Atualize se mudou estado (Gestor promovido, etc)
   ├─ Data atualizado: Sempre hoje (DD/MM/AAAA)
   └─ Republicar com Artifact (mesma URL)

Manuais de Referência (Markdown)

📄 wallenberg-drenagem-continua-v2_3_REDEFINIDO.md
   ├─ Detalhamento completo de Passos 1-10
   ├─ Explicação de cada Fase
   ├─ Hierarquia de Gestores
   ├─ Exemplos de execução (item "auto" resolvido, como agir)
   └─ Tamanho: Compacto (ref. consulta)

📄 rotina_fechamento_template.md
   ├─ Template que Wallenberg lê ANTES de cada rodada
   ├─ O que foi entregue na rodada anterior
   ├─ O que ficou pendente
   ├─ Retrabalho a evitar
   └─ Para quem? Wallenberg (contexto antes de começar)
```

---

## E. PASSOS DETALHADOS (Fases 1-8)

```
FASE 1: PREPARAÇÃO & DESCOBERTA

Passo 0: Leia Arquivo de Estado
Arquivo: 01_CEO/_estado_wallenberg.md (Seção 1)
Responda:
- Onde parei na rodada anterior?
- Que Gestores ficaram bloqueados?
- Que padrões observei?
- O que priorizar hoje?
Resultado: Contexto para não reinventar a roda

Passo 1: Descubra Gestores Dinamicamente
NÃO use lista fixa (Kelsen, Lúcio)
Execute:
1. Glob: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\.claude\agents\*.md
2. Cruze com: 01_CEO/Gestores/{Nome} (...)/
3. Verdadeiro Gestor = arquivo .claude/agents/{nome}.md 
                      + pasta 01_CEO/Gestores/{Nome} (...)/
Resultado: Lista dinâmica (cresce quando Cardozo/Fechamento forem criados)

Passo 2: Leia e Reconcilie Pendências
Leia: 01_CEO/Pendencias/pendencias.json
Schema: owner, agente, crit, alc, res, acao, status, resolvido_em
Ações:
- Separe por owner (qual pendência é de qual Gestor)
- Filtre: status = "aberta"
- Cruze com Notion "Treinos e Testes"
Resultado: Fila reconciliada, pronta para Passo 5

FASE 2: LEITURA DE SKILLS

Passo 3: Avalie Skills Criadas
Pasta: 01_CEO/Skills_Propostas/2026/Agosto/
Para cada Skill com Status = "proposta":
1. TIPO:
   ├─ Habilidade/Inteligência (conhecimento, não tool)
   └─ Ferramenta/Tool (instalar, conectar)
2. GESTOR DESTINO:
   └─ Para qual Gestor? (Kelsen/Lúcio/Cardozo/Fechamento)
3. EXISTE:
   ├─ SIM → Qual nível? (Formação/Aprendizado/Especialista/Autonomous)
   └─ NÃO → Vai ser criado no Passo 4
Resultado: Checklista de Skills prontas para próximos passos

FASE 3: CRIAÇÃO DE INFRAESTRUTURA

Passo 4: Crie Gestores Respeitando Hierarquia
Para cada Skill SEM Gestor:
HIERARQUIA (respeite a ordem):
1. Legal (Kelsen) — Sem dependências, cria sempre
2. Arquitetura (Lúcio) — Depende de Kelsen
3. Complementares (Cardozo) — Depende de Lúcio
4. Fechamento — Depende de Cardozo
FLUXO:
├─ Skill é sobre legislação?
│  ├─ SIM: Kelsen deve existir → Cria se não existir
│  └─ NÃO: Siga
│
├─ Skill é sobre arquitetura?
│  ├─ SIM: Lúcio deve existir AND Kelsen deve existir
│  │       Se Kelsen não existe → BLOQUEIA (Skill "bloqueada por hierarquia")
│  │       Se Lúcio não existe → Cria Lúcio (com Kelsen como pré-req)
│  └─ NÃO: Siga
│
├─ Skill é sobre complementares?
│  ├─ SIM: Cardozo deve existir AND Lúcio deve existir AND Kelsen deve existir
│  │       Se algum falta → BLOQUEIA
│  │       Se todos existem → Cria Cardozo se não existir
│  └─ NÃO: Siga
│
└─ Skill é sobre fechamento?
   ├─ SIM: Fechamento deve existir AND Cardozo/Lúcio/Kelsen devem existir
   │       Se algum falta → BLOQUEIA
   │       Se todos existem → Cria Fechamento se não existir
   └─ NÃO: Nenhum Gestor aplicável
QUANDO CRIA GESTOR:
1. Nível: "Formação" (não Autonomous ainda)
2. Estrutura:
   ├─ .claude/agents/{gestor}.md (tools: Agent)
   ├─ 01_CEO/Gestores/{Gestor} ({Tipo})/
   ├─ 01_CEO/Gestores/{Gestor}/Agentes/ (vazia, aguarda equipe)
   └─ _estado_{gestor}.md (arquivo de estado)
3. Livro-razão: Registre criação + hierarquia respeitada
4. Skill Status: "Gestor criado em Formação, aguardando Autonomous"
Resultado: Gestores criados em ordem, hierarquia respeitada

FASE 4: ACIONAMENTO DE GESTORES (Paralelo)

Passo 5: Acione Gestores e Processe Pendências
Para CADA Gestor (em paralelo, não sequencial):
5.a. ACIONE:
     └─ Agent tool: subagent_type = "{gestor}" (minúsculas)
5.b. PEÇA QUE LEIA E RECONCILIE:
     ├─ Próprio arquivo de estado (_estado_{gestor}.md)
     ├─ Notion "Treinos e Testes" (filtro: seu nome, Status=pendente)
     ├─ Reconcilie antes de reportar:
     │  ├─ Pendência já resolvida? Remove
     │  ├─ Pendência em sua alçada (auto)? Executa + registra
     │  └─ Cruza fronteira? Sinaliza sem executar

5.c. PASSE ITENS DE PENDENCIAS.JSON (seu owner):
     ├─ alc:"auto" (autonomia delegada):
     │  └─ EXECUTA literalmente (não é sugestão)
     │  └─ Se bloquear → Registra bloqueio, não fica esperando
     │
     └─ alc:"humano"/"tecnico"/"planejado":
        └─ Apenas CONFIRMA se segue real (reconcilia vs arquivos)
5.d. SE SEM EQUIPE:
     └─ Não force → Apenas relata pendências (ex: exame de nível aguardando)
5.e. SE PRECISA ACIONAR AGENTE:
     ├─ Verifica: Agent em .claude/agents/{gestor}.md?
     ├─ SIM: Gestor aciona Agente direto (você recebe resumo)
     └─ NÃO (Gestor novo): Você aciona, devolve artefato para Gestor auditar
RESULTADO: Relatório de cada Gestor
├─ Execuções reais: O que fez
├─ Itens "auto" fechados: Quantos
├─ Bloqueios: O que não deu
└─ Próximas ações

FASE 5: IMPLANTAÇÃO DE FERRAMENTA

Passo 6: Implante Skills Tipo "Ferramenta" (Se Autonomous)
Para cada Skill Status="proposta" do tipo Ferramenta/Tool:
1. VERIFICA NÍVEL:
   ├─ Gestor destino = Autonomous?
   │  ├─ SIM → Prossiga
   │  └─ NÃO → Pule para "Aguardando" abaixo
2. SIM — AUTONOMOUS, IMPLANTE:
   
   ├─ Leia Skill inteira:
   │  └─ Suficiente para instalar? (comando, requisitos, passos claros)
   │
   ├─ Se incompleta:
   │  ├─ NÃO invente o que falta
   │  ├─ Marque: Status = "skill incompleta, devolvida"
   │  └─ Registre: O que falta exatamente
   │
   ├─ Se suficiente, execute:
   │  ├─ Instale exatamente conforme descrito (npm, pip, MCP, etc)
   │  ├─ Conecte ao agente (.claude/agents/{agente}.md se MCP)
   │  ├─ Teste tecnicamente (não é caso cliente, é validação)
   │  ├─ Registre resultado real:
   │  │  ├─ Funcionou como documentado? SIM
   │  │  ├─ Divergiu em algo? QUAL?
   │  │  └─ Bloqueios técnicos? QUAL?
   │  │
   │  └─ Atualize Skill Status:
   │     ├─ "implantada" (tudo OK)
   │     └─ "implantada com ressalva" (divergiu, descrever)
3. NÃO — FORMAÇÃO/APRENDIZADO, AGUARDE:
   └─ Skill Status: "pronta, aguardando Autonomous"
   └─ Ferramenta fica pronta MAS não conecta à equipe ainda
   └─ Próxima rodada (quando Autonomous) → Implanta
REGRA DE PRIORIDADE:
├─ Cliente Real > Ferramenta (se bloqueia, adia para próxima rodada)
└─ Se nenhuma Skill pendente: Registre "nenhuma pendente", não invente
Resultado: Ferramenta implantada ou em espera (status claro)

FASE 6: VARREDURA DE MELHORIA

Passo 7: Gestor Sem Pendências Faz Varredura
Se um Gestor NÃO tem pendência (lista limpa):
NÃO fica parado (correção Claudemberg 07/08/2026)
Peça varredura concreta na própria área:
├─ Skill/POP com lacuna conhecida (nunca formalizou)
├─ Padrão de erro recorrente na equipe (histórico)
├─ POP desatualizado (não é "aberta", mas está velho)
├─ Capacidade/ferramenta que falta (gap nunca formalizado)
└─ Treino/exame de nível de Agente (ainda não administrado)
Se encontra algo real E resolvível em sua alçada:
├─ Executa + Registra em pendencias.json
└─ Status: Já "resolvida", mas registra execução
Se varredura não rende nada:
├─ REGISTRE NO ARQUIVO DE ESTADO: "Varredura checou X, Y, Z — nada encontrado"
└─ (Obrigação é fazer varredura DE VERDADE, não garantir resultado)
Resultado: Melhoria interna contínua, Gestor nunca ocioso

FASE 7: LEARNING AGENT & RASTREABILIDADE

Passo 8a: Learning Agent (Pesquisa + Propõe)
Pesquise vídeos sobre:
├─ Autonomous agents optimization
├─ Multi-agent queue management
├─ Delegação automática
├─ Claude AI tutorials
├─ IA em arquitetura
└─ Produtividade em construção
Fontes paralelas:
├─ YouTube: "Autonomous agents", "Claude AI", vídeos longos (transcrever)
├─ Instagram: maxcarrau.ia, 99hud, seanaiux, o.engenheirolider, goxyvi
├─ WebSearch: Implementações reais, case studies
Localize: 3-5 fontes de alta qualidade (views adequados, data recente)
Analise:
├─ Implementações concretas: Como fazem?
├─ Padrões de sucesso: O que funcionou?
└─ Problemas resolvidos: Como resolveram?
Mapeie para esta rotina:
├─ "Qual passo desta rotina pode otimizar?"
├─ "Gap entre o que fazemos e o vídeo mostra?"
├─ Exemplos possíveis:
│  ├─ Passo 1: Descobrir Gestores com caching
│  ├─ Passo 2: Reconciliação paralela (mais rápido)
│  ├─ Passo 5: Acionar múltiplos Gestores simultaneamente (já fazemos)
│  └─ Passo 7: Varredura de melhoria com IA (metatask)
SE encontrar oportunidade real:
├─ Documente: [NOVO v2.X] — data, técnica, vídeo fonte, passo afetado
├─ Backup: Antes de editar
├─ Modifique: SKILL.md (atualize passo, mantenha intenção)
├─ Registre: No livro-razão
├─ Regenere: PDF gêmeo
└─ (NÃO EXECUTA — só propõe para Claudemberg revisar)
Resultado: Melhoria contínua proposta (para revisão humana)

Passo 8b: Registro no Livro-Razão
Arquivo: 01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md
SE houve execução real nesta rodada (Passo 5, 6, 7):
├─ Uma entrada por Gestor com execução real
├─ Modelo:
│  ├─ Data
│  ├─ Gestor
│  ├─ O que decidiu
│  ├─ Por quê
│  ├─ O que foi criado/alterado
│  ├─ Backup feito
│  └─ Como desfazer
│
└─ Gere PDF gêmeo do arquivo .md (exceto arquivos de estado)
SE item de pendencias.json foi resolvido:
├─ Edite arquivo: Status → "resolvida"
├─ Campo: resolvido_em → AAAA-MM-DD (hoje)
└─ Não apague (é histórico)
Resultado: Rastreabilidade completa

Passo 8c: Atualização do Painel Fundador
Arquivo: 01_CEO/Painel_Fundador/painel_fundador_sttk.html
SE houve execução real nesta rodada:
1. Leia livro-razão do mês (decisões de hoje)
2. Para cada decisão ainda não no FEED:
   ├─ Prependa objeto ABAIXO DE FEED-AUTO (mais recente no topo)
   ├─ Formato:
   │  {d:"DD/MM",
   │   et:"TIPO",
   │   t:"título curto",
   │   who:"quem fez",
   │   p:"uma frase do que aconteceu"}
   │
   └─ Tipos válidos: decisao, promocao, agente, skill, sistema, correcao, marco, capacidade
3. Atualize data:
   └─ <span class="updated">DD/MM/AAAA</span>
4. Se card mudou estado:
   └─ Atualize aquele card (chip, data-state, pg, sum)
   └─ Não mexa em outros cards
5. Republique:
   └─ Artifact: file_path = arquivo HTML
   └─ url = (URL existente — MESMO LINK)
6. Registre no livro-razão:
   └─ "Atualizou Painel: [o quê]"
SE nada aconteceu hoje:
└─ Não republique nem registre (Princípio 15)
Resultado: Painel sincronizado, feed atualizado

FASE 8: VIGILÂNCIA & RESUMO FINAL

Passo 9: Autoescalonamento (Detecta Estagnação)
Após Passos 1-8, confira cada Gestor:
SE SEM execução real NEM varredura real nesta rodada:
└─ Sinalize: "SEM PROGRESSO ESTA RODADA: {Gestor}"
└─ Registre no estado dele
SE padrão de estagnação (N rodadas consecutivas):
├─ Confira: _estado_wallenberg.md (histórico de rodadas)
├─ Se padrão confirmado → Sinalize forte:
│  "PADRÃO ESTAGNAÇÃO: {Gestor} há N rodadas consecutivas"
└─ Escalona para Claudemberg (necessita revisão humana)
Resultado: Bloqueios reais surfaciam, escalona quando necessário

Passo 10: Resumo Final
Para CADA Gestor processado, escreva 2-4 linhas:
├─ O que encontrou
├─ O que resolveu sozinho (quantos itens "auto" de pendencias.json)
├─ Se acionou Agente da equipe (por quê)
└─ O que registrou no livro-razão
SE Gestor não tinha nada:
└─ Uma linha, siga para próximo (não preencha por preencher)
FECHAMENTO — Métricas totais:
├─ Quantos Gestores passaram (ex: 3 Gestores)
├─ Quantos tiveram execução real (ex: 2 com execução)
├─ Quantos itens pendencias.json foram fechados (ex: 5 itens)
├─ Quantas melhorias Learning Agent propôs (ex: 2 técnicas)
├─ Tempo total (08:00–11:30 = 210 min)
└─ Status geral: SUCESSO / COM RESSALVAS / BLOQUEADO
Resultado: Visibilidade completa, pronto para Claudemberg validar
```

---

## F. AUTOMAÇÃO

```
✅ Agendador: 10:15 toda manhã (seg-sex)
   └─ Dispara Drenagem Contínua (após Rotina Diária Skills)
   └─ 1h de intervalo (Diária acaba ~09:15, Drenagem começa 10:15)
   └─ Sem interferência humana

✅ CronJob PDF: 20:00 toda noite
   └─ Gera PDFs: SKILL.md (se Learning Agent propôs melhoria)
   └─ Gera PDFs: Livro-razão (backup)
   └─ Sem ação necessária
```

**Implementado de fato (28/08/2026):** tarefa `wallenberg-drenagem-continua` registrada em `mcp scheduled-tasks`, cron `15 10 * * 1-5`, `enabled: true`. Esta é a peça que faltava na versão anterior (v2.3 original) — o arquivo existia, mas nunca virou tarefa ativa.

---

## G. PERMISSÕES NECESSÁRIAS

```
✅ Agent — Acionar Gestores (Kelsen, Lúcio, Cardozo, Fechamento)
✅ Read/Write — Editar pendencias.json, arquivo de estado, livro-razão
✅ Glob — Descobrir Gestores dinamicamente (.claude/agents/*.md)
✅ Notion API — Consultar "Treinos e Testes" (collection://...)
✅ Artifact — Republice Painel Fundador
```

---

## H. INTEGRAÇÃO COM ROTINA DIÁRIA SKILLS

```
FLUXO DIÁRIO:

08:00 ────→ Wallenberg Rotina Diária Skills
            ├─ Cria 1-3 Skills (Status: "proposta")
            └─ Fim: ~09:15

[Intervalo 1 hora]

10:15 ────→ Wallenberg Drenagem Continua
            ├─ Lê Skills criadas
            ├─ Implementa (se Autonomous)
            ├─ Cria Gestores faltantes
            ├─ Testa + Valida
            └─ Fim: ~11:30

[Intervalo]

20:00 ────→ CronJob PDF (ambas as rotinas)

PRÓXIMO DIA: Repete
```

---

## I. SAÍDA ESPERADA (Relatório)

```
Formato ao fim da execução:

✅ EXECUÇÃO COMPLETA — Wallenberg Drenagem Continua v2.3
⏱️  Início: 10:15 | Fim: 11:30 | Duração: 75 min

📊 RESULTADO POR GESTOR:

🔹 Kelsen (Legal):
   • Pendências lidas: 2 abertas, 1 resolvida
   • Itens "auto" fechados: 1 (Skill "LICIN 2.0 Atualizado" aprovada)
   • Acionou: Hely (Agente de Projeto Legal)
   • Registrado em livro-razão: Resolução de legislação CAU-RJ

🔹 Lúcio (Arquitetura):
   • Sem pendências abertas
   • Varredura realizada: Verificou POP desatualizado
   • Encontrou melhoria: Atualizou template de Estudo Preliminar
   • Registrado em livro-razão: Melhoria interna (POP v2.0)

🔹 Cardozo (Complementares):
   • Nível: Formação (aguardando Autonomous)
   • Skill "MCP Render" pronta, mas aguardando nível
   • Status: "pronta, aguardando Autonomous"

─────────────────────────────────────
📊 MÉTRICAS TOTAIS:
   • Gestores processados: 3
   • Com execução real: 2
   • Itens pendencias.json fechados: 1
   • Melhorias Learning Agent propôs: 2 (caching em Passo 1, reconciliação paralela)
   • Skills implantadas (Autonomous): 0 (nenhum Gestor em Autonomous ainda)

🚀 Próxima Execução: Amanhã 10:15
   (Será atualizado conforme Gestores atingem Autonomous)

✅ Status Geral: SUCESSO
```

---

## HISTÓRICO DE VERSÕES

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0–2.2 | 27/07 a 25/08/2026 | Ver histórico completo nos backups datados de `01_CEO/Decisoes_Autonomas/_backups/` |
| 2.3 | 25/08/2026 | Divisão final Passo 8 = implantação. Nunca chegou a ficar registrada como tarefa ativa em `scheduled-tasks` (wrapper órfão) — apagada em 28/08/2026 por esse motivo. |
| 2.3 (recriação, 1ª tentativa) | 28/08/2026 | Recriada fundida com o `PLAYBOOK_ROTINAS_AUTOMATICAS.md` — **revertida a pedido de Claudemberg** ("você recriou o que já existia não as novas mudanças que eu pedi"). |
| 2.3 (recriação, 2ª tentativa) | 28/08/2026 | Reescrita em markdown limpo (headers, bullets) em vez do texto exato — **também revertida** a pedido de Claudemberg ("apague o que acabou de criar e recrie como eu mandei"). |
| 2.3 (recriação, 3ª tentativa — esta) | 28/08/2026 | Seções B e C (Descrição e Instruções) **copiadas integralmente**, formatação ASCII original preservada em blocos de código, sem reescrita. Seções A, D-I também no formato original. Tarefa registrada em `scheduled-tasks` (ver Seção F). |

---

**Última atualização:** 28/08/2026
**Status:** ✅ Operacional — registrada em `scheduled-tasks` (cron `15 10 * * 1-5`)
**Próximo:** Primeira rodada agendada real, 10:15 do próximo dia útil
