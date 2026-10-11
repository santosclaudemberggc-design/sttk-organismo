---
name: vidro-fachada-poente-ini-r-fator-solar-transmitancia-rj
description: Como o vidro é medido no desempenho térmico e na etiqueta de eficiência residencial (INI-R, Portaria Inmetro 309/2022, que remete à NBR 15575) — fator solar (FS), transmitância do vidro (U), percentual de elementos transparentes (Pt,APP) — e a brecha de usar vidro de controle solar mais sombreamento para ganhar área envidraçada na fachada poente do Rio sem perder desempenho. Use sempre que Lúcio/Oscar (ou Tenreiro) for definir tamanho de janela, pano de vidro, esquadria da fachada oeste ou especificar vidro — mesmo que o pedido só mencione "vidro", "pele de vidro", "janela grande", "insulfilm", "vidro refletivo" ou "etiqueta Procel/PBE", sem citar a INI-R pelo nome.
version: v1.2
status: ativa-com-ressalva
validacao: "Lúcio 29/09/2026 — PROCEDE COM RESSALVA (R1: FS 0,87 / U 5,70 / Pt 17% a confirmar na NBR 15575-1 §11.4.7.2; R2: zona da INI-R para o Rio pós-NBR 15220-3:2024; R3: metamodelo INI-R não comprova NBR 15575 em obra nova enquanto a R4 da Skill 15575-4 estiver aberta)"
fonte_primaria_lida: "Portaria Inmetro 309/2022, Anexo II (INI-R) — parcial"
data: 2026-09-29
changelog: "v1.2 (29/09/2026, treino Oscar) — piso FS 0,20 no §3.2, recusa de sombreamento registrada no §3.4, 2 itens novos no checklist. v1.1 (29/09/2026, Lúcio, validação Passo 4.2) — §3.3 alinhado à Skill de proteção solar (poente = sombreamento vertical/AHF; varanda/AVS sozinha é fraca contra sol baixo); ressalva (4) NBR 15575 obrigatória × INI-R voluntária; §3.1 'reprovar' → 'não atender ao prescritivo'; §6 ZB 4A marcada como indício."
tipo: Inteligência (Trilha A)
gestor_alvo: Lúcio (Arquitetura)
agente_principal: Oscar (projeto arquitetônico)
agentes_cross: Tenreiro (especificação de vidro/esquadria em interiores), Burle (render com vidro de controle solar — cor e reflexo mudam a imagem)
---

# Skill: Vidro na Fachada Poente — Fator Solar, Transmitância e Percentual de Vidro (INI-R / NBR 15575) no Rio

> ⚠️ RESSALVA DE FONTE. (1) **Lida no texto primário:** a Portaria Inmetro 309, de 06/09/2022 (PDF oficial do PBE Edifica, 311 páginas; lidos os Arts. 1º a 5º e o Anexo II, INI-R, itens 4, 6 e Anexos A e B). (2) Os **valores do vidro do modelo de referência** (FS 0,87 · U 5,70 · Pt 17%) vêm da **minuta** da INI-R (LabEEE/UFSC, 09/11/2020, Tabela C.9). A versão final da INI-R **não repete a tabela**: remete à NBR 15575-1, subseção 11.4.7.2, que é paga e **não foi lida**. Trate esses três números como "valor de referência provável, a confirmar na NBR 15575-1". (3) **Zona bioclimática:** a INI-R de 2022 usa as **8 zonas antigas** (Tabela A.1, ZB1 a ZB8), enquanto a NBR 15220-3:2024 passou a 12 zonas (Rio: indício de 4A, ver `nbr15220-3-bioclimatica-rj`). **A confirmar:** qual zona a INI-R manda usar para o Rio depois da reclassificação. (4) **Duas réguas diferentes, não confundir:** a NBR 15575 é o desempenho mínimo exigível da edificação residencial; a INI-R/ENCE é etiqueta **voluntária**. O método simplificado (metamodelo) descrito aqui vale para a **etiqueta**. A Skill `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj` registra (fonte secundária, R4 dela) que a Emenda 2025 tornou a simulação anual obrigatória em obra nova; se isso se confirmar, passar no metamodelo da INI-R **não comprova** a NBR 15575, e a obra nova precisa da simulação de qualquer forma. Também não se sabe se a Emenda 2025 mudou os valores de referência de (2).

## 1. POR QUE ESSA SKILL EXISTE

A Skill `lucio-protecao-solar-externa-dispositivos-rj` resolve o sombreamento (brise, cobogó, veneziana), mas **exclui de propósito a especificação do vidro** (linha 126). O cliente da Barra/Recreio quer pano de vidro para a vista, e a vista quase sempre está a oeste (lagoa, pôr do sol) ou ao sul (mar). A pergunta real de Oscar é: **"quanto vidro posso pôr no poente, e que vidro, sem reprovar no desempenho térmico?"** A resposta não é um número mágico de fator solar. É **entender a regra do jogo** da avaliação.

