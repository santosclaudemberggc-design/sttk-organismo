---
name: coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj
description: "Parâmetros de ventilação natural, iluminação natural e pé-direito mínimo para edificações residenciais no RJ — COE (LC 198/2019), prismas, dutos e vãos."
version: "1.5"
changelog: "1.5 (02/11/2026, Kelsen, aprovado por Claudemberg) — rótulo NBR 15575-1:2024 trocado por NBR 15575-1:2025 (incorpora a Emenda 1 de 05/12/2025) no §1, no Registro de Erros e nas Fontes; números mantidos (2,50 m; 2,30 m; pp. 76, 102 e 105 do PDF), porque o parecer Kelsen de 02/11/2026 (`parecer_nbr15575-1_2025_comparacao_02-11.md`) achou idênticos 16.1.1, 16.2.1, Anexo F e Tabelas F.1/F.2; fonte passa a apontar o PDF 2025 em `D:\\008_Normas ABNT\\001_ABNT`. 1.4 (31/10/2026, Kelsen, revisão final do Briefing Único v2, ALTO 11) — §2 ganha o caso da casa unifamiliar/bifamiliar: prisma e afastamentos laterais, de fundos e entre edificações com mínimo de 1,50 m, sem H/4 (COES Art. 31, parágrafo único, consolidado SMU p. 17, conferido no PDF); o 3,00 m do PVI (Art. 5º §1º I, p. 4) fica para as demais edificações; PV da casa em 1,50 m é interpretação (Gate); §4 cita Art. 17 §3º (não §§3º e 4º). 1.3 (31/10/2026, Hely via Kelsen, continuação aprovada por Claudemberg) — §1 separa casa unifamiliar/bifamiliar (COES Art. 31 + NBR 15575-1:2025 item 16.1.1: 2,50 m; 2,30 m) do Art. 12 (só multifamiliar e mista); §4 nota do Art. 31 II sobre vãos na casa; Anexo F da NBR segue informativo. 1.2 (29/09/2026, Oscar via Lúcio, aprovado por Claudemberg) — confirmação de fonte primária do Hely (28/09, COES consolidado SMU): regra dos 6 m movida para Art. 18 §1º e retirada a afirmação de que acima de 6 m a ventilação mecânica é obrigatória; banheiro com exaustão mecânica citando Art. 17 §2º II e §4º (sem vão fixado, leitura interpretativa); R6 sem a explicação sem lastro do 1/8, citando Art. 18 §7º; nova seção 'Macetes de quem faz'. 1.1 (28/09/2026, Lúcio, aprovado por Claudemberg) — correções do treino em caso fictício: §3 PV como alternativa ao duto longo; §4 regra de vão para banheiro com exaustão mecânica marcada 'a confirmar'; nota em R6."
status: ativa-com-ressalva
created: 2026-09-21
author: Rotina Diária Skills v3.2
gestor_validador: lucio
agente_principal: oscar
cross_disciplina:
  - tenreiro
  - baumgart
  - landell
fonte_primaria_lida: "sim — LC 198/2019 Art. 5º, 12º, 14º, 17º e 18º lidos via câmara.rj.gov.br"
fonte_primaria_confirmada:
  fonte: "COES (LC 198/2019) consolidado SMU/Busca Fácil — Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf, lido por Hely em 28/09/2026 (confirmacoes_2026-09-28.md, item 1)"
  pontos:
    - { dispositivo: "Art. 17 §2º II (ventilação mecânica)", fonte_primaria_lida: sim }
    - { dispositivo: "Art. 17 §4º (transitórios: dutos, ar condicionado, mecânicos, ventokit)", fonte_primaria_lida: sim }
    - { dispositivo: "Art. 18 tabela (banheiros/lavabos: 1/10 natural, 1/8 dutos)", fonte_primaria_lida: sim }
    - { dispositivo: "Art. 18 §1º (duto natural sobre outros compartimentos, horizontal ≤ 6 m)", fonte_primaria_lida: sim }
    - { dispositivo: "Art. 18 §7º (iluminação na totalidade do vão, ventilação no mínimo na metade)", fonte_primaria_lida: sim }
metadata:
  tipo: Inteligência (Trilha A)
  norma_base: "LC 198/2019 — COE do Rio de Janeiro (Código de Obras e Edificações)"
  zona_geografica: "Rio de Janeiro (aplicável em toda cidade, incluindo Barra da Tijuca e Recreio)"
  tags:
    - ventilacao-natural
    - iluminacao-natural
    - pe-direito
    - prisma-ventilacao
    - coe-rj
    - oscar-revit
