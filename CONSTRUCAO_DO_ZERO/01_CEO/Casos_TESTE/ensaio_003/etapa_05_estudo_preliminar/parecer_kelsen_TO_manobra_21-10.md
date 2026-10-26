# Parecer Kelsen — TO (vaga coberta e marquise) e manobra das vagas descobertas — Ensaio Sombra 003, etapa 05 v3 (21/10/2026)

Ordem de Wallenberg, por Claudemberg, em 21/10/2026. A execução (leitura do primário e do modelo, só leitura) foi do Hely. É **análise preliminar**: não é parecer final e depende do Gate de Claudemberg. Modelo, programa, gabarito lacrado e `_estado_ensaio_003.json` não foram alterados.

Fontes: `Agentes/Hely/Fontes_Legislacao/` — LC 270/2024, COES consolidado SMU, Dec. 3.046/81. Página = página do PDF, lida por `pdftotext -layout` nesta execução. Vigência na Busca Fácil não reconsultada (mesma falha de rede da manhã).
Regramento: `caso_sombra_003.md` §5.4, lido inteiro (Arts. 5º, 6º, 7º, 8º, 9º, 12, 21).
Base: lote 571,60 m² (Gate 20/10). Teto do Regramento 0,40 × 571,60 = **228,64 m²**. TO do RIU fictício (§5.3) 50% → 285,80 m².

## Q1 — vaga coberta e marquise saem da projeção?

**Números (de onde vêm):**
- Projeção bruta do térreo: **245,95** (quadro sem fatores, id 455316, relatório do Oscar 21-10 tarde, l.36).
- Vaga 1 coberta: **14,55** (região TO id 455417, mesmo relatório, l.43).
- Vaga 2 coberta: **14,55** (região CA id 455475, l.44; não há região TO própria da vaga 2. Usei o mesmo valor porque as duas vagas têm 2,6075 × 5,275, l.18-20).
- Marquise: **13,01** (região TO id 455431, l.43; elemento 454246, tipo "MARQUISE BALANCO 15 cm", área 13,01, lido por mim no EP_v3: bbox x 2,50–11,79, y 4,00–6,00, face inferior z 3,30). **Ela avança 2,00 m sobre o afastamento frontal de 6,00 m.**

**Texto primário:**
- LC 270, Art. 350, p.125: "A projeção horizontal das edificações inclui toda a área coberta da edificação, com as seguintes exceções: I - as áreas em balanço destinadas a varandas, sacadas, saliências e marquises nos termos do Código de Obras [...]; III - estacionamento coberto nos termos do Código de Obras [...], nas edificações uni e bifamiliares, limitado a uma vaga."
- LC 270, Art. 347, p.124 (ATE, não TO): "I - portaria, marquises [...]"; "II - locais cobertos e descobertos destinados à vagas de estacionamento [...], inclusive seus acessos e áreas de manobra".
- COES, Art. 9º, p.6: marquises "balanceadas sobre os afastamentos das edificações, dentro dos limites do lote", com "I - [...] altura útil mínima de dois metros e cinquenta centímetros"; "II - [...] escoamento das águas pluviais exclusivamente para dentro dos limites do lote"; IV - 1,50 m das divisas só para afastamentos laterais e de fundos.
- COES, glossário, p.28: "PROJEÇÃO HORIZONTAL - Toda a área coberta da edificação, excluídas as áreas em balanço, como as varandas, sacadas e saliências."
- COES, Art. 29 I, p.15: vaga "dois metros e cinquenta centímetros de largura e cinco metros de comprimento" (vagas cobertas medem 2,6075 × 5,275: atende).
- Dec. 3.046, XXIII, p.4: "Os locais cobertos para estacionamento ou guarda de veículos somente serão permitidos: a) em subsolo [...]; b) [...] pavimento-garagem" (pp.4-5).
- Dec. 3.046, VII, pp.2-3: varandas "devendo, contudo, atender aos afastamentos frontais mínimos [...], sobre os quais não poderão ser projetados balanços." O texto fala de varanda, não de marquise.
- LC 270, Art. 363 §2º, p.130: "Nas faixas de afastamento frontal mínimo das edificações somente serão permitidos:" — a lista (I a XII) traz "VII - saliências, varandas e sacadas abertas e balanceadas", mas **não nomeia marquise**.
- **Regramento, Art. 5º:** "Taxa de ocupação máxima: 40% da área do lote." Não define projeção, não lista exclusões e não remete à lei municipal. Art. 6º fixa o frontal de 6,00 m sem falar de balanço. Art. 9º: Comissão de Obras aprova antes do protocolo.