## 2. A REGRA DO JOGO (Portaria 309/2022, Anexo II — INI-R)

- **A etiqueta residencial (ENCE) é voluntária** (Art. 1º, §1º), mas desde **01/05/2024** só é emitida por estes requisitos (Art. 3º). O desempenho térmico mínimo vem da NBR 15575 (Skill `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj`), e a INI-R usa a **mesma régua**.
- **Fator solar (FS), definição 4.62:** fração da radiação solar que bate no vidro e vira calor dentro do ambiente, contando a parte transmitida e a absorvida e reemitida. **Quanto menor, menos calor entra.** O vidro comum fica perto de 0,87.
- **Três caminhos de avaliação:**

| Método | Onde | O que faz com o vidro | Resultado máximo |
|---|---|---|---|
| **Prescritivo** | Anexo A | Compara U e CT da parede, **Pt,APP** (percentual de vidro), **At,APP** (área de vidro) e Pv,APP (abertura para ventilação) com os valores de referência da NBR 15575-4, Seção 11. **Não enxerga o FS do vidro nem o sombreamento** | Só **classe C** |
| **Simplificado** | Anexo B.I (metamodelo) | Modelo real × modelo de referência. **Considera o FS do vidro, a transmitância do vidro e os ângulos de sombreamento** | Classes A a E |
| **Simulação** | Anexo C | Tudo o que ficar fora dos limites do simplificado | Classes A a E |

- **Limites do método simplificado (Tabela 6.1), texto primário:**
  - FS do elemento transparente: **0,20 a 0,87**
  - Transmitância do elemento transparente: **2,50 a 5,87 W/(m²·K)**
  - Área de vidro por ambiente: **0 a 60 m²**
  - Ângulo vertical de sombreamento da fachada (AVS): **0° a 55°**; ângulos horizontais (AHF D/E): **0° a 80°**
  - Pé-direito: **2,40 a 7,50 m**

  Fora de qualquer desses intervalos (ex.: vidro com FS abaixo de 0,20, pé-direito duplo acima de 7,50 m), **vai para simulação**.
- **Modelo de referência (a régua):** minuta INI-R, Tabela C.9: vidro com **FS 0,87**, **U 5,70 W/(m²·K)** e **Pt,APP 17%** da área de piso do ambiente de permanência prolongada; ventilação Pv,APP 7,65% (fator de ventilação 45%). Ressalva (2): confirmar na NBR 15575-1 §11.4.7.2.

## 3. A BRECHA VÁLIDA: "O VIDRO COMPRA ÁREA DE VIDRO"

Leitura do método (lógica da comparação real × referência, não um número de norma):

1. **No prescritivo, o pano de vidro grande costuma não atender** (o que não é reprovação: manda para o simplificado ou para a simulação), porque o método só olha o *percentual* de vidro contra a referência (cerca de 17% do piso) e ignora que o vidro é de controle solar. Uma sala de 30 m² com 12 m² de vidro tem Pt = 40%.
2. **No simplificado, o mesmo pano pode passar.** A referência é vidro comum (FS 0,87) sem sombreamento. O projeto real pode compensar mais área com **FS menor** (vidro de controle solar ou laminado com película incorporada) e com **ângulos de sombreamento** (beiral, varanda, brise: Skill de proteção solar, até AVS 55°). Quem entrega a carga térmica total igual ou menor que a da referência passa, e pode subir de classe. **Piso:** FS abaixo de 0,20 (típico de vidro refletivo muito escuro) tira o ambiente do simplificado e manda para simulação (Tabela 6.1).
3. **Ordem de custo-benefício para a fachada oeste do Rio (recomendação, não regra):** primeiro o **sombreamento externo**, depois o **FS do vidro**, e por último a **redução de área**. O sombreamento bloqueia o sol antes do vidro; o FS baixo também corta luz (ver 4.2). **Atenção ao tipo de sombra no poente:** o sol da tarde é baixo, e a Skill `lucio-protecao-solar-externa-dispositivos-rj` (§2) manda **dispositivo vertical** na fachada oeste. Varanda profunda e beiral dão AVS (horizontal), que o metamodelo credita, mas protegem pouco contra o sol baixo das 15h–18h. No poente, conte com os **ângulos horizontais (AHF)**: brise vertical, empenas/paredes laterais da varanda. Varanda reentrante (fechada dos lados) entrega os dois ângulos e não é computável (Skill `varandas-nao-computaveis-ate-to-coes-lc198-rj`, respeitado o limite de 1,50 m de profundidade quando serve cômodo).
4. **Consequência de processo:** se o cliente quer pano de vidro, **Oscar avisa no Estudo Preliminar** que a comprovação será pelo método simplificado ou por simulação, e não pelo prescritivo. Isso tem custo de consultoria e precisa entrar na proposta. **Se o cliente recusar o sombreamento** no poente, registre como decisão informada, com a consequência declarada (simulação obrigatória e/ou classe menor).

