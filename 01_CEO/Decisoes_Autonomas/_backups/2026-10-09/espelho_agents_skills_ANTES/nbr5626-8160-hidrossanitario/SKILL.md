---
name: nbr5626-8160-hidrossanitario
description: NBR 5626:2020 (água fria/quente), NBR 8160:1999 (esgoto sanitário), NBR 10844:1989 (águas pluviais) e correlatas — dimensionamento de instalações hidrossanitárias prediais. Use sempre que Saturnino (ou qualquer Agente) for dimensionar ramais de água, esgoto, calhas pluviais, reservatório, ventilação de esgoto, ou verificar pressão/velocidade em tubulação — mesmo que o pedido só mencione "hidráulica", "esgoto", "caixa d'água" ou "drenagem", sem citar a norma pelo nome.
version: v1.2
fonte_primaria_lida_nbr8160: sim (itens 3, 4.1 a 4.5, 5.1 a 5.2, Tabelas 1 a 8, início do Anexo B; PDF em D:\008_Normas ABNT)
fonte_primaria_lida_nbr5410: sim (item 6.2.9.4, subitens 6.2.9.4.1 a 6.2.9.4.4; PDF em D:\008_Normas ABNT)
fonte_primaria_lida_nbr5626: não (ressalva mantida)
fonte_primaria_lida_nbr10844: não (ressalva mantida)
---

# NBR 5626/8160/10844 — Hidrossanitário Predial

Skill de Inteligência Técnica da área Hidrossanitário, equipe de Cardozo (Gestor Complementares). Quem consome: **Saturnino** (Agente Hidrossanitário).

## Normas-base

| Norma | Assunto | Versão | Status de leitura |
|-------|---------|--------|-------------------|
| NBR 5626:2020 | Água fria e quente | 2020 (unificou 5626 antiga + 7198) | **Fonte primária não lida** — valores da seção 1 com ressalva |
| NBR 8160:1999 | Esgoto sanitário — projeto e execução | Capa do PDF: "SET 1999", válida a partir de 01.11.1999, substitui a NBR 8160:1983 | **Lida (PDF real)**. Revisão posterior a 1999 não verificável sem busca externa — confirmar antes de protocolar |
| NBR 10844:1989 | Águas pluviais | 1989 | **Fonte primária não lida** — seção 3 com ressalva |
| NBR 9649 | Redes coletoras de esgoto sanitário | não verificada | — |
| NBR 7229 | Fossas sépticas | não verificada | — |

## 1. Água fria/quente (NBR 5626:2020) — COM RESSALVA (fonte primária não lida)

**Pressão:** máxima estática 400 kPa (40 mca) em qualquer ponto — acima disso, VRP obrigatória. Mínima dinâmica 10 kPa (1 mca) nos pontos de utilização. Velocidade: 0,5 a 3,0 m/s.

**Dimensionamento — método dos pesos relativos (Hunter adaptado):** Qp (L/s) = 0,3 × √ΣUP, para ΣUP entre 2 e 6000.

| Ponto | Peso (UP) | Vazão de projeto |
|---|---|---|
| Lavatório | 0,3 | 0,15 L/s |
| Vaso sanitário (caixa) | 0,3 | 0,15 L/s |
| Vaso sanitário (válvula) | 2,4 | 1,70 L/s |
| Chuveiro | 0,4 | 0,20 L/s |
| Banheira | 1,5 | 0,30 L/s |
| Pia de cozinha | 0,7 | 0,25 L/s |
| Máquina lava-louça | 0,5 | 0,15 L/s |
| Máquina lava-roupa | 1,0 | 0,30 L/s |

**⚠️ Valores acima vêm de fonte secundária (28/08/2026)**, só para os aparelhos padrão da tabela. Aparelho fora da lista: não extrapolar por analogia.

**Reservatório:** mínimo 1 dia de consumo (200 L/habitante, salvo código de obras local diferente). Superior por gravidade; inferior para sucção de bomba.

