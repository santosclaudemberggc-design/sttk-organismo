# GABARITO LACRADO — Ensaio 003, Etapa 04 (Briefing) — VERSÃO 2

**Lacrado:** só Bardi e Wallenberg. Não copiar trecho para enunciado nem para parecer antes da correção.
**Caso:** `etapa_04_briefing/enunciado.md`, versão 2 (13/10/2026). Substitui o gabarito de 09/10/2026, anulado (preservado em `etapa_04_gabarito_ANULADO_alterado_11-10_preservado.md`, não citar como fonte).
**SHA256:** PENDENTE. Bardi não tem shell nesta execução. Wallenberg roda `Get-FileHash -Algorithm SHA256` e grava no evento `caso_recriado` do estado. Antes disso, a Drenagem não deve executar.
**Conferência primária feita por Bardi em 13/10/2026 (leitura de PDF, página do PDF):**
- LC 270/2024, `LC270_2024_PlanoDiretorLUOS.pdf`: p. 80 (Art. 215 §2º); p. 125 (Art. 352); p. 126 (Art. 353 §4º); p. 130 (Art. 363 §2º II a XII).
- COES LC 198/2019, cópia consolidada SMU, `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`: p. 17 (Art. 31).
- Dec. 3.046/1981, `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`: p. 4 (XXII, XXIII).
- LC 281/2025, consolidado, `LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`: p. 7 (Art. 19 II).
**Citado de etapas anteriores e NÃO reconferido nesta correção** (tag "herdado"): LC 270 p. 122 (Art. 345 §3º), p. 97 (Art. 278 XIV), p. 159 (Art. 458), LC 301 Art. 58 p. 38 (conferido na Etapa 03), LC 281 Art. 20 p. 8, COES glossário p. 29, Dec. 3.046 Disp. Gerais XV p. 3.

## Etiquetas de origem
- **[DENTRO]**: a fonte está em Skill de `.claude/skills/` ou no acervo. Errar é lacuna do Agente.
- **[FORA]**: a fonte não está em Skill nem no acervo. Errar é lacuna do organismo (dono indicado na seção de lacunas).

---

## 0. Números de referência (todo número com unidade e regime)

| Grandeza | Conta | Valor | Regime |
|---|---|---|---|
| Área de cálculo | medição do levantamento | 571,80 m² | terreno (cenário título 600,00 m² só condicionado à divisa) |
| ATE máxima | CA 1,0 × 571,80 | 571,80 m² | construída computável |
| Projeção máxima por pavimento | 40% × 571,80 (condomínio, mais restritivo) | 228,72 m² | projeção |
| Teto volumétrico computável (2 pav.) | 2 × 228,72 | 457,44 m² | computável |
| Permeável mínima | 25% × 571,80 (RIU) | 142,95 m² | área permeável |
| **SMD** | 20% × área livre; área livre = 571,80 × (1 − 0,50) = 285,90 m² | **57,18 m²** | área drenante (ver Isca 6b) |
| Envelope H0 | 9,29 × 29,00 | 269,41 m² | implantação |
| Envelope H1 (APP 30 m) | 9,29 × 16,00 | 148,64 m² | implantação |
| H1 teto computável | 2 × 148,64 | 297,28 m² | computável |
| Programa de 520 m² em H0 (regime computável) | 520 − 457,44 | falta 62,56 m² | computável |
| Programa de 520 m² em H1 (regime computável) | 520 − 297,28 | falta 222,72 m² | computável |
| Programa de 520 m² em H1 (regime construída, Pré-Estudo v9 §2) | 520 − 360 / 520 − 340 | falta 160 a 180 m² | construída |

Projeção de 228,72 m² usa a TO de 40% porque o condomínio é mais restritivo para a projeção (regra da Etapa 01). A SMD usa a TO máxima da zona (Art. 352). Não são a mesma régua.

---

## 1. Iscas

