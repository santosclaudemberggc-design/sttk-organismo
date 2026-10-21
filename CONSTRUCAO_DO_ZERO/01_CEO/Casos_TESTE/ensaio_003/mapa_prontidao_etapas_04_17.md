# Mapa de prontidão — Ensaio 003, etapas 4 a 17

> Wallenberg, 09/10/2026 (análise do organismo, aprovada por Claudemberg). **Não é execução do ensaio** e não abre gabarito: é a conferência, antes de cada etapa chegar, de se a equipe dona **tem a ferramenta** para entregar o que a etapa pede. Fonte: `tools:` de cada `.claude/agents/*.md`, `Inventario_Capacidade/inventario_capacidade_sttk.md`, `D:\011_VITRUVIUS\STATUS_PROJETO.md`, estados dos agentes. Rotina Ensaio Sombra (Bardi) relê esta tabela antes de montar cada etapa.

Legenda: 🟢 a equipe tem o que precisa · 🟡 entrega em texto/memorial, sem o desenho ou o cálculo assinado que um caso real exige · 🔴 trava por falta de ferramenta ou de equipe.

| # | Etapa | Dono → Agentes | Prontidão | O que falta (e quem destrava) |
|---|---|---|---|---|
| 4 | Briefing | Lúcio → Oscar | 🟢 | Etapa de texto/programa. Sem trava de ferramenta. |
| 5 | Estudo Preliminar | Lúcio → Oscar, Burle, Portinari | 🔴 | **Oscar não tem nenhuma tool do Vitruvius que funcione**: o `tools:` dele usa nomes antigos (`mcp__vitruvius__create_wall`), e o servidor expõe `mcp__vitruvius__vitruvius_create_wall`; 10 nomes da lista nem existem mais. **Burle**: `generate_image`/`generate_video` (Higgsfield) pausado por orçamento e sem as tools de envio de imagem-base. Destrava: Plano Vitruvius (Fase 0) + decisão de orçamento do render (Claudemberg). Sem isso, a etapa sai só em texto, como no Ensaio 002. |
| 6 | Anteprojeto | Lúcio → Oscar, Burle, Portinari | 🔴 | Mesmo bloqueio da 5, mais: pranchas, cortes, quadro de áreas a partir do modelo — dependem das Fases 1–2 do Plano Vitruvius. |
| 7 | Legal — entrada (simulada) | Kelsen → Hely | 🟡 | Hely sem WebFetch/WebSearch (pedido parado desde 01/10, edição negada pela permissão automática — Claudemberg aplica a linha). `gerar_prancha_legal.py` existe e funciona; o quadro de áreas depende do Anteprojeto. |
| 8 | Estrutural | Cardozo → Baumgart | 🟡 | Baumgart só tem Read/Write/Edit/Glob/Grep/Skill: entrega memorial e pré-dimensionamento em texto, sem software de cálculo. Num caso real o cálculo com ART é de engenheiro (Skill `legal-art-crea…`). Ensaio deve cobrar: o que o Agente prepara para o calculista e o que ele **não** pode assinar. |
| 9 | Hidrossanitário | Cardozo → Saturnino | 🟡 | Idem: memorial e dimensionamento por norma em texto; sem desenho. |
| 10 | Elétrico | Cardozo → Landell | 🟡 | Idem. |
| 11 | Interiores | Cardozo → Tenreiro | 🟡 | Produz especificação; imagens dependem de Burle (bloqueado). |
| 12 | Paisagismo | Cardozo → Glaziou | 🟡 | Idem. |
| 13 | Automação | Cardozo → Landell | 🟡 | Idem. |
| 14 | Compatibilização | Lelé → Zanettini | 🟡 | **[15/10/2026]** Zanettini em Shadow (EXAME-ZAN-02). Compatibilização em texto e PDF: sem modelo BIM, sem clash detection; complementares sem acesso ao Vitruvius (pendência de Claudemberg e Cardozo). |
| 15 | Projeto Executivo | Lelé → Reidy | 🟡 | **[15/10/2026]** Reidy em Shadow (EXAME-REI-02, 9,18). Compila e confere em texto; escrita de documentação no Vitruvius pendente de decisão de Claudemberg. |
| 16 | Orçamento Executivo | Lelé → Limmer | 🟡 | **[15/10/2026]** Limmer em Shadow (EXAME-LIM-02, 10,00). Skill `orcamento-executivo-analitico-sinapi-rj` v1.0 (ativa-com-ressalva). Consulta SINAPI depende de Wallenberg (terminal). |
| 17 | Liberação de Obra (Gate 16) | Lelé + Wallenberg | 🟡 | Etapa de decisão; trava se a 14–16 não existirem. |

## O que isso significa para o ensaio

1. **Etapa 4 pode seguir normalmente** (amanhã, pelo fluxo de sempre).
2. **Antes da etapa 5 chegar**, Claudemberg decide uma de duas: (a) segurar a etapa 5 até a Fase 3 do `D:\011_VITRUVIUS\PLANO_AGENTE_GUIADO.md` (exame de ferramenta do Oscar; estimativa 7–8 sessões do Vitruvius); ou (b) rodar a 5 em texto e marcar no parecer "desenho pendente — Vitruvius", como no Ensaio 002. Recomendação de Wallenberg: **(a)**. Rodar em texto não treina o que o Oscar vai precisar fazer num cliente real. Enquanto o Vitruvius avança, a etapa 4 (Briefing) roda normalmente.

**Decidido por Claudemberg em 19/10/2026: opção (a), segurar a etapa 5 até a Fase 3 passar.** Em 19/10 o teste de fumaça da Fase 0 passou (Oscar acionado pelo Lúcio: criar, ler e apagar um nível de teste no Projeto1, 6 de 6 passos). Falta a Fase 3 (exame de desenho). Lembrete: o Burle segue sem render (orçamento pausado), então a etapa 5 pode sair com a parte de imagem pendente mesmo depois da Fase 3.

**Decidido por Claudemberg em 20/10/2026: Fase 3 aprovada (8,75) e trava v3 da etapa 5 liberada.** Modelo: etapa_05_estudo_preliminar/entrega_v3/EP_v3.rvt (volumetria E). Parecer: parecer_bardi_v3_correcao.md.
3. **Antes da etapa 14**, Lelé precisa ter equipe. Pendência aberta para o Lelé propor (Regra de Cascata).
4. **Etapas 8–13** podem rodar como estão, desde que o enunciado do Bardi deixe claro o limite: o Agente prepara, o profissional habilitado assina.
