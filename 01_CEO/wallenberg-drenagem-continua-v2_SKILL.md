---
name: wallenberg-drenagem-continua-v2-3
version: 2.4.0
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

✅ Passo 2.5: PORTÃO DE TRABALHO — Validar se fila tem conteúdo
   ├─ Verifica: `pendencias.json` tem itens com alc:"auto" abertos?
   ├─ Verifica: `Skills_Propostas/2026/{mês}/` tem .md/proposta?
   ├─ Verifica: Notion "Treinos e Testes" tem Status="pendente"?
   │
   ├─ SE TUDO VAZIO (fila = 0):
   │  └─ Registra: "Portão validado: fila vazia em {data} {hora}"
   │  └─ **ENCERRA AQUI** — Não abre Gestor nenhum (economia de tokens)
   │  └─ Status geral: "Drenagem Contínua: rodada completada (fila vazia)"
   │
   └─ SE FILA TEM CONTEÚDO (alc:auto + skills + notion > 0):
      └─ Prossiga para Passo 3 (abre Gestores com fila real)

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
   
   1. PESQUISE VÍDEOS: **[AMPLIADO 03/09/2026, Claudemberg — não fica preso a poucas contas nem só YouTube]**
      ├─ YouTube: "Autonomous agents workflow", "Multi-agent systems", "Claude AI" — busca ampla, sem lista fixa de canal
      ├─ Instagram/Facebook (Meta), busca ampla — sem lista fixa de perfil, deixe a busca achar quem está relevante agora
      ├─ Outras plataformas de vídeo além do YouTube (ex.: Vimeo, canais técnicos que hospedam vídeo fora do YouTube) que gerem conteúdo sobre "Autonomous agents workflow", "Multi-agent systems", "Claude AI"
      ├─ WebSearch: "automação delegação", "otimização rotinas", "IA arquitetura"
      ├─ Assista de verdade via `/watch:watch` — vídeo longo: transcreva; reel/curto: leia comentários também
      └─ Localize: 3-5 fontes alta qualidade (views, data recente, confiável) — mais se a rodada justificar
   
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
Fontes paralelas: **[AMPLIADO 03/09/2026, Claudemberg — não fica preso a poucas contas nem só YouTube]**
├─ YouTube: "Autonomous agents", "Claude AI", vídeos longos (transcrever via /watch:watch) — busca ampla, sem canal fixo
├─ Instagram/Facebook (Meta) — busca ampla, sem lista fixa de perfil
├─ Outras plataformas de vídeo além do YouTube que gerem esse tipo de conteúdo
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

## J. ADENDOS OPERACIONAIS (instruções de Claudemberg — não alteram as seções B/C, que são cópia integral)

**J.1 — Skill do tipo Ferramenta: validação obrigatória, não opcional (31/08/2026).**
Quando a rotina `wallenberg-rotina-diaria-skills` criar Skill do tipo **Ferramenta/Tool**, esta rotina (Passo 6) NÃO só verifica se o Gestor está Autonomous — ela **analisa, cria/conecta, testa tecnicamente e valida se a ferramenta é realmente útil dentro do organismo STTK** antes de considerar a Skill "implantada". "Pronta, aguardando Autonomous" só vale para a etapa de aplicar à equipe; a validação técnica da ferramenta em si acontece assim que a Skill chega.

**J.2 — Cadeia CEO -> Gestor -> Agente não pode travar (31/08/2026).**
Gestor sem Agente acionável, exame de nível represado, ou "aguardando Autonomous" NÃO são motivo para a cadeia parar. Se um Gestor está abaixo de Autonomous e isso bloqueia o treino da equipe dele, Wallenberg desenha e administra os exames de nível do próprio Gestor na mesma janela (Exame 2/3), e então o Gestor treina a equipe até o nível máximo. Exame represado é pendência real a resolver na rodada, não item a só sinalizar.

