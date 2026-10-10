---
name: nbr14565-2019-cabeamento-estruturado-automacao-residencial
description: NBR 14565:2019 (cabeamento estruturado, comercial) como complemento da NBR 16264 (residencial) para a infraestrutura física de automação residencial de alto padrão — hierarquia DG/DA/TO, cabos por aplicação (Cat6A, KNX, coaxial, som, CFTV), dimensionamento de rack (incl. NVR/DVR), pré-conduit e interface com a NBR 5410. Use sempre que Landell (ou qualquer Agente) for planejar rack, sala técnica, eletrodutos de sinal, pontos de rede/TV/KNX por ambiente ou CFTV — mesmo que o pedido só mencione "rede", "rack", "cabeamento", "home theater" ou "pré-conduit", sem citar a norma pelo nome.
version: v1.3
fonte_primaria_lida: sim (NBR 16415:2015 itens 1, 6.1.1, 6.1.5, 7.2.2, 7.6.1.3.2, 7.6.2.1.4, 7.6.2.2.3 e Anexo B; NBR 5410:2004 item 6.2.9.5 — PDFs em D:\008_Normas ABNT) — NBR 14565 e NBR 16264 continuam não lidas
status: ativa-com-ressalva
data: 2026-09-23
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_principal: Landell (Automação+Elétrica)
agentes_cross: Oscar (infraestrutura em planta — eletrodutos, shafts), Baumgart (dimensionamento de shaft técnico, rack)
---

# Skill: NBR 14565:2019 — Cabeamento Estruturado como Base para Automação Residencial de Alto Padrão

## 1. POR QUE ESSA SKILL EXISTE

A lacuna mais cara em projetos residenciais de alto padrão em Barra/Recreio é a **ausência de infraestrutura física de cabeamento** planejada antes da alvenaria. O resultado: condominios que têm NBR 5410 correto (circuitos elétricos) e automação residencial instalada (KNX, Lutron, HomeKit), mas sem os **eletrodutos, passantes e patch panels** dimensionados para suportar o sistema.

A NBR 14565:2019 é a norma de **cabeamento estruturado** (originalmente comercial), mas é exatamente o padrão que profissionais experientes em residencial de alto padrão adotam — porque é a única referência técnica rigorosa disponível para estruturar a infraestrutura física de dados, AV e automação em um projeto.

**Relação com as demais Skills de Landell:**
- `nbr5410-eletrica-automacao` → circuitos elétricos, DPS, demanda, carga (camada de força)
- `automacao-residencial-tendencias` → protocolos e fabricantes (KNX, Z-Wave, Matter, Lutron)
- **Esta skill** → infraestrutura física (eletrodutos, cabos, racks, patch panels) que conecta os dois

---

## 2. O QUE É A NBR 14565:2019

**ABNT NBR 14565:2019 — Cabeamento estruturado para edifícios comerciais**

Apesar do título "comercial", é o padrão adotado por profissionais de alto padrão residencial porque:
- Define hierarquia clara de backbone → horizontal → área de trabalho
- Especifica distâncias máximas de cabo por categoria
- Define o dimensionamento de salas técnicas, DG (Distribuidor Geral) e racks
- Cobre Cat5e, Cat6, Cat6A (dados), par trançado para automação, coaxial para TV

**Normas relacionadas:**
| Norma | Escopo |
|-------|--------|
| ABNT NBR 14565:2019 | Cabeamento estruturado (infraestrutura física) |
| ABNT NBR 16264 (ed. 2016) | Cabeamento estruturado **residencial** (TIC + broadcast + automação residencial) — referência primária para residência; ver Avaliação do Gestor |
| ABNT NBR 16415:2015 (1ª ed. 06/08/2015, válida desde 06/09/2015) — **lida** | Caminhos e espaços para cabeamento estruturado conforme a NBR 14565, em edifícios monousuário e multiusuário (item 1). Exige compartimento dedicado, sem compartilhar infraestrutura com cabos elétricos (6.1.1). **Não dá distância de separação sinal/força**: segurança elétrica, incêndio e compatibilidade eletromagnética estão fora do escopo (item 1). Ver §6 |
| ABNT NBR 16665:2019 | Cabeamento estruturado para data centers (corrigido pelo Gestor; a versão original citava "NBR 16065:2012", número incorreto) |
| ISO/IEC 11801:2017 | Equivalente internacional (referência premium) |
| ABNT NBR 5410:2004 | Instalações elétricas de baixa tensão (camada de força) |

