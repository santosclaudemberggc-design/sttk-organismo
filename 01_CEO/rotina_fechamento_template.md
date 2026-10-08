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
## O QUE NÃO FAZER (acumulado)

Consolidado em 30/09/2026 a partir de todas as rodadas de 01/09 a 29/09 (movidas para `01_CEO/rotina_fechamento_historico.md`). Itens já resolvidos/superados por rodada mais nova não aparecem de novo — quem quiser o detalhe completo lê o histórico.

**Kelsen (Legal):**
- Vaga de estacionamento — dimensão mínima (COES Art. 29, 25 m²/vaga com manobra) — não duplique; Skill de 07/10 v1.0 (`vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj`).
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
- Levantamento topográfico/cadastral orientado ao DULI (LICIN 2.0) — não duplique; Skill de 05/10 (v1.5 em 07/10).
- NBR 6492:2021 — memoriais e entregáveis por etapa — não duplique; Skill de 06/10 (v1.1 ativa-com-ressalva).
- Ventilação cruzada / fachada poente / vidro de controle solar — não duplique sem parâmetro numérico real; coberta por Partido (16/09), Proteção Solar (17/09, v1.1→v1.3) e Vidro/INI-R (29/09 v1.2).
- COE LC 198/2019 ventilação/iluminação/pé-direito — não duplique; Skill de 21/09.
- NBR 15575-4 Emenda 2025 (desempenho térmico) — não duplique; Skill de 22/09.
- TDC/LICIN 2.0 e Partido/Conforto Térmico — não duplique; Skills de 16/09.
- NBR 9050:2020 (acessibilidade) — não duplique; Skill de 15/09 v1.1.

**Cardozo/Complementares (Baumgart, Saturnino, Landell, Tenreiro, Glaziou, Mindlin):**
- Entrada de energia Light / ligação nova RECON-BT — não duplique; Skill Landell de 05/10 v1.1.
- Contenção de escavação em argila mole / hélice contínua — não crie Skill nova; coberta pela Skill de fundações em solos moles v1.3 (confirmado 07/10).
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

**Última atualização:** 08/10/2026 (Fechamento do Dia de 07/10, rodou com atraso — rodadas de 29/09, 01/10, 02/10 e 05/10 movidas para `rotina_fechamento_historico.md`; consolidado ganhou os temas de 05-07/10)
**Próxima leitura:** 08/10/2026 (quinta-feira) — Diária Skills pipeline seg-qui
