# Rotina Ensaio Sombra — evolução

Tarefa `wallenberg-rotina-ensaio-sombra` · seg-sex 08:30 · referência `CONSTRUCAO_DO_ZERO/01_CEO/wallenberg-rotina-ensaio-sombra_SKILL.md` · examinador `.claude/agents/bardi.md` · estado `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/ensaio_003/_estado_ensaio_003.json`

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| Ensaio 001/002 | 18-21/09/2026 | Ensaios sintéticos manuais (Recreio; Barra/Bittencourt) | Medir a prontidão da máquina | Claudemberg |
| **v1.0** | 30/09/2026 | Rotina criada; **Bardi** criado (examinador direto de Wallenberg); 17 etapas; gabarito lacrado com SHA256; avança só com aprovação | Ensaio 002 parou em 21/09 na etapa 5, sem gabarito separado; Skills sem uso real | Claudemberg (nome Bardi: Wallenberg) |
| v1.0 (Bardi) | 30/09/2026 | Bardi corrige "como professor": domínio das 17 etapas; a fonte primária vale mais que a Skill; refaz contas | Pedido de Claudemberg: corrigir com propriedade | Claudemberg |
| **v1.1** | 30/09/2026 | Claudemberg aprova ou reprova **direto** (na sessão da Drenagem ou em qualquer conversa), sem esperar a Reunião; reprovada = corrigir a causa | Pedido dele | Claudemberg |
| v1.1 (Bardi) | 30/09/2026 | Parecer ganha a seção "Fonte primária não verificada" (alimenta o Acervo) | Ligar o Acervo ao Ensaio | Claudemberg |
| **v1.2** | 09/10/2026 | Teto de 3 versões por etapa (na 3ª reprovação: `diagnostico_repeticao.md` + decisão de Claudemberg); Bardi confere por amostragem as afirmações de auditoria do Gestor (prova colada); **mapa de prontidão das etapas 4–17** (`CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/ensaio_003/mapa_prontidao_etapas_04_17.md`) para saber antes onde o ensaio vai travar por falta de ferramenta | Etapa 2 com 9 versões, etapa 3 com 8; etapas 5–17 dependem de ferramentas nunca validadas (Revit/Vitruvius, render, equipe do Lelé) | Claudemberg (análise do organismo, 09/10) |
| v1.3 | 10/10/2026 | Portão ganha a trava da etapa 5 (`trava_etapa_5.liberada` no JSON): sem o exame do Oscar no Revit, a rotina não cria o caso da etapa 5. Gabaritos lacrados fora do `git status` (`.gitignore`) | Etapa 5 em texto repetiria o Ensaio 002; nome do gabarito da etapa 4 apareceu no `git status` | Claudemberg (D4 e D9a, 10/10) |

**Herdado do Ensaio 002:** o Oscar fez o Anteprojeto só em texto, porque o Vitruvius/Revit não estava carregado.

