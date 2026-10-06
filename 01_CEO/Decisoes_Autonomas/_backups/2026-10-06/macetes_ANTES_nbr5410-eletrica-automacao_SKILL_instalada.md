---
name: nbr5410-eletrica-automacao
description: NBR 5410:2004 (instalações elétricas de baixa tensão, vigente) + revisão 2026 em consulta pública + protocolos de automação residencial (KNX, Zigbee/Z-Wave, Modbus). Use sempre que Landell (ou qualquer Agente) for dimensionar circuito elétrico, definir DR/DPS, calcular corrente/condutor, especificar aterramento, ou escolher protocolo de automação — mesmo que o pedido só mencione "elétrica", "circuito", "disjuntor" ou "automação", sem citar a norma pelo nome.
version: v1.1
fonte_primaria_lida: sim (NBR 5410:2004 versão corrigida 17/03/2008, itens 5.1.3.2, 5.4.2, 5.4.3.5, 5.4.3.6, 6.2.6.1 (Tabela 47), 6.2.9.4, 6.2.9.5, 6.2.11.1.6, 6.3.5.2.1, 6.4.3.1 (Tabela 58), 9.5.2, 9.5.3 — PDF em D:\008_Normas ABNT)
---

# NBR 5410 — Elétrica e Automação Residencial

Skill de Inteligência Técnica da área Elétrica+Automação, equipe de Cardozo (Gestor Complementares). Quem consome: **Landell** (Agente Automação+Elétrica).

## Norma vigente vs. revisão em consulta

| Norma | Situação |
|---|---|
| NBR 5410:2004 (versão corrigida 17/03/2008, incorpora a Errata 1) | **Vigente — única com força normativa hoje.** Usar em todo projeto atual. Cancelou e substituiu a NBR 5410:1997 (Prefácio). |
| NBR 5410 (revisão 2026) | Em segunda consulta pública, publicação prevista fim de 2026. **Ainda NÃO tem força normativa.** |
| NBR 5419 | Vigente (SPDA — proteção contra descargas atmosféricas), vinculada ao projeto elétrico |

**⚠️ A "NBR 5410 2026" ainda não foi publicada. Todo projeto protocolado hoje segue a versão 2004 — não cite a revisão como exigência atual.**

## 1. Parâmetros fundamentais (NBR 5410:2004 — conferido no texto em 29/09/2026)

**Divisão de circuitos em locais de habitação (9.5.3):**
- **9.5.3.1:** todo ponto que alimente, de modo exclusivo ou virtualmente dedicado, equipamento com corrente nominal **acima de 10 A** constitui circuito independente (é o "TUE" — chuveiro, ar-condicionado, forno etc.).
- **9.5.3.2:** tomadas de cozinhas, copas, áreas de serviço, lavanderias e locais análogos ficam em circuitos **exclusivos dessas tomadas**.
- **9.5.3.3:** como exceção à regra geral de 4.2.5.5, **iluminação e tomadas (fora as de 9.5.3.2) podem dividir circuito comum** se: a) IB do circuito comum ≤ 16 A; b) a iluminação não estiver toda num só circuito comum; c) as tomadas não estiverem todas num só circuito comum.
- **Corrigido na v1.1:** a v1.0 dizia "iluminação exclusivo por cômodo" e "máximo 1.500 W por circuito de TUG". **Nenhuma das duas regras está no texto.** O limite real é o de 9.5.3.3 (IB ≤ 16 A no circuito comum), e o dimensionamento segue IB ≤ In ≤ Iz.
- **9.5.4:** todo circuito terminal é protegido por dispositivo que seccione **simultaneamente todos os condutores de fase**. Unipolares lado a lado com alavancas acopladas não contam como multipolares.

**Previsão de carga (9.5.2):** pelo menos um ponto de luz fixo no teto por cômodo, com interruptor (9.5.2.1.1). Tomadas: banheiro ≥ 1 perto do lavatório; cozinha/área de serviço 1 a cada 3,5 m de perímetro, com ≥ 2 acima da bancada; sala e dormitório 1 a cada 5 m (9.5.2.2.1). Potência mínima por tomada: 600 VA até 3 pontos e 100 VA nos excedentes em áreas molhadas; 100 VA nos demais cômodos (9.5.2.2.2). Aquecedor elétrico de água é ligado direto, sem tomada (9.5.2.3).

