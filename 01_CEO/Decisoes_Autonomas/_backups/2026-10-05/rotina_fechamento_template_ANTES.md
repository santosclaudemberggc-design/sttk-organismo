---
name: rotina-fechamento-template
description: "Template de Fechamento de Rotina — preenchido ao fim de cada rodada, lido no início da próxima"
metadata:
  type: operacional
  lido_por: wallenberg-rotina-diaria-skills-v2, wallenberg-drenagem-continua-v2
  escrito_por: ambas rotinas
  frequencia: toda rodada (Diária: daily, Drenagem: 3x/semana)
---

# Fechamento de Rotina — Template Reutilizável

**Leia isto ao INÍCIO de cada rodada para saber:**
- O que foi feito na rodada anterior
- O que ficou pendente
- O que não fazer (evitar retrabalho) — ver a seção consolidada no fim deste arquivo

**Preencha isto ao FIM de cada rodada para que a próxima saiba:**
- O que foi entregue
- O que ficou bloqueado e por quê
- O que tomar cuidado

**Manutenção [v1.0 — 30/09/2026]:** o Fechamento do Dia (20:00) mantém este arquivo com só as 2 rodadas mais recentes + a seção consolidada "O QUE NÃO FAZER (acumulado)" no fim. Rodadas mais antigas vão, inteiras, para `01_CEO/rotina_fechamento_historico.md` — nada é apagado.

---

## [2026-10-02] — Diária Skills v3.5.0 (Sexta) — FLUXO DE SEXTA (Passos 6, 9, 10; sem Skill nova)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Friday. Início às 09:06. Fluxo de sexta, sem pesquisa e sem Skill nova.
- [x] **Passo 0:** passagem de 01/10 lida. Ensaio 003 está na etapa 2/17 (Viabilidade), `aguardando_execucao`; só leitura. O último `status` do feed era de 28/09.
- [x] **Pendência órfã corrigida:** `hely-ferramentas-webfetch-websearch-semanal` era citada no livro-razão de 01/10, mas não existia no `pendencias.json`. Agora está registrada (média, humano, pauta da Semanal). Backup em `_backups/2026-10-02/`.
- [x] **Passo 6 (Painel):** 3 eventos de marco: Ensaio 003 + Bardi (30/09), etapa 1 aprovada (01/10), etapa 2 criada (02/10). 3/3 OK.
- [ ] **Passo 7 (Learning Agent):** não rodou. É opcional e não havia vídeo novo na fila.
- [x] **Passo 9 (Dashboard):** evento `sistema` e evento `status` gravados por último, 2/2 OK. `painel_status.json` reescrito com contagem real: 19 membros (10 Auto, 4 Assisted, 1 Shadow, 4 Formação; Bardi entrou), 3 de 5 Gestores Autonomous, pendências 50 de 58 fechadas (8 ativas: 1 crítica, 2 alta, 3 média, 2 baixa), 6 Skills na semana. `caso_real` e `marcos` mantidos, porque não há evidência nova no livro-razão.
- [x] **Passo 10 (Análise):** abaixo.

### ANÁLISE DA SEMANA 28/09–02/10

- **Produção:** 6 Skills (2 por Gestor), todas ativas com ressalva, 1 arquivada (LC 301) e macetes em 4 Skills. Ao todo, 45 instaladas.
- **Fraqueza principal:** são 2 semanas seguidas com 0 Skill usada em caso real. O primeiro teste de verdade, a etapa 1 do Ensaio 003, obrigou o Kelsen a corrigir 4 Skills que já estavam "ativas" (OODC, Decreto 3046, varandas e habite-se). Achou erro de artigo (Art. 106 em vez de 110) e de documento. Isso mostra que "ativa com ressalva" não quer dizer "certa". O Ensaio corrige mais do que a Diária produz.
- **Bloqueadores recorrentes:**
  - (1) NBR 15575 partes 1, 4 e 5 fora do acervo. Trava a ressalva de 3 Skills térmicas. Sugestão de compra.
  - (2) Hely sem WebFetch/WebSearch. Decisão da Semanal.
  - (3) Drive sem ferramenta de escrita de conteúdo. 3 correções esperam Claudemberg.
  - (4) `/watch` com 0 vídeo assistido em 01/10. A busca não achou vídeo assistível, e o bug de 403/429 continua.
- **Próximas prioridades:**
  - (a) Etapa 2 do Ensaio. Villaça é Assisted, mas Mascaró e Fiker estão em Formação, nunca examinados. Risco alto de reprovação, porque é a primeira vez da equipe.
  - (b) Segunda: Cardozo volta à contenção em argila mole só com fonte primária.
  - (c) Pauta da Semanal: ferramentas do Hely, compra da NBR 15575 e as correções de Drive. Também a pendência órfã do `CLAUDE.md` (validação de 31/07 nunca fechada).