**J.3 — Varredura de documentos no Drive "Dptº de Projetos" (31/08/2026) — passo recorrente.**
A cada rodada (ou a cada N rodadas, a critério de Wallenberg), cada Gestor acionado verifica, na pasta compartilhada do Google Drive **"Dptº de Projetos"**, os documentos da **própria área** — atualização, completude, terminologia vigente (LICIN 2.0 / Decreto 55.622/2025, sem termos pré-LICIN soltos). É levantamento de leitura; correção segue o fluxo normal de pendência.
- **Documento que pertence a mais de um Gestor** (ex.: a planilha canônica de entregáveis com abas de todas as disciplinas): o Gestor apenas **lista e sinaliza**; **quem audita é o CEO Wallenberg**.
- **Padronização de documentos entre Gestores**: também é auditoria de Wallenberg, não de Gestor isolado (conecta com a função de padronização cross-departamento de 08/08/2026).

**J.4 — Sincronização 14/09/2026: 2 decisões que só existiam na tarefa agendada, nunca chegaram a este arquivo-fonte.**
Achado de Claudemberg (mesmo dia da correção da Rotina Diária Skills v3.0): este arquivo é citado pela tarefa agendada `wallenberg-drenagem-continua-local` como "arquivo-fonte completo", mas duas decisões reais de Claudemberg, já aplicadas na tarefa agendada, nunca tinham sido sincronizadas de volta aqui. Sem esta sincronização, quem consultasse este arquivo por dúvida reintroduziria comportamento já descartado por custo. Registrando as duas agora:

- **Portão de Trabalho — Opção B / Alvo A (02/09/2026).** O Passo 2.5 (seção C/E acima) descreve a versão simples original ("se fila tem conteúdo, prossiga para todos"). **Isso está superado.** A regra real, em vigor desde 02/09/2026: (1) Skill em `Skills_Propostas` com Status "proposta" só entra na contagem da fila se **ainda não foi avaliada** por rodada anterior — Skill já avaliada e parada em "aguardando ratificação de Claudemberg" NÃO conta, ela só volta na Reunião Semanal/Mensal; (2) mesmo com fila não-vazia, a Fase 4 (Passo 5) aciona **SOMENTE os Gestores com item real na própria fila** (auto_abertas dele, OU skill nova endereçada a ele, OU Notion pendente dele) — Gestor sem nada na fila não é aberto, registra "sem fila, não acionado". Motivo: abrir os 3 Gestores só para ouvir "nada a fazer" queimava ~90k tokens/rodada; no plano Pro isso batia no teto semanal e travava o organismo.

- **Learning Agent só roda às segundas + execução real (Item 4, 08/09/2026).** O Passo 8a (seção C/E acima) descreve pesquisa de vídeo incondicional a cada rodada. **Isso está superado.** Regra real desde 08/09/2026: o Passo 8a só executa **SE hoje é segunda-feira E houve execução real nesta rodada** (Gestor fechou item, Agente produziu, ou skill implantada). Fora disso, pule o 8a inteiro — não pesquise vídeo, não transcreva. Motivo: a busca diária de vídeo queimava cota do plano Pro e vinha rendendo ~zero mudança real ao SKILL.md.

- **Passo 7.5 — Varredura Mensal de Documentos no Drive (Item 4, 08/09/2026) — só na 1ª rodada útil do mês.** Este é um passo inteiro que existe na tarefa agendada mas não tinha entrado aqui (é mais específico que o J.3 acima, que é de 31/08 e fala em "Dptº de Projetos" genérico). Para CADA Gestor acionado na rodada, na 1ª rodada útil do mês: peça varredura dos documentos dele no Drive (Kelsen: POPs de Legal + base legislativa; Lúcio: POP-PROJ + templates de Arquitetura; Cardozo: os 6 POPs de disciplina). Use o conector MCP de Drive (search_files/get_file_metadata/read_file_content). **Autônomo** (backup do "antes" + livro-razão + "como desfazer"): sinaliza base desatualizada/erro factual/contradição/duplicata/arquivo de teste em pasta oficial; corrige (update_file) referência a lei revogada, nº de norma errado, link quebrado, cabeçalho desatualizado; exclui/resolve duplicata (trash_file — confirmado em teste real 08/09 que o MCP cria, edita e trasheia arquivo existente); cria documento que falte (create_file). **Não-autônomo** — só sinaliza para Claudemberg: reescrever documento canônico por julgamento (reordenar seções, reinterpretar conteúdo). Nas demais rodadas do mês, pule este passo. Registre no `_estado` de cada Gestor o que foi varrido; se nada precisou mudar, registre "sem correção necessária" (a obrigação é varrer, não achar).

