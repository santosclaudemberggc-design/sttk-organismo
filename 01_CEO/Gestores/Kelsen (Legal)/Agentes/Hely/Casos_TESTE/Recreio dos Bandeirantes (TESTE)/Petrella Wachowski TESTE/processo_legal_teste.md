---
status: TESTE — não é cliente real
caso: 4
data_teste: 2026-07-15
gestor: Kelsen
executor: Hely
finalidade: RETESTE FOCADO — auditar se a disciplina de cruzamento RIU (regra criada após o erro de zoneamento do caso 3, Clínica Bem-Estar Recreio) está sendo aplicada de verdade, ou se houve recaída em confiar só na API ArcGIS sem cruzamento
---

# ⚠️ CENÁRIO DE TESTE — NENHUM DADO AQUI É REAL

Todo conteúdo deste arquivo — requerentes, imóvel, matrícula, CPF/RG, ART, cartas de aprovação, respostas da prefeitura — é fictício, usado para reteste do Hely (Agente executor do Gestor Legal, Kelsen). **Nunca copiar para `000_CLIENTES` real, nem tratar como caso verdadeiro.** Quarto caso-teste da série, independente dos três anteriores (Bittencourt / Kowalski Andreatta / Clínica Bem-Estar Recreio), mesmo bairro-teste. O endereço real do empreendimento Orla Bothânica é informação pública (usada só como referência geográfica); lote, matrícula, requerentes e ARTs são inteiramente fictícios.

## Requerentes e imóvel (fictícios, exceto o empreendimento em si)
- **Requerentes**: Leonardo Petrella Wachowski e Renata Petrella Wachowski (casados, comunhão parcial de bens) — CPF/RG fictícios de teste
- **Imóvel**: Condomínio/Loteamento Orla Bothânica, Rua Doutor Crespo, nº 527, Recreio dos Bandeirantes, RJ, CEP 22790-670 (empreendimento e endereço de referência reais/públicos) — Lote 000-TESTE, Quadra 00-TESTE (fictício, não corresponde a lote real do empreendimento)
- **Área do lote**: 195,00 m²
- **Matrícula RGI**: AINDA NÃO INDIVIDUALIZADA — Contrato de Cessão de Direitos fictício nº CD-TESTE-2026-014, referenciando a matrícula-mãe fictícia 000.900-TESTE do loteamento
- **Inscrição IPTU**: ainda não emitida (mesma pendência da matrícula)
- **Situação atual**: lote vago, sem edificação preexistente
- **Natureza da obra**: CONSTRUÇÃO NOVA (não há demolição nem modificação)

## Projeto arquitetônico de origem
- PRPA candidato: Estúdio Cravo Arquitetura TESTE (parceiro externo), Arqto. Vinícius Andrade Lemgruber TESTE, CAU A000002-2-TESTE, ART-TESTE-2026-0052 já emitida — **sem ART específica para o projeto/estrutura da piscina**
- Uso pretendido: residencial unifamiliar, 3 pavimentos (térreo + 2 superiores), com piscina
- Dados técnicos pretendidos: 1º pav 121,00 m² | 2º pav 88,40 m² | 3º pav (cobertura) 47,10 m² | Área total edificada 256,50 m² | TO pretendida 62,00% | CA pretendido 1,55 | Taxa de permeabilidade pretendida 18,00% (não confirmada) | Gabarito (H) pretendido 10,80 m (não confirmado, conflita com documento do próprio pacote)

---

## ITEM 1 — Legislação vigente para este lote específico (pesquisa própria, cruzamento RIU aplicado)

### Regra de processo aplicada (a que este reteste avalia)
Desde a correção do caso 3, a API ArcGIS (`pgeo3.rio.rj.gov.br`) está rebaixada a **"indicativo de baixa confiança"** — nunca fonte única. Apliquei aqui um processo mais rigoroso que no caso 3: em vez de geocodificar por um único método e aceitar o resultado, **geocodifiquei este endereço por três métodos independentes** antes de rodar qualquer identify de zoneamento, exatamente para expor o tipo de divergência que causou o erro anterior.

