# Checagem de Oscar — Etapa 04 (Briefing), Ensaio Sombra 003, v2 — 12/10/2026

Prova de cada correção (1 a 8) da rodada. Sem prova, o item está marcado como não feito. Os comandos são as buscas (Glob, Grep, Read) feitas nesta execução. Pasta: `...\etapa_04_briefing\entrega\v2\`.

**Aviso de colisão de arquivos (ver item 1):** a pasta `v2\` tem também os arquivos `01_briefing_corpo_003.md`, `02_planilha_ambientes_003.md`, `03_organograma_esquemas_003.md` e `04_matriz_decisoes_cliente_003.md`, sem o sufixo `_v2`. Não são destes autor (cabeçalho "refação v2, pedida por Lúcio"; "Revit indisponível nesta sessão"). Não os abri além do cabeçalho e não os alterei. Nenhum destes quatro foi usado como prova.

---

## RODADA DE 13/10/2026: correções 1 a 7 (com prova)

Autor: Oscar. Escrita só em arquivos `_v2` desta pasta e nesta checagem. Não editei 08 (Lúcio), os quatro arquivos sem sufixo (outra execução), a Etapa 01, Skills, enunciado ou caso. Sem git, sem apagar. Greps feitos na pasta `...\entrega\v2\`, com glob `0[1-7]_*_v2.md` (01 a 07) ou `0[1-8]_*_v2.md` (01 a 08).

**Correção 1: SMD com TO 50%, 57,18 m².**
- Grep `68,62|68\.62|12%`, arquivos 01 a 08. Antes (estado de 12/10): 01 com 4 linhas (P6, P-h, §7, §8 item 6); 02 com 2 (§2.4 e §4); 05 com 2 (E-28); 07 com 1 (item 4); 08 com 1. Total em 01 a 07: 9 linhas.
- Depois, em 01 a 07: **0 linhas**. Única ocorrência restante: `08_auditoria_lucio_003_v2.md:24` (arquivo de Lúcio, não editado; a reescrita é dele).
- Grep do rótulo "TO 50% do RIU do dossiê, não conferida no Dec. 3.046 (lacuna); SMD em aberto para Kelsen": 8 ocorrências em 4 arquivos (01: 4; 02: 2; 05: 1; 07: 1). São os mesmos lugares em que a SMD aparecia.
- Grep `12%` em 01 a 07: 0. Não sobra "12%" ligado à SMD.
- Conta em 05 E-28: 571,80 × (1 − 0,50) = 285,90 m²; 20% × 285,90 = 57,18 m².

**Correção 2: ligação com a Etapa 01.** Escrito em 01 §7 e 05 E-28: "Consistente com a Etapa 01, §1, quadro, parâmetro 14 ('daria 10%', linha 36 do parecer)". **Desvio da instrução:** a instrução dizia "linha 14". Lido em `parecer_legal_base_003.md`: a linha 14 é a regra de comparação; "daria 10%" está na linha 36 (quadro, parâmetro 14). Por isso a citação foi corrigida para a linha 36. Não está escrito que a Etapa 01 foi corrigida.

**Correção 3: área do lote como pergunta aberta.** 01 P1 reescrito, com as duas fontes: 571,80 m² (caso §5.2, linha 52; enunciado da Etapa 04, linha 35) e 600,00 m² (caso §5.1, linha 46; caso §5.3, linha 66, RIU "Área do lote no cadastro"). Caso linha 94, seção 5.6: "Área do lote adotada: 600,00 m²" (estudo de 08/2024), que contradiz o próprio caso. **Desvio da instrução:** a instrução dizia "linha 66, seção 5.1". A linha 66 está na §5.3 (RIU), e foi citada assim. Frase "O Legal recomenda 571,80" retirada de P-a. A mesma frase estava em 04 B-01 ("Legal recomenda", "Confirmado 571,80"): também retirada. Grep "Legal recomenda|O Legal recomenda" em 01 a 08: 0 linhas. 05 topo: nota de base aritmética e cenário de 600,00 m² (projeção 240,00; teto 480,00; permeável 150,00; parecer da Etapa 01, §2.2, linhas 66 a 72, [nv]).

**Correção 4: nome da cópia em toda citação de página.**
- Regra: escrita na legenda de 01 (linha 10). **Desvio da instrução:** a instrução dizia que a regra já estava na linha 10 de 01, e não estava. Foi acrescentada agora.
- Nomes reais confirmados por Glob em `Fontes_Legislacao` (pasta do Hely): `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`; `LC270_2024_PlanoDiretorLUOS.pdf`; `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`; `LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`; `LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf`. Nenhuma "cópia não identificada".
- Antes: 95 linhas com citação de página em 01 a 08 e nesta checagem (contagem de 12/10). O nome da cópia aparecia só em listas de arquivos (05, abertura da seção V; 06, itens 10 e 11), não na citação.
- Depois, Grep de citação de página (COES, LC 270, LC 281, LC 301, Dec. 3.046), arquivos 01 a 07: **92 linhas** com página. Grep do nome da cópia nos mesmos arquivos: 01: 22; 02: 25; 03: 6; 04: 12; 05: 33; 06: 1 (a outra linha, itens 10 e 11, traz o nome no próprio caminho do arquivo); 07: 9. Em cada arquivo, as linhas com nome são pelo menos tantas quanto as linhas com página.
- Limite declarado: a conferência é por linha e por arquivo, não por ocorrência. Citações só de artigo, sem página (ex.: LC 270 Art. 354 §7º no corpo de 01, P3), não receberam o nome, salvo as que 07 §6 lista.
- 07 §6 (atenção especial): todas as citações [nv] com nome, inclusive LC 270 Art. 354 §7º, Art. 345 §4º III, Art. 353 §4º, Art. 363 §§2º e 3º, Art. 278 XIV, Arts. 215 e 216; Dec. 3.046 (Disp. Gerais VII, XI, XIV, XV, XXII, XXIII a); LC 281 Arts. 9, 19, 20, 22 III e 40; LC 301 Art. 58; COES Art. 28 IV e Art. 35.
- 08 (Lúcio) não editado. Tem citações antigas sem o nome; não é minha.

**Correção 5: esquemas em escala.** 03 §3 agora tem MOTIVO (a Etapa 04 proíbe desenho; escala e dimensão exigem desenho; nenhuma área de ambiente está fixada no dossiê) e DONO (Oscar e Lúcio). 07 §4 já tinha motivo (linha 27, "O enunciado proíbe desenho") e dono (linha 28). Grep "Motivo:|Dono: Oscar e Lúcio": 03 linha 95 e 07 linha 28. Decisão de adiamento mantida.

**Correção 6: contagem de palavras.** Grep "palavra|Wallenberg" em 01 a 07: nenhum número, nenhum "~". Menções: "a fazer por Wallenberg com ferramenta" em 01 (linhas 6 e 158), 04 (linha 82), 06 (linha 54, reescrita de "não feita") e 07 (linha 11). Item 8 desta checagem também ajustado.

**Correção 7: auditoria.** Auditoria de Lúcio (08). Nada escrito em 08.

**Item 2 da rodada de 12/10 (pasta de gabarito) reescrito sem o nome.** Grep dos dois termos de identificação (omitidos aqui), arquivos 01 a 08: só `08_auditoria_lucio_003_v2.md:13` (declaração de busca de Lúcio, arquivo dele, não editado). Zero nos arquivos 01 a 07.

**Pendências que ficam, e por quê:**
- SMD: a TO de 50% não foi conferida no Dec. 3.046 nem no Anexo XXI da LC 270 (não lido). A projeção usa TO de 40% e a SMD usa TO de 50%. Kelsen decide (P-h).
- Área do lote: 571,80 m² × 600,00 m², pergunta ao cliente e a Kelsen (P-a).
- 08 (Lúcio) ainda traz 68,62 m² e 12%: arquivo dele.
- Contagem de palavras: Wallenberg, com ferramenta.

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

**Comando (rodada 12/10, reescrito em 13/10):** Grep de dois termos de identificação do material de gabarito lacrado (termos omitidos neste texto) em `...\entrega\v2`, arquivos 01 a 08 (modo conteúdo).
**Saída:**
- `08_auditoria_lucio_003_v2.md:13`: declaração de busca de Lúcio, arquivo dele, não editado (não é leitura do material).
- `06_declaracao_leitura_003_v2.md`, seção C: frase reescrita em 13/10 como "o material de gabarito lacrado do ensaio, não aberto". Não há mais nome da pasta em 01 a 07.
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
**Artigos abertos nesta execução:** COES Art. 29 I e II (p. 15, cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf, [lido v2]); LC 270 Art. 347 II e VII (p. 124, cópia LC270_2024_PlanoDiretorLUOS.pdf, [lido v2]); LC 270 Art. 350 III e V (p. 125, cópia LC270_2024_PlanoDiretorLUOS.pdf, [lido v2]); COES Art. 8º §4º (p. 5, cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf, [lido v2]).
**Status:** FEITO, com lacuna declarada. A soma de não computáveis fixada (50,00) não fecha. Faltam manobras (n a definir) e varandas (V a definir). P-o pendente. Contas E-15 e E-16 dependem de "a" e não foram re-derivadas.

---

## Item 6 (rodada 12/10): SMD, superado em 13/10 (correção 1)

**Comando de conta (12/10, superado):** a conta com TO de 40% saiu desta checagem. A conta atual está na correção 1 de 13/10.

**Comando (12/10, superado):** o Grep daquela rodada foi substituído pelo Grep da correção 1 de 13/10.
**Rótulo (12/10, superado):** trocado em 13/10 pelo rótulo atual, idêntico em todos os lugares (correção 1).
**Divergência (12/10, superada):** ver correção 2 de 13/10. A citação correta é a linha 36 do parecer (não a linha 14).
**Artigo aberto nesta execução:** LC 270 Art. 352 caput (p. 125, cópia LC270_2024_PlanoDiretorLUOS.pdf, [lido v2]): "vinte por cento da área livre do terreno resultante da aplicação da Taxa de Ocupação máxima".
**Status:** FEITO. Número 142,95 mantido como operacional (mais restritivo), com a SMD em aberto.

---

## Item 7 (rodada 12/10): citação de página, superado em 13/10 (correção 4)

**Prova de leitura nesta execução (PDF por página, [lido v2]):**
- COES, `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`, p. 5: Art. 8º §§1º a 9º. Confirmados: §1º (recuo de 1,00 m da testada), §2º (2,50 m das divisas), §3º (1,50 m não afastada), §4º (não computa ATE e TO), §5º (20% não residencial), §6º (aeração de 50% do vão).
- COES, p. 15, cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf: Art. 29 I a V, confirmados.
- COES, p. 17, cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf: Art. 31 I a VI e parágrafo único, confirmados (V = acessibilidade; III = vagas; parágrafo único = 1,50 m).
- LC 270, `LC270_2024_PlanoDiretorLUOS.pdf`, p. 122: Art. 345 §1º I (CAB ≤ 1) e §3º (sem OODC onde CAB = CAM).
- LC 270, cópia LC270_2024_PlanoDiretorLUOS.pdf, p. 124: Art. 347 II e VII; Art. 349 (TO).
- LC 270, cópia LC270_2024_PlanoDiretorLUOS.pdf, p. 125: Art. 350 caput, I, III, IV, V; Art. 352 caput (SMD).

**Citações com cópia nomeada na peça:** `05_anexo_contas_briefing_003_v2.md`, cabeçalho da Seção V e Seção V.
**Citações não reabertas [nv]:** Dec. 3.046 (pp. 2-5, cópia Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf); LC 281 (pp. 2-8, cópia LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf); LC 301 (p. 38, cópia LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf); NBR 6492 (PDF pp. 14-15); LC 270 pp. 79-80, 97, 126, 130 e Anexo XXI (cópia LC270_2024_PlanoDiretorLUOS.pdf); COES pp. 3, 13, 29 (cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf).
**Status (12/10):** parcial. Em 13/10 todas as citações de página de 01 a 07 receberam o nome da cópia na mesma citação (correção 4 de 13/10).

---

## Item 8. checagem_oscar_v2.md com prova

Este arquivo. Cada item tem comando (ou leitura) e saída. Itens 1 a 7 com prova acima.
**Contagem de palavras:** a fazer por Wallenberg com ferramenta. Nenhum número estimado.
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
| 6 (12/10) | SMD (valor antigo, ver histórico) | Superado em 13/10 (correção 1) |
| 7 (12/10) | Página com nome da cópia | Superado em 13/10 (correção 4) |
| 8 | checagem com prova | Feito |
