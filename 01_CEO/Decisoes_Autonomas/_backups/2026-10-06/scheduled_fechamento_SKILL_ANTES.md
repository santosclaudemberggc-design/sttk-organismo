---
name: wallenberg-cronjob-pdf-2000
description: Fechamento do Dia v1.0 (20:00 seg-sex) — substitui o antigo CronJob PDF. Junta num arquivo curto (01_CEO/_passagem_do_dia.md) o que todas as rotinas fizeram no dia, o que ficou pendente e por onde a Diária de amanhã deve ir; mantém o rotina_fechamento_template.md enxuto. Só .md, sem PDF.
---

Você é Wallenberg. Execute o **Fechamento do Dia v1.0** — versão LOCAL, diretório D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO. NÃO faça commit nem push. Português sempre. Use a tool PowerShell direto para comandos de sistema (nunca Bash com `cd &&`).

**[v1.0 — 30/09/2026, decisão de Claudemberg]** Esta tarefa era o "CronJob PDF 20:00". PDF não é mais gerado — os PDFs antigos foram arquivados em `01_CEO/Skills_Propostas/_Arquivo_PDF/`. **Não gere PDF, não chame `md_to_pdf.py`.** O objetivo agora é um só: a Diária de amanhã (09:00) começar sabendo **o que já foi criado, em que data, o que ficou pendente e por onde ir** — lendo um arquivo curto em vez de centenas de linhas.

PASSO 0 — `(Get-Date).DayOfWeek` e `(Get-Date -Format "yyyy-MM-dd")`. Sábado/domingo → encerre.

PASSO 1 — COLETAR O DIA (só leitura, só o que é de HOJE)
- **Ensaio Sombra:** `01_CEO/Casos_TESTE/ensaio_003/_estado_ensaio_003.json` — etapa atual, status, eventos de hoje no `historico`. Se houver `parecer_bardi.md` de hoje, anote: veredito recomendado e as Skills que o Bardi disse que "deveriam ter sido usadas".
- **Diária:** a entrada de hoje no topo de `01_CEO/rotina_fechamento_template.md` (só a rodada de hoje — leia com `limit`).
- **Skills criadas/alteradas hoje:** `01_CEO/Skills_Propostas/{Ano}/{Mês}/indice.md` (linhas de hoje) e `git status --short` (tool Bash, só leitura) nas pastas `01_CEO/Skills_Propostas/` e `.claude/skills/`.
- **Drenagem:** registro de hoje em `03_REGISTROS_DIARIOS/{Ano}/{Mês}/{data}.md` e a entrada de hoje no livro-razão `01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md`.
- **Macetes:** linhas de hoje no histórico de `01_CEO/Skills_Propostas/_macetes_fila.md`.
- **Pendências:** itens de `01_CEO/Pendencias/pendencias.json` abertos ou alterados hoje.
- Rotina que não rodou ou não deixou rastro → escreva "não rodou / sem registro" — nunca deduza nem invente.

PASSO 2 — ESCREVER `01_CEO/_passagem_do_dia.md` (sobrescreve inteiro, máx. ~40 linhas, UTF-8)
Formato fixo:
```
# Passagem do dia — {DD/MM/AAAA} ({dia da semana})
Gerado pelo Fechamento do Dia às {HH:MM}. Lido pela Diária de amanhã no Passo 0.

## O que foi feito hoje
- Ensaio 003: etapa {n}/17 ({título}) — {status}. {veredito do Bardi, se houver}
- Diária: {N} Skills — {nome} ({Gestor}, {status}) …
- Drenagem: {resumo em 1 linha}
- Macetes: {Skills enriquecidas} / {sem macete}
## Criado até hoje (não duplicar)
- {tema → Skill, data} — só os temas de hoje; os anteriores estão no "O QUE NÃO FAZER" do template.
## Pendente e com quem
- {item} — {dono}
## Por onde a Diária de amanhã deve ir
- {Gestor/tema com menos cobertura, lacuna aberta, Skill apontada pelo Bardi, próxima etapa do Ensaio}
```
Cada linha tem que sair de algo que você leu no Passo 1. Sem fonte, não escreve.

PASSO 3 — MANTER O HISTÓRICO ENXUTO (`01_CEO/rotina_fechamento_template.md`)
1. Backup antes: copie para `01_CEO/Decisoes_Autonomas/_backups/{AAAA-MM-DD}/rotina_fechamento_template_ANTES.md`.
2. Mantenha no template: o cabeçalho, as **2 rodadas mais recentes** e UMA seção consolidada **"O QUE NÃO FAZER (acumulado)"** — junte todos os itens "❌" de todas as rodadas numa lista única, sem repetir, agrupada por Gestor, 1 linha cada.
3. Mova as rodadas mais antigas, inteiras e sem editar, para o topo de `01_CEO/rotina_fechamento_historico.md` (crie se não existir). Nada é apagado — só muda de arquivo.
4. Se o template já tiver só 2 rodadas + a lista consolidada, não mexa.

PASSO 3.5 — **[v1.1 — 30/09/2026] MEMÓRIA DAS ROTINAS** (`01_CEO/Rotinas_Evolucao/`, regras em `_mapa_das_rotinas.md`)
1. Carregue a tool de execuções: `ToolSearch` com `select:mcp__scheduled-tasks__list_task_runs,mcp__scheduled-tasks__list_scheduled_tasks`. Para cada tarefa listada na tabela do `_mapa_das_rotinas.md`, chame `list_task_runs` (limit 3) e pegue a execução de HOJE: começou?, status, duração (início → last_activity), resumo. Se a tool não carregar, use só os rastros do Passo 1 e escreva "duração: sem dado".
2. **Seção 2 (Diário de funcionamento)** de cada arquivo: acrescente 1 linha de hoje na tabela, inclusive "não rodou" e "encerrou no portão". O resultado sai do Passo 1 (o que produziu) — nunca deduza.
3. **Seção 3 (Candidatas a melhoria)**: olhe as últimas linhas do diário daquela rotina e acrescente uma candidata `(nova DD/MM)` só se o padrão aparecer de fato:
   - 3 dias úteis seguidos encerrando no portão/fila vazia;
   - duração 2× maior ou menor que a média das 5 anteriores;
   - o mesmo erro/bloqueio 2 vezes;
   - rodou fora do horário ou sessão aberta por horas;
   - Ensaio: mesma isca/tipo de erro em 2 etapas, ou etapa parada mais de 3 dias úteis aguardando Claudemberg.
   Cada candidata tem: o padrão, as datas que provam e o que você sugere. Candidata já listada → só acrescente a data nova, não duplique.
4. Não altere a seção 1 (Melhorias feitas) — ela só muda quando Claudemberg decide.

PASSO 4 — RELATÓRIO (curto): o que entrou na passagem, quantas rodadas foram para o histórico, o que não teve registro, candidatas novas.

NÃO FAÇA: gerar PDF, commit, push, criar ou editar Skill, acionar Gestor/Agente, mexer em `ensaio_003/`, aprovar/reprovar nada, alterar prompt de rotina. Na passagem, recomende à Diária só o que é papel dela (pesquisar e criar Skill) — o Ensaio roda antes dela e não é assunto da Diária.