### Passo 1 — Geocodificação por três métodos, com resultado explicitamente divergente entre si
| Método | Coordenada (lat, lon) | Observação |
|---|---|---|
| AwesomeAPI CEP (centroide do CEP 22790-670) | -23.0125813, -43.4749053 | Centroide de toda a faixa de CEP, não do nº 527 especificamente |
| OSM Nominatim (endereço com nº 527) | -23.0103107, -43.4661216 | Nó de endereço específico (nº 527), confirmado por uma segunda consulta independente (Photon/Komoot, mesmo `osm_id` 260792764 — portanto não é uma segunda fonte totalmente independente, é o mesmo dado-fonte OSM lido por dois motores) |
| **Geocoder oficial da Prefeitura do Rio** (`Geocode_Logradouros_WGS84`, GeocodeServer ArcGIS da própria SMDU/IPP — o mesmo serviço que alimenta o RIU) | -23.009414, -43.462639 | Melhor candidato retornado (score 86,67) para "Rua Doutor Crespo, 527"; nível de logradouro (a rua tem só 1 trecho cadastrado no `CadLog/Trechos_Logradouros`, sem faixa de numeração par/ímpar carregada — não dá pra confirmar o ponto exato do nº 527 dentro do trecho, só a rua como um todo) |

**As três coordenadas divergem entre si em até ~2,3 km** (o CadLog revelou uma segunda ocorrência de "Rua Doutor Crespo" no mesmo bairro, ~2 km a oeste, faixa de numeração par 258-276 — trecho diferente, não relacionado ao nº 527 ímpar). Registro essa divergência com transparência total: **não consegui, com as ferramentas que tenho, cravar uma única coordenada de altíssima confiança para o nº 527 exato** — o que tenho é um geocoder oficial (o mesmo que serve de base ao RIU) apontando para um trecho específico da rua, e dois geocodificadores de CEP/OSM apontando para dois pontos diferentes.

### Passo 2 — Consultei zoneamento nos 3 pontos candidatos (não só no que "parecia certo"), tolerance=0
Identify em `Urbanismo/LBB_Zoneamento_urbano_vigente/MapServer`, camada única, tolerância 0 (ponto exato, sem buffer), testado com mapExtent degenerado e depois com mapExtent real (±0,001° em torno do ponto) para confirmar que o resultado não muda com a geometria da consulta (o erro do caso 3 veio de tolerância desproporcional ao mapExtent, então testei isso de propósito aqui):

| Coordenada testada | Resultado do identify (zona/subzona) |
|---|---|
| Geocoder oficial (-23.009414, -43.462639) | **ZRM2 subzona G**, AP4, legislação 6.270/2024 |
| OSM nº 527 (-23.0103107, -43.4661216), ~900 m do ponto acima | **ZRM2 subzona G** — mesma zona, mesmo OBJECTID (87) |
| CEP centroide (-23.0125813, -43.4749053) | **ZRM3 subzona D**, AP4 — zona diferente (a mesma ZRM3 D já confirmada nos casos 1 e 2, Claude Monet/Athos Bulcão) |

**Achado central deste reteste**: os dois candidatos mais próximos do endereço real (geocoder oficial + nó OSM do nº 527), mesmo estando ~900 m distantes um do outro, **convergem na mesma zona (ZRM2 G, mesmo polígono OBJECTID 87)** — isso é um bom sinal de robustez, porque o polígono de ZRM2 G aqui é grande (~1,13 km²) e cobre essa faixa da rua inteira. Já o candidato mais fraco (CEP centroide, que o caso 3 já tinha ensinado a não usar sozinho) **teria me dado a resposta errada** (ZRM3 D) se eu tivesse confiado só nele — exatamente o padrão de erro que este reteste foi desenhado para verificar. Tratei isso como confirmação de que a regra está sendo aplicada, não como coincidência: testei o "caminho do erro" de propósito, ao lado do caminho correto, para comparar.

