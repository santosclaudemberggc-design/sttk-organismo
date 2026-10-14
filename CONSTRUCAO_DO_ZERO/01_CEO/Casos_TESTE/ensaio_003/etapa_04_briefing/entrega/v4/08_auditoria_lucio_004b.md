# 08b. Auditoria reduzida de Lúcio, Etapa 04 (Briefing), v4, após correção pontual
## Ensaio Sombra 003, família Montenegro Prates (caso 100% FICTÍCIO)

**Auditor:** Lúcio (Gestor Arquitetura) | **Executor da correção:** Oscar | **Data:** 13/10/2026
**Escopo:** somente os trechos alterados pela correção de D1, D2, D3, R1 e P-SMD, conforme a auditoria 08 (`08_auditoria_lucio_004.md`). Não reauditei o restante da v4.
**Limite:** esta auditoria não é Gate da Coordenação. Gate (Claudemberg): pendente. Nada aqui é parecer final para cliente.

---

## 0. Veredito reduzido

| Item | Veredito | Prova |
|---|---|---|
| D1 (número 10.000 retirado) | **APROVADO** | §2.1 |
| D2 (COES 31 IV e LC 270 350 II como conflito) | **APROVADO** nos trechos; uma ressalva de conteúdo para Kelsen | §2.2 |
| D3 (base única 159,44) | **APROVADO** nos trechos; pendência de conferência em P-04 | §2.3 |
| P-SMD (sem escolha de valor) | **APROVADO** | §2.4 |
| R1 (declaração do Glob) | **NÃO APROVADO como está**: a declaração admite repetição do Glob amplo nesta execução | §2.5 |
| Backups | **Ressalva de processo**: não são cópia byte a byte | §3 |

Os trechos alterados atendem ao pedido de correção. Não aprovo a v4 como entregável, porque R1 está reprovada e o Gate segue pendente.

---

## 1. Método desta auditoria

Lúcio não tem shell. A verificação foi feita por Grep com `-n` nos arquivos `0[1-6]_*.md` da pasta `entrega/v4/` e por Read das linhas omitidas pelo tamanho. Quando a linha foi omitida, eu a li integralmente antes de dar veredito.

---

## 2. Prova por item

### 2.1 D1 — número sem fonte retirado

- Grep por `10\.000` nos arquivos 01 a 06: **nenhum resultado** (zero ocorrências do número).
- `01_briefing_corpo_003_v4.md`, linha 115 (§5.4): "...dispensa de faixa, LC 270 Art. 215 §2º, não lido nesta execução [nv]; limite a confirmar por Kelsen." Sem valor. Não atribuído à Etapa 03.
- `04_matriz_decisoes_cliente_003_v4.md`, linha 22 (M-10): "A dispensa de faixa, LC 270 Art. 215 §2º, não lido nesta execução [nv]; limite a confirmar por Kelsen, depende de medição." Sem valor.
- **Resultado:** aprovado.

### 2.2 D2 — COES Art. 31 IV e LC 270 Art. 350 II como conflito

- `01_briefing_corpo_003_v4.md`, linha 81 (§3, alternativa A), lida integralmente: "Dispensa do COES Art. 31 IV (p. 17 [lido]) não tratada no status acima... **CONFLITO para Kelsen** (§6, P-varanda)... Não decidido aqui."
- `01_briefing_corpo_003_v4.md`, linhas 95 e 96 (§4): tabela com as duas linhas novas, ambas marcadas "**CONFLITO para Kelsen**... Não decidido".
- `01_briefing_corpo_003_v4.md`, linha 131 (§6, P-varanda), lida integralmente: pergunta (i) sobre COES 31 IV e (ii) sobre LC 270 350 II, marcada "não decidido aqui".
- `04_matriz_decisoes_cliente_003_v4.md`, linha 76 (T-04): "Incluir (ver 01 §3 e §6, P-varanda)... Conflito para Kelsen, não decidido".
- `06_declaracao_leitura_e_bloqueios_003_v4.md`, linhas 125 e 128 (§3(e)): COES Art. 31 IV com texto verbatim ("...em telha vã, com um pavimento de altura") e LC 270 Art. 350 I e II com texto verbatim ("as varandas e terraços assentes no terreno, para as edificações uni, bifamiliares e multifamiliares").
- Nenhum trecho decide a alternativa A nem as varandas.

**Ressalvas de conteúdo (não bloqueiam o item, vão a Kelsen ou ao Oscar):**
- a) A alternativa A no texto da v4 é "vaga **descoberta**" (01 linha 81). A dispensa do COES IV fala de estacionamento **coberto**. Está registrado como pergunta a Kelsen na linha 81, mas a pergunta precisa aparecer também na linha de P-varanda da matriz, que hoje só cita o T-04.
- b) A auditoria 08 pedia "04 linha P-varanda". A matriz 04 não tem linha com esse nome; o conflito está no T-04. Não é defeito de conteúdo, é diferença de referência.
- c) Não receberam a pergunta D2 (fora do pedido, mas relacionados): 02 linha 23 (A9, Garagem: já cita Art. 31 III) e 05 E-17. Não bloqueiam.

- **Resultado:** aprovado nos trechos, com as ressalvas a e c.

### 2.3 D3 — base única de folga permeável (159,44)

