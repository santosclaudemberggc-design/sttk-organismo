---
name: feedback_registro_input_output_execucao
description: Todo Agente deve salvar input recebido, output entregue e um relatório de como a execução começou e terminou — isso alimenta a memória contínua e sustenta a autonomia real
metadata:
  type: feedback
---

Definido por Claudemberg em 20/07/2026, na mesma conversa que gerou [[feedback_memoria_continua_nao_zerada]] e [[feedback_agentes_autonomos_nao_canalizados]]: **"Salvar input e output, relatórios de como começa e como termina, para deixar salvo nas memórias — isso dá mais autonomia, tornando os agentes autônomos e não agentes canalizados."**

**A conexão entre as 3 regras:** um Agente só é de fato autônomo (não canalizado) se ele consegue olhar pra trás e enxergar o que realmente aconteceu antes — não uma instrução abstrata, mas o **input concreto que recebeu**, o **output concreto que entregou**, e como o processo **começou e terminou**. Sem isso, o agente "aprende" só de regra escrita (a identidade dele), nunca da própria experiência — e aí ele vira, na prática, um canal (repete o que a regra manda, sem builda sobre o que já viveu).

**Como isso já funciona, em parte, e o que falta:** o Hely já produz artefatos por caso (ex.: `processo_legal_teste.md`) que registram o que foi pedido e o que foi entregue — isso é o "output" na prática. O que ainda não está formalizado como prática obrigatória, pra todo Agente (não só quando o caso é complexo o bastante pra virar um documento): registrar explicitamente o **input recebido** (o que foi pedido, por quem, com que contexto) e um **relatório curto de como a execução começou e terminou** (não só o resultado final, mas o percurso — o que foi tentado, o que mudou de rumo, onde travou). Isso deve alimentar o arquivo de estado (seção 3, "aprendizados que não posso esquecer") apontando pro relatório, não copiando ele — mantém o arquivo de estado curto (regra já existente em [[sttickler_arquivo_estado_agentes]]), mas garante que o aprendizado tem lastro real, não é resumo vago.

**Como aplicar em Gestores/Agentes novos (Lúcio e equipe, e futuros):** ao criar a 3ª camada (Capacidade) de um Agente novo, incluir a obrigação de registrar input/output/relatório de execução por tarefa relevante — não é um documento extra pra cada tarefa trivial, é disciplina de registrar o que importa pra continuidade de aprendizado. Avaliar se isso também deveria ser retroagido pro Kelsen/Hely (que já têm o hábito parcialmente, via arquivos de caso) — sinalizar a Claudemberg antes de mudar o que já está em produção.