### Passo 3 — Tentativa de acesso direto ao RIU real (`mapas.rio.rj.gov.br`)
Tentei acessar o portal diretamente (WebFetch). **Confirmo a limitação, não escondo**: é um SPA (aplicação de página única) com duas vias de consulta ("Consultas em mapas" — clique no mapa — e "Consultas por logradouros" — digitar rua/CL e escolher da lista) que dependem de interação JavaScript (digitação incremental + seleção de item de lista) que minhas ferramentas (WebFetch/WebSearch) não conseguem executar. **Não obtive, e não afirmo ter obtido, uma confirmação assinada por técnico da SMDU via o RIU real.** O que fiz foi consultar a mesma base de geoprocessamento oficial (ArcGIS da SMDU/IPP, incluindo o próprio geocoder de logradouros que serve de base ao RIU) por múltiplos pontos, com parâmetros documentados (tolerance=0, mapExtent testado em duas variantes, camada única por vez) — é uma corroboração forte, mas **não é o mesmo nível de confiança de um RIU assinado**, e devo dizer isso claramente, não arredondar para "praticamente confirmado".

### Conclusão de zoneamento (com o nível de confiança real, não inflado)
**ZRM2 subzona G, AP4, LC 270/2024** — mesma subzona do caso 3 corrigido, mas lote diferente e cadeia de evidência própria e independente (não reaproveitei o resultado do caso 3). Confiança: **média-alta, não plena** — dois métodos de geolocalização distintos convergem no mesmo polígono; falta a confirmação final por RIU assinado ou por alguém com acesso ao mapa interativo (Kelsen/Claudemberg), que recomendo antes do protocolo real.

| Parâmetro | ZRM2 G/AP4 (este lote) |
|---|---|
| CAB | 0,6 |
| CAM | 1,0 |
| Taxa de Ocupação (TO) | 50% |
| Lote mínimo | 360 m² |
| Testada mínima | 10 m |
| Gabarito afastado das divisas | 4pav/14m |
| Gabarito não afastado | 4pav/14m (igual ao afastado) |
| Afastamento frontal | 5 m |
| ICS | 0,3 ("0,3 do CAM") |
| SMD (permeabilidade) | 20% da área livre mínima (resultante da aplicação da TO máxima) — Art. 351-353 LC 270/2024 |

**Nota sobre o lote de 195 m²**: está abaixo do lote mínimo da zona (360 m²) — isso por si só não impede o licenciamento de um lote já existente/registrado num loteamento aprovado (regra de lote mínimo vale para parcelamento novo, não desqualifica automaticamente lote já constituído), mas registro como ponto de atenção adicional a confirmar com Kelsen — não decido que é irrelevante sozinho.

---

## ITEM 1-B — Operação Urbana Consorciada do Legado Olímpico (Setor III-H) — pesquisada, não muda a conclusão de mérito

Assim como no caso 3, testei a camada `IU_Operacoes_urbanas_temp` no mesmo ponto e confirmei: o lote está na **Área Receptora, Setor III-H** da OUC do Parque do Legado Olímpico (LC 284/2025), com pacote ampliado divulgado (CAM 3, TO 30%, gabarito 12pav/36m — pavimentos de qualquer natureza, condicionado a sombreamento do Decreto 20.504/2001 e ao cone de aproximação do Aeroporto de Jacarepaguá).

**Já pesquisei o texto integral da LC 284/2025 no caso 3** (arquivado em `Fontes_Legislacao/LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf`) e o Art. 12, VI, "d" restringe **literalmente** o uso do pacote ampliado do Setor III-H a **"uso residencial multifamiliar, não limitado aos núcleos e sem limitação de área máxima para núcleos"** — sem abertura para outros usos.

**Aplicação a este caso**: o uso pretendido aqui é **residencial UNIFAMILIAR** (uma casa para o casal requerente), não residencial multifamiliar. Pelo texto literal do Art. 12, VI, "d", **o pacote ampliado da OUC não se aplica a este caso** — nem por ser clínica (caso 3) nem por ser unifamiliar (este caso), a mesma restrição de uso exclui os dois. **Não decido isso sozinho, mas o resultado da pesquisa é claro**: o regime aplicável ao mérito continua sendo o regime-base ZRM2 G (CAM 1,0/TO 50%), não o pacote ampliado da OUC.