---

## 3. HIERARQUIA DE CABEAMENTO RESIDENCIAL (ADAPTADO DA NBR 14565)

```
DG (Distribuidor Geral) — rack principal, entrada de operadoras
    └─ Backbone horizontal → DAs (Distribuidores de Andar)
             └─ Cabeamento horizontal → TOs (Tomadas de Telecomunicações)
```

| Nível | Equivalente residencial | Componente |
|-------|------------------------|-----------|
| DG | Central técnica / rack | Patch panel, switch, roteadores, homologação |
| DA | Rack de andar ou sala | Patch panel secundário, switch por pavimento |
| TO | Tomada de rede/AV | Outlet RJ-45, outlet HDMI, saída KNX |

**Regra de ouro:** planejar a localização do DG, dos DAs e de cada TO **antes do projeto estrutural fechado** — o eletroduto precisa passar na laje ou na parede, e depois da alvenaria o custo de retrofit é proibitivo.

---

## 4. CABEAMENTO POR APLICAÇÃO — O QUE ESPECIFICAR

| Aplicação | Cabo recomendado | Padrão |
|-----------|-----------------|--------|
| Rede de dados / Wi-Fi AP | Cat6A U/FTP | ISO/IEC 11801 Class EA |
| Automação KNX cabeada | Cabo KNX TP (verde) 2×2×0,8 mm (0,8 = diâmetro do condutor, não mm²) | EN 50090-2-2 |
| TV por satélite / antena | RG-6 quad-shield | ABNT NBR 5281 |
| Sistema de som distribuído | 2×1,5 mm² flexível | Especificação fabricante |
| CFTV / câmeras IP | Cat6A ou cabo coaxial RG-59 | Depende da câmera (IP vs. analógica) |
| Controle de acesso / interfone | Par trançado 4×0,5 mm² | Especificação fabricante |
| Alarme / sensores | 4×0,5 mm² blindado | NBR 11785 |

> **Para projetos KNX:** o cabo KNX TP (verde) é dedicado e NUNCA dividido com outros sistemas. Distância máxima por segmento: 1.000 m (TP1). Pode ser roteado junto a outros cabos de sinal (NÃO junto a 220V — coerente com NBR 16415 6.1.1 e NBR 5410 6.2.9.5; ver §6).

---

## 5. DIMENSIONAMENTO DE RACK E SALA TÉCNICA

### Rack residencial (projeto típico 200–500 m²)
- **Rack de 15–20 Us** para residências médias
- **Rack de 20–30 Us** para residências com home theater, automação completa, CFTV
- Regra: calcular Us ocupados pelos equipamentos e acrescentar 30–40% de reserva

### O que vai no rack
| Equipamento | Us típico |
|-------------|----------|
| Patch panel Cat6A 24 portas | 1U |
| Switch gerenciado 24p | 1U |
| Roteador / firewall | 1U |
| Interface KNX (IP Gateway) | 0,5U ou DIN |
| Amplificador de som distribuído | 2U |
| UPS (no-break) | 2–3U |
| Gravador de CFTV (NVR/DVR) | a confirmar (depende do modelo) |
| Organizador de cabos | 1U por patch panel |

### Localização do rack
- Preferencialmente em armário embutido, área de serviço ou closet técnico
- Ventilação mínima: 2 grelhas de 150×150 mm ou ventilador forçado se rack > 10Us com equipamentos ativos
- Distância máxima do rack ao ponto mais distante: **90 m** (limite da NBR 14565 para cabeamento horizontal)

---

## 6. ELETRODUTOS DE PRÉ-CONDUIT (BOAS PRÁTICAS)

O investimento mais barato e mais valioso em residencial de alto padrão: instalar **eletrodutos vazios** (pré-conduit) antes da alvenaria, dimensionados para os cabos especificados.

| Situação | Eletroduto recomendado |
|----------|----------------------|
| Trecho vertical (shaft) | PVC rígido Ø 50 ou 75 mm (permite passar múltiplos cabos) |
| Trecho horizontal em laje | PVC corrugado Ø 25 mm por ponto (Cat6A) + Ø 20 mm (KNX) |
| Do rack aos pontos do mesmo andar | PVC corrugado Ø 32–40 mm (tubulação de percurso) |
| Externo / intempéries | PVC rígido com luvas de vedação |

