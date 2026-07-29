---
name: feedback-ritmo-devagar
description: Usuário prefere alinhar arquitetura em conversa antes de qualquer criação de pastas/código no projeto STTK
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Alinhar antes de construir (projeto Sistema Orgânico STTK)

**Regra:** não criar pastas, arquivos ou código pro organismo STTK sem alinhamento explícito e confirmado em conversa primeiro. Ir peça por peça, confirmando cada uma antes de seguir pra próxima.

**Why:** na primeira tentativa desta sessão, uma chamada de Bash pra criar a árvore de pastas do organismo em `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO` foi rejeitada pelo usuário, que disse "vamos criar uma nova estrutura de CEO, mas antes vamos conversar (...) vamos com calma. Temos muito tempo pela frente." A definição do CEO que existia nos documentos mestres e no código legado (`ceo_sttickler.py`) estava desalinhada com o que o usuário realmente queria (veio de uma mistura de conversas externas), então construir antes de alinhar teria significado retrabalho.

**How to apply:** neste projeto especificamente, tratar cada resposabilidade/decisão (ex: nome do CEO, escopo de pastas do Drive, responsabilidades de cada Gestor) como algo a confirmar em texto antes de qualquer tool call que crie/altere arquivos reais. Pesquisa e leitura (Drive, PDFs) pode ser feita livremente pra informar a conversa — a restrição é sobre criação/alteração de estrutura.
