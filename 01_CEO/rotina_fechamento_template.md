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
