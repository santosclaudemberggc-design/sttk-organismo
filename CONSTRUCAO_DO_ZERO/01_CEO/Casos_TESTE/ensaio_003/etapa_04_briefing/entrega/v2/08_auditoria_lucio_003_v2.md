# Auditoria de Lúcio — Etapa 04 (Briefing), Ensaio Sombra 003, v2 — rodada de correção 13/10/2026

**Auditor:** Lúcio (Gestor Arquitetura). **Autor das peças:** Oscar (correção de 13/10, primeiro plano).
**Regra desta auditoria:** verificação sem prova colada = não feita. Cada item traz o comando e a saída (ou trecho com linha). Caso fictício.
**Escopo das buscas:** só dentro de `...\etapa_04_briefing\entrega\v2\` e dos arquivos de fonte citados. A pasta de material lacrado do ensaio não foi aberta, lida, listada nem buscada por Lúcio. O termo da pasta não aparece neste arquivo.

---

## Item 1. SMD: 57,18 m² (TO 50%), rótulo, retirada do "12%" — FEITO

**Comando:** Grep `68,62|68\.62|12%` em `*_v2.md`.
**Saída (resumo):**
- `checagem_oscar_v2.md`: 3 linhas, todas descrevendo a troca (declaração de antes/depois, não conteúdo vigente).
- `08_auditoria_lucio_003_v2.md`: linha da tabela antiga (esta versão a substitui).
- Nenhuma ocorrência de 68,62 ou 12% como valor vigente em 01, 02, 03, 04, 05, 06, 07 (versões `_v2`).

**Comando:** Grep `57,18` em `*_v2.md`.
**Saída (trechos):**
- `01_briefing_corpo_003_v2.md:45` (P6): "dá **57,18 m²** com TO 50%: 571,80 × (1 − 0,50) × 0,20."
- `01_briefing_corpo_003_v2.md:123` (P-h): "20% da área livre da TO máxima, 57,18 m² com TO 50%"
- `01_briefing_corpo_003_v2.md:148` (§8 item 6): "20% × 285,90 = 57,18 m²"
- `02_planilha_ambientes_003_v2.md:66` (§2.4): "20% × 285,90 = **57,18 m²** (E-28)"
- `05_anexo_contas_briefing_003_v2.md:103` (E-28): "SMD = 20% × 285,90 = **57,18 m²**"
- `07_bloqueios_003_v2.md:35` (§4): "com TO 50%: 57,18 m²"

**Rótulo** (Grep `TO 50% do RIU do dossiê, não conferida no Dec. 3.046 \(lacuna\); SMD em aberto para Kelsen`): presente em 01 (P6, P-h, §8), 02 (§2.4, §4), 05 (E-28), 07 (§4). Confere com a instrução.

**Residuais fora do escopo desta correção (arquivos sem sufixo `_v2`, de outra execução, não são nossos):** `01_briefing_corpo_003.md`, `02_planilha_ambientes_003.md`, `05_anexo_contas_briefing_003.md` e `07_bloqueios_003.md` ainda trazem 68,62. Não foram alterados e não são base desta entrega.

---

## Item 2. Consistência com a Etapa 01 — FEITO, com correção de referência

**Instrução recebida:** "Etapa 01, §1, linha 14".
**Verificado por Lúcio:** Grep `daria 10%` em `etapa_01_legal_base\entrega\parecer_legal_base_003.md`.
**Saída:** `parecer_legal_base_003.md:36`: "Mecanismo geral da LC 270 (SMD = 20% da área livre da TO máx.) daria 10%". Esta é a linha do quadro (parâmetro 14). A instrução dizia linha 14; o Oscar citou a linha 36, e a linha 36 é a correta.
**Conta registrada em 01 §7 e 05 E-28:** 20% × 50% = 10% de 571,80 = 57,18 m². Consistente.
**Etapa 01:** não alterada (não foi tocada em nenhuma das rodadas).

---

## Item 3. Dado de terreno (571,80 × 600,00) como pergunta aberta — FEITO

**Comando:** Grep `P1\. ` em `01_briefing_corpo_003_v2.md`.
**Saída:** linha 35: "**P1. Área do lote: PERGUNTA ABERTA, NÃO FECHADA.** Dois valores, cada um com a fonte". Dois valores com fonte; nenhum escolhido.

**Fontes conferidas por Lúcio (Grep em `caso_sombra_003.md`):**
- 571,80 m²: linha 52, dentro de `### 5.2` (levantamento). Medida.
- 600,00 m²: linha 46 (descrição do lote), linha 66 (tabela de `### 5.3` RIU, "Área do lote no cadastro"), linha 94 (`### 5.6`, "Área do lote adotada: **600,00 m²**").
- A linha 94 mostra que o próprio caso usa 600,00 como "adotada" num estudo de 2024 (`### 5.6`). Por isso a divergência fica aberta para Kelsen, não resolvida.

