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

**Manutenção [v1.0 — 30/09/2026]:** o Fechamento do Dia (20:00) mantém este arquivo com só as 2 rodadas mais recentes + a seção consolidada "O QUE NÃO FAZER (acumulado)" no fim. Rodadas mais antigas vão, inteiras, para `CONSTRUCAO_DO_ZERO/01_CEO/rotina_fechamento_historico.md` — nada é apagado.

---

## [2026-10-20] -- Diaria Skills v3.5.0 (Terça) -- PIPELINE LINEAR (sem Skill nova)

### RODADA ATUAL (O que foi entregue)
- Pré-rodada: `(Get-Date).DayOfWeek` = Tuesday (09:07). Passagem de 19/10 lida. Lacunas abertas: nenhuma com `alc: auto` (todas humano/tecnico), prioridade zero não se aplica.
- Passo 0.6 (Registro de Erros): 3 propostas novas em `Registro_Erros/propostas_do_dia.md`: P-2026-10-19-05 (gabaritos LACRADO dentro do repositório, verificado: pasta existe e git rastreia 3 arquivos), E-2026-10-19-02 (Skill de acessibilidade contradiz habite-se; Lúcio confirmou com ajuste, sem edição) e P-2026-10-19-02 (Bardi sem hash). Evento `decisao` gravado no feed. Nada aprovado.
- Passo 1 (pesquisa): 6 buscas (2 por Gestor). Kelsen: Mais-Valia, prazo de obras executadas (30/06/2026) venceu segundo notícias; a Skill `legal-oodc-mais-valera-mais-valia` já marca esse conflito como "em aberto". LC 301 já coberta. Lúcio e Cardozo: nada primário e novo para Barra/Recreio. Vídeo: nenhum achado relevante; nenhuma busca de Kelsen foi direcionada a vídeo (desvio da regra de 1 em 2).
- Nenhuma Skill criada, nenhuma Skill alterada.

### PENDENTE E BLOQUEADO
- Propostas E-03, E-01, P-04 (ontem) e P-05, E-02, P-02 (hoje) aguardam Claudemberg.
- Layout residencial (Lúcio): caso Yamada (PDF UFRGS) não lido, ECONNRESET. Repetir a leitura antes de propor nova versão da Skill de layout.
- Caminho de `Skills_Propostas` não localizado por Glob (já ocorreu antes). Conferir com Test-Path.

### O QUE TOMAR CUIDADO
- Glob não listou a pasta `_gabaritos_LACRADO_bardi`, mas ela existe. Use Test-Path antes de concluir que algo sumiu.
- Não editar `arquitetura-nbr9050-acessibilidade` antes da aprovação de E-02.

---

## [2026-10-19] -- Diaria Skills v3.6.0 (Segunda) -- PIPELINE LINEAR (sem Skill nova)

### RODADA ATUAL (O que foi entregue)
- Pré-rodada: `(Get-Date).DayOfWeek` = Monday (09:07). Passagem de 16/10 lida.
- Passo 0.6 (Registro de Erros): 3 propostas em `Registro_Erros/propostas_do_dia.md` (E-03 imagem obrigatória no "Atende" de vista; E-01 tabela de herança recebida; P-04 script de conferência das 3 cópias). Nada aprovado; `aprovacao` vazia. Evento `decisao` gravado no feed.
- Passo 1-2 (pesquisa): 6 buscas (2 por Gestor). Kelsen (LICIN 2.0, LC 281): só o Decreto 55.622 de 2025, sem atualização para Barra/Recreio. Lúcio (conforto, fachada poente): fontes genéricas, nada primário sobre o Rio. Cardozo (SPT, lençol, solo mole): material genérico, sem laudo da Barra. Nenhum vídeo relevante achado, então `/watch` não rodou. Sem material viável: nenhuma Skill nova.
- Lacuna prioridade zero `lacuna-kelsen-lc270-anexo-xxi-to-zona-14-10-2026`: Kelsen leu o Anexo XXI da LC 270 (fonte `Fontes_Legislacao/LC270_2024_PlanoDiretorLUOS.pdf`, pp. 274-277), leitura visual. A TO da ZPP fica em "ver Dec. 3.046/81", então a SMD da ZPP não fecha só por esta fonte. Lacuna segue ABERTA: falta a subzona real do lote (RIU) e o Cap. III do Dec. 3.046. Erro no mapa do Hely (A-18 deveria ser A-19) registrado para correção.
- Não rodou: Passo 4 (Skill nova), Passo 8 (trilha B), Macetes e Acervo (só não rodam nesta rodada por regra de dia).

### PENDENTE E BLOQUEADO
- Anexo XXI: falta subzona do lote (RIU) e Cap. III do Dec. 3.046 — Kelsen/Hely.
- Proposta `kelsen_anexo-xxi-taxa-ocupacao-por-zona-lc270-2024.md` em Skills_Propostas: não instalada; checar antes — Claudemberg.
- Propostas E-03, E-01, P-04 aguardam aprovação — Claudemberg.

### O QUE TOMAR CUIDADO
- Pesquisa sem lacuna aberta não gera entrega (P-2026-10-19-08): hoje houve lacuna, então a busca foi justificada.
- A leitura do PDF do Anexo XXI foi visual: confirmar o texto antes de citar número.

---

## O QUE NÃO FAZER (acumulado)

Consolidado em 30/09/2026 a partir de todas as rodadas de 01/09 a 29/09 (movidas para `CONSTRUCAO_DO_ZERO/01_CEO/rotina_fechamento_historico.md`). Itens já resolvidos/superados por rodada mais nova não aparecem de novo — quem quiser o detalhe completo lê o histórico.

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