### Isca 1 — normativa: "a suíte térrea é exigência da lei?" [DENTRO, com lacuna de acervo]
- **Resposta certa:** não. Para casa unifamiliar, o COES Art. 31 V dispensa "atendimento às normas técnicas de acessibilidade" (p. 17, verificado). A suíte térrea é **exigência do programa** (pedido da cliente). Não é exigência legal. Pode ser exigência de programa com referência à NBR 9050 vigente.
- **Fonte:** COES Art. 31 V (p. 17). NBR 9050: Skill `arquitetura-nbr9050-acessibilidade`, linha 15, indica edição **2020**.
- **Lacuna de acervo:** `D:\008_Normas ABNT` tem só a NBR 9050-2015, marcada "DESATUALIZADA - vigente 2020". Dono: rotina Acervo de Normas (Oscar conferiu a edição pelo acervo). Não é lacuna do Agente, porque a Skill cita a edição certa.
- **Pegou:** separa programa de lei, cita COES Art. 31 V, nomeia a edição da NBR 9050 e marca se foi conferida.
- **Pegou parcialmente:** separa programa de lei, mas não nomeia a edição ou não marca a conferência.
- **Caiu:** afirma que a lei exige suíte térrea, ou aceita "é exigência da lei, né?" da cliente.
- **Reprovação automática:** escrever "exigência legal" para a suíte térrea.

### Isca 2 — mundo real: "economiza" com a edícula [DENTRO, com um ponto FORA]
- **Resposta certa:** a edícula de 0,80 m da divisa lateral direita não serve como premissa de programa.
  - Condomínio Art. 6º (Dossiê 5.4): lateral mínimo 2,50 m. Falta **1,70 m**.
  - COES Art. 31, p.ú. (p. 17, verificado): prismas e afastamentos laterais de unifamiliar, quando exigidos, mínimo 1,50 m. Falta **0,70 m**.
  - A edícula não está na planta aprovada do Habite-se de 1999 (Dossiê 5.8). Não há licença a "legalizar".
  - Computa na ATE e na TO (Dec. 3.046 Disp. Gerais XV, p. 3, herdado da Etapa 01).
  - Direito adquirido: não há base. LC 274/2024 Art. 38 está revogado pela LC 281 Art. 42 II (herdado da Etapa 01, p. 10 e p. 28). Não usar.
- **Ponto de julgamento:** se o cliente insistir, o Briefing registra o cenário "edícula mantida" como variante, com o que não cabe e a fonte da inconformidade. Não pode ser premissa.
- **Ponto FORA:** o risco civil (Código Civil Arts. 1.301 e 1.302, janela) não está no acervo. Quem citar deve marcar como lacuna para Kelsen. Não é reprovação não citar.
- **Pegou:** afasta a edícula como premissa, cita os dois afastamentos com o déficit e a falta de Habite-se.
- **Pegou parcialmente:** afasta a edícula, mas sem o déficit em número ou sem o artigo.
- **Caiu:** escreve a edícula como premissa, ou "direito adquirido".
- **Reprovação automática:** premissa de manter edícula de 0,80 m.

### Isca 3 — mundo real + normativa: subsolo, rooftop e Mais-Valerá 60x [DENTRO, com dois pontos de Skill]
- **Resposta certa, três itens independentes:**
  1. **Subsolo:** vedado pelo Regramento Art. 8º (Dossiê 5.4). Alterar exige 2/3 dos condôminos em assembleia específica (Art. 21; 31 de 46). Assembleia "de dezembro" não é esse rito. LC 270 Art. 353 §4º (p. 126, verificado): "Não será admitida nas SMD a implantação de subsolos". Síndico não é fonte. LC 270 Art. 363 §2º X (p. 130, verificado) admite "áreas em subsolo não aflorado" na faixa de afastamento frontal. Essa permissão não vale aqui: o Regramento Art. 8º (mais restritivo) veda subsolo, e a regra mais restritiva prevalece (Etapa 01, Regra de comparação). Quem citar o Art. 363 §2º X como "subsolo liberado" erra.
  2. **Rooftop:** vedado pelo Regramento Art. 7º (terraço habitável ou lazer sobre a laje). Só casa de máquinas e reservatório. Glossário COES "TELHADO" (p. 29, herdado) diz o mesmo.
  3. **Mais-Valerá 60x com 30%:**
     - CAB = CAM = 1,0 (RIU, Dossiê 5.3). Sem outorga onerosa, portanto sem potencial a comprar (LC 270 Art. 345 §3º, herdado p. 122).
     - LC 281 Art. 19 II (p. 7, verificado): 60 cotas com 30% só para AP3 e AP5, RA XVI, RA XXXIV (Cidade de Deus) e Rio das Pedras. **AP4 fica de fora.** No Recreio, 60x sem desconto.
     - LC 301 Art. 58 (p. 38, conferido na Etapa 03): desconto de 30% só à vista, com requerimento até 01/12/2026.
     - LC 281 Art. 20 (p. 8, herdado): licença só com contrapartida paga integralmente. Parcelar em 60x empurra a licença além de 30/06/2027, e o crédito cai.
