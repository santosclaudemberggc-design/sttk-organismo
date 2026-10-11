# NBR 5419:2026 — SPDA: Proteção contra Descargas Atmosféricas

**Versão:** 1.0  
**Status:** avaliada — procede com ressalva  
**Data:** 15/09/2026
**Avaliado em:** 16/09/2026  
**Tipo:** Inteligência (Trilha A)  
**Para:** Landell (Elétrica+Automação) — cross: Baumgart (Estrutural), Oscar (Arquitetura)  
**Gestor:** Cardozo (Complementares)

---

## O que é

NBR 5419:2026 — Sistema de Proteção contra Descargas Atmosféricas (SPDA). Publicada pela ABNT em março de 2026, com errata em abril de 2026 e período de transição de 180 dias (projetos podem usar a versão anterior até ~setembro/2026). Substitui a NBR 5419:2015 (que era dividida em 4 partes). A versão 2026 consolida tudo em documento único.

## Contexto regulatório

- **Federal:** a instalação de SPDA é exigida conforme análise de risco (Gerenciamento de Risco conforme a própria NBR 5419). Não é opcional — se a análise de risco indicar necessidade, é obrigatório.
- **Municipal RJ:** o COSCIP/CBMERJ referencia a NBR 5419 para edificações acima de determinada altura ou área, e o LICIN 2.0 exige conformidade para obtenção de habite-se em edificações que necessitem SPDA.
- **Para residências:** casas unifamiliares isoladas raramente necessitam de SPDA (a análise de risco geralmente indica nível tolerável). Mas condomínios, edifícios residenciais e áreas com alta incidência de raios (Ng elevado) frequentemente exigem.

## Mudanças principais da versão 2026

1. **Ng (Nível Keraunico) agora por satélite/sensor municipal:** a versão anterior usava mapas isocerâunicos nacionais (imprecisos). A 2026 determina que o Ng seja obtido por dados de satélite ou sensores por município — mais preciso e geralmente com valores MAIORES que os antigos mapas.

2. **Medição de resistência de aterramento NÃO é mais exigida:** a norma agora requer apenas medição de **continuidade elétrica** com miliohmetro (resistência do condutor, não do solo). Isso simplifica significativamente a verificação do sistema de aterramento.

3. **Inspeção periódica a cada 3 anos:** obrigatória para manter a eficácia do SPDA.

4. **Documento único:** consolida as 4 partes da versão 2015 (Princípios gerais, Gerenciamento de risco, Danos físicos, Sistemas elétricos/eletrônicos) em um único documento.

## Parâmetros numéricos por nível de proteção

### Raio da esfera rolante (captação)

| Nível de proteção | Raio da esfera | Aplicação típica |
|-------------------|---------------|-----------------|
| I (máxima) | 20 m | Edificações com risco de explosão, hospitais |
| II | 30 m | Edificações com grande concentração de pessoas |
| III | 45 m | Edificações comerciais, residenciais multifamiliar |
| IV (mínima) | 60 m | Residenciais unifamiliares (quando necessário) |

### Malha de captação

| Nível de proteção | Dimensão da malha |
|-------------------|------------------|
| I (máxima) | 5 m × 5 m |
| II | 10 m × 10 m |
| III | 15 m × 15 m |
| IV (mínima) | 20 m × 20 m |

### Seções mínimas de condutores

| Material | Seção mínima | Aplicação |
|----------|-------------|-----------|
| Cobre | 35 mm² | Captores, descidas e aterramento |
| Alumínio | 70 mm² | Captores e descidas (não para aterramento) |
| Aço galvanizado | 50 mm² | Captores, descidas e aterramento |

### Espaçamento de descidas

| Nível de proteção | Espaçamento máximo entre descidas |
|-------------------|----------------------------------|
| I | 10 m |
| II | 15 m |
| III | 20 m |
| IV | 25 m |

## Brecha válida (mentalidade v3.0)

A maioria dos projetistas elétricos no RJ trata o SPDA como "só um para-raios em cima do prédio" e terceiriza para empresas especializadas sem entender os parâmetros. Profissionais experientes:

