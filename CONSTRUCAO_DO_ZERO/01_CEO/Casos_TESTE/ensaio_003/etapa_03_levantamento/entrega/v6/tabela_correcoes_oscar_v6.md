# Tabela de correções — Oscar — Etapa 03 (Levantamento), v6 — Ensaio Sombra 003

**Executor:** Oscar | **Para:** Lúcio (auditoria) | **Data:** 08/10/2026 | Análise preliminar.
**Base:** `parecer_bardi_v5.md` (07/10/2026) e a entrega v5 (só leitura). A v6 está em `entrega/v6/`. Nota 00 da v6: não escrita (é de Lúcio).

## 0. Divergências entre a ordem e o que encontrei (para Lúcio decidir)

1. **XXII do Dec. 3.046:** a ordem diz que a Skill `decreto3046-81-lc270-2024-licin-barra-recreio` não traz o XXII. Conferi por Grep: a Skill está na **v1.5, de 08/10/2026** (Kelsen), com changelog, checklist (§5, linha 143) e R12 (linha 232), citando "Disp. Gerais XXII e XXIII a (p. 4 do PDF, lidos por Kelsen)". Citei o XXII como vem da Skill v1.5, e não por "R3 da Skill de vaga" como alternativa.
2. **Nome do cliente:** a ordem diz "Barros". O enunciado (`enunciado.md`) e as cinco peças da v5 dizem "Família Montenegro Prates". Mantive Montenegro Prates nos cabeçalhos das quatro peças e do anexo. Se o ensaio trocou o nome, a troca são os cinco cabeçalhos.
3. **Número de itens:** a ordem fala em "4 itens" de "O que corrigir (v6)". O parecer tem 5 (o 5º é do Bardi). Tratei os 5 na Seção 1.
4. **Estado de Oscar:** a entrada de 07/10 do meu arquivo de estado registrava "v5 aprovada por Lúcio". O parecer de 07/10 recomenda REPROVAR, e a ordem de 08/10 manda refazer como v6. Atualizei o estado para registrar a reprovação pendente. O status vigente é decisão de Lúcio.
5. **Frontal:** o RIU (dossiê 5.3) diz 5,00 m e o Regramento (5.4) diz 6,00 m. Usei 6,00 m, o mais restritivo, e a conclusão vale para os dois.

## 1. Itens do parecer (O que corrigir, v6; e Erros que reprovam)

