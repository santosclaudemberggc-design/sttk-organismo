# Rotina Macetes de Profissionais e Empresas — evolução

Tarefa `wallenberg-rotina-macetes-profissionais` · seg-sex 14:00 · fila `CONSTRUCAO_DO_ZERO/01_CEO/Skills_Propostas/_macetes_fila.md` · sem arquivo de referência (o prompt agendado é a fonte única)

## 1. Melhorias feitas
| Versão | Data | O que mudou | Por quê (evidência) | Decidiu |
|---|---|---|---|---|
| v1.0 | 29/09/2026 | Criada: macetes de profissionais, validados pelo Gestor dono, com treino fictício | "Os macetes dos melhores profissionais são o essencial para a inteligência dos agentes" | Claudemberg |
| v1.1 | 29/09/2026 | Duas fontes obrigatórias: (A) profissional renomado e (B) grande empresa; `/watch` em modo legenda; yt-dlp atualizado às segundas | Falha do /watch em 24/09 | Claudemberg |
| **v1.2** | 30/09/2026 | Treino retirado; prioridade 0a/0b ligada ao Ensaio; fonte C (legal) para o Kelsen; regra das 2 tentativas; portão de custo (Gestor sem Skill não é aberto; fila esgotada → só ter/qui) | Varandas travou o Kelsen; 36 de 43 Skills sem macete (cerca de 12 dias úteis e depois rodaria vazia) | Claudemberg |
| **pausa** | 09/10/2026 | Tarefa agendada desligada (`enabled: false`). Volta quando: (a) uma rodada manual com o `/watch` no motor Gemini assistir de fato pelo menos 1 vídeo do YouTube, e (b) a fila tiver Skills com fonte A/B/C provável (Skills jurídicas do Kelsen vão direto à fonte C) | Rodadas de 07/10 e 08/10 (3 commits) com 0 macetes: prioridade vazia, Skills jurídicas sem fonte pública, vídeos bloqueados pelo YouTube | Claudemberg (análise do organismo, 09/10) |
| pausa confirmada | 10/10/2026 | Pausa mantida até o teste do `/watch` (motor Gemini) num vídeo do YouTube | Mesma evidência da pausa de 09/10 | Claudemberg (D8, 10/10) |

**Tentado e revertido:** treino fictício (29/09 → 30/09).

## 2. Diário de funcionamento
| Data | Rodou? | Duração | Resultado | Observação |
|---|---|---|---|---|
| 29/09 | sim | ~11 min | 8 macetes em 2 Skills; varandas sem macete | Rodou às 18:09 (1ª execução no dia da criação) |
| 30/09 | pausada | — | — | Revisão das rotinas |
| 01/10 | sim | ~9 min | 7 macetes em 2 Skills (nbr15220-3 Lúcio v1.1→v1.2; fundacoes-solos-moles Cardozo 1.2→1.3); varandas sem macete (2ª rodada) | — |
| 07/10 | sim | sem dado (início 14:14; a sessão ainda aparece "running", com última atividade em 08/10 07:19) | 0 macetes; `legal-oodc-mais-valera-mais-valia` (Kelsen), 2ª rodada sem macete → "Sem fonte pública" | Prioridade 1 vazia; prioridade 2 só ter/qui. Diário sem linhas de 02 a 06/10 |
| 09/10 | não rodou | — | — | Tarefa pausada (`enabled: false`) em 09/10. Última execução: 08/10 (14:14 local), 0 macetes |

## 3. Candidatas a melhoria
- (confirmada 01/10) A fonte C não destravou o Kelsen: varandas falhou pela 2ª rodada seguida (tipo A e C tentados, só achada a ata do COMPUR 2007 com opinião, sem técnica nova) e foi para "Sem fonte pública", como esta candidata antecipava em 29/09.
- (nova 07/10) **As Skills de interpretação jurídica do Kelsen saem da fila sem macete.**
  - Evidência (`_macetes_fila.md`): varandas (29/09 e 01/10) e OODC (05/10 e 07/10), 2 rodadas cada, zero fonte A/B/C com credencial. Contraexemplo: `decreto3046` recebeu macete tipo C (Dicionário da SMDU) em 06/10.
  - Sugestão: para Skills de decisão jurídica caso a caso, ir direto à fonte C oficial (dicionário, cartilha ou parecer da SMDU) na 1ª rodada, em vez de A/B.
- (nova 07/10) Sessão de 07/10 ainda "running" na manhã de 08/10. Observar se repete.
