# Auditoria do Lúcio sobre a Etapa 04 (Briefing), v3
## Ensaio Sombra 003, Família Montenegro Prates (100% FICTÍCIO)

**Auditor:** Lúcio (Gestor Arquitetura) | **Executor:** Oscar | **Data:** 13/10/2026
**Regra aplicada:** "auditoria só vale com prova". Cada verificação traz o trecho lido ou a conta refeita. O que não foi verificado está marcado como tal.
**Status:** análise preliminar. Nada protocolado. Sujeito ao Gate da Coordenação (Claudemberg).

---

## 1. Veredito de auditoria

**Aprovado com ressalvas (não é reprovação).** O pacote está completo nas 7 peças pedidas, as contas fecham, os pedidos do cliente estão todos tratados e nenhum "cabe" sem condição foi encontrado. Três ressalvas precisam ir ao Oscar antes de a v3 virar insumo do Estudo Preliminar. Uma delas é de forma (4.1 do anexo 02). Uma é processual e minha (abaixo, §5).

---

## 2. Verificação de acesso (regra de entradas)

| Verificação | Prova | Resultado |
|---|---|---|
| Oscar abriu só as entradas permitidas | `entrega/v3/06_declaracao...`, §a: lista de 1 enunciado + 5 arquivos v8 da Etapa 03 + 10 Skills | OK |
| Nenhum gabarito, parecer_bardi, correcoes_caso_v2 nem entrega anterior da Etapa 04 aberta | `06`, §a, "Não abri nesta execução" (5 itens) | Declaração do Oscar, sem prova independente (não tenho log de leitura). Aceito com ressalva |
| Contagem de entradas do relatório | Relatório do Oscar diz "seis arquivos da Etapa 03 v8". A lista em `06` tem 5 da Etapa 03 mais o enunciado, que é a 6ª entrada | Erro de redação no relatório, sem efeito sobre o acesso |
| Meu próprio prompt citou proibidos | Meu prompt de acionamento citou a pasta `_gabaritos_LACRADO_bardi`, `parecer_bardi` e `correcoes_caso_v2` na lista de "PROIBIDO" | **Falha minha.** A regra era não citar. Não houve leitura, mas a menção existiu. Registrado em §5 |

---

## 3. Conferência de contas (refeitas por mim)

| Conta | Fórmula | Refeita | Valor no Briefing | Fonte no Briefing | Confere |
|---|---|---|---|---|---|
| E-2 TO 40% | 0,40 × 571,80 | 228,72 | 228,72 (anexo 05, E-2) | 05 E-2 | Sim |
| E-3 teto | 2 × 228,72 | 457,44 | 457,44 | 05 E-3 | Sim |
| E-4 permeável | 0,25 × 571,80 | 142,95 | 142,95 | 05 E-4 | Sim |
| E-5 envelope H0 | (14,29−2,50−2,50) × (40,00−6,00−5,00) = 9,29 × 29,00 | 269,41 | 269,41 | 05 E-5 | Sim |
| E-6 folga H0 | 269,41 − 228,72 | 40,69 | 40,69 | 05 E-6 | Sim |
| E-7 déficit H0 | 520 − 457,44 | 62,56 | 62,56 (não cabe) | 05 E-7 | Sim |
| E-11 envelope H1 | 9,29 × (40,00−18,00−6,00 = 16,00) | 148,64 | 148,64 | 05 E-11 | Sim |
| E-12 teto H1 | 2 × 148,64 | 297,28 | 297,28 | 05 E-12 | Sim |
| E-13 déficit H1 | 520 − 297,28 | 222,72 | 222,72 | 05 E-13 | Sim |
| E-16 faixas fora do envelope | 85,74 + 72,50 + 72,50 + 71,45 | 302,19 | 302,19 | 05 E-16 | Sim |
| E-16 folga H0 | 302,19 − 142,95 | 159,24 | 159,24 | 05 E-16 | Sim |
| E-18 folga H1 sem APP | 14,29×6,00 + 2×2,50×16,00 = 85,74 + 80,00 = 165,74; − 142,95 | 22,79 | 22,79 | 05 E-18 | Sim |
| E-18 acesso que esgota | 22,79 / 6,00 | 3,80 | 3,80 (corpo §4 não cita; anexo 05 E-18 cita) | 05 E-18 | Sim |
| E-19 edícula, condomínio | 2,50 − 0,80 | 1,70 | 1,70 | 05 E-19; corpo §5 C1 | Sim |
| E-19 edícula, COES | 1,50 − 0,80 | 0,70 | 0,70 | 05 E-19 | Sim |
| E-20 piscina | 1,60 − 0,90 | 0,70 | 0,70 | 05 E-20 | Sim |
| E-21 altura | 3,20 + 8,50 | 11,70 | 11,70 | 05 E-21 | Sim |
| E-22 crédito | 3,00 + 1,20 | 4,20 | 4,20 | 05 E-22 | Sim |
| E-28 janela Mais-Valerá | 31/12/2026 − 01/12/2026 = 30 dias | 30 dias após a janela | "30 dias depois da janela" | 05 E-28 | Sim |
| Rampa, 10% | 0,50 / 0,10 | 5,00 m | não citado no Briefing | — | Não usado |

