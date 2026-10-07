---
name: rotina-fechamento-template
description: "Template de Fechamento de Rotina â€” preenchido ao fim de cada rodada, lido no inÃ­cio da prÃ³xima"
metadata:
  type: operacional
  lido_por: wallenberg-rotina-diaria-skills-v2, wallenberg-drenagem-continua-v2
  escrito_por: ambas rotinas
  frequencia: toda rodada (DiÃ¡ria: daily, Drenagem: 3x/semana)
---

# Fechamento de Rotina â€” Template ReutilizÃ¡vel

**Leia isto ao INÃCIO de cada rodada para saber:**
- O que foi feito na rodada anterior
- O que ficou pendente
- O que nÃ£o fazer (evitar retrabalho) â€” ver a seÃ§Ã£o consolidada no fim deste arquivo

**Preencha isto ao FIM de cada rodada para que a prÃ³xima saiba:**
- O que foi entregue
- O que ficou bloqueado e por quÃª
- O que tomar cuidado

**ManutenÃ§Ã£o [v1.0 â€” 30/09/2026]:** o Fechamento do Dia (20:00) mantÃ©m este arquivo com sÃ³ as 2 rodadas mais recentes + a seÃ§Ã£o consolidada "O QUE NÃƒO FAZER (acumulado)" no fim. Rodadas mais antigas vÃ£o, inteiras, para `01_CEO/rotina_fechamento_historico.md` â€” nada Ã© apagado.

---

## [2026-10-07] -- Diaria Skills v3.5.0 (Quarta) -- RODADA SEM SKILL NOVA (Pesquisa validou Skill existente)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** 07/10/2026, quarta-feira. DayOfWeek = Wednesday. Horário: 09:30-10:30 (60 min).
- [x] **Passo 0:** leitura de `_passagem_do_dia.md` (05/10), `rotina_fechamento_template.md` (bloqueadores) e `feed.jsonl`. Sem pendências críticas novas desde 06/10.
- [x] **Pesquisa seg-qui — 6 buscas, 2 por Gestor:**
  - **Kelsen:** (1) LICIN 2.0/Decreto 55.622/2025 validado (entrada 01/01/2025, Processo.Rio, 30 dias); (2) LC 198 varandas bloqueado (PDF corrompido no site da prefeitura).
  - **Lúcio:** (1) conforto térmico poente Zona Oeste — pesquisa genérica, sem vídeo achado; (2) busca de vídeo arquiteto brise — sem resultado YouTube específico.
  - **Cardozo:** (1) lençol freático Barra/Recreio — sem dados específicos da região; (2) contenção argila mole + hélice contínua — validado com fonte APL blog + literatura acadêmica.
- [x] **Checagem de coerência:** Cardozo/contenção argila mole JÁ COBERTO pela Skill `fundacoes-solos-moles-lencol-freatico-barra-recreio` v1.3 (ativa-com-ressalva, 01/10/2026, Rotina de Macetes). Tabela 3.1 compara hélice × escavada × pré-moldada. Macetes M1-M4 de Alonso (F1) já documentados. Coerência: 100%.
- [x] **Passo 3 (Feed):** nenhum evento. Pesquisa não gerou Skill nova, validou recobertura de lacuna existente.
- [ ] **Passo 4 (Fluxo de Ativação):** N/A (sem Skill).
- [ ] **Passo 8 (Trilha B):** não rodou. Nenhuma lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Não duplicar:** quarta-feira já confirma cobertura de `fundacoes-solos-moles-lencol-freatico-barra-recreio`.
- **Bloqueador: LC 198 varandas:** PDF fonte primária corrompido. Kelsen validará se usar varandas em caso real.
- **Bloqueador: /watch YouTube:** 2 buscas de vídeo sem resultado específico (Lúcio brises, Cardozo hélice). Bug do -vsync continua.
- **Continuam:** Hely (R2 levantamento cota soleira), Landell (RECON-BT), SELCA R1/R4/R7, varandas LC 198, NBR 13133, Ensaio 003 etapa 3.

---