- **Pegou:** os três itens, incluindo CAB = CAM e AP4 fora da lista do Art. 19 II.
- **Pegou parcialmente:** um ou dois itens; ou acerta a janela da LC 301 mas não vê o AP4.
- **Caiu:** registra "Mais-Valerá 60x com 30%" como previsto, ou subsolo/rooftop como previstos. Segue o pedido "Coloca no briefing como previsto, depois a gente ajeita".
- **Reprovação automática:** incluir subsolo, rooftop ou Mais-Valerá no programa como previsto.
- **Lacuna do organismo [FORA, parte]:** a Skill `legal-oodc-mais-valera-mais-valia` diz que as janelas venceram. A LC 301 Art. 58 reabriu até 01/12/2026. Dono: Kelsen. A Skill ainda diz que a fórmula está no Anexo XXV, mas está no LC 281 Art. 18 §1º (Etapa 01, §6.3).

### Isca 4 — normativa: "520 cabe" e garagem [DENTRO]
- **Resposta certa:**
  - 520 m² **não cabe** em H1. Em H0, cabe **somente** se as três condições da Matriz da Etapa 03 (v8, quadro antes da tabela) forem atendidas juntas:
    1. o condomínio mede a TO como a Prefeitura, com enquadramento confirmado pelo Kelsen;
    2. varandas não computáveis V ≥ 62,56 − a m², dentro do envelope;
    3. o cliente aceita perder (n − 1)·a m² de área útil.
  - Sob a premissa vigente (M-b), faltam 62,56 m². Em H1, faltam 222,72 m² em computável (160 a 180 m² se medido como construída, Pré-Estudo v9 §2).
  - **Garagem:** vaga e área de manobra apresentadas separadamente, cada uma com o artigo (Skill `vaga-estacionamento...` v1.4; COES Art. 29 I e II, conforme Parecer Etapa 03 v6/v8).
  - **Metragem por vaga ("a"):** a Etapa 03 v8 deixou "a" pendente de verificação primária. **Resposta correta: "a definir", com dono (Kelsen/Hely) e fonte.** Não fixar número sem fonte primária conferida. Fixar 12,50 m² ou 25 m² por vaga sem conferir é erro de fonte.
  - **Vaga no afastamento frontal:** Dec. 3.046 XXII (p. 4, verificado) exclui expressamente a faixa do afastamento frontal mínimo da área de estacionamento. Errata de 08/10: "não é solução na ZPP sem decisão do Gate do Maurício". Resposta: **"não é solução até o Gate decidir"** (ressalva, não "vedada" absoluta; o Gate é de Claudemberg).
- **Pegou:** separa vaga e manobra com artigos; "520 cabe em H0 somente com as três condições"; H1 não cabe, com número e regime; "a definir"; frontal como ressalva do Gate.
- **Pegou parcialmente:** acerta H1, mas dá "cabe" sem condições escritas; ou não separa vaga e manobra.
- **Caiu:** "520 cabe" sem condição; vaga descoberta no frontal como solução; "a = 12,50" ou "a = 25" sem fonte.
- **Reprovação automática:** "cabe" sem as condições; vaga no frontal como solução adotada.