---

# COE RJ — Ventilação Natural, Iluminação e Pé-Direito em Edificações Residenciais
## LC 198/2019 — Parâmetros para Projeto

---

## POR QUE ESTA SKILL

Toda aprovação LICIN 2.0 no Rio de Janeiro precisa atender ao COE (LC 198/2019). Os erros mais frequentes em projeto residencial envolvem poços/prismas de ventilação subdimensionados, vãos de iluminação abaixo do mínimo e pé-direito fora do exigido — três fontes comuns de exigência da prefeitura na análise. Esta Skill reúne os parâmetros verificados direto no texto da lei.

---

## 1. PÉ-DIREITO MÍNIMO (Art. 12º e 14º; Art. 31 para casa)

**Primeiro, separe o tipo de edificação.** O Art. 12 do COES não vale para casa.

### Casa unifamiliar ou bifamiliar (COES Art. 31 + NBR 15575-1:2025, item 16.1.1)

O COES Art. 31 (consolidado SMU, p. 17) dispensa a casa unifamiliar e bifamiliar, "desde que mantidas as condições de salubridade e higiene da habitação", de: I área mínima; II "dimensões mínimas das circulações, dos compartimentos, dos vãos de iluminação e ventilação e dos reservatórios d´água"; III vagas; IV afastamento frontal para abrigo em telha vã; V acessibilidade; VI gás. O COES não fixa pé-direito para casa (o Art. 12 só fala de multifamiliar e mista: *interpretação*, Gate).

Para casa, o pé-direito mínimo vem da **NBR 15575-1:2025, item 16.1.1** (edição que incorpora a Emenda 1 de 05/12/2025; p. 64 da norma, p. 76 do PDF do acervo `D:\008_Normas ABNT\001_ABNT`):

| Compartimento da casa | Pé-Direito Mínimo |
|---|---|
| Regra geral (salas, quartos, cozinha etc.) | **2,50 m** |
| Vestíbulos, halls, corredores, instalações sanitárias e despensas | **2,30 m** |
| Teto com vigas, inclinado ou abobadado | 2,50 m em pelo menos 80% da superfície do teto; no restante, até 2,30 m |

Texto: "A altura mínima de pé-direito não pode ser inferior a 2,50 m. Em vestíbulos, halls, corredores, instalações sanitárias e despensas, é permitido que o pé-direito seja reduzido ao mínimo de 2,30 m." A obrigação de seguir a NBR vem do COES Art. 1º §3º III e do CDC Art. 39 VIII (*interpretação*, parecer Kelsen 31/10/2026). Atenção: 2,30 m na casa é **mais alto** que os 2,20 m do Art. 12 para transitórios. Não use 2,20 m em casa.

**Dimensões de cômodo na casa:** a NBR 15575-1 não as torna obrigatórias. O item 16.2.1 (p. 64 da norma, p. 76 do PDF) diz "sugere-se prever" o espaço para os móveis do Anexo F; o Anexo F se declara "(informativo)" (p. 90 da norma, p. 102 do PDF) e a Nota 1 da Tabela F.2 (p. 93 da norma, p. 105 do PDF) diz que a norma "não estabelece dimensões mínimas de cômodos". Ressalva: a Nota 2 da mesma tabela diz que, se o projeto adotar móveis opcionais, "as dimensões mínimas devem ser obedecidas" (dentro de anexo informativo; peso jurídico é *interpretação*, Gate).

### Residencial multifamiliar ou misto (Art. 12º, consolidado SMU p. 7)

Texto: "Os compartimentos das unidades residenciais em edificações multifamiliares ou mistas deverão atender às seguintes disposições quanto à altura útil mínima".

| Tipo de Compartimento | Pé-Direito Mínimo |
|---|---|
| Permanência prolongada (salas, quartos, escritórios) | **2,50 m** |
| Permanência transitória (banheiros, circulações, depósitos) | **2,20 m** |

### Não residencial (Art. 14º — referência cruzada para uso misto)

| Uso | Pé-Direito Mínimo |
|---|---|
| Salas e quartos hoteleiros | **2,60 m** |
| Lojas | **3,00 m** |
| Banheiros e circulações | **2,20 m** |