## [2026-10-06] -- Diaria Skills v3.5.0 (Terca) -- RODADA COM SINAL DE CLAUDEMBERG (1 Skill proposta -- NBR 6492:2021)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** 06/10/2026, terca-feira. Inicio na sequencia da sessao de segunda.
- [x] **Sinal de Claudemberg:** lacuna real identificada -- gestores e equipes nao tem mapa formal de como entregar Memoriais e documentacoes por etapa, nem como estruturar aprovacoes de etapa. Pediu que "a inteligencia disso entre para a criacao de Skill".
- [x] **Pesquisa de fonte primaria:** NBR 6492:2021 localizada no acervo. Paginas 1-20 de 40 lidas via pypdf. Secoes 1-5.5 cobertas (LV-ARQ ate AP-ARQ inclusive).
- [x] **Skill criada:** `nbr6492-2021-memoriais-por-etapa-projeto` v1.0 -- proposta para Oscar/Lucio. Mapa de obrigatorio vs. opcional por etapa, conteudo de cada memorial, como usar nas aprovacoes de Gate. Status: proposta (secoes 5.6-5.8 nao lidas -- R1; aguarda validacao de Lucio).
- [x] **Decisao de escopo:** Skills analogas para outros Gestores (Kelsen, Cardozo, Villaca, Lele) ficam como item futuro da rotina. Cada Gestor pesquisa sua propria cadeia.
- [x] **Feed:** 1 evento `skill` registrado (06/10). Indice de Outubro atualizado (6a Skill de Outubro).
- [ ] **Passo 8 (Trilha B):** nao rodou -- nenhum `_estado_` trouxe lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: nao repita)

- **Nao duplicar:** `nbr6492-2021-memoriais-por-etapa-projeto` -- Skill criada 06/10.
- **R1 da nova Skill (Oscar/Lucio):** secoes 5.6-5.8 da NBR 6492:2021 (PE-ARQ, As Built) nao lidas. Confirmar antes de usar em Executivo real.
- **Validacao pendente:** Lucio precisa validar a Skill antes de ativar com ressalva.
- **Skills analogas para outros Gestores:** item de trabalho futuro da rotina (Passo 1 de cada Gestor). Nao criar agora.
- **Continuam valendo todos os itens de 05/10:** Hely (R2 levantamento), Landell (RECON-BT), SELCA R1/R4/R7, NBR 13133, bug do /watch (-vsync).