**Análise por item:**

| Item | TO do RIU / LC 270 | TO 40% do Regramento |
|---|---|---|
| VAGA 1 | **SAI** pela letra (Art. 350 III, "limitado a uma vaga"; medida atende o COES Art. 29 I). Ressalva: na ZPP, Dec. 3.046 XXIII só admite local coberto para veículo em subsolo ou pavimento-garagem; se isso alcança a casa unifamiliar é tensão aberta desde 01/10 (item 3) → Gate | **INTERPRETAÇÃO → Gate** |
| VAGA 2 | **NÃO SAI** (Art. 350 III, "limitado a uma vaga") | **INTERPRETAÇÃO → Gate**; se valer a lei municipal por analogia, NÃO SAI |
| MARQUISE | **INTERPRETAÇÃO → Gate.** Está em balanço com altura útil de 3,30 m, então o Art. 350 I a tiraria. Mas ela fica sobre o afastamento frontal mínimo, e o Art. 363 §2º ("somente serão permitidos") não lista marquise, enquanto o COES Art. 9º admite marquise "sobre os afastamentos". Não verificado: pilares e escoamento para dentro do lote | **INTERPRETAÇÃO → Gate** |

**Por que o Regramento fica em interpretação:** "taxa de ocupação" é termo técnico do direito urbanístico, e a leitura usual é tomá-lo no sentido da lei municipal. Mas o Regramento é de 2010 e a LC 270 é de 2024. Em 2010, a projeção era a do regime anterior (Dec. 3.046/Dec. 322), que não li para essa definição. Nenhum texto do Regramento diz qual lei usar. A leitura literal ("toda a área coberta") conta tudo. Quem decide como o condomínio lê o próprio artigo é a Comissão de Obras (Art. 9º). Sem texto não há conclusão de lei. → Gate e consulta à Comissão.

**Contas (teto 228,64):**

| Cenário | Projeção | Atende? |
|---|---|---|
| A. Nada sai (leitura literal do Regramento) | 245,95 | **NÃO** (+17,31) |
| B. Sai só a vaga 1 | 245,95 − 14,55 = 231,40 | **NÃO** (+2,76) |
| C. Sai só a marquise | 245,95 − 13,01 = 232,94 | **NÃO** (+4,30) |
| D. Saem vaga 1 + marquise (quadro 455449) | 245,95 − 14,55 − 13,01 = **218,39** | SIM (folga 10,25) |
| E. Saem vaga 1 + vaga 2 + marquise | 218,39 − 14,55 = 203,84 | SIM, mas a vaga 2 **sem base em lei** |

Contra a TO do RIU (285,80), todos os cenários atendem. A TO municipal não é a trava. A trava é o Regramento.