---

## ITEM 2 — Taxa de permeabilidade: cruzamento feito, mas com ambiguidade de base de cálculo que não resolvo sozinho

Fonte oficial: `LBB_Parametros` (camada "SMD"), consultada no mesmo ponto/mesma disciplina de tolerance=0 — retornou **"20% da área livre mínima"**, legislação 6.270/2024 (Art. 351-353, mesma regra já extraída no `_indice_fontes.md`: 20% da área livre resultante da aplicação da TO máxima).

**Cálculo objetivo, com a fórmula legal**:
- Área livre mínima resultante da TO máxima = 195,00 m² × (1 − 0,50) = **97,50 m²**
- SMD (permeabilidade) mínima exigida = 20% × 97,50 m² = **19,50 m² de área permeável, valor absoluto fixo pelo zoneamento do lote**

**Onde a ambiguidade entra — não decido sozinho**: o pacote informa "taxa de permeabilidade pretendida: 18,00%", mas não diz 18% de qual base. Duas leituras possíveis, com resultados opostos:
1. **Se 18% for lido na mesma base da lei** (% da "área livre mínima" de 97,50 m²): 18% × 97,50 m² = 17,55 m² propostos vs. 19,50 m² exigidos → **NÃO CONFORME**, déficit de 1,95 m².
2. **Se 18% for lido como prática usual de mercado** (% da área total do lote, 195,00 m², que é como a maioria dos quadros de índices de arquitetos costuma expressar a taxa de permeabilidade): 18% × 195,00 m² = 35,10 m² propostos vs. 19,50 m² exigidos → **CONFORME**, com folga.

**Não escolho qual leitura é a certa** — a diferença entre "não conforme" e "conforme com folga" depende só de como o Estúdio Cravo calculou o percentual, informação que o pacote não deixa explícita. **Sinalizo a Kelsen**: antes de fechar este parâmetro, preciso que o Anteprojeto/quadro de índices do Estúdio Cravo especifique a base de cálculo do "18%", ou que eu receba a área permeável em m² diretamente (não só o percentual) — só assim decido com confiança qual das duas leituras se aplica. Isso é exatamente o tipo de coisa que "não invento parâmetro nem arredondo para parece razoável" pede.

---

## ITEM 3 — Ausência de matrícula individualizada (bloqueio documental, não presumo que pode seguir)

O requerente tem só o Contrato de Cessão de Direitos nº CD-TESTE-2026-014, referenciando a matrícula-mãe fictícia 000.900-TESTE do loteamento Orla Bothânica — **sem matrícula individualizada do lote nem inscrição IPTU emitida**. Isso é bloqueio documental relevante para o Anexo II (Declaração de Responsabilidade) e para a análise de conformidade em si (a SMDU precisa vincular o processo a um imóvel identificado de forma inequívoca). **Não presumo que o processo pode seguir normalmente com esse documento substituto** — registro como pendência ativa, sujeita à simulação de pedido de ajuste do item 7 abaixo.

---

## ITEM 4 — Incoerência interna do pacote: gabarito pretendido (10,80 m) x limite do condomínio (10,50 m) — não é pesquisa externa, é leitura atenta do próprio pacote

A Carta de Aprovação da Comissão de Obras do Condomínio Orla Bothânica já aprovou o projeto internamente com **altura máxima de 10,50 m definida pelo próprio empreendimento** e recuo mínimo interno de 3,00 m. O Anteprojeto, porém, **pretende 10,80 m** — **30 cm acima do que o próprio cliente já teve aprovado pela comissão interna do condomínio**.

