# Nota de auditoria — Lúcio — Etapa 03, v5 (07/10/2026)

**Motivo da v5:** a v4 foi reprovada (parecer_bardi_v4) por 3 erros de forma:
1. a nota v4 declarou "E… igual à v3" sem ter conferido;
2. o Anexo G remetia o crédito à Peça 2 §5.1, que não fala de crédito;
3. a Peça 1 §9 trazia a declaração de leitura da v2, e a nota v4 tinha uma frase que o próprio rodapé desmentia.

**Executor:** Oscar, em duas chamadas. A 2ª fechou 3 células da G por decisão minha.
**Auditoria:** Lúcio.
**A v4 ficou intocada.** Nenhum número, condição ou conclusão mudou.

## Correção do que a nota v4 omitiu (v3 → v4)
Na v4, as linhas E-6 e E-7 do Anexo mudaram de "Peça 2 §4.1 / §4.2" para "Peça 2 §5.1 / §5.2". A mudança estava certa, mas não foi declarada. A nota v4 dizia "D, E, G, H iguais à v3", e isso era falso para a E. A G também herdou da v3, sem conferência, a remissão errada do crédito.

## Diff real v4 → v5, arquivo por arquivo
**Método:** li a v4 e a v5 de cada peça lado a lado. No Anexo, li inteiras as tabelas F, G e I, e conferi pela posição das linhas que as seções C-1 a E não mudaram (o arquivo tem 1 linha a mais, a regra nova da G).

**Peça 1 (`01_..._v5.md`)**
- Título, linha 4 e assinatura: troca de v4 para v5 e de 06/10 para 07/10/2026.
- Linha 5: `anexo_contas_003_v4.md` passa a `anexo_contas_003_v5.md`.
- §9: a frase "Li só o `parecer_bardi_v2.md`, o enunciado e a v2…" foi substituída pela leitura desta versão: parecer_bardi_v4, enunciado e entrega v4 (Peças 1–3 e anexo v4), mais o estado do Oscar. Também foi acrescentada a frase "Na v5: só correção de remissões e de rótulos".
- O resto do texto não mudou.

**Peça 2 (`02_..._v5.md`)**
- Título, linha 4 (data, versão e `anexo_contas_003_v5.md`) e assinatura.
- O corpo (§0 a §9) é idêntico ao da v4.

**Peça 3, Matriz (`03_..._v5.md`)**
- Título, linha 4 e assinatura.
- Coluna "Detalhe": 5 remissões foram corrigidas, porque o fato do impacto não estava na seção citada.

| Linha | v4 | v5 |
|---|---|---|
| 6 | P2 §7 | P2 §3.4, §7 |
| 7 | P2 §7 | P2 §3.4, §7 |
| 8 | P1 §6 | P1 §6; P2 §7 |
| 12 | P2 §2 | P2 §2; Anexo E-14 |
| 16 | P2 §7 | P2 §5.2, §6, §7; Anexo I-3 |

- Foi acrescentada uma linha que declara essas correções.

**Anexo (`anexo_contas_..._v5.md`)**
- Título, Data e título da F: troca de v4 para v5.
- Origem: foi acrescentada a frase da v5.
- Foi acrescentada uma linha de regra abaixo do título da G: "a célula só cita a seção que afirma a frase inteira, com a mesma condição; afirmação parcial = —".
- **Tabela G, 7 células corrigidas (linhas 1, 3, 4, 5, 6 e 7 da G):**

| Linha da G | Coluna | v4 | v5 |
|---|---|---|---|
| 228,72 cabe | Peça 1 | §1 | — |
| Varandas | Peça 3 | linha 20 | — |
| Edícula | Peça 1 | §4 | — |
| Piscina | Peça 1 | §4 | — |
| Árvores | Peça 1 | §5 | — |
| Crédito | Peça 2 | §5.1 | — |
| Crédito | Peça 3 | Anexo C-16, E-16 | — (o fato vive só no Anexo: C-16, E-16) |

- Nota da I-2: foi acrescentada a frase "as 14 remissões foram conferidas contra a Matriz v5, sem mudança".
- C-1 a C-17, D, E, F, H e I-1 a I-3 não mudaram.

## Remissões conferidas (§5-bis v1.5)
- **G:** 27 células conferidas por Oscar. Conferi de novo as 9 linhas contra o corpo v5.
- **Conferidas por Oscar, sem erro:** D (15 linhas), E (17), F (19), I-2 (14, cuja soma bate com a frase da Peça 2 §9: "linhas 1–3, 5–10, 12, 14, 20–22") e as remissões internas do corpo das Peças 1 e 2.
- **E-6/E-7:** a §5.1 da Peça 2 v5 trata da edícula e a §5.2, da piscina. Confirmado por mim.
- **Matriz:** 24 linhas conferidas por Oscar, 5 corrigidas. Conferi as 5 contra a Peça 2 v5.
- **Não conferidas nesta versão:** as remissões externas (seções de Skills, parecer do Hely, Kelsen R-n, Mascaró, Villaça, artigos de lei, itens do dossiê). Nenhuma delas mudou desde a v4.

## Processo
- **Skill de levantamento v1.4 → v1.5:** o §5-bis ganhou um item novo. A cada versão, as tabelas de remissão (E, F, G…) são conferidas contra o corpo atual, e toda alteração é declarada na nota. O item também cobre a regra da célula da G, a declaração de leitura e o ajuste feito só pelo autor.
- **Backup:** `01_CEO/Decisoes_Autonomas/_backups/2026-10-07/`. O registro está no livro-razão de Outubro.
- **Lacuna do Agente:** remissão herdada sem conferência. Está registrada no `_estado_oscar`.
- **Lacuna de auditoria (minha):** declarei uma tabela como igual sem comparar. Está registrada no `_estado_lucio`.
- **Ajustes desta v5:** todos foram feitos pelo Oscar (autor). Eu não editei as peças.

**Contagem:** a preencher por Wallenberg com ferramenta.