### Conclusão Q1
- **LC 270 / RIU:** VAGA 1 **SAI** (Art. 350 III, p.125), com a ressalva do Dec. 3.046 XXIII (p.4) → Gate. VAGA 2 **NÃO SAI** (mesmo inciso). MARQUISE: **INTERPRETAÇÃO → Gate** (350 I sim; 363 §2º não lista marquise no frontal). Em qualquer leitura, TO municipal atende (máx. 245,95 ≤ 285,80).
- **Regramento Art. 5º:** VAGA 1, VAGA 2 e MARQUISE: **INTERPRETAÇÃO → Gate** e Comissão de Obras (Art. 9º). Pela leitura literal, a projeção é 245,95 > 228,64 e **não atende**. Só atende se o condomínio aceitar as exclusões da LC 270 para a vaga 1 **e** para a marquise (218,39). Só com a vaga 1 (231,40) ou só com a marquise (232,94) não atende.
- **O fator ×0 da vaga 2 não tem base para TO.** No CA/ATE ele tem base: Art. 347 II (p.124, "inclusive seus acessos e áreas de manobra"). A marquise no CA tem base no Art. 347 I (p.124). Isso responde ao E-2026-10-21-05.
- **Saída segura sem depender de interpretação:** reduzir a projeção bruta para ≤ 228,64 (cortar ≥ 17,31 m²), ou recuar a marquise para fora do afastamento frontal **e** obter o aceite da Comissão.

## Q2 — manobra no afastamento frontal e vaga presa

**Texto primário:**
- COES, Art. 29, p.15: vagas "quando projetadas" terão "II - [...] área de manobra, livre de quaisquer obstáculos, contígua à menor dimensão demarcada, de dois metros e cinquenta centímetros de largura por cinco metros de comprimento"; "IV - deverão ter acesso direto e desimpedido às faixas de circulação de veículos, que terão, no mínimo, dois metros e cinquenta centímetros de largura".
- COES, Art. 29 §1º, p.15: fila admitida "Nas edificações multifamiliares" ("filas com no máximo três vagas enfileiradas", I); §1º III admite vagas da mesma unidade "enfileiradas, com apenas uma delas acessando diretamente a circulação" (garagem com 33 ou mais vagas). §2º: uso comercial ou público. **Nada para unifamiliar.**
- COES, Art. 29 §3º, p.15: com acesso direto pelo logradouro, "não será exigida a demarcação da faixa relativa à circulação". Dispensa a demarcação, não a manobra (Skill de vaga, R5).
- COES, Art. 31, p.17: unifamiliar e bifamiliar ficam dispensadas de "III - vagas de estacionamento".
- Dec. 3.046, XXII, p.4: "Será permitida a utilização da área livre do lote para estacionamento ou guarda de veículos [...] excetuada aquela do afastamento frontal mínimo obrigatório".
- LC 270, Art. 347 II, p.124: separa "vagas" de "seus acessos e áreas de manobra".
- LC 270, Art. 363 §2º, p.130: no frontal, "somente" I "rampas para veículos" (§3º: até 10% e 0,50 m), II rampa/passarela de veículos só com terreno abaixo do logradouro, e "XII - estacionamento descoberto ou coberto apenas em edificações unifamiliares e bifamiliares". Não lista "manobra" nem "acesso de veículos em nível".
- LC 270, Art. 364, p.130: laterais e fundos pelo COES.

**(a) Manobra no afastamento frontal.** O Dec. 3.046 XXII veda no frontal o **estacionamento ou guarda** de veículos. Ele não fala de manobra. A LC 270 (347 II) trata manobra como coisa distinta da vaga. Leitura favorável: manobra e acesso não são "estacionamento", e cruzar o frontal para chegar ao lote é inevitável em qualquer casa. Leitura contrária: o Art. 363 §2º diz "somente serão permitidos" e não lista manobra. A área de manobra do Art. 29 II é uma área de 2,50 × 5,00 m que precisa ficar livre, e na ZPP o frontal não pode guardar veículo. Não há texto que resolva. Observação de geometria: com vagas de 2,50 × 6,00 em fila na faixa de 2,50 m, a "menor dimensão" de cada vaga é a de 2,50 m. A manobra contígua da vaga 1 cai no frontal, e a da vaga 2 cai **sobre a vaga 1**. Se forem tratadas como vagas paralelas, a alternativa do Dec. 45.917 Art. 10 (faixa de 3,00 m ao longo do lado maior; Skill de vaga, não relido hoje) também não cabe numa faixa de 2,50 m.

