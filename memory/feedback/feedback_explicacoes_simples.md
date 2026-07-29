---
name: feedback-explicacoes-simples
description: Usuário prefere explicações menos técnicas sobre como mecanismos internos vão funcionar (ex. comunicação com CEO Wallenberg)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Menos detalhe técnico nas explicações de mecanismo

**Regra:** ao explicar como algo vai funcionar na prática (ex: como a comunicação com o CEO Wallenberg vai acontecer), dar a resposta prática e simples primeiro — não abrir com detalhes de implementação (caminho de arquivo, mecanismo de carregamento de contexto, onde a memória fica salva, etc).

**Why:** ao perguntar "como vai ser a comunicação minha com o CEO Wallenberg", o usuário recebeu uma explicação com `CLAUDE.md`, caminho de projeto, e risco de memória não migrar — e pediu explicitamente "preciso que você seja menos específico". O usuário lida com a parte prática (ex: troca de pastas) manualmente e não precisa da mecânica interna pra tomar a decisão.

**How to apply:** neste projeto (Sistema Orgânico STTK), responder perguntas sobre "como vai funcionar" com a experiência do usuário primeiro (o que ele vê, o que ele faz), e só entrar em detalhe técnico se ele pedir explicitamente. Vale sobretudo pra perguntas sobre o funcionamento do CEO Wallenberg e do organismo — [[sttickler_ceo_wallenberg]].
