---
name: entrada-energia-light-ligacao-nova-padrao-recon-bt-rj
description: Entrada de energia da Light para residência nova no Rio (Barra/Recreio) — escolha do padrão (monofásico até 8 kVA, bifásico até 13 kVA, trifásico 13 a 76 kVA demandados), limite de 75 kW de carga instalada para continuar em baixa tensão na rede aérea (acima disso, média tensão e subestação), quando a Light exige ART/RRT/TRT (acima de 15 kVA), quando a ligação precisa de "estudo" (acima de 24 kVA ou ramal acima de 30 m), ligação provisória de obra, a armadilha de a microgeração solar ficar limitada à potência disponibilizada, e as medidas do padrão no muro (poste, caixa de medição a 1,5 m, eletroduto, aterramento). Use sempre que Landell for dimensionar a entrada de energia, prever carregador de carro elétrico, ar-condicionado central, piscina aquecida ou energia solar, ou quando Oscar for desenhar o muro frontal e o acesso, mesmo que o pedido só mencione "relógio de luz", "padrão da Light", "ligação nova", "poste", "medidor", "trifásico" ou "energia da obra".
version: v1.1
status: ativa-com-ressalva
validacao: "Cardozo (Gestor Complementares), 05/10/2026 — PROCEDE COM RESSALVA. Faixas, 75 kW, 15 kVA, 24 kVA/30 m, conexão temporária, microgeração e medidas do vídeo conferem com o FAQ e a transcrição; corrigidos o limite de 300 kVA (só simplificada/blindada simplificada), o RT em MT, a ligação de obra sem fonte e a leitura do COE Art. 35. Segue com ressalva porque RECON-BT, REN 1000 e rede aérea × subterrânea não foram lidas."
changelog:
  - "v1.0 (05/10/2026, Rotina Diária v3.5.0): proposta."
  - "v1.1 (05/10/2026, Cardozo): 300 kVA restrito à simplificada e à blindada simplificada; TRT admitido em MT até 800 kVA (não 'só TRT'); FAQ usa 75 kVA na seção de MT (incoerência da própria Light marcada); Grupo A entre 50 e 75 kW (REN 1000 art. 23 §1º, citado pelo FAQ); vistoria: acesso impedido também gera cobrança, MT não cobra; 'ligação de obra não aproveita o padrão definitivo' removido (sem fonte); vídeo vale para padrão até 38 kVA; 3 itens do §4 marcados como não conferidos na transcrição (conferidos depois por Wallenberg na transcrição completa: 00:52, 02:31, 03:57); COE Art. 35 §2º conferido no primário e a inferência sobre o padrão separada do texto da lei; Art. 33 V incluído; coerência com automacao-residencial-tendencias e nbr14565 acrescentada."
fonte_primaria_lida: "Light S.A., 'FAQ para Solicitações Técnicas — Ligação Nova' (PDF oficial, light.com.br/Downloads/Ligação Nova/LIGACAO_NOVA_INFORMACOES.pdf), lido inteiro via pypdf em 05/10/2026; vídeo oficial da Light 'padrão de ligação até 38 kVA' (youtu.be/2RG3FdAizUQ, 6min09s), assistido via /watch (transcrição Whisper + quadros)"
data: 2026-10-05
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_principal: Landell (Elétrica + Automação)
agentes_cross: Oscar (muro frontal e acesso), Baumgart (base do poste/caixa no muro), Hely (ART/RRT no processo), Lelé (orçamento da entrada)
---

# Skill: Entrada de energia Light — ligação nova e padrão (RECON-BT), residência no Rio

> ⚠️ RESSALVA DE FONTE. (1) **Lido no primário:** o FAQ oficial de Ligação Nova da Light (PDF) e o vídeo oficial da Light sobre o padrão. (2) **Não lido:** o texto da **RECON-BT 2024** (Light). O download do PDF oficial devolveu página HTML, não o arquivo. Os desenhos, as tabelas de disjuntor/condutor por faixa e o Fascículo 07 (padrões de entrada individual) **não estão nesta Skill**. (3) **Não lida:** a REN ANEEL 1000/2021, que o FAQ cita como base. O limite de 75 kW e o de 2.500 kW vêm do FAQ da Light, não da resolução. (4) **Não confirmado:** se o lote da Barra/Recreio está em rede **aérea ou subterrânea**. Muda tudo (seção 3). Pergunte à Light (consulta de viabilidade) antes de fechar o padrão.

