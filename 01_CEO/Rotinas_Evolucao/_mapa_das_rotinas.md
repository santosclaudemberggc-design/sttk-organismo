# Mapa das Rotinas — como se complementam

Pasta criada em 30/09/2026 por decisão de Claudemberg. É a **memória das rotinas**: o que já foi melhorado, como elas estão funcionando no dia a dia e o que os dados mostram que ainda precisa melhorar.

## Regras desta pasta
1. **Antes de mudar qualquer rotina, leia o arquivo dela aqui** (seção 1 e 3). Não reintroduza o que já foi retirado, nem repita uma tentativa que já falhou, sem evidência nova.
2. **Toda mudança numa rotina ganha uma linha na seção 1** do arquivo dela, com versão, data, o que mudou, a evidência e quem decidiu. Isso é feito no mesmo dia, junto com o livro-razão.
3. **O Fechamento do Dia (20:00) escreve a seção 2** (diário de funcionamento) de cada rotina e marca padrões na **seção 3** (candidatas a melhoria).
4. **A Reunião Semanal (segunda 17:00) lê a seção 3 de todas as rotinas.** Só vai à pauta o que tem evidência acumulada. Claudemberg decide; a candidata vira melhoria (seção 1) ou é descartada com o motivo.

## Agenda (desde 01/10/2026)
| Horário | Rotina | Arquivo | Tarefa agendada |
|---|---|---|---|
| seg-sex 08:30 | Ensaio Sombra | `ensaio_sombra.md` | `wallenberg-rotina-ensaio-sombra` |
| seg-sex 09:00 | Diária de Skills | `diaria.md` | `wallenberg-rotina-diaria-skills-v2-7` |
| seg-sex 11:00 | Drenagem Contínua | `drenagem.md` | `wallenberg-drenagem-continua-local` |
| seg 13:00 | Acervo de Normas | `acervo.md` | `wallenberg-rotina-acervo-normas` |
| seg-sex 14:00 | Macetes | `macetes.md` | `wallenberg-rotina-macetes-profissionais` |
| seg 17:00 | Reunião Semanal | `reuniao.md` | `wallenberg-reuniao-semanal` |
| seg-sex 20:00 | Fechamento do Dia | `fechamento_do_dia.md` | `wallenberg-cronjob-pdf-2000` (id antigo, mantido) |

## Como uma alimenta a outra
```
Ensaio Sombra (Bardi monta caso + gabarito lacrado)
   └─> Drenagem (Gestor executa, Bardi corrige) ──> Claudemberg aprova/reprova
            │                                           └─ reprovada → Drenagem corrige a causa e refaz
            ├─ parecer aponta Skill não usada ──> Macetes (prioridade 0a)
            └─ parecer aponta fonte que faltou ──> Acervo (prioridade P1, lista de compra)
Diária (cria/ativa Skills) ── lê ──> passagem do dia (Fechamento 20:00)
Acervo (norma nova muda Skill) ──> pendencias.json ──> Drenagem corrige
Todas ──> Fechamento do Dia (passagem + diário de funcionamento) ──> Reunião (verifica ensaios + candidatas)
```

## Candidatas gerais (valem para todas as rotinas e Agentes)
- **(nova 30/09) Arquivo temporário solto na raiz do projeto.**
  - Evidência: `t.bin`, de cerca de 25 KB, criado em 30/09 às 13:41 durante a pesquisa CAU/CONFEA + ANPD do Kelsen/Hely. Era uma página HTML do CONFEA salva incompleta ("Carregando conteúdo…"). Ficou fora do git, sem valor de fonte. Apagado em 30/09 com autorização de Claudemberg.
  - Sugestão: regra para todos os Agentes e rotinas: arquivo temporário (download para leitura, rascunho, saída de script) vai para uma pasta de rascunho (ex.: `_tmp/`, no `.gitignore`) e é apagado ao fim da tarefa, nunca deixado na raiz. Fonte que vale guardar vai para o acervo certo (`Fontes_Legislacao` do Hely ou `D:\008`).
  - Também detectar no Fechamento do Dia: arquivo novo não rastreado na raiz → candidata.
  - Decisão: Reunião de 05/10.

## Teste único do organismo
Ensaio Sombra 003. O treino fictício foi retirado da Diária e dos Macetes em 30/09. O Notion "Treinos e Testes" ficou só para exames de nível.
