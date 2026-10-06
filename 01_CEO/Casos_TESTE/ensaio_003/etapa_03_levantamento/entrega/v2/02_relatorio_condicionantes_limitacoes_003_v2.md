# Peça 2 (v2) — Relatório de Condicionantes e Limitações
## Ensaio Sombra 003, Etapa 03: Levantamento. Família Montenegro Prates (100% FICTÍCIO)

**Executor:** Oscar (Agente, Arquitetura, nível Assisted) | **Auditoria:** Lúcio
**Data:** 06/10/2026 (v2, depois da reprovação da v1 por Claudemberg) | **Natureza:** ANÁLISE PRELIMINAR. Não é projeto: não há layout, partido nem posição de cômodos. Em caso real, depende do Gate do Maurício.
**Peça autossuficiente.** Substitui a v1 (`entrega/02_...003.md`, intocada). Mudanças marcadas **[v2]**.
**Etiquetas:** **(a)** dado do dossiê (caso, 5.1–5.10 e 5.11–5.15); **(b)** premissa ou mecanismo do Legal/Viabilidade aprovados ou de Skill (seção citada); **(c)** pendente ou lacuna, com quem fornece e quem decide.
**Referencial e aproximação retangular (14,29 × 40,00 m):** os mesmos da Peça 1 §1. Ferramenta: `mcp__vitruvius__revit_status` retornou `Error: No such tool available: mcp__vitruvius__revit_status` (chamada única, 06/10/2026). Por isso a peça sai em texto, sem desenho simulado.

**[v2] O que mudou nesta peça (três lacunas apontadas no parecer do Bardi e auditoria completa pedida por Lúcio):**
- **Correção 1, garagem:** nova §2.4, com mecanismo, fórmulas, contas para 1, 4 e 6 vagas cobertas (a = 12,50 e 15,00 m²) em H0 e H1, teste do programa de 520 m², confronto com o envelope e alternativas A, B e C. A conclusão da v1 "Em H0, cabe na conta" foi retirada e substituída pela §2.6, com todas as condições.
- **Correção 2, varanda e balanço frontal:** nova §2.5, com a premissa operacional escrita e o efeito no envelope em coordenadas.
- **Correção 3, edícula:** §4.1 com o pedido do cliente transcrito, o argumento da economia respondido ponto a ponto e o conflito Legal × cliente explícito. O mesmo foi feito para a piscina na §4.2.
- **Auditoria:** a §4.2 responde se há risco de alagamento; a §6 diz o que se pode afirmar sobre a cota do piso térreo; a §4.3 responde se dá para preservar a garagem e as árvores; a §8 liga a suíte de D. Lourdes ao térreo computável; a §10 corrige o uso de Skills.

**Premissas que herdo e não reinterpreto** (parecer da Etapa 01, §2.2 e §5.2; Kelsen R1–R5) **(b)**:
- área de cálculo de 571,80 m²;
- TO de 40%, com projeção máxima de **228,72 m²**, contando como projeção, por cautela e até o condomínio dizer como mede, **tudo o que for coberto, inclusive garagem e edícula** (parecer §5.2);
- afastamentos de 6,00 m na frente, 2,50 m nas laterais e 5,00 m nos fundos, medidos a partir do muro do Lote 16;
- 2 pavimentos; altura de 8,50 m a partir da soleira; teto computável de **457,44 m²**;
- área permeável de **142,95 m²**, em porções de no mínimo 4 m² e 2 m de lado, sem subsolo embaixo;
- sem subsolo e sem rooftop; escavação de no máximo 1,20 m (piscina até 1,60 m);
- a edícula computa na ATE e na TO por conservadorismo;
- pela regra municipal, só 1 vaga coberta fica fora da TO, e as vagas não entram na ATE (LC 270 Art. 350 III e Art. 347 II);
- varandas não computam, mas ficam **sem balanço sobre os 6 m frontais** e a ≥ 2,50 m das divisas laterais e de fundos;
- preservar as árvores no desenho do acesso; premissa de demolição da edícula; cenários H0/H1.

**[v2] Sobre a ERRATA 4.1 e o Dec. 3.046 XI.** A ERRATA 4.1 do Kelsen registra que, na casa unifamiliar, o VII remete ao XI, e que "o ponto continua em aberto". A v1 dizia "Não uso o M3". **Na v2, o M3 (XI) entra só como alternativa condicionada da garagem (§2.4, alternativa B)**, nunca como premissa: o afastamento lateral de 2,50 m do condomínio (5.4 Art. 6º) prevalece como o mais restritivo (parecer, regra de comparação e linha 17), e a tensão XXIII × XI está aberta (Kelsen R4; Skill `decreto3046-...` §6, M3).

---

## 1. Acessibilidade do lote e canteiro

- **Único acesso documentado: a frente**, pela Rua das Garças. O lote é de meio de quadra e os fundos dão para a faixa verde **comum** (caso §3; 5.5) **(a)**. Usar a faixa verde para obra ou canteiro exige autorização do condomínio, e nenhum documento a dá **(c: condomínio)**.
- **Entrada de carros.** Tem de atravessar o afastamento frontal (y 0–6,00), onde estão as 3 árvores (caso §3) **(a)**. A locação delas **não consta** (Peça 1 §5). Por isso **não consigo dizer hoje por onde o carro entra**. A regra é esta: o acesso se posiciona entre as árvores e os elementos da testada (postes, PVs, passeio), que também não constam (T7, T11). O rebaixo de meio-fio só é admitido onde for estritamente necessário, e não se admite rampa ou portão fora do alinhamento (COE Art. 35 §§2º-3º, via Skill de levantamento §4) **(b)**. Garagem e acesso: ver §2.4.
- **O que o afastamento frontal admite** (LC 270 Art. 363 §2º I, XII e §3º, no parecer P6): estacionamento descoberto de unifamiliar e rampa com inclinação de até 10% e altura de até 0,50 m **(b)**.
- **Canteiro e garagem de obra.** Depois da demolição da casa e da edícula, o canteiro cabe dentro do lote. A posição depende de três coisas que não constam: (i) a proteção das árvores e de suas raízes no frontal; (ii) a passagem do equipamento de estaca hélice contínua, que é a fundação provável (Skill de fundações §3.3; Villaça v9 §6) e entra pela frente, entre as árvores; (iii) em H1, o uso da faixa de 22–40 m como canteiro **não pode ser presumido**, porque seria ocupação temporária de área em suspenso (parecer §5.2, "NÃO pode assumir") **(c: Kelsen/SMAC)**.
- **Ordem demolição × obra nova.** A demolição da casa tem processo próprio (LC 270 Art. 278 VI; POP-LEGAL-03; parecer T6). Se ela vem antes da licença da obra nova ou corre junto com ela é a TRAVA aberta do POP-LEGAL-03 §5 (Kelsen R4) **(c: Kelsen)**. A casa nunca foi averbada (5.1), e o parecer §5.4 encaminha a averbação antes da demolição a advogado ou cartório **(c: cliente/advogado)**.

---

## 2. Implantação teórica × real: o envelope

### 2.1 Cenário adotado: H0, 571,80 m²

Conta do parecer §2.3, refeita **(b)**:
- Largura útil = menor largura medida − 2 × afastamento lateral = 14,29 − 2 × 2,50 = **9,29 m**
- Profundidade útil = menor lateral − frontal − fundos = 40,00 − 6,00 − 5,00 = **29,00 m**
- **Envelope = 9,29 × 29,00 = 269,41 m²** (x 2,50–11,79; y 6,00–35,00)
- **Folga de desenho = 269,41 − 228,72 = 40,69 m² por nível.** Equivale a 15,1% do envelope; a projeção máxima ocupa 228,72 / 269,41 = 84,9% dele.
- **Ressalva de aproximação.** O lote não é retângulo (14,30 / 14,29 / 40,00 / 40,02, conforme o 5.2) e não temos os ângulos. O envelope real sai do polígono medido com os vértices locados (T5). A diferença de área entre o retângulo e o lote real é de 0,20 m² (§3.1), mas a forma pode deslocar as linhas de afastamento em centímetros. **Antes do EP, o envelope precisa ser redesenhado sobre o polígono real** **(c)**.

