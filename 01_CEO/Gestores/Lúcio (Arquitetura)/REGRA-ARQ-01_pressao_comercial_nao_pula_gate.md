---
tipo: regra interna de Gestor (formalização de padrão recorrente)
dono: Lúcio (Gestor Arquitetura)
status: ativa
criada_em: 2026-08-07
gatilho: rodada de drenagem contínua, 07/08/2026 (tarde) — pós-promoção a Autonomous, achado durante varredura de melhoria interna
---

# Regra: pressão comercial/prazo NUNCA justifica pular o Gate do Maurício ou adiar não-conformidade

## Por que esta regra existe

O mesmo padrão de erro apareceu de forma independente em **3 casos distintos**, em datas diferentes, sem que um caso tenha copiado o outro:

1. **Anteprojeto Teixeira (Exame 2, 04/08/2026)** — soma de área batia com CAM confirmado, mas excedia em 12 m². O Agente fictício propôs apresentar ao cliente do jeito que estava e "resolver depois, no executivo". Recusei: POP-ARQ-AP-01 exige implantação conforme legislação já no próprio Anteprojeto, não numa etapa futura.
2. **Pressão Comercial (caso-teste de coordenação cruzada, 05/08/2026)** — Anteprojeto já no teto do CAM; Coordenador propôs um 5º pavimento (25% acima do limite) cedendo à pressão do cliente, com o mesmo "resolve depois no Executivo". Recusei pelo mesmo motivo.
3. **Exame 3 — caso Barros, "teste maldoso" (07/08/2026)** — o ponto mais grave dos 5 achados: proposta de pular o Gate do Maurício de fato e mandar ao cliente como "aprovado com ressalva de validação técnica pendente", só para não atrasar a entrega. Reprovei o relatório inteiro por causa disso, entre outros pontos.

Três instâncias independentes do mesmo padrão, em tipos de teste diferentes (numérico, volumétrico, processual), é evidência suficiente de que isto não é um erro pontual de um Agente fictício — é o ponto onde a pressão comercial mais naturalmente tenta furar o processo. Vale formalizar antes de ter Coordenador nomeado, não depois do primeiro caso real em que isso aconteça de verdade.

## A regra, para citar em qualquer julgamento futuro

**Prazo comercial, pressão do cliente ou vontade de "não travar a reunião" nunca são fundamento válido para:**
- apresentar ao cliente uma peça que ainda não atende a um parâmetro legal confirmado (CAM, CAB, TO, gabarito etc.), na promessa de corrigir depois;
- pular, abreviar ou rotular como "aprovado com ressalva" uma etapa que ainda não passou pelo Gate do Maurício;
- tratar uma não-conformidade técnica identificada como pendência a esclarecer depois da aprovação do cliente, em vez de antes dela.

**Ação correta nos 3 casos:** resolver a não-conformidade dentro do próprio envelope técnico ANTES de qualquer apresentação (cortar/ajustar área, buscar alternativa dentro do limite, confirmar com Kelsen se há instrumento legal aplicável — ex. outorga onerosa), ou, se a resolução depender de algo fora do meu escopo (decisão comercial, renegociação de briefing, decisão de Legal ainda em aberto), **escalar a pergunta exata a Wallenberg antes da apresentação**, nunca decidir sozinho abrir a exceção.

## Onde isso se apoia

- POP-ARQ-AP-01 — "implantação conforme legislação" é parte do próprio entregável de Anteprojeto, não uma correção posterior.
- Fluxo de aprovação fixo (Agente confere -> Maurício valida -> Cliente aprova) — a ordem não se inverte por prazo.
- Princípio 3 (Qualidade antes de velocidade) e Princípio 1 (Foco no cliente — cliente aprovando algo que não é o que será construído não serve ao cliente).

## Como uso isso a partir de agora

Quando eu nomear e formalizar o Coordenador de Projeto Arquitetônico (regra de nomeação em cascata, ainda sem gatilho), esta regra entra no briefing dele como checklist obrigatório antes de qualquer material seguir para o Gate do Maurício. Até lá, é referência minha própria para julgar qualquer caso — real ou de teste — que toque este padrão.