- **Sugestão (não aplicada, para a Semanal):** a Diária poderia priorizar as Skills que a próxima etapa do Ensaio vai usar, em vez de criar Skill de tema novo. A etapa 3 é o Levantamento, de Lúcio.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- Tudo que estava em 01/10 continua valendo: SELCA R1/R4, Cobertura R1, contenção (Cardozo), varandas, reservatório, rebaixamento R1/R3, vidro R1/R2 e o bug do /watch.

---

## [2026-10-01] — Diária Skills v3.5.0 (Quinta) — RODADA COMPLETA (2 Skills ativadas com ressalva)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Thursday. Início às 09:07. Pipeline seg-qui.
- [x] **Passo 0:** `_passagem_do_dia.md` de 30/09 lido; a v1.0 da passagem foi lida corretamente. Prioridade zero conferida: a etapa 1 do Ensaio 003 (legal_base) **já foi criada hoje pelo Bardi** e está com status `aguardando_execucao`, pronta para a Drenagem. Só leitura, nada tocado. O último evento `status` do feed é de 28/09.
- [x] **Kelsen/Hely, `selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj` v1.1:** ativa-com-ressalva e instalada. Fecha a pendência SELCA de 29/09. O texto integral do DOERJ foi lido (pypdf). Kelsen fez 6 correções factuais; ressalvas R1 a R5. Primeira Skill nova de Kelsen desde 25/09.
- [x] **Lúcio/Oscar, `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj` v1.1:** ativa-com-ressalva e instalada. Fecha o "U cobertura ≤ x" aberto na Skill da NBR 15575-4. Lúcio corrigiu o §4 (IPT), limitou a brecha do FT e retirou 2 macetes sem fonte.
- [x] **Coerência:** remissões de volta em 5 Skills (legal-base, rebaixamento, nbr15575-4, nbr15220-3, nbr9575). Backups em `_backups/2026-10-01/` (5 arquivos). Sem contradição de valor.
- [x] **Cardozo:** sem Skill (contenção/NBR 9061 sem fonte primária).
- [x] **Feed:** 2 eventos, 2/2 OK. **Livro-razão:** `Decisoes_Autonomas/2026/Outubro.md` criado, com "como desfazer".
- [~] **/watch:** as 3 buscas de vídeo (uma por Gestor) não acharam URL de vídeo assistível sobre os eixos. Só apareceram artigos e uma matéria que cita um vídeo (Talita Catelani), sem link. Nada assistido nesta rodada.
- [ ] **Passo 8 (Trilha B):** não rodou, porque nenhum `_estado_` trouxe lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **SELCA, R1:** competência SMAC × INEA (LC 140/2011, Art. 9º, XIV, e a resolução do CONEMA sobre impacto local). Kelsen achou também que lote com APP ou área alagadiça sai da LMS e vai para LMP+LMI, ainda municipal (Dec. 51.503/2022, Art. 27, parágrafo único). Dono: Hely.
- **SELCA, R4:** lei estadual de outorga (Lei 3.239/1999, a confirmar) não lida. Dono: Hely.
- **Cobertura, R1:** confirmar a Tabela 5 e o FT no texto publicado da NBR 15575-5:2021 (norma paga, fora do acervo). **Sugestão de compra:** NBR 15575 partes 1, 4 e 5, recorrentes em 3 Skills térmicas.
- **Cardozo, candidata:** contenção de escavação em argila mole (NBR 9061 / cortina / estaca-prancha). Só criar com fonte primária ou fonte técnica de profissional lida.
- **Continuam valendo:** varandas (3 lacunas, Kelsen); reservatório (reuso voluntário, Kelsen); rebaixamento R1/R3 (Hely); vidro R1/R2 (Lúcio); bug do /watch (`-vsync`).

---