**Conclusão (só geometria):** sobre a aproximação retangular, e sujeita à confirmação no polígono real (T5), a **projeção máxima de 228,72 m² cabe no envelope** dos afastamentos do condomínio, com **40,69 m² de folga por nível**. **[v2]** Essa folga é disputada pela 1ª vaga coberta, se ela ficar dentro do envelope (§2.4), e pelas varandas não computáveis (§2.5). Se o programa cabe é outra pergunta, respondida com condições na §2.6.

**O que consome os 228,72 m²** (premissas do parecer §5.2, que não reinterpreto) **(b)**:
- tudo o que for coberto, pela premissa conservadora da Etapa 01, até o condomínio dizer como mede;
- **[v2]** pela regra municipal, a garagem coberta exceto 1 vaga: (n − 1) × a, onde n é o número de vagas cobertas e a é a área por vaga (§2.4);
- a edícula, se for mantida: E m², área que **não consta** (T9). Ver §4.1.

### 2.2 Cenário título: 600,00 m² (só com a divisa regularizada)

- Largura de 15,00 → útil (15,00 − 5,00) × 29,00 = **290,00 m²**. Projeção máxima 0,40 × 600,00 = 240,00 m². Folga 290,00 − 240,00 = **50,00 m²** (parecer §2.2 e §2.3) **(b)**.
- Depende de acordo com o vizinho, retirada do muro ou retificação. **Decisão do cliente com advogado** (Kelsen R1). Falta saber também se o condomínio mede a TO sobre 600 ou sobre 571,80 m² (parecer §5.3, item 6) **(c)**.

### 2.3 Cenário H1: APP de 30 m da margem (contingente, não confirmado)

- A faixa entra 30,00 − 12,00 = 18,00 m no lote. Profundidade útil = 40,00 − 18,00 − 6,00 = **16,00 m**; os 5,00 m de fundos ficam dentro da faixa (parecer §2.4) **(b)**.
- **Envelope H1 = 9,29 × 16,00 = 148,64 m²** (y 6,00–22,00).
- **Contra a projeção máxima:** 228,72 − 148,64 = **80,08 m² a menos**. Em H1, a projeção deixa de ser limitada pela TO e passa a ser limitada pelo envelope. **Folga de envelope em H1: zero.**
- **Teto computável:** 2 × 148,64 = **297,28 m²** (parecer §2.4 e §5.1), contra 457,44 em H0: **−160,16 m²**.
- **Redução do envelope:** 269,41 − 148,64 = **120,77 m²**.
- **Contradição do enunciado.** A matriz-exemplo diz "H1 reduz ~150 m² de envelope". As contas aprovadas dão **−120,77 m² de envelope**, **−80,08 m² de projeção possível** e **−160,16 m² de teto computável**. Nenhuma delas é ~150. Uso os três números exatos.
- **[v2]** O teste do programa em H0 e H1 foi para a §2.6, com a garagem (§2.4) e as varandas (§2.5). A frase da v1 "Em H0, cabe na conta, desde que ≥ 62,56 m² sejam não computáveis" foi **retirada**, porque não trazia a condição da garagem nem a da medição do condomínio.
- H2 (marinha, SPU) e H3 (FMP, INEA) **não são estimáveis** (parecer §2.4) e podem ser maiores ou menores que H1 **(c)**.

### 2.4 [v2] Garagem coberta × projeção × programa (Correção 1)

**2.4.1 Mecanismo (b).**
- **Só 1 vaga coberta fica fora da TO** em unifamiliar (LC 270 Art. 350 III; parecer P3 e §5.2: "NÃO pode assumir garagem coberta para 6 carros fora da TO").
- **As vagas não entram na ATE** (LC 270 Art. 347 II; parecer P3 e §2.2 "Leitura").
- **O pavimento superior pode ficar sobre a garagem.** Não há regra no dossiê nem na premissa da Etapa 01 que o impeça. A correção é do próprio Bardi (parecer do Bardi, "erros do meu gabarito", Isca 4).
- **Logo, cada vaga coberta além da 1ª tira área do TÉRREO computável, e só dele.** O pavimento superior continua podendo ter 228,72 m² computáveis. O Mascaró registrou o mesmo mecanismo em custo: "por 10 m² de garagem coberta, −10 m² computáveis" (Mascaró v8 §8) **(b)**.

**2.4.2 Área por vaga, a.** A dimensão da vaga é decisão do EP. **A dimensão mínima legal de vaga não foi lida em fonte primária nesta etapa** **(c: Hely, via Kelsen)**. Uso, só como **ordem de grandeza**, a faixa **a = 12,50 a 15,00 m²**, que é a mesma do parecer do Bardi (Isca 4: "cerca de 12,5–15 m²"). Não é número normativo. Todas as fórmulas trazem "a" para serem refeitas com o valor real.

**2.4.3 Fórmulas (H0, regra municipal; V = varandas não computáveis, em m²):**
- Térreo computável: **T = 228,72 − (n − 1) · a**
- Computável total: **C = 457,44 − (n − 1) · a** (superior de 228,72 + térreo T)
- Garagem coberta: **G = n · a**
- Construída total: **A = C + G + V = 457,44 − (n − 1)·a + n·a + V = 457,44 + a + V**. A construída **não depende de n**: cada vaga a mais troca área útil por área de garagem, m² por m².
- Com edícula mantida de área E (§4.1): T = 228,72 − (n − 1)·a − E, e C = 457,44 − (n − 1)·a − E.

**2.4.4 Contas H0 (base 228,72 por nível; 457,44 de teto computável):**

| n (vagas cobertas) | Origem | a (m²) | (n − 1)·a | Térreo T | Computável C | Garagem G = n·a | Construída A = 457,44 + a + V |
|---|---|---|---|---|---|---|---|
| 1 | mínimo | 12,50 | 0,00 | 228,72 | 457,44 | 12,50 | 469,94 + V |
| 1 | mínimo | 15,00 | 0,00 | 228,72 | 457,44 | 15,00 | 472,44 + V |
| 4 | reunião (caso §4) | 12,50 | 37,50 | 191,22 | 419,94 | 50,00 | 469,94 + V |
| 4 | reunião (caso §4) | 15,00 | 45,00 | 183,72 | 412,44 | 60,00 | 472,44 + V |
| 6 | WhatsApp (5.10) | 12,50 | 62,50 | 166,22 | 394,94 | 75,00 | 469,94 + V |
| 6 | WhatsApp (5.10) | 15,00 | 75,00 | 153,72 | 382,44 | 90,00 | 472,44 + V |

Conferência: 228,72 − 37,50 = 191,22; 457,44 − 37,50 = 419,94; 419,94 + 50,00 = 469,94. 228,72 − 75,00 = 153,72; 457,44 − 75,00 = 382,44; 382,44 + 90,00 = 472,44.

**2.4.5 Contas H1 (base 148,64 por nível; 297,28 de teto computável).** Em H1, quem limita é o **envelope**, não a TO (§2.3). Uma vaga coberta dentro do envelope ocupa envelope mesmo estando fora da TO. **Por isso, em H1, todas as n vagas consomem o térreo: T₁ = 148,64 − n·a e C₁ = 297,28 − n·a.** A forma (n − 1)·a, pedida na instrução como base 297,28/148,64, só vale se a 1ª vaga ficar **fora do envelope**, o que só a alternativa B permite (abrigo no afastamento lateral, sujeito ao condomínio). Mostro as duas:

| n | a | 1ª vaga dentro do envelope: T₁ = 148,64 − n·a | C₁ = 297,28 − n·a | 1ª vaga fora do envelope (só alt. B): T₁ = 148,64 − (n−1)·a | C₁ = 297,28 − (n−1)·a |
|---|---|---|---|---|---|
| 1 | 12,50 | 136,14 | 284,78 | 148,64 | 297,28 |
| 1 | 15,00 | 133,64 | 282,28 | 148,64 | 297,28 |
| 4 | 12,50 | 98,64 | 247,28 | 111,14 | 259,78 |
| 4 | 15,00 | 88,64 | 237,28 | 103,64 | 252,28 |
| 6 | 12,50 | 73,64 | 222,28 | 86,14 | 234,78 |
| 6 | 15,00 | 58,64 | 207,28 | 73,64 | 222,28 |

