# NBR 6118:2026 com Emenda 1 — Skill de Inteligência Técnica Estrutural

## Para qual Agente serve
**Baumgart** (Estrutural) — equipe de Cardozo (Gestor Complementares). Esta é uma Skill de **Trilha A (Inteligência)**: normas técnicas e técnicas de projetar, não ferramenta de software. Alimenta o saber-fazer de Baumgart em projetos de estruturas de concreto armado (fundações, vigas, pilares, lajes).

## Status
proposta — aguardando ratificação de Claudemberg

## O que esta Skill ensina

### Contexto da Norma
A **NBR 6118:2026** é a versão vigente da norma de projeto de estruturas de concreto armado e protendido no Brasil. A **Emenda 1 foi publicada em 11 de março de 2026**, atualizando a NBR 6118:2023. O Baumgart já referencia CC1/CC2/CC3 em seu frontmatter — esta Skill consolida o que cada classe significa na prática e o que mudou.

**Regra de transição:** projetos protocolados para aprovação **antes de março/2026**, ou nos **180 dias seguintes**, podem continuar sob NBR 6118:2023. Projetos novos após esse prazo: obrigatoriamente NBR 6118:2026.

---

### 1. Classes de Consequência (CC) — Obrigatório definir no início

| Classe | Exemplos | O que exige |
|--------|----------|-------------|
| CC1 | Residências unifamiliares até 2 pavimentos | Requisitos mínimos — sem ATP obrigatória |
| CC2 | Edifícios até 5 pavimentos, pequenas reformas | Verificação padrão |
| CC3 | Edifícios >5 pavimentos, subsolos, marquises, estruturas protendidas, reformas com eliminação de pilares | **ATP obrigatória + revisor independente** |

**Ação prática:** ao receber Briefing de Lúcio, a primeira pergunta de Baumgart é: "Qual a CC desta estrutura?" — define toda a estratégia de projeto e exigências de revisão.

---

### 2. Avaliação Técnica de Projeto (ATP) — Nova exigência CC3

A ATP (revisão independente de projeto estrutural) passa a ser **regra geral para CC3**. O avaliador deve emitir parecer formal que integra o projeto entregue.

- Não se aplica a CC1 e CC2 em regime normal
- Para marquises: CC3 por padrão, ATP obrigatória
- O parecer do ATP é parte do projeto, não opcional

---

### 3. Durabilidade e Agressividade Ambiental

- O **contratante (cliente)** deve fornecer explicitamente a **Classe de Agressividade Ambiental (CAA)** e as condições de exposição antes do projeto
- A norma reforça: durabilidade é "capacidade de resistir às influências ambientais definidas no início do projeto"
- **Novo:** controle de temperatura em grandes volumes de concreto — risco de formação tardia de etringita acima de ~65°C (relevante para blocos de fundação de grande porte)

**Cobrimentos mínimos por CAA:** manter os valores da NBR 6118:2023, agora com maior ênfase na responsabilidade do contratante em definir a CAA antes do início.

---

### 4. Dimensionamento — Mudanças Práticas

#### Emendas de Armadura
- Traspasse **proibido acima de Ø32 mm** — usar luvas mecânicas
- Luvas mecânicas: resistência mínima **15% superior** à resistência de escoamento da barra

#### Redistribuição de Esforços
- Limite geral: **δ ≥ 0,75** (redução máxima de 25% dos momentos elásticos)
- Verificar sempre se o detalhamento suporta a redistribuição adotada

#### Lajes em Balanço e Marquises (CRÍTICO)
- **Nova armadura inferior de segurança** dimensionada para suportar ações permanentes
- Funciona como mecanismo residual contra colapso total (aprendizado pós-colapso de marquises no Brasil)
- Não é opcional — é exigência de segurança estrutural

#### Punção (Lajes)
- Armadura inferior deve **atravessar a laje e estar ancorada além do contorno crítico**
- Estribos suplementares: ganchos de **135° a 180°**

#### Pilares de Borda
- Emenda reorganiza equações para pilares de borda — distingue casos específicos, reduzindo risco de aplicação incorreta do momento efetivo no perímetro crítico

---

### 5. Detalhamento — Regras Revisadas

| Item | Regra NBR 6118:2026 |
|------|---------------------|
| Armadura positiva secundária | Mínimo 20% da principal; espaçamento máx. 33 cm |
| Telas soldadas nervuradas | Ancoragem mínima 10φ (≥10 cm) |
| Frequência natural mínima de pisos | **3 Hz** (verificar conforto de vibração) |
| Ganchos de estribos | 135° a 180° (não mais 90° em elementos críticos) |

---

### 6. Checklist Prático para Baumgart (início de todo projeto)

- [ ] Definir Classe CC (CC1/CC2/CC3) antes de qualquer cálculo
- [ ] Se CC3: contratar e registrar ATP (revisor independente)
- [ ] Solicitar ao cliente/Lúcio a CAA e condições de exposição
- [ ] Verificar se há balanços/marquises → armadura inferior de segurança obrigatória
- [ ] Verificar se há emendas de armadura >Ø32 mm → usar luvas mecânicas
- [ ] Calcular redistribuição de esforços com δ ≥ 0,75
- [ ] Conferir punção em lajes com armadura além do contorno crítico
- [ ] Verificar frequência natural de pisos (mín. 3 Hz)
- [ ] Atualizar detalhes padrão (ganchos 135-180°, armadura secundária 20% da principal)
- [ ] Conferir se projeto está na janela de transição (180 dias pós-março/2026)

---

## O que esta Skill NÃO cobre
- Cálculo de fundações (NBR 6122 — assunto separado)
- Estruturas metálicas (NBR 8681)
- Estruturas de madeira (NBR 7190)
- Detalhamento completo de todos os elementos — ver a norma na íntegra para detalhes específicos

## Limitações honestas
- Esta Skill é baseada em fontes secundárias (blogs técnicos especializados) que analisam a norma. O texto oficial completo da NBR 6118:2026 é pago (ABNT) e não foi verificado diretamente. Para casos críticos (CC3, marquises, protensão), Baumgart deve consultar o texto normativo oficial.
- Valores de cobrimento não foram atualizados explicitamente — verificar se houve alteração em relação à versão 2023.

## Fontes
- blog.apl.eng.br — "NBR 6118:2026: o que mudou com a revisão" (verificado por WebFetch em 28/08/2026)
- masteremmodelagem.com.br — "NBR 6118:2026 — Principais mudanças, Emenda 1" (busca WebSearch em 28/08/2026)
- sienge.com.br/blog/nbr-6118 (WebSearch em 28/08/2026)
- Data da Emenda 1: 11 de março de 2026 (confirmado em múltiplas fontes)