**Como desfazer:** reverter esta seção J.4 via git revert. Não afeta as seções B/C (permanecem cópia integral de 28/08, como protocolo já estabelecido).

**J.5 — v2.4 (16/09/2026): checagem cruzada, filtro geográfico e log estruturado — mesclados, não sobrescritos.**
Pedido original era "sobrescrever integralmente" a tarefa agendada e este arquivo com um pipeline novo. Antes de executar, confirmado que a v2.3 (seções B/C acima + adendos J.1-J.4) tem mecanismo real e testado que o texto do pedido não mencionava (Portão de Trabalho, hierarquia de criação de Gestor, gate de Autonomous, autoescalonamento, fronteira crítica) — sobrescrever teria apagado tudo isso. Decisão de Claudemberg: **mesclar**. As 4 adições entraram na tarefa agendada (`wallenberg-drenagem-continua-local`, fonte operativa real) dentro do esqueleto de 8 fases/10 passos da v2.3, sem remover nada:

- **Filtro geográfico (Passo 2).** Fonte da verdade: `INDICE_PRIORIDADES.md` (raiz). Foco vigente: Barra da Tijuca e Recreio dos Bandeirantes. Item sem dimensão geográfica (a maioria dos itens de Skill/pendência do organismo, ex. Painel, Learning Agent, exame de nível) **não é descartado** — só item claramente identificado como de fora do RJ é sinalizado "Brecha de Escopo". Ajuste feito no pedido original: o texto pedia descarte sumário de "qualquer dado de outros bairros/cidades", o que na prática descartaria quase tudo — a maioria dos itens do organismo não tem dimensão geográfica nenhuma.
- **Mecanismo antifrail de refação (Passo 5.b.1).** Teste do Notion com ID que não bate com o Gestor/Agente que vai executá-lo é invalidado (`Status: INVALIDADO_REFAZER`), nunca conta como progresso, e o desvio de atribuição vira entrada "Desvio de Governança" no livro-razão. Corrigido no mesmo passo: o pedido original descrevia Gestores como "treinados e homologados diretamente pelo CEO (Claudemberg)" — Claudemberg não é o CEO do organismo (é Wallenberg, em todo outro arquivo do sistema); exame de Gestor é administrado por Wallenberg com Claudemberg presente/ratificando na Semanal, e exame de Agente pelo próprio Gestor da célula.
- **Staging de MCP antes de implantar (Passo 6.3).** Nunca escreve `~/.claude/settings.json` autonomamente. Se a Skill de ferramenta exigir MCP novo, monta o fragmento JSON em `01_CEO/Painel_Fundador/staging_mcp.json` e para, aguardando validação manual de Claudemberg — gate novo, adicional ao gate de Autonomous já existente, não substitui.
- **Log estruturado em vez de edição de HTML (Passo 8c).** Desde a migração de 16/09/2026 (Painel lê `feed.jsonl` via `fetch()`), editar `painel_fundador_sttk.html` diretamente virou proibido — Passo 8c reescrito para invocar `Append-STTKLog.ps1` com a assinatura real (`-LogPath -D -Et -T -Who -P` + opcional `-Rec`). Corrigido no mesmo passo: o pedido original descrevia o script fazendo "Exponential Backoff" contra file-lock — o script real (rodada anterior desta mesma sessão) faz retry de intervalo fixo (150ms × 8 tentativas), não backoff exponencial; o texto foi ajustado para descrever o comportamento real, não o pretendido.
- **Auditoria do nó terminal Lelé (Passo 5.f, novo).** Lelé não existia quando a v2.3 foi escrita. Em Formação/Sandbox: só mentoria e julgamento de conflito, proibido despachar subagente até o log de promoção ser assinado por Wallenberg. Diagnóstico e métrica de teste persistem em `01_CEO/Painel_Fundador/auditoria_lele.json` (estático, sobrescrito por rodada — diferente do `feed.jsonl`, que é incremental).