Em H1, a construída máxima dentro do envelope é **297,28 m²**, qualquer que seja n, porque garagem e varandas cobertas também têm de caber nos 148,64 m² por nível (§2.5).

**2.4.6 Teste do programa (sem redimensionar).** O programa de cerca de 520 m² construídos (caso §4) foi testado pela Viabilidade como **457,44 computáveis + 42,56 a 62,56 m² não computáveis (varandas + garagem coberta)** = 500 a 520 m² (Mascaró v8 §1; Villaça v9 §2) **(b)**.

(i) **Área útil.** Com n vagas cobertas, a área computável cai (n − 1)·a abaixo dos 457,44 que a Viabilidade supôs:
- **4 vagas:** −37,50 m² (a = 12,50) a −45,00 m² (a = 15,00) → C = 419,94 a 412,44 m²;
- **6 vagas:** −62,50 m² (a = 12,50) a −75,00 m² (a = 15,00) → C = 394,94 a 382,44 m².
Essa queda sai **inteira do térreo**, que é onde ficam a suíte acessível de D. Lourdes, o social e o serviço (caso §4): térreo de 191,22–183,72 m² com 4 vagas e de 166,22–153,72 m² com 6 vagas, contra 228,72 com 1.

(ii) **Área construída.** Para chegar a 520 m², é preciso **V ≥ 520 − 457,44 − a = 62,56 − a**: **V ≥ 50,06 m²** (a = 12,50) ou **V ≥ 47,56 m²** (a = 15,00), **qualquer que seja n**. Para o piso da Viabilidade (500 m²): V ≥ 42,56 − a = 30,06 ou 27,56 m².

(iii) **Onde V pode ficar.** Pela premissa da §2.5, as varandas só ficam dentro do envelope (x 2,50–11,79; y 6,00–35,00), ou seja, na **folga de 40,69 m² por nível** fora da projeção computável. No térreo, essa folga também tem de abrigar a 1ª vaga coberta, se ela ficar dentro do envelope e fora da projeção.
- Capacidade de V em H0 = (40,69 − a) no térreo + 40,69 no superior = **81,38 − a**: **68,88 m²** (a = 12,50) ou **66,38 m²** (a = 15,00). Se a 1ª vaga ficar fora do envelope (alternativa B), a capacidade sobe para 81,38 m².
- **Confronto:** necessário 50,06 / 47,56 contra capacidade de 68,88 / 66,38 → **sobram 18,82 m²** nos dois casos (81,38 − 62,56). Construída máxima: 457,44 + a + (81,38 − a) = **538,82 m²**.
- **Mas essa capacidade só existe se as varandas e a 1ª vaga ficarem fora da projeção que o condomínio mede.** Isso depende do que está em aberto:

| Regime de medição da TO (quem confirma) | 1ª vaga coberta | Varandas (balanço ou reentrante) | Construída máxima H0 | O programa de 520 m² |
|---|---|---|---|---|
| **M-a:** o condomínio mede como a Prefeitura, e o Kelsen confirma o enquadramento (LC 270 Art. 350 I e III; COES Art. 8º §4º) | fora da TO | fora da TO, dentro do envelope | 457,44 + a + V ≤ **538,82** | **Cabe geometricamente** (V necessário de 50,06/47,56 contra capacidade de 68,88/66,38) |
| **M-c:** o condomínio aceita a 1ª vaga fora, mas conta as varandas cobertas como projeção | fora da TO | dentro dos 228,72 | 457,44 + a = **469,94 / 472,44** | **Não cabe:** faltam 50,06 / 47,56 m² |
| **M-b:** o condomínio conta como projeção **tudo o que é coberto** (**premissa conservadora vigente**, parecer §5.2) | dentro dos 228,72 | dentro dos 228,72 | **457,44** (computável = 457,44 − n·a − V) | **Não cabe:** faltam 62,56 m² |

- **Dependem de Kelsen + condomínio:** (1) se a varanda reentrante e a varanda em balanço ficam fora da TO para o condomínio (o parecer §2.2, "Leitura", só as exclui "desde que o condomínio meça a TO do mesmo jeito, o que o Regramento não diz"); (2) como o condomínio mede a TO, inclusive para a 1ª vaga coberta (parecer §5.3 item 6). **Não decido.** Hoje vale o M-b, por premissa da Etapa 01.
- **Achado para Lúcio, que sobe a Villaça:** em H1, a folga de envelope é zero (§2.3). Com varandas dentro do envelope (§2.5), a construída máxima é **297,28 m²**. A área de trabalho S3/H1 da Viabilidade (339,84 a 359,84 m², isto é, 297,28 + 42,56 a 62,56; Mascaró v8 §1) **não tem espaço físico sob as premissas desta etapa**, salvo abrigos no afastamento lateral pela alternativa B, se o condomínio admitir. Não corrijo número da Viabilidade: sinalizo.

**2.4.7 Alternativas para a garagem (cada uma com conta e efeito). Quem escolhe é o cliente, no Briefing.**

**(A) 1 vaga coberta + (n − 1) vagas descobertas no afastamento frontal** (LC 270 Art. 363 §2º XII; parecer P6) **(b)**.
- Térreo computável = 228,72 (nenhuma vaga além da 1ª consome projeção). Útil preservada.
- Consumo do frontal (85,74 m² = 14,29 × 6,00):

| n − 1 descobertas | a | Consumo (n−1)·a | % do frontal | Sobra do frontal para árvores, raízes, acesso, pedestres e jardim |
|---|---|---|---|---|
| 3 (n = 4) | 12,50 | 37,50 | 43,7% | 48,24 |
| 3 (n = 4) | 15,00 | 45,00 | 52,5% | 40,74 |
| 5 (n = 6) | 12,50 | 62,50 | 72,9% | 23,24 |
| 5 (n = 6) | 15,00 | 75,00 | 87,5% | 10,74 |

- **Conflitos:** (1) as 3 árvores ficam no frontal, com locação desconhecida (T11): a viabilidade de A depende de as copas e raízes deixarem livres (n − 1)·a + acesso; (2) o acesso de veículos e o de pedestres também saem desse frontal (§1); (3) o frontal é a área preferencial para a superfície drenante, porque tem vegetação (LC 270 Art. 353 I, parecer P6).
- **Permeabilidade H0** (folga de 159,24 m² fora do envelope, §3.2): depois das vagas, sobram 159,24 − 37,50 = 121,74 e 159,24 − 45,00 = 114,24 (n = 4); 159,24 − 62,50 = 96,74 e 159,24 − 75,00 = 84,24 (n = 6), antes de descontar acesso, piscina e deck. **Cabe**, desde que as alternativas permeáveis A/B da §3.2 (laterais e fundos inteiros) não sejam tocadas.
- **Permeabilidade H1, se a APP não contar como permeável** (folga de 22,79 m², §3.3): **não cabe com n = 4 nem com n = 6** (37,50 a 75,00 > 22,79). Cabe no máximo **1 vaga descoberta** (12,50 ou 15,00 ≤ 22,79; duas dariam 25,00 ou 30,00 > 22,79), e sobram 10,29 ou 7,79 m² para todo o acesso. Se o acesso atravessar os 6,00 m do frontal, a largura máxima fica em 10,29 / 6,00 = **1,71 m** ou 7,79 / 6,00 = **1,29 m**. Se piso drenante nas vagas conta como permeável é decisão do **Kelsen** (§3.2) **(c)**.