## [2026-09-29] — Diária Skills v3.4.0 (Terça) — RODADA COMPLETA (2 Skills ativadas, 4 treinos OK)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Tuesday. Início às 08:14. Pipeline seg-qui.
- [x] **Passo 0.5, treinos atrasados:** as 2 Skills de 28/09 foram treinadas, ambas OK. Reservatório (Saturnino): v1.2 com 4 esclarecimentos. Varandas (Hely): as 3 lacunas da Skill ficam pendentes com Kelsen (ver abaixo).
- [x] **Cardozo/Baumgart, `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` v1.2:** ativa-com-ressalva e instalada. Fonte primária: Lei 5.234/2008 (ALERJ). Cardozo: PROCEDE COM RESSALVA, com v1.1 e correções técnicas. Treino do Baumgart OK (7 de 7 iscas).
- [x] **Lúcio/Oscar, `vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj` v1.2:** ativa-com-ressalva e instalada. Fecha a lacuna de vidro de 28/09. Fonte primária: Portaria Inmetro 309/2022, Anexo II. Lúcio: PROCEDE COM RESSALVA e corrigiu uma contradição com a Skill de proteção solar (no poente, sombreamento vertical). Treino do Oscar OK (6 de 6 iscas).
- [x] **Coerência v3.4.0:** remissões de volta gravadas na Skill de fundações da Barra (linha 129) e na de proteção solar (seção 6).
- [x] **Kelsen:** sem Skill. A busca achou a LC 299/2026 (MCMV, fora do perfil STTK) e o Decreto Estadual 50.473/2026 (SELCA, ver pendência).
- [x] **/watch:** vídeo jXFca_Az9f8 (ponteiras filtrantes), aproveitado só pela transcrição. O download do vídeo deu 403 e as legendas vieram na 2ª tentativa (a 1ª deu 429). As buscas de vídeo para Kelsen e Lúcio não acharam material relevante.
- [x] **Feed:** 2 eventos, 2/2 OK. **Livro-razão:** entrada 29/09 mais adendo. **Backups:** `_backups/2026-09-29/` (8 arquivos).
- [ ] **Passo 8 (Trilha B):** não rodou, porque nenhum `_estado_` trouxe lacuna de ferramenta.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Varandas (Kelsen), 3 lacunas do treino:** como lançar no projeto uma varanda que já nasce com vidro retrátil (COES caput e §10, LC 145/2014); se casas geminadas contam como uma edificação para os 5 m e para o §3º; varanda gourmet como cômodo disfarçado. Só editar a Skill depois de ler o texto.
- **Reservatório:** reuso voluntário de unifamiliar sob os Arts. 3º a 9º da Res. Conj. (Kelsen).
- **Rebaixamento, Hely:** R1, confirmar na INEA 63/2012 ou na CERHI 221/2020 que os 5.000 L/dia valem como dispensa de **outorga** (a Lei 5.234 é de cobrança); R3, qual órgão autoriza o lançamento na rede pluvial municipal.
- **Vidro, Lúcio:** R1, confirmar 0,87 / 5,70 / 17% na NBR 15575-1 §11.4.7.2; R2, zona da INI-R para o Rio depois da NBR 15220-3:2024.
- **SELCA, Decreto Estadual 50.473 de 15/09/2026 (novo licenciamento ambiental do RJ):** Hely verifica o que muda para obra residencial perto de lagoa na Barra/Recreio.
- **Cardozo, fora do escopo:** a `nbr6122-2019-fundacoes` remete escavação à NBR 11682 (encostas); a candidata certa pode ser a NBR 9061, a confirmar.
- **Formato dos treinos:** 4 de 4 Agentes passaram das 15 linhas. Cardozo e Lúcio vão cobrar isso como padrão.
- **Continuam valendo:** Skill de partido de 16/09 (linhas 70-72, os 20% do §5º), que o Lúcio confirmou; bug do `/watch` (`-vsync`, 429/403); pendências de Lint de 25/09.

---

## O QUE NÃO FAZER (acumulado)

Consolidado em 30/09/2026 a partir de todas as rodadas de 01/09 a 29/09 (movidas para `01_CEO/rotina_fechamento_historico.md`). Itens já resolvidos/superados por rodada mais nova não aparecem de novo — quem quiser o detalhe completo lê o histórico.

**Kelsen (Legal):**
- LC 301/2026 (AEIU Praça Onze, cadeia de 30%, Art. 64) — não crie Skill nova; coberta e corrigida nas Skills de 18/09 v1.1, 23/09 e 24/09 (Art. 64 fechado: é LC 229, fora da AP4).
- Decreto 3046/81 + LC 270/2024 LICIN Barra/Recreio — não duplique; Skill de 21/09 (ratificada).
- Varanda não computável (COES Art. 8º) — não duplique; Skill de 28/09 v1.1.
- OODC/Mais-Valerá/Mais-Valia — não duplique; Skill de 15/09 v1.1.
- NBR 5419:2001 (SPDA) — não use como base; obsoleta, use a NBR 5419:2026 (Skill de 15/09).
- LC 291/2025 — não crie Skill separada; coberta como histórico na Skill LC 301.
- Regime de Licenciamento de Portugal (out/2026) — fora de escopo, não é RJ.
- SELCA / Decreto Estadual 50.473/2026 — não duplique; Skill de 01/10 v1.1.

**Lúcio — cobertura:**
- Ucob, absortância de telha, ático ventilado e FT (NBR 15575-5) — não duplique; Skill de 01/10 v1.1.