**Proibido:** tubulação de água potável em contato com esgoto; conexão direta rede pública/reservatório sem caixa intermediária.

## 2. Esgoto sanitário (NBR 8160:1999) — CONFERIDO NO PDF REAL em 29/09/2026

**Sistema separador absoluto:** nenhuma ligação entre esgoto sanitário e águas pluviais (4.1.3.1).

**Declividades (4.2.3.2 — a norma usa "recomendam-se"):**
- mínima **2% para DN ≤ 75**;
- mínima **1% para DN ≥ 100**;
- **máxima 5%** (4.2.5.2).

*(Corrigido na v1.2: a v1.1 dizia "2% para DN ≤ 100" e "1% para DN > 100". DN 100 pede 1%, não 2%.)*

**Mudanças de direção:** trechos horizontais com peças ≤ 45° (4.2.3.3); horizontal→vertical ≤ 90° (4.2.3.4). É vedado ligar ramal de descarga ou de esgoto em inspeção de joelho ou curva do ramal de descarga da bacia sanitária (4.2.3.5).

**Tabela 3 — UHC e DN mínimo do ramal de descarga** (a unidade da norma é "UHC", unidade de Hunter de contribuição):

| Aparelho | UHC | DN mínimo |
|---|---|---|
| Bacia sanitária | 6 | 100 (ver nota) |
| Banheira de residência | 2 | 40 |
| Bidê | 1 | 40 |
| Chuveiro de residência | 2 | 40 |
| Lavatório de residência | 1 | 40 |
| Pia de cozinha residencial | 3 | 50 |
| Tanque de lavar roupas | 3 | 40 |
| Máquina de lavar louças | 2 | 50 (seguir recomendação do fabricante) |
| Máquina de lavar roupas | 3 | 50 (seguir recomendação do fabricante) |

*(Corrigido na v1.2: bacia tem **6 UHC** sem distinção entre caixa e válvula (a v1.1 dizia 4/6); banheira **2 UHC / DN 40** (a v1.1 dizia 3/50); pia de cozinha **3 UHC** (a v1.1 dizia 2). Incluídos bidê e tanque.)*

**Bacia sanitária em DN 100, exceção condicionada (Tabela 3, nota 1):** a norma admite reduzir para DN 75 **somente** se isso for justificado pelo método hidráulico do Anexo B **e** depois da revisão da NBR 6452:1985, com bacia de fábrica com saída própria para DN 75. Portanto a regra "nunca abaixo de DN 100" é o padrão, mas não é absoluta. DN 75 sem a memória de cálculo do Anexo B e sem bacia específica continua não conforme. A situação atual da NBR 6452 não foi verificada.

**Aparelho fora da Tabela 3 (5.1.2.2, Tabela 4):** estima-se a UHC pelo DN do ramal: DN 40 = 2; DN 50 = 3; DN 75 = 5; DN 100 = 6.

**Ramais de esgoto (Tabela 5):** máximo de UHC por DN: DN 40 = 3; DN 50 = 6; DN 75 = 20; DN 100 = 160.

**Tubos de queda (Tabela 6):** máximo de UHC para prédio de até 3 pavimentos / prédio com mais de 3: DN 40 = 4/8; DN 50 = 10/24; DN 75 = 30/70; DN 100 = 240/500; DN 150 = 960/1900.

**Subcoletores e coletor predial (Tabela 7, 5.1.4.1):** coletor predial com **DN mínimo 100**. Máximo de UHC para DN 100: 180 (1%), 216 (2%), 250 (4%). Para DN 150: 700 (1%), 840 (2%), 1000 (4%).

**Desconectores (5.1.1):** fecho hídrico mínimo de 0,05 m. Caixa sifonada DN 100 até 6 UHC, DN 125 até 10 UHC, DN 150 até 15 UHC (5.1.1.2).