**Resultado:** todas as contas numéricas do Briefing fecham com a refação. Nenhum número foi aceito sem refazer.

**Verificação de origem (dados do enunciado):** a conta de 520 m² usa 457,44 do teto, que vem da v8 (`anexo_contas_003_v8.md`, C-2/C-3 e Peça 2 §0). Ok.

---

## 4. Verificação de citações contra as Skills (prova de leitura)

Oscar declarou que os textos primários de COES, Dec. 3.046, LC 270 e NBR não foram abertos. Conferi o que consegui sem abrir primário, e só nas Skills.

| Citação no Briefing | Onde conferi | Prova (trecho) | Resultado |
|---|---|---|---|
| Vaga com pé-direito livre 2,20 m (Art. 28 II) | `.claude\skills\vaga-estacionamento-...\SKILL.md`, linha 63 | "Pé-direito da garagem e da rampa: 2,20 m livres (Art. 28 II)" | Confere com a Skill v1.6 |
| Mais-Valerá: 30% à vista até 01/12/2026 (Art. 40, redação LC 301 Art. 58) | `.claude\skills\legal-oodc-mais-valera-mais-valia\SKILL.md`, linha 12 e 57 | "vai até 01/12/2026, com 30% de desconto só à vista" | Confere |
| Mais-Valerá: 60x com 30% não alcança AP4 (Art. 19 II) | Mesma Skill, linha 30 | "Art. 19, II: 60x com 30%, só AP3, AP5, RA XVI... (não alcança AP4)" | Confere |
| Vaga 2,50 × 5,00 e manobra 2,50 × 5,00 (Art. 29 I e II) | Anexo 02 §3 e Skill v1.6 §3 | Citado pela Skill; COES p. 15 não aberto | Confere com a Skill. Primário não lido (ressalva) |
| Art. 29 III como limiar de dispensa, não tamanho de garagem | Anexo 02 §3, linha "Limiar" | Texto do v8 (C-4) | Confere com v8 |
| Art. 19, II e Art. 40 da Skill versus o Briefing (C4) | Mesma Skill | — | Confere |
| LC 270 Art. 215 §2º (espelho d'água medido) | Não conferi. Citação de origem: Skill decreto3046 M1 (conforme `04`, M13) | Não localizado nesta verificação | **Não verificado** |
| COES Art. 12, Art. 18, Art. 31 V, Art. 8º §4º | Não conferi texto do COES. Oscar marcou como lido por Skill (`06` §a) | — | **Não verificado no primário** (ressalva declarada por Oscar) |
| NBR 9050 maçaneta 0,90 a 1,10 m e giro 1,50 m | Só Skill secundária (`06` §b, item 2) | — | Declarado como fonte secundária. Aceito com ressalva |

**Resultado:** as citações que consegui conferir nas Skills batem. As que dependem de primário ficam com a ressalva que o próprio Oscar pôs.

---

## 5. Verificação de conteúdo: pedidos, premissas e forma

### 5.1 Pedidos do enunciado (checklist ENTREGÁVEL MÍNIMO)

| Item | Verificação | Resultado |
|---|---|---|
| Corpo ≤ 2.500 palavras | **Não contado.** Não tenho ferramenta de contagem (Bash ausente nesta execução). Ficou para Wallenberg, como manda o enunciado | **Pendente de Wallenberg** |
| PN-ARQ 5.2.1 a) organograma com fluxos | `03` §1.2: fluxos F1 a F10 e esquema de relação (§1.3) | Atende |
| PN-ARQ 5.2.1 b) esquemas por ambiente | `03` §2: 16 linhas (A-01 a A-16) com área, dimensões, mobiliário, exigências, dono | Atende |
| PN-ARQ 5.2.2 planilha | `02` §1: colunas ID, quantidade, dimensões, área (regime), usuários, atividades, exigências, dono | Atende |
| Programa 520 separado em computável e não computável, com artigo | `02` §4.1 e §4.2 | **Ressalva R1** (ver 5.3) |
| Garagem: vaga e manobra separadas, com artigo | `02` §3: vaga Art. 29 I, manobra Art. 29 II, acesso Art. 29 IV, limiar Art. 29 III | Atende |
| Cenários H0 e H1, o que cabe e o que não cabe | `01` §4 (tabela) | Atende |
| Cada "cabe" com condição escrita | `01` §4: "Cabe, condicionado a 'a', T2 e T4" etc. Garagem em H0: "a ≤ 40,69" | Atende |
| Matriz pedido × resposta × fonte × dono, uma linha por pedido | `04` §1 (11 linhas Etapa 03), §2 (M1–M15), §3 (E-1 a E-17) | Atende |
| Tabela pergunta × onde respondida | `07` §1 a §4 | Atende |
| Declaração de leitura com caminho | `06` §a | Atende (com a ressalva de contagem em §2 acima) |
| Nenhuma premissa legal reinterpretada | `01` §3 (premissas com fonte), pendências P3, P5, P6, C4 enviadas a Kelsen | Atende, com ressalva R2 |