**(B) Abrigo de carro aberto, coberto por telha-vã, no afastamento lateral do térreo, pelo Dec. 3.046 XI** (Skill `decreto3046-...` §6, M3; Skill `varandas-...` §4.1) **(b)/(c)**.
- **Municipal:** com frontal menor que 10,00 m (aqui 6,00 m), o XI permite ocupar os afastamentos laterais do térreo com abrigos de veículos abertos e cobertos por telha-vã, fora da ATE e da TO.
- **Condomínio:** o Art. 6º (2,50 m de afastamento lateral, 5.4) prevalece como o mais restritivo (parecer, regra de comparação). **Só vale se o condomínio admitir** abrigo no afastamento lateral. Além disso, a tensão XXIII × XI está aberta (Kelsen R4). **Donos: condomínio + Kelsen.**
- **Efeito se admitido:** as vagas no abrigo não consomem a projeção, e o térreo computável volta a 228,72. Uma faixa lateral tem 2,50 × 29,00 = 72,50 m². Com a = 15,00, as 5 vagas de n = 6 (75,00 m²) **não cabem numa só lateral**. Se 2,50 m de largura comporta uma vaga depende da dimensão mínima de vaga, que não foi lida **(c: Hely)**.
- **Efeito na permeabilidade:** as alternativas permeáveis da §3.2 usam faixas laterais **inteiras** (A: fundos + lateral esquerda = 143,95, folga de 1,00; B: duas laterais = 145,00, folga de 2,05). Um abrigo de k vagas numa lateral tira k·a dessa faixa. **Saída:** abrigo na **lateral direita** + permeável A (fundos + lateral esquerda, intacta = 143,95), **só se a piscina não estiver nos fundos**. Se a piscina estiver nos fundos (permeável B), o abrigo quebra a B, e o déficit é k·a − 2,05: com k = 3, 35,45 (a = 12,50) ou 42,95 (a = 15,00); com k = 5, 60,45 ou 72,95. Esse déficit teria de sair do frontal, com as árvores, ou da sobra do envelope, já disputada pelas varandas.

**(C) O cliente reduz as vagas cobertas ou aceita área útil menor.** Pela §2.4.4, cada vaga coberta além da 1ª custa a m² (12,50 a 15,00) de térreo útil. Decisão do **cliente no Briefing** (Etapa 04), informada por estas contas. Não redimensiono.

**2.4.8 [v2] Resposta à pergunta do enunciado "Árvores: pode preservar garagem + árvores?"** **Sim, com condição.**
- Com a garagem coberta dentro do envelope (n vagas, custo de (n − 1)·a de térreo útil) ou com a alternativa B: as árvores **não disputam** área com a garagem, porque ficam no frontal, fora do envelope. Só o **acesso** passa pelo frontal, e a posição dele depende da locação das árvores e da testada (T7, T11).
- Com a alternativa A (vagas descobertas no frontal): **só se a locação (T11) deixar livres (n − 1)·a + o acesso**: 37,50 a 45,00 m² com 4 vagas e 62,50 a 75,00 m² com 6, de um frontal de 85,74 m². Parecer de Oscar: com 6 vagas, preservar as 3 árvores no frontal é improvável, mas quem decide é a locação, que não existe.
- O pedido de remover as árvores "pra fazer a rampa da garagem" (5.10) perdeu o motivo: sem subsolo, não há rampa para descer (parecer P6).

### 2.5 [v2] Varanda e balanço frontal: premissa operacional e efeito no envelope (Correção 2)

**Premissa operacional, válida até decisão do Kelsen** **(b)/(c)**:
1. **Nenhum balanço de varanda na faixa y 0–6,00 (afastamento frontal).** Fonte: Skill `varandas-...` §4.1, "Até decidir: não projetar varanda de casa em balanço sobre o afastamento frontal mínimo na ZPP"; ERRATA 4.1 do Kelsen (o VII remete ao XI na casa unifamiliar, e o ponto está em aberto); Kelsen R4; parecer linha 16 e §5.2 ("NÃO pode assumir varanda balanceada sobre o recuo frontal").
2. **Única saliência admitida sobre o frontal:** a do Dec. 3.046 XIV, de **até 0,40 m, acima do térreo, só para jardineira e ar-condicionado**, fora da ATE e da TO (Skill `decreto3046-...` §6, complemento do M3; Skill `varandas-...` §4.1).
3. **Varandas a ≥ 2,50 m das divisas laterais e de fundos** (COES Art. 8º §2º; parecer linha 16 e §5.2). Contra os fundos, prevalece o afastamento de 5,00 m do condomínio (5.4 Art. 6º). **Se o condomínio admite balanço de varanda dentro do afastamento de fundos de 5,00 m, o Regramento não diz (c: condomínio).** Por conservadorismo, não admito.

**Efeito no envelope (coordenadas do referencial da Peça 1 §1):**
- **Face frontal de qualquer pavimento em y ≥ 6,00.** Só a jardineira e a condensadora podem chegar a **y = 5,60**, e só acima do térreo.
- **Varandas confinadas a x 2,50–11,79 e, conservadoramente, a y 6,00–35,00**, isto é, ao próprio envelope H0 (269,41 m² por nível). Em H1, a y 6,00–22,00 (148,64 m² por nível).
- **Consequência:** as varandas não computáveis **disputam a folga de 40,69 m² por nível** com a 1ª vaga coberta (§2.4.6 iii). Em H1, a folga é zero, e toda varanda sai da área computável.
- **Se o Kelsen decidir que o XI afasta o VII** para a casa unifamiliar, volta a valer, municipalmente, o COES Art. 8º §1º: varanda sobre o afastamento frontal até **1,00 m da testada** (y ≥ 1,00), em toda a largura da fachada. Ganho potencial, por pavimento superior: 9,29 × (6,00 − 1,00) = **46,45 m²** de faixa para varanda. **O condomínio continua sendo pergunta própria:** o Art. 6º fixa o afastamento frontal de 6,00 m e não diz se varanda em balanço pode avançar sobre ele. Pela regra de comparação (parecer), vale o mais restritivo. Sem resposta escrita do condomínio, a faixa y 0–6,00 continua fechada **(c: condomínio)**.

### 2.6 [v2] Cabe o programa de 520 m²? (substitui o "cabe em H0" da v1)

**Em H0, o programa de cerca de 520 m² construídos cabe somente se as três condições abaixo forem atendidas ao mesmo tempo:**
1. **Medição da TO pelo condomínio:** o condomínio confirma por escrito que mede a TO como a Prefeitura, excluindo 1 vaga coberta e as varandas, em balanço ou reentrantes (regime M-a da §2.4.6), e o Kelsen confirma o enquadramento. **Sob a premissa vigente (M-b, parecer §5.2), não cabe: a construída máxima é 457,44 m² e faltam 62,56 m².**
2. **Varandas não computáveis confirmadas:** V ≥ 62,56 − a, isto é, **≥ 50,06 m²** (a = 12,50) ou **≥ 47,56 m²** (a = 15,00), dentro do envelope e sem balanço frontal (§2.5). A capacidade geométrica é de 68,88 a 66,38 m² (folga de 18,82 m²).
3. **Número de vagas cobertas (n) aceito com o custo em área útil:** a construída não muda com n, mas a **área computável útil cai (n − 1)·a**: com 4 vagas, para 419,94–412,44 m²; com 6 vagas, para 394,94–382,44 m². O térreo útil cai para 191,22–183,72 ou 166,22–153,72 m². A alternativa: vagas descobertas no frontal (A, com as árvores e a permeabilidade como condição) ou abrigo lateral (B, com o condomínio como condição).

Mais duas condições comuns: o envelope tem de ser confirmado no polígono real (T5), e a edícula não pode ser mantida dentro da projeção (cada m² dela sai do térreo, §4.1).

**Em H1, não cabe:** a construída máxima dentro do envelope é 297,28 m² (faltam 520,00 − 297,28 = **222,72 m²**). Mesmo contando só a área computável, faltam 160,16 m² (Mascaró v8 §1; Villaça v9 §8.3). Redefinir o programa em H1 é decisão do cliente no Briefing, com Lúcio. Eu não a faço.

---

## 3. Faixas fora do envelope e área permeável

### 3.1 Faixas (H0, aproximação 14,29 × 40,00)

