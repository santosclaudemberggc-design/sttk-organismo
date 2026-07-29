---
name: feedback-pdf-junto-com-md
description: "Toda vez que um documento de conteúdo é criado em .md no organismo STTK, precisa vir junto uma versão .pdf"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 45721438-1d5e-4c47-af6a-1ed9bf78c707
---

Regra permanente definida por Claudemberg em 15/07/2026: todo documento de conteúdo criado em `.md` dentro do organismo STTK (Registro Diário, caso-teste, índice de fontes, relatório etc.) precisa ter uma versão `.pdf` correspondente, na mesma pasta, mesmo nome de arquivo — pra poder visualizar sem precisar abrir o `.md` bruto.

**Como aplicar:** usar `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\_ferramentas\md_to_pdf.py` (script Python com `markdown` + `xhtml2pdf`, ambos instalados via pip, estilo já configurado — títulos, tabelas, listas, blocos de código legíveis). Gerar o PDF assim que o `.md` for criado ou editado de forma relevante, não deixar acumular.

**Escopo:** aplica a documentos ativos do organismo (Registros Diários, casos-teste, Skills, propostas de Gestor em `.md`). **Não se aplica** a `CLAUDE.md` (arquivo de instrução, não documento de conteúdo) nem a `00_HISTORICO\` (arquivos legados, não editados ativamente). Regra registrada também em `CLAUDE.md`, seção "Onde tudo mora".

**Pendência em aberto (15/07/2026):** as propostas de Gestor/Skill hoje são `.html` (ex: `gestor_legal_proposta.html`, `skill_base_legislativa_bairro_proposta.html`, `gestor_arquitetura_proposta.html`), não `.md` — a regra como definida não cobre esses arquivos literalmente. Perguntei a Claudemberg se ele quer estender a regra pra HTML também; aguardando resposta antes de decidir.