**Atenção:** pé-direito medido da laje ao piso acabado (não estrutura bruta). Em projetos BIM (Revit/Vitruvius): parametrizar com folga mínima de 5 cm para embutidos de forro.

---

## 2. PRISMAS DE VENTILAÇÃO E ILUMINAÇÃO — PVI e PV (Art. 5º; Art. 31, parágrafo único, para casa)

**Primeiro, separe o tipo de edificação.** O mínimo de 3,00 m do PVI não vale para casa.

### Casa unifamiliar ou bifamiliar: mínimo de 1,50 m (COES Art. 31, parágrafo único)

Texto da lei (COES consolidado SMU, p. 17; conferido por Kelsen no PDF em 31/10/2026): "Os prismas de ventilação e iluminação e afastamentos laterais, de fundos e entre edificações, de edificações unifamiliares ou bifamiliares, quando exigidos, serão de, no mínimo, um metro e cinquenta centímetros, independente da altura da edificação."

- Casa: prisma, quando existir, com lado mínimo de **1,50 m**, sem a regra H/4 (a lei diz "independente da altura da edificação").
- O mesmo 1,50 m vale para os afastamentos laterais, de fundos e entre edificações da casa, quando exigidos (para as demais edificações, o Art. 4º II e III, p. 3, fixa no mínimo 2,50 m).
- A legislação da zona (Dec. 3.046/81, LC 270/2024, convenção de condomínio) pode exigir mais. Vale a mais restritiva (R2).
- *Interpretação, Gate:* o parágrafo único fala em "prismas de ventilação e iluminação", sem separar PVI e PV. Lido de forma ampla, também o PV da casa passa a ter 1,50 m (e não 1,00 m). Até o Gate decidir, usar 1,50 m também no PV da casa, que é o lado seguro.

### Demais edificações (multifamiliar, mista, não residencial): COES Art. 5º, §1º (consolidado SMU, p. 4)

### PVI — Prisma de Ventilação e Iluminação (serve luz + ar para compartimento de permanência prolongada)

**Regra dimensional:**
- Seção horizontal **constante** ao longo de toda a altura
- Ângulos internos ≥ 90° (seção retangular ou poligonal convexa, nunca aguda)
- **Nenhum dos lados ≤ H/4** (onde H = altura do prisma = número de pavimentos × pé-direito)
- **Mínimo absoluto de qualquer lado: 3,00 m**

**Exemplo prático:**
- Edifício de 4 pavimentos (H ≈ 10 m) → cada lado ≥ H/4 = 2,5 m → prevalece o mínimo absoluto: **lado ≥ 3,0 m**
- Edifício de 20 pavimentos (H ≈ 50 m) → cada lado ≥ 50/4 = 12,5 m

**Erro comum:** projetar prisma com lado < 3 m em edifícios baixos, achando que a relação H/4 não seria acionada. Fora da casa, o mínimo de 3 m é incondicional. Na casa unifamiliar ou bifamiliar, o mínimo é 1,50 m (Art. 31, parágrafo único; ver acima).

### PV — Prisma de Ventilação apenas (serve ar para compartimento de permanência transitória: banheiro, lavabo, DML)

**Regra dimensional:**
- **Nenhum dos lados ≤ H/20**
- **Mínimo absoluto de qualquer lado: 1,00 m**

**Exemplo prático:**
- Edifício de 4 pavimentos (H ≈ 10 m) → lado ≥ H/20 = 0,5 m → prevalece o mínimo: **lado ≥ 1,0 m**
- Edifício de 25 pavimentos (H ≈ 62 m) → lado ≥ 62/20 = 3,1 m

---

## 3. DUTOS DE VENTILAÇÃO NATURAL (Art. 18, § 1º)

Texto da lei (Art. 18 §1º, fonte primária lida — COES consolidado SMU via Hely, 28/09): "Os dutos de ventilação natural poderão ser feitos sobre outros compartimentos e não poderão ter comprimento horizontal maior de que seis metros."

- Dutos de ventilação natural **podem passar sobre outros compartimentos**
- **Comprimento horizontal máximo: 6 m**
- Uso típico: ventilação de banheiros internos em apartamentos compactos

**O que a lei NÃO diz:** o Art. 18 §1º não diz que, acima de 6 m, a ventilação mecânica passa a ser obrigatória. Ele só proíbe o duto natural com mais de 6 m na horizontal. A saída fica a critério do projeto, entre as formas que a lei admite (ver §5 e Macetes).

