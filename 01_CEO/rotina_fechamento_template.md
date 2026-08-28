---
name: rotina-fechamento-template
description: "Template de Fechamento de Rotina — preenchido ao fim de cada rodada, lido no início da próxima"
metadata:
  type: operacional
  lido_por: wallenberg-rotina-diaria-skills-v2, wallenberg-drenagem-continua-v2
  escrito_por: ambas rotinas
  frequencia: toda rodada (Diária: daily, Drenagem: 3x/semana)
---

# Fechamento de Rotina — Template Reutilizável

**Leia isto ao INÍCIO de cada rodada para saber:**
- O que foi feito na rodada anterior
- O que ficou pendente
- O que não fazer (evitar retrabalho)

**Preencha isto ao FIM de cada rodada para que a próxima saiba:**
- O que foi entregue
- O que ficou bloqueado e por quê
- O que tomar cuidado

---

## [DATA-RODADA] — Diária Skills / Drenagem

### RODADA ANTERIOR (O que foi entregue)

- [ ] **Skills criadas:** [listar nomes + versão (v1, v2, etc.)]
- [ ] **Skills documentadas:** [listar paths]
- [ ] **PDFs regenerados:** [listar quantos]
- [ ] **Painel atualizado:** Sim/Não (se sim, que eventos adicionados?)
- [ ] **Livro-razão registrado:** Sim/Não
- [ ] **Learning Agent propôs melhorias:** [listar quantas + resumo]

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Item bloqueador 1:** [descrição] → **Ação:** [o que fazer]
- **Item bloqueador 2:** [descrição] → **Ação:** [o que fazer]
- *Se não houver bloqueadores, deixar vazio*

### O QUE NÃO FAZER (Avoid retrabalho)

- ❌ **Skill X não crie novamente** — já existe em `Skills_Propostas/2026/Agosto/`
- ❌ **Evento Y não adicione ao Painel** — redundante com evento Z de ontem
- ❌ **Reunião Z não agende** — já agendada para 25/08 (terça-feira)
- *Se não houver retrabalho a evitar, deixar vazio*

---

## ESTA RODADA (Preencher ao terminar)

### Entregáveis