## 1. POR QUE ESSA SKILL EXISTE

A Skill `nbr5410-eletrica-automacao` pede como entrada "fornecimento da concessionária (mono/bi/trifásico)" e deixa média tensão fora do escopo. Ninguém no organismo sabia **como a Light decide isso**. Em casa de alto padrão na Barra/Recreio, com ar-condicionado em todos os cômodos, piscina aquecida e carregador de carro elétrico, a carga instalada pode chegar perto do limite em que a Light deixa de atender em baixa tensão. Descobrir isso na hora da ligação custa meses.

## 2. A REGRA (FAQ Light, Ligação Nova)

**Faixas de padrão de entrada individual (carga demandada):**

| Padrão | Faixa |
|---|---|
| Monofásico | 0 a 8 kVA |
| Bifásico | 0 a 13 kVA |
| Trifásico | 13 a 76 kVA |
| Sistema subterrâneo | até 1.143 kVA (220/127 V), conforme o padrão de atendimento da Light |

**Nível de tensão (carga instalada / demanda):**
- Baixa tensão em **rede aérea**: carga instalada **≤ 75 kW**.
- Baixa tensão em **sistema subterrâneo**: até o limite de carga do padrão da Light.
- **Média tensão** (primária < 69 kV): carga instalada **> 75 kW** e demanda contratada ≤ 2.500 kW. Exige subestação. Padrões do FAQ: subestação simplificada com transformador em poste ou pedestal ("obrigatório para regiões atendidas em rede subterrânea", texto do FAQ), blindada simplificada ou blindada convencional. **Só a simplificada e a blindada simplificada** ficam limitadas a 300 kVA e 13,8 kV. O FAQ recomenda pedir **viabilidade técnica** antes (nível de tensão e rede aérea ou subterrânea).
- **Incoerência da própria Light:** a seção de MT do FAQ fala em "carga instalada acima de 75 **kVA**"; a seção de requisitos fala em 75 **kW**. Vale o kW (é o que o FAQ atribui à REN 1000), mas confirme no caso real (R2).
- **Grupo A entre 50 e 75 kW:** o FAQ cita a REN 1000/2021, art. 23 §1º. Unidade com carga e/ou geração **acima de 50 kW e até 75 kW** pode ser enquadrada no Grupo A (média tensão) se tiver potencial de prejudicar outros consumidores, justificado em estudo da Light. Ficar abaixo de 75 kW não garante BT.
- Tensões de BT da Light: 220/127 V (aérea e subterrânea, 4 fios); 380/220 V (subterrâneo dedicado).

**Atenção:** o FAQ usa **carga instalada** para o limite de 75 kW e **carga demandada** para as faixas do padrão. São coisas diferentes. Landell calcula as duas (ressalva 2: o método de demanda está na RECON-BT, não lida).

**Responsável técnico:** carga demandada **acima de 15 kVA** → a preparação do local tem de ser feita por profissional com **ART (CREA-RJ), RRT (CAU) ou TRT (CFT)** quitado. Em MT o responsável técnico é obrigatório: até 800 kVA pode ser técnico do CFT com TRT; acima de 800 kVA, só profissional do CREA com ART, e a ART de execução tem de ser no CREA-RJ. Landell prepara a documentação, mas não assina ART/RRT/TRT.

**Com ou sem estudo:** o fluxo rápido (sem estudo) vale para **entrada individual até 24 kVA, rede aérea, ramal até 30 m**. Fora disso, a Light faz estudo e o prazo cresce.

**Prazos (BT, sem estudo):** validação de documentos em 5 dias úteis; vistoria e instalação do medidor em até 5 dias úteis. A energia fica disponível na instalação do medidor.

**Vistoria:** a Ligação Nova é gratuita. Se o padrão tiver irregularidade ou se o acesso às instalações estiver impedido (FAQ), ou se o técnico **não achar a numeração da casa** (vídeo), a nova vistoria é cobrada na conta pela Tabela de Valores dos Serviços Cobráveis da ANEEL ("Vistoria de unidade consumidora"). Em MT não há essa cobrança (FAQ).

**Ligação provisória de obra ("Conexão Temporária"):** sem estudo em rede aérea com carga **inferior a 24 kW**; com estudo em rede subterrânea ou carga acima de 24 kW (aí exige ART/RRT/TRT).