**Condutores:** dimensionar por método de referência + corrente de projeto, com fatores de correção (6.2.5 e 6.2.6.1.2, que também exige queda de tensão (6.2.7) e seção mínima). Seção mínima, Tabela 47 (6.2.6.1.1): iluminação 1,5 mm² Cu; força (tomadas incluídas) 2,5 mm² Cu; sinalização/controle 0,5 mm² Cu. **LSHF "recomendado em áreas de escape": a confirmar**, porque o item não foi lido nesta conferência (6.2.9.6.8 só trata de dispensa de obturação corta-fogo em poço vertical com cabo livre de halogênio).

**Aterramento (5.4.3.6):** em edificação alimentada em TN-C, o PEN **deve** ser separado em neutro e PE no ponto de entrada ou no quadro principal. Daí para dentro o esquema é TN-S (globalmente, TN-C-S). A única exceção (nota 1) é a edificação em que se possa descartar com segurança o uso, imediato ou futuro, de equipamentos eletrônicos interligados por linhas de sinal. **Corrigido na v1.1:** a v1.0 dizia "TN-S recomendado". Em residência com automação/rede, o texto torna a separação obrigatória. O PE segue a Tabela 58 (6.4.3.1.3): S ≤ 16 mm² → PE = S; 16 < S ≤ 35 → 16; S > 35 → S/2.

**DR 30 mA obrigatório (5.1.3.2.2), qualquer que seja o esquema de aterramento:** a) circuitos de locais com banheira ou chuveiro; b) tomadas em áreas externas; c) tomadas internas que possam alimentar equipamento no exterior; d) em habitação, pontos de cozinha, copa, lavanderia, área de serviço, **garagem** e demais dependências internas molhadas ou sujeitas a lavagem. Notas: vale para tomadas até 32 A (nota 1); em d) admite-se excluir pontos de iluminação a 2,50 m ou mais de altura (nota 3); a proteção pode ser individual, por circuito ou por grupo de circuitos (nota 5). **Corrigido na v1.1:** a lista da v1.0 (banheiro, área de serviço, cozinha) estava incompleta, faltavam garagem, tomadas externas e tomadas internas que alimentam o exterior.

**DPS:**
- Linha de energia (5.4.2.1.1): obrigatório quando a instalação é alimentada por linha total ou parcialmente aérea em região AQ2 (mais de 25 dias de trovoada por ano), ou em região AQ3. Dispensa só por risco calculado e assumido, e nunca se houver risco à segurança das pessoas (nota).
- Linha de sinal (5.4.2.2.1): **toda linha externa de sinal** (telefonia, dados, vídeo, antena) deve ter proteção contra surtos no ponto de entrada/saída da edificação (6.3.5.3). A entrada de sinal deve ser no mesmo ponto da entrada de energia (nota 3).
- Localização (6.3.5.2.1): no ponto de entrada ou no quadro principal o mais próximo possível dele. DPS adicionais para equipamento sensível devem ser coordenados com os de montante (nota 3).
- **Corrigido na v1.1:** a v1.0 dizia "DPS obrigatório com equipamentos sensíveis". O gatilho normativo é o de 5.4.2.1.1 (AQ2 com linha aérea / AQ3) mais toda linha externa de sinal. Equipamento sensível é caso de DPS **adicional** (6.3.5.2.1 nota 3; 5.4.3.5 c)).

**Sinal x força (6.2.9.5):** circuitos de faixa I (ex.: sinal/SELV) e de faixa II (127/220 V) não compartilham a mesma linha, a menos que: todos os condutores sejam isolados para a tensão mais alta; ou estejam em compartimentos separados do conduto; ou em eletrodutos separados. Distância em cm: **não dada** (a nota remete a 5.4 e 6.4; 5.4.3.5 f) só pede "separação adequada, por distanciamento ou blindagem" e cruzamento em ângulo reto). Coerente com a NBR 16415 6.1.1 (ver Skill `nbr14565-...`).

## 2. O que muda na revisão 2026 (monitorar, não aplicar ainda)