## 4. ESPECIFICAÇÃO (o que Oscar pede ao fornecedor)

1. **Três números declarados pelo fabricante, por vidro composto (não por lâmina):** FS (ou "fator solar"/SHGC), **transmissão luminosa (TL)** e **U (W/m²·K)**. Sem os três em catálogo técnico ou laudo, o vidro não entra na avaliação.
2. **Não troque luz por calor às cegas.** Vidro de FS muito baixo e muito refletivo costuma ter TL baixa: escurece a sala e piora a iluminação natural exigida pelo COES (Skill `coe-lc198-2019-...`). Confira TL junto com FS.
3. **Película aplicada depois ("insulfilm") não é o vidro do projeto.** Para a avaliação vale o elemento transparente especificado e instalado.
4. **Burle:** vidro de controle solar muda a cor e o reflexo. O render da fachada tem de usar o vidro especificado, senão o cliente aprova uma imagem que a obra não entrega.
5. **Nenhum valor de FS de produto comercial está nesta Skill** (as fontes lidas em 28/09 não traziam números; decisão: não inventar). Cada projeto usa o catálogo técnico do vidro escolhido.

## 5. CHECKLIST DE OSCAR (fachada envidraçada)

- [ ] Pt,APP de cada sala/dormitório com vidro a oeste ou norte (área de vidro ÷ área de piso)
- [ ] Algum ambiente acima da referência (cerca de 17%, a confirmar)? Então o prescritivo não basta, e isso é avisado ao cliente no EP
- [ ] Sombreamento existente (varanda, beiral, brise), com o AVS e os AHF estimados
- [ ] Vidro candidato com FS, TL e U de catálogo
- [ ] FS entre 0,20 e 0,87, U entre 2,50 e 5,87 e pé-direito até 7,50 m? Se sim, cabe no simplificado; se não, vai para simulação
- [ ] Zona bioclimática usada na avaliação conferida (ressalva 3)
- [ ] TL do vidro compatível com a iluminação natural exigida pelo COES (§4.2)
- [ ] Cliente quer etiqueta A ou B? O prescritivo não serve (vai no máximo à C), então avisar no EP
- [ ] Render (Burle) com o vidro especificado

## 6. RELAÇÃO COM OUTRAS SKILLS (checagem de coerência 29/09/2026)

- `lucio-protecao-solar-externa-dispositivos-rj`: **complementa**. Lá fica o dispositivo de sombra; aqui, o vidro e a régua de avaliação. Aquela Skill exclui a especificação de vidro (linha 126); a linha 126 de lá remete para esta desde 29/09/2026. Dispositivo por orientação (vertical no poente) é dela; o §3.3 daqui segue essa regra.
- `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj`: **complementa**. Lá ficam as vedações opacas (U e CT de parede; zona a confirmar, indício 4A); aqui, os elementos transparentes. Os valores de parede ficam só lá.
- `nbr15220-3-bioclimatica-rj`: **complementa**. A zona do Rio é definida lá. Aqui só se aponta a divergência de zoneamento da INI-R (8 zonas) como ressalva, sem fixar zona.
- `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj`: **complementa**. O vão mínimo legal de iluminação e ventilação é piso; o vidro escolhido aqui não pode baixar a TL a ponto de prejudicar a iluminação exigida lá.
- `varandas-nao-computaveis-ate-to-coes-lc198-rj`: **complementa**. A varanda é o sombreamento mais barato e não entra na ATE/TO.

## 7. O QUE ESTA SKILL NÃO COBRE

- Valores numéricos de parede e cobertura de referência (NBR 15575-4/5, Skill própria)
- Cálculo do método simplificado (usar a ferramenta oficial do PBE Edifica/interface web; o método é do consultor)
- Segurança do vidro (laminado/temperado, NBR 7199), guarda-corpo de vidro (NBR 14718) e acústica do vidro

## 8. FONTES

- Portaria Inmetro nº 309, de 06/09/2022 (consolidada, retificada NT01), Anexo II, INI-R: https://pbeedifica.com.br/sites/default/files/Port_309_2022_Edificacoes_Retificada%20NT01.pdf. **Lida (primária)**: Arts. 1º, 3º e 5º; itens 4.62, 6.1 e 6.2 (Tabela 6.1); Anexo A (prescritivo, Tabela A.1); Anexo B (referência → NBR 15575-1 §11.4.7.2).
- Minuta INI-R, LabEEE/UFSC, 09/11/2020, Tabela C.9 e C.10: https://labeee.ufsc.br/sites/default/files/documents/2020.11.09-INI-R_V1.pdf. **Minuta, não o texto final.**
- Lacuna de 28/09/2026 (rodada anterior): fontes comerciais (SindusCon-SP, AGC, Contramarco) sem números. Não foram usadas aqui.