**Etapa 01 §2.1 (Grep no parecer, linha 56):** "Decisão: calcular sobre 571,80 m²". Foi uma decisão de cálculo da Etapa 01, não premissa deste Briefing. Registrada como tal.

**Frase "O Legal recomenda 571,80" removida:** Grep `Legal recomenda` em `*_v2.md` → 0 ocorrências. (Restam só em `01_briefing_corpo_003.md:112` e `04_matriz_decisoes_cliente_003.md:49`, sem sufixo, não nossos.)

**Contas com 600,00 registradas como cenário:** Grep `240,00|480,00|150,00` → `05_anexo_contas_briefing_003_v2.md:11` e `01_briefing_corpo_003_v2.md:40`. Os valores vêm de `parecer_legal_base_003.md`, §2.2, linhas 66-72 (verificado por Lúcio: 0,40 × 600 = 240; mín(600; 480) = 480; 0,25 × 600 = 150).

**Desvio do relatório do Oscar:** ele citou a linha 66 como "§5.3" (correto) e o `### 5.1` como fonte dos 600 (a fonte de 600 é `### 5.1` na linha 46 e `### 5.3` na linha 66, e a linha 94 em `### 5.6`). Nenhuma escolha foi feita.

---

## Item 4. Citação de página com nome da cópia (COES e LC 270) — PARCIAL

**Regra (01, legenda, linha 10):** "COES p. N, Art. X (cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf)". LC 270: `LC270_2024_PlanoDiretorLUOS.pdf`.

**Comando:** Grep `(COES|LC 270|LC270)[^\n]{0,40}p\. ?[0-9]+` em `*_v2.md` (amostra, saída limitada a 120 linhas).
**Saída:** todas as linhas de amostra com página de COES ou LC 270 trazem o nome da cópia (ex.: `07_bloqueios_003_v2.md:32`: "COES Art. 31 V (p. 17, cópia COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf, [lido v2])"; `02_planilha_ambientes_003_v2.md:46`: "LC 270 Art. 347 II (p. 124, cópia LC270_2024_PlanoDiretorLUOS.pdf [lido v2])").

**Residuais encontrados por Lúcio:**
- `06_declaracao_leitura_003_v2.md:49`: "COES pp. 5, 15, 17; LC 270 pp. 122, 124, 125)" — **sem nome da cópia**. Falha.
- `06_declaracao_leitura_003_v2.md:44`: a lista "LC 270 (pp. 79-80, 97, 123, 126, 130, Anexo XXI; cópia LC270...)" traz o nome uma vez para várias páginas. Pela regra ("cada página deve trazer o nome"), é insuficiente. Marcado como parcial.
- A contagem de Oscar (92 linhas antes/depois) não foi reproduzida por Lúcio. Não é usada como prova.

**Dec. 3.046, LC 281, LC 301:** a legenda de 01 manda o mesmo padrão, mas a regra desta rodada cobre COES e LC 270. Não auditado aqui.

**Status:** PARCIAL. Falta corrigir 06 linhas 44 e 49. Não corrigido por Lúcio, porque a correção é do autor (Oscar).

---