**Inspeção (4.2.6.2):** no máximo 25,00 m entre dispositivos de inspeção; no máximo 15,00 m entre a ligação ao coletor público e a inspeção mais próxima; no máximo 10,00 m entre os trechos de ramais de bacias, caixas de gordura e caixas sifonadas e a inspeção. Em prédio com mais de 2 pavimentos, a caixa de inspeção fica a pelo menos 2,00 m do tubo de queda. Caixa de inspeção (5.1.5.3): profundidade máxima de 1,00 m; lado ou diâmetro interno mínimo de 0,60 m. Acima de 1,00 m, poço de visita (mínimo de 1,10 m).

**Caixas de gordura (5.1.5.1):** 1 cozinha: pequena (CGP) ou simples (CGS); 2 cozinhas: CGS ou dupla (CGD); 3 a 12 cozinhas: CGD; mais de 12: especial (CGE, V = 2N + 20 litros). Pias em pavimentos sobrepostos descarregam em tubo de queda exclusivo para caixa de gordura **coletiva**. Caixa individual nos andares é **vedada** (4.2.6.1).

**Velocidade de autolimpeza de 0,6 m/s e enchimento máximo de 75%:** **não localizados** nos itens 4 e 5 nem no trecho lido do Anexo B. O Anexo B só traz, para o tubo de queda, uma taxa de ocupação menor que 1/3 (B.2.1.4). **Não citar em memorial** até conferir o restante do Anexo B.

### Ventilação (4.3 e 5.2)

- A norma admite **duas formas**: primária + secundária, **ou somente primária** (4.3.1). Somente primária exige verificar a suficiência pelo modelo do Anexo C (4.3.2). Se não for suficiente, alterar a geometria ou prover ventilação secundária (4.3.3).
- *(Corrigido na v1.2: a regra "coluna secundária obrigatória acima de 5 andares" **não existe** no texto lido. O critério é a verificação do Anexo C.)*
- A ventilação secundária pode ser feita com ramais e colunas **ou com válvulas de admissão de ar (VAA)** devidamente posicionadas (4.3.4).
- Terminal do ventilador (4.3.6): a pelo menos 4,00 m de janela, porta ou vão, salvo se elevado 1,00 m acima da verga; 2,00 m acima de laje utilizada para outros fins; caso contrário, 0,30 m; com terminal chaminé ou tê.
- Distância máxima do desconector ao tubo ventilador (Tabela 1): DN 40 = 1,00 m; DN 50 = 1,20 m; DN 75 = 1,80 m; DN 100 = 2,40 m.
- Toda tubulação de ventilação com aclive mínimo de 1% (4.3.13). Diâmetros: Tabela 2 (colunas e barriletes) e Tabela 8 (ramais de ventilação: grupo com bacia até 17 UHC = DN 50; de 18 a 60 UHC = DN 75).
- Prédio de um só pavimento: pelo menos um tubo ventilador DN 100, respeitando a Tabela 1 (4.3.11).
- Bacias em bateria: tubo ventilador de circuito, mais um suplementar a cada grupo de no máximo 8 bacias (4.3.19).

## 3. Águas pluviais (NBR 10844:1989) — COM RESSALVA (fonte primária não lida)

Fórmula de calha: **Q = C × I × A / 360**. I pela curva IDF local, nunca um número de cabeça. **O valor de ~150 mm/h para o RJ é aproximação sem fonte primária.**

Calha horizontal: inclinação mínima 0,5%, velocidade máxima 1,5 m/s (fonte secundária). Pluvial sempre separado do esgoto (confirmado pela NBR 8160, 4.1.3.1).

## Macetes de quem faz (só com fonte: escolha que a própria norma deixa ao projetista)