| Item do parecer | Ação feita | Arquivo e linha da v6 | Status |
|---|---|---|---|
| **O que corrigir 1** (Oscar): refazer a garagem com a Skill de vaga (vaga e manobra separadas, com artigo); rever a alternativa A contra o XXII e a geometria; propagar para Matriz, P2 e Anexo G/E | a = **25,00** m² por vaga (Skill de vaga §3; COES Art. 29 III; composição 12,50 + 12,50, R6). Contas refeitas: C-4 a C-9, C-13, C-14, C-15, C-17. Alternativa A marcada **vedada** (tensão XII × XXII e conta geométrica, 10,00 m contra 6,00 m). Alternativa B marcada **inviável** com a = 25,00. Propagado para Matriz, P2 e anexo (E e G) | Anexo C-4 (linha 43), C-5 (56–62), C-6 (66–74), C-7 (78), C-8 (94), C-9 (115), C-13 (156), C-14 (170), C-15 (182), C-17 (193); P2 §1 (linhas 12, 17–18), §2 (33), §3.3 (52–57), §3.4 (62), §4 (69), §5.3 (102), §8 (124); Matriz linhas 4 (arquivo, linha 19), 9 (24), 13 (28), 21 (36), 22 (37), bloco de condições (10); Anexo E-5 (235), E-8 (238), E-12 (242) | **Atendido com pendência.** Pendências: R1 da Skill de vaga (dimensão obrigatória, Gate); manobra compartilhada (Art. 29 IV) pode baixar a média (Hely via Kelsen); incidência do XXII na subzona A-ENS (Kelsen); número de vagas fica para o Briefing |
| **O que corrigir 2** (Oscar/Lúcio): aplicar a regra da G às 27 células | 27 células conferidas uma a uma contra a seção citada. Resultado: 5 citações trocadas, 2 notações, 20 mantidas (9 delas, da edícula, piscina e árvores, com afirmação estreitada ou impacto reescrito). Detalhe na Seção 2 | Anexo G (linhas 279–287); Matriz linha 4 (arquivo, linha 19) | **Atendido.** Auditoria final de Lúcio |
| **O que corrigir 3** (Kelsen): errata ao parecer da Etapa 01 (l. 181); inclusão do XXII na Skill `decreto3046`, com remissão à Skill de vaga R3 | Não edito parecer nem Skill. Verifiquei: o XXII **já está** na Skill decreto v1.5 (08/10/2026, Kelsen), com R12 remetendo à Skill de vaga R3. A errata do parecer da Etapa 01 (l. 181) não aparece no que li | P2 §2 (linha 33), P2 §3.3 (alternativa A); Anexo C-8; Anexo I-1 (última linha); Anexo H | **Atendido com pendência.** XXII incluído (Kelsen, 08/10). Errata da l. 181: **pendente, Kelsen** |
| **O que corrigir 4** (Drenagem): atualizar o espelho `.agents/skills` (levantamento v1.5; vaga v1.0) | Não feito por mim. Não edito Skills, e o espelho é da Drenagem | — | **Não atendido por Oscar**, por estar fora da fronteira de execução. Motivo: não é tarefa minha. Registrado para Lúcio encaminhar à Drenagem |
| **O que corrigir 5** (Bardi): registrar o erro do gabarito da Isca 4 e cobrar a herança corrigida na Etapa 04 | Não é tarefa de Oscar. A v6 não cita "Isca 4" nem o gabarito como fonte (a citação "parecer do Bardi, Isca 4" saiu do C-4) | Anexo C-4 (linha 43, texto novo) | **Não é de Oscar.** Registrado para Lúcio e Bardi |
| **Erro 1** (G viola a regra de citação) | Refeita a G, célula por célula (Seção 2) | Anexo G (linhas 279–287) | **Atendido** |
| **Erro 2** (a = 12,50–15,00 conta só a vaga, sem manobra; origem na garagem da Matriz 9, 22 e 24, C-5, C-7, C-8, C-9, C-15, P2 §1, §3.3, §5.3 e §8) | a = 25,00 por Skill de vaga v1.0 §1, §3, R6 (COES Art. 29 I–III). Removidas da v6 todas as referências à faixa antiga. Verificado por Grep na v6: nenhum "12,50–15,00" nas quatro peças nem no anexo | Peças 1, 2, 3 e anexo, todas as linhas da garagem (ver Seção 5) | **Atendido com pendência**, a mesma de O que corrigir 1 (R1, manobra compartilhada) |
| **Erro 3** (alternativa A contra o Dec. 3.046 XXII; premissa do parecer da Etapa 01, l. 181) | A marcada **vedada** na leitura restritiva (Skill decreto v1.5 R12; Skill vaga R3). Tensão XII × XXII registrada, sem resolvê-la. Geometria: 10,00 m de vaga + manobra contra 6,00 m de frontal; 1 vaga em H1 sem a APP (25,00 > 22,79) não cabe. Sem terceira solução: qualquer uma vira pendência | P2 §2 (linha 33), §3.3 (52–57), §5.3 (102); Anexo C-8 (94); Matriz linha 9 (24) | **Atendido com pendência**: Kelsen (incidência do XXII na subzona A-ENS; Gate da tensão XII × XXII; errata da l. 181) |

## 2. Tabela G: as 27 células (regra da v5 e da Skill de levantamento v1.5 §5-bis)

Regra: a célula só cita a seção que afirma a frase inteira, com a mesma condição; afirmação parcial = "—". Cada célula foi conferida de novo contra o texto da seção citada.

Legenda: **Mudou** = citação trocada; **Notação** = mesma seção, forma diferente; **Mantida** = sem mudança de citação (pode haver ajuste no texto da afirmação, indicado).

