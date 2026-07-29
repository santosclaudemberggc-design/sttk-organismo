---
name: sttickler-rotina-diaria-skills
description: "Rotina automática diária (08:00, todo dia) do Wallenberg — motor Cérebro + Criador de Skills; propostas aprovadas na Reunião Mensal"
metadata: 
  node_type: memory
  type: project
  originSessionId: e81aacdf-a49f-4bd0-8b27-e5782bb435ee
  modified: 2026-07-20T11:31:09.125Z
---

Decisão de Claudemberg em 15/07/2026: o Wallenberg passa a ter uma **rotina automática fixa**, rodando **todo dia às 08:00** (7 dias/semana), que é o motor diário das Funções 3 (Cérebro) e 5 (Criador de Skills).

**O que a rotina faz, toda manhã:**
1. Pesquisa **Skills novas** e consolida o que encontrar.
2. Varre **mercado, CAU, CREA, e sites de grandes empresas** (Brasil e exterior) para ver como cada uma está performando.
3. Com o conhecimento adquirido, **redige Skills novas para os Gestores**.

**Governança (o ponto central desta decisão):** as Skills produzidas ficam como **proposta acumulada** — NÃO entram para o Gestor na hora. Elas são apresentadas e aprovadas por Claudemberg na **Reunião Mensal ao Conselho** (Função 7), não na Semanal. Isso ajusta como a regra de ouro se aplica às Skills: é o mesmo padrão de autonomia com prestação de contas do [[sttickler-ceo-wallenberg]] (Princípio 13) — Wallenberg produz sozinho o operacional (pesquisar/redigir), mas a decisão estrutural (Skill virar oficial) continua sendo de Claudemberg, consolidada mensalmente.

**Onde salva:** rascunhos em `01_CEO/Skills_Propostas/{Ano}/{Mês}/`, cada Skill num arquivo com a fonte da pesquisa junto, mais um índice mensal que alimenta a Reunião Mensal. Cada `.md` tem PDF correspondente ([[feedback-pdf-junto-com-md]]).

**Detalhe técnico:** tarefa automática local (`create_scheduled_task`, id `wallenberg-rotina-diaria-skills`, cron `0 8 * * *`). Só roda com o app aberto no horário; se fechado, roda no próximo lançamento. Não é alarme garantido.

**Princípios aplicáveis:** 3 (Qualidade), 5 (Delegação), 6 (Melhoria contínua), 8 (Rastreabilidade), 13 (Autonomia com prestação de contas), 17 (Aprendizado compartilhado), 20 (Revisão periódica).

---

**SEGUNDA ROTINA — Reunião Semanal (decisão de Claudemberg em 20/07/2026):** "a Reunião Semanal deve virar rotina". Criada a tarefa automática `wallenberg-reuniao-semanal`, cron `30 10 * * 1` (toda **segunda às 10:30**, Função 9). Mesma limitação técnica: só roda com o app aberto; se fechado, roda no próximo lançamento.

**O que ela faz:** lê todos os Registros Diários desde a segunda anterior, consolida (sem sobrescrever) a pauta em `04_REUNIOES_SEMANAIS/{AAAA-MM-DD}_pauta.md`, e monta os itens que precisam da decisão de Claudemberg — Gestores novos propostos/aprovados (nome + 3 camadas + equipe), Skills a formalizar, encaminhamentos estruturais de semanas anteriores ainda não decididos (carregados adiante até serem resolvidos), e travas que dependem dele. Gera PDF.

**Divisão dos três níveis (ver [[feedback-tres-niveis-reuniao]]):** Diário = travas/aprovações graves; **Semanal = decidir o que vamos FAZER, e a ÚNICA instância de decisão estrutural** (exceto via de urgência dos Gates 13/16); Mensal = consolidado ao Conselho. Agentes contratados por um Gestor sob autonomia delegada NÃO entram na Semanal — vão pra Mensal. Nada é aprovado por silêncio: se Claudemberg não estiver presente, a pauta fica aguardando decisão dele.