**Lúcio (Arquitetura):**
- Ventilação cruzada / fachada poente / vidro de controle solar — não duplique sem parâmetro numérico real; coberta por Partido (16/09), Proteção Solar (17/09, v1.1→v1.3) e Vidro/INI-R (29/09 v1.2).
- COE LC 198/2019 ventilação/iluminação/pé-direito — não duplique; Skill de 21/09.
- NBR 15575-4 Emenda 2025 (desempenho térmico) — não duplique; Skill de 22/09.
- TDC/LICIN 2.0 e Partido/Conforto Térmico — não duplique; Skills de 16/09.
- NBR 9050:2020 (acessibilidade) — não duplique; Skill de 15/09 v1.1.

**Cardozo/Complementares (Baumgart, Saturnino, Landell, Tenreiro, Glaziou, Mindlin):**
- Rebaixamento de lençol / outorga INEA de obra — não duplique; Skill Baumgart de 29/09 v1.2.
- NBR 6484:2020 / sondagem SPT — não crie Skill separada; coberta pela Skill de fundações Barra/Recreio v1.1.
- Fundações em solos moles Barra/Recreio — não duplique; Skill Baumgart de 21/09.
- Reservatório de retardo (Dec. 23.940) — não duplique; Skill Saturnino de 28/09 v1.1.
- NBR 6122:2022 (fundações) — não duplique; Skill de 07/09.
- NBR 6120:2019 (cargas) — não duplique; Skill de 08/09.
- NBR 8681:2025 (segurança/fatores) — não duplique; Skill de 09/09.
- NBR 10844:1989 (águas pluviais) — não duplique; Skill de 10/09.
- NBR 9575:2024 (impermeabilização) — não duplique; Skill de 02/09.
- NBR 5410 (elétrica) — não duplique; Skill de 28/08.
- NBR 14565:2019 (cabeamento estruturado) — não duplique; Skill Landell de 23/09.
- COSCIP/CBMERJ Decreto 42/2018 — não duplique; Skill de 04/09 v1.1.
- Resolução SMDU 10/2026 (RDT) — não duplique; Skill de 03/09.
- NBR 15575:2025 (desempenho acústico de pisos) — não duplique; Skill de 03/09.
- NBR 15220-3:2024 (zoneamento bioclimático) — não duplique; Skill de 01/09.
- NBR 7229:1993, NBR 13969:1997, NBR 10521:1988 — não crie Skill separada; substituídas pela NBR 17076:2024.
- Iluminação de interiores NBR ISO/CIE 8995-1 — não duplique; Skill Tenreiro de 18/09.
- Remoção de árvores FPJ/SMAC — não duplique; Skill Glaziou de 18/09.
- Espécies nativas da Mata Atlântica — não duplique; Skill Glaziou de 22/09.
- APA Barra (condicionantes por lote) — não tente de novo; dados públicos insuficientes (confirmado 22/09).
- Proteção Solar Externa (brises/cobogó/venezianas) — não duplique; Skill Lúcio/Oscar de 17/09 (v1.1→v1.3).
- Memorial Descritivo/Apresentação Técnica (Mindlin) — não duplique; Skill de 16/09.

**Ferramentas/Vitruvius (padrão vigente: tudo fica dentro do Revit):**
- PyNite, anaStruct, StructPy, CBE Clima Tool, EasyEletric, PyFlo/pipedream, open-garden-planner, Blueprint3d — não proponha; standalone, não integram Revit.
- RevitCortex 173, BIMwright/rvt-mcp 229, UV-Tech/revit-claude-mcp 40, LuDattilo/revit-mcp-server 138, IbrahimFahdah/revit-claude-mcp 46, Simone-Balin/Sam-AEC 100+ — não crie Skill isolada; já registrados em `vitruvius_achados`.
- pyRevit-MCP, mcp-servers-for-revit, Autodesk APS Sample MCP Server — não crie Skill; pago ou arquivado/inativo.
- Luw.ai, Remodel AI, Redraw, Leonardo AI, Modly — não crie Skill; cloud (vazamento de dados) ou foco errado.
- Blender MCP, Architecture MCP (sceneview-tools) — não pesquise/proponha de novo; já coberto (01/08) ou retorna 404.
- Apresentação interativa ao cliente — busca PAUSADA; só retomar quando um caso real forçar a decisão.

**Vídeos já assistidos via /watch (não repetir):**
- jXFca_Az9f8, Z0buYmS8fDE, 0-QDPnEIkvw, VUCChmNYpKU — conteúdo já extraído, sem novidade em reassistir.

**Painel/Sistema:**
- `painel_fundador_sttk.html` — não editar até Claudemberg resolver o conflito do span `id="updated"` travado.

---

**Última atualização:** 01/10/2026 (Fechamento do Dia v1.0 — rodada de 28/09 movida para `rotina_fechamento_historico.md`; template de volta a 2 rodadas + consolidado)
**Próxima leitura:** 02/10/2026 (sexta-feira) — Diária Skills fluxo de sexta (Passos 6-10)