1. **Ventilação só primária no lugar de coluna de ventilação (4.3.1 b + 4.3.2 + Anexo C).** A norma permite dispensar a ventilação secundária inteira se o modelo do Anexo C comprovar que a primária basta. Economia: sem coluna, sem ramais de ventilação e sem furos extras em laje e shaft. Custo: fazer e anexar a verificação do Anexo C ao memorial. Sem ela, a dispensa não vale.
2. **VAA no lugar de ramal ou coluna até a cobertura (4.3.4).** Quando a secundária for necessária, a norma aceita válvula de admissão de ar como alternativa aos ramais e colunas prolongados acima da cobertura. Evita atravessar a cobertura impermeabilizada, o que reduz o retrabalho de impermeabilização. A condição é "devidamente posicionadas".
3. **Não prolongar todos os tubos de queda até a cobertura (4.3.12).** Se o prédio já tem pelo menos um tubo ventilador primário DN 100, os demais tubos de queda ficam dispensados de prolongamento, desde que: comprimento de até 1/4 da altura do prédio, até 36 UHC e coluna de ventilação ligada acima da cobertura ou a outra existente (Tabela 2). Resultado: menos terminais na cobertura.
4. **Dispensa de ventilar o ramal da bacia (4.3.18).** A ventilação é dispensada se a bacia estiver ligada por ramal exclusivo a um tubo de queda a no máximo 2,40 m, e esse tubo receber, logo abaixo e no mesmo pavimento, outros ramais devidamente ventilados. Isso economiza um ramal de ventilação por banheiro quando o leiaute permite.
5. **UHC reduzida no coletor residencial (5.1.4.2).** Em prédio residencial, o coletor e os subcoletores somam **só o aparelho de maior descarga de cada banheiro**, não todos. Isso reduz a ΣUHC e pode manter o DN 100 onde a soma bruta levaria ao DN 150.
6. **Declividade maior antes de subir o diâmetro (Tabela 7 + 4.2.5.2).** No DN 100, passar de 1% para 2% eleva a capacidade de 180 para 216 UHC; a 4%, para 250 UHC. Se a cota do terreno permitir (máximo de 5%), aumentar a declividade pode evitar trocar para DN 150. Depende da cota do coletor público, que é dado de campo.
7. **Uma caixa sifonada para o banheiro inteiro (4.2.2.3).** Lavatório, bidê, banheira e chuveiro de uma mesma unidade podem ir para uma caixa sifonada única, que também recebe a lavagem de piso (com grelha). É um desconector no lugar de vários. Vale respeitar o limite de UHC da caixa (5.1.1.2) e a Tabela 1.
8. **Caixa de gordura só quando exigida (4.2.6.1).** O uso é *recomendado*. Se a autoridade pública não exigir, fica a critério do projetista. Exceção sem escolha: pias em pavimentos sobrepostos exigem caixa coletiva. **Pendente:** confirmar se Águas Rio ou a Prefeitura exigem caixa de gordura no RJ antes de dispensar.
9. **Lavagem de piso ou de garagem abaixo da rua (4.2.7.2).** Esgoto só de lavagem de pisos ou automóveis dispensa caixa de inspeção. Basta uma caixa sifonada de diâmetro mínimo 0,40 m ligada direto à caixa coletora.
10. **Aparente em vez de enterrado (4.2.5.5).** Em tubulação aparente, as interligações podem ser feitas com junção a 45° e dispositivo de inspeção, sem caixa de inspeção. Enterrada exige caixa ou poço de visita.

Nenhum macete acima vem de "prática de mercado". Todos são alternativas escritas na própria NBR 8160:1999.

## Checklist prático ao receber Briefing (via Cardozo, vindo de Lúcio)
1. Pavimentos, unidades, tipologia
2. Pontos de utilização por unidade/andar → ΣUP (água) e ΣUHC (esgoto, Tabela 3)
3. Pressão disponível na rede pública
4. Volume de reservatório (≥ 1 dia de consumo)
5. Pressão > 400 kPa em algum ponto? → VRP (NBR 5626, com ressalva)
6. Dimensionar água fria/quente
7. Dimensionar esgoto: Tabelas 3, 5, 6 e 7; bacia DN 100 (DN 75 só pela nota 1 da Tabela 3)
8. Declividades: 2% (DN ≤ 75), 1% (DN ≥ 100), máximo 5%
9. Ventilação: só primária verificada pelo Anexo C, ou secundária (ramais/colunas ou VAA)
10. Inspeção: 25 m / 15 m / 10 m; caixa ≤ 1,00 m de profundidade
11. Calhas/condutores pluviais com IDF local RJ confirmado
12. Confirmar separação absoluta pluvial/esgoto (4.1.3.1)

