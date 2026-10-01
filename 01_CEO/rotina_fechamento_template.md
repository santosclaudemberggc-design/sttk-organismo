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

## [2026-09-28] — Diária Skills v3.2 (Segunda) — RODADA COMPLETA (2 Skills ativadas)

### RODADA ATUAL (O que foi entregue)

- [x] **Dia confirmado:** `(Get-Date).DayOfWeek` = Monday. Início às 08:38. Pipeline seg-qui.
- [x] **Saturnino, `reservatorio-retardo-decreto23940-aguas-pluviais-rj` v1.1:** ativa-com-ressalva e instalada. Decreto 23.940/2004 e Res. Conj. 001/2005 lidos no texto primário (PDFs extraídos com pypdf porque o WebFetch devolveu binário). Cardozo leu os dois PDFs inteiros: PROCEDE COM RESSALVA, com 4 correções aplicadas.
- [x] **Kelsen, `varandas-nao-computaveis-ate-to-coes-lc198-rj` v1.1:** ativa-com-ressalva e instalada. COES Art. 8º §4º (varanda residencial fora da ATE e da TO). Kelsen conferiu no consolidado da SMU, sem alteração, e acrescentou o Dec. 45.917 Art. 6º (5 m entre varandas em grupamento).
- [x] **Lúcio:** sem Skill. A lacuna de vidro de controle solar é real, mas as fontes não trazem números.
- [x] **Feed:** 2 eventos, 2/2 OK.
- [x] **Livro-razão:** entrada 28/09 em `Setembro.md`, com "como desfazer". Primeira entrada da Diária seg-qui desde 10/09.
- [x] **Backups:** `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/` (3 arquivos).
- [~] **/watch (v3.3.1):** Lúcio assistiu de verdade "EP14 - Vidros com controlo solar" (youtube.com/shorts/Z0buYmS8fDE), mas as legendas deram 429 e a extração de quadros do script falhou (o ffmpeg novo não aceita `-vsync`). Tirei os quadros com ffmpeg direto e vi 4. É conversa comercial (Portugal) sem parâmetro técnico, então não gerou Skill. Kelsen e Cardozo: a busca de vídeo não achou material relevante (só notícias e texto).
- [ ] **Passo 8 (Trilha B):** não rodou. Nenhum `_estado_` trouxe lacuna de ferramenta nesta rodada.

### O QUE FICOU PENDENTE (Cuidado: não repita)

- **Lúcio corrige a Skill de partido de 16/09** (linhas 70-72). O limite de 20% da área útil vem do §5º do COES (não residencial). Kelsen recomenda retirar a "projeção máxima 2 m (Dec. 7336/1988)".
- **Kelsen R1:** a Barra/Recreio (LC 270/2024 com o Dec. 3046/81 incorporado) tem regra própria de cômputo de varanda? Hely confirma no RIU/SMDU.
- **Remissão cruzada:** `legal-base-legislativa-bairro`, linha 85, apontar para a Skill de varandas (Kelsen, com backup).
- **Saturnino:** texto da Lei Estadual 9.164/2020 na ALERJ; Decretos 26.168/2006 e 32.119/2010; vigência do rito pós-LICIN 2.0; conflito de uso com a NBR 16783 (descarga sanitária).
- **Bug do /watch:** `scripts/frames.py` usa `-vsync`, que o ffmpeg instalado já não aceita (trocar por `-fps_mode`). É plugin de terceiro, então não editei; decisão de Claudemberg. O 429 nas legendas voltou (o mesmo de 24/09).
- **Orçamento:** foram 7 WebSearch, e não 6. A 7ª localizou o texto primário da LC 198, porque a busca de Kelsen só trouxe a matéria indireta.
- Continuam valendo as pendências de 25/09 (Lint: duplicata no `indice.md`, contradição nbr6122 x fundações Barra, LC 301, span do Painel, livro-razão no prompt agendado).

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

**Última atualização:** 30/09/2026 (Fechamento do Dia v1.0 — 1ª execução deste formato: template reduzido a 2 rodadas + consolidado; rodadas de 01/09 a 25/09 movidas para `rotina_fechamento_historico.md`)
**Próxima leitura:** 01/10/2026 (quinta-feira) — Diária Skills pipeline seg-qui