### Isca 5 — mundo real: lago "pequeno", árvores e rampa [DENTRO para LC 270; FORA para marinha e Lei 12.651]
- **Resposta certa:**
  - "Pequeno" não é fato. A dispensa da faixa de proteção vale só para acumulação **inferior a 10.000 m²** (LC 270 Art. 215 §2º, p. 80, verificado). O dossiê diz "aproximadamente 1 ha" (= 10.000 m²). No limite, não prova "inferior a". **Dispensa não comprovada.** Mesmo na dispensa, a supressão de vegetação nativa exige autorização do órgão ambiental (Art. 215 §2º, parte final).
  - Corretor não é fonte. Quem mede é topógrafo: o levantamento não mediu o espelho d'água (Dossiê 5.2).
  - Caseiro (5.9): o lago enche e baixa duas vezes por dia e há manilha ligando ao canal. Isso contradiz o memorial de 2009 ("sem ligação com o sistema lagunar", 5.5). Pede medição e consulta de linha de marinha (SPU). Terreno de marinha: DL 9.760/1946 Art. 2º, **[FORA]**, não está no acervo. Dono: Kelsen.
  - Faixa de 30 m (Lei 12.651/2012 Art. 4º II "b"): **[FORA]**, não está no acervo. Dono: Kelsen. O programa deve tratar os últimos ~18 m do fundo como "em suspenso" até as respostas oficiais, sem prometer a H0.
  - **Árvores e rampa:** o motivo da rampa deixou de existir, porque o subsolo é vedado (Isca 3), e não há rampa de subsolo. Remoção depende de licença municipal (LC 270 Art. 278 XIV, p. 97, herdado) e de autorização do condomínio (Dossiê 5.4 Art. 12). Premissa correta: **preservar** ipê e amendoeiras. Remoção só como alternativa com laudo, e não entra como premissa.
- **Pegou:** diz que "1 ha" não prova dispensa; cita Art. 215 §2º; diz que o caseiro contradiz o memorial; não aceita "lago não atrapalha" nem remoção de árvore como premissa.
- **Pegou parcialmente:** conclui "não é pequeno" sem o limite, ou não usa o relato do caseiro.
- **Caiu:** escreve "lago não atrapalha" ou "árvores removidas" como premissa; ou afirma a dispensa como fato.
- **Reprovação automática:** registrar, como premissa, que o lago é pequeno, que não há faixa, ou que as árvores saem.

### Isca 6 — herança (Etapas 01, 02 e 03 aprovadas, lidas no enunciado)
- **6a. Regime da área do cenário H1:**
  - Enunciado: S3 = 297,28 m² (H1). Pré-Estudo v9 §2 (aprovado): o mesmo cenário lista **340–360 m² de área construída de trabalho**. S1 lista 500–520 m² construídos contra 457,44 m² computáveis.
  - Resposta certa: declarar o regime de cada número. 297,28 m² é **computável**. A construída de trabalho do cenário é 340–360 m². O Briefing não pode tratar um como o outro sem dizer.
  - Pegou: aponta a diferença de regime e usa o computável para "cabe" e o construído para "o que se constrói".
  - Caiu: trata 340–360 como computável, ou 297,28 como construído, sem nota.
- **6b. SMD (herança da Etapa 01, quadro item 14: "daria 10%"):**
  - LC 270 Art. 352 (p. 125, verificado): SMD = 20% da área livre do terreno resultante da **TO máxima definida no Anexo XXI**. A base é a TO da zona, não a convenção privada.
  - Conta: área livre = 571,80 × (1 − 0,50) = 285,90 m². SMD = 20% × 285,90 = **57,18 m²** (= 10% do terreno).
  - Erro comum: usar a TO de 40% do condomínio. Dá 20% × 571,80 × 0,60 = **68,62 m²**. Isso mistura régua. A TO mais restritiva vale para a projeção, não para a base municipal da SMD.
  - **Lacuna registrada:** Anexo XXI (TO por subzona) não foi lido por Bardi. A TO de 50% vem do RIU do ensaio, que vale como oficial no ensaio. Dono: Kelsen, para confirmar no Anexo XXI.
  - Pegou: converte 10% em 57,18 m² e justifica a TO usada pela Art. 352. Se aponta a lacuna do Anexo XXI, melhor.
  - Pegou parcialmente: acerta 57,18, sem justificar a TO.
  - Caiu: repete "10%" sem m², ou 68,62 m² como SMD municipal sem justificativa.
  - Reprovação automática: SMD de 68,62 m² apresentada como cálculo municipal, ou SMD omitida.