| Faixa | Coordenadas | Conta | Área |
|---|---|---|---|
| Afastamento frontal | x 0–14,29; y 0–6,00 | 14,29 × 6,00 | **85,74 m²** |
| Lateral esquerda | x 0–2,50; y 6,00–35,00 | 2,50 × 29,00 | **72,50 m²** |
| Lateral direita | x 11,79–14,29; y 6,00–35,00 | 2,50 × 29,00 | **72,50 m²** |
| Afastamento de fundos | x 0–14,29; y 35,00–40,00 | 14,29 × 5,00 | **71,45 m²** |
| **Soma fora do envelope** | | | **302,19 m²** |
| Envelope | | 9,29 × 29,00 | 269,41 m² |
| **Total da aproximação** | | 14,29 × 40,00 | **571,60 m²** |

**Fechamento:** 571,60 contra os 571,80 do levantamento dá diferença de **−0,20 m² (0,035%)**. A diferença vem de usar a menor largura (14,29) e a menor lateral (40,00), e é desprezível para as conclusões. Área livre com a projeção máxima: 571,80 − 228,72 = **343,08 m²** (parecer §2.2) **(b)**.

### 3.2 Locação CONCEITUAL dos 142,95 m² permeáveis (H0)

Regras do Legal (parecer §5.2; LC 270 Art. 353 III) **(b)**: porções de **no mínimo 4 m² e 2,00 m de lado**, sem subsolo embaixo. O Art. 353 I recomenda a superfície drenante preferencialmente onde há vegetação (parecer P6) **(b)**.

| Faixa | Aptidão (só regra, sem desenho) |
|---|---|
| Frontal (85,74 m²) | É a área **preferencial** (Art. 353 I), porque tem as árvores. Concorre com a entrada de carros, o caminho de pedestres e, se houver, vagas descobertas (Art. 363 §2º XII; alternativa A da §2.4.7) |
| Laterais (2 × 72,50 m²) | A largura de 2,50 m é maior que os 2,00 m mínimos, então as porções são aptas. Concorrem com circulação de serviço e, se o condomínio admitir, com abrigos do XI (alternativa B) |
| Fundos (71,45 m²) | Aptos. Concorrem com piscina e deck (§4.2) |
| Sobra do envelope (40,69 m² por nível) | **[v2]** Disputada pelas varandas e pela 1ª vaga (§2.4, §2.5). Só conta como permeável a parte descoberta sobre solo natural com 4 m² e 2 m de lado |

**Folga declarada (H0):** fora do envelope há 302,19 m² e o mínimo é 142,95 m². Portanto **até 302,19 − 142,95 = 159,24 m²** fora do envelope podem ser impermeáveis (acessos, caminhos, piscina, deck, vagas descobertas), desde que os 142,95 m² fiquem em porções válidas. **Em H0, a permeabilidade não é condicionante crítica, desde que se respeite a locação abaixo.**

**Locação conceitual dos 142,95 m² (H0): zoneamento, não desenho** *(acrescentado por Lúcio na auditoria da v1, 06/10; mantido)*. Duas alternativas, porque a posição da piscina não consta (T10):

| Alternativa | Faixas permeáveis (inteiras, jardim sobre solo natural) | Conta | Total | Folga sobre 142,95 |
|---|---|---|---|---|
| **A**: piscina fora dos fundos (ou demolida) | fundos + lateral esquerda | 71,45 + 72,50 | **143,95 m²** | +1,00 m² |
| **B**: piscina nos fundos | lateral esquerda + lateral direita | 72,50 + 72,50 | **145,00 m²** | +2,05 m² |

- As duas fecham o mínimo **só com faixas inteiras** e folga pequena (1,00 e 2,05 m²). Por isso, **em qualquer alternativa, o frontal precisa manter jardim em torno das 3 árvores** como reserva (Art. 353 I), com área a definir no EP, depois da locação (T11).
- Cada faixa lateral tem 2,50 m de largura. Se uma parte dela for pavimentada no sentido do comprimento, a parte permeável restante só conta se mantiver **≥ 2,00 m de lado** (Art. 353 III): no máximo **0,50 m** pavimentado ao longo da faixa. Uma circulação de serviço de 1,20 m numa lateral **desqualifica a faixa inteira** (2,50 − 1,20 = 1,30 m < 2,00 m), e o que ela perder tem de sair do frontal ou da sobra do envelope.
- **[v2]** Um abrigo do XI numa lateral (alternativa B da garagem) tira k·a da faixa. Só é compatível com a alternativa permeável A se ficar na lateral direita (§2.4.7).
- Todas as porções ficam sem subsolo embaixo (parecer §5.2). Jardim de chuva **não** entra nesta conta até a análise da §3.4. Em H1, ver a §3.3: a alternativa A deixa de existir, porque os fundos ficam dentro da faixa H1.

**Efeito do acesso de veículos no frontal:** consome (largura do acesso) × 6,00 m². Mesmo que o frontal inteiro (85,74 m²) ficasse impermeável, ainda sobrariam 159,24 − 85,74 = 73,50 m² de folga. Não fixo a largura do acesso: é EP.

**Efeito da piscina nos fundos:** a piscina **não é área permeável**. A área dela (não consta) sai dos 71,45 m², e as sobras dos fundos só contam se tiverem 2,00 m de lado. Exemplo de regra: se a piscina deixar uma faixa de 1,50 m até a divisa, essa faixa **não conta**.

**Padrão de superfície.** Jardim e gramado sobre solo natural atendem à regra sem dúvida aparente. Se **brita, piso drenante ou grelha de concreto com grama** contam como superfície drenante para a SMDU e para o condomínio, eu não decido **(c: Kelsen)**. Até lá, conto como permeável só o jardim sobre solo natural.

### 3.3 O que muda em H1

| Zona | Conta | Área |
|---|---|---|
| Faixa H1 (y 22,00–40,00) | 14,29 × 18,00 | **257,22 m²** |
| Frontal | 14,29 × 6,00 | 85,74 m² |
| Laterais até y 22,00 | 2 × 2,50 × 16,00 | 80,00 m² |
| Envelope H1 | 9,29 × 16,00 | 148,64 m² |
| Soma | | 571,60 m² |

- **Se a APP vegetada contar como permeável:** só a faixa H1 (257,22 m²) já supera os 142,95 m².
- **Se não contar:** fora do envelope, até y 22,00, sobram 85,74 + 80,00 = **165,74 m²**. A folga é de 165,74 − 142,95 = **22,79 m²** para **todos** os acessos e caminhos, com o envelope H1 inteiramente ocupado. Um acesso de veículos que atravesse o frontal consome largura × 6,00 m², e com **largura ≥ 22,79 / 6,00 = 3,80 m a folga acaba**. **[v2]** Com uma vaga descoberta no frontal, o limite cai para 1,71 ou 1,29 m (§2.4.7 A). A partir daí, a projeção teria de ficar abaixo do envelope H1 para abrir área permeável. **É risco real de desenho em H1.**
- **Quem decide se APP vegetada conta como permeável: Kelsen**, à luz da resposta da SMAC. **Não decido.**
- Piscina ou deck na faixa H1: **não pode ser presumido**. Seria intervenção em área de proteção (LC 281 Art. 22 III, no parecer P2; parecer §5.2) **(c: Kelsen/SMAC)**.

### 3.4 Jardim de chuva com NA a 0,90 m

- A Skill `paisagismo-jardim-de-chuva` apresenta a técnica como solução de infiltração ("recarrega o lençol"; "até 30% do escoamento") e declara que **não há NBR específica** (seção "Limitações honestas") **(b)**. **A Skill não diz nada sobre a separação entre o fundo do jardim e o lençol freático.** Registro a lacuna para Cardozo (seção "Escopo, crescimento e manutenção" da própria Skill).
- A Skill de fundações §5 (parceria com Glaziou) manda verificar se o lençol já não está saturado na cota de infiltração **(b)**. O NA da sondagem é de **0,90 m** (5.7) **(a)**. O NA máximo provável (chuva forte, lago cheio) **não é conhecido** (Skill `rebaixamento-...` §6) **(c)**.
- **Parecer:** **não recomendo** jardim de chuva como solução de infiltração neste lote sem análise de Glaziou e Saturnino sobre a folga entre o fundo e o NA máximo. Pode virar acúmulo de água. Se o jardim de chuva conta como superfície drenante para fins legais, quem decide é o Kelsen **(c)**.

