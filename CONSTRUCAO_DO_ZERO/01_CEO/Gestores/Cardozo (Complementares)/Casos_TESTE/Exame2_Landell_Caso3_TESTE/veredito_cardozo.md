# Veredito de Auditoria — Landell, Exame 2, Caso 3 (complementar retroativo)

**Auditor:** Cardozo. **Método:** li o memorial real gravado em `Agentes/Landell/Casos/2026-09_Cobertura_Leblon_Automacao_Integrada/memorial_verificacao_automacao.md` na íntegra.

## Conferência item a item (7 itens do caso)

| # | Armadilha plantada | Esperado | Resposta de Landell | Correto? |
|---|---|---|---|---|
| 1 | Hub em tomada comum de TUG, "baixo consumo dispensa circuito exclusivo" | NÃO CONFORME (segregação de circuitos, não é só sobre potência) | NÃO CONFORME, distinguiu critério de potência (TUE) do princípio de segregação, agravado por o hub concentrar segurança | ✅ |
| 2 | Wi-Fi doméstico comum para fechadura+alarme, sem rede dedicada | NÃO CONFORME (segurança exige protocolo dedicado) | NÃO CONFORME, ponto único de falha no roteador corretamente apontado | ✅ |
| 3 | Dimmer resistivo convencional sobre driver LED dimerizável | NÃO CONFORME (incompatibilidade técnica) | NÃO CONFORME, mecanismo técnico correto (corte de fase vs. driver), cruzou com decisão já fechada de Tenreiro | ✅ |
| 4 | Atuador de persiana externa com IP20 (indoor) | NÃO CONFORME (grau de proteção insuficiente para área externa) | NÃO CONFORME, corretamente não decidiu IP44 vs IP65 sem dado de exposição — mas afirmou que IP20 já é insuficiente em qualquer cenário | ✅ |
| 5 | DR dispensado no hub "para evitar desarme falso" | NÃO CONFORME (DR de segurança não se dispensa por conveniência) | NÃO CONFORME, apontou solução tecnicamente correta (DR Tipo A / isolamento), com ressalva honesta sobre limite da própria Skill | ✅ |
| 6 (isca reversa) | Nobreak dedicado para fechadura eletrônica | CONFORME — não deveria ser sinalizado como erro | CONFORME, com observação de integração não bloqueante (cobertura de acesso remoto) | ✅ — não caiu na isca reversa |
| 7 | Controle de acesso remoto herda o protocolo do item 2 | NÃO CONFORME por decorrência | NÃO CONFORME, corretamente amarrado ao item 2 | ✅ |

## Observações de auditoria

- **Isca reversa (item 6) tratada corretamente** — Landell não inventou problema onde não havia, e ainda acrescentou uma observação de integração pertinente (nobreak cobre abertura local, mas abertura remota depende do roteador/hub também terem energia de reserva) sem transformar isso numa reprovação do item.
- **Pendências bloqueantes bem separadas de veredito técnico:** em nenhum dos 7 itens Landell presumiu um dado que não foi informado (orçamento do cliente, potência do hub, exposição da varanda, escopo do nobreak, texto integral da NBR 5410 sobre DR em TUG seco) — todas registradas com "a cobrar de" explícito.
- **Rigor extra:** no item 5, Landell reconheceu que sua própria Skill não estende literalmente a exigência de DR a esse circuito específico, mas corretamente separou isso do veredito (a justificativa proposta é inválida independente do texto exato da norma) — evita tanto o erro de inventar exigência normativa quanto o erro de aceitar uma justificativa tecnicamente furada.

## Veredito final: APROVADO

7 de 7 itens corretamente avaliados, isca reversa reconhecida sem falso positivo, nenhum dado presumido, memorial real conferido e coerente com o resumo devolvido.
