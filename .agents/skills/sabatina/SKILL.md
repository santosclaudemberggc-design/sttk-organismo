---
name: sabatina
description: Entrevista implacável de Wallenberg com Claudemberg para afiar um plano antes de construir qualquer coisa nova no organismo — ferramenta, MCP, app, Skill, Agente, rotina ou mudança de estrutura. Só roda quando Claudemberg chama /sabatina numa conversa ao vivo.
disable-model-invocation: true
---

# Sabatina — entender antes de construir

Adaptada da skill `grill-me`/`grilling` de Matt Pocock (github.com/mattpocock/skills), em 18/10/2026.
Treinada e aprovada por Claudemberg em 18/10/2026, ao vivo, no caso fictício "quadro de áreas gerado no
Revit pelo Oscar" (4 rodadas, 17 perguntas).

**Quem usa:** Wallenberg, em conversa ao vivo com Claudemberg. **Nunca** em rotina agendada nem dentro de
subagente: lá ninguém responde, e uma sabatina sem humano vira a IA concordando consigo mesma.

**Quando usar:** antes de criar ou mudar ferramenta, MCP (ex.: Vitruvius), app (ex.: Sistema de Gestão),
Skill, Agente, rotina ou estrutura. Gestor ou Agente que quiser uma ferramenta nova manda o pedido a
Wallenberg, e Wallenberg leva o pedido para uma sabatina com Claudemberg.

## Como conduzir

1. **Mapear a árvore de decisões.** Liste para você o que precisa ser decidido e o que depende do quê.
   Ex.: "quem usa a ferramenta" vem antes de "que dados ela lê".
2. **Rodadas de perguntas.** Em cada rodada, faça todas as perguntas cujas pré-condições já estão
   resolvidas — no máximo 5 por rodada. Numere. Cada pergunta traz **a sua resposta recomendada**, e é
   escrita de modo que "sim" aceite a recomendação.
3. **Fato você descobre; decisão é de Claudemberg.** O que dá para verificar (o que já existe no
   organismo, o que a ferramenta faz, o que a norma diz) você pesquisa antes de perguntar — nunca pergunte
   a Claudemberg algo que você mesmo pode checar. Vasculhe antes de criar (Princípio 15).
4. **Fonte externa não entra direto.** Se a resposta de Claudemberg trouxer conteúdo de fora (vídeo, site,
   lista genérica), confira contra as Skills do organismo antes de aceitar — termos e regras do Rio
   (LC 270/2024, COES) vencem termos nacionais genéricos.
5. **Antagonismo.** Se a resposta de Claudemberg tiver risco ou contradição com algo já decidido, diga
   antes de seguir — cite o documento de origem.
6. **Espere a resposta.** Nunca responda por Claudemberg nem avance a rodada sem ele.
7. **Linguagem simples**, em português, sem termo técnico sem explicação.

## Como termina

Termina quando não restar pergunta aberta. Então entregue um **resumo do entendimento comum** com:

- o problema que isso resolve e para quem (qual Gestor/Agente);
- o que será construído e o que fica de fora;
- como saberemos que funcionou (o teste, com caso fictício);
- quem é o dono depois de pronto.

E pergunte: **"Entendemos a mesma coisa? Posso começar?"** Nada é construído antes do sim.
