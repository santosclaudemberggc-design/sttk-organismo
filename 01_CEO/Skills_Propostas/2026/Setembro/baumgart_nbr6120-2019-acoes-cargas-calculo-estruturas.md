---
name: nbr6120-2019-acoes-cargas-calculo-estruturas
description: "NBR 6120:2019 — Ações para o Cálculo de Estruturas de Edificações (cargas permanentes e acidentais). Complemento direto da NBR 6118 (superestrutura) e NBR 6122 (fundações)"
version: 1.0
status: "ratificada (Claudemberg, 09/09/2026 — Reunião Semanal)"
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_alvo: Baumgart (Estrutural, principal) — cross: Saturnino (cargas em áreas molhadas/coberturas), Tenreiro (cargas de revestimento/interiores)
criado: 2026-09-08
fonte_primaria: "ABNT NBR 6120:2019 — Ações para o cálculo de estruturas de edificações (publicada out/2019, substitui NBR 6120:1980)"
fonte_secundaria:
  - "https://www.anavidro.com.br/abnt-nbr-6120-calculo-de-estrutura-em-edificacoes/"
  - "https://portaldoprojetista.com.br/cargas-para-projetos-estruturais-nbr-6120/"
  - "https://portaldaengenharia.com.br/tabela-10-nbr-6120-cargas-variaveis/"
confianca: média (valores de referência de fontes secundárias — texto integral da norma ABNT não lido)
---

# NBR 6120:2019 — Ações para o Cálculo de Estruturas de Edificações

## O que é

Norma brasileira que fixa os **valores mínimos de cargas** (permanentes + acidentais/variáveis) que devem ser considerados no dimensionamento estrutural de edificações. Publicada em outubro de 2019, substituiu a NBR 6120:1980 (versão corrigida 2000) — a atualização mais esperada do setor estrutural em 39 anos.

**Tríade fundamental do cálculo estrutural para construção do zero:**
- **NBR 6118** (concreto armado) → dimensiona a **superestrutura** (vigas, pilares, lajes)
- **NBR 6122** (fundações) → dimensiona o que **sustenta** a superestrutura
- **NBR 6120** (cargas) → define as **ações** que as duas anteriores precisam resistir

Sem a 6120, o Baumgart não sabe QUANTO dimensionar — as outras duas dizem COMO.

## Escopo e exclusões

**Aplica-se a:** toda edificação (residencial, comercial, industrial, mista).

**NÃO cobre (normas próprias):**
- Ação do vento → NBR 6123
- Ações sísmicas → NBR 15421
- Estruturas em situação de incêndio → NBR 15200 / NBR 14323
- Pontes e viadutos → NBR 7188

## Principais mudanças da versão 2019 vs 1980

1. **Tabelas de cargas variáveis redefinidas por tipo de uso** — separação clara: hotéis, escolas, residências, hospitais, indústrias, garagens, coberturas, áreas comuns. Na versão de 1980 era genérica.
2. **Nova tabela de força horizontal em guarda-corpos e barreiras de proteção** — inexistente na versão anterior.
3. **Atualização de cargas de veículos** — categorização por área de circulação (garagem residencial vs comercial vs industrial).
4. **Novos termos, definições e simbologias** — alinhamento com normas internacionais.
5. **Revisão completa de pesos específicos** — todos os materiais de construção reavaliados.

## Classificação das ações

### 1. Ações permanentes (cargas mortas)

Peso próprio da estrutura + elementos construtivos fixos: forro, telhado, revestimentos, alvenaria, instalações embutidas. Determinadas pela **Tabela 1** da norma (pesos específicos aparentes de materiais de construção).

**Armadilha comum:** esquecer o peso de revestimento cerâmico em lajes de banheiro/cozinha (pode adicionar 0,8 a 1,2 kN/m² dependendo da espessura do contrapiso + cerâmica).

### 2. Ações variáveis (cargas acidentais)

Cargas de uso/ocupação: pessoas, móveis, veículos, equipamentos. Valores mínimos fixados pelas **Tabelas de cargas variáveis** da norma (antiga Tabela 2, reorganizada em 2019 em múltiplas tabelas por uso).

**Valores de referência — cargas variáveis mínimas (fontes secundárias):**

| Ocupação / Uso | Carga distribuída (kN/m²) | Observação |
|----------------|---------------------------|------------|
| Dormitórios (residencial) | 1,5 | Sem acesso público |
| Salas, cozinhas, lavanderias (residencial) | 1,5 | Inclui áreas de serviço |
| Banheiros (residencial) | 1,5 | Considerar peso de louças/box |
| Varandas (residencial) | 2,0 | Acesso restrito moradores |
| Escritórios | 2,0 | Sem arquivo pesado |
| Escadas (sem acesso público) | 2,5 | Prédio residencial |
| Escadas (com acesso público) | 3,0 | Prédio comercial/misto |
| Garagem — veículos leves | 3,0 | + carga concentrada por eixo |
| Coberturas inacessíveis | 0,5 | Apenas manutenção eventual |
| Coberturas com painéis solares | ≥ 1,5 | + carga de manutenção |
| Terraços e coberturas acessíveis | 3,0 | Com acesso de público |