- `02_planilha_ambientes_003_v4.md`, linha 41 (§2, Permeável): "Folga em H0 de **159,44 m²** (base única, 05 E-10: 302,39 − 142,95). Diferença de 0,20 m² em relação ao 159,24 da Etapa 03 C-12 (aproximação retangular de 571,60)". Uma base, uma diferença declarada.
- `04_matriz_decisoes_cliente_003_v4.md`, linha 35 (P-04): "Impermeáveis consomem a folga de 159,44 m² em H0. Com a piscina nos fundos, só a locação B fecha (+2,05)."
- `05_anexo_contas_briefing_003_v4.md`, linha 64 (E-10): "Folga H0: 302,39 − 142,95 = **159,44 m²**". Não alterada, já estava com a base escolhida.
- `05_anexo_contas_briefing_003_v4.md`, linha 65: a conferência com 159,24 da Etapa 03 aparece como registro. Coerente com a diferença declarada no 02.

**Pendência de conferência (não é do D3 em si):**
- O "+2,05" de P-04 não foi reconferido com a nova base 159,44. Não sei se foi calculado com 159,24 ou 159,44. Oscar não reconferiu. Vai como pendência para Oscar, não decido aqui.

- **Resultado:** aprovado nos trechos alterados, com pendência do +2,05.

### 2.4 P-SMD — sem escolha de valor

- `01_briefing_corpo_003_v4.md`, linha 17 (§0 item 4): "Os dois 57,18 vêm de contas diferentes e não se confirmam entre si. Não escolho e não copio 57,18 como resultado."
- `01_briefing_corpo_003_v4.md`, linha 126 (§6, P-SMD): "A TO é da zona, não do cálculo: Kelsen decide qual TO vale pelo Anexo XXI".
- `02_planilha_ambientes_003_v4.md`, linha 44: "57,18 m² (enunciado) ou 68,62 m² (Art. 352, TO 40%)... Divergência aberta (P-SMD)".
- `05_anexo_contas_briefing_003_v4.md`, linhas 47, 53, 210: divergência, observação e pendência, sem escolha.
- **Conferência de conta:** 0,20 × 343,08 = 68,62 (TO 40%, área livre 571,80 − 228,72 = 343,08). 0,20 × 285,90 = 57,18 (TO 50%, área livre 571,80 − 285,90). Ambas conferem.
- **Resultado:** aprovado.

### 2.5 R1 — declaração do Glob amplo

- `06_declaracao_leitura_e_bloqueios_003_v4.md`, linha 39 (§1, item 14), lida integralmente: o item registra que o Glob "rodado nesta execução (ajuste de 13/10/2026)" retornou 40 caminhos, todos da pasta de Fontes_Legislacao do Hely, e que nenhum pertence à pasta do ensaio nem ao examinador. Registra também que dois arquivos foram abertos, por página, para conferir D2 (COES p. 17 e LC 270 p. 125).
- **Problema de método:** o próprio item confirma que o Oscar repetiu o **Glob amplo** em `CONSTRUCAO_DO_ZERO` por `**/Fontes_Legislacao/*.pdf` nesta execução. A R1 apontava exatamente esse método, como ressalva. A repetição não entra como correção; é uma nova ocorrência do mesmo desvio.
- A declaração de que a listagem não traz nome do ensaio ou do examinador é verdadeira para os 40 nomes listados. Não verifico o que o Glob não listou (a ferramenta não informa limite).
- A correção pedida ("declarar por escrito que nenhum nome retornado pelo Glob amplo é da pasta do ensaio ou do examinador") foi feita, mas a declaração se apoia em um Glob amplo repetido. Por isso não aprovo R1 como está.
- **Ação pedida:** Oscar reescreve o item 14 deixando claro que o Glob amplo foi repetido nesta execução, que isso é desvio do método da R1, e que a declaração vale só para a listagem de 13/10. Não rodar Glob amplo de novo.
- **Resultado:** **não aprovado**.

---

## 3. Backups (ressalva de processo)

- Backups criados pelo Oscar em `_backups/2026-10-13/`: `lucio_ANTES_v4-ajuste_01_briefing_corpo_003_v4.md`, `..._02_planilha_ambientes_003_v4.md`, `..._04_matriz_decisoes_cliente_003_v4.md`, `..._06_declaracao_leitura_e_bloqueios_003_v4.md`.
- Backup de `oscar.md` criado por Lúcio: `lucio_ANTES_v4-ajuste_oscar.md`.
- **Ressalva:** nenhum backup foi feito por cópia byte a byte. Lúcio e Oscar não têm shell. Os backups foram reescritos com Write a partir da leitura integral, com prova só de conteúdo, sem hash. Não sei se havia BOM ou CRLF. Para prova de bytes, alguém com PowerShell deve comparar o hash com a versão original, se ela existir em outro lugar.
- **Livro-razão `Outubro.md`:** não copiei integralmente (464 linhas), por falta de shell e custo de reescrita. Reversão: apagar o bloco acrescentado ao final. Registrado no próprio livro-razão.

---

## 4. Pendências para Kelsen (via Lúcio)

- **P-SMD:** qual TO vale pela LC 270 Anexo XXI (57,18 com TO 50% ou 68,62 com TO 40%).
- **P-varanda:** COES Art. 31 IV aplicado à alternativa A (vaga coberta ou descoberta) e harmonização com Dec. 3.046 XXII; LC 270 Art. 350 II nas varandas térreas.
- **Dispensa de faixa (LC 270 Art. 215 §2º):** limite a confirmar, [nv].

## 5. Pendências de Oscar (fora deste pedido, não corrigidas por Lúcio)

- 02 linha 26 (A12): cita "04 M-14", que não existe (a matriz vai até M-12). Referência quebrada.
- 04 linha 35 (P-04): "+2,05" não reconferido com 159,44.
- 06 §1 item 14: reescrever sem a repetição do Glob amplo como declaração limpa (ver 2.5).
- 02 linha 23 (A9) e 05 E-17: sem a pergunta D2 (ressalva 2.2 c).

---

Lúcio, 13/10/2026 (auditoria reduzida da v4 corrigida)
