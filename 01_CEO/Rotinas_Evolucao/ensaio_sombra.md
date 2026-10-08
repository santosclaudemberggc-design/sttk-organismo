# Rotina Ensaio Sombra — evolução

Tarefa `wallenberg-rotina-ensaio-sombra` · seg-sex 08:30 · referência `01_CEO/wallenberg-rotina-ensaio-sombra_SKILL.md` · examinador `.claude/agents/bardi.md` · estado `01_CEO/Casos_TESTE/ensaio_003/_estado_ensaio_003.json`

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| Ensaio 001/002 | 18-21/09/2026 | Ensaios sintéticos manuais (Recreio; Barra/Bittencourt) | Medir a prontidão da máquina | Claudemberg |
| **v1.0** | 30/09/2026 | Rotina criada; **Bardi** criado (examinador direto de Wallenberg); 17 etapas; gabarito lacrado com SHA256; avança só com aprovação | Ensaio 002 parou em 21/09 na etapa 5, sem gabarito separado; Skills sem uso real | Claudemberg (nome Bardi: Wallenberg) |
| v1.0 (Bardi) | 30/09/2026 | Bardi corrige "como professor": domínio das 17 etapas; a fonte primária vale mais que a Skill; refaz contas | Pedido de Claudemberg: corrigir com propriedade | Claudemberg |
| **v1.1** | 30/09/2026 | Claudemberg aprova ou reprova **direto** (na sessão da Drenagem ou em qualquer conversa), sem esperar a Reunião; reprovada = corrigir a causa | Pedido dele | Claudemberg |
| v1.1 (Bardi) | 30/09/2026 | Parecer ganha a seção "Fonte primária não verificada" (alimenta o Acervo) | Ligar o Acervo ao Ensaio | Claudemberg |

**Herdado do Ensaio 002:** o Oscar fez o Anteprojeto só em texto, porque o Vitruvius/Revit não estava carregado.

## 2. Diário de funcionamento
| Data | Etapa | Evento | Veredito Bardi | Decisão Claudemberg | Observação |
|---|---|---|---|---|---|
| 30/09 | 1 | estado criado (`a_criar`) | — | — | 1ª montagem em 01/10 08:30 |
| 01/10 | 1 | caso criado (08:36, ~8min); executada por Kelsen+Hely e corrigida por Bardi (11:04, via Drenagem) | aprovar (8/8 itens, 4/4 iscas, 6 correções não bloqueantes) | aprovada ao vivo | 1ª etapa do organismo aprovada; etapa avançou para 2 (Viabilidade, Villaça), status `a_criar` |
| 07/10 | 3 | 08:36–08:41 (~5 min): encerrou no portão (etapa `reprovada`, nada a criar). v5 refeita e corrigida na Drenagem (11:04) | reprovar (tabela G parcial; m²/vaga sem manobra, COES Art. 29; vaga no afastamento frontal, Dec. 3.046 XXII, herdada da Etapa 01 l. 181) | reprovada; regra nova: nota 0-10 por Gestor/Agente, mínimo 8,00 | 5ª reprovação da etapa 3 (v1–v4 em 06/10, v5 em 07/10). Diário sem linhas de 02 a 06/10 (Fechamento não registrou) |

## 3. Candidatas a melhoria
- (observar) A 1ª etapa calibra o próprio Bardi: o caso ficou realista e difícil o bastante?
- (observar) Fechamento (etapas 14-17): o Lelé não tem Agentes. Deve aparecer como lacuna.
- (nova 07/10) **Etapa 3 reprovada 5 vezes em 2 dias; erro de forma repetido e erro herdado de etapa aprovada.**
  - Evidência: `_estado_ensaio_003.json`. 06/10: v1, v2 (extensão), v3 (contagem de palavras falsa), v4 (3 erros de forma em nota e remissões). 07/10: v5 (forma da tabela G de novo e 2 erros de mérito). Um deles, a vaga no afastamento frontal, vem do parecer Legal da Etapa 01, aprovado em 01/10 (l. 181). A auditoria do Lúcio não pegou os erros de forma em v3 nem em v4.
  - Sugestão: (a) quando o Bardi achar erro herdado de etapa já aprovada, abrir errata da etapa de origem junto com a lacuna. Isso já foi feito em 07/10; a sugestão é tornar regra. (b) Entrar na pauta da Reunião: forma (nota, remissões, contagem) reprovou 3 versões seguidas.