## Item 5. Esquemas em escala adiados, com dono e motivo — FEITO (mantido)

**Comando:** Grep `adiad` em `*_v2.md`.
**Saída:**
- `03_organograma_esquemas_003_v2.md:95`: "**Esquemas gráficos do item 5.2.1 b: adiados para a Etapa 05**, sem escala e sem dimensão fixada. **Motivo:** a Etapa 04 proíbe desenho (...). **Dono:** Oscar e Lúcio."
- `07_bloqueios_003_v2.md` §4 (linha 24): "Esquemas em escala (PN-ARQ 5.2.1 b): adiados para a Etapa 05", com motivo e dono no mesmo bloco.
- `04_matriz_decisoes_cliente_003_v2.md:84`: remissão ao adiamento.

**Ressalva:** `01_briefing_corpo_003_v2.md:146` (§8 item 4) ainda diz "Organograma em diagrama (03, §1, em texto e ASCII)". Oscar afirmou que "ASCII" não aparece; o termo aparece nesta linha. Resíduo menor, não corrigido.

---

## Item 6. Contagem de palavras — FEITO (pendente de Wallenberg, sem número)

**Comando:** Grep `palavra` em `*_v2.md`.
**Saída:** "a fazer por Wallenberg com ferramenta" em 01 (linha 6 e 158), 04 (linha 82), 06 (linha 54), 07 (linha 11). Nenhum número de palavras e nenhum "~" associado.
**Confirmação:** o item 6 da instrução é não inventar número. Está cumprido. A contagem continua pendente de Wallenberg.

---

## Item 7. Auditoria com prova — FEITO (esta peça)

Esta peça foi reescrita por Lúcio. Não reproduz a versão anterior, que dizia "Feito" para SMD 68,62 e para o item 6 sem prova.

---

## Ressalvas de processo (declaradas, não resolvidas)

1. **Busca ampla em `ensaio_003`:** o relatório do Oscar informa um Glob `*.md` na pasta `ensaio_003` com 129 resultados (100 exibidos). Lúcio não viu a lista. Não é possível afirmar se algum nome da pasta de material lacrado apareceu nela. Não é abertura nem leitura de conteúdo, mas a regra proíbe citar ou listar. Registrado para Wallenberg decidir se isso exige tratamento.
2. **Declarações de Oscar em 06 (seção A) e checagem:** citam "Glob amplo ... listou os nomes de etapas, pareceres e entregas". Mesma ressalva do item 1.
3. **Arquivos sem sufixo `_v2` na mesma pasta** continuam com valores antigos (68,62, "Legal recomenda"). Não são base desta entrega e não foram alterados.

---

## Resumo de status

| # | Item | Status | Prova |
|---|---|---|---|
| 1 | SMD 57,18 (TO 50%), rótulo, sem "12%" | FEITO | Grep `57,18` (6 arquivos) e `68,62\|12%` (só em checagem e nesta peça) |
| 2 | Consistência com Etapa 01 | FEITO (linha 36, não 14) | `parecer_legal_base_003.md:36` "daria 10%" |
| 3 | Terreno 571,80 × 600,00 aberto | FEITO | `01 P1` linha 35; `caso_sombra_003.md` linhas 46, 52, 66, 94 |
| 4 | Nome da cópia em cada página COES/LC 270 | PARCIAL | `06` linhas 44 e 49 sem nome completo |
| 5 | Esquemas em escala adiados, com dono e motivo | FEITO (mantido) | `03` linha 95; `07` §4 |
| 6 | Contagem de palavras sem número | FEITO (pendente Wallenberg) | Grep `palavra` |
| 7 | Auditoria com prova | FEITO | esta peça |

**Pendências para o autor (Oscar):** corrigir 06 linhas 44 e 49 (nome da cópia); tirar "ASCII" de 01 §8 item 4.
**Pendências de decisão:** Kelsen decide P-h (TO 50% da SMD) e P-a (571,80 × 600,00). Wallenberg faz a contagem de palavras e decide a ressalva 1.