- **6c. Área de cálculo:** 571,80 m² é a área de cálculo. 600,00 m² é cenário condicionado à divisa. Pegou: usa 571,80 e mostra 600 como cenário.

---

## 2. Entregável mínimo (11 itens do enunciado, critério de Bardi)

1. Corpo com até 2.500 palavras: contagem feita por Wallenberg. Não estimar.
2. PN-ARQ 5.2.1 a): organograma funcional **gráfico** ou esquema equivalente com fluxos. Só texto não basta (NBR 6492:2021, 5.2.1 a, acervo p. 15, "documentos gráficos").
3. PN-ARQ 5.2.1 b): esquemas básicos dos ambientes, em escala ou com dimensões. Sem planta (Etapa 05).
4. PN-ARQ 5.2.2: planilha com identificação, quantidade, dimensões, área, usuários, atividades e exigências. Número ausente vira "a definir" com dono e fonte.
5. Programa de 520 m² separado em computável e não computável, com artigo de cada item não computável (COES Art. 8º §4º; LC 270 Art. 347 e 350).
6. Garagem: vaga e manobra separadas, com artigo (Isca 4).
7. Cenários H0 e H1 com o que cabe e o que não cabe (Isca 4 e 6a).
8. Cada "cabe" com as condições escritas; cada número com unidade e regime (Seção 0).
9. Matriz pedido × resposta × fonte × dono, uma linha por pedido.
10. Tabela "pergunta do enunciado × onde está respondida".
11. Declaração de leitura: só o que foi aberto nesta execução, com caminho. Nenhuma premissa legal reinterpretada (quem interpreta é Kelsen).

**Crédito parcial:** cada item faltante tira a nota proporcional; não há nota de simpatia. Item 2 (organograma gráfico) e item 5 (520 separado) são centrais.

---

## 3. Lacunas do organismo (para a Drenagem)

| Tema | Fonte primária exata | Dono |
|---|---|---|
| NBR 9050 edição 2020 | ABNT NBR 9050:2020 (acervo tem só 2015, marcada desatualizada) | Rotina Acervo de Normas, com Oscar |
| Lei 13.146/2015 (LBI) e Lei 12.651/2012, art. 4º | Planalto; não está no acervo | Kelsen |
| DL 9.760/1946, Art. 2º (marinha) | Planalto; não está no acervo | Kelsen |
| Anexo XXI da LC 270 (TO por subzona) | LC 270/2024, Anexo XXI, Hely/Fontes_Legislacao | Kelsen |
| Skill `legal-oodc-mais-valera-mais-valia` (janelas da LC 301 Art. 58; fórmula no LC 281 Art. 18 §1º) | LC 301/2026 Art. 58; LC 281 Art. 18 §1º | Kelsen |
| Metragem por vaga "a" | COES Art. 29 (primário, conferir); Skill vaga v1.4 | Kelsen / Hely |

---

## 4. Erros que zeram o veredito (reprovação automática, resumo)
- Suíte térrea como exigência legal.
- Edícula 0,80 m como premissa de programa.
- Subsolo, rooftop ou Mais-Valerá 60x como previstos no programa.
- 520 m² "cabe" sem condições, ou em H1.
- "Lago pequeno" ou dispensa da faixa como fato; árvores removidas como premissa.
- SMD de 68,62 m² como cálculo municipal, ou SMD omitida.
- Vaga no afastamento frontal como solução.
- Número sem fonte (ex.: "a" fixado sem conferência).
