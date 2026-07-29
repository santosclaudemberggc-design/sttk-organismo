---
name: sttickler_niveis_agentes_formacao
description: "Os 4 níveis dos agentes, a cascata de treino/execução autônoma e os Gates como trava de alucinação"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3d61a6b3-ab8c-4190-834f-5a05da02f172
  modified: 2026-07-23T15:03:31.446Z
---

Definido por Claudemberg em 22-23/07/2026, a partir da taxonomia de maturidade de agentes e da referência ORBIS ([[sttickler_orion_orbis_e_mauricios]]).

**Os 4 níveis (medem AUTORIDADE DE EXECUÇÃO, e são POR ESCOPO — o mesmo agente pode estar em níveis diferentes em frentes diferentes):**
1. **Formação** — identidade/regras definidas, testado em sandbox, sem acesso operacional real. Humano = operador.
2. **Shadow** — monitora e recomenda; o humano decide e age. Mede-se a precisão.
3. **Assisted** — cria a ação, mas ela fica retida até aprovação manual (human-in-the-loop). Mede-se a consistência.
4. **Autonomous** — age de ponta a ponta dentro da fronteira de risco; auditado por exceção (human-on-the-loop); **pode treinar e testar os agentes abaixo dele**.

**Modelo de execução autônoma de pendências (regra de Claudemberg, 23/07):**
- Agente **Autonomous** executa as próprias pendências sozinho, sem ordem de Claudemberg.
- Agente que **ainda não é Autonomous** → o **Autonomous responsável por ele dispara** a execução da pendência dele, também sem ordem de Claudemberg. (Kelsen dispara Hely; Wallenberg dispara Gestor não-autônomo.)
- **Tudo que é feito/mudado/criado passa por Claudemberg** — na Reunião Semanal, ou ele vê no Painel do Fundador, ou (futuro) no Sistema de Gestão de Projetos. Nada é aprovado por silêncio.
- **A fronteira NÃO se rompe:** documento que chega ao cliente/prefeitura, Gates 13/16, eliminar agente, mudar escopo de Gestor — continuam exigindo Claudemberg antes. Autonomia proativa vale só dentro da alçada do agente.
- **Toda execução autônoma:** backup antes + livro-razão no mesmo dia.

**Os Gates do coordenador externo (Maurício Costa) são a trava contra ALUCINAÇÃO dos agentes** — é a função deles dentro do fluxo. Nenhuma autonomia passa por cima do Gate. Por isso o Gate do Maurício é pré-requisito de produção real: sem ele, não há freio de alucinação na ponta. Ver [[sttickler_ceo_wallenberg]] (Função 11, Gates 13/16).

**Cascata de treino (Wallenberg → Gestor → Agente):** o Autonomous treina e testa quem está abaixo, com um exame por transição de nível (Shadow=precisão, Assisted=consistência, Autonomous=teste maldoso/se trava sozinho). Critério que atravessa todos: quanto trabalho sobra para Claudemberg. Estado atual: Kelsen=Autonomous (22/07); Hely=Assisted interno/Formação cliente; Lúcio=Formação incompleta; Wallenberg=Autonomous.
