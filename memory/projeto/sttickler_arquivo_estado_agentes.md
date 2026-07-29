---
name: sttickler-arquivo-estado-agentes
description: Todo agente do organismo STTK tem arquivo de estado que lê ao nascer e escreve ao morrer — decidido 20/07/2026
metadata: 
  node_type: memory
  type: project
  originSessionId: be2ae7d0-4de9-4a7d-b17f-ced23b4a45df
  modified: 2026-07-20T18:27:28.819Z
---

Decisão de Claudemberg em **20/07/2026**: todo agente do Sistema Orgânico STTK tem **um** arquivo de estado — memória privada entre execuções. Lê ao nascer (antes de interpretar o pedido), escreve ao morrer (antes de devolver o retorno pro nível de cima). Cada um escreve só no próprio.

- Wallenberg: `01_CEO\_estado_wallenberg.md`
- Kelsen: `01_CEO\Gestores\Kelsen (Legal)\_estado_kelsen.md`
- Hely: `01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\_estado_hely.md`

Estrutura fixa de 4 seções: onde parei / pendências abertas / aprendizados que não posso esquecer / como escrever nele.

**Why:** os subagentes (Kelsen, Hely) nascem zerados a cada acionamento e perdiam tudo que não virasse documento solto; Wallenberg perde contexto a cada fechamento do app. O estado é o que sustenta continuidade real (Princípio 8, Rastreabilidade).

**How to apply:** convive com o Registro Diário, não substitui — estado é memória privada ("de onde eu parei"), Registro Diário é o que sobe pra Claudemberg no mesmo dia. O estado é curto e aponta pros documentos, não copia conteúdo. Todo Gestor/Agente novo nasce com o seu, no mesmo molde, dentro da própria pasta. **Não gera PDF** (exceção à regra de [[feedback-pdf-junto-com-md]] — é arquivo de máquina reescrito toda hora, Princípio 19).

Ponto correlato decidido no mesmo dia: **Wallenberg não vira subagente** — a centralidade dele vem de ser a conversa que Claudemberg abre. Ver [[sttickler-ceo-wallenberg]].