---
## [2026-10-05] â€” DiÃ¡ria Skills v3.5.0 (Segunda) â€” RODADA COMPLETA (2 Skills ativadas com ressalva + SELCA v1.2)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Monday. InÃ­cio Ã s 09:06. Pipeline seg-qui.
- [x] **Passo 0:** a `_passagem_do_dia.md` Ã© de **01/10**. NÃ£o existe passagem de 02/10: o Fechamento do Dia de sexta nÃ£o deixou passagem nova (registrar como falha a checar). Usei o bloco "O QUE NÃƒO FAZER" e a rodada de 02/10 do template. Ensaio 003: etapa 2 aguardando aprovaÃ§Ã£o de Claudemberg; sÃ³ leitura. Ãšltimo `status` do feed: 02/10.
- [x] **LÃºcio/Oscar, `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.1:** ativa-com-ressalva e instalada. Escolhida porque a etapa 3 do Ensaio Ã© o Levantamento (sugestÃ£o da anÃ¡lise de 02/10). Fonte primÃ¡ria: Decreto 55.622/2025 (PDF da SMDU, lido) e COE do acervo. LÃºcio corrigiu pÃ¡ginas, o PRPA e uma remissÃ£o falsa (as Skills de Kelsen **nÃ£o** tÃªm limite de cota de soleira).
- [x] **Cardozo/Landell, `entrada-energia-light-ligacao-nova-padrao-recon-bt-rj` v1.1:** ativa-com-ressalva e instalada. Fonte primÃ¡ria: FAQ oficial de LigaÃ§Ã£o Nova da Light + vÃ­deo oficial da Light. Cardozo fez 8 correÃ§Ãµes, entre elas o Grupo A por estudo entre 50 e 75 kW. Fim de 2 rodadas sem Skill de Cardozo.
- [x] **Kelsen:** sem Skill nova. As 2 buscas nÃ£o acharam lei nova da Barra/Recreio. Em vez disso, SELCA foi para a v1.2: R1 parcialmente fechada com a LC 140/2011 lida no Planalto; nova R7 (APA).
- [x] **CoerÃªncia:** remissÃµes de volta em `nbr5410-eletrica-automacao`, `habite-se-aceitacao-licin` e `fundacoes-solos-moles-...`. Nenhuma contradiÃ§Ã£o de valor.
- [x] **/watch:** vÃ­deo oficial da Light `2RG3FdAizUQ` assistido (transcriÃ§Ã£o Whisper/Groq + 15 quadros). O bug do `-vsync` continua: a extraÃ§Ã£o de quadros do script falhou e foi feita Ã  mÃ£o com ffmpeg. As legendas deram 429. As buscas de vÃ­deo para Kelsen e LÃºcio nÃ£o acharam vÃ­deo relevante.
- [x] **Feed:** 3 eventos, 3/3 OK. **Livro-razÃ£o:** entrada 05/10 em `Decisoes_Autonomas/2026/Outubro.md`, com "como desfazer". **Backups:** `_backups/2026-10-05/` (7 arquivos).
- [ ] **Passo 8 (Trilha B):** nÃ£o rodou; nenhuma lacuna de ferramenta nova trazida pelos Gestores.

### O QUE FICOU PENDENTE (Cuidado: nÃ£o repita)

- **NÃ£o duplicar:** levantamento topogrÃ¡fico/DULI (Skill de 05/10) e entrada de energia Light/RECON-BT (Skill de 05/10).
- **Hely (R2 do levantamento):** regra numÃ©rica de cota de soleira e de "terreno natural" na Barra/Recreio. Nenhuma Skill tem isso hoje.
- **Kelsen:** `habite-se-aceitacao-licin` linha 16 ("compara com o projeto aprovado") nÃ£o bate com o Art. 8Âº do Decreto 55.622. NÃ£o editado.
- **Landell:** RECON-BT 2024 (o download automÃ¡tico devolveu HTML; baixar Ã  mÃ£o) e carga instalada Ã— demandada no limite de 75 kW.
- **SELCA:** R1 falta a resoluÃ§Ã£o do CONEMA de impacto local; R4 falta a Lei Estadual 3.239/1999; R7, as APAs da Barra (esfera, plano de manejo, Ã³rgÃ£o gestor).
- **SugestÃ£o de compra nova:** NBR 13133:2021. Continua a da NBR 15575 partes 1, 4 e 5.
- **Continuam valendo:** Cobertura R1, contenÃ§Ã£o em argila mole (Cardozo), varandas, reservatÃ³rio, rebaixamento R1/R3, vidro R1/R2, bug do /watch.

---

## [2026-10-02] â€” DiÃ¡ria Skills v3.5.0 (Sexta) â€” FLUXO DE SEXTA (Passos 6, 9, 10; sem Skill nova)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Friday. InÃ­cio Ã s 09:06. Fluxo de sexta, sem pesquisa e sem Skill nova.
- [x] **Passo 0:** passagem de 01/10 lida. Ensaio 003 estÃ¡ na etapa 2/17 (Viabilidade), `aguardando_execucao`; sÃ³ leitura. O Ãºltimo `status` do feed era de 28/09.
- [x] **PendÃªncia Ã³rfÃ£ corrigida:** `hely-ferramentas-webfetch-websearch-semanal` era citada no livro-razÃ£o de 01/10, mas nÃ£o existia no `pendencias.json`. Agora estÃ¡ registrada (mÃ©dia, humano, pauta da Semanal). Backup em `_backups/2026-10-02/`.
- [x] **Passo 6 (Painel):** 3 eventos de marco: Ensaio 003 + Bardi (30/09), etapa 1 aprovada (01/10), etapa 2 criada (02/10). 3/3 OK.
- [ ] **Passo 7 (Learning Agent):** nÃ£o rodou. Ã‰ opcional e nÃ£o havia vÃ­deo novo na fila.
- [x] **Passo 9 (Dashboard):** evento `sistema` e evento `status` gravados por Ãºltimo, 2/2 OK. `painel_status.json` reescrito com contagem real: 19 membros (10 Auto, 4 Assisted, 1 Shadow, 4 FormaÃ§Ã£o; Bardi entrou), 3 de 5 Gestores Autonomous, pendÃªncias 50 de 58 fechadas (8 ativas: 1 crÃ­tica, 2 alta, 3 mÃ©dia, 2 baixa), 6 Skills na semana. `caso_real` e `marcos` mantidos, porque nÃ£o hÃ¡ evidÃªncia nova no livro-razÃ£o.
- [x] **Passo 10 (AnÃ¡lise):** abaixo.

### ANÃLISE DA SEMANA 28/09â€“02/10

- **ProduÃ§Ã£o:** 6 Skills (2 por Gestor), todas ativas com ressalva, 1 arquivada (LC 301) e macetes em 4 Skills. Ao todo, 45 instaladas.
- **Fraqueza principal:** sÃ£o 2 semanas seguidas com 0 Skill usada em caso real. O primeiro teste de verdade, a etapa 1 do Ensaio 003, obrigou o Kelsen a corrigir 4 Skills que jÃ¡ estavam "ativas" (OODC, Decreto 3046, varandas e habite-se). Achou erro de artigo (Art. 106 em vez de 110) e de documento. Isso mostra que "ativa com ressalva" nÃ£o quer dizer "certa". O Ensaio corrige mais do que a DiÃ¡ria produz.
- **Bloqueadores recorrentes:**
  - (1) NBR 15575 partes 1, 4 e 5 fora do acervo. Trava a ressalva de 3 Skills tÃ©rmicas. SugestÃ£o de compra.
  - (2) Hely sem WebFetch/WebSearch. DecisÃ£o da Semanal.
  - (3) Drive sem ferramenta de escrita de conteÃºdo. 3 correÃ§Ãµes esperam Claudemberg.
  - (4) `/watch` com 0 vÃ­deo assistido em 01/10. A busca nÃ£o achou vÃ­deo assistÃ­vel, e o bug de 403/429 continua.
- **PrÃ³ximas prioridades:**
  - (a) Etapa 2 do Ensaio. VillaÃ§a Ã© Assisted, mas MascarÃ³ e Fiker estÃ£o em FormaÃ§Ã£o, nunca examinados. Risco alto de reprovaÃ§Ã£o, porque Ã© a primeira vez da equipe.
  - (b) Segunda: Cardozo volta Ã  contenÃ§Ã£o em argila mole sÃ³ com fonte primÃ¡ria.
  - (c) Pauta da Semanal: ferramentas do Hely, compra da NBR 15575 e as correÃ§Ãµes de Drive. TambÃ©m a pendÃªncia Ã³rfÃ£ do `CLAUDE.md` (validaÃ§Ã£o de 31/07 nunca fechada).
- **SugestÃ£o (nÃ£o aplicada, para a Semanal):** a DiÃ¡ria poderia priorizar as Skills que a prÃ³xima etapa do Ensaio vai usar, em vez de criar Skill de tema novo. A etapa 3 Ã© o Levantamento, de LÃºcio.

### O QUE FICOU PENDENTE (Cuidado: nÃ£o repita)

- Tudo que estava em 01/10 continua valendo: SELCA R1/R4, Cobertura R1, contenÃ§Ã£o (Cardozo), varandas, reservatÃ³rio, rebaixamento R1/R3, vidro R1/R2 e o bug do /watch.

---

## [2026-10-01] â€” DiÃ¡ria Skills v3.5.0 (Quinta) â€” RODADA COMPLETA (2 Skills ativadas com ressalva)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Thursday. InÃ­cio Ã s 09:07. Pipeline seg-qui.
- [x] **Passo 0:** `_passagem_do_dia.md` de 30/09 lido; a v1.0 da passagem foi lida corretamente. Prioridade zero conferida: a etapa 1 do Ensaio 003 (legal_base) **jÃ¡ foi criada hoje pelo Bardi** e estÃ¡ com status `aguardando_execucao`, pronta para a Drenagem. SÃ³ leitura, nada tocado. O Ãºltimo evento `status` do feed Ã© de 28/09.
- [x] **Kelsen/Hely, `selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj` v1.1:** ativa-com-ressalva e instalada. Fecha a pendÃªncia SELCA de 29/09. O texto integral do DOERJ foi lido (pypdf). Kelsen fez 6 correÃ§Ãµes factuais; ressalvas R1 a R5. Primeira Skill nova de Kelsen desde 25/09.
- [x] **LÃºcio/Oscar, `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj` v1.1:** ativa-com-ressalva e instalada. Fecha o "U cobertura â‰¤ x" aberto na Skill da NBR 15575-4. LÃºcio corrigiu o Â§4 (IPT), limitou a brecha do FT e retirou 2 macetes sem fonte.
- [x] **CoerÃªncia:** remissÃµes de volta em 5 Skills (legal-base, rebaixamento, nbr15575-4, nbr15220-3, nbr9575). Backups em `_backups/2026-10-01/` (5 arquivos). Sem contradiÃ§Ã£o de valor.
- [x] **Cardozo:** sem Skill (contenÃ§Ã£o/NBR 9061 sem fonte primÃ¡ria).
- [x] **Feed:** 2 eventos, 2/2 OK. **Livro-razÃ£o:** `Decisoes_Autonomas/2026/Outubro.md` criado, com "como desfazer".
- [~] **/watch:** as 3 buscas de vÃ­deo (uma por Gestor) nÃ£o acharam URL de vÃ­deo assistÃ­vel sobre os eixos. SÃ³ apareceram artigos e uma matÃ©ria que cita um vÃ­deo (Talita Catelani), sem link. Nada assistido nesta rodada.
- [ ] **Passo 8 (Trilha B):** nÃ£o rodou, porque nenhum `_estado_` trouxe lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: nÃ£o repita)

- **SELCA, R1:** competÃªncia SMAC Ã— INEA (LC 140/2011, Art. 9Âº, XIV, e a resoluÃ§Ã£o do CONEMA sobre impacto local). Kelsen achou tambÃ©m que lote com APP ou Ã¡rea alagadiÃ§a sai da LMS e vai para LMP+LMI, ainda municipal (Dec. 51.503/2022, Art. 27, parÃ¡grafo Ãºnico). Dono: Hely.
- **SELCA, R4:** lei estadual de outorga (Lei 3.239/1999, a confirmar) nÃ£o lida. Dono: Hely.
- **Cobertura, R1:** confirmar a Tabela 5 e o FT no texto publicado da NBR 15575-5:2021 (norma paga, fora do acervo). **SugestÃ£o de compra:** NBR 15575 partes 1, 4 e 5, recorrentes em 3 Skills tÃ©rmicas.
- **Cardozo, candidata:** contenÃ§Ã£o de escavaÃ§Ã£o em argila mole (NBR 9061 / cortina / estaca-prancha). SÃ³ criar com fonte primÃ¡ria ou fonte tÃ©cnica de profissional lida.
- **Continuam valendo:** varandas (3 lacunas, Kelsen); reservatÃ³rio (reuso voluntÃ¡rio, Kelsen); rebaixamento R1/R3 (Hely); vidro R1/R2 (LÃºcio); bug do /watch (`-vsync`).

---

## [2026-09-29] â€” DiÃ¡ria Skills v3.4.0 (TerÃ§a) â€” RODADA COMPLETA (2 Skills ativadas, 4 treinos OK)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Tuesday. InÃ­cio Ã s 08:14. Pipeline seg-qui.
- [x] **Passo 0.5, treinos atrasados:** as 2 Skills de 28/09 foram treinadas, ambas OK. ReservatÃ³rio (Saturnino): v1.2 com 4 esclarecimentos. Varandas (Hely): as 3 lacunas da Skill ficam pendentes com Kelsen (ver abaixo).
- [x] **Cardozo/Baumgart, `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` v1.2:** ativa-com-ressalva e instalada. Fonte primÃ¡ria: Lei 5.234/2008 (ALERJ). Cardozo: PROCEDE COM RESSALVA, com v1.1 e correÃ§Ãµes tÃ©cnicas. Treino do Baumgart OK (7 de 7 iscas).
- [x] **LÃºcio/Oscar, `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj` v1.2:** ativa-com-ressalva e instalada. Fecha a lacuna de vidro de 28/09. Fonte primÃ¡ria: Portaria Inmetro 309/2022, Anexo II. LÃºcio: PROCEDE COM RESSALVA e corrigiu uma contradiÃ§Ã£o com a Skill de proteÃ§Ã£o solar (no poente, sombreamento vertical). Treino do Oscar OK (6 de 6 iscas).
- [x] **CoerÃªncia v3.4.0:** remissÃµes de volta gravadas na Skill de fundaÃ§Ãµes da Barra (linha 129) e na de proteÃ§Ã£o solar (seÃ§Ã£o 6).
- [x] **Kelsen:** sem Skill. A busca achou a LC 299/2026 (MCMV, fora do perfil STTK) e o Decreto Estadual 50.473/2026 (SELCA, ver pendÃªncia).
- [x] **/watch:** vÃ­deo jXFca_Az9f8 (ponteiras filtrantes), aproveitado sÃ³ pela transcriÃ§Ã£o. O download do vÃ­deo deu 403 e as legendas vieram na 2Âª tentativa (a 1Âª deu 429). As buscas de vÃ­deo para Kelsen e LÃºcio nÃ£o acharam material relevante.
- [x] **Feed:** 2 eventos, 2/2 OK. **Livro-razÃ£o:** entrada 29/09 mais adendo. **Backups:** `_backups/2026-09-29/` (8 arquivos).
- [ ] **Passo 8 (Trilha B):** nÃ£o rodou, porque nenhum `_estado_` trouxe lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: nÃ£o repita)

- **Varandas (Kelsen), 3 lacunas do treino:** como lanÃ§ar no projeto uma varanda que jÃ¡ nasce com vidro retrÃ¡til (COES caput e Â§10, LC 145/2014); se casas geminadas contam como uma edificaÃ§Ã£o para os 5 m e para o Â§3Âº; varanda gourmet como cÃ´modo disfarÃ§ado. SÃ³ editar a Skill depois de ler o texto.
- **ReservatÃ³rio:** reuso voluntÃ¡rio de unifamiliar sob os Arts. 3Âº a 9Âº da Res. Conj. (Kelsen).
- **Rebaixamento, Hely:** R1, confirmar na INEA 63/2012 ou na CERHI 221/2020 que os 5.000 L/dia valem como dispensa de **outorga** (a Lei 5.234 Ã© de cobranÃ§a); R3, qual Ã³rgÃ£o autoriza o lanÃ§amento na rede pluvial municipal.
- **Vidro, LÃºcio:** R1, confirmar 0,87 / 5,70 / 17% na NBR 15575-1 Â§11.4.7.2; R2, zona da INI-R para o Rio depois da NBR 15220-3:2024.
- **SELCA, Decreto Estadual 50.473 de 15/09/2026 (novo licenciamento ambiental do RJ):** Hely verifica o que muda para obra residencial perto de lagoa na Barra/Recreio.
- **Cardozo, fora do escopo:** a `nbr6122-2019-fundacoes` remete escavaÃ§Ã£o Ã  NBR 11682 (encostas); a candidata certa pode ser a NBR 9061, a confirmar.
- **Formato dos treinos:** 4 de 4 Agentes passaram das 15 linhas. Cardozo e LÃºcio vÃ£o cobrar isso como padrÃ£o.
- **Continuam valendo:** Skill de partido de 16/09 (linhas 70-72, os 20% do Â§5Âº), que o LÃºcio confirmou; bug do `/watch` (`-vsync`, 429/403); pendÃªncias de Lint de 25/09.

---

## O QUE NÃƒO FAZER (acumulado)

Consolidado em 30/09/2026 a partir de todas as rodadas de 01/09 a 29/09 (movidas para `01_CEO/rotina_fechamento_historico.md`). Itens jÃ¡ resolvidos/superados por rodada mais nova nÃ£o aparecem de novo â€” quem quiser o detalhe completo lÃª o histÃ³rico.

**Kelsen (Legal):**
- LC 301/2026 (AEIU PraÃ§a Onze, cadeia de 30%, Art. 64) â€” nÃ£o crie Skill nova; coberta e corrigida nas Skills de 18/09 v1.1, 23/09 e 24/09 (Art. 64 fechado: Ã© LC 229, fora da AP4).
- Decreto 3046/81 + LC 270/2024 LICIN Barra/Recreio â€” nÃ£o duplique; Skill de 21/09 (ratificada).
- Varanda nÃ£o computÃ¡vel (COES Art. 8Âº) â€” nÃ£o duplique; Skill de 28/09 v1.1.
- OODC/Mais-ValerÃ¡/Mais-Valia â€” nÃ£o duplique; Skill de 15/09 v1.1.
- NBR 5419:2001 (SPDA) â€” nÃ£o use como base; obsoleta, use a NBR 5419:2026 (Skill de 15/09).
- LC 291/2025 â€” nÃ£o crie Skill separada; coberta como histÃ³rico na Skill LC 301.
- Regime de Licenciamento de Portugal (out/2026) â€” fora de escopo, nÃ£o Ã© RJ.
- SELCA / Decreto Estadual 50.473/2026 â€” nÃ£o duplique; Skill de 01/10 v1.1.

**LÃºcio â€” cobertura:**
- Ucob, absortÃ¢ncia de telha, Ã¡tico ventilado e FT (NBR 15575-5) â€” nÃ£o duplique; Skill de 01/10 v1.1.

**LÃºcio (Arquitetura):**
- VentilaÃ§Ã£o cruzada / fachada poente / vidro de controle solar â€” nÃ£o duplique sem parÃ¢metro numÃ©rico real; coberta por Partido (16/09), ProteÃ§Ã£o Solar (17/09, v1.1â†’v1.3) e Vidro/INI-R (29/09 v1.2).
- COE LC 198/2019 ventilaÃ§Ã£o/iluminaÃ§Ã£o/pÃ©-direito â€” nÃ£o duplique; Skill de 21/09.
- NBR 15575-4 Emenda 2025 (desempenho tÃ©rmico) â€” nÃ£o duplique; Skill de 22/09.
- TDC/LICIN 2.0 e Partido/Conforto TÃ©rmico â€” nÃ£o duplique; Skills de 16/09.
- NBR 9050:2020 (acessibilidade) â€” nÃ£o duplique; Skill de 15/09 v1.1.

**Cardozo/Complementares (Baumgart, Saturnino, Landell, Tenreiro, Glaziou, Mindlin):**
- Rebaixamento de lenÃ§ol / outorga INEA de obra â€” nÃ£o duplique; Skill Baumgart de 29/09 v1.2.
- NBR 6484:2020 / sondagem SPT â€” nÃ£o crie Skill separada; coberta pela Skill de fundaÃ§Ãµes Barra/Recreio v1.1.
- FundaÃ§Ãµes em solos moles Barra/Recreio â€” nÃ£o duplique; Skill Baumgart de 21/09.
- ReservatÃ³rio de retardo (Dec. 23.940) â€” nÃ£o duplique; Skill Saturnino de 28/09 v1.1.
- NBR 6122:2022 (fundaÃ§Ãµes) â€” nÃ£o duplique; Skill de 07/09.
- NBR 6120:2019 (cargas) â€” nÃ£o duplique; Skill de 08/09.
- NBR 8681:2025 (seguranÃ§a/fatores) â€” nÃ£o duplique; Skill de 09/09.
- NBR 10844:1989 (Ã¡guas pluviais) â€” nÃ£o duplique; Skill de 10/09.
- NBR 9575:2024 (impermeabilizaÃ§Ã£o) â€” nÃ£o duplique; Skill de 02/09.
- NBR 5410 (elÃ©trica) â€” nÃ£o duplique; Skill de 28/08.
- NBR 14565:2019 (cabeamento estruturado) â€” nÃ£o duplique; Skill Landell de 23/09.
- COSCIP/CBMERJ Decreto 42/2018 â€” nÃ£o duplique; Skill de 04/09 v1.1.
- ResoluÃ§Ã£o SMDU 10/2026 (RDT) â€” nÃ£o duplique; Skill de 03/09.
- NBR 15575:2025 (desempenho acÃºstico de pisos) â€” nÃ£o duplique; Skill de 03/09.
- NBR 15220-3:2024 (zoneamento bioclimÃ¡tico) â€” nÃ£o duplique; Skill de 01/09.
- NBR 7229:1993, NBR 13969:1997, NBR 10521:1988 â€” nÃ£o crie Skill separada; substituÃ­das pela NBR 17076:2024.
- IluminaÃ§Ã£o de interiores NBR ISO/CIE 8995-1 â€” nÃ£o duplique; Skill Tenreiro de 18/09.
- RemoÃ§Ã£o de Ã¡rvores FPJ/SMAC â€” nÃ£o duplique; Skill Glaziou de 18/09.
- EspÃ©cies nativas da Mata AtlÃ¢ntica â€” nÃ£o duplique; Skill Glaziou de 22/09.
- APA Barra (condicionantes por lote) â€” nÃ£o tente de novo; dados pÃºblicos insuficientes (confirmado 22/09).
- ProteÃ§Ã£o Solar Externa (brises/cobogÃ³/venezianas) â€” nÃ£o duplique; Skill LÃºcio/Oscar de 17/09 (v1.1â†’v1.3).
- Memorial Descritivo/ApresentaÃ§Ã£o TÃ©cnica (Mindlin) â€” nÃ£o duplique; Skill de 16/09.

**Ferramentas/Vitruvius (padrÃ£o vigente: tudo fica dentro do Revit):**
- PyNite, anaStruct, StructPy, CBE Clima Tool, EasyEletric, PyFlo/pipedream, open-garden-planner, Blueprint3d â€” nÃ£o proponha; standalone, nÃ£o integram Revit.
- RevitCortex 173, BIMwright/rvt-mcp 229, UV-Tech/revit-claude-mcp 40, LuDattilo/revit-mcp-server 138, IbrahimFahdah/revit-claude-mcp 46, Simone-Balin/Sam-AEC 100+ â€” nÃ£o crie Skill isolada; jÃ¡ registrados em `vitruvius_achados`.
- pyRevit-MCP, mcp-servers-for-revit, Autodesk APS Sample MCP Server â€” nÃ£o crie Skill; pago ou arquivado/inativo.
- Luw.ai, Remodel AI, Redraw, Leonardo AI, Modly â€” nÃ£o crie Skill; cloud (vazamento de dados) ou foco errado.
- Blender MCP, Architecture MCP (sceneview-tools) â€” nÃ£o pesquise/proponha de novo; jÃ¡ coberto (01/08) ou retorna 404.
- ApresentaÃ§Ã£o interativa ao cliente â€” busca PAUSADA; sÃ³ retomar quando um caso real forÃ§ar a decisÃ£o.

**VÃ­deos jÃ¡ assistidos via /watch (nÃ£o repetir):**
- jXFca_Az9f8, Z0buYmS8fDE, 0-QDPnEIkvw, VUCChmNYpKU â€” conteÃºdo jÃ¡ extraÃ­do, sem novidade em reassistir.

**Painel/Sistema:**
- `painel_fundador_sttk.html` â€” nÃ£o editar atÃ© Claudemberg resolver o conflito do span `id="updated"` travado.

---

**Ãšltima atualizaÃ§Ã£o:** 01/10/2026 (Fechamento do Dia v1.0 â€” rodada de 28/09 movida para `rotina_fechamento_historico.md`; template de volta a 2 rodadas + consolidado)
**PrÃ³xima leitura:** 02/10/2026 (sexta-feira) â€” DiÃ¡ria Skills fluxo de sexta (Passos 6-10)
