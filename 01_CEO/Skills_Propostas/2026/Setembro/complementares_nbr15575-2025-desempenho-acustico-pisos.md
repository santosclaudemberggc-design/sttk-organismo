# NBR 15575:2025 — Desempenho Acústico de Sistemas de Pisos

## Para qual Gestor/Agente serve

**Cardozo (Complementares)** — cross-disciplina entre 3 Agentes:
- **Baumgart (Estrutural):** responsável pela laje/sistema estrutural de piso — a escolha de tipologia (maciça, nervurada, steel deck, LSF) determina o desempenho acústico de base.
- **Saturnino (Hidrossanitário):** tubulações que atravessam pisos entre pavimentos criam pontes acústicas — o tratamento de passantes e o encamisamento são exigência direta desta norma.
- **Tenreiro (Interiores):** especificação de revestimento e contrapiso — pisos flutuantes, mantas acústicas, contrapiso dessolidarizado são as soluções mais comuns para atender L'nT,w.

Complementarmente: **Lúcio/Oscar** — a definição de layout e programa de necessidades influencia quais ambientes ficam sobrepostos e quais critérios se aplicam.

## Tipo

**Inteligência (Trilha A)** — norma técnica ABNT, conhecimento de projetar.

## Status

ratificada — 03/09/2026, Claudemberg (rodada de auditoria com Wallenberg)

**Convertida em Skill real em 03/09/2026:** `.claude/skills/nbr15575-acustico-pisos/SKILL.md`

## Versão

v1.0 — 03/09/2026

## O que esta Skill ensina

A ABNT NBR 15575 (Edificações Habitacionais — Desempenho) teve sua revisão publicada em dezembro de 2024, em vigor desde junho de 2025 (180 dias de adaptação). A Parte 3 (Sistemas de Pisos) traz alterações relevantes nos critérios de desempenho acústico.

### Principal novidade da versão 2025

**Inclusão de ambientes sem dormitório:** a versão anterior (2013/2021) exigia desempenho acústico obrigatório apenas para pisos entre unidades autônomas sobrepostas com dormitório receptor. A versão 2025 **estende o requisito para ambientes onde NÃO há dormitório** — salas, cozinhas, corredores e até banheiros agora têm critério de desempenho mínimo obrigatório para ruído aéreo entre unidades.

Isso impacta diretamente o dimensionamento de lajes e a especificação de revestimentos em TODOS os pavimentos-tipo, não apenas nos andares com dormitórios sobrepostos.

### Parâmetros de medição

- **DnT,w [dB]** — Diferença padronizada de nível ponderada: mede isolamento ao ruído aéreo entre ambientes sobrepostos. Quanto MAIOR, melhor.
- **L'nT,w [dB]** — Nível de pressão sonora de impacto padronizado ponderado: mede transmissão de ruído de impacto (passos, arraste de móveis, queda de objetos). Quanto MENOR, melhor.

### Vias de transmissão

O ruído aéreo entre unidades sobrepostas viaja por **1 via direta** (pela laje) e **12 vias indiretas** (pelas paredes laterais, estrutura, etc.). O ruído de impacto viaja por **1 via direta** e **4 vias indiretas**. Isso significa que isolar o piso sem tratar as paredes é insuficiente.

### Tabela de requisitos — Ruído Aéreo (DnT,w)

**Pisos entre unidades autônomas sobrepostas:**

| Nível de Desempenho | Critério | Observação |
|---------------------|----------|------------|
| M (Mínimo) | DnT,w ≥ 45 dB | Obrigatório por lei |
| I (Intermediário) | DnT,w ≥ 50 dB | Voluntário, diferencial competitivo |
| S (Superior) | DnT,w ≥ 55 dB | Voluntário, premium |

### Tabela de requisitos — Ruído de Impacto (L'nT,w)

**Pisos entre unidades autônomas sobrepostas:**

| Nível de Desempenho | Critério | Observação |
|---------------------|----------|------------|
| M (Mínimo) | L'nT,w ≤ 80 dB | Obrigatório por lei |
| I (Intermediário) | L'nT,w ≤ 72 dB | Voluntário |
| S (Superior) | L'nT,w ≤ 63 dB | Voluntário |

### Impacto por disciplina

#### Baumgart (Estrutural)
- Laje maciça de concreto (e ≥ 10 cm) atende DnT,w ≥ 45 dB na maioria dos casos, mas NÃO garante L'nT,w ≤ 80 dB sozinha — necessita tratamento complementar.
- Lajes nervuradas e steel deck têm massa menor por m² e geralmente exigem forro acústico ou contrapiso flutuante para atingir M.
- Sistemas LSF (Light Steel Frame) — já problematizados na Skill de NBR 15220-3:2024 para zona 4A — exigem simulação computacional também para acústica.

#### Saturnino (Hidrossanitário)
- Tubulações verticais (prumadas) que atravessam lajes entre unidades são pontes acústicas. Encamisamento com luva resiliente e vedação com material viscoelástico são exigência prática.
- Caixas sifonadas, ralos e registros embutidos no piso transmitem ruído de impacto direto — devem ser dessolidarizados da laje.
- Bombas de recalque e pressurizadores em cobertura/subsolo: fixação com amortecedores de vibração.

#### Tenreiro (Interiores)
- Contrapiso flutuante (dessolidarizado da laje estrutural por manta resiliente) é a solução mais comum para reduzir L'nT,w.
- Espessura e tipo de manta: polietileno expandido (≥ 5 mm), lã de rocha, borracha reciclada. Cada material tem frequência de ressonância diferente.
- Piso colado vs. piso flutuante: piso cerâmico colado diretamente no contrapiso transmite mais impacto; piso vinílico ou laminado sobre manta absorve parte.
- Rodapés e arremates: o piso flutuante NÃO pode ter contato rígido com as paredes (deixar junta de dilatação coberta pelo rodapé), senão vira ponte acústica.

### Ensaio obrigatório

O ensaio de desempenho acústico é realizado **em campo** (in-loco), não em laboratório, conforme metodologias ISO 16283-1 (ruído aéreo) e ISO 16283-2 (ruído de impacto). Deve ser contratado pelo incorporador/construtor antes da entrega da unidade.

## Limitações honestas

- Os valores numéricos exatos para ambientes sem dormitório na versão 2025 não estão publicados em fonte aberta (a norma ABNT é documento pago). Os valores M/I/S acima (45/50/55 dB e 80/72/63 dB) são para pisos entre unidades sobrepostas com qualquer ambiente receptor — confirmar na norma completa se há diferenciação por tipo de ambiente.
- Esta Skill não substitui a consulta à norma ABNT oficial pela equipe de projeto.

## Fonte

- [NBR 15575 Desempenho Acústico — Ca2 Consultores](https://ca-2.com/nbr-15575-requisitos-de-desempenho-acustico/) — verificada em 03/09/2026
- [NBR 15575 Desempenho Acústico — Scala Acústica](https://scaladb.com.br/nbr-15575-desempenho-acustico-em-edificacoes/) — verificada em 03/09/2026
- [NBR 15575 Norma de Desempenho — Sienge](https://sienge.com.br/blog/o-que-e-nbr-15575/) — verificada em 03/09/2026
- [NBR 15575:2025 — ProAcústica/INTERLAB](https://www.proacustica.org.br/interlab//norma) — verificada em 03/09/2026