**(b) Vaga presa / em fila.** O Art. 29 IV exige acesso "direto e desimpedido" à circulação. A fila só é admitida em multifamiliar (§1º) e não residencial (§2º). A vaga 2 não tem acesso direto, porque o acesso passa pela vaga 1. Se as vagas da casa são "vagas nos termos do COES" (Skill de vaga, R1 leitura A: o Art. 29 vale "quando projetadas"), a vaga 2 **não atende**. Se a dispensa do Art. 31 III alcança a medida (leitura B), a casa pode guardar carros como quiser, mas aí também não há "vaga" para reivindicar benefício. Quantidade: a casa não tem vaga obrigatória na leitura prática (R2), então a vaga 2 não é exigida.

**Coerência com B1:** mantida. A B1 tratava do **local** da vaga descoberta (afastamento lateral), permitido pelo XXII p.4, que só exclui o frontal. A Q2 trata de **manobra e acesso**, que a B1 já deixou para conferir (COES Art. 29 II e IV). Nada a corrigir na B1.

### Conclusão Q2
- **(a) Manobra no afastamento frontal: INTERPRETAÇÃO → Gate.** Pela letra, XXII veda só estacionamento ou guarda no frontal, mas o Art. 363 §2º não lista manobra entre os usos permitidos ("somente"). Até o Gate, siga a leitura restritiva da Skill de vaga, R3: não contar com o frontal como área de manobra.
- **(b) Vaga 2 presa atrás da vaga 1: NÃO PERMITIDO como vaga nos termos do COES** (Art. 29 IV, p.15; fila só em multifamiliar ou não residencial, §§1º-2º). Pode ficar como espaço de guarda sem status de vaga, já que a casa não tem vaga obrigatória (Art. 31 III, p.17). Essa leitura (R1) também é ponto de Gate.
- Para Arquitetura (não é mérito legal): a faixa de 2,50 m comporta uma vaga com acesso direto, desde que a manobra não dependa do frontal. Duas vagas em fila não cabem.

## Pontos para o Gate
1. **Regramento Art. 5º:** a TO de 40% usa as exclusões da LC 270 (Art. 350) ou a projeção literal? Também perguntar à Comissão de Obras (Art. 9º). Pela leitura literal, o EP v3 não atende (245,95 > 228,64).
2. **Marquise sobre o afastamento frontal:** COES Art. 9º ("sobre os afastamentos") × LC 270 Art. 363 §2º (não lista marquise), na ZPP com Dec. 3.046 VII (veda balanço de varanda no frontal).
3. **Garagem coberta no térreo de unifamiliar na ZPP:** Dec. 3.046 XXIII × LC 270 Art. 350 III (tensão aberta desde 01/10).
4. **Manobra no frontal:** XXII (veda "estacionamento ou guarda") × 363 §2º ("somente").
5. **R1 da Skill de vaga:** a dispensa do Art. 31 III alcança o Art. 29 IV (vaga presa)?

## O que não foi verificado
- Vigência na Busca Fácil: não reconsultada (rede sem DNS hoje de manhã). Não tentei de novo.
- Marquise: se não há pilares e se a água escoa para dentro do lote (COES Art. 9º II). Vi só a bbox e o nome do tipo.
- A área TO da vaga 2 (14,55) não tem região TO própria. O número é do esquema CA.
- Não sei por que a área da região da vaga (14,55) é maior que a do ambiente (13,75). Provavelmente inclui meia parede. Não conferi.
- Dec. 45.917 Art. 10: citado pela Skill, não relido no primário hoje.
- Definição de projeção/TO vigente em 2010 (regime anterior à LC 270), para ler o Regramento na data dele: não pesquisada.
- Posição exata das vagas descobertas em y e da manobra: não li a geometria, só os relatórios.
