# Auditoria Lúcio, 004c. Ajuste pontual da v4 (Etapa 04, Briefing)
## Ensaio Sombra 003, Montenegro Prates (caso 100% FICTÍCIO). Lúcio, 13/10/2026

**Escopo:** só os cinco pontos pedidos. Oscar editou `01`, `02`, `04`, `05` e `06` nos pontos indicados. `03` e `08` não foram tocados por pedido. Backups de todos os cinco arquivos editados: `_backups/2026-10-13/lucio_ANTES_v4-final_*` (gravados por reescrita, sem shell; contagem de linhas batida: 151, 214, 96, 61 e 153, iguais aos originais). Nenhuma busca nova, nenhum gabarito, parecer ou entrega antiga aberto por mim nesta auditoria.

**Limite:** o `03` não tem backup, então a alegação de que não foi tocado não é comprovável por mim. Os provas abaixo são buscas com `Grep`/`Read` feitas por mim agora.

---

## Veredito por ponto

| Ponto | Descrição | Veredito |
|---|---|---|
| 1 | R1, item 14 do `06` (varredura ampla) | **NÃO APROVADO (não verificado)** |
| 2 | A12, `02` linha 26 (referência M-14) | **APROVADO** |
| 3 | P-04, `+2,05` com base 159,44 | **NÚMERO CONFIRMADO; premissa de localização NÃO VERIFICADA. Não aprovado como fechado** |
| 4 | D2 em `02` A10 e `05` E-17 | **APROVADO** (com ressalva de tag [lido], ver abaixo) |
| 5 | Alternativa A, pergunta a Kelsen | **APROVADO** |

**Veredito geral da auditoria: NÃO APROVADO.** O ponto 1 não pode ser comprovado nesta execução, e a regra desta auditoria manda não aprovar nesse caso. O ponto 3 fecha só o número; a premissa de que piscina, deck e jardim cabem na locação B não tem fonte.

---

## Ponto 1. R1, item 14 do `06`

**Pedido:** deixar claro que a varredura ampla foi feita nesta execução e que nenhum nome retornado é da pasta do ensaio ou do examinador.

**Prova (Read do `06`, linha 39):**
> 14. Varredura ampla `**/Fontes_Legislacao/*.pdf` (Glob), pasta de busca `CONSTRUCAO_DO_ZERO`. **(a)** Nesta execução: **não verificado.** O resultado dessa chamada não está no contexto desta execução e a busca não foi repetida, por pedido de Lúcio. ... **(b)** Nomes retornados: **não verificado** nesta execução ...

**Análise:** o item foi reescrito com honestidade, mas o pedido era afirmar que a varredura foi feita nesta execução. O próprio Oscar declara que não tem o resultado dela no contexto. Não é possível provar, nem por mim nem por ele, que a chamada foi feita nesta execução. A declaração correta é "não verificado", e por isso o ponto não é aprovado.

**Pendência residual:** o cabeçalho da seção 1 do `06` ainda diz "Listagem (só nomes, nenhum arquivo aberto)", o que contradiz o item 14(c), que registra dois arquivos abertos. Estava fora dos cinco pontos e não foi corrigido. Decisão de Lúcio: corrigir o cabeçalho para "Listagem (nomes; dois arquivos abertos, ver 14)".

**Item 11 a 13 do `06`:** as cópias legais citadas vêm da rodada anterior de 13/10. Não foram relidas nesta execução. A declaração em §1 diz "lidas nesta execução" e precisa de correção (também fora dos cinco pontos).

---

## Ponto 2. A12, `02` linha 26

**Prova (Grep de "M-14" em `v4`):** nenhuma ocorrência no arquivo 02 nem nos demais. Só resta em `08_auditoria_lucio_004b.md` linha 105, que é o registro do defeito anterior, não a v4.

**Prova (Grep de "Consome a folga permeável"):**
> 26: | A12 | Deck | ... | Consome a folga permeável (E-10 e 04 P-04) | Cliente; Kelsen (permeável) |

**Veredito:** referência corrigida para "04 P-04", que é a linha da matriz que trata de piscina, deck e jardim. Aprovado.

---

## Ponto 3. P-04, `+2,05`

**Prova (Grep de "P-04" no arquivo 04, linha 35):**
> P-04 | Piscina, deck, jardim (caso §4) | Impermeáveis consomem a folga de 159,44 m² em H0. Com a piscina nos fundos, só a locação B fecha (+2,05). Em H1, não se presume | Peça 2 §4; Anexo E-4 | ...