**⚠️ LACUNA CONHECIDA:** estes valores são de fontes secundárias (portais de engenharia). Antes de dimensionamento real, o Baumgart DEVE consultar o texto integral da NBR 6120:2019 (norma paga da ABNT) para confirmar valores exatos, combinações de ações e fatores de ponderação.

### 3. Cargas especiais

| Tipo | Valor | Fonte na norma |
|------|-------|----------------|
| Paredes divisórias móveis | mín. 1,0 kN/m² | Seção de paredes |
| Compartimentos especiais (almoxarifado, arquivo) | +3,0 kN/m² | Incremento sobre uso base |
| Guarda-corpo / parapeito — horizontal | 0,8 kN/m | Força horizontal por metro |
| Guarda-corpo / parapeito — vertical | mín. 2,0 kN/m | Força vertical mínima |
| Degraus isolados de escada | 2,5 kN | Carga concentrada, posição mais desfavorável |

## Como Baumgart usa esta Skill

**Entrada obrigatória (dados que vêm de Lúcio/Oscar):**
- Programa de necessidades (cômodos, áreas, usos)
- Planta baixa com layout de paredes/lajes
- Tipo de cobertura (laje, telhado, terraço acessível)
- Garagem: quantidade de vagas, tipo de veículo
- Presença de painéis solares / equipamentos pesados na cobertura

**Saída (o que Baumgart produz com a 6120):**
- Quadro de cargas por pavimento e por cômodo
- Combinação de ações (permanente + acidental + especial)
- Envio ao modelo 6118 (superestrutura) e 6122 (fundações) para dimensionamento

**Sequência de cálculo:**
1. Levantar cargas permanentes (Tabela 1 — pesos específicos)
2. Levantar cargas variáveis por uso (Tabelas por ocupação)
3. Adicionar cargas especiais (divisórias, guarda-corpo, equipamentos)
4. Aplicar combinações de ações e fatores de ponderação (Tabelas de combinação da NBR 6120 + NBR 8681)
5. Alimentar o modelo de cálculo da NBR 6118 (superestrutura)
6. Alimentar o modelo de cálculo da NBR 6122 (fundações)

## Cross-disciplina

- **Saturnino (Hidrossanitário):** cargas de reservatórios d'água sobre lajes/coberturas; peso de tubulações embutidas em lajes; contrapiso para caimento em áreas molhadas.
- **Tenreiro (Interiores):** peso de revestimentos especiais (mármore, porcelanato grande formato 120×120, boiserie); considerar quando especificar materiais pesados em lajes superiores.
- **Glaziou (Paisagismo):** carga de terra/substrato + vegetação em coberturas verdes ou floreiras estruturais (dado de entrada: espessura e peso específico do substrato).
- **Landell (Elétrica/Automação):** peso de quadros elétricos, nobreaks e equipamentos de automação em salas técnicas.

## Interação com outras normas do Baumgart

| Norma | Relação com a NBR 6120 |
|-------|----------------------|
| NBR 6118:2026 Em.1 (concreto armado) | Recebe as cargas da 6120 como dado de entrada |
| NBR 6122:2019 Em.1 (fundações) | Recebe o somatório de cargas para dimensionar fundação |
| NBR 8681 (ações e segurança) | Define fatores de combinação e ponderação das ações da 6120 |
| NBR 9575:2024 (impermeabilização) | Peso de sistemas impermeabilizantes em coberturas → carga permanente |
| COSCIP/CBMERJ Decreto 42/2018 | Compartimentação e TRRF podem afetar espessuras → afeta cargas permanentes |

## Erros comuns a evitar

1. **Usar valores da NBR 6120:1980** — a norma de 1980 está CANCELADA. Valores mudaram significativamente, especialmente para garagens e coberturas.
2. **Esquecer o peso de revestimentos** — porcelanato + argamassa + contrapiso pode somar 1,0-1,5 kN/m². Em projeto de interiores com materiais pesados (mármore, pedra natural), pode chegar a 2,0+ kN/m².
3. **Ignorar paredes divisórias** — mesmo que a planta não especifique paredes internas, a NBR 6120 exige considerar 1,0 kN/m² mínimo como carga distribuída de divisórias.
4. **Subestimar cobertura com painéis solares** — mín. 1,5 kN/m² + manutenção. Projeto com muitos painéis pode dobrar a carga de cobertura vs. o previsto sem eles.
5. **Não separar garagem residencial de comercial** — a NBR 2019 categoriza diferente; misturar subestima a carga em garagem comercial.

## Lacunas conhecidas (a fechar antes de uso real)

1. **Texto integral da NBR 6120:2019 não lido** — valores acima são de fontes secundárias. Aquisição do PDF oficial da ABNT é responsabilidade de Wallenberg/Claudemberg.
2. **Tabelas completas de pesos específicos (Tabela 1) não disponíveis** — essenciais para cargas permanentes. Dependem do texto integral.
3. **Fatores de combinação de ações (NBR 8681)** — a 6120 referencia a 8681 para combinações. A 8681 não foi lida. Para dimensionamento real, ambas são necessárias.
4. **Emenda ou revisão posterior a 2019** — nenhuma encontrada na pesquisa de 08/09/2026. Versão vigente confirmada como 2019 (sem emenda publicada até a data).
