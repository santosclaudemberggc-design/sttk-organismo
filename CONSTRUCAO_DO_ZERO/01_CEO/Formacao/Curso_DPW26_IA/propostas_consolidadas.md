# Curso DPW26 — propostas consolidadas para Claudemberg aprovar

As 3 aulas geraram 29 propostas (A a AC, ver `aula1`, `aula2`, `aula3`). Muitas eram a mesma ideia vinda de
professores diferentes. Juntei em **9**, por ordem de valor. Nada foi aplicado.

| # | Proposta | O que muda na prática | Junta | Dono | Esforço |
|---|---|---|---|---|---|
| 1 | **Modelo único de parecer** | Todo parecer de Gestor termina com: recomendação · dono · prazo · métrica · premissas que derrubam o plano (com evidência) · o que a IA fez · o sinal que faria voltar atrás · **tem volta ou não?** | E, J, L | Gestores | Médio |
| 2 | **Contraprova antes da defesa** | Antes de fechar parecer, pedir "o que invalidaria isso?" e, em decisão sem volta, um pré-mortem ("deu errado em 12 meses, por quê?") | F, K, M | Bardi, Kelsen, Villaça, Lúcio | Baixo |
| 3 | **Decisão sem volta marcada** | Liberação de Obra, protocolo LICIN e partido aprovado pelo cliente chegam a Claudemberg com a ficha do item 1 e rigor extra | J | Wallenberg, Lelé, Artigas | Baixo |
| 4 | **Nada falta em silêncio** | Regra para todos: informação ausente vira "a confirmar"; todo número tem fonte, data-base e regra de cálculo | G, I, N | Todos | Baixo |
| 5 | **Evals em toda mudança** | Alterou Skill ou prompt de agente → roda as 3 avaliações da pasta `evals/` antes de valer; palavra-canário nos testes para provar leitura completa | V, U | Bardi, Drenagem | Médio |
| 6 | **Descrições e critérios** | Auditar Skills sem descrição/gatilho (várias vazias) e agentes sem critérios de aceite explícitos | A, B | Drenagem | Médio |
| 7 | **Revit: catálogo e fundação** | Oscar só usa tipos do catálogo do template; níveis, eixos e tipos antes de paredes; um pedaço por vez | W, X | Oscar, Lúcio | Médio |
| 8 | **Cliente: conhecimento tácito + transcrição** | Reunião com cliente transcrita e guardada no caso; campo "na visão de Claudemberg" no Briefing | T, Y | Lúcio, Kelsen | Baixo |
| 9 | **Apresentação ao cliente** | Design system STTK no Claude Design; revisão final "como o cliente leigo leria isto" | P, Q | Portinari, Mindlin | Médio |

**Ficaram de fora** (pequenos ou já cobertos): C alertas no topo, D minuto quebrado, H eventos no gráfico,
O ata padrão, R/Z modelo por agente, S sabatina × CLARO, AA teste de página, AB skill de terceiro,
AC um assunto por chat. Podem entrar depois, um a um.

**Aplicadas em 02/11/2026 (sabatina aceita por Claudemberg):** 4 e 2 — `CLAUDE_agente_slice.md`,
`CLAUDE_gestor_slice.md` e isca de lacuna em `.claude/agents/bardi.md`. Teste: próximo caso do Ensaio.
**Aplicadas em 02/11/2026:** 1 e 3 — `01_CEO/Padroes_Documentos/MODELO_PARECER_FICHA_DECISAO.md`, apontado no
`CLAUDE_gestor_slice.md`; recusa no `.claude/agents/artigas.md`. Métrica só em Viabilidade e Orçamento.

**Sugestão de ordem:** 4 e 2 primeiro (baixo esforço, evitam erro já visto), depois 1 e 3 juntos (um modelo
só), depois 5 e 6 (dão base para medir o resto). 7, 8 e 9 quando houver caso real para testar.