**Conta refeita por mim:**
- Base de folga (05, E-10): 302,39 − 142,95 = 159,44. Confere.
- Locação B, Anexo C-12 da Etapa 03 v8 (relato de Oscar, não relido por mim): 145,00 m² (duas laterais de 72,50).
- 145,00 − 142,95 = **+2,05**. Confere aritmeticamente.
- Pela outra via: 302,39 − 145,00 = 157,39; 159,44 − 157,39 = **+2,05**. Confere.

**O que não está comprovado:** que piscina, deck e jardim caibam na locação B. O Oscar declara que as áreas de piscina, deck e jardim não constam em nenhuma fonte v8 que ele leu. A frase "só a locação B fecha" depende dessa localização, que não tem fonte. Também não relli o C-12 por mim. Por isso o número está confirmado, mas o ponto não está aprovado.

**Ressalva de sensibilidade (Oscar):** se os 0,20 m² de diferença (302,39 contra 302,19) forem permeáveis, o resultado seria +2,25. O número usado é o conservador. Isso vale para registro.

**Problema fora do escopo, não corrigido:** a coluna "Fonte" de P-04 diz "Anexo E-4", o que se confunde com as letras E-n do arquivo 05. O correto seria "Etapa 03, Anexo E, item 4". Registrado como pendência.

---

## Ponto 4. D2 em `02` A10 e `05` E-17

**Prova (Grep de "Pergunta D2"):**
- `02` linha 24, A10: "... COES Art. 31 IV, p. 17 [lido], e LC 270 Art. 350 II, p. 125 [lido]. Pergunta D2 para Kelsen (ver 01 §6, P-varanda, itens i e ii): não decidido aqui."
- `05` linha 129, E-17: "- COES Art. 31 IV (p. 17 [lido]) e LC 270 Art. 350 II (p. 125 [lido]). Pergunta D2 para Kelsen (ver 01 §6, P-varanda, itens i e ii): não decidido aqui."

**Veredito:** D2 incluída nos dois lugares, com a remissão ao P-varanda e sem decisão. Aprovado.

**Ressalva:** as tags [lido] das citações COES p. 17 e LC 270 p. 125 vêm da rodada anterior. Nesta execução não reabri esses PDFs. Por isso o texto de D2 está conforme a leitura anterior, não reconferido agora. É o próprio item 14(c) do `06`.

---

## Ponto 5. Alternativa A, `01` seção 3

**Prova (Read da linha 81 do `01`):**
> ... A alternativa A, como está escrita aqui, é descoberta, e a dispensa do COES IV só fala de coberto. Pergunta para Kelsen: a dispensa do COES Art. 31 IV, que fala de estacionamento coberto, se aplica à alternativa A, que está escrita como descoberta, ou só a uma versão coberta dela? Não decidido aqui.

**Status C-8 (texto obrigatório, em itálico), na mesma linha:** "Vaga descoberta no afastamento frontal mínimo é vedada na ZE-5 pelo Dec. 3.046 XXII (p. 4), salvo exceção específica da subzona não verificada; a LC 270 Art. 363 §2º XII é divergente e está em Gate." Igual ao que estava antes (comparado com o backup, onde a linha tinha a mesma redação). Não foi alterado.

**Verificação do resto:** Grep de "Ppergunta para Kelsen: a dispensa" e "Não decidido aqui." no `01`. O texto de decisão não aparece em nenhuma outra seção. A seção 4 (linha "Vaga coberta no afastamento frontal") e o `06` (checklist d) não afirmam decisão.

**Veredito:** aprovado. A pergunta está como pergunta, sem decidir.

---

## Pendências abertas (não resolvidas nesta auditoria)

1. Ponto 1: comprovar a varredura de `Fontes_Legislacao` nesta execução, ou manter "não verificado". Sem isso, R1 não fecha.
2. Ponto 3: confirmar com a Etapa 03 v8 (C-12) e fundamentar a localização de piscina, deck e jardim na locação B. Sem fonte, a frase "só a locação B fecha" fica como premissa não verificada.
3. `06` cabeçalho da seção 1 ("nenhum arquivo aberto") contradiz o item 14(c). Corrigir.
4. `06` itens 11 a 13: as cópias legais são da rodada de 13/10, não desta. Corrigir a declaração.
5. `04` P-04, coluna Fonte: "Anexo E-4" → "Etapa 03, Anexo E, item 4".
6. Gate da Coordenação: pendente de Claudemberg (inalterado).

---

Lúcio, 13/10/2026 (auditoria 004c)