| # | Linha (afirmação) | Peça | Citação v5 | Citação v6 | Situação | Motivo (uma frase) |
|---|---|---|---|---|---|---|
| 1 | 228,72 cabe no envelope | P1 | — | — | Mantida | A Peça 1 não afirma que 228,72 cabe; só traz o envelope de 269,41. |
| 2 | 228,72 cabe no envelope | P2 | §3 | §1, item 1 | **Mudou** | A §3 só descreve envelope e folga (§3.1); a frase completa está em §1, item 1. |
| 3 | 228,72 cabe no envelope | P3 | linha 1 | — | **Mudou** | A linha 1 trata da área de cálculo e não menciona 228,72 cabe. |
| 4 | 520 em H0 só com as 3 condições | P1 | — | — | Mantida | A Peça 1 não trata do programa de 520. |
| 5 | 520 em H0 só com as 3 condições | P2 | §1 | §1, itens 2 a 4 | Notação | Os itens 2 a 4 juntos formam a afirmação (cabe com 3 condições; M-b não; H1 não). |
| 6 | 520 em H0 só com as 3 condições | P3 | linhas 5, 9, 21, 24 | linha 24 | **Mudou** | Só a linha 24 afirma as três partes; a 5 só fala de H1, a 9 não fala de 520 e a 21 só traz M-a, M-c e M-b. |
| 7 | Varandas: sem balanço em y 0–6,00; XIV até 5,60; dentro do envelope | P1 | §1 | — | **Mudou** | A §1 traz envelope e XIV 5,60, mas não o "sem balanço em y 0–6,00". |
| 8 | Varandas (idem) | P2 | §3.2 | §3.2 | Mantida | A §3.2 afirma as três partes. |
| 9 | Varandas (idem) | P3 | — | — | Mantida | A linha 20 trata de VII × XI, não da afirmação. |
| 10 | Edícula: falta 1,70 m pelo condomínio; parecer de demolição total; decide o cliente (afirmação estreitada †) | P1 | — | — | Mantida | A Peça 1 só marca a edícula para demolição (cor do DULI), sem parecer. |
| 11 | Edícula (idem †) | P2 | §5.1 | §5.1 | Mantida (texto †) | A §5.1 diz "faltam 1,70 m pelo condomínio", "Parecer: demolição total" e "Decide o cliente". "Inviável", que estava na afirmação, não aparece no texto. |
| 12 | Edícula (idem †) | P3 | linha 2 | linha 2 | Mantida (texto †) | A linha 2 traz parecer de demolição, 1,70 m pelo condomínio e dono cliente. |
| 13 | Piscina: fundo até 0,70 m abaixo do NA (risco de água); decide o cliente, com o laudo (afirmação estreitada †) | P1 | — | — | Mantida | A Peça 1 não trata de NA nem de profundidade da piscina. |
| 14 | Piscina (idem †) | P2 | §5.2 | §5.2 | Mantida (texto †) | A §5.2 diz "Fundo até 0,70 m abaixo do NA", "Risco de água: sim" e "Decide o cliente, com o laudo". "Fora das premissas" está só em §1, item 6. |
| 15 | Piscina (idem †) | P3 | linha 3 | linha 3 | Mantida (texto †) | A linha 3 traz fundo 0,70 m abaixo do NA e dono cliente + laudo (Baumgart/Cardozo). |
| 16 | Árvores: parecer de preservar; garagem + árvores sim, com condição (afirmação com "garagem" †) | P1 | — | — | Mantida | A Peça 1 §5 só lista o que falta; não afirma preservar nem garagem. |
| 17 | Árvores (idem †) | P2 | §5.3 | §5.3 | Mantida (texto †) | A §5.3 diz "Parecer: preservar" e "Garagem + árvores: sim, com condição". |
| 18 | Árvores (idem †) | P3 | linha 4 | linha 4 | Mantida (impacto reescrito) | O impacto da linha 4 foi reescrito: garagem no envelope, frontal só com acesso e árvores. A versão antiga falava de vagas no frontal, que saíram. |
| 19 | Crédito de 3,0; teto de 4,2 | P1 | — | — | Mantida | Sem seção que afirme a frase inteira. |
| 20 | Crédito (idem) | P2 | — | — | Mantida | Sem seção que afirme a frase inteira. |
| 21 | Crédito (idem) | P3 | — (o fato vive só no Anexo: C-16, E-16) | — | Mantida | O fato está só no Anexo (C-16, E-16), que não é peça. |
| 22 | Curvas a cada 1,00 m | P1 | §3, T1 | §3; §7 (T1) | Notação | As duas seções afirmam a frase: §3 e T1 em §7. |
| 23 | Curvas a cada 1,00 m | P2 | — | — | Mantida | A Peça 2 não trata de curvas. |
| 24 | Curvas a cada 1,00 m | P3 | linha 11 | linha 11 | Mantida | A linha 11 afirma que, sem curvas a cada 1 m, não há forma real do envelope. |
| 25 | Piso térreo: soleira = implantação; +3,20 prevista; depende de T2–T4 e R2 | P1 | §3 | §3 | Mantida | A §3 afirma as quatro partes. |
| 26 | Piso térreo (idem) | P2 | §6 | §6 | Mantida | A §6 afirma as quatro partes. |
| 27 | Piso térreo (idem) | P3 | linha 10 | — | **Mudou** | A linha 10 diz "+3,20 é prevista" e "T2–T4 e R2", mas não "soleira = implantação" (ponto apontado pelo parecer). |