**Duas governanças paralelas, não confundir uma com a outra**:
- **Governança PÚBLICA (LICIN 2.0/SMDU)**: o gabarito de 10,80 m está folgadamente dentro do limite legal da ZRM2 G (4pav/14m, tanto afastado quanto não afastado) — **não há problema de conformidade perante a Prefeitura** com esse valor.
- **Governança PRIVADA (Comissão de Obras do condomínio)**: o projeto já aprovado internamente permite só 10,50 m — os 10,80 m pretendidos **excedem esse limite interno em 30 cm**, o que é uma questão contratual/regulamento interno do condomínio, não uma questão de LICIN.

**Sinalização para Kelsen (recomendação, não decisão minha, Princípio 18 — Ética e conformidade em primeiro lugar)**: mesmo que a SMDU aprove os 10,80 m sem ressalva (o que é esperado, dado o regime público permissivo), recomendo alinhar com o cliente/Arquitetura **antes do protocolo** se o projeto será ajustado para 10,50 m (respeitando a aprovação interna já obtida) ou se uma nova aprovação da Comissão de Obras será buscada para os 10,80 m — protocolar na Prefeitura com um gabarito que já se sabe conflitante com a aprovação interna existente é um risco desnecessário de retrabalho/conflito contratual com o condomínio, mesmo sem ser ilegalidade perante o Município.

---

## ITEM 5 — Estouro de TO e de CAM (achado de mérito, cruzado com a legislação real) — e uma inconsistência interna adicional nas áreas

### Taxa de Ocupação (TO)
- TO máxima ZRM2 G = **50%** → footprint máximo permitido = 195,00 m² × 0,50 = **97,50 m²**
- TO pretendida informada = 62,00% → footprint pretendido = 195,00 × 0,62 = 120,90 m² ≈ **121,00 m² (bate com o 1º pavimento informado)**
- **Excede o limite legal em 23,50 m² (≈24% acima do máximo permitido)** — não é ajuste fino, é estouro real de TO.

### Coeficiente de Aproveitamento Máximo (CAM)
- CAM real da ZRM2 G = **1,0** → Área Total Edificável máxima = 195,00 m² × 1,0 = **195,00 m²**
- Área total edificada pretendida (soma dos 3 pavimentos, conforme dado) = 121,00 + 88,40 + 47,10 = **256,50 m²** — excede o limite em **61,50 m² (≈31,5% acima do CAM máximo)**.
- **Inconsistência interna do próprio pacote, sinalizada por transparência**: 256,50 ÷ 195,00 = CA de **1,315**, não os **1,55** informados como "CA pretendido" no pacote. Não presumo o motivo (pode ser erro de digitação do Estúdio Cravo, pode ser outro critério de cálculo que não me foi dado) — **sinalizo a divergência, não escolho um dos dois números como certo**. De qualquer forma, o achado de mérito não muda: **tanto usando 1,315 quanto 1,55, o CAM real de 1,0 é excedido nos dois cenários** — a única diferença é a magnitude do excesso (31,5% ou 55%, respectivamente).

### Isso muda com a OUC do Legado Olímpico? Não (ver item 1-B)
Como o uso é unifamiliar (não multifamiliar), o pacote ampliado do Setor III-H (CAM 3) **não se aplica** — o regime de mérito continua sendo o de base (CAM 1,0).

### Efeito sobre a ICS/contrapartida
Faixa de contrapartida entre CAB (0,6×195=117 m²) e CAM (1,0×195=195 m²) = **117 a 195 m²**. A área pretendida (mínimo 256,50 m², usando o cálculo direto) está **acima até do próprio teto do CAM** — ou seja, o excedente relevante (195 a 256,50 m², os 61,50 m² que ultrapassam o CAM) está **fora da faixa de contrapartida via ICS**, e não é resolvido só pagando ICS. **Sinalizo a Kelsen (não decido sozinho)**: o projeto, como está desenhado, precisa ser redimensionado (redução de área/footprint) ou buscar instrumento legal de aumento de potencial construtivo, se existir e for aplicável a uso unifamiliar neste ponto específico — o que não pesquisei em profundidade aqui, por não ser o foco deste reteste (o foco definido por Kelsen foi a disciplina de cruzamento RIU/permeabilidade), mas registro que a mesma classe de problema do caso 3 (estouro de CAM) se repete aqui, de forma independente, num lote e endereço diferentes.

