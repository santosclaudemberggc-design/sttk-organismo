# Partido Arquitetônico e Conforto Térmico Passivo — Orientação Solar, Ventilação e Tipologias no RJ

**Versão:** 1.0  
**Status:** avaliada — PROCEDE COM RESSALVA  
**Data:** 16/09/2026  
**Tipo:** Inteligência (Trilha A)  
**Para:** Lúcio/Oscar (Arquitetura, principal) — cross: Tenreiro (Interiores), Baumgart (Estrutural)  
**Gestor:** Lúcio (Arquitetura)  
**Avaliação (16/09/2026):** Orientação solar/ventilação/tipologias mapeadas para RJ, aplicáveis a Levantamento/EP/Anteprojeto. Ressalvas: (1) beiral 0,80–1,0m sem fonte citada (usar SOL-AR conforme texto); (2) LC 299/2026 não verificada por Lúcio (confirmar com Kelsen se questionada); (3) ruído urbano × ventilação implícito (escalar se rua ruidosa). Baixa prioridade — não bloqueiam execução.

---

## O que é

Repertório técnico de estratégias de conforto térmico passivo para projetos residenciais no Rio de Janeiro — orientação solar por fachada, ventilação cruzada, tipologias para lotes cariocas e zoneamento de programa. Estas estratégias devem ser incorporadas desde o Estudo Preliminar, não como adaptações posteriores.

**Nota normativa:** a Zona Bioclimática do Rio de Janeiro é **ZB 8** conforme NBR 15220-3:2005 (ainda a versão em vigor para fins de parâmetros construtivos), mas a nova edição 2024 reclassificou o RJ para **ZB 4A**. Ver Skill `complementares_nbr15220-3-2024-reclassificacao-bioclimatica-rj.md` para os parâmetros específicos da reclassificação. Esta Skill trata de estratégias passivas válidas para o clima carioca independentemente do rótulo de zona.

---

## Ventos dominantes no Rio de Janeiro

O RJ opera sob sistema de **brisa marítima-terrestre** modulado pela topografia (serra, baía, oceano). Não há um único vetor para toda a cidade — a direção varia por zona:

| Zona | Direção predominante | Observação |
|------|---------------------|-----------|
| Zona Norte (Méier, Tijuca, Ramos) | NE manhã, SW tarde | Brisa terrestre-marítima cíclica |
| Centro / Zona Sul (Botafogo, Flamengo, Copacabana) | SE/L predominantes | Influência oceânica mais direta |
| Zona Oeste (Santa Cruz, Sepetiba) | SW e NE | Velocidade maior (~18 nós/33 km/h) |
| Jacarepaguá / Barra | N-S ou S/SW-NE | Influência da Lagoa e da Serra |

**Ciclo diário:** madrugada/manhã = brisa terrestre (NE/N); tarde/noite = brisa marítima (SW/SE). A sazonalidade afeta temperatura e umidade, não a direção predominante — o padrão de brisa é estável o ano todo.

**Regra prática:** o arquiteto deve consultar a rosa dos ventos do INMET para o bairro específico antes de definir a fachada de captação. Lotes diferentes a 500 m de distância podem ter comportamentos distintos pelo efeito da topografia.