- Tabelas de corrente alinhadas à IEC 60364-5-52 (métodos B1, B2, C, D, E, F, G) — dimensionamento mais preciso, seções de cabo podem mudar
- Harmonização com NBR 5419 — elimina contradições de aterramento entre as duas normas
- Novas tecnologias: infraestrutura de recarga de VE, geração distribuída (solar), iluminação pública/equipamentos urbanos

## 3. Automação residencial

Pontos que precisam estar definidos no Briefing antes de projetar:

| Aspecto | Definir antes |
|---|---|
| Protocolo | KNX (robusto, padrão europeu) · Zigbee/Z-Wave (sem fio, residencial) · Modbus (industrial) |
| Topologia | Barramento centralizado vs. mesh distribuído |
| Integração elétrica | Atuadores precisam de circuito dedicado — planejar junto |
| BMS | Em projetos maiores, checar com Cardozo se cliente exige BMS integrado |

## Checklist prático ao receber Briefing

1. Tipo de edificação + carga total estimada (kVA)
2. Planta com pontos de tomada/iluminação + lista de equipamentos > 10 A (circuito independente, 9.5.3.1)
3. Fornecimento da concessionária (mono/bi/trifásico) e se a linha de chegada é aérea (gatilho de DPS, 5.4.2.1.1) — faixas, limite de 75 kW e padrão da Light: ver Skill `entrada-energia-light-ligacao-nova-padrao-recon-bt-rj`
4. Separação do PEN na entrada, com TN-S dali para dentro (5.4.3.6)
5. Corrente de projeto por circuito, fator de demanda, dimensionar condutores (6.2.6.1.2)
6. Disjuntores multipolares nos circuitos com mais de uma fase (9.5.4), DR 30 mA nos casos de 5.1.3.2.2, DPS conforme 5.4.2 e 6.3.5
7. VE, solar ou automação previstos? → reservar circuitos/dutos agora
8. Compatibilizar shafts elétricos com Saturnino. A NBR 5410 6.2.9.4.1 exige afastamento tal que intervir numa linha não danifique a outra, e 6.2.9.4.4 proíbe linha elétrica abaixo de tubulação que condense, salvo proteção. **"30 cm" não consta em 6.2.9.4 (lido)**: pode ser critério de projeto do organismo, nunca exigência da NBR 5410 (coerente com a Skill `nbr5626-8160-hidrossanitario`)
9. Confirmar se nova versão da norma foi publicada antes do protocolo

**Erros comuns:** não separar circuito de equipamento > 10 A · omitir DR nos casos de 5.1.3.2.2 (garagem e tomada externa esquecidas) · dimensionar cabo sem fator de agrupamento · esquecer DPS na entrada de linha de sinal externa · manter PEN além do ponto de entrada · linha elétrica sob tubulação de água sem proteção (6.2.9.4.4).

## Macetes de quem faz (só onde a norma deixa escolha ao projetista; fonte = texto lido)

1. **Circuito comum iluminação + tomadas (9.5.3.3).** A norma permite juntar luz e TUG (fora cozinha/serviço) num circuito com IB ≤ 16 A, desde que nem toda a iluminação e nem todas as tomadas fiquem num único circuito. Mais econômico: 2 ou mais circuitos mistos (ex.: ala íntima e ala social), cada um com parte da luz e parte das tomadas. Menos disjuntores e menos eletrodutos do que separar luz de tomada, e a regra b)/c) garante que um desarme não apaga a casa inteira.
2. **DR por grupo de circuitos (5.1.3.2.2 nota 5).** A proteção pode ser por ponto, por circuito ou por grupo. Mais econômico: um DR por grupo (ex.: banheiros + área de serviço). Contrapartida, tirada do próprio texto: um defeito desliga o grupo todo. Circuito que não pode cair (ex.: congelador) merece circuito e DR próprios, como recomenda a nota 4.
3. **PE comum a vários circuitos (6.4.3.1.5).** Um só condutor de proteção pode servir circuitos que estejam **no mesmo conduto**, dimensionado pela maior fase (Tabela 58). Economiza um condutor por circuito no mesmo eletroduto. Não vale entre eletrodutos diferentes.
4. **Folga de ocupação e trecho longo sem caixa (6.2.11.1.6).** O limite é 40 % (3+ condutores), 31 % (2) e 53 % (1). Trecho contínuo: até 15 m (interno) ou 30 m (externo) em reta, menos 3 m por curva de 90°. A nota deixa uma escolha: em vez de caixa intermediária, **subir uma bitola a cada 6 m** acima do limite. Onde uma caixa ficaria feia ou inacessível (forro, fachada), subir a bitola é mais barato que abrir caixa de inspeção depois. Máximo de 3 curvas de 90° por trecho (6.2.11.1.7).
5. **Sinal x força: eletroduto separado vs. compartimento (6.2.9.5).** Das três opções, a mais barata no embutido é o eletroduto separado, que não exige especificar cabo de sinal com isolação de 450/750 V. No aparente, uma canaleta com compartimentos separados resolve com uma peça só (6.2.9.5 a)).
6. **Carga de iluminação sem projeto luminotécnico (9.5.2.1.2).** Como alternativa à NBR 5413, pode-se usar 100 VA nos primeiros 6 m² + 60 VA a cada 4 m² inteiros. Serve para dimensionar circuito cedo, antes de Tenreiro fechar as luminárias, e não precisa refazer a conta quando a luminária final entra, desde que a potência real caiba no valor previsto. **Atenção:** é carga para dimensionamento, não potência de lâmpada (nota).