**Microgeração (solar):** até 75 kW, **limitada à potência disponibilizada** para a unidade consumidora. Prazos da Light: análise de documentos em 5 dias úteis; orçamento em 15 dias (sem obra) ou 30 (com obra); análise de projeto em até 30 dias; obra de conexão em até 60 dias (rede aérea < 2,3 kV).

## 3. BRECHAS E ARMADILHAS (Barra/Recreio, alto padrão)

- **Dimensione a entrada já pensando no solar.** Como a microgeração fica limitada à potência disponibilizada, uma entrada mono de 8 kVA trava o sistema solar do cliente. Se o cliente pode querer solar ou carro elétrico, a entrada trifásica nasce no projeto, não na reforma.
- **Fique abaixo do limite de 75 kW de carga instalada** quando der, para não cair em média tensão com subestação. Isso se resolve no projeto: equipamentos com potência menor, chuveiro a gás ou bomba de calor no lugar de resistência, carregador de carro com controle de carga. É decisão de Landell com o cliente, documentada no memorial.
- **24 kVA e 30 m de ramal** separam o caminho rápido do caminho com estudo. Casa com testada longa e poste da Light distante pode passar dos 30 m sem ninguém perceber.
- **Rede subterrânea** muda padrão, limite e prazo. Não presuma rede aérea (ressalva 4).
- **Ligação de obra é outro pedido** (Conexão Temporária no FAQ), com limite próprio (24 kW). Se o padrão definitivo pode ou não servir à obra **não está no FAQ**: confirmar na RECON-BT (R1). Entra no cronograma de Lelé antes do início da obra.
- **Grupo A entre 50 e 75 kW** (seção 2): em casa de alto padrão com carga alta, mesmo abaixo de 75 kW, a Light pode exigir MT por estudo. Peça a viabilidade cedo.

## 4. O PADRÃO NO MURO (vídeo oficial da Light, rede aérea)

**Escopo do vídeo:** o FAQ apresenta esse vídeo como guia do padrão para carga **até 38 kVA**. Entre 38 e 76 kVA (trifásico), as medidas abaixo **não estão confirmadas**; vale o Fascículo 07 da RECON-BT (R1). Os 3 itens que Cardozo marcou na validação (poste no limite do muro, armação secundária, caixa de aterramento) foram conferidos por Wallenberg na transcrição completa do vídeo em 05/10/2026; o minuto está em cada item.

O que Oscar precisa reservar no muro frontal e Landell especificar:
- **Poste** dentro do lote, no limite do muro com a rua (vídeo, 00:52). Poste da Light **do outro lado da rua** → poste de **7 m ou 7,5 m**. Poste da Light **na mesma calçada** → **5 m ou 6 m**.
- **Caixa de medição** no muro (ou no poste, se não houver muro), **voltada para a rua**, com o **centro do visor a 1,5 m do solo**.
- **Caixa do disjuntor** pode ficar voltada para dentro do lote, a **no máximo 1 m** da caixa de medição.
- **Eletroduto de entrada:** **1"** monofásico; **2"** bifásico/trifásico; cabeçote ou curva de 180° no topo; fixado no poste em no mínimo 3 pontos. Armação secundária (haste + isolador roldana) no furo mais alto do poste, voltada para a rua (vídeo, 02:31-02:38). Opção sem eletroduto de entrada: prensa-cabo na caixa e abraçadeiras no muro.
- **Sobra de 30 cm** de cabo na caixa de medição.
- **Aterramento:** haste de **2,40 m**, diâmetro mínimo **5/8"**, em caixa de aterramento (vídeo, 03:57-04:15); **neutro ligado ao aterramento** (conector cunha ou split bolt).
- Fabricantes de caixa e poste: só os da lista "Fabricantes Validados" da Light.

**Conflito com arquitetura:** o COE (LC 198/2019, lido no primário) obriga toda edificação a ter "sistema de distribuição de energia elétrica, ligado à rede pública, e compartimentos para medidores", atendendo às normas das concessionárias (Art. 33, V). O Art. 35, §2º veda "degraus, rampas de acesso ao lote e abertura de portões fora do alinhamento". O COE **não fala** de caixa ou poste do padrão. A posição deles no lote vem do vídeo/RECON-BT. O que o COE trava é o acesso (portão e rampa ficam dentro do lote), e é por isso que o nicho do padrão e o acesso disputam a mesma faixa do muro. Prever os dois juntos desde o Estudo Preliminar.

