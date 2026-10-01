---
name: nbr15220-3-bioclimatica-rj
description: NBR 15220-3:2024 — reclassificação do zoneamento bioclimático brasileiro de 8 para 12 zonas; Rio de Janeiro (município) mudou de categoria (indício não confirmado em fonte primária: ZB 8 → ZB 4A), com impacto direto em CTpar (capacidade térmica) de vedações. Use sempre que qualquer Agente de Complementares (Tenreiro, Baumgart, Glaziou) ou de Arquitetura (futuro Agente de Estudo Preliminar, Lúcio) precisar confirmar a zona bioclimática de um projeto no RJ antes de especificar vedação, sistema construtivo, cobertura verde, ou dimensionar solução industrializada/modular (LSF, painel leve) — mesmo que o pedido só mencione "zona bioclimática", "desempenho térmico" ou "ZB", sem citar a norma pelo nome.
version: v1.1
---

# NBR 15220-3:2024 — Zoneamento Bioclimático (Rio de Janeiro mudou de categoria)

Skill de Inteligência Técnica cross-disciplina, equipes de Cardozo (Complementares: Tenreiro, Baumgart, Glaziou) e de Lúcio (Arquitetura: futuro Agente de Estudo Preliminar).

## ⚠️ O código exato da nova zona do Rio NÃO está confirmado em fonte primária

A NBR 15220-3:2024 substituiu o zoneamento de 8 zonas (ZB 1-8, vigente desde 2005) por 12 zonas com nomenclatura alfanumérica (1R, 1M, 2R, 2M, 3A, 3B, 4A, 4B, 5A, 5B, 6A, 6B). **O Rio de Janeiro mudou de categoria bioclimática** — isso está confirmado por fonte técnica (CBCS). Mas o código específico **"ZB 4A"** vem de uma **única fonte secundária** (blog Lato Qualitas), citada igualmente nas duas rodadas de pesquisa que originaram esta Skill (22/07 e 01/09/2026) — não é duas confirmações independentes, é a mesma fonte fraca repetida duas vezes. Nenhuma rodada confirmou o código na ferramenta oficial.

**Antes de usar "ZB 4A" como parâmetro em memorial, cálculo ou peça de cliente real: confirme na ferramenta oficial "Busca ZB"** (normadedesempenho.com.br/busca-zb, cobre os 5.507 municípios) ou no relatório técnico ABNT TR 15220-3-1. Não trate "ZB 4A" como fato fechado só porque aparece neste documento.

**O que É seguro afirmar sem essa confirmação:** não usar "ZB 8" como referência para o Rio a partir de agora — isso está sólido (múltiplas fontes técnicas confirmam a mudança de categoria, mesmo sem cravar o código exato).

## Limbo de ~6 meses (jun-dez/2025)
O zoneamento novo (NBR 15220-3) já valia desde jun/2025, mas a NBR 15575 que o operacionaliza só emendou em dez/2025. Projetos protocolados nesse intervalo são ponto de atenção — checar qual critério foi de fato aplicado.

## Impacto direto na NBR 15575 (Desempenho)

A Emenda 1/2025 da NBR 15575 alinha os requisitos às 12 novas zonas:

| Requisito | Antes (ZB 8) | Agora (ZB 4A — indício não confirmado) |
|---|---|---|
| Capacidade Térmica (CTpar) | Isenta para sistemas de baixa inércia | **Obrigatória — mín. 130 kJ/(m².K)** para vedações |
| Temperatura Operativa Mínima | Verificação exigida | **Não exigida** — só a máxima |
| Isolamento em Cobertura | Obrigatório | **Não obrigatório** (mas desempenho térmico ainda precisa ser verificado por transmitância/CTpar) (isolante como premissa de desempenho: ver `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj`, §4) |

Sistemas de baixa inércia (Light Steel Frame, pré-moldados leves) que não atendem CTpar ≥ 130 prescritivamente **precisam de simulação computacional** para comprovar desempenho.

## Por Agente

**Tenreiro (Interiores):** transmitância e CTpar de paredes internas compartilhadas com envoltória passam a ter o requisito da nova zona (indício: ZB 4A, não confirmado). NBR 8995-1 (iluminação) não muda — é por tarefa, não por zona.

**Baumgart (Estrutural):** a escolha do sistema construtivo tem implicação térmica que pode gerar exigência de simulação — concreto armado e alvenaria estrutural convencional geralmente atendem CTpar ≥ 130 sem problema; LSF e pré-moldados leves podem não atender.

**Glaziou (Paisagismo):** dimensionamento de cobertura verde (pesos já usados na Skill de paisagismo) permanece adequado, mas o memorial não deve referenciar ZB 8; a nova zona fica "a confirmar (indício: ZB 4A)" até a fonte primária. Jardim de chuva e paisagismo exterior sem impacto direto.

## O que fazer

1. Retirar a referência a ZB 8 para o Rio (o Rio saiu da ZB 8). Não substituir automaticamente por "ZB 4A": é indício não confirmado até ler a fonte primária (ABNT ou ferramenta "Busca ZB"). Até lá, o memorial registra "zona a confirmar (indício: ZB 4A)"
2. Verificar CTpar ≥ 130 kJ/(m².K) para vedações de envoltória em projeto residencial novo no RJ
3. Documentar adoção da Emenda 1/2025 em projetos iniciados após dezembro/2025
4. Não usar "padrão histórico" de ZB 8 — inválido desde 2024

## Período de transição
Intervalo de 6 meses entre a vigência da NBR 15220-3 (2024) e as emendas da NBR 15575 (dezembro/2025). Projetos aprovados nesse intervalo devem documentar qual versão adotaram, para defesa técnico-legal.

## Fontes
- NBR 15220-3:2024 — ABNT (texto oficial via Target/ABNT Catálogo)
- CBCS — "Novo zoneamento bioclimático amplia precisão..." (21/10/2025)
- Lato Qualitas — "5 Mudanças na NBR 15575 que Você Não Pode Ignorar em 2026" (30/01/2026)
- NBR 15575 Emenda 1/2025 — ABNT

## Limitações honestas
Texto oficial ABNT não foi lido diretamente — fontes técnicas secundárias, verificadas em 01/09/2026.

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.

## Histórico
- v1.0 — 01/09/2026 (convertida em Skill 03/09/2026).
- v1.1 — 28/09/2026 — coerência aprovada por Claudemberg: "O que fazer" item 1 deixou de mandar trocar ZB 8 por ZB 4A; tabela e notas por Agente marcam ZB 4A como indício não confirmado. Alinhada com `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj` v1.1. Backup: `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/nbr15220-3_SKILL_pre-coerencia.md`.