**Resumo da G:** 27 células. 5 citações trocadas (células 2, 3, 6, 7 e 27). 2 notações (células 5 e 22). 20 mantidas. Dentro das 20, as células 10 a 18 (edícula, piscina e árvores) têm a afirmação estreitada no texto da G (marcada †) e, na célula 18, o impacto da Matriz linha 4 foi reescrito. As demais 11 mantidas não mudaram.
Anexo G atualizado nas linhas 279–287 do anexo `anexo_contas_003_v6.md`.

## 3. Proposta à Skill de levantamento v1.6 (não editada; Lúcio aplica)

**A Skill de levantamento v1.5 hoje contradiz a Skill de vaga? NÃO.** Ela não traz valor de "a" nem fala de vaga no frontal, então não há conflito de número. **Mas é omissa, e a omissão está onde o erro nasceu:** a §5-bis manda calcular "térreo = projeção − (n−1)·a" sem dizer de onde sai "a". A faixa de 12,50–15,00 veio do caso, não da Skill. Além disso, a §5-bis cita como fonte do Art. 350 III "o parecer Legal do caso", que é remissão a documento de caso e não a Skill.

**Texto proposto para a §5-bis, primeiro item (substituir a frase de garagem):**

> "Garagem: só 1 vaga coberta fica fora da TO em unifamiliar (LC 270 Art. 350 III). Cada vaga coberta a mais sai do térreo computável: térreo = projeção − (n−1)·a. Valor de a = 25,00 m² por vaga, por COES (LC 198/2019) Art. 29 III, p. 15 do PDF consolidado SMU ("25 m² de área de estacionamento por vaga"), com composição vaga 2,50 × 5,00 m (Art. 29 I) + manobra 2,50 × 5,00 m (Art. 29 II), leitura conservadora conforme a Skill vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj §3 e R6. Não usar 12,50 m² (só a vaga). A manobra compartilhada (Art. 29 IV) não reduz o valor por vaga sem confirmação de Hely/Kelsen."

**Texto proposto, novo item na §2 ou na §5-bis (afastamento frontal):**

> "Afastamento frontal mínimo na ZPP: sem vaga descoberta nem subsolo nessa faixa, na leitura restritiva (Dec. 3.046/81, Disp. Gerais XXII e XXIII a, p. 4; Skill decreto3046 v1.5 §5 e R12; Skill vaga R3). O conflito com LC 270 Art. 363 §2º XII e COES Art. 28 IV fica para o Gate do Maurício. A subzona do lote é a confirmar via RIU (Kelsen)."

**Troca de remissão:** "conforme o parecer Legal do caso" → "LC 270 Art. 350 III", sem referência ao caso.

## 4. Pendências, por dono (Oscar não fala direto com Kelsen; passa por Lúcio)

**Kelsen (via Lúcio):**
- **K1.** O XXII (vaga descoberta vedada no afastamento frontal mínimo) incide sobre a subzona do lote? O dossiê (5.3) diz "ZPP, subzona A-ENS", e a Skill decreto (R6) diz que a nomenclatura de subzonas não está confirmada. Pergunta exata: "Pelo RIU do Lote 17, Quadra C, Rua das Garças, Recreio, a subzona de Dec. 3.046 é a A-ENS? O XXII se aplica a essa subzona?"
- **K2.** Errata ao parecer da Etapa 01, l. 181: a premissa da alternativa A não citou o XXII.
- **K3.** Tensão LC 270 Art. 363 §2º XII e COES Art. 28 IV × Dec. 3.046 XXII/XXIII a: Gate do Maurício.
- **K4.** R1 da Skill de vaga: a dimensão mínima de vaga é obrigatória na unifamiliar isolada, ou só vale se a vaga for projetada?
- **K5.** Manobra compartilhada (COES Art. 29 IV; Skill de vaga §3): reduz a média de 25,00 m² por vaga? Se reduzir, a conta da garagem muda.
- **K6.** R2 da Skill de vaga: na casa isolada, há número mínimo de vagas? Em condomínio de casas (46 lotes, 5.4), as vagas suplementares do Dec. 3.046 XXI (1 para cada 5 unidades, não vinculadas) se aplicam ao condomínio do lote, e afetam a área comum ou a faixa verde?