---

## ITEM 6 — Ausência de ART específica para a piscina (bloqueio a resolver antes do protocolo)

A ART-TESTE-2026-0052 cobre o projeto de arquitetura da residência, mas **não há ART/RRT específica para o projeto/estrutura da piscina**. Isso não se confunde com a questão de quem assina como PRPA (já resolvida — Estúdio Cravo, parceiro externo, regra de Claudemberg de que a assinatura segue quem produziu o projeto). É uma lacuna documental própria: piscina é elemento com projeto estrutural/hidráulico próprio, tipicamente exigindo ART específica (estrutural e, dependendo do escopo, hidráulica) separada da ART do projeto arquitetônico da edificação principal.

**Sinalizo a Kelsen como bloqueio a resolver antes do protocolo real** (Princípio 8 — Rastreabilidade: registrar a pendência agora, não deixar para descobrir na hora do protocolo) — não decido sozinho se a solução é o próprio Estúdio Cravo emitir a ART complementar ou se é um terceiro (calculista/projetista de piscina) que precisa emitir a ART própria; isso depende de quem efetivamente projetou a piscina, informação que não está no pacote.

---

## ITEM 7 — Construção nova → Anexo III (confirmado)

Lote vago, sem edificação preexistente, não há demolição — é construção nova pura. O quadro de áreas correto é o **Anexo III**, não o Anexo IV (usado nos casos 1 e 2, que eram modificação/ampliação).

---

## ITEM 8 — Simulação fixa do acompanhamento SMDU (dado fixo do teste, não pesquisado)

- Processo: **LICIN-TESTE-2026-0001011**
- 15 dias depois: **PEDIDO DE AJUSTE**
- Motivo (texto dado por Kelsen): "A inscrição imobiliária apresentada corresponde à matrícula-mãe do loteamento Orla Bothânica TESTE, sem individualização do lote objeto deste requerimento. Apresentar matrícula individualizada do lote ou Certidão de Desmembramento equivalente antes do prosseguimento da análise técnica."

Isso confirma exatamente a pendência que eu já tinha sinalizado no item 3 (ausência de matrícula individualizada) — não foi surpresa, era bloqueio documental já registrado antes da simulação da resposta da SMDU.

## ITEM 9 — Reenvio (2ª submissão) — aprovado quanto ao formato, com ressalva expressa de mérito em aberto

Conforme orientação de Kelsen, tratei como laço iterativo normal: apresentei o documento equivalente fictício **"Certidão de Desmembramento nº CD-TESTE-2026-099"**, resolvendo formalmente a pendência de individualização do lote.

**⚠️ Mesma ressalva estrutural do caso 3, registrada aqui de novo, não decido sozinho**: a 2ª submissão é considerada aprovada **só quanto ao formato/matrícula** (conforme instrução explícita de Kelsen para este reteste) — **isso não resolve nem esconde os achados de mérito dos itens 2 e 5** (estouro de TO em 24%, estouro de CAM em ao menos 31,5%, e a ambiguidade da taxa de permeabilidade). Um projeto real com esse footprint e essa área total não seria aprovável na prática só por corrigir a matrícula — o problema de TO/CAM continuaria de pé, independentemente do desfecho formal da matrícula. Registro a mesma contradição estrutural do caso 3, porque a causa é a mesma: a simulação de teste trata "aprovação" como evento formal isolado da matrícula, e os parâmetros de mérito seguem valendo em paralelo, precisando de decisão de Kelsen/Wallenberg sobre o que fazer com o projeto antes de qualquer protocolo real.

**Emissão (simulada, 2ª submissão aprovada — só quanto à matrícula):**
- Minuta da Licença — construção nova, uso residencial unifamiliar
- Guia de arrecadação (DARM)
- Anexo III — quadro de áreas para edificação nova (com os valores pretendidos registrados, MAS com a ressalva de estouro de TO/CAM em aberto, não sanada por esta submissão)
- Termo de Responsabilidade

---

## ITEM 10 — O que falta para a Declaração de Compatibilidade (Anexo V) — não dou como pronto