---

## 4. Conflitos percebidos

### 4.1 Edícula: pedido do cliente, parecer de Oscar e conflito Legal × cliente (Correção 3)

**[v2] O pedido, literal:**
- Caso §4 (reunião de 25/09/2026): "Querem **manter a edícula e a piscina existentes** ('já estão prontas, economiza')." **(a)**
- Pergunta 2 do cliente na Etapa 01 (enunciado da Etapa 01, §2): "Queremos manter a edícula e a piscina. O arquiteto anterior disse que têm direito adquirido." Resposta aprovada: **não há direito adquirido**, porque a edícula não consta da planta do Habite-se (5.8), e o "Art. 38 da LC 274" está revogado (parecer P2) **(b)**.

**Afastamentos:**

| Regra | Exigido | Existente (5.2) | Falta |
|---|---|---|---|
| Condomínio, 5.4 Art. 6º (prevalece) | 2,50 m | 0,80 m | **1,70 m** |
| COES, unifamiliar (parecer, linha 12; Art. 31 p.ú.) | 1,50 m | 0,80 m | **0,70 m** |
| Código Civil Art. 1.301 (janela) | 1,50 m | 0,80 m, **com janela** | 0,70 m (risco civil: Kelsen R5) |
| Vão de iluminação ou ventilação | Uma faixa de 0,80 m não é afastamento nem prisma (parecer P2). Um PV, só para ventilação, já exige lado de **no mínimo 1,00 m**, e um PVI, **no mínimo 3,00 m** (Skill `coe-lc198-...` §2) | 0,80 m | não atende nem como PV |

**[v2] Resposta ao argumento "já está pronta, economiza", ponto a ponto:**
1. **Para ficar, ela deixa de estar "pronta".** A face a 0,80 m da divisa teria de recuar até 2,50 m: faltam 1,70 m (condomínio, Art. 6º). Isso significa demolir uma faixa de 1,70 m × a profundidade da edícula (que não consta, T9) e refazer a fachada e a janela. Vira obra nova sobre uma construção que nunca foi licenciada (5.8).
2. **O rito fica sem caminho limpo.** Mantida a edícula, o processo vira um híbrido de demolição parcial com construção irregular a legalizar, que o parecer descreve como "sem caminho limpo". O enquadramento é decisão do Kelsen (parecer P2) **(c)**. A legalização é improvável: a LC 281 exige iluminação e ventilação conforme as normas (Art. 22 II) e veda ocupar área de recuo (Art. 22 III); o prazo do Art. 16 §5º (30/06/2026) venceu; a leitura do Art. 40 (redação da LC 301 Art. 58, até 01/12/2026) está em tensão aberta (parecer P2; Kelsen R4) **(b)/(c)**. Mesmo legalizada na Prefeitura, continuaria violando o Art. 6º do condomínio se não recuar (parecer P2).
3. **Cada m² mantido sai do térreo computável.** Na ZPP, a edícula computa na TO e na ATE (Dec. 3.046 XV; adotado por conservadorismo, parecer linha 17) **(b)**. Fórmula: **térreo computável = 228,72 − (n − 1)·a − E**, onde E é a área da edícula mantida. Exemplo com 4 vagas e a = 12,50: 191,22 − E. O térreo já é disputado pela garagem (§2.4) e pela suíte acessível (§8).
4. **Refazer a janela reabre o risco civil.** A janela existente desde 1998 provavelmente já passou do prazo de ano e dia do CC Art. 1.302. Ampliar ou refazer reabre o risco (parecer P2; Kelsen R5) **(b)/(c: advogado)**.
5. **Pesa no prazo do crédito.** O crédito está condicionado à licença emitida até 30/06/2027 (caso §2; 5.14) **(a)**. Um rito híbrido acrescenta enquadramento e exigências ao caminho crítico (parecer §4.2). A licença pela via do LICIN Art. 4º §2º vale 3 meses e precisa ser revalidada (Kelsen R3) **(b)**.
6. **A economia não é quantificável em R$ com o dossiê:** a área da edícula não consta (T9), a demolição dela está [NC] no Mascaró v8 §6.4, e o custo de recuar e refazer a fachada não foi orçado **(c)**.

**Conclusão:** **a economia alegada não se sustenta dentro das premissas.** Manter "como está" é **inviável pelo condomínio, independentemente da Prefeitura**. Manter em parte custa demolição parcial, fachada nova, rito híbrido e área de térreo.

**Conflito explícito, para o Briefing (Etapa 04):**

| Parte | Posição | Fonte |
|---|---|---|
| Cliente | Quer manter a edícula ("já estão prontas, economiza") | caso §4; Etapa 01, pergunta 2 |
| Legal | Recomenda prever a demolição; não há direito adquirido | parecer P2 e §5.2 |
| Arquitetura (Oscar) | Manter "como está" é inviável pelo condomínio (falta 1,70 m), independentemente da Prefeitura. **Parecer: demolição total.** Se a família quiser as funções (churrasqueira, depósito), elas entram no projeto novo, dentro do envelope e contando na projeção. O programa já prevê "cozinha + área gourmet" (caso §4) | 5.4 Art. 6º; esta seção |
| **Quem decide** | **O cliente, informado por esta tabela.** Se insistir em manter, total ou parcialmente: o **Kelsen** define o rito, e a **Comissão de Obras do condomínio** aprova antes do protocolo (5.4 Art. 9º) | parecer §5.2; 5.4 Art. 9º |

- **Posição da edícula:** com a face em x ≈ 13,49, ela está na faixa lateral direita (x 11,79–14,29). Se a profundidade dela (em x) passar de 1,70 m, uma parte fica dentro do envelope. A posição em y não consta: se estiver em y > 35,00, cai no afastamento de fundos; se estiver em y > 22,00, cai na faixa H1 **(c: T9)**.

### 4.2 Piscina: pedido do cliente, parecer de Oscar e risco de alagamento

**[v2] O pedido:** o mesmo da edícula, "já estão prontas, economiza" (caso §4), e a pergunta 2 da Etapa 01. A resposta aprovada: piscina descoberta não depende de licença própria e pode ser mantida **se** couber no projeto novo (parecer P2; LC 270 Art. 278 §1º II) **(b)**.

- **Posição, dimensões, profundidade e cota: não constam no dossiê.** O "~4 × 8 m nos fundos" do enunciado é estimativa não documental **(c: T10)**.
- **Quem fixa o limite de 1,60 m:** o **Regramento do condomínio**, Art. 8º (5.4), que é norma privada e não lei. Pela lei municipal, piscina descoberta **não depende de licença** (LC 270 Art. 278 §1º II, no parecer P2) **(a)+(b)**. O enunciado diz "a Lei permite até 1,60 m", o que não confere.

**[v2] Resposta à pergunta do enunciado "Risco de alagamento?":**
- **Água do lençol contra a piscina: SIM, há risco.** Com o NA a 0,90 m (5.7) e fundo de até 1,60 m, se as duas medidas partirem da mesma superfície, o fundo fica até **1,60 − 0,90 = 0,70 m abaixo do NA**. Consequências, pelas Skills **(b)**: **subpressão e flutuação** com a piscina vazia (na manutenção), verificadas com o NA máximo (Skill `rebaixamento-...` §6 e §4.3); **infiltração** se a estanqueidade falhar sob pressão de água externa (Skill `rebaixamento-...` §4.3, remetendo à NBR 9575). A amarração entre a borda, o terreno atual e a soleira de +3,20 **não consta**, e um aterro muda a conta **(c: T4, T10)**.
- **Água na escavação e na obra: SIM, há risco.** Escavar abaixo do NA é extração de água subterrânea. Acima de 5.000 L/dia, cai fora do uso insignificante, e a outorga ou certidão do INEA tem de sair **antes** da escavação (Skill `rebaixamento-...` §2; R1 da Skill ainda aberta) **(c: Hely via Kelsen)**. Bombear em argila mole (2,5 a 9,0 m, conforme 5.7) traz **risco de recalque em vizinho** (Skill `rebaixamento-...` §1 e §3). O mesmo vale para blocos e baldrames, que já podem passar o NA mesmo dentro do limite de 1,20 m do Art. 8º (Mascaró v8 §6.1) **(c: Baumgart/Cardozo)**.
- **Alagamento superficial do lote e da piscina pelo lago: NÃO DETERMINÁVEL com o dossiê.** Não há cota do terreno (T4), cota máxima do lago nem regime de marés (T19), nem marcação de áreas alagáveis (T22). O relato de oscilação duas vezes por dia e da manilha ligada ao canal (5.9) **agrava** o risco. O NA máximo provável não é conhecido (Skill `rebaixamento-...` §6) **(c)**.