1. **Fazem a análise de risco ANTES de definir se precisa de SPDA:** muitos projetos residenciais unifamiliares em áreas com Ng baixo NÃO precisam de SPDA. Instalar sem necessidade é custo desnecessário para o cliente.
2. **Usam o Ng municipal atualizado (satélite):** o valor antigo dos mapas isocerâunicos pode subestimar ou superestimar o risco real. O Ng por satélite/sensor é mais preciso e é o que a 2026 exige.
3. **Sabem que resistência de aterramento NÃO é mais medida:** muitas empresas ainda cobram ensaio de resistência de aterramento referenciando a norma anterior. A 2026 exige apenas continuidade com miliohmetro — mais barato e mais rápido.
4. **Aproveitam estrutura metálica como captor/descida natural:** a norma permite usar a armadura de concreto armado e estruturas metálicas como parte do SPDA, reduzindo significativamente o custo de instalação.

## Impacto no fluxo STTK

### Para Landell (Elétrica — principal)

- **No Levantamento:** verificar Ng municipal por satélite para o terreno do projeto. Se Ng for alto (> 5 raios/km²/ano), antecipar necessidade de SPDA no estudo preliminar.
- **No Anteprojeto:** fazer análise de risco conforme NBR 5419:2026. Definir nível de proteção (I a IV). Dimensionar malha de captação, descidas e aterramento conforme tabelas acima.
- **Na especificação:** cobre 35 mm² é o padrão mais seguro para captores, descidas e aterramento. Alumínio 70 mm² pode ser usado em captores/descidas se houver restrição de custo, mas NUNCA para aterramento.
- **Na verificação:** exigir apenas continuidade com miliohmetro, não resistência de aterramento. Reduz custo da medição e está conforme a norma vigente.

### Para Baumgart (Estrutural — cross)

- **Armadura como SPDA natural:** se a estrutura for em concreto armado, verificar se as armaduras podem ser usadas como parte do sistema de captação e descida (conexões entre barras devem garantir continuidade). Isso requer coordenação com Landell no detalhamento.
- **Fundação como aterramento:** a malha de aterramento pode ser integrada às fundações (estacas/sapatas com armadura contínua). Prever bitolas e conexões durante o projeto estrutural, não depois.

### Para Oscar (Arquitetura — cross)

- **Cobertura:** captores (hastes, cabos ou malha) ficam na cobertura. Se o projeto tiver cobertura inclinada, verificar com Landell a melhor posição para captores sem comprometer a estética.
- **Platibanda/beiral:** podem servir como suporte para cabo captor horizontal, desde que tenham altura suficiente para o raio da esfera rolante do nível de proteção especificado.

## O que NÃO muda

- A análise de risco continua sendo o ponto de partida — sem análise, não se define se precisa de SPDA.
- A NBR 5419 NÃO substitui o COSCIP/CBMERJ para instalações elétricas — cada norma cuida do seu escopo.
- A versão 2026 NÃO invalida SPDAs já instalados e aprovados conforme a versão 2015, desde que estejam dentro do prazo de inspeção (3 anos).

## Limitações desta Skill

1. **Texto integral da NBR 5419:2026 NÃO lido:** norma paga da ABNT. Parâmetros numéricos extraídos de artigos técnicos especializados (eletroproj.com.br). Confirmar valores com o texto original antes de aplicar em projeto real.
2. **Ng municipal não listado:** depende de dados de satélite/sensores para cada município. Obter junto ao INPE ou bases de dados meteorológicas locais (ex.: ELAT/INPE).
3. **Valores da versão 2001 NÃO usados:** foi identificada uma cópia da NBR 5419:2001 durante a pesquisa, mas por ser versão obsoleta (pré-2015, pré-2026), nenhum parâmetro dela foi utilizado.
4. **Errata de abril/2026:** a norma recebeu errata logo após publicação. Os parâmetros desta Skill refletem a versão corrigida conforme reportado por fontes técnicas, mas o texto exato da errata não foi lido.

## Fontes

- eletroproj.com.br — artigo técnico sobre NBR 5419:2026 (acessado 15/09/2026)
- NBR 5419:2026 (referenciada, parâmetros de fontes secundárias)
- INPE/ELAT — referência para dados Ng por satélite (não consultado diretamente)
- Cross-referência: NBR 5410 (instalações elétricas de baixa tensão), COSCIP/CBMERJ, LC 270/2024 (LICIN 2.0)