- [ ] **Skills criadas:** [nomes + v#]
- [ ] **Skills documentadas:** [paths]
- [ ] **PDFs regenerados:** [quantos]
- [ ] **Painel atualizado:** Sim/Não (descrever mudanças)
- [ ] **Livro-razão registrado:** Sim/Não (data entry)
- [ ] **Learning Agent melhorias:** [quantas + resumo]

### Bloqueadores (se houver)

- **Bloqueador 1:** [descrição clara]
  - Causa: [por quê trava]
  - Impacto: [o que não conseguiu fazer]
  - Próximo passo: [quem resolve, quando]

- **Bloqueador 2:** [descrição clara]

*Se nenhum bloqueador, escrever: "Sem bloqueadores esta rodada"*

### Retrabalho Evitado (se houver)

- **Item 1:** Skill X não recriada (já existe v2 de 20/08)
- **Item 2:** Evento Y não adicionado (redundante)

*Se nenhum retrabalho evitado, deixar vazio*

### Status Final

- **Rodada:** ✅ Completa / ⚠️ Parcial (se parcial, descrever)
- **Taxa de Sucesso:** [X de Y itens planejados entregues]
- **Próxima Rodada Recomendação:** [2-3 itens prioritários baseado em bloqueadores]

---

## HISTÓRICO DE RODADAS

*Apenas os últimos 2-3 encerramentos para referência rápida*

### [2026-08-28] Diária Skills v2.7 — 2 rodadas

- ✅ Entregou: **5 Skills novas** (Baumgart/NBR6118, Saturnino/NBR5626-8160, Landell/NBR5410, Glaziou/NBR16636-4, Portinari/Presenton), 9 PDFs (5 Skills + 4 índices atualizados), índice com 5 novas linhas + observações das 2 rodadas, livro-razão registrado, `_estado_cardozo.md` atualizado
- ⚠️ Bloqueadores: (1) **Painel Fundador não publicado** — v2.7 move Painel para Sexta-feira. HTML local tem o evento 28/08 (Trilha A estreia) pronto em `01_CEO/Painel_Fundador/painel_fundador_sttk.html`. Publicar na Sexta 01/09 via Artifact com url `https://claude.ai/code/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27` (fazer WebFetch no artifact antes de publicar — regra AULA CLAUDE).
- ❌ Retrabalho evitado: (1) FreeCAD MCP e Revit MCP Study (27/08) não recriados; (2) PPTAgent (26/08) não duplicado — Presenton é ferramenta diferente (MCP nativo vs CLI)
- 🎯 Status: **Completa** — 5 Skills (4 Trilha A + 1 Trilha B), 4 áreas Cardozo cobertas. Pendentes sem Skill Trilha A ainda: Tenreiro (Interiores) e Mindlin (Apresentação). Painel publicar Sexta.

### [2026-08-27] Diária Skills v2.4

- ✅ Entregou: 2 Skills novas (FreeCAD MCP para Baumgart, Revit MCP Study 173 tools para Oscar), 2 PDFs, índice atualizado
- ⚠️ Bloqueadores: (1) **CRÍTICO** — descoberta de divergência entre Painel publicado (ao vivo, 12/08) e cópia local do repositório (selo "15/08" mas faltando ~2 semanas de eventos reais). Cópia local RECONCILIADA com sucesso (histórico completo restaurado + evento Cardozo/26-08 adicionado), mas a **republicação via Artifact falhou 3x** com erro "identical content already refused... resent unchanged" — aparente falso positivo da ferramenta, não resolvido. Arquivo local está correto e pronto; o link ao vivo segue desatualizado até alguém retentar publish.
- ❌ Retrabalho: Nenhum
- 🎯 Status: Parcial — Passos 1-5 e 8 completos; Passo 6 com correção pronta mas publicação bloqueada; Passo 7 sem achado novo

### [2026-08-26] Drenagem Contínua

- ✅ Entregou: 3 Gestores drenados (Kelsen/Lúcio/Cardozo); equipe Cardozo formalizada (Baumgart, Landell, Saturnino, Glaziou, Tenreiro, Mindlin — 6 agentes, `.md` criados); Resolução SMDU Nº 10/2026 catalogada em `_indice_fontes.md`; livro-razão e estados atualizados
- ⚠️ Bloqueadores: (1) b14 aguarda resposta SMDU — verificar email santosclaudembergg@hotmail.com; (2) PPTAgent implantação requer `pip install pptagent` por Wallenberg antes de 28/08; (3) Painel não atualizado (Cardozo + 6 agentes ausentes — deixar para próxima sessão); (4) WAN 2.2 Burle — report esperado amanhã 27/08; (5) Decisão pendente: sobreposição Revit MCP 138 tools vs. Vitruvius; (6) 2 Skills BIM de Cardozo aguardam decisão de incorporação no CLAUDE.md
- ❌ Retrabalho: Nenhum
- 🎯 Status: Parcial — Passos 1-5 e 7 completos; Passo 6 (Painel) adiado; Passo 8 (PPTAgent) parcial (proposta verificada, implantação bloqueada)

### [2026-08-26] Diária Skills v2.4

- ✅ Entregou: 2 Skills (Resolução SMDU Nº 10/2026 RDT + PPTAgent para Portinari), 8 PDFs (2 novos + 6 retroativos de 23-24/08), índice retroativo com 6 linhas de 23-24/08
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho: Nenhum evitado
- 🎯 Status: Completa (8 passos)

### [2026-08-21] Diária Skills

- ✅ Entregou: 2 Skills novas (Learning Agent Fase 2 + Architecture MCP), 3 PDFs
- ⚠️ Bloqueadores: Nenhum
- ❌ Retrabalho: Nenhum evitado
- 🎯 Status: Completa (7 de 7 passos)

---

## INSTRUÇÕES DE USO

1. **Ao INICIAR rodada:** Leia "RODADA ANTERIOR" + "O QUE FICOU PENDENTE" + "O QUE NÃO FAZER"
2. **AO TERMINAR rodada:** Preencha "ESTA RODADA" (todos os campos)
3. **Ao formatar:** Mova "ESTA RODADA" para "HISTÓRICO" (após 48h de fechamento)
4. **Cada rodada lê isto:** para não repetir trabalho

---

**Última atualização:** [data da última rodada]  
**Próxima leitura:** [data da próxima rodada]