**[v2] Resposta ao argumento "economiza":** a piscina só pode ser mantida, e a economia só existe, **se** ela, depois de levantada:
- (i) estiver fora da faixa H1, ou H0 for confirmado **(c: Kelsen/SMAC)**;
- (ii) tiver profundidade ≤ 1,60 m (5.4 Art. 8º);
- (iii) estiver em estado estrutural e de estanqueidade compatível com NA de 0,90 m, inclusive contra flutuação, com laudo de Baumgart/Cardozo;
- (iv) não ocupar área necessária ao envelope ou à permeabilidade (§3.2: com a piscina nos fundos, só a alternativa B, com as duas laterais inteiras e folga de 2,05 m², fecha o mínimo).

**O que pode acabar com a economia:** profundidade > 1,60 m (teria de ser reduzida, ou seja, obra); laudo desfavorável (refazer impermeabilização ou estrutura); posição em H1 ou no afastamento de fundos sem admissão do condomínio (5.4 é silente; **c: condomínio/Kelsen**); aterro do lote (T4) que deixe a borda abaixo do novo nível do terreno; conflito com a permeabilidade, que obrigaria a abrir mão das laterais para circulação ou abrigo. **Em R$, não é quantificável:** dimensões e estado não constam (T10), e a demolição da piscina e a piscina nova estão [NC] no Mascaró v8 §6.4.

- **Não é área permeável** (§3.2).
- **Parecer:** **não dá para dizer hoje se a piscina pode ser mantida.** Até o levantamento (T10) e o laudo, o EP **não usa a piscina existente como premissa**. **Decide o cliente, com o laudo.** Se estiver em H1: Kelsen/SMAC. Se estiver no afastamento de fundos: condomínio.

### 4.3 Árvores: parecer de Oscar

- Ficam no afastamento frontal (caso §3) **(a)**. **Locação, DAP e estado não constam** (Peça 1 §5) **(c: T11 + laudo de profissional habilitado)**.
- **O motivo do pedido de remoção caiu.** A cliente quer tirar as árvores "pra fazer a rampa da garagem" (5.10), mas sem subsolo não há rampa para descer (parecer P6) **(b)**. O afastamento frontal admite estacionamento descoberto de unifamiliar e rampa de até 10% e 0,50 m (LC 270 Art. 363 §2º, no parecer P6) **(b)**.
- **Remoção** exige licença municipal (LC 270 Art. 278 XIV) **e** autorização do condomínio (5.4 Art. 12) (parecer, linha 23) **(a)+(b)**. Quando vinculada a obra, o pedido segue pela SMAC/SISARV junto com o licenciamento (Skill `remocao-...` §3), com compensação (§5). Árvore sadia sem risco documentado raramente sai (Skill `remocao-...` §6), regra prática de fonte secundária (R3 da Skill) **(b)/(c)**. A espécie de cada árvore vem do laudo; se for exótica, o tratamento muda, mas a lista da SMAC não foi levantada (Skill `remocao-...` §6 item 3 e §10) **(c: Glaziou)**.
- **Ganho de espaço com a remoção:** não muda a projeção nem o envelope, porque as árvores estão fora do envelope, no frontal. Só liberaria espaço para o acesso e para vagas descobertas no frontal (alternativa A), e reduziria a vegetação preferencial para a superfície drenante (Art. 353 I).
- **[v2] "Pode preservar garagem + árvores?" Sim, com condição** (detalhe na §2.4.8): com garagem coberta no envelope ou abrigo lateral (B), sim, e o que decide é só a posição do acesso (T7, T11). Com vagas descobertas no frontal (A), só se a locação deixar livres (n − 1)·a + o acesso.
- **Parecer:** **preservar as 3 árvores e posicionar o acesso de veículos conforme a locação a levantar.** Remover uma delas só se, com a locação em mãos, não houver acesso viável, e mesmo assim com laudo, licença e autorização do condomínio. **Decisão do cliente**, sujeita à SMAC e ao condomínio.

### 4.4 APP / FMP / marinha nos fundos

- O levantamento **não resolve** nenhuma das três questões, que exigem demarcação oficial (parecer §2.4). Alerta: **se H1 se confirmar, os últimos 18 m (y 22–40) ficam fora do desenho**, com os efeitos numéricos das §§2.3, 2.4.5, 2.6 e 3.3 **(b)**.
- A contradição entre 5.5 ("sem ligação com o sistema lagunar") e 5.9 (maré, manilha ligando ao canal) **reforça** o risco. O caseiro não prova nada, mas também não pode ser descartado. Se a ligação se confirmar, entra a LC 270 Art. 216 V (Kelsen R2) **(b)/(c)**.
- O levantamento ajuda com medições: área do espelho d'água (T13), régua de maré (T14, T19), posição da manilha (T13) e áreas alagáveis (T22). Ver a Peça 1 §7 e a §9 abaixo.

---

## 5. Permeabilidade: o que o enunciado pede e o que confere

- Mínimo de **142,95 m²** (25% × 571,80) (parecer, linha 14) **(b)**. Locação conceitual na §3.2. Padrão: jardim ou grama sobre solo natural; brita e piso drenante dependem do Kelsen (§3.2).
- O enunciado associa a "LC270 Art. 353 III" a um "valor mínimo de lote por zona". **Não confere.** No parecer aprovado, o Art. 353 III é a regra das **porções de superfície drenante com no mínimo 4 m² e 2 m de lado** (parecer, linha 14 e §5.2). Lote mínimo não é condicionante deste caso: o lote existe e está registrado (5.1).

---

## 6. Cotas e referenciais

| Item | Situação | Quem decide ou fornece |
|---|---|---|
| Cota de soleira | +3,20 m **prevista** (5.2), não "atual" como diz o enunciado; referência do condomínio | Topógrafo (T3); Kelsen/Hely (Art. 458) |
| Ponto mais alto da edificação | ≤ +11,70 m no referencial do condomínio, se a soleira for +3,20 (5.4 Art. 7º) | conta (a)+(b) |
| Cota do terreno atual e aterro até +3,20 | **Não consta**. Sem ela não se sabe o volume de aterro | Topógrafo (T4) |
| Efeito do aterro na fundação | Aterro sobre argila mole gera **atrito negativo** nas estacas (Skill de fundações M4); a pergunta já está registrada no Mascaró v8 §10 | Baumgart/Cardozo (**não dimensiono**) |
| **[v2] Cota do piso térreo da casa nova** | **O que se afirma:** a cota de soleira é a cota de implantação da edificação (glossário do COE, via Skill de levantamento §2, linha III); a referência de projeto é a soleira **prevista** de +3,20 (5.2), no referencial condominial; a altura de 8,50 m é contada a partir da soleira (5.4 Art. 7º), então piso térreo acima da soleira consome altura. **O valor final não é afirmável hoje:** depende do RN do meio-fio (T2), da amarração oficial e do Art. 458 (T3), do terreno natural e do aterro (T4) e da regra numérica de soleira e terreno natural do Hely (Skill de levantamento R2). O desnível rua–soleira também decide a rampa de D. Lourdes (§8) | Dados: topógrafo. Regra: Hely/Kelsen. Fixação: EP (Lúcio/Oscar) |
| Cota da piscina (se mantida) | Não consta | Topógrafo (T10) |
| Regra numérica de soleira contra o meio-fio e de "terreno natural" para gabarito | Não está nas Skills legais (Skill de levantamento R2) | Hely/Kelsen |