**Separação sinal/força — o que a norma confirma (lida em 29/09/2026):**
- **Confirmado, NBR 16415:2015 item 6.1.1:** o cabeamento estruturado deve ficar em compartimentos (eletrodutos, eletrocalhas etc.) dedicados a ele e **não pode usar a mesma infraestrutura de distribuição que os cabos elétricos**. Pode ser citado em memorial.
- **Confirmado, NBR 16415 6.1.1:** shaft compartilhado com cabos elétricos é admitido, desde que atenda às IEC 60364-4-41, 60364-4-44 e 60364-5-52. Para reduzir interferência, a norma **recomenda** (não exige) caminhos separados, barreiras na infraestrutura e separação dentro de caixas que terminem os dois sistemas. A separação deve ser mantida ao longo de todo o caminho.
- **Confirmado, NBR 5410:2004 item 6.2.9.5:** circuitos de faixa I e de faixa II (anexo A) não compartilham a mesma linha, a menos que todos os condutores sejam isolados para a tensão mais alta, que fiquem em compartimentos separados do conduto ou que se usem eletrodutos separados.
- **A confirmar — distância mínima sinal/força:** nenhuma das duas normas dá distância em cm. A 16415 deixa EMC fora do escopo (item 1). A NBR 5410 6.2.9.5 (nota) remete a 5.4 e 6.4, e 5.4.3.5 f) pede "separação adequada, por distanciamento ou blindagem" e cruzamento em ângulo reto, também sem número. Não inventar valor.
- **Corrigido:** a exceção "salvo divisória metálica" da v1.2 não aparece nessas palavras. O texto real é "compartimentos separados do conduto" (5410 6.2.9.5 a)) e "barreiras" como recomendação (16415 6.1.1). Não exige que a divisória seja metálica.
- **Atribuição:** a vedação vem da NBR 16415 (6.1.1) e da NBR 5410 (6.2.9.5), não da NBR 14565, que segue não lida.

**Laje — ressalva lida:** a NBR 16415 6.1.5 diz que eletrodutos embutidos no piso (cobertos por concreto) em geral não oferecem a flexibilidade do cabeamento estruturado e devem ser evitados. Esse texto foi pensado para leiaute de escritório (6.1.5 b), d)). A linha "trecho horizontal em laje" da tabela acima segue válida para residência, que tem leiaute fixo, mas é **escolha de projeto, não recomendação da norma**. Onde passar pela laje, terminar o eletroduto a pelo menos 50 mm acima do piso acabado (7.6.2.2.3).

**Ocupação dos eletrodutos da tabela:** pela Tabela B.1 (Anexo B, informativo, 40 %), cabem 4 cabos Cat6A U/UTP (Ø 8,6 mm) em 1" (25,4 mm) e 2 em 3/4" (19 mm). O "Ø 25 mm" da tabela precisa ser o **diâmetro interno**; corrugado comercial "25" pode ter interno menor (a confirmar no catálogo).

### Macetes de quem faz (só onde a norma deixa escolha ao projetista; fonte = texto lido)

1. **Folga de ocupação: projetar a 40 % e parar em 60 %.** NBR 16415 7.6.2.1.4: o eletroduto é dimensionado para 40 % e considerado "cheio" aos 60 %. Cabo novo depois disso só entra se os cabos já instalados forem retirados. Escolha mais econômica: subir uma bitola já no projeto quando a conta der perto de 40 %. A diferença de custo de um tubo maior na obra é pequena; a alternativa, pelo próprio texto, é arrancar os cabos existentes para passar o novo.
2. **Eletroduto de reserva vs. tubo único maior.** NBR 16415 7.6.1.3.2 recomenda planejar o caminho para a capacidade máxima, por **estruturas com capacidade para crescimento ou por espaço para caminhos adicionais no futuro**. A norma deixa as duas opções. Mais barata e sem retrabalho em residência: um eletroduto vazio de reserva com guia, no mesmo trajeto do rack ao ponto. Ele não disputa a ocupação de 40 % do tubo em uso, e ampliar depois não mexe no cabeamento que já funciona (conclusão tirada de 7.6.2.1.4).
3. **Trecho reto longo, curvas contadas.** NBR 16415 7.6.2.1.4: sem curvas, até 70 m entre pontos de acesso; com curvas, no máximo 2 curvas de até 90° e 15 m entre pontos de acesso. Escolha econômica: traçar os trechos retos (shaft, prumada) sem curva, o que dispensa caixas de passagem intermediárias. Quando a curva for inevitável, concentrá-las perto das caixas. Curva em "U" (180°) é proibida, e a conversão exige caixa (6.1.5).
4. **Separação sinal/força: eletroduto separado ou compartimento separado.** A NBR 5410 6.2.9.5 aceita três caminhos: isolar tudo para a tensão mais alta, compartimentos separados do mesmo conduto ou eletrodutos separados. A NBR 16415 6.1.1 exige infraestrutura dedicada. Para o trecho **embutido**, o eletroduto separado atende as duas normas sem depender de especificar cabo de sinal com isolação de 450/750 V. Para trecho **aparente** (canaleta/eletrocalha), uma canaleta de múltiplos compartimentos (16415 Tabela 1: "único ou múltiplos compartimentos") atende 5410 6.2.9.5 a) com uma peça só. Não há distância mínima em norma lida; ver §6.
5. **Tubo que atravessa laje sai 50 mm acima do piso acabado.** NBR 16415 7.6.2.2.3 (nota): a sobra evita que o concreto obstrua o tubo durante a concretagem e protege contra água. Custo zero no projeto; evita desentupir ou refazer o trecho depois da laje pronta.