**J.5.1 — Motor de Triagem, algoritmo de 3 travas (16/09/2026, mesmo dia).** O mecanismo antifrail acima ganhou forma final de motor nomeado, aplicado a cada linha consumida da fila Notion "Treinos e Testes" (qualquer Gestor, não só Lelé), na tarefa agendada (Passo 5.b.1):
- **Trava 1 (Geográfica):** só se aplica quando o teste declara localidade explícita. Fora de Barra/Recreio (`INDICE_PRIORIDADES.md`) → `INVALIDADO_REFAZER`, finding "Brecha de Escopo". Teste sem dimensão geográfica não é afetado — ajuste feito na mesma sessão porque a especificação original invalidaria quase todo exame do organismo.
- **Trava 2 (Célula técnica):** é o mecanismo antifrail já descrito acima, agora nomeado formalmente — finding "Desvio de Atribuição Funcional".
- **Trava 3 (Assinatura):** homologação de sucesso em exame de nível de Gestor exige Wallenberg (CEO) revisando com Claudemberg (Founder) presente/ratificando — nunca auto-homologado. Exame de Agente segue a autoridade do próprio Gestor da célula (sem essa exigência extra).

**J.5.2 — Ciclo de vida de `01_CEO/Painel_Fundador/auditoria_lele.json` (schema inicializado 16/09/2026).** Arquivo de persistência estática (sobrescrita por rodada inteira, não incremental) com 3 chaves de topo: `metadados` (versão do pipeline, timestamp real, nível atual do Lelé), `metricas` (total_testes, sucessos, falhas, invalidados, `prontidao_promocao_shadow_pct` = sucessos/total_testes, com teste invalidado contando no denominador e nunca no numerador) e `historico_testes` (lista de casos, cada um com `status: "aprovado"` ou `"INVALIDADO_REFAZER"` + `motivo` + `registrado_como: "Desvio de Governança"` quando barrado). A cada rodada em que Lelé for acionado (Passo 5.f), o arquivo é lido por inteiro, cada linha nova do Notion passa pelo Motor de Triagem (J.5.1), os contadores são recalculados, e o arquivo inteiro é reescrito (não append) em UTF-8 sem BOM, 2 espaços de indentação.

Este arquivo-fonte (seções B/C) **não foi reescrito** para os novos mecanismos — permanece cópia histórica da v2.3, como já era o protocolo desde a 3ª tentativa de recriação (28/08/2026, ver Histórico de Versões). Quem precisar do comportamento real e vigente da v2.4 consulta a tarefa agendada diretamente, ou este adendo J.5.

**J.5.3 — Guarda preemptiva de diretório na criação de Gestor (Passo 4, 16/09/2026).** Mesmo endurecimento SRE já aplicado ao Passo 8c (Painel) e à Rotina Diária (Passo 4, Skills_Propostas): antes de criar `.claude/agents/{gestor}.md` ou `01_CEO/Gestores/{Gestor} ({Tipo})/Agentes/` para um Gestor novo, a tarefa agendada agora dispara `New-Item -ItemType Directory -Force` na árvore de pastas dele — idempotente, previne erro fatal de caminho ausente quando a árvore do Gestor nunca existiu antes (todo Gestor novo, por definição).

