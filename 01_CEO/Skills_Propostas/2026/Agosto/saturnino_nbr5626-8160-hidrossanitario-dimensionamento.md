# NBR 5626/8160 — Skill de Inteligência Técnica Hidrossanitária

## Para qual Agente serve
**Saturnino** (Hidrossanitário) — equipe de Cardozo (Gestor Complementares). Esta é uma Skill de **Trilha A (Inteligência)**: normas técnicas e técnicas de projetar, não ferramenta de software. Alimenta o saber-fazer de Saturnino em projetos de instalações prediais de água fria, água quente, esgoto sanitário, e drenagem pluvial.

## Status
proposta — aguardando ratificação de Claudemberg

## O que esta Skill ensina

### Normas-Base do Projeto Hidrossanitário Predial

| Norma | Assunto | Versão Vigente |
|-------|---------|----------------|
| **ABNT NBR 5626:2020** | Sistemas prediais de água fria e quente — projeto, execução, operação e manutenção | 2020 (unificou NBR 5626 antiga + NBR 7198) |
| **ABNT NBR 8160:1999** | Sistemas prediais de esgoto sanitário — projeto e execução | 1999 (verificar possível revisão) |
| **ABNT NBR 10844:1989** | Instalações prediais de águas pluviais | 1989 (verificar atualização) |
| **ABNT NBR 9649** | Projeto de redes coletoras de esgoto sanitário | Vigente |
| **ABNT NBR 7229** | Projeto, construção e operação de fossas sépticas | Vigente |

---

### 1. Sistemas Prediais de Água — NBR 5626:2020

#### Parâmetros Obrigatórios de Pressão
- **Pressão máxima estática:** 400 kPa (40 mca) em qualquer ponto da instalação
- **Pressão mínima dinâmica:** 10 kPa (1 mca) nos pontos de utilização
- **Velocidade máxima na tubulação:** 3,0 m/s (para evitar ruído e erosão)
- **Velocidade mínima:** 0,5 m/s (para evitar deposição)

#### Método de Dimensionamento (Hunter Adaptado)
O dimensionamento de água fria usa o **método dos pesos relativos** (Hunter method adaptado para norma brasileira):

| Ponto de Utilização | Peso (UP) | Vazão de projeto |
|---------------------|-----------|-----------------|
| Lavatório | 0,3 | 0,15 L/s |
| Vaso sanitário (caixa acoplada) | 0,3 | 0,15 L/s |
| Vaso sanitário (válvula) | 2,4 | 1,70 L/s |
| Chuveiro | 0,4 | 0,20 L/s |
| Banheira | 1,5 | 0,30 L/s |
| Pia de cozinha | 0,7 | 0,25 L/s |
| Máquina de lavar louça | 0,5 | 0,15 L/s |
| Máquina de lavar roupa | 1,0 | 0,30 L/s |

**Fórmula prática:** Qp (L/s) = 0,3 × √Σ UP  _(aplica-se para ΣUP entre 2 e 6000)_

#### Reservatório de Água
- **Volume mínimo:** 1 dia de consumo (200 L/habitante, salvo especificação em código de obras local)
- **Reservatório superior:** para gravidade (mínimo 2 mca de pressão dinâmica no ponto mais desfavorável)
- **Reservatório inferior:** para sucção da bomba elevatória

#### O que NÃO pode
- Pressão estática > 400 kPa — obrigatório válvula redutora de pressão (VRP)
- Tubulação de água potável em contato direto com tubulação de esgoto
- Conexão direta rede pública / reservatório sem caixa d'água intermediária

---

### 2. Sistemas de Esgoto Sanitário — NBR 8160:1999

#### Conceitos Fundamentais
- **Ramais de descarga:** coletam os dejetos dos aparelhos sanitários
- **Ramal de esgoto:** coleta os ramais de descarga no mesmo ambiente
- **Tubo de queda:** coluna vertical que coleta esgoto de múltiplos andares
- **Ramal de escoamento:** coleta os tubos de queda e leva ao coletor predial
- **Coletor predial:** leva o esgoto até a rede pública ou fossa

#### Critérios de Dimensionamento
- **Inclinação mínima:** 2% (1 cm por metro) para tubulações DN ≤ 100 mm
- **Inclinação mínima:** 1% para tubulações DN > 100 mm
- **Velocidade crítica de autolimpeza:** mín. 0,6 m/s (garantir limpeza por arraste)
- **Grau de enchimento máximo:** 75% da seção (para manter ventilação interna)

#### Unidades Hunter de Esgoto (UHE) por Aparelho

| Aparelho | UHE | DN mínimo do ramal |
|----------|-----|-------------------|
| Lavatório | 1 | 40 mm |
| Vaso sanitário (cx. acoplada) | 4 | 100 mm |
| Vaso sanitário (válvula) | 6 | 100 mm |
| Chuveiro | 2 | 40 mm |
| Banheira | 3 | 50 mm |
| Pia de cozinha | 2 | 50 mm |
| Máquina de lavar roupa | 3 | 50 mm |

**Regra de ouro:** ramal de esgoto de vaso sanitário nunca abaixo de DN 100 mm.