**Erros comuns:** interligar esgoto e pluvial · omitir VRP · ventilação só primária sem a verificação do Anexo C · declividade abaixo de 2% em DN ≤ 75 ou abaixo de 1% em DN ≥ 100 · bacia em DN 75 sem cálculo do Anexo B · caixa de gordura individual em pavimentos sobrepostos.

## Coordenação com outros Agentes de Cardozo
- **Baumgart:** shafts e furos, com o leiaute apresentado antes do detalhamento estrutural.
- **Landell:** proximidade entre água e linha elétrica. **A NBR 5410:2004 não fixa distância de 30 cm** (nem outra distância numérica) no item de proximidade com linhas não elétricas. O que ela exige (6.2.9.4):
  - **6.2.9.4.1:** o afastamento entre as superfícies externas deve garantir que a intervenção em uma linha não traga risco de dano à outra (critério de desempenho, sem número);
  - **6.2.9.4.2:** afastar das canalizações que produzam calor, fumaça ou vapor, ou interpor anteparo (relevante para tubulação de água quente);
  - **6.2.9.4.4:** quando a linha elétrica seguir o mesmo percurso de canalizações que possam gerar condensação (**tubulações de água** e de vapor), ela **não deve ficar abaixo delas**, salvo com proteção contra os efeitos da condensação.
  - Os 30 cm podem ser adotados como critério de projeto do organismo, mas **nunca citados como exigência da NBR 5410**.
- **Glaziou:** raízes que ameaçam tubulação externa; tipo de tubo e proteção.
- **Mindlin:** leiaute de shafts e esquemas verticais legíveis para prancha.

## O que esta Skill NÃO cobre
Combate a incêndio/hidrantes (NBR 13714) · gás predial (NBR 15526) · tratamento de efluentes/ETE · reuso (ver Skill `nbr16783-reuso-agua`).

## Limitações honestas
- NBR 8160: PDF lido é a edição de set/1999. Não verifiquei se houve revisão posterior, porque não tenho busca externa. Confirmar antes de protocolar.
- Anexos B (além de B.2.1), C, D e E a H da NBR 8160 não foram lidos por inteiro. Macetes 1 e 2 dependem do Anexo C, cujo modelo precisa ser lido antes do primeiro uso real.
- NBR 5626:2020 e NBR 10844:1989: fonte primária **não lida**. Seções 1 e 3 continuam com valores de fonte secundária.
- Peso de água fria para ducha higiênica/bidê segue sem fonte. Pelo esgoto, o bidê tem 1 UHC / DN 40 (Tabela 3 da NBR 8160).

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente: reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.

## Histórico
- v1.0 — 28/08/2026 (convertida em Skill 03/09/2026).
- v1.1 — 28/09/2026 — "30 cm água/eletroduto, exigência NBR 5410" marcado "a confirmar".
- v1.2 — 29/09/2026 — Saturnino, a pedido de Cardozo (via Wallenberg/Claudemberg): NBR 8160:1999 conferida no PDF real. Corrigidos: declividades (DN ≤ 75 / DN ≥ 100, máximo 5%), UHC de bacia, banheira e pia, regra de ventilação ">5 andares" (inexistente) e ressalva da nota 1 da Tabela 3 (DN 75 para bacia). 0,6 m/s e 75% rebaixados a "não localizado". NBR 5410 6.2.9.4 lida: não existem 30 cm na norma. Criada a seção "Macetes de quem faz" com 10 itens, todos com fonte na norma. Backup em `01_CEO/Decisoes_Autonomas/_backups/2026-09-29/`.