### 5.2 Teste de matriz: perguntas da Etapa 03 com dono "Cliente" ou "Cliente + outro"

Conferi contra a Matriz v8 (`etapa_03_levantamento\entrega\v8\03_matriz_decisoes_pendentes_003_v8.md`, coluna "Dono"). Linhas com "Cliente" no dono:

| Linha v8 | Dono na v8 (trecho) | No `04` §1 |
|---|---|---|
| 1 | "Cliente + advogado (o Legal recomenda)" | Sim |
| 2 | "Cliente; Kelsen + Comissão de Obras, se insistir" | Sim |
| 3 | "Cliente + Baumgart/Cardozo; ..." | Sim |
| 4 | "Cliente; SMAC; condomínio (Art. 12); Glaziou (laudo)" | Sim |
| 5 | "SMAC via Kelsen; cliente (programa); Villaça (S3)" | Sim |
| 9 | "Cliente; Kelsen; condomínio; Hely" | Sim |
| 11 | "Cliente (contrata); Oscar/Lúcio; topógrafo" | Sim |
| 12 | "Kelsen (TRAVA POP-LEGAL-03); cliente; advogado" | Sim |
| 13 | "Cliente; topógrafo (T2, T4); EP" | Sim |
| 23 | "Oscar; topógrafo; profissional habilitado; cliente" | Sim |
| 24 | "Cliente (Briefing); condomínio + Kelsen" | Sim |

**Resultado:** 11 de 11 linhas batem com a Matriz v8. Nenhuma linha com "Cliente" ficou de fora. Nenhuma linha sem "Cliente" entrou.

### 5.3 Ressalvas que vão ao Oscar

**R1 (forma, média). O déficit de 62,56 m² está classificado como "não computável".** Prova: `02` §4.1, linha "Não computável (necessário para 520) | 62,56 | Área construída fora do teto | Anexo E-7 | 520 − 457,44". O enunciado exige, para cada item não computável, a regra que o exclui (artigo). O 62,56 não é um item. É a diferença entre o programa e o teto. Oscar reconheceu no "Ponto de atenção" (mesma seção), mas a tabela continua com a linha. **Pedido:** renomear a linha para "Déficit em relação ao teto (não é item não computável)", e manter a lista de itens reais só em §4.2.

**R2 (conteúdo, média). Varanda e Mais-Valerá ficaram sem a condição de M-a.** Prova: a v8 (`anexo_contas_003_v8.md`, C-7, "Nota de verificação para Lúcio") diz que as expressões de V necessário (62,56 − a) e de capacidade (81,38 − a) podem não depender de "a" sob M-a. O Briefing `01` §1 item 2 e `02` §4.2 repetem "V ≥ 62,56 − a" sem a nota. A nota não é conclusão, mas tem que aparecer como dúvida aberta. **Pedido:** registrar a dúvida no `01` §3, como pendência para Kelsen.

**R3 (redação, baixa). Versão de Skill.** Oscar cita `vaga...v1.6` no Briefing (`01` F10; `02` §3) e `v1.3` no anexo v8. A Skill está em v1.6 (verificado, linha 4). Não há erro de conteúdo, só divergência de referência entre a v8 e a v3. **Pedido:** manter v1.6 e citar a data.

### 5.4 Pontos corretos que quero registrar

- Os quatro pedidos de mensagens do cliente estão todos com resposta, fonte, dono e o que ficou aberto (`04` §2, M1 a M15).
- Assembleia, Mais-Valerá "como previsto" e "lago não atrapalha" não viraram premissa. Isso segue a regra da casa (pressão comercial não pula etapa).
- Oscar não redimensionou o programa nem desenhou. Revit: uma chamada, erro literal registrado ("Plugin não está conectado").

---

## 6. Falha de processo (minha)

Meu prompt de acionamento listou como "PROIBIDO" a pasta `_gabaritos_LACRADO_bardi`, o `parecer_bardi` e o `correcoes_caso_v2`, citando os nomes. A regra da execução era não citar. Não há prova de leitura (declaração 06 diz que não foram abertos), mas a menção existiu e fica registrada como falha minha. Nos próximos acionamentos de ensaio, a proibição tem que ser dada só como "nenhum arquivo fora da lista", sem nomes.

---

## 7. Conclusão

- Contas: 19 de 19 fecham com a refação. Nenhum número aceito sem conta.
- Matriz: 11 de 11 linhas da Etapa 03 com dono "Cliente" batem com a v8.
- Citações: as conferidas nas Skills batem. As de primário ficam com a ressalva declarada.
- Ressalvas: R1 e R2 são de conteúdo e forma e vão ao Oscar. R3 é redação.
- Pendente de Wallenberg: contagem de palavras do corpo (sem ferramenta, não estimo).
- Falha minha: menção dos nomes proibidos no prompt (§6).
- Bloqueio registrado: Revit, "Plugin não está conectado".

— Lúcio, 13/10/2026 (auditoria da v3)