Fora destes, nenhum macete entra sem fonte lida.

---

## 7. INTERFACE COM O PROJETO ELÉTRICO (NBR 5410)

A NBR 14565 e a NBR 5410 atuam em camadas distintas mas precisam ser coordenadas desde o briefing:

| NBR 5410 (Landell — camada de força) | NBR 14565 (Landell — camada de sinal) |
|--------------------------------------|---------------------------------------|
| Quadro de distribuição, disjuntores, DPS | Rack, patch panels, switches |
| Tomadas 2P+T (NBR 14136) | Tomadas RJ-45, HDMI, coaxial |
| Circuitos dedicados (ar, forno, etc.) | Circuito dedicado para rack (recomendado: 20A exclusivo) |
| Fiação em eletrodutos separados | Cabeamento em eletrodutos de sinal |

**Atenção ao circuito do rack:** o rack concentra equipamentos críticos (roteador, servidor, automação). Prever circuito **dedicado** de 20A para o rack principal, com tomada de 20A + filtro de linha ou no-break no próprio rack.

**Aterramento do rack:** o gabinete metálico do rack deve receber cabo de aterramento dedicado (verde-amarelo, seção conforme NBR 5410 Tabela 58 — para fase até 16 mm², o condutor de proteção tem a mesma seção da fase; ex.: circuito de 20A em 2,5 mm² → PE 2,5 mm². Corrigido pelo Gestor em 23/09: a versão anterior citava "Tabela 54F / usualmente 4 mm²", referência inexistente). Coordenar com o projeto elétrico: o ponto de aterramento do rack não é o mesmo que o neutro do circuito de força.

---

## 8. PONTOS MÍNIMOS POR AMBIENTE (REFERÊNCIA PARA BRIEFING)

| Ambiente | Dados (Cat6A) | TV/Coaxial | KNX pontos | Obs. |
|----------|--------------|------------|-----------|------|
| Sala de estar | 2–4 | 1 | 2–4 (luz + persiana) | + 1 se home theater |
| Sala de jantar | 1–2 | — | 1–2 | |
| Dormitório master | 2 | 1 | 2–3 | |
| Dormitório comum | 1–2 | 1 | 1–2 | |
| Cozinha | 1–2 | — | 1–2 (luz + cortina) | |
| Home office | 3–4 | — | 1–2 | Switch local se > 2 devices |
| Área externa / varanda | 1 (IP67) | 1 | 1–2 | Caixas externas IP65 |
| Hall / circulação | — | — | 1–2 (luz) | Sensores de presença |

---

## 9. QUANDO ACIONAR ESTA SKILL

Landell consulta esta Skill sempre que o briefing mencionar:
- Automação KNX, Lutron, Crestron, Control4 ou similar
- Home theater, som distribuído ou CFTV
- "Smart home" de qualquer protocolo
- Projeto de alto padrão (acima de R$ 8.000/m² de construção, como estimativa de escopo)
- Cliente que solicita "futuro" para automação (pré-conduit)

---

## 10. RESSALVAS

