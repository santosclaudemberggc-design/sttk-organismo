# Livro-razão de Decisões Autônomas — Outubro/2026

## 06/10/2026 — Lúcio: Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.2 → v1.3 (pós-reprovação da v2 da Etapa 03 por extensão)
**O quê:** §5-bis ganhou 1 item: conferência de forma e extensão contra o enunciado (limite de páginas, contado; conclusão primeiro; contas em anexo citado por número; matriz uma linha por decisão). Aplicado em `.claude/skills/.../SKILL.md` e na cópia de `Skills_Propostas/2026/Outubro/`, índice atualizado.
**Por quê:** parecer_bardi_v2 (item 2 do "O que corrigir"); Claudemberg reprovou a v2 só pela extensão.
**Como desfazer:** backup `01_CEO/Decisoes_Autonomas/_backups/2026-10-06/levantamento-topografico-cadastral-orientado-duli-licin-rj_SKILL_v1.2_ANTES_v1.3.md` (apagar o item novo e o changelog v1.3, voltar version para v1.2).

## 06/10/2026 — Lúcio: Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.1 → v1.2 (pós-reprovação Ensaio 003 Etapa 03)

**O que foi feito:** checklist §5-bis de fechamento do relatório de Levantamento (toda área não computável com conta contra computável e programa; "cabe" sempre com condições; premissa conservadora vira regra com número + linha na matriz; todo pedido do cliente respondido com conflito Legal × cliente explícito; tabela pergunta × seção; NBR 6492 5.1.2; ler enunciados de todas as etapas anteriores). §5 curvas a cada 1 m (NBR 6492 5.1.1 b — antes deixava o intervalo ao topógrafo, em tensão com a Skill `nbr6492-2021-memoriais-por-etapa-projeto`). §7: varandas Diferente → Complementa.
**Coerência:** só remissões a Skills existentes (nbr6492-memoriais §2, varandas §4.1); nenhum limite legal novo; Art. 350 III citado como premissa do parecer Legal aprovado.
**Arquivos:** `.claude/skills/.../SKILL.md`; `Skills_Propostas/2026/Outubro/lucio_levantamento-...md`; `indice.md`. Espelho `.agents/skills/` NÃO atualizado (pendência já aberta).
**Como desfazer:** backup `01_CEO/Decisoes_Autonomas/_backups/2026-10-06/levantamento-topografico-cadastral-orientado-duli-licin-rj_SKILL_ANTES.md`. Também: o "crédito R$ 3 mi sem fonte" (pendência desta data) é alarme falso — fonte 5.14 do enunciado da Etapa 02; pendência pode ser fechada por Wallenberg.

## 06/10/2026 — Wallenberg, Drenagem Contínua v2.5.0: Ensaio 003 etapa 3 executada e corrigida

**O que foi feito:** Lúcio acionado (único Gestor com fila: etapa 3 do Ensaio + Skill proposta nova). Lúcio acionou Oscar; entrega em `01_CEO/Casos_TESTE/ensaio_003/etapa_03_levantamento/entrega/` (4 arquivos). Lacre conferido antes da correção (SHA256 `3F55C997…180C3` = histórico). Bardi corrigiu: recomenda **REPROVAR** (isca 2 inteira; iscas 1, 3, 4 parciais — falta conta de vagas cobertas × 457,44 m² computáveis, efeito da varanda no envelope sem linha na matriz, argumento do cliente sobre a edícula sem resposta). Bardi também registrou 3 erros do próprio gabarito no parecer, sem reescrevê-lo.
**Incidente:** busca do Lúcio listou os nomes dos arquivos de `_gabaritos_LACRADO` (sem conteúdo). Bardi: não compromete. Virou pendência `ensaio-gabarito-fora-da-pasta-06-10-2026` (decisão de Claudemberg).
**Arquivos alterados:** `_estado_ensaio_003.json` (→ `aguardando_aprovacao` / `aguardar_claudemberg`, histórico += executada_e_corrigida); `pendencias.json` (+3 itens: gabarito fora da pasta; crédito R$ 3 mi sem fonte na v9 do Villaça; aviso ao Cardozo + espelho `.agents/`); `feed.jsonl` (+2 eventos: marco do Ensaio, skill NBR 6492).
**Como desfazer:** reverter o commit local desta rodada (`git revert`); o estado do ensaio volta para `executar`.

## 06/10/2026 — Lúcio (Arquitetura), Drenagem Contínua: Skill `nbr6492-2021-memoriais-por-etapa-projeto` ATIVA-COM-RESSALVA + harmonização