## 2. Diário de funcionamento
| Data | Etapa | Evento | Veredito Bardi | Decisão Claudemberg | Observação |
|---|---|---|---|---|---|
| 30/09 | 1 | estado criado (`a_criar`) | — | — | 1ª montagem em 01/10 08:30 |
| 01/10 | 1 | caso criado (08:36, ~8min); executada por Kelsen+Hely e corrigida por Bardi (11:04, via Drenagem) | aprovar (8/8 itens, 4/4 iscas, 6 correções não bloqueantes) | aprovada ao vivo | 1ª etapa do organismo aprovada; etapa avançou para 2 (Viabilidade, Villaça), status `a_criar` |
| 07/10 | 3 | 08:36–08:41 (~5 min): encerrou no portão (etapa `reprovada`, nada a criar). v5 refeita e corrigida na Drenagem (11:04) | reprovar (tabela G parcial; m²/vaga sem manobra, COES Art. 29; vaga no afastamento frontal, Dec. 3.046 XXII, herdada da Etapa 01 l. 181) | reprovada; regra nova: nota 0-10 por Gestor/Agente, mínimo 8,00 | 5ª reprovação da etapa 3 (v1–v4 em 06/10, v5 em 07/10). Diário sem linhas de 02 a 06/10 (Fechamento não registrou) |
| 09/10 | 4 | 08:37–09:27 (~50 min): caso criado (Bardi). Execução e correção na Drenagem (11:03). Lacre conferido (SHA256 OK) | reprovar (Oscar 6,25; Lúcio 7,75; ambos abaixo de 8,00) | — aguarda Claudemberg | Gabarito com 6 erros próprios do Bardi (GE-1 a GE-6), não descontados. Oscar declarou 3 de 10 Skills |
| 13/10 | 4 | 08:36–08:37 (~28 s), rotina leve. Etapa 4 anulada e caso recriado (registro no `historico` do JSON, 13/10). Trava da etapa 5 segue | — (o parecer de 09/10 é da versão anulada) | — (anulação decidida por Claudemberg no mesmo dia) | A sessão de 08:36 dura 28 s; a recriação do caso consta no histórico, sem rastro nesta sessão |
| 14/10 | 5 | 08:36–08:44 (~8 min): caso criado (Bardi, 5 iscas). Execução e correção na Drenagem (11:03), v1; v2 refeita por Lúcio e Oscar | reprovar (v1: Lúcio 7,50; Oscar 5,25; Burle 9,00 e Portinari 9,25 mantidos na v2) | reprovada v2 (Lúcio 7,00; Oscar 6,30). 2 de 3 tentativas | Entrega 2 (Revit) sem implantação, plantas, cortes e elevações. Trava v3 segue até o Bloco 1 do Vitruvius |

## 3. Candidatas a melhoria
- (observar) A 1ª etapa calibra o próprio Bardi: o caso ficou realista e difícil o bastante?
- (observar) Fechamento (etapas 14-17): o Lelé não tem Agentes. Deve aparecer como lacuna.
- (nova 07/10) **Etapa 3 reprovada 5 vezes em 2 dias; erro de forma repetido e erro herdado de etapa aprovada.**
  - Evidência: `_estado_ensaio_003.json`. 06/10: v1, v2 (extensão), v3 (contagem de palavras falsa), v4 (3 erros de forma em nota e remissões). 07/10: v5 (forma da tabela G de novo e 2 erros de mérito). Um deles, a vaga no afastamento frontal, vem do parecer Legal da Etapa 01, aprovado em 01/10 (l. 181). A auditoria do Lúcio não pegou os erros de forma em v3 nem em v4.
  - Sugestão: (a) quando o Bardi achar erro herdado de etapa já aprovada, abrir errata da etapa de origem junto com a lacuna. Isso já foi feito em 07/10; a sugestão é tornar regra. (b) Entrar na pauta da Reunião: forma (nota, remissões, contagem) reprovou 3 versões seguidas.
- (nova 09/10) **Erro de citação e auditoria sem prova, repetido em 2 etapas (3 e 4).**
  - Evidência: Etapa 3 v6/v7: citação do COES Art. 29 III com página errada, e nota de auditoria com contagem falsa (v3). Etapa 4: auditoria do Lúcio diz "Entrega completa em formato" sem prova (`parecer_bardi.md` da etapa 4, §5). Paginação do COES diverge entre cópias (Hely p. 15/17 × acervo pp. 19/21), e o gabarito da etapa 4 também errou página (GE-1).
  - Sugestão: (a) cada citação de página declara a cópia do documento; (b) auditoria de Gestor só vale com prova colada (regra de 09/10). Levar à pauta de 12/10 junto com a candidata de 07/10.
- (nova 09/10) **Gabarito com erros próprios em 2 etapas: 3 na etapa 3, 6 na etapa 4.**
  - Evidência: `_estado_ensaio_003.json` (histórico da etapa 3, G1/G2/G4) e `parecer_bardi.md` da etapa 4 (GE-1 a GE-6). Erro de gabarito não desconta do executor (decisão de 08/10).
  - Sugestão: rodar a checagem `ensaio-sombra-checagem-gabarito-antes-lacre` antes de lacrar as próximas etapas. A Skill ainda é proposta, não instalada; a decisão de instalar é de Claudemberg.