## 5. MACETES DE QUEM FAZ

Fonte única desta rodada: o **vídeo oficial da própria Light** (concessionária, não profissional independente — macete tipo B).
- "Se o técnico não achar a numeração da sua casa, você será cobrado por uma nova visita" (Light, vídeo, ~5:20). Em obra nova, **placa de número provisória visível** antes de pedir a vistoria.
- A primeira vistoria é gratuita; a segunda, não. **Conferir o padrão contra a RECON-BT antes de pedir**, não depois de reprovar.
- Pedido pelos canais digitais (WhatsApp, agência virtual, app Light Cliente).

Nenhum macete de eletricista ou engenheiro independente com fonte foi achado nas buscas desta rodada.

## 6. CHECKLIST DO LANDELL

- [ ] Carga instalada total (kW) — passou de 75 kW? → MT/subestação, avisar Cardozo
- [ ] Carga ou geração acima de 50 kW? → risco de Grupo A por estudo da Light (REN 1000 art. 23 §1º), pedir viabilidade
- [ ] Demanda acima de 38 kVA? → medidas do vídeo não valem, usar Fascículo 07 da RECON-BT
- [ ] Carga demandada (kVA) → faixa mono/bi/tri
- [ ] Demanda > 15 kVA? → ART/RRT/TRT do instalador
- [ ] Rede aérea ou subterrânea na testada? (consultar a Light)
- [ ] Poste da Light na mesma calçada ou do outro lado? (levantamento cadastral do Oscar)
- [ ] Ramal > 30 m ou demanda > 24 kVA? → pedido com estudo, prazo maior
- [ ] Cliente pode querer solar ou carro elétrico? → entrada dimensionada para isso
- [ ] Ligação provisória de obra pedida à parte (< 24 kW sem estudo)

## 7. RELAÇÃO COM OUTRAS SKILLS

- `nbr5410-eletrica-automacao` — **Complementa.** A 5410 trata da instalação **depois do medidor**; esta trata da **entrada até o medidor** e das regras da Light. A NBR 5410 continua sendo a regra da instalação interna (DR, DPS, condutores); aqui não há valor de condutor nem de disjuntor interno.
- `legal-art-crea-responsabilidade-tecnica-rj` — **Diferente.** Ela trata da ART de engenheiro terceirizado no Projeto Legal. Aqui a ART/RRT/TRT é a do **instalador do padrão**, exigida pela Light acima de 15 kVA.
- `automacao-residencial-tendencias` — **Complementa.** Ela traz solar e bateria como tendência; aqui está a trava da Light (microgeração limitada à potência disponibilizada). Sem conflito de valor.
- `nbr14565-2019-cabeamento-estruturado-automacao-residencial` — **Diferente.** Trata da entrada de sinal/telecom (DG); aqui, da entrada de energia. Mesma fronteira: Landell não assina ART/RRT. Sem conflito de valor.
- Aterramento: o vídeo manda ligar o neutro à haste no padrão. Isso é coerente com a `nbr5410-eletrica-automacao` (separação do PEN na entrada, TN-S dali para dentro, 5.4.3.6). Não há contradição.
- `levantamento-topografico-cadastral-orientado-duli-licin-rj` (ainda proposta, em `Skills_Propostas/2026/Outubro/`) — **Complementa.** O levantamento cadastral traz a posição do poste da Light, que define a altura do poste do padrão.

## 8. RESSALVAS ABERTAS (dono)

- **R1 (Landell):** ler a RECON-BT 2024 (Fascículo 07 e cálculo de demanda) — baixar manualmente do site da Light.
- **R2 (Landell):** carga instalada × demandada no limite de 75 kW — confirmar na RECON-BT/REN 1000.
- **R3 (Landell/Oscar):** mapa de rede aérea × subterrânea na Barra/Recreio.

## FONTES

- Light S.A. — FAQ para Solicitações Técnicas (Ligação Nova): https://www.light.com.br/Downloads/Liga%C3%A7%C3%A3o%20Nova/LIGACAO_NOVA_INFORMACOES.pdf (lido em 05/10/2026)
- Light S.A. — vídeo "padrão de ligação até 38 kVA": https://youtu.be/2RG3FdAizUQ (assistido via /watch em 05/10/2026; transcrição Whisper/Groq + 15 quadros)
- COE LC 198/2019, Art. 35 — acervo `D:\008_Normas ABNT\002_Prefeitura_RJ\`