**Implicação de projeto:** banheiro distante mais de 6 m da fachada ou de um PV não pode usar duto natural longo. Alternativas: (a) encurtar o duto para ≤ 6 m; (b) criar um PV (§2, lado ≥ 1,00 m e ≥ H/20) junto ao compartimento; (c) usar outra forma de ventilação admitida para compartimento de permanência transitória no Art. 17 §4º (ar condicionado ou equipamento mecânico). A ordem entre elas é decisão de projeto, não da lei. Planejamento de planta deve prever isso antes do lançamento estrutural.

**Nota de numeração:** o Art. 17 §1º trata de outro assunto (comunicação dos vãos com o exterior). Não citar Art. 17 para a regra dos 6 m.

---

## 4. VÃOS MÍNIMOS PARA ILUMINAÇÃO NATURAL (Art. 18º)

| Tipo de Compartimento | Proporção Mínima de Vão (área do vão / área do compartimento) |
|---|---|
| Salas de estar, quartos, dormitórios | **1/8 (12,5%)** |
| Cozinha, copa, refeitório | **1/10 (10%)** |
| Conjunto sala-cozinha integrada | **1/8 da área total integrada** |
| Banheiros com ventilação natural | **1/10** |
| Banheiros com ventilação por duto | **1/8** |
| Banheiros com exaustão mecânica | **A lei não fixa vão.** A tabela do Art. 18 só traz 1/10 (natural) e 1/8 (dutos). O Art. 17 §4º diz que os compartimentos de permanência transitória "deverão sempre possuir ventilação, que poderá ser assegurada por dutos, sistemas de ar condicionado ou equipamentos mecânicos, incluindo aparelhos tipo ventokit para banheiros"; o Art. 17 §2º II define ventilação mecânica como a "feita com o auxílio de equipamentos mecânicos". **LEITURA INTERPRETATIVA (Hely, 28/09, para auditoria de Kelsen):** com exaustão mecânica, o COES não exige vão mínimo no banheiro. Não foi achado regulamento complementar sobre isso. |

**Banheiros (tabela do Art. 18, fonte primária lida):** "Banheiros e Lavabos (apenas a ventilação é obrigatória). 1/10 quando natural, 1/8 quando por dutos". A proporção de vão se refere à ventilação, não à iluminação. A lei **não explica** por que o vão é maior (1/8) quando a ventilação é por duto.

**Art. 18 §7º:** "A iluminação deve ser garantida na totalidade do vão e a ventilação, no mínimo, na metade deste." Ou seja, a esquadria pode ter só metade da área abrindo, desde que o vão inteiro ilumine.

**Exemplo:** quarto de 12 m² → vão mínimo = 12/8 = **1,5 m²** de janela.

**Casa unifamiliar ou bifamiliar:** o COES Art. 31 II (consolidado SMU p. 17) dispensa as "dimensões mínimas ... dos vãos de iluminação e ventilação". As proporções da tabela acima não são exigência legal para casa; servem como referência de projeto. Continua valendo a condição de salubridade do caput e a exigência de ventilação e iluminação natural direta nos compartimentos de permanência prolongada (Art. 17 §3º, consolidado SMU p. 9, conforme parecer Kelsen 31/10/2026; *interpretação*, Gate). Os de permanência transitória seguem o Art. 17 §4º (só ventilação, que pode ser mecânica).

**Barra da Tijuca — aplicação:** apartamentos com planta aberta e cozinha integrada à sala seguem a regra de 1/8 da área total combinada. Relevante para os layouts típicos de condomínios horizontais da região.

---

## 5. VENTILAÇÃO NATURAL — MODOS ACEITOS PELO COE

O COE aceita as seguintes formas de ventilação natural:

1. **Vãos abertos diretos** para o exterior (fachada, cobertura)
2. **Via varandas ou terraços cobertos** que abrem para o exterior, afastamentos ou prismas
3. **Dutos** (comprimento horizontal ≤ 6 m, Art. 18 §1º — ver § 3 acima)
4. **Ventilação mecânica** (Art. 17 §2º II) — admitida expressamente para compartimentos de permanência transitória (Art. 17 §4º: dutos, ar condicionado ou equipamentos mecânicos, incluindo ventokit para banheiros). A extensão a "alguns usos não residenciais" não foi conferida na leitura de 28/09 — a confirmar antes de citar.

