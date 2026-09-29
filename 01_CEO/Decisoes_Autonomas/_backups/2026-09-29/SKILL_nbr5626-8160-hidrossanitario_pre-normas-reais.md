---
name: nbr5626-8160-hidrossanitario
description: NBR 5626:2020 (água fria/quente), NBR 8160:1999 (esgoto sanitário), NBR 10844:1989 (águas pluviais) e correlatas — dimensionamento de instalações hidrossanitárias prediais. Use sempre que Saturnino (ou qualquer Agente) for dimensionar ramais de água, esgoto, calhas pluviais, reservatório, ventilação de esgoto, ou verificar pressão/velocidade em tubulação — mesmo que o pedido só mencione "hidráulica", "esgoto", "caixa d'água" ou "drenagem", sem citar a norma pelo nome.
version: v1.1
---

# NBR 5626/8160/10844 — Hidrossanitário Predial

Skill de Inteligência Técnica da área Hidrossanitário, equipe de Cardozo (Gestor Complementares). Quem consome: **Saturnino** (Agente Hidrossanitário).

## Normas-base

| Norma | Assunto | Versão vigente |
|-------|---------|----------------|
| NBR 5626:2020 | Água fria e quente — projeto/execução/manutenção | 2020 (unificou 5626 antiga + 7198) |
| NBR 8160:1999 | Esgoto sanitário — projeto e execução | 1999 — **confirmar se houve revisão antes de protocolar** |
| NBR 10844:1989 | Águas pluviais | 1989 — **confirmar se houve revisão antes de protocolar** |
| NBR 9649 | Redes coletoras de esgoto sanitário | Vigente |
| NBR 7229 | Fossas sépticas | Vigente |

## 1. Água fria/quente (NBR 5626:2020)

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

**⚠️ Valores acima só para os aparelhos padrão da tabela.** Se o Briefing especificar aparelho fora da lista (spa, hidromassagem, torneira privativa), esses têm valor próprio — não extrapole por analogia sem confirmar na norma.

**Reservatório:** mínimo 1 dia de consumo (200 L/habitante, salvo código de obras local diferente). Superior por gravidade (mín. 2 mca no ponto mais desfavorável); inferior para sucção de bomba.

**Proibido:** tubulação de água potável em contato com esgoto; conexão direta rede pública/reservatório sem caixa intermediária.

## 2. Esgoto sanitário (NBR 8160:1999)

**Dimensionamento:** inclinação mínima 2% (DN ≤ 100mm) ou 1% (DN > 100mm). Velocidade crítica de autolimpeza ≥ 0,6 m/s. Grau de enchimento máximo 75% da seção.

| Aparelho | UHE | DN mínimo do ramal |
|---|---|---|
| Lavatório | 1 | 40mm |
| Vaso sanitário (caixa) | 4 | 100mm |
| Vaso sanitário (válvula) | 6 | 100mm |
| Chuveiro | 2 | 40mm |
| Banheira | 3 | 50mm |
| Pia de cozinha | 2 | 50mm |
| Máquina de lavar roupa | 3 | 50mm |

**Regra de ouro: ramal de esgoto de vaso sanitário nunca abaixo de DN 100mm.**

Ventilação: primária obrigatória (prolongamento do tubo de queda acima da cobertura), sempre; secundária (coluna de ventilação) obrigatória se atende mais de 5 andares. Sem ventilação adequada → sifonamento e mau cheiro.

## 3. Águas pluviais (NBR 10844:1989)

Fórmula de calha: **Q = C × I × A / 360** — Q vazão (L/s), C coeficiente de escoamento (telha cerâmica 0,90; concreto/impermeabilizado 0,95), I intensidade de chuva (mm/h, curva IDF local), A área de contribuição (m²).

**⚠️ A intensidade de chuva para o Rio de Janeiro (~150 mm/h para TR=5 anos usada como referência) é aproximação — confirme os dados atuais de INMET/Prefeitura antes de dimensionar calha de projeto real, não use este número de cabeça.**

Calha horizontal: inclinação mínima 0,5%, velocidade máx. 1,5 m/s. Condutor pluvial sempre separado do esgoto sanitário — interligação proibida.

## Checklist prático ao receber Briefing (via Cardozo, vindo de Lúcio)
1. Pavimentos, unidades, tipologia
2. Pontos de utilização por unidade/andar → ΣUP e ΣUHE
3. Pressão disponível na rede pública
4. Volume de reservatório (≥ 1 dia de consumo)
5. Pressão > 400 kPa em algum ponto? → VRP
6. Dimensionar água fria/quente (Hunter adaptado)
7. Dimensionar esgoto (mín. DN 100 para vaso)
8. Inclinações de esgoto conforme DN
9. Ventilação de esgoto (primária sempre, secundária se >5 andares)
10. Calhas/condutores pluviais com IDF local RJ confirmado
11. Confirmar separação absoluta pluvial/esgoto

**Erros comuns:** interligar esgoto e pluvial (proibido) · omitir VRP em prédio alto · omitir ventilação de esgoto · inclinação insuficiente (<2%) · ramal de vaso <DN100.

## Coordenação com outros Agentes de Cardozo
Baumgart (shafts/furos, layout antes do detalhamento estrutural) · Landell (separação física água/eletroduto — distância de 30 cm e atribuição à NBR 5410 **a confirmar (fonte não verificada)**; não citar em memorial como exigência normativa) · Glaziou (raízes que ameaçam tubulação externa, tipo de tubo/proteção) · Mindlin (layout de shafts e esquemas verticais legíveis para prancha).

## O que esta Skill NÃO cobre
Combate a incêndio/hidrantes (NBR 13714) · gás predial (NBR 15526) · tratamento de efluentes/ETE · reuso de água cinza (checar código de obras municipal).

## Limitações honestas
- NBR 8160 (1999) e NBR 10844 (1989) — confirmar se houve revisão/emenda publicada antes de protocolar em caso real.
- Valores de UP/UHE são das tabelas normativas padrão — aparelho fora da lista tem valor próprio, não extrapolar.
- IDF de 150mm/h para RJ é referência aproximada, não definitiva.
- Texto oficial ABNT não foi lido diretamente — fontes técnicas secundárias verificadas em 28/08/2026.

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.

## Histórico
- v1.0 — 28/08/2026 (convertida em Skill 03/09/2026).
- v1.1 — 28/09/2026 — coerência aprovada por Claudemberg: "30 cm água/eletroduto, exigência NBR 5410" marcado "a confirmar (fonte não verificada)". Nenhuma fonte primária localizada; não inventada.