**Claudemberg (decisão de cliente ou de risco, via Lúcio):**
- **C1.** Número de vagas e onde ficam (4 ou 6, cobertas ou não): decisão do cliente no Briefing. A v6 não escolhe.
- **C2.** Alternativa A vedada e B inviável com a = 25,00: se o cliente quiser vaga descoberta no frontal, a saída vira nova alternativa, que é pendência de Claudemberg ou Kelsen, não decisão de Oscar.
- **C3.** Gate do Maurício antes de qualquer uso num caso real.

**Lúcio:**
- L1. Confirmar o nome do cliente (Seção 0, item 2).
- L2. Aplicar a Skill de levantamento v1.6 (Seção 3), se aprovar.
- L3. Escrever a nota 00 da v6 (não escrevi).
- L4. Encaminhar à Drenagem o espelho `.agents/skills` (item 4 do parecer).
- L5. Rever o status "v5 aprovada" do meu estado (Seção 0, item 4).
- L6. Villaça, S3/H1 (área de 339,84 a 359,84 m² sem espaço físico; a alternativa B era a saída e agora é inviável).

**Contagem:** a contagem de palavras das peças e do anexo da v6 é "a preencher por Wallenberg com ferramenta". Não tenho ferramenta de contagem e não estimei.

**Revit:** não testado nesta v6. Último teste, 06/10/2026: `No such tool available`.

## 5. Propagação e verificação (Grep na pasta v6, nas quatro peças e no anexo)

- **"12,50–15,00", "12,50 a 15,00", "15,00 m²/vaga":** nenhuma ocorrência nas peças 1, 2 e 3 nem no anexo. A única ocorrência de "12,50" no anexo é a composição vaga 2,50 × 5,00 (C-4), que é texto legal e não a faixa antiga.
- **Valores antigos da conta** ("419,94", "412,44", "394,94", "50,06", "47,56", "68,88", "66,38", "191,22", "183,72", "166,22", "43,7%", "72,9%", "1,71 m", "1,29 m"): nenhuma ocorrência nas quatro peças nem no anexo.
- **"Isca 4", "gabarito" como fonte, "LACRAD":** nenhuma citação como fonte. A Peça 2 declara "nenhum gabarito aberto", que é só declaração.
- **Peça 1:** não tinha garagem nem alternativa A. Mudou só no cabeçalho, em §0 (Revit), e em §9 (declaração de leitura): linhas 4, 9, 176 e 178.
- **Peça 2:** linhas 12, 17, 18, 33, 52–57, 62, 69, 72, 102, 124 e 134 (cabeçalho e assinatura).
- **Matriz:** linhas 4 (arquivo, linha 19), 9 (24), 13 (28), 21 (36), 22 (37), bloco de condições (10), nota final (43 e 45).
- **Anexo:** C-4 a C-9, C-13 a C-15, C-17, E-5, E-8, E-12, G (linhas 279–287), H, I-1 e I-2.

## 6. Declaração de leitura desta execução

Li, por caminho exato: `parecer_bardi_v5.md` (inteiro); `enunciado.md`; a entrega v5 (Peças 1–3, `anexo_contas_003_v5.md`, nota 00 da v5, só leitura); a Skill `vaga-estacionamento-dimensao-minima-coes-lc198-lc270-unifamiliar-rj` v1.0 (inteira); a Skill `decreto3046-81-lc270-2024-licin-barra-recreio` v1.5 (Grep "XXII|XXIII", linhas 9, 19, 143, 232, e leitura do checklist e da R12); a Skill `levantamento-topografico-cadastral-orientado-duli-licin-rj` v1.5 (inteira, com §5-bis); e o meu arquivo de estado. Não abri nem listei nada em `_gabaritos`, nem fiz Glob na raiz do ensaio_003. Não editei parecer, gabarito, `pendencias.json`, Skill nem a v5. Não fiz git push.

— Oscar, 08/10/2026 (v6)