**Não é permitido:** ventilação de compartimento de permanência prolongada (quarto, sala) exclusivamente por duto ou por compartimento intermediário sem vão para o exterior.

---

## 6. BARRA DA TIJUCA E RECREIO — CONTEXTO

- Tipologia dominante: condomínios horizontais (casas e sobrados) e edifícios multifamiliares até 2 pavimentos em Subzona A (Decreto 3046/81)
- Lotes maiores: menor pressão sobre prismas, mas a regra H/4 ainda se aplica quando houver edifício com mais de 1 pavimento e fechamento lateral
- Bairros com restrições de gabarito (Decreto 3046/81): reduz H → reduz exigência de prisma, mas o mínimo de 3 m (PVI) e 1 m (PV) é sempre o piso para multifamiliar e misto. Para casa unifamiliar ou bifamiliar (tipologia Sttickler), o piso é 1,50 m, sem H/4 (Art. 31, parágrafo único)

---

## 7. MACETES DE QUEM FAZ (só onde a própria lei deixa escolha ao projetista)

Cada macete abaixo vem do texto do COES lido na fonte primária (consolidado SMU, via Hely 28/09). Nenhum vem de "praxe".

1. **O duto pode passar por cima de outros cômodos (Art. 18 §1º).** O limite é só o trecho horizontal de 6 m. O duto pode correr sobre forro de circulação, closet ou outro banheiro. Isso permite deixar o banheiro no miolo da planta sem PV próprio, desde que o trecho horizontal até a saída fique ≤ 6 m.
2. **Para banheiro, lavabo e demais transitórios, a forma de ventilar é escolha do projeto (Art. 17 §4º).** A lei aceita dutos, ar condicionado ou equipamento mecânico (inclusive ventokit). Quando o duto natural não cabe em 6 m, a lei não obriga a nenhuma saída específica: comparar custo e desempenho de PV, duto mais curto ou exaustão mecânica.
3. **Banheiro e lavabo não precisam de iluminação natural (tabela do Art. 18: "apenas a ventilação é obrigatória").** A proporção de vão serve à ventilação. Com isso, a janela de banheiro pode ser pensada só para ventilar, sem precisar de vidro grande para luz.
4. **Esquadria com metade fixa (Art. 18 §7º).** A ventilação precisa estar em no mínimo metade do vão, e a iluminação no vão inteiro. Uma janela com metade fixa e metade de abrir atende, desde que o vão total cumpra a proporção.

Observação: o macete 2 depende, para banheiro com exaustão mecânica sem vão, da leitura interpretativa do §4 acima (Kelsen audita antes de uso em caso real).

---

## RESSALVAS

**R1 — Versão do COE:** LC 198/2019 pode ter sido emendada após janeiro de 2019. Verificar se houve atualização antes de qualquer consulta de aprovação.

**R2 — Prevalência entre leis:** o Decreto 3046/81 (Barra/Recreio) e a LC 270/2024 podem estabelecer parâmetros adicionais ou exigências especiais para a ZE-5. COE é o mínimo; a legislação urbanística de zona pode ser mais restritiva.

**R3 — Uso misto:** projetos com uso misto (residencial + comercial) podem precisar atender ao maior pé-direito (ex.: 3,00 m de loja no térreo).

**R4 — Hely valida LICIN:** na hora da montagem do processo LICIN 2.0, Hely verifica se a análise municipal exige cálculo e inserção do PVI no memorial descritivo ou apenas na planta.

**R5 — Denominador H/4 do PVI não verificado por memória para edifícios altos (Lúcio, 21/09):** o COE anterior (Decreto-Lei 322/76) usava denominadores menores (H/5 ou H/6). Se LC 198/2019 realmente usa H/4, isso é endurecimento material. Para o contexto da Barra/Recreio (gabarito 2 pavimentos, H ≈ 5m), o mínimo absoluto de 3m prevalece sempre — risco operacional baixo. Para projetos multi-pavimento fora de zona de gabarito restrito, Hely deve confirmar o denominador exato no Art. 5º da LC 198/2019 antes do primeiro uso de Oscar.

