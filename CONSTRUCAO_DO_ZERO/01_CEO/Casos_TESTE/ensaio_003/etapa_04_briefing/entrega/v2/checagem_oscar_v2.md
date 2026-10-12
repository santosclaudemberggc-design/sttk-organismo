# Checagem de Oscar — Etapa 04 (Briefing), Ensaio Sombra 003, v2 — 12/10/2026

Prova de cada correção (1 a 8) da rodada. Sem prova, o item está marcado como não feito. Os comandos são as buscas (Glob, Grep, Read) feitas nesta execução. Pasta: `...\etapa_04_briefing\entrega\v2\`.

**Aviso de colisão de arquivos (ver item 1):** a pasta `v2\` tem também os arquivos `01_briefing_corpo_003.md`, `02_planilha_ambientes_003.md`, `03_organograma_esquemas_003.md` e `04_matriz_decisoes_cliente_003.md`, sem o sufixo `_v2`. Não são destes autor (cabeçalho "refação v2, pedida por Lúcio"; "Revit indisponível nesta sessão"). Não os abri além do cabeçalho e não os alterei. Nenhum destes quatro foi usado como prova.

---

## Item 1. Presença dos arquivos da v2 (Glob)

**Comando:** Glob `*` em `...\entrega\v2`.
**Saída (resumo, com o nome exato):**
- `01_briefing_corpo_003_v2.md` (meu)
- `02_planilha_ambientes_003_v2.md` (meu)
- `03_organograma_esquemas_003_v2.md` (meu)
- `04_matriz_decisoes_cliente_003_v2.md` (meu)
- `05_anexo_contas_briefing_003_v2.md` (meu)
- `06_declaracao_leitura_003_v2.md` (meu)
- `07_bloqueios_003_v2.md` (meu)
- `08_auditoria_lucio_003_v2.md` (meu)
- `checagem_oscar_v2.md` (meu)
- `01_briefing_corpo_003.md`, `02_planilha_ambientes_003.md`, `03_organograma_esquemas_003.md`, `04_matriz_decisoes_cliente_003.md` (**não são meus**; ver aviso)

**Prova de conteúdo dos meus arquivos:** Read de `01_briefing_corpo_003_v2.md` (linhas 1 a 4): cabeçalho "Etapa 04 — Briefing (corpo) — v2"; Read de `01_briefing_corpo_003.md` (linhas 1 a 6, não meu): cabeçalho "refação v2, pedida por Lúcio".
**Status:** FEITO. Oito peças e a checagem, todas com sufixo `_v2`. Colisão com quatro arquivos de outra execução: registrada, não resolvida (decisão de Lúcio ou Wallenberg).

---

## Item 2. Gabarito não tocado

**Comando:** Grep `LACRADO|_gabaritos` em `...\entrega\v2` (modo conteúdo).
**Saída:**
- `08_auditoria_lucio_003_v2.md:13`: "Grep por `LACRADO` e `_gabaritos` nas peças v2..." (declaração de busca, não leitura).
- `06_declaracao_leitura_003_v2.md:36`: "A pasta de gabaritos lacrados (`_gabaritos_LACRADO_bardi`) ... nenhum arquivo aberto, lido, citado, listado ou buscado nesta execução."
- Nenhuma outra ocorrência, inclusive nos quatro arquivos de outra execução.

**Status:** FEITO. Nenhuma citação de gabarito como fonte. A palavra "gabarito" usada no sentido urbanístico (altura e pavimentos) é outro uso.

---

## Item 3. NBR 9050: edição 2020 marcada como não conferida

**Comando:** Glob `**/*9050*` em `D:\008_Normas ABNT`.
**Saída:** `D:\008_Normas ABNT\001_ABNT\01_Arquitetura\NBR 9050-2015 Acessibilidade (DESATUALIZADA - vigente 2020).pdf` (único arquivo).
**Prova na peça:** `05_anexo_contas_briefing_003_v2.md`, V-40 ("A edição 2020 não está no acervo e não foi conferida. Fica FORA DO ORGANISMO."); `07_bloqueios_003_v2.md`, item 3.
**Status:** FEITO. Conteúdo do PDF de 2015 não aberto. Nenhum número da Skill usado.

---

## Item 4. Organograma em diagrama; esquemas em escala adiados

**Comando:** Grep `ASCII|diagrama|adiad` em `03_organograma_esquemas_003_v2.md`.
**Prova:** `03_organograma_esquemas_003_v2.md` §1.1 (diagrama em bloco de código, relação entre ambientes e fluxos F1 a F8); §3 ("Esquemas gráficos do item 5.2.1 b: adiados para a Etapa 05, sem escala e sem dimensão fixada").
**Comando:** Grep `diagrama|adiad|ASCII` em `03_organograma_esquemas_003_v2.md` (modo conteúdo). **Saída:** linha 3 ("Esta peça é texto, tabela e diagrama simples"), linha 46 ("Leitura do diagrama:"), linha 95 ("Esquemas gráficos do item 5.2.1 b: adiados para a Etapa 05"). A palavra "ASCII" não aparece; o diagrama é o bloco de código da §1.1.
**Fonte da norma:** NBR 6492:2021, 5.2.1 a) e b). Citação herdada da v1 (PDF p. 15), **não reaberta nesta execução [nv]**.
**Status:** FEITO quanto ao diagrama e ao adiamento. Fonte da norma: parcial (não reaberta).

---

## Item 5. Tabela computável × não computável, com números e artigos

**Comando de conta (aritmética conferida):**
- 520 − 457,44 = 62,56 (confere com E-12).
- 4 × 12,50 = 50,00 (confere com E-18).
- 2 × 228,72 = 457,44 (confere com E-2).

**Prova na peça:** `01_briefing_corpo_003_v2.md` §4-bis (tabela L1 a L9 com artigos); `05_anexo_contas_briefing_003_v2.md`, E-27; `02_planilha_ambientes_003_v2.md` §2.1 e §2.2.
**Artigos abertos nesta execução:** COES Art. 29 I e II (p. 15, [lido v2]); LC 270 Art. 347 II e VII (p. 124, [lido v2]); LC 270 Art. 350 III e V (p. 125, [lido v2]); COES Art. 8º §4º (p. 5, [lido v2]).
**Status:** FEITO, com lacuna declarada. A soma de não computáveis fixada (50,00) não fecha. Faltam manobras (n a definir) e varandas (V a definir). P-o pendente. Contas E-15 e E-16 dependem de "a" e não foram re-derivadas.

---

## Item 6. SMD: 12% sobre área livre, rotulada, divergência registrada

**Comando de conta:** 1 − 0,40 = 0,60; 571,80 × 0,60 = 343,08; 343,08 × 0,20 = 68,616 → 68,62. Também 571,80 × 0,12 = 68,616 → 68,62.

**Comando:** Grep `68,62` em `...\v2\` (modo contagem). **Saída, só dos meus arquivos:** `01_briefing_corpo_003_v2.md:4`, `02_planilha_ambientes_003_v2.md:2`, `05_anexo_contas_briefing_003_v2.md:2`, `07_bloqueios_003_v2.md:1`, `08_auditoria_lucio_003_v2.md:1`, `checagem_oscar_v2.md:3`. Não aparece em `04_matriz_decisoes_cliente_003_v2.md`, então a matriz não usa o número. Os arquivos sem sufixo `_003.md` (de outra execução) também contêm 68,62 (01: 4; 02: 3; 05: 9); não são prova deste autor.
**Rótulo:** "RIU do dossiê; SMD em aberto (P-h)" em `01_briefing_corpo_003_v2.md` P6 e `02_planilha_ambientes_003_v2.md` §2.4.
**Divergência:** "10%" da Etapa 01 (§1, linha 14) registrada em `01_briefing_corpo_003_v2.md` §7 e E-28; não resolvida.
**Artigo aberto nesta execução:** LC 270 Art. 352 caput (p. 125, [lido v2]): "vinte por cento da área livre do terreno resultante da aplicação da Taxa de Ocupação máxima".
**Status:** FEITO. Número 142,95 mantido como operacional (mais restritivo), com a SMD em aberto.

---

## Item 7. Citação de página do COES com o nome da cópia usada

**Prova de leitura nesta execução (PDF por página, [lido v2]):**
- COES, `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`, p. 5: Art. 8º §§1º a 9º. Confirmados: §1º (recuo de 1,00 m da testada), §2º (2,50 m das divisas), §3º (1,50 m não afastada), §4º (não computa ATE e TO), §5º (20% não residencial), §6º (aeração de 50% do vão).
- COES, p. 15: Art. 29 I a V, confirmados.
- COES, p. 17: Art. 31 I a VI e parágrafo único, confirmados (V = acessibilidade; III = vagas; parágrafo único = 1,50 m).
- LC 270, `LC270_2024_PlanoDiretorLUOS.pdf`, p. 122: Art. 345 §1º I (CAB ≤ 1) e §3º (sem OODC onde CAB = CAM).
- LC 270, p. 124: Art. 347 II e VII; Art. 349 (TO).
- LC 270, p. 125: Art. 350 caput, I, III, IV, V; Art. 352 caput (SMD).

**Citações com cópia nomeada na peça:** `05_anexo_contas_briefing_003_v2.md`, cabeçalho da Seção V e Seção V.
**Citações não reabertas [nv]:** Dec. 3.046 (pp. 2-5); LC 281 (pp. 2-8); LC 301 (p. 38); NBR 6492 (PDF pp. 14-15); LC 270 pp. 79-80, 97, 126, 130 e Anexo XXI; COES pp. 3, 13, 29.
**Status:** PARCIAL. Páginas do COES e da LC 270 acima foram abertas nesta execução. Demais citações marcadas [nv] com a fonte de origem (v1 ou Etapa 01). A auditoria de Lúcio deve ver essa separação.

---

## Item 8. checagem_oscar_v2.md com prova

Este arquivo. Cada item tem comando (ou leitura) e saída. Itens 1 a 7 com prova acima.
**Contagem de palavras:** não feita (sem ferramenta). Pendente de Wallenberg. Nenhum número estimado.
**Status:** FEITO, com a contagem de palavras pendente por limite de ferramenta.

---

## Resumo de status

| # | Correção | Status |
|---|---|---|
| 1 | Dez Skills declaradas e duas aplicadas | Feito (05 seção S; 01 P12) |
| 2 | Isca 3: CAB = CAM = 1,0 e consequência | Feito, com ressalva da linha 53 da Skill |
| 3 | NBR 9050 2020 não conferida | Feito |
| 4 | Organograma em diagrama; esquemas adiados | Feito (fonte da norma não reaberta) |
| 5 | Tabela computável × não computável | Feito, lacuna declarada (soma não fecha) |
| 6 | SMD 12% = 68,62 m², rotulada, divergência registrada | Feito |
| 7 | Página do COES com nome da cópia | Parcial (demais páginas [nv]) |
| 8 | checagem com prova | Feito |