---

## 7. Fundações: só o condicionante de levantamento

A sondagem 5.7 dá NA de 0,90 m, argila orgânica mole de 2,5 a 9,0 m e areia compacta abaixo de 11 m **(a)**. O Mascaró v8 §6.1 e o Villaça v9 §6 já apontaram estacas (hélice contínua) e radier inadequado **(b)**. **Não dimensiono nada.** O que o levantamento precisa entregar a Baumgart: a cota do terreno atual e o aterro previsto (atrito negativo, M4); a posição dos 3 furos em relação à projeção futura (NBR 8036, pela Skill de fundações R7: no mínimo 3 furos entre 200 e 400 m² de projeção; reforço local de 1 furo a cada 100–150 m²); a data e a condição da medição do NA (o NA médio anual e o NA máximo podem ser diferentes, conforme a Skill de fundações §6 e a Skill `rebaixamento-...` §6); e os vizinhos, para vistoria cautelar **(c: Baumgart/Cardozo)**.

---

## 8. Acessibilidade de D. Lourdes

- A suíte acessível é **programa, não exigência legal**: o COES dispensa a casa unifamiliar das normas de acessibilidade (Art. 31 V, no parecer §5.2) **(b)**. A Skill `arquitetura-nbr9050-...` ("Brecha válida" item 3 e "Limitações" item 3) aponta a mesma isenção para unifamiliar privada **(b)**.
- **[v2] A suíte acessível fica no térreo** (caso §1 e §4) e disputa o **térreo computável**: T = 228,72 − (n − 1)·a − E. Com 4 vagas cobertas, sobram 191,22 a 183,72 m²; com 6, 166,22 a 153,72 m², para a suíte, o social, a cozinha/gourmet e o serviço com dependência (§2.4.4). A distribuição é do EP, e o programa é da Etapa 04. Aqui só registro o efeito.
- **O desnível entre a rua (meio-fio) e a soleira não é conhecido**, porque faltam o RN do meio-fio e a cota do terreno (T2, T4) **(c)**.
- **Impacto, pela Skill NBR 9050 (tabela de rampas):** obra nova com no máximo 8,33%, até 0,80 m de desnível e 9,60 m por segmento, e patamares de 1,20 m. Recomendável 5%. Largura mínima de 1,20 m **(b)**. Conta de ordem de grandeza: comprimento = desnível / inclinação. Exemplo: 0,50 m a 8,33% → 6,00 m, o afastamento frontal inteiro. Um desnível maior ultrapassa o frontal ou exige mais de um segmento com patamar.
- **Interface com o Legal:** no afastamento frontal, a rampa é admitida até 10% e 0,50 m de altura (Art. 363 §2º, no parecer P6) **(b)**. **Se o desnível rua–soleira passar de 0,50 m**, a parte excedente da rampa acessível teria de ficar fora do frontal, ou seja, dentro do envelope ou das laterais, e, se coberta, consome projeção. **Esse é o efeito de desenho a levar ao Briefing.** O valor do desnível depende de T2/T4. A solução fica no EP.
- Os parâmetros numéricos da Skill vêm de fonte secundária, porque a norma não foi lida (Skill, "Limitações" item 1). Antes do anteprojeto, é preciso conferir no texto da NBR 9050 **(c)**.

---

## 9. Análise de riscos: o que o Legal deixou aberto e onde o levantamento ajuda

| # | Aberto no Legal | O levantamento ajuda? | Impacto no desenho |
|---|---|---|---|
| 1 | APP: área do espelho d'água < 10.000 m²? | **Sim:** medir o espelho (T13). A decisão é da SMAC | H0 ou H1 (§2.3, §2.6) |
| 2 | Marinha: há influência de maré? | **Sim:** régua de maré e regime de marés (T14, T19). A decisão é da SPU | Domínio da União sobre a faixa |
| 3 | FMP (INEA) | Não. Depende da certidão do INEA | Não estimável |
| 4 | Ligação lago–canal (5.5 × 5.9; Art. 216 V) | **Sim:** locar a manilha (T13). A decisão é da SMAC/Kelsen | Reforça H1/H2 |
| 5 | Cota de soleira no referencial oficial (Art. 458) | **Sim:** T3 | Rito (avaliação técnica) e alturas |
| 6 | Divisa com o Lote 16 | **Sim:** linha do PAL e muro (T5). A decisão é do cliente com advogado | 571,80 × 600 |
| 7 | **[v2]** Como o condomínio mede a TO (1ª vaga coberta, varandas em balanço e reentrantes, abrigo do XI) | Não. Pergunta ao condomínio, via cliente | **Decide se o programa de 520 m² cabe em H0** (§2.4.6 iii, §2.6) |
| 8 | Edícula: rito e cômputo | Parcial: área (T9) | Térreo computável (§4.1) |
| 9 | Demolição × obra nova (TRAVA do POP-LEGAL-03 §5) | Não | Cronograma |
| 10 | Brita ou piso drenante como superfície drenante; APP como permeável | Não | Folga permeável (§3); alternativa A da garagem em H1 |
| 11 | **[v2]** Varanda e balanço sobre o frontal: Dec. 3.046 VII × XI (unifamiliar) | Não | Até 46,45 m² por pavimento superior de faixa para varanda, se o Kelsen e o condomínio admitirem (§2.5) |
| 12 | **[v2]** Garagem coberta: Dec. 3.046 XXIII × XI (abrigo lateral) | Não | Alternativa B da garagem (§2.4.7) |
| 13 | **[v2]** Dimensão mínima legal de vaga (não lida) | Não | Valor de "a" em todas as contas da §2.4 |
| 14 | **[v2]** Áreas alagáveis e regime de marés (NBR 6492 5.1) | **Sim:** T19, T22 | Risco de alagamento (§4.2) |

---

## 10. Skills usadas (seções) [v2]

`levantamento-topografico-cadastral-orientado-duli-licin-rj` §2 (linha III), §3, §4, §5, R2; `decreto3046-81-lc270-2024-licin-barra-recreio` §4 e §6 (M1, M2, **M3 e complemento XIV**); **`varandas-nao-computaveis-ate-to-coes-lc198-rj` §2 (Art. 8º §§1º, 2º, 4º) e §4.1 inteira (VII, XI, XIV e "Em aberto")**; **`nbr6492-2021-memoriais-por-etapa-projeto` §2 (LV-ARQ) e §3 (nota LV)**; `coe-lc198-2019-...` §2 (PV ≥ 1,00 m; PVI ≥ 3,00 m); `fundacoes-solos-moles-...` §3.3, §5, §6, R7, M4; `rebaixamento-lencol-freatico-...` §1–§4, §6; `paisagismo-jardim-de-chuva` (Como usar; Limitações honestas; lacuna registrada); `remocao-arvores-smac-fpj-...` §3, §5, §6, §10; `arquitetura-nbr9050-acessibilidade` (tabela de rampas; Brecha válida item 3; Limitações).

**Correção da v1:** a v1 dizia "A `varandas-nao-computaveis-...` **não foi usada**: nesta etapa não se define varanda". **Estava errado.** Esta etapa define o envelope, e o envelope é onde as varandas não computáveis precisam caber (§2.4.6 iii, §2.5). A Skill foi usada na v2. A v1 também dizia "Não usei Skill de NBR 6492 'memoriais por etapa'". A Skill se aplica ao relatório de Levantamento e foi usada (Peça 1 §7.1).

## 11. Declaração [v2]

Ensaio 100% fictício. Nada foi protocolado nem enviado, e nenhum órgão, condomínio ou cliente foi contatado. **Não abri, listei, li ou citei nada em `_gabaritos_LACRADO\`.** Li o `etapa_03_levantamento\parecer_bardi.md` por ordem expressa de Lúcio, para corrigir a v1. Não reinterpretei premissa legal da Etapa 01, não redimensionei o programa e não desenhei. Análise preliminar, sujeita à auditoria de Lúcio.

— Oscar, 06/10/2026 (v2)