**Decisão (alçada de Gestor dono):** v1.0 (proposta da Diária de hoje) → v1.1 `ativa-com-ressalva`, instalada em `.claude/skills/nbr6492-2021-memoriais-por-etapa-projeto/SKILL.md`; cópia em `Skills_Propostas/2026/Outubro/` e `indice.md` atualizados.
**Conferência no primário:** NBR 6492:2021 do acervo (`D:\008_Normas ABNT\001_ABNT\04_Desenho_Tecnico\`), capa, sumário, prefácio, Seções 1-3 e Seção 5 inteira (pp. 6-11). Erros corrigidos: título da norma; R1 da v1.0 (dizia 5.6-5.8 não lidas "pp. 21-40" — estão nas pp. 10-11); EV-ARQ confundido com pré-estudo financeiro; condição inventada para o memorial do EP; jogo do AP incompleto; LV sem ambientais/marés/fotos; As Built com itens que não são da norma; Gate atribuído ao Artigas e REGRA-ARQ-01 citada fora de contexto.
**Contradição encontrada (Grep em `.claude/skills/`):** `nbr6492-representacao-grafica` (Cardozo/Mindlin) dizia que a NBR 6492 "só define COMO representar, não O QUE incluir" — contraria a Seção 1 da norma. Classificação: **complementa** (mesma norma, Seção 4/Anexo A × Seção 5). Harmonizado: linha corrigida na Skill do Cardozo com nota de origem. Backups: `_backups/2026-10-06/nbr6492-representacao-grafica_SKILL_ANTES.md` (integral) e `..._memoriais-por-etapa-projeto_v1.0_ANTES.md` (frontmatter integral + resumo; texto integral no commit 2ee07aa).
**Como desfazer:** restaurar a Skill do Cardozo pelo backup; restaurar a v1.0 pelo git (2ee07aa) e apagar a pasta da Skill instalada.
**Pendências:** Cardozo ciente da edição na Skill dele (via Wallenberg). Espelho `.agents/skills/nbr6492-representacao-grafica/SKILL.md` (não versionado) ainda com a frase antiga — não editei, governança do espelho desconhecida. Não aplicada ao Ensaio 003 etapa 3 (validada depois e separadamente).
**Registrador:** Lúcio.

---

## 05/10/2026 — Reunião Semanal v2.0 (seg, 17:00) — RATIFICAÇÕES EM BLOCO

**Contexto:** Pauta `2026-10-05_pauta.md` apresentada. Claudemberg ratificou via asserção direta sobre assertividade de Skills.

**RATIFICADO — 3 itens:**
1. ✅ R1: Rotina Acervo de Normas v1.2 (05/10) — levantamento P1+P2+P3+P4, índice expandido 6→25 normas, 3 itens críticos em `pendencias.json`
2. ✅ R2: Rotina Macetes de Profissionais v1.2 (05/10) — 2 macetes Cardozo/NBR 6122 v1.3 (Falconi/Votorantim)
3. ✅ R3: Rotina Diária Skills v3.5.0 (05/10) — 2 Skills ativadas (Lúcio/Levantamento, Landell/Entrada Light)

**DECIDIDO — 2 itens:**
- ✅ **D1a:** Aplicar regra permanente — arquivo temporário em `_tmp/` (gitignore), nunca na raiz. Detectação no Fechamento do Dia via Glob. Efetivo imediato: atualizar `.gitignore`, POPs de Agentes, rotinas de limpeza.
- ✅ **D2a:** Autorizar trim de `_estado_kelsen.md` + `_estado_hely.md` — represado 3 semanas (14/09 Claudemberg sinalizou). Contexto sobe 48,9% vs. baseline; trim comprovado zero perda de histórico. Início 07/10 (próxima segunda).

**Status:** ✅ COMPLETO. Pauta 2026-10-05_pauta.md marcada "Ratificado Claudemberg 05/10/2026".

**Registrador:** Wallenberg  
**Ratificador:** Claudemberg (CEO)  
**Data Ratificação:** 05/10/2026, 17:30 UTC

---

## 05/10/2026 — Rotina Macetes de Profissionais v1.2 (seg, 14:00)

- **O que decidiu:** acrescentar 2 macetes (M1 + M2) à Skill `nbr6122-2019-fundacoes` (Cardozo/Baumgart), elevando de v1.2 para v1.3. Fontes: Sinduscon-Rio, webinar sobre revisão NBR 6122 — Frederico Falconi (coord. revisão, USP) e Fernando Holanda (Votorantim Cimentos).
- **Por quê:** Skill selecionada por prioridade 1 (sem seção "Macetes de quem faz"). Pesquisa trouxe fontes tipo A + B verificáveis. Cardozo confirmou que nenhum macete contradiz a norma.
- **O que alterou:**
  1. `.claude\skills\nbr6122-2019-fundacoes\SKILL.md` — versão v1.2→v1.3; seção "Macetes de quem faz" (M1 + M2) adicionada.
  2. `01_CEO\Skills_Propostas\2026\Setembro\baumgart_nbr6122-2022-emenda1-fundacoes-projeto-execucao.md` — Versao v1.0→v1.1; seção "## 11. Macetes de Quem Faz" adicionada.
  3. `01_CEO\Skills_Propostas\_macetes_fila.md` — 3 novas linhas no histórico; Próximas da fila atualizada.
  4. `01_CEO\Decisoes_Autonomas\_backups\2026-10-05\cardozo_ANTES_nbr6122-2019-fundacoes_SKILL.md` — backup criado.
  5. `03_REGISTROS_DIARIOS\2026\10\2026-10-05.md` — entrada adicionada.
  6. `01_CEO\Painel_Fundador\feed.jsonl` — evento skill/Cardozo adicionado.
- **Rodadas sem macete:** Kelsen (`legal-oodc-mais-valera-mais-valia`) — 1ª rodada (tipo C, 3 fontes sem OAB). Lúcio (`levantamento-topografico-cadastral-orientado-duli-licin-rj`) — 1ª rodada (tipos A+B, 4 fontes sem autor CREA para DULI/LICIN). Ambas retornam na próxima semana.
- **Bloqueios:** Machado Meyer retornou 403. Legalizzar e N Partners sem autor com OAB identificado. NBR 13133 não comprada (acervo).
- **Como desfazer:**
  1. Restaurar backup: `01_CEO\Decisoes_Autonomas\_backups\2026-10-05\cardozo_ANTES_nbr6122-2019-fundacoes_SKILL.md` → `.claude\skills\nbr6122-2019-fundacoes\SKILL.md`.
  2. Reverter versão no espelho `Skills_Propostas\2026\Setembro\baumgart_nbr6122...md` manualmente (remover seção 11 e ajustar Versao para v1.0).
  3. Remover as 3 linhas de 05/10 do histórico do `_macetes_fila.md`.
  4. Remover evento do `feed.jsonl`.

---

## 05/10/2026 — Rotina Acervo de Normas v1.2 (seg, 1ª do mês — modo COMPLETO)

- **O que decidiu:** atualizar o índice do acervo `D:\008_Normas ABNT\_indice_acervo.md` com todas as normas levantadas no modo COMPLETO (P1+P2+P3+P4) e criar 3 itens de pendência no `pendencias.json`.
- **Por quê:** modo COMPLETO (dia 5 ≤ 7). P1 (Bardi): 2 normas apontadas como "fonte primária não verificada" no parecer v7 da etapa 2. P4: 22 normas adicionais mapeadas nas Skills ativas e ausentes do acervo.
- **O que alterou:**
  1. `D:\008_Normas ABNT\_indice_acervo.md` — índice expandido: coluna "Etapa Ensaio" adicionada; lista de compra atualizada de 6 para 25 itens com tabela de urgência (3 normas travando o Ensaio no topo).
  2. `01_CEO\Pendencias\pendencias.json` — 3 novos itens abertos adicionados (alçada humana, compra requer Claudemberg): `acervo-compra-normas-ensaio-etapa2`, `acervo-compra-normas-ensaio-etapa3`, `acervo-normas-compra-geral-05-10-2026`.
  3. `03_REGISTROS_DIARIOS\2026\10\2026-10-05.md` — entrada adicionada.
- **Bloqueios:** nenhum. Raiz de `D:\008_Normas ABNT\` limpa (zero arquivo solto). Nenhuma norma gratuita e oficial identificada para download imediato.
- **Como desfazer:**
  1. Restaurar `_indice_acervo.md` da versão anterior via `git checkout` (último commit antes desta rotina).
  2. Remover os 3 itens adicionados ao `pendencias.json` (ids: `acervo-compra-normas-ensaio-etapa2`, `acervo-compra-normas-ensaio-etapa3`, `acervo-normas-compra-geral-05-10-2026`).
  3. Editar `2026-10-05.md` removendo o bloco da rotina de acervo.

---

## 01/10/2026 — Rotina Diária Skills v3.5.0 (qui, 09:07) — 2 Skills novas ativadas com ressalva

**1. Skill `selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj` (Kelsen/Hely), v1.1, ativa-com-ressalva.**
- **O que decidiu:** criar e ativar a Skill do novo SELCA (Decreto Estadual 50.473/2026). A versão é a v1.1, já corrigida por Kelsen.
- **Por quê:** fecha a pendência aberta em 29/09 ("SELCA: o que muda para obra residencial perto de lagoa", dono Hely). Kelsen estava sem Skill nova desde 25/09. O texto integral do DOERJ foi extraído com pypdf e lido. Kelsen conferiu artigo por artigo, fez 6 correções factuais e deu PROCEDE COM RESSALVA. Ressalvas: R1, competência SMAC × INEA (LC 140) não lida; R2, prazos antigos só da nota Mayer Brown; R3, a seção 8 é tese e só entra em caso real depois do Gate do Maurício; R4, a lei de outorga não foi lida; R5, as normas operacionais do INEA não foram lidas. Wallenberg retirou a R6 (treino em caso fictício), porque o treino foi extinto na v3.5.0.
- **O que alterou:** `01_CEO/Skills_Propostas/2026/Outubro/kelsen_selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj.md` (novo); `.claude/skills/selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj/SKILL.md` (novo); remissões de volta em `.claude/skills/legal-base-legislativa-bairro/SKILL.md` (1 linha nova no fim da seção LMS) e em `.claude/skills/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio/SKILL.md` (ressalva 6, linha da tabela e linha de fonte: o SELCA agora consta como conferido no texto primário). Sem mudança de regra nas duas.
- **Backup:** `_backups/2026-10-01/legal-base-legislativa-bairro__SKILL.md` e `_backups/2026-10-01/rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio__SKILL.md`.
- **Como desfazer:**
  1. Apague a pasta `.claude/skills/selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj/`.
  2. Restaure os 2 backups sobre os `SKILL.md` originais.
  3. Volte o `Status` do `.md` em `Skills_Propostas` para `proposta` ou mova-o para `_Arquivadas/2026/`.
  4. Ajuste o `indice.md` de Outubro.

**2. Skill `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj` (Lúcio/Oscar), v1.1, ativa-com-ressalva.**
- **O que decidiu:** criar e ativar a Skill de desempenho térmico da cobertura: Ucob × absortância, fator FT do ático ventilado, emitância de telha metálica e o aviso do IPT.
- **Por quê:** preenche o "U cobertura ≤ x — confirmar" da Skill `nbr15575-4-emenda2025-...`. Textos lidos: o Projeto de Emenda NBR 15575-5 (mar/2021, sem valor normativo) e o artigo do IPT (2017), ambos extraídos com pypdf. Lúcio deu PROCEDE COM RESSALVA e corrigiu o §4: a cobertura sem isolante do IPT já não passava no simplificado. Também limitou a brecha do FT a 0,4 < α ≤ 0,6 e retirou 2 macetes sem fonte lida. Ressalvas: R1, projeto de emenda; R2, o envelope das 2 colunas é premissa; R3, Emenda 2025 e simulação; R4, os números do IPT são tendência; R5, o isolante é premissa, não exigência.
- **O que alterou:** `01_CEO/Skills_Propostas/2026/Outubro/lucio_cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj.md` (novo); `.claude/skills/cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj/SKILL.md` (novo); remissões de volta (1 citação cada, sem mudança de regra) em:
  - `.claude/skills/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj/SKILL.md` (após a tabela de Coberturas);
  - `.claude/skills/nbr15220-3-bioclimatica-rj/SKILL.md` (linha 30);
  - `.claude/skills/nbr9575-impermeabilizacao/SKILL.md` (linha 29).
- **Backup:** `_backups/2026-10-01/nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj__SKILL.md`, `_backups/2026-10-01/nbr15220-3-bioclimatica-rj__SKILL.md` e `_backups/2026-10-01/nbr9575-impermeabilizacao__SKILL.md`.
- **Como desfazer:**
  1. Apague a pasta `.claude/skills/cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj/`.
  2. Restaure os 3 backups.
  3. Volte o `Status` do `.md` em `Skills_Propostas` para `proposta` ou arquive-o.
  4. Ajuste o `indice.md` de Outubro.

**3. Cardozo sem Skill.** A busca sobre contenção de escavação em argila mole (NBR 9061, estaca-prancha) não achou fonte primária. Parte do tema já está na Skill de rebaixamento de 29/09. Não forcei.

**Painel:** 2 eventos `skill` gravados no `feed.jsonl` via `Append-STTKLog.ps1`, 2/2 OK.

**Fonte de verdade para rever:** `01_CEO/rotina_fechamento_template.md`, rodada de 01/10/2026.

---

## 01/10/2026 — Drenagem Contínua v2.5.0 (qui, 11:04) — Ensaio 003 etapa 1 executada e corrigida

**1. Ensaio Sombra 003, etapa 1 (Legal base) — Kelsen/Hely executaram, Bardi corrigiu.**
- **O que decidiu:** executar a etapa liberada (`proxima_acao: executar`). Lacre do gabarito conferido antes e depois (SHA256 48867C3C…C9F9 = histórico). Ninguém abriu `_gabaritos_LACRADO/` além do Bardi.
- **Resultado:** entrega em `01_CEO/Casos_TESTE/ensaio_003/etapa_01_legal_base/entrega/` (`parecer_legal_base_003.md` do Hely, `auditoria_kelsen_003.md` do Kelsen — LIBERA COM RESSALVA). Parecer do Bardi: `etapa_01_legal_base/parecer_bardi.md` — **recomendação APROVAR** (8/8 itens, 4/4 iscas, contas refeitas e corretas; 6 correções não bloqueantes: Skill OODC × LC 301 Art. 58; leitura do Dec. 3.046 inciso XI; 520 m² × teto 457,44 m² computáveis; lençol 0,90 m × piscina/escavação; divergência POP-GESTOR-LEGAL-01 §4.3 × POP-LEGAL-02; Hely sem WebFetch). Bardi registrou erro do próprio gabarito ("computáveis") sem alterá-lo.
- **O que alterou:** `_estado_ensaio_003.json` → `aguardando_aprovacao` / `aguardar_claudemberg`, histórico `executada_e_corrigida`. Evento `marco` no `feed.jsonl` (1/1 OK).
- **Como desfazer:** voltar o JSON a `aguardando_execucao`/`executar`, remover a última linha do histórico e apagar `entrega/` + `parecer_bardi.md`.
- **Sobe a Claudemberg:** aprovar/reprovar a etapa 1 (só ele). Kelsen sinalizou: PRPA não definido; propostas de correção em 4 Skills (OODC, Dec. 3046, varandas, habite-se) — não aplicadas nesta rodada (Kelsen as trata como dono; Bardi alerta que a de varandas precisa reler o fim do inciso VII).

**2. Passo 7.5 — varredura mensal de Drive (Kelsen).** 3 correções objetivas (POP-ARQ-PL-01 seção 7.1 e versão; Memorial com caractere corrompido). **Não aplicadas:** `update_file` do MCP só altera título/pasta; a via Service Account é vetada no automático. Registrado item `kelsen-drive-varredura-mensal-01-10-correcoes` (humano) em `pendencias.json` com texto literal antes/depois. Lúcio e Cardozo não foram acionados nesta rodada (sem fila) — a varredura mensal deles fica para a próxima rodada em que forem acionados no mês.

## 01/10/2026 — Kelsen (Legal): correções pós-Ensaio 003, etapa 1 (ordem direta de Claudemberg, via Wallenberg)

- **O que mudou:**
  - **Skill `legal-oodc-mais-valera-mais-valia` v1.1**, instalada e proposta. Janela da LC 281 Art. 40 aberta até 01/12/2026, 30% só à vista (LC 301 Art. 58). Os dois regimes foram separados: OODC pura (LC 270 Art. 111, Fórmula 1 do Anexo XXV) e LC 281 (Art. 18 §1º). Entrou a isenção de 5 anos da **LC 270 Art. 110**, com exceções no §1º, §3º e §8º.
  - **Skill `decreto3046` v1.3.** R1 reescrita (a isenção está no Art. 110, e não no 106), M3 (VII->XI, unifamiliar), M4 (Art. 111 §5º), §7 sobre como checar a vigência do Dec. 3.046. Exemplo sem artigo marcado.
  - **Skill `varandas` v1.2.** Nova §4.1 sobre o regime da ZPP (VII, XI e XIV). A minha proposta "VII mais restritivo" ficou restrita a multifamiliar.
  - **Skill `habite-se`.** Arts. 4º, 6º e 8º conferidos no PDF oficial. O item de documentos estava errado (Art. 6º é requerimento, não Habite-se).
  - **POP-GESTOR-LEGAL-01 §4.3.** Sai "POP-LEGAL-02 SUSPENSO"; entra a regra de ler o `status:` do próprio POP.
  - **POP-LEGAL-02.** Nova R.8 (LC 270 Arts. 106-111).
  - **`hely.md`.** Corpo: checklist de 7 itens e correção da menção a WebSearch/WebFetch. O frontmatter não foi tocado.
  - **`auditoria_kelsen_003.md`.** Errata 4.1.
  - Pelo Hely: `_indice_fontes` (Dec. 3.046 e LC 270 Arts. 106-111), `_estado_hely` (checklist), cópias proposta = instalada (md5 conferido) e 8 PDFs regerados e conferidos visualmente.
- **Por quê:** parecer do Bardi, seção "O que corrigir", e a minha auditoria. Ao reler o primário, LC 270 pp. 40-41, achei dois erros a mais, um meu e um do Bardi:
  - a isenção de 5 anos existe, no Art. 110;
  - o Anexo XXV é sim a fonte da fórmula da OODC pura.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/kelsen_ANTES_*` (20 arquivos, cópia feita pelo Hely antes de qualquer edição).
- **Como desfazer:** copiar cada `kelsen_ANTES_*` de volta ao caminho original. Nos arquivos `_SKILL_instalada`, o destino é `.claude/skills/<nome>/SKILL.md`. Depois, regerar os PDFs a partir dos .md restaurados (ou restaurar os .pdf do backup).
- **Sobe a Wallenberg:** pedido formal de ferramenta para o Hely (WebFetch + WebSearch), sem edição de frontmatter. As dúvidas de mérito, Art. 110 §8º na AP4 e VII x XI na unifamiliar, vão ao Gate do Maurício.

## 01/10/2026 — Wallenberg: aprovação da etapa 1 do Ensaio 003 e cadeia de pedido de ferramenta

- **Claudemberg aprovou ao vivo a etapa 1** ("Aprovo a etapa 1"). No `_estado_ensaio_003.json`: `etapa_atual` 2, `status_etapa` a_criar, `proxima_acao` criar_caso, e histórico `aprovada_por_claudemberg`. A próxima Rotina Ensaio Sombra (Bardi) monta a etapa 2 (Viabilidade, Villaça).
- **Ordem de Claudemberg (regra durável):** o Gestor corrige os erros que o seu Agente cometeu no ensaio e capacita esse Agente. A ferramenta ou plugin que o Gestor não consegue dar sobe a Wallenberg. O que Wallenberg não tem permissão de fazer sobe a Claudemberg na Reunião Semanal. Kelsen executou a ordem (entrada acima).
- **Pedido de WebFetch + WebSearch para o Hely:** tentei adicionar as duas ao `tools:` do `.claude/agents/hely.md`. O classificador de permissão do modo automático negou a edição (auto-modificação). Não contornei. Foi para a pauta da Semanal como `hely-ferramentas-webfetch-websearch-semanal` em `pendencias.json`. O `hely.md` não foi alterado. Existe um backup preventivo em `_backups/2026-10-01/wallenberg_ANTES_hely_tools.md`, que pode ser descartado.


## 01/10/2026 — Rotina Macetes de Profissionais v1.2: 7 macetes em 2 Skills (quinta, 14:14)

- **Fila do dia** (máx. 1 por Gestor; Villaça não tem Skill e não foi aberto):
  - Kelsen: `varandas-nao-computaveis-ate-to-coes-lc198-rj`. Prioridade 0a: Bardi apontou a leitura do Dec. 3.046 VII/XI. Era a 2ª rodada.
  - Lúcio: `nbr15220-3-bioclimatica-rj`. Prioridade 0b: a etapa 3 do Ensaio é o Levantamento. A Skill é cross; Cardozo ficou registrado como co-dono.
  - Cardozo: `fundacoes-solos-moles-lencol-freatico-barra-recreio`. Prioridade 1.
- **nbr15220-3 v1.1 → v1.2 (Lúcio), 3 macetes tipo A.** Fontes: Lamberts/LabEEE (ENCAC 2025) e o Projeto de Revisão ABNT de jun/2024, pp. 1, 13, 20-23.
  - M1: a zona se confirma no mapa do LabEEE. O Rio é 4A e é a cidade característica da zona (TMYx, estação 837550).
  - M2: a 2024 não tem diretrizes construtivas por zona; a indústria pediu a retirada.
  - M3: o microclima entra como premissa, sem trocar de zona.
  - A ressalva da zona passou de "indício" para "confirmada no texto de Consulta Nacional; texto final não lido". A seção Limbo recebeu a regra dos 180 dias do prefácio, marcada como "só no texto de projeto".
- **fundacoes-solos-moles 1.2 → 1.3 (Cardozo), 4 macetes tipo A.**
  - M1 a M3 vêm de Urbano R. Alonso (Instituto de Engenharia, 2023): teste do trado junto ao furo de sondagem; leitura do perfil de consumo de concreto; erros de execução a proibir na especificação.
  - M4 vem de Danziger/Gerscovich (UERJ, 2017): atrito negativo na argila da Baixada de Jacarepaguá.
- **varandas: sem macete na 2ª rodada → lista "Sem fonte pública".** Tentativas: tipo A (CAU/RJ, arquitetos) e tipo C (Ademi-RJ, Sinduscon-Rio, CAU/RJ, SMU). A única fonte C achada foi a ata do COMPUR de 13/09/2007 (Ademi/AsBEA). Ela traz só opinião sobre fechamento de varanda e nenhuma técnica nova.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/macetes_ANTES_*` (2 arquivos).
- **Como desfazer:**
  - Copiar cada `macetes_ANTES_<skill>_SKILL_instalada.md` para `.claude/skills/<skill>/SKILL.md`.
  - Nas cópias de `Skills_Propostas/2026/Setembro/`, reverter pelo git (`git checkout <commit>~1 -- <arquivo>`).
  - Reverter também `_estado_lucio.md` e `_estado_cardozo.md`.
- **Pendências geradas (não resolvidas aqui; ficam para a Drenagem/Reunião):**
  - (1) Cinco Skills ainda tratam a ZB 4A como "indício": nbr15575-4-emenda2025, lucio-protecao-solar, vidro-fachada-poente, especies-nativas e cobertura-transmitancia. É preciso alinhar com a 15220-3 v1.2 (donos: Lúcio, e Cardozo para especies-nativas).
  - (2) Divergência de anexo na `nbr6122-2019-fundacoes`. A Skill diz Anexo J para hélice; Alonso cita o Anexo N. Cardozo suspeita que o erro está na Skill. É preciso conferir na norma.

## 02/10/2026 — Rotina Diária Skills v3.5.0 (sex, 09:06) — fluxo de sexta, sem Skill nova

- **O que decidiu:**
  - (1) Registrar em `pendencias.json` o item `hely-ferramentas-webfetch-websearch-semanal`. A entrada de 01/10 dizia que ele existia, mas não tinha sido gravado.
  - (2) Gravar 5 eventos no feed: 3 marcos, 1 `sistema` e 1 `status`.
  - (3) Reescrever `painel_status.json` com as contagens reais da semana.
- **Por quê:** é o fluxo de sexta (Passos 6, 9 e 10). A pendência órfã foi apontada pela passagem de 01/10.
- **O que alterou:**
  - `01_CEO/Pendencias/pendencias.json`: 1 item e o `atualizado_em`.
  - `01_CEO/Painel_Fundador/feed.jsonl`: 5 linhas no fim.
  - `01_CEO/Painel_Fundador/painel_status.json`.
  - `01_CEO/rotina_fechamento_template.md`: rodada de 02/10 no topo.
  - Este arquivo.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-02/` (pendencias, painel_status, Outubro e template, todos `_ANTES`).
- **Como desfazer:**
  - Copiar cada `_ANTES` de volta ao caminho original.
  - No `feed.jsonl`, apagar as 5 últimas linhas (30/09 marco Ensaio/Bardi; 01/10 marco etapa 1; 02/10 marco etapa 2; 02/10 sistema Dashboard; 02/10 status Resumo).

---

## 02/10/2026 — Drenagem Contínua v2.5.0 (sex, 11:03–~11:30) — Ensaio 003, etapa 2 executada e corrigida

- **Portão:** 0 itens auto+aberta; 0 Skills novas (as 2 de outubro já estão `ativa-com-ressalva`); Notion com 0 `pendente` e 2 `em execução` (LELE-002 e VILLACA-001, aguardando a Trava 3); ensaio_pend=SIM (etapa 2, `executar`).
- **Execução:** Villaça (Gestor Viabilidade) executou com Mascaró (custo de obra) e Fiker (revenda). Entrega em `01_CEO/Casos_TESTE/ensaio_003/etapa_02_viabilidade/entrega/` (3 arquivos).
- **Incidente de processo:** na 1ª passada, Villaça delegou Mascaró e Fiker em segundo plano e devolveu sem integrar, o mesmo antipadrão de delegação órfã de 09/09. Wallenberg vigiou o disco até os 2 arquivos existirem e retomou Villaça (SendMessage), que auditou e integrou. Villaça registrou a lição no próprio `_estado_villaca.md`.
- **Lacre:** SHA256 `36FC592A…C88` conferido antes da execução e antes da correção. Íntegro.
- **Correção do Bardi:** recomendação **APROVAR COM RESSALVA**. Iscas pegas: 1 (OODC), 3 (radier × sondagem) e 4 (corretor e crédito). Iscas parciais: 2 e 5 (CUB e revenda aplicados sobre a área computável, e não sobre a construída). Parecer em `etapa_02_viabilidade/parecer_bardi.md`.
- **JSON do ensaio:** `aguardando_aprovacao` / `aguardar_claudemberg`. O histórico recebeu o evento `executada_e_corrigida`.
- **Painel:** 1 evento `marco` gravado via Append-STTKLog (OK).
- **Como desfazer:** reverter o commit desta rodada. No `feed.jsonl`, apagar a última linha (02/10, marco, Bardi, etapa 2 corrigida).

---

## 05/10/2026 — Rotina Diária Skills v3.5.0 (seg, 09:06) — 2 Skills ativadas com ressalva + SELCA v1.2

- **O que decidiu:**
  - (1) Ativar `levantamento-topografico-cadastral-orientado-duli-licin-rj` (Lúcio/Oscar), v1.1, ativa-com-ressalva. Fonte primária: Decreto 55.622/2025 (PDF da SMDU) e COE LC 198/2019 (acervo).
  - (2) Ativar `entrada-energia-light-ligacao-nova-padrao-recon-bt-rj` (Cardozo/Landell), v1.1, ativa-com-ressalva. Fonte primária: FAQ oficial de Ligação Nova da Light + vídeo oficial da Light assistido via /watch.
  - (3) Kelsen: Skill SELCA de v1.1 para v1.2, com a R1 parcialmente fechada (LC 140/2011 lida no Planalto) e a nova R7 (APA).
  - (4) Remissões de volta em `nbr5410-eletrica-automacao`, `habite-se-aceitacao-licin` e `fundacoes-solos-moles-lencol-freatico-barra-recreio`.
- **Por quê:** a etapa 3 do Ensaio 003 é o Levantamento (Lúcio), e não havia Skill de levantamento. O Cardozo estava sem Skill desde 01/10, e a entrada de energia da Light era lacuna declarada na nbr5410 ("fornecimento da concessionária"). Para o Kelsen, as buscas não acharam lei nova da Barra/Recreio, então a rodada fechou ressalva em vez de criar Skill.
- **O que alterou:**
  - Novos: `01_CEO/Skills_Propostas/2026/Outubro/lucio_levantamento-topografico-cadastral-orientado-duli-licin-rj.md` e `cardozo_entrada-energia-light-ligacao-nova-padrao-recon-bt-rj.md`; `.claude/skills/levantamento-topografico-cadastral-orientado-duli-licin-rj/` e `.claude/skills/entrada-energia-light-ligacao-nova-padrao-recon-bt-rj/`.
  - Editados: `.claude/skills/selca-.../SKILL.md` e a cópia `kelsen_selca-...md` (por Kelsen); `.claude/skills/nbr5410-eletrica-automacao/SKILL.md` (item 3 e linha de fora de escopo); `.claude/skills/habite-se-aceitacao-licin/SKILL.md` (linha 22); `.claude/skills/fundacoes-solos-moles-lencol-freatico-barra-recreio/SKILL.md` (checklist de aterro); `Skills_Propostas/2026/Outubro/indice.md`; `_estado_lucio.md`, `_estado_cardozo.md`, `_estado_kelsen.md` (pelos Gestores); este arquivo.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-05/` (selca, nbr5410, habite-se, fundações, índice e este livro-razão, todos `_ANTES`).
- **Como desfazer:**
  - Apagar `.claude/skills/levantamento-topografico-cadastral-orientado-duli-licin-rj/` e `.claude/skills/entrada-energia-light-ligacao-nova-padrao-recon-bt-rj/`, e voltar o `status` das duas cópias em `Skills_Propostas` para `proposta`.
  - Copiar `selca_SKILL_ANTES_v1.2.md` para a Skill instalada e para a cópia espelho.
  - Copiar `nbr5410_SKILL_ANTES_remissao_light.md`, `habite-se_SKILL_ANTES_remissao_levantamento.md` e `fundacoes_SKILL_ANTES_remissao_levantamento.md` de volta para as respectivas `.claude/skills/<nome>/SKILL.md`.
  - Copiar `indice_outubro_ANTES.md` de volta para `indice.md`.
  - No `feed.jsonl`, apagar as 3 linhas de 05/10 gravadas por esta rodada.
- **Pendências geradas:**
  - (1) Hely: regra numérica de cota de soleira e de "terreno natural" na Barra/Recreio (R2 do levantamento). Lúcio conferiu que nenhuma Skill de Kelsen trata disso.
  - (2) Kelsen: `habite-se-aceitacao-licin` linha 16 diz que a vistoria compara "com o projeto aprovado"; o Art. 8º do Decreto 55.622 só manda vistoriar os itens do Art. 3º (achado lateral do Lúcio, não editado).
  - (3) Landell: baixar à mão a RECON-BT 2024 (o download automático devolveu HTML) e confirmar carga instalada × demandada no limite de 75 kW.
  - (4) Sugestão de compra: ABNT NBR 13133:2021 (levantamento topográfico).
  - (5) Kelsen sugeriu citar o Art. 13 §2º da LC 140 na linha de supressão do checklist §9 da SELCA (não aplicado, fora do pedido).

## 05/10/2026 — Drenagem Contínua v2.5.0 (11:03, segunda) — Ensaio 003 etapa 2, refazer v6
- **O que foi decidido:** o estado do ensaio (`proxima_acao: refazer`) e o parecer v5 do Bardi (REPROVAR, 3 itens) mandavam refazer a etapa 2. Lacre do gabarito conferido (SHA256 36FC592A…C88 = histórico).
- **Villaça (Gestor) + Mascaró + Fiker:** entrega `01_CEO/Casos_TESTE/ensaio_003/etapa_02_viabilidade/entrega/v6/` (pre_estudo_viabilidade_003.md, custo_obra_mascaro_003_v6.md, revenda_fiker_003_v5.md). 3 itens da v5 corrigidos + varredura (10 correções no Pré-Estudo, 11 no Fiker). Nenhum número mudou.
- **Skill alterada:** `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` v1.3→v1.4 (§2.4 playground "quando não classificado como área construída" + nota literal do CUB) nas 2 cópias (`.claude/skills/` e `Skills_Propostas/2026/Outubro/`). Backups integrais: `_backups/2026-10-05/viabilidade_SKILL_instalada_v1.3_INTEGRAL_ANTES_v1.4.md` e `villaca_viabilidade_SKILL_copia_v1.3_INTEGRAL_ANTES_v1.4.md`.
- **Bardi:** `parecer_bardi_v6.md` — recomenda **REPROVAR**: faixas de metragem do controle web do Fiker sobre área computável (erro desde a v2; W8/W13 fora; S1 topo +~R$ 711 mil; isca 4 caiu para parcial); W1 omitido na "Limitação de tipo"; Skill §3.1/3.2 sem a regra de base de área do filtro; espelho `.agents/skills/` em v1.3.
- **Estado do ensaio:** `status_etapa: aguardando_aprovacao`, `proxima_acao: aguardar_claudemberg`; histórico += `refeita_e_corrigida` v6 (com nota de que v2–v5 de 02/10 não tinham sido registradas no histórico).
- **Painel:** 1 evento `marco` (Bardi) via Append-STTKLog.ps1 — OK.
- **Learning Agent (8a, segunda):** 2 propostas anexadas a `01_CEO/wallenberg-drenagem-continua-v2_SKILL.md` (não executadas). Backup integral em `_backups/2026-10-05/wallenberg-drenagem-continua-v2_SKILL_INTEGRAL_ANTES_learning_05_10.md`.
- **Como desfazer:** apagar `entrega/v6/` e `parecer_bardi_v6.md`; copiar os 2 backups v1.3 de volta para as cópias da Skill; voltar o JSON do ensaio para `reprovada`/`refazer` e remover a última linha do histórico; remover a linha de 05/10 (Bardi, marco) do `feed.jsonl`; copiar o backup da SKILL da Drenagem por cima.

## 06/10/2026 — Rotina Macetes de Profissionais v1.2: 5 macetes em 2 Skills (terça, 14:00)
- **Portão:** terça; 0a (Kelsen OODC) e 0b (Lúcio levantamento) com 2ª rodada marcada para outra data; prioridade 1 vazia (as 5 Skills da lista "só da norma" já tinham a seção). Modo fila esgotada → prioridade 2, permitido às terças.
- **Kelsen — `decreto3046-81-lc270-2024-licin-barra-recreio` 1.3→1.4 (instalada + cópia `Skills_Propostas/2026/Setembro/`):** M5 (Dicionário de Termos Técnicos da LC 270, SMDU, 2ª ed. dez/2025, como índice remissivo — limite: o verbete OODC não remete ao Art. 110) e M7 (afastamento frontal medido do alinhamento, inclusive o projetado por PAA; LC 270 Art. 363 lido) + item de checklist "Consultar PAA". M6 (ATC) **rejeitado**: o Art. 151 II não define ATC. Tipo C.
- **Cardozo — `nbr5410-eletrica-automacao` v1.1→v1.2 (só instalada; a cópia de agosto é registro histórico):** E1 (evitar DR único na proteção geral, fundido no item 2), E2 (iluminação seca × molhada, **corrigido**: o exemplo do manual deixa o banheiro sem DR, contra 5.1.3.2.2 a)), E3 (TUG de cozinha em circuitos de 2–3 pontos, escolha de projeto). Fonte A+B: manual "Instalações Elétricas Residenciais", Elektro/Pirelli/Procobre, jul/2003, rev. técnica Prof. Hilton Moreno; conferido contra a NBR 5410:2004.
- **Fontes guardadas:** `01_CEO/Skills_Propostas/_macetes_fontes/2026-10-06/` (2 PDFs).
- **Vídeos:** nenhum (as fontes achadas eram documentos).
- **Pendências:** Kelsen — regra de medição do afastamento frontal no Dec. 3.046 (limite b do M7) e PDF da proposta defasado (não regerado).
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-06/macetes_ANTES_*.md`, `macetes_fila_ANTES.md`, `livro_razao_outubro_ANTES_macetes.md`.
- **Como desfazer:** copiar `macetes_ANTES_decreto3046-81-lc270-2024_SKILL_instalada.md` e `_proposta.md` de volta para a Skill instalada e para a cópia de setembro; copiar `macetes_ANTES_nbr5410-eletrica-automacao_SKILL_instalada.md` de volta para `.claude/skills/nbr5410-eletrica-automacao/SKILL.md`; copiar `macetes_fila_ANTES.md` de volta para `_macetes_fila.md`; apagar a pasta de fontes de 06/10 e as 2 linhas de 06/10 do `feed.jsonl` gravadas por esta rotina.