Fora destes, nenhum macete entra sem fonte lida.

## Coordenação com outros Agentes de Cardozo

Saturnino (shafts: afastamento por 6.2.9.4.1 e linha elétrica fora de baixo da tubulação por 6.2.9.4.4; a norma não dá valor em cm) · Baumgart (passagem de eletrodutos prevista no memorial estrutural antes da concretagem; 6.2.11.1.12 exige eletroduto e caixas vedados contra nata de concreto) · Glaziou (tomadas externas com DR 30 mA, 5.1.3.2.2 b); IP65 para jardim segue boa prática da equipe, sem item lido nesta conferência) · Tenreiro (posição de tomadas/interruptores validada antes de finalizar prumadas; quantidade mínima por 9.5.2.2.1).

## O que esta Skill NÃO cobre

Média tensão (ANEEL + concessionária; gatilho na Light: carga instalada > 75 kW, ou Grupo A por estudo entre 50 e 75 kW — ver `entrada-energia-light-ligacao-nova-padrao-recon-bt-rj`) · telecomunicações/cabeamento estruturado (NBR 14565, NBR 16264, NBR 16415 — ver Skill `nbr14565-...`) · CFTV/segurança eletrônica · SPDA detalhado (NBR 5419).

## Limitações honestas

- A revisão 2026 está em segunda consulta pública (junho/2026) — mudanças listadas são previstas, não confirmadas. Todo projeto protocolado agora segue 2004.
- Tabelas completas de corrente admissível da versão 2004 não estão reproduzidas aqui — consultar a norma diretamente para dimensionamento real.
- Texto oficial lido em 29/09/2026 **só nos itens listados no frontmatter**. O restante (LSHF, IP por ambiente) segue como fonte secundária, marcado "a confirmar". O "30 cm" foi conferido e não consta em 6.2.9.4.

## Escopo, crescimento e manutenção

Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.

## Histórico de versões

- **v1.0 — 03/09/2026:** Skill real criada a partir da proposta ratificada (fontes secundárias). Sem campo de versão no frontmatter.
- **v1.1 — 29/09/2026 — fonte primária lida (PDF NBR 5410:2004 em `D:\008_Normas ABNT`), pedido de Claudemberg via Wallenberg/Cardozo:** removidos "iluminação exclusiva por cômodo" e "1.500 W por TUG", que não estão no texto (a regra real é a de 9.5.3); TN-S passou de "recomendado" a separação obrigatória do PEN (5.4.3.6); lista de DR completada (5.1.3.2.2); gatilho de DPS corrigido (5.4.2.1.1 / 5.4.2.2.1); Tabela 47 e Tabela 58 citadas; sinal x força (6.2.9.5) coerente com a NBR 16415; "30 cm" e LSHF marcados "a confirmar"; seção "Macetes de quem faz" (6 itens). Backup em `01_CEO/Decisoes_Autonomas/_backups/2026-09-29/`.