**R6 — Tabela de banheiros: o 1/8 por dutos não tem justificativa na lei (revisto 29/09):** a tabela do Art. 18 traz "1/10 quando natural" e "1/8 quando por dutos" para banheiros e lavabos, onde "apenas a ventilação é obrigatória". A lei **não justifica** por que o duto exige proporção maior. A explicação anterior desta Skill ("com duto, a janela serve só para luz") foi retirada: não tem base no texto. O que a lei diz sobre vão está no Art. 18 §7º: iluminação na totalidade do vão, ventilação no mínimo na metade. Os números 1/10 e 1/8 valem como estão na lei. Oscar parametriza as janelas de banheiro no Revit por esses números, sem inventar a razão.

**R7 — Altura H dos prismas deve incluir espessura de lajes (Lúcio, 21/09):** os exemplos usam "H = n_pavimentos × pé-direito". H real inclui a espessura das lajes (≈ 20–25 cm por andar). Para 4 pavimentos, H real ≈ 10,8–11,0 m vs. 10 m estimado. O erro se torna material em edifícios de 10+ pavimentos. Oscar deve parametrizar o Revit com a altura total real do prisma (piso do 1º compartimento servido ao topo do último), não com estimativa simplificada.

---

## REGISTRO DE ERROS

- **31/10/2026 — origem: revisão final do Briefing Único v2 (ALTO 11); corrigido por Kelsen.** Erro: o §2 dizia que o mínimo de 3,00 m do PVI era "incondicional" e o §6 o chamava de "sempre o piso", também para casa. Para casa unifamiliar ou bifamiliar, o COES Art. 31, parágrafo único, fixa 1,50 m para prismas e afastamentos laterais, de fundos e entre edificações, "independente da altura da edificação". Também corrigida a citação "Art. 17 §§3º e 4º" para "Art. 17 §3º" (o §4º trata de permanência transitória e não exige ventilação natural). Conferido no PDF consolidado SMU: Art. 4º (p. 3), Art. 5º (p. 4), Art. 17 (p. 9), Art. 31 (p. 17).
- **31/10/2026 — origem: parecer Kelsen COES Art. 31 (`CONSTRUCAO_DO_ZERO/01_CEO/Gestores/Kelsen (Legal)/parecer_coes_art31_lc270_31-10.md`); corrigido por Hely.** Erro: o §1 aplicava o pé-direito do Art. 12 (2,50/2,20 m) a todo residencial, sem separar a casa. O Art. 12 só vale para multifamiliar e mista; a casa unifamiliar/bifamiliar é dispensada de dimensões pelo Art. 31 e segue a NBR 15575-1:2025 item 16.1.1 (2,50 m; 2,30 m em vestíbulo, hall, corredor, sanitário e despensa). Também acrescentado ao §4 que o Art. 31 II dispensa as dimensões de vãos na casa. Conferido em fonte primária: COES consolidado SMU pp. 7 e 17; NBR 15575-1:2025 pp. 76, 102 e 105 do PDF (lidas por Hely na edição 2024; iguais na 2025, parecer Kelsen 02/11/2026). Busca on-line na Câmara (31/10/2026): nenhuma LC de 2026 (296 a 302) altera o COES.

## FONTES VERIFICADAS

- **NBR 15575-1:2025** (incorpora a Emenda 1 de 05/12/2025) — `D:\008_Normas ABNT\001_ABNT\ABNT_NBR_15575_1_2025_Edificações_habitacionais_Desempenho_Parte.pdf` — itens 16.1.1 e 16.2.1 (p. 76 do PDF), Anexo F informativo (p. 102), Notas 1 e 2 da Tabela F.2 (p. 105) — lidos por Hely em 31/10/2026 na edição 2024; conferidos por Kelsen na edição 2025 em 02/11/2026, texto igual (`parecer_nbr15575-1_2025_comparacao_02-11.md`) ✓
- **COES consolidado SMU** — Art. 12 (p. 7) e Art. 31 (p. 17) — lidos por Hely em 31/10/2026 ✓

- **LC 198/2019 (COE RJ)** — Arts. 5º, 12º, 14º, 17º, 18º — lidos em [camara.rj.gov.br](https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/c1982019.html) ✓ (fonte primária)
- **COES (LC 198/2019) consolidado SMU/Busca Fácil** — `CONSTRUCAO_DO_ZERO/01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` — Art. 17 §2º II e §4º; Art. 18 tabela, §1º e §7º — lidos por Hely em 28/09/2026 (`confirmacoes_2026-09-28.md`, item 1) ✓ (fonte primária)
- **Instituto Bramante** — notas sobre pé-direito e ventilação no COE (complementar, confirmado pela fonte primária)