Fontes: [Scielo — Regime de ventos na RMRJ](https://www.scielo.br/j/esa/a/vwHXKmDBVyWgrr7vCDxcJ4d/?lang=pt&format=html) | [INMET — Direção Predominante NCB 1961-1990](https://portal.inmet.gov.br/uploads/normais/Vento-Direcao-Predominante_NCB_1961-1990.xls)

---

## Ventilação cruzada — parâmetros técnicos

### Área mínima de abertura

| Referência | Exigência |
|-----------|----------|
| NBR 15220-3 (ZB 8) | Abertura ≥ **15% da área de piso** do compartimento |
| LC 198/2019 (Código de Obras RJ) | Ventilação ≥ **1/15 da área de piso** (6,67%) |
| RTQ-R (Regulamento Técnico Qualidade Residencial) | Fórmula A2/A1 ≥ **0,25** (soma das demais fachadas ≥ 25% da maior fachada) |

A NBR 15220-3 e o RTQ-R são mais exigentes que o Código de Obras. Em projetos de qualidade, usar a referência mais exigente.

### Proporção entrada/saída

- Abertura de **saída deve ser 10 a 25% maior** que a de entrada — cria efeito Venturi e acelera o fluxo interno
- Corredores internos de áreas comuns **não podem ser contabilizados** como abertura de ventilação cruzada (RTQ-R)

### Como posicionar as aberturas

- Abertura de **entrada**: voltada para barlavento (pressão positiva — fachada que recebe o vento)
- Abertura de **saída**: voltada para sotavento (pressão negativa — fachada oposta ou perpendicular)
- **Solução para lotes com única fachada livre:** pátio interno, recuo lateral ou abertura zenital na cobertura funcionam como saída de ar quente

### Varanda como câmara de transição

A varanda cumpre três funções bioclimáticas simultâneas:
1. **Amortece a variação de pressão e temperatura** entre rua e interior
2. **Protege a esquadria de chuvas tropicais** — permite que ela permaneça aberta durante chuva
3. **Sombreia a abertura principal** — reduz carga térmica direta na fachada

Parâmetros legais (Decreto Municipal 7336/1988 e LC 198/2019):
- Projeção máxima: **2 metros**
- Área máxima: **20% da área útil** da unidade (não computa no CA)

Eficácia depende de esquadria interna **operável** (máximo ar, guilhotina, pivotante) — varanda com esquadria fixa de correr com dois folhos não garante ventilação cruzada real.

### Pé-direito e efeito chaminé

- Pé-direito alto (≥ 2,80 m no térreo, ≥ 3,0 m no social) potencializa o efeito chaminé
- **Lanternins e domus na cobertura** extraem o ar quente acumulado no topo — complementam a ventilação cruzada horizontal
- Pé-direito duplo no social com caixilho operável no topo é a solução mais eficaz para lotes de uma só fachada

Fontes: [LC 198/2019 — Código de Obras RJ](https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/c1982019.html) | [PBE Edifica — RTQ-R ventilação cruzada](https://pbeedifica.com.br/forum/viewtopic.php?t=1385) | [Vitruvius — A varanda na Cidade Maravilhosa](https://vitruvius.com.br/revistas/read/arquitextos/13.147/4457)

---

## Orientação solar por fachada — latitude ~22-23°S

| Fachada | Verão (dez–mar) | Inverno (jun–ago) | Brise recomendado |
|---------|----------------|------------------|------------------|
| **Norte** | Sol alto (previsível, ângulo >= 67°) | Sol baixo (~44° máximo), valioso para conforto | **Horizontal** — intercepta ângulo alto |
| **Sul** | Quase sem sol direto, luz difusa | Sem insolação direta | Dispensável — valorizar luz difusa |
| **Leste** | Sol da manhã (baixo), temperatura amena | Sol baixo manhã, temperatura ainda fria | **Combinado** (vertical + horizontal) |
| **Oeste** | Sol da tarde, ângulo baixo com acúmulo térmico do dia | Menos intenso | **Vertical** — único que intercepta ângulo < 30° |

**Fachada mais crítica no RJ: OESTE.** A fachada poente recebe sol quando o ar externo já acumulou calor ao longo do dia. Em apartamentos de andar alto, a carga térmica oeste no horário 12h–18h é a principal causa de desconforto. Brise horizontal **não funciona** na fachada oeste — o sol entra com ângulo ≤ 30° nas últimas horas; somente brise vertical ou vegetação densa controlam efetivamente.

### Dimensionamento de brises — ferramenta

- **SOL-AR** (LABEEE/UFSC, software gratuito): gera automaticamente os ângulos alfa/beta/gama por latitude e orientação — usar antes de especificar qualquer brise
- **Ângulo alfa (α):** altura solar vertical → dimensiona profundidade do brise horizontal
- **Ângulo beta (β):** azimute relativo à normal da fachada → dimensiona profundidade do brise vertical
- Para fachada norte em lat. 23°S: beiral de **0,80–1,0 m** consegue proteger do sol direto no verão mantendo ganho solar no inverno

Fontes: [Gelker Ribeiro Arquiteto — Orientação Solar](https://gelkerribeiro.com.br/orientacao-solar/) | [Refax — Critérios técnicos de brise](https://refax.com.br/blog/brise-horizontal-vertical-ou-combinado-criterios-tecnicos-de-especificacao/) | [LABEEE/UFSC — Aula Orientação e Diagrama Solar](https://labeee.ufsc.br/sites/default/files/disciplinas/Aula-Orientacao%20e%20Diagrama%20solar.pdf)

---

## Zoneamento de programa por orientação

| Orientação | Características climáticas | Ambientes recomendados |
|-----------|--------------------------|----------------------|
| **Norte** | Sol previsível, brise horizontal funciona | Dormitórios principais, sala de estar, varanda de convívio |
| **Leste** | Sol da manhã, temperatura amena | Dormitórios (despertar com luz suave), área de café da manhã |
| **Sul** | Luz difusa o ano todo, sem sobrecarga | Serviço, garagem, depósito, circulações, banheiros de serviço |
| **Oeste** | Sobrecarga térmica à tarde | Evitar dormitórios e salas. Banheiros ou ambientes de uso curto apenas |

**Cozinha:** gera calor interno próprio (cooktop, forno) — posicionar com ventilação permanente garantida, preferencialmente com abertura sul ou leste para não somar calor externo ao interno.

**Banheiros internos** (sem janela): aceitar ventilação mecânica (NBR 7195 e Código de Obras) ou iluminação zenital tubular em lotes estreitos geminados onde abertura externa é impossível.

---

## Tipologias para lotes cariocas

### Lote estreito (frente 5–8 m, profundidade 20–30 m)

**Desafio:** lotes coloniais urbanos típicos do Rio — geminados em uma ou duas laterais, ventilação cruzada frontal-fundos impossível sem solução especial.

**Partido longitudinal com pátio central ("pulmão"):**
- Pátio ou recuo a 1/3 ou 1/2 da profundidade divide em bloco frontal + bloco posterior
- Área mínima funcional do pátio: **2,0 m de largura** × comprimento livre
- Permite ventilação cruzada perpendicular à frente + iluminação natural dos cômodos internos
- Sem pátio central, a solução é abertura zenital (domus/claraboia) na cobertura como saída do ar

**Distribuição por piso (regra geral):**
- Térreo: programa social integrado (sala/jantar/cozinha sem paredes internas não-estruturais) — planta livre maximiza largura útil real
- Superior: zona íntima (dormitórios + banheiros)
- Escada em eixo lateral para liberar a largura central

**Iluminação zenital obrigatória:**
- Claraboias tubulares em banheiros, corredores e closets sem janela lateral
- Domus fixo ou operável na escada = exaustor de ar quente pelo efeito chaminé

### Lote de esquina

**Vantagem:** duas fachadas livres = ventilação cruzada em duas direções independentes.

Posicionar entrada de ar na fachada que captura o vento predominante (NE ou SE no RJ conforme bairro) e saída na fachada perpendicular. O recuo de esquina obrigatório cria ângulo de captação extra — o fluxo encontra menos obstáculos do que em lote de meio de quadra.

### Cobertura em edifício (duplex/cobertura)

**Desafio:** maior exposição solar direta — laje de cobertura sem pavimento acima pode atingir 60–70°C no verão carioca.

Estratégias:
- **Telhado verde extensivo** (substrato 8–15 cm, sedum/grama/bromélias, ~100–150 kg/m²): temperatura da laje cai para ~30–35°C. Não computa como pavimento no gabarito (LC 198/2019). LC 299/2026 (cobertura verde como "solução baseada na natureza") incentiva o instrumento.
- **Pé-direito duplo no social** com lanternin ou caixilho operável no topo → efeito chaminé
- **Orientação do terraço:** sul ou leste para área de refeições (fresco); leste ou norte para jardim

### Fundo de vila / geminado

- Lote encravado com única frente para a passagem interna
- Solução: abertura na fachada da vila (entrada) + abertura zenital na cobertura (saída por efeito chaminé)
- Quando afastamento regulamentar permitir: pátio descoberto lateral ou nos fundos

### Cobogó — brise + ventilação simultâneos

Elemento vazado modular desenvolvido para o clima tropical brasileiro (anos 1920–30). Filtra incidência solar direta + mantém fluxo de ar permanente:
- **Melhor uso:** fachadas leste e oeste, onde o ângulo baixo do sol inviabiliza brise fixo horizontal convencional
- **Limitação:** não oferece controle acústico (o ar e o som passam juntos)
- **Sem normalização ABNT específica:** dimensionamento por projeto (carta solar + RTQ-R)

Fonte: [SustentArqui — Cobogó na Arquitetura Bioclimática](https://sustentarqui.com.br/o-uso-do-cobogo-na-arquitetura-bioclimatica/)

---

## Brecha válida (mentalidade v3.0)

A maioria dos projetos no RJ trata o conforto térmico como custo (ar-condicionado, insulfilm). O profissional experiente percebe que:

1. **Orientação correta não custa nada** — mas decide na largura do corredor, na posição da escada e no zoneamento do programa. Corrigir depois é caro ou impossível.

2. **Varanda com 2 m de projeção não computa no CA** mas resolve o problema de ventilação e de privacidade. Em lotes onde cada m² de CA é disputado, a varanda bioclimática é "área gratuita".

3. **Telhado verde não computa como pavimento no gabarito** mas reduz em ~35°C a temperatura da laje abaixo — elimina a necessidade de ar-condicionado no dormitório da cobertura.

4. **Cobogó na fachada oeste** é mais eficaz e mais barato do que qualquer brise metálico articulado — e está na tradição da arquitetura moderna carioca (Niemeyer, Paulo Casé).

5. **Lote estreito com pátio central** que parece "sacrificar área" geralmente tem menor índice de desconforto e maior valor de locação que o lote totalmente construído sem ventilação cruzada.

---

## Impacto no fluxo STTK

### Para Lúcio/Oscar (Arquitetura)

- **Levantamento:** anotar orientação solar do lote (Norte magnético), identificar o vento predominante do bairro (INMET), identificar restrições de vizinhança (geminado, afastamentos)
- **Estudo Preliminar:** zoneamento de programa já orientado pelo sol e vento — nunca deixar dormitório principal na fachada oeste sem solução de brise
- **Anteprojeto:** dimensionar abertura de ventilação (15% da área de piso) e verificar proporção entrada/saída antes de fechar planta

### Para Tenreiro (Interiores)

- Selecionar esquadrias operáveis nos ambientes de convívio — esquadria de correr com apenas dois folhos trava a ventilação natural; preferir máximo ar ou pivotante
- Cobogó como elemento decorativo-funcional é opção viável para separadores de ambientes e fachadas internas de átrio

### Para Baumgart (Estrutural)

- Telhado verde intensivo (jardim praticável, substrato > 30 cm) exige **cálculo estrutural específico** — carga > 300 kg/m² não é coberta pelo dimensionamento convencional de laje de cobertura

---

## ⚠️ Ressalvas

- **Rosa dos ventos por bairro:** valores do INMET são por estação automática, não por bairro residencial. Fonte indicada para precisão: Atlas Eólico Brasileiro (ANEEL) ou levantamento local
- **Ângulos de brise calculados:** use SOL-AR (LABEEE/UFSC) para os valores exatos do projeto específico — os ângulos nesta Skill são orientativos
- **Zoneamento bioclimático:** NBR 15220-3:2005 classifica RJ em ZB 8; NBR 15220-3:2024 reclassifica para ZB 4A. Para parâmetros construtivos precisos, ver Skill `complementares_nbr15220-3-2024-reclassificacao-bioclimatica-rj.md`

---

## Fontes

- [Scielo — Caracterização do regime de vento na RMRJ](https://www.scielo.br/j/esa/a/vwHXKmDBVyWgrr7vCDxcJ4d/?lang=pt&format=html)
- [INMET — Direção Predominante 1961-1990](https://portal.inmet.gov.br/uploads/normais/Vento-Direcao-Predominante_NCB_1961-1990.xls)
- [LC 198/2019 — Código de Obras Rio de Janeiro](https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/c1982019.html)
- [LC 299/2026 — Cobertura Verde RJ](https://www.legisweb.com.br/legislacao/?id=489304)
- [PBE Edifica — RTQ-R ventilação cruzada A2/A1](https://pbeedifica.com.br/forum/viewtopic.php?t=1385)
- [Vitruvius — A varanda na Cidade Maravilhosa](https://vitruvius.com.br/revistas/read/arquitextos/13.147/4457)
- [Gelker Ribeiro Arquiteto — Orientação Solar](https://gelkerribeiro.com.br/orientacao-solar/)
- [Refax — Brise horizontal, vertical ou combinado](https://refax.com.br/blog/brise-horizontal-vertical-ou-combinado-criterios-tecnicos-de-especificacao/)
- [UGREEN — Carta Solar e dimensionamento de brises](https://www.ugreen.com.br/carta-solar-o-que-e-e-como-utiliza-la-para-dimensionar-brises/)
- [SustentArqui — Cobogó na Arquitetura Bioclimática](https://sustentarqui.com.br/o-uso-do-cobogo-na-arquitetura-bioclimatica/)
- [Monitor do Mercado — Lote estreito 4m x 20m](https://monitordomercado.com.br/noticias/imoveis/379740-o-desafio-arquitetonico-de-projetar-uma-casa-confortavel-e-super-ventilada-em-um-lote-extremamente-estreito-de-apenas-4-metros-de-largura-por-20-metros-de-fundo/)
- [ArchDaily PT — Casas em terrenos estreitos](https://www.archdaily.com/pt//909320/casas-brasileiras-13-residencias-em-terrenos-estreitos)
- [Vobi — Orientação Solar em projetos de arquitetura](https://www.vobi.com.br/blog/orientacao-solar)
- [ProjetEEE/MME — Zoneamento Bioclimático Brasileiro](https://projeteee.mme.gov.br/glossario/zoneamento-bioclimatico-brasileiro/)