#### Ventilação do Sistema de Esgoto
- **Coluna de ventilação** obrigatória em tubos de queda que atendem mais de 5 andares
- **Ventilação primária** (prolongamento do tubo de queda acima da cobertura) — o mínimo
- Colunas sem ventilação adequada provocam sifonamento e mau cheiro

---

### 3. Drenagem Pluvial Predial — NBR 10844:1989

#### Princípio de Dimensionamento
- **Intensidade de chuva de projeto:** baseada em curvas IDF da cidade (Rio de Janeiro: ~150 mm/h para TR de 5 anos, verificar dados Prefeitura/INMET atuais)
- **Calha horizontal:** usar inclinação mínima de 0,5%, velocidade máxima 1,5 m/s
- **Condutor vertical (pluvial):** separado do esgoto sanitário (norma proíbe interligação)

**Fórmula de dimensionamento de calha:**
Q = C × I × A / 360
- Q = vazão (L/s)
- C = coeficiente de escoamento (telha cerâmica: 0,90; concreto/impermeabilizado: 0,95)
- I = intensidade de chuva (mm/h) — da curva IDF local
- A = área de contribuição (m²)

---

### 4. Checklist Prático para Saturnino (início de todo projeto)

**Ao receber Briefing de Cardozo (que veio de Lúcio):**
- [ ] Identificar: número de pavimentos, número de unidades, tipologia (residencial/comercial/misto)
- [ ] Levantar: pontos de utilização por unidade e por andar — calcular ΣUP e ΣUHE
- [ ] Verificar: pressão disponível na rede pública (mínimo 10 kPa para o ponto mais desfavorável)
- [ ] Calcular: volume de reservatório (inferior + superior) com no mín. 1 dia de consumo
- [ ] Verificar: se pressão supera 400 kPa em algum ponto → especificar VRP
- [ ] Dimensionar: ramais de água fria e quente pelo método Hunter adaptado
- [ ] Dimensionar: ramais de esgoto (mín. DN 100 para vaso sanitário)
- [ ] Dimensionar: inclinações de esgoto (mín. 2% para DN ≤ 100 mm, 1% para DN > 100 mm)
- [ ] Especificar: ventilação do sistema de esgoto (primária obrigatória, secundária se >5 andares)
- [ ] Dimensionar: calhas e condutores pluviais pela fórmula Q = C×I×A/360 com IDF local RJ
- [ ] Confirmar: separação absoluta entre rede pluvial e rede de esgoto

**Erros comuns que Saturnino deve evitar:**
1. Interligar esgoto sanitário com drenagem pluvial (proibido pela norma)
2. Não prever VRP em edifícios altos (pressão > 400 kPa nos andares inferiores)
3. Omitir ventilação de esgoto (gera sifonamento de sifões e mau cheiro)
4. Inclinação de esgoto insuficiente (<2%) — provoca entupimento recorrente
5. Ramal de vaso sanitário em DN <100 mm — viola a norma

---

### 5. Coordenação com Outros Agentes de Cardozo

- **Baumgart (Estrutural):** compatibilizar furos/shafts com a estrutura — apresentar layout de shafts antes do detalhamento estrutural
- **Landell (Elétrica):** separação física de 30 cm entre tubulações de água e eletrodutos (NBR 5410 exige)
- **Glaziou (Paisagismo):** atenção a raízes que podem entupir/romper tubulações de esgoto externas — especificar tipo de tubo e proteção
- **Mindlin (Apresentação):** fornecer layout de shafts e esquemas verticais em formato legível para pranchas

---

## O que esta Skill NÃO cobre
- Projetos de combate a incêndio/hidrantes (NBR 13714 — especialidade separada)
- Projetos de gás predial (NBR 15526 — especialidade separada)
- Tratamento de efluentes (ETE — projeto ambiental especializado)
- Reuso de água cinza (verificar código de obras municipal RJ para regulamentação específica)

## Limitações honestas
- Os valores de UHE e UP desta Skill são os das tabelas normativas padrão — verificar se o Briefing especifica aparelhos fora da lista (spa, hidromassagem, torneira privativa) que têm valores específicos
- A intensidade de chuva (IDF) para Rio de Janeiro deve ser verificada nos dados mais recentes do INMET/Prefeitura — o valor de 150 mm/h para TR=5 anos é referência aproximada, não definitiva
- NBR 8160 é de 1999 e NBR 10844 de 1989 — verificar se houve revisão ou emenda publicada desde então antes de protocolar projetos oficiais

## Fontes
- NBR 5626:2020 — norma vigente (ABNT; conteúdo via fontes secundárias verificadas: nptengenharia.com.br, normas.com.br — WebSearch 28/08/2026)
- NPT Engenharia — "Projeto Hidráulico Predial: Guia Completo 2026" (nptengenharia.com.br — WebSearch 28/08/2026)
- ABNT NBR 8160:1999 — conteúdo via fontes técnicas de referência do setor
- ABNT NBR 10844:1989 — conteúdo via fontes técnicas de referência do setor
- Data de verificação: 28/08/2026