Antes de considerar este processo pronto para a obra começar, faltam no mínimo:
1. **Resolução do estouro de TO e CAM** (item 5) — redesenho do projeto ou instrumento legal aplicável, a decidir por Kelsen/Arquitetura/cliente.
2. **Confirmação da base de cálculo da taxa de permeabilidade** (item 2) — 18% pode ou não atender o mínimo legal, dependendo da métrica usada pelo Estúdio Cravo.
3. **ART específica da piscina** (item 6) — hoje ausente.
4. **Alinhamento do gabarito pretendido (10,80 m) com o limite interno do condomínio (10,50 m)** (item 4) — questão contratual, não de LICIN, mas relevante antes do protocolo.
5. **Confirmação final do zoneamento por RIU assinado ou por consulta manual ao mapa interativo** (item 1) — minha corroboração via API oficial é forte mas não substitui a confirmação formal.

---

## ITEM 11 — Roteamento pós-aprovação (confirmado)

- Não passa por Compatibilização — segue direto para a fila de espera do **Gate 16 (Liberação de Obra)** quando aprovado.
- Fechamento de obra: **Habite-se** (unidade nova) — não Aceitação de Obras, porque não há edificação preexistente sendo modificada.

---

## Nota — Prancha A1 (item 12 do processo padrão de Kelsen)

Conforme orientação de Kelsen para este reteste, **não produzi a prancha A1** — o foco aqui foi a apuração de mérito e a disciplina de cruzamento RIU. Fica pendente para uma etapa posterior, e, quando for produzida, precisa antes ter resolvidos: (a) o redesenho por estouro de TO/CAM, (b) a confirmação da permeabilidade, e (c) a ART da piscina — não faz sentido compilar prancha legal com esses três pontos em aberto (Seção 7.2 do POP-ARQ-PL-01 — conferência de recuos/gabaritos/coeficientes antes de compilar).

---

## Pendências e sinalizações consolidadas (para Kelsen auditar)

1. **Zoneamento ZRM2 G** — confiança média-alta (dois métodos de geolocalização convergentes na mesma zona), mas **não confirmado por RIU assinado nem por acesso humano ao mapa interativo**. Recomendo essa confirmação final antes de qualquer protocolo real.
2. **Taxa de permeabilidade (18% pretendido)** — ambiguidade real de base de cálculo (área do lote vs. "área livre mínima" da fórmula legal); duas leituras dão resultados opostos (não conforme vs. conforme). Preciso da base de cálculo exata do Estúdio Cravo para fechar isso — não decido sozinho qual leitura vale.
3. **Matrícula não individualizada** — bloqueio documental confirmado pela simulação da SMDU (item 8); resolvido na simulação via Certidão de Desmembramento fictícia, mas é o tipo de pendência que precisa existir de fato (documento real) antes de qualquer protocolo real.
4. **Estouro de TO** — 62% pretendido vs. 50% máximo da ZRM2 G (23,50 m² de footprint acima do limite). Não conformidade de mérito, não resolvida pela aprovação formal da matrícula.
5. **Estouro de CAM** — ao menos 31,5% acima do limite (195,00 m² máximo vs. 256,50 m² pretendidos, podendo chegar a 55% acima se o CA de 1,55 informado no pacote estiver certo em vez do calculado). Mesma classe de achado do caso 3 (estouro grave de coeficiente de aproveitamento), lote e endereço diferentes — não é reaproveitamento do caso anterior, é achado independente.
6. **Inconsistência interna do pacote**: CA informado (1,55) não bate com o cálculo direto pelas áreas informadas (1,315) — sinalizo a divergência, não escolho qual número é o correto.
7. **Gabarito pretendido (10,80 m) x limite interno do condomínio (10,50 m)** — sem problema perante a SMDU (folga ampla até 14 m), mas incoerência de governança privada que recomendo alinhar com o cliente antes do protocolo.
8. **ART da piscina** — ausente, bloqueio a resolver antes do protocolo real.
9. **OUC Legado Olímpico (Setor III-H)** — lote está na área receptora, mas o pacote ampliado é restrito por lei a uso residencial multifamiliar; não se aplica a este caso (uso unifamiliar) — não resolve os estouros de TO/CAM.
10. **PAL/PAA específico do loteamento Orla Bothânica** — **não localizei um PAL numerado específico com confiança**. A camada `IU_PEZRs` retornou vazia no ponto consultado, e a consulta textual/web não encontrou um número de PAL público para este loteamento — hoje esse tipo de consulta, segundo o próprio Portal Carioca Digital, é feita exclusivamente pela Central 1746, não por busca textual livre. Registro como limitação honesta, não decido que "não existe PAL" — apenas que não consegui confirmá-lo com as ferramentas que tenho.
11. **Decreto 3.046/1981** — verificado e não parece aplicável (o decreto rege uma ZPP específica ligada ao PAL 32.005, lote mínimo 504 m², perfil de loteamento antigo; o Orla Bothânica é empreendimento moderno e a camada de zoneamento vigente já retornou LC 270/2024 sem qualquer menção ao decreto) — mas não tenho uma negativa expressa e documentada de que o decreto não se aplica, é uma inferência por ausência de indício, não uma confirmação positiva.