**Como desfazer:** reverter esta seção J.5 (incluindo J.5.1/J.5.2/J.5.3) via git revert; reverter a tarefa agendada separadamente (fora do controle de versão deste repositório).

---

## HISTÓRICO DE VERSÕES

| Versão | Data | Mudança |
|--------|------|---------|
| 2.4 (adendo J.5) | 16/09/2026 | **Mesclagem, não substituição.** Filtro geográfico (Barra/Recreio via `INDICE_PRIORIDADES.md`), mecanismo antifrail de refação de teste mal atribuído no Notion, staging de MCP antes de instalar (`staging_mcp.json`), Passo 8c migrado de edição direta de HTML para `Append-STTKLog.ps1`, auditoria do nó terminal Lelé (`auditoria_lele.json`). Pedido original era sobrescrita integral; recusado depois de confirmar que apagaria Portão de Trabalho, hierarquia de Gestor, gate de Autonomous e fronteira crítica — nenhum dos quais estava no texto novo. |
| 2.3 (adendo J.4) | 14/09/2026 | **Sincronização de divergência real** — 2 decisões já aplicadas na tarefa agendada (`wallenberg-drenagem-continua-local`) desde 02/09 e 08/09 nunca tinham chegado a este arquivo-fonte: Portão de Trabalho Opção B/Alvo A (skill já avaliada não conta na fila; só abre Gestor com item real) e Learning Agent restrito a segunda-feira + execução real, além do Passo 7.5 (varredura mensal de Drive) inteiro. Achado por Claudemberg no mesmo dia da correção da Rotina Diária Skills v3.0. |
| 2.3 (adendos J.1–J.3) | 31/08/2026 | Instruções de Claudemberg após a 1ª rodada real: validação obrigatória de Skill-ferramenta; cadeia CEO→Gestor→Agente não trava (Wallenberg destrava exames de Gestor abaixo de Autonomous); varredura recorrente de documentos no Drive "Dptº de Projetos" com auditoria de Wallenberg para docs cross-Gestor e padronização. Seções B/C intactas. |
| 1.0–2.2 | 27/07 a 25/08/2026 | Ver histórico completo nos backups datados de `01_CEO/Decisoes_Autonomas/_backups/` |
| 2.3 | 25/08/2026 | Divisão final Passo 8 = implantação. Nunca chegou a ficar registrada como tarefa ativa em `scheduled-tasks` (wrapper órfão) — apagada em 28/08/2026 por esse motivo. |
| 2.3 (recriação, 1ª tentativa) | 28/08/2026 | Recriada fundida com o `PLAYBOOK_ROTINAS_AUTOMATICAS.md` — **revertida a pedido de Claudemberg** ("você recriou o que já existia não as novas mudanças que eu pedi"). |
| 2.3 (recriação, 2ª tentativa) | 28/08/2026 | Reescrita em markdown limpo (headers, bullets) em vez do texto exato — **também revertida** a pedido de Claudemberg ("apague o que acabou de criar e recrie como eu mandei"). |
| 2.3 (recriação, 3ª tentativa — esta) | 28/08/2026 | Seções B e C (Descrição e Instruções) **copiadas integralmente**, formatação ASCII original preservada em blocos de código, sem reescrita. Seções A, D-I também no formato original. Tarefa registrada em `scheduled-tasks` (ver Seção F). |

---

**Última atualização:** 16/09/2026 (adendo J.5 — v2.4 mesclada na tarefa agendada, ver Histórico de Versões)
**Status:** ✅ Operacional — registrada em `scheduled-tasks` (cron `15 10 * * 1-5`)
**Atenção:** este arquivo é referência de consulta; a tarefa agendada (`C:\Users\santo\.claude\scheduled-tasks\wallenberg-drenagem-continua-local\SKILL.md`) é o que executa de fato. Ao propor melhoria via Learning Agent (Passo 8a), sincronizar os dois lados — não só este arquivo.