1. **[Corrigida pelo Gestor em 23/09/2026]** A NBR 14565:2019 é norma comercial. A versão original afirmava que "não há norma ABNT residencial equivalente" — **falso**: existe a ABNT NBR 16264 (Cabeamento estruturado residencial, ed. 2016, baseada na ISO/IEC 15018 e alinhada à ISO/IEC 11801-4), que cobre TIC, broadcast e automação residencial. Para residência, a 16264 é a referência primária; a 14565 entra só como complemento (backbone, distâncias, categorias). Nenhuma das duas é exigência legal para residência unifamiliar — são referência técnica.
2. Parâmetros KNX seguem EN 50090 (norma europeia) — não há equivalente ABNT. A certificação KNX é feita pela associação KNX Brasil.
3. **[Corrigida pelo Gestor em 23/09/2026]** Projeto elétrico (NBR 5410) e projeto de cabeamento estruturado são **documentos separados**. Landell **prepara** os dois, mas **não assina**: ART/RRT exige profissional habilitado (engenheiro eletricista/CREA ou arquiteto/CAU com atribuição). A versão original dizia "ambos assinados por Landell" — fronteira errada.
4. O gatilho de "R$ 8.000/m² de construção" (Seção 9) é referência de mercado indicativa de escopo, não critério normativo. Em Barra/Recreio 2026, projetos acima desse valor ainda podem não incluir automação completa, e projetos abaixo podem tê-la por exigência do cliente. Landell deve usar o gatilho como orientação de briefing, não como regra de contratação.
5. **[Número NÃO confirmado em fonte — verificar antes de citar em memorial]** A ABNT NBR 14159 (Instalações prediais — sistemas privados de telecomunicações) não é citada nesta Skill, mas é a referência usada por operadoras para dimensionar a entrada de fibra óptica no DG. Em projetos que especificam entrada de fibra óptica GPON/XGS-PON, Landell deve verificar a NBR 14159 para dimensionar a sala técnica de entrada — limitar-se à NBR 14565 pode subestimar o espaço físico necessário.

---

## Avaliação do Gestor (Cardozo, 23/09/2026)

Veredito: **PROCEDE COM RESSALVA**. Não é ratificação de Claudemberg. Correções aplicadas: NBR 16264 (residencial) existe e é a referência primária; data center = NBR 16665:2019 (não 16065); cabo KNX 0,8 mm de diâmetro; PE do rack pela Tabela 58 da NBR 5410 (mesma seção da fase); Landell não assina ART/RRT. Não confirmados: NBR 5281, NBR 11785, NBR 14159 e a atribuição da separação sinal/força à 14565. Avaliação completa no arquivo-fonte em `01_CEO/Skills_Propostas/2026/Setembro/`.

---

## Histórico de versões

- **v1.0 — 23/09/2026:** versão proposta por Landell, corrigida e avaliada por Cardozo (procede com ressalva).
- **v1.1 — 28/09/2026 — correções do treino aprovadas por Claudemberg:** (1) §6: separação sinal/força marcada "a confirmar (norma candidata: NBR 16415)", deixa de ser atribuída como fato à NBR 14565; (2) frontmatter: `name:` alinhado ao nome da pasta e `description:` incluída; (3) §5: linha do gravador de CFTV (NVR/DVR) incluída na tabela do rack, espaço em U "a confirmar (depende do modelo)". Registro do treino: `01_CEO/Gestores/Cardozo (Complementares)/Casos_TESTE/treino_skills/2026-09-28_nbr14565-2019-cabeamento-estruturado-automacao-residencial.md`.
- **v1.2 — 28/09/2026 — coerência aprovada por Claudemberg:** §2, tabela de normas: NBR 16415 marcada "a confirmar (ano e escopo não verificados)", coerente com a §6 (antes aparecia como "NBR 16415:2021" sem marca).
- **v1.3 — 29/09/2026 — fonte primária lida (PDFs reais em `D:\008_Normas ABNT`), pedido de Claudemberg via Wallenberg/Cardozo:** (1) NBR 16415 confirmada como **2015** (não 2021) e escopo lido (item 1); a EMC fica fora do escopo. (2) §6: vedação de infraestrutura compartilhada confirmada (16415 6.1.1 + 5410 6.2.9.5). A distância sinal/força segue "a confirmar", porque nenhuma das duas dá número. A "divisória metálica" foi corrigida para "compartimento separado", que é o texto real. (3) Ressalva sobre eletroduto em laje (16415 6.1.5) e terminação a 50 mm (7.6.2.2.3). (4) Ocupação Cat6A por Tabela B.1. (5) Seção "Macetes de quem faz" com 5 itens, cada um com o item da norma. Não lidas ainda: NBR 14565, 16264, 5281, 11785, 14159 e o limite de 90 m. Backup em `01_CEO/Decisoes_Autonomas/_backups/2026-09-29/`.