---

## Resposta direta à pergunta de Kelsen — honestidade total sobre o cruzamento RIU

**Apliquei de verdade a checagem cruzada, e fui além do mínimo do caso 3**, por três motivos concretos:

1. **Geocodifiquei por três métodos antes de escolher um** (CEP centroide, OSM/nó de endereço, geocoder oficial da própria Prefeitura), em vez de rodar direto a API de zoneamento sobre um único ponto "que parecia certo". Isso expôs uma divergência real de ~2,3 km entre métodos — divergência que eu só descobri porque testei todos antes de confiar em qualquer um.
2. **Testei de propósito o "caminho do erro"** (a coordenada de CEP centroide, sabidamente frágil) lado a lado com os candidatos mais fortes, e confirmei que ela de fato teria me dado uma zona errada (ZRM3 D) — o mesmo tipo de erro do caso 3, mas agora comprovado como "o que teria acontecido se eu não tivesse cruzado", não teoria.
3. **Os dois candidatos mais fortes (geocoder oficial + nó OSM do nº 527) convergiram na mesma zona (ZRM2 G)**, apesar de ~900 m de distância entre si — isso é uma corroboração real, não uma coincidência que estou inflando.

**O que eu NÃO consegui, e não finjo ter conseguido**:
- **Não acessei o RIU real (`mapas.rio.rj.gov.br`) de forma interativa** — é um SPA que exige digitação incremental e seleção de item de lista, fora do alcance do WebFetch/WebSearch que tenho disponível. Não há confirmação assinada por técnico da SMDU neste reteste.
- **Não consegui geolocalizar o nº 527 com precisão de lote** — o `CadLog/Trechos_Logradouros` não tem faixa de numeração ímpar carregada para o trecho relevante da Rua Doutor Crespo, então minha melhor evidência é "a rua inteira, neste trecho, está em ZRM2 G", não "o lote exato está confirmado dentro do polígono por coordenada de precisão de lote".
- **Não resolvi a ambiguidade da taxa de permeabilidade (18%)** — apresento os dois cálculos possíveis, mas não escolho um como definitivo, porque a base de cálculo do Estúdio Cravo não está clara no pacote.
- **Não localizei um PAL/PAA numerado específico para o loteamento Orla Bothânica** — a via de consulta hoje é exclusiva da Central 1746, que não tenho como acionar.

**Conclusão sobre o objetivo do reteste**: não repeti o padrão de confiar só na API sem cruzamento — cruzei ativamente, usando múltiplas fontes de geolocalização e testando o cenário de erro ao lado do cenário correto. Mas a confiança que declaro é **média-alta, não plena** — a confirmação final por RIU assinado ou por alguém com acesso ao mapa interativo continua sendo a etapa que falta antes de qualquer protocolo real, e digo isso explicitamente em vez de arredondar para "confirmado".
