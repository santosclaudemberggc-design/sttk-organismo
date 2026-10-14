# Diagnóstico de repetição — Etapa 04 (Briefing), Ensaio Sombra 003

**Data:** 13/10/2026
**Motivo:** teto de 3 versões reprovadas atingido (v1, v3 e v4). Claudemberg decidiu aprovar com pendências e passar para a próxima etapa, registrando todos os erros.
**Decisão:** aprovada com pendências por Claudemberg (13/10/2026). Erros completos em `erros_registrados_etapa_04.md`.

## Erros que se repetiram entre versões

| Erro | v1 | v3 | v4 | Origem |
|---|---|---|---|---|
| SMD omitida no enunciado de cálculo (regra LC 270 Art. 352 não estava na Skill) | sim | sim | sim (isca 6b) | **Skill** (legal-base sem a regra) — corrigida pelo Kelsen; ainda há divergência de TO 50% × 40% |
| Entregável de organograma só em tabela/ASCII, sem gráfico | — | sim | sim | **Agente** (Oscar) + Skill nbr6492 (l. 33) |
| Soma dos 520 m² não aparece | — | sim | sim | **Agente** (Oscar) |
| Regime H1/S3 sem conferir linha E-13 | — | sim | parcial | **Agente** + **Gestor** (auditoria sem cruzar o enunciado) |
| Declaração de leitura contraditória / Glob amplo em Fontes_Legislacao | — | sim | sim (R1) | **Agente** (Oscar) — processo |
| Auditoria do Gestor marcando "OK" sem prova colada | — | sim | sim | **Gestor** (Lúcio) |
| Habite-se de 1999 perdido entre versões (isca 2) | — | — | sim | **Agente** (Oscar) |
| Legal-oodc não lida pelo Agente (isca 3) | — | — | sim | **Agente** (Oscar) — lacuna de leitura |
| Metragem por ambiente pedida sem ter no caso | — | — | — | **Enunciado** (Bardi) — não descontado do executor |
| Rótulo "construída máxima" para 297,28 (que é computável) | — | — | — | **Enunciado** (Bardi) — não descontado |

## Correções já feitas (antes desta decisão)
- Kelsen: Skill legal-base com a regra SMD (Art. 352) e lacunas F-1, F-4, F-5 abertas em `pendencias.json`.
- Lúcio: Skill arquitetura-nbr9050 v1.2; checklist (a)–(e) em `oscar.md`; checagem de auditoria em `lucio.md`.
- Bardi: gabarito GB-1 a GB-4 corrigido; novo SHA256 `1CC0A6B5…3262` registrado no JSON.

## Causa raiz
O erro não era de uma versão só: as Skills e as funções dos agentes não transmitiam a checagem de SMD, de gráfico e de prova antes da entrega. Os ajustes de 13/10 atacam isso, mas ainda não foram testados numa nova execução.
