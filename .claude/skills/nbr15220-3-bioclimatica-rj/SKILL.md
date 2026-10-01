---
name: nbr15220-3-bioclimatica-rj
description: NBR 15220-3:2024 — reclassificação do zoneamento bioclimático brasileiro de 8 para 12 zonas; Rio de Janeiro (município) mudou de categoria (ZB 8 → ZB 4A, confirmado no texto da Consulta Nacional ABNT jun/2024 e no mapa do LabEEE; texto final publicado ainda não lido), com impacto direto em CTpar (capacidade térmica) de vedações. Use sempre que qualquer Agente de Complementares (Tenreiro, Baumgart, Glaziou) ou de Arquitetura (futuro Agente de Estudo Preliminar, Lúcio) precisar confirmar a zona bioclimática de um projeto no RJ antes de especificar vedação, sistema construtivo, cobertura verde, ou dimensionar solução industrializada/modular (LSF, painel leve) — mesmo que o pedido só mencione "zona bioclimática", "desempenho térmico" ou "ZB", sem citar a norma pelo nome.
version: v1.2
---

# NBR 15220-3:2024 — Zoneamento Bioclimático (Rio de Janeiro mudou de categoria)

Skill de Inteligência Técnica cross-disciplina — **co-donos: Cardozo** (Complementares: Tenreiro, Baumgart, Glaziou) **e Lúcio** (Arquitetura: Oscar).

## ⚠️ Zona do Rio: ZB 4A confirmada no texto da Consulta Nacional — texto final ABNT ainda não lido

A NBR 15220-3:2024 substituiu o zoneamento de 8 zonas (ZB 1-8, vigente desde 2005) por 12 zonas com nomenclatura alfanumérica (1R, 1M, 2R, 2M, 3A, 3B, 4A, 4B, 5A, 5B, 6A, 6B). **O Rio de Janeiro (município) é 4A — "levemente quente e úmida"** (22,9 °C ≤ TBSm < 25,00 °C; UR > 70,3 %), e é a **cidade característica da zona 4A** (TBSm 24,38 °C; UR 75,01 %; estação WMO 837550, arquivo TMYx). Fonte: Projeto de Revisão ABNT NBR 15220-3, jun/2024 (texto da Consulta Nacional, CB-002), item 5.2.5.1 (p. 13), Tabela A.1 (p. 20) e tabela de arquivos climáticos (p. 23) — conferido por Lúcio em 01/10/2026; e mapa interativo do LabEEE (Lamberts, ENCAC 2025, slide 32).

**Limite:** o documento lido traz no rodapé "NÃO TEM VALOR NORMATIVO" — é o projeto de jun/2024, não o texto final publicado. Em memorial, citar "ZB 4A (NBR 15220-3:2024; confirmada no projeto da Consulta Nacional e no mapa LabEEE)". Não declarar "100% confirmado em texto oficial" até alguém ler a versão publicada (ABNT Catálogo/Target).

**O que É seguro afirmar:** o Rio saiu da ZB 8 — não usar "ZB 8" como referência para o Rio.

## Limbo de ~6 meses (jun-dez/2025)
O zoneamento novo (NBR 15220-3) já valia desde jun/2025, mas a NBR 15575 que o operacionaliza só emendou em dez/2025. Projetos protocolados nesse intervalo são ponto de atenção — checar qual critério foi de fato aplicado.

**Base escrita da transição (só no texto de projeto, jun/2024, p. 1 — prefácio):** "A ABNT NBR 15220-3:2024 não se aplica aos projetos de construção que tenham sido protocolados para aprovação no órgão competente pelo licenciamento anteriormente à data de sua publicação como Norma Brasileira, bem como àqueles que venham a ser protocolados no prazo de 180 dias após esta data, devendo, neste caso, ser utilizada a versão anterior da ABNT NBR 15220-3." Ou seja: o marco é a **data de protocolo** do projeto, não a data de início. Confirmar no texto publicado se essa cláusula ficou igual e qual é a data de publicação; as datas "jun/2025" e "dez/2025" acima seguem vindo de fonte secundária.

## Impacto direto na NBR 15575 (Desempenho)

A Emenda 1/2025 da NBR 15575 alinha os requisitos às 12 novas zonas:

| Requisito | Antes (ZB 8) | Agora (ZB 4A — ver aviso acima) |
|---|---|---|
| Capacidade Térmica (CTpar) | Isenta para sistemas de baixa inércia | **Obrigatória — mín. 130 kJ/(m².K)** para vedações |
| Temperatura Operativa Mínima | Verificação exigida | **Não exigida** — só a máxima |
| Isolamento em Cobertura | Obrigatório | **Não obrigatório** (mas desempenho térmico ainda precisa ser verificado por transmitância/CTpar) (isolante como premissa de desempenho: ver `cobertura-transmitancia-ucob-absortancia-atico-ventilado-nbr15575-5-rj`, §4) |

Sistemas de baixa inércia (Light Steel Frame, pré-moldados leves) que não atendem CTpar ≥ 130 prescritivamente **precisam de simulação computacional** para comprovar desempenho.

## Por Agente

**Tenreiro (Interiores):** transmitância e CTpar de paredes internas compartilhadas com envoltória passam a ter o requisito da nova zona (ZB 4A — ver aviso acima). NBR 8995-1 (iluminação) não muda — é por tarefa, não por zona.

**Baumgart (Estrutural):** a escolha do sistema construtivo tem implicação térmica que pode gerar exigência de simulação — concreto armado e alvenaria estrutural convencional geralmente atendem CTpar ≥ 130 sem problema; LSF e pré-moldados leves podem não atender.

**Glaziou (Paisagismo):** dimensionamento de cobertura verde (pesos já usados na Skill de paisagismo) permanece adequado, mas o memorial não deve referenciar ZB 8; citar ZB 4A com a forma indicada no aviso acima. Jardim de chuva e paisagismo exterior sem impacto direto.

## O que fazer

1. Retirar a referência a ZB 8 para o Rio (o Rio saiu da ZB 8). Usar ZB 4A citando a fonte (projeto da Consulta Nacional jun/2024 + mapa LabEEE), sem declarar "texto oficial confirmado" — ver aviso no topo e Macete M1
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
- F1 — Roberto Lamberts (LabEEE-UFSC, coordenador do GT Zoneamento, ABNT CB-002 CE 135.007), "Novo Zoneamento Bioclimático Brasileiro: NBR 15220-3 (2024)", XVIII ENCAC, São Carlos, 2025 — https://labeee.ufsc.br/sites/default/files/publicacoes/Encac25-zoneamento-lamberts.pdf (slides 24, 32, 33, 37, 41, 43-44; lidos por Wallenberg em 01/10/2026)
- F2 — Projeto de Revisão ABNT NBR 15220-3, jun/2024 (Consulta Nacional, "não tem valor normativo") — https://labeee.ufsc.br/sites/default/files/documents/zoneamento_projeto.pdf (pp. 1, 13, 20-21, 23; conferidas por Lúcio em 01/10/2026)
- Mapa interativo LabEEE — https://labeee.ufsc.br/zoneamento/

## Limitações honestas
Texto final publicado pela ABNT ainda não foi lido. A zona do Rio (4A) e a regra de transição estão no texto da Consulta Nacional (jun/2024) — fonte da própria comissão, mas sem valor normativo. Datas jun/2025 e dez/2025 seguem de fonte secundária. Slides de Lamberts (F1) lidos por Wallenberg; Lúcio não conseguiu abrir o PDF (arquivo > 10 MB) e conferiu só F2.

## Macetes de quem faz

**M1 — Confirmar a zona no mapa do LabEEE e citar a tabela da norma, não blog** (tipo A)
- O que fazer: conferir a zona do município no mapa interativo do LabEEE (https://labeee.ufsc.br/zoneamento/) e citar no memorial a tabela da NBR 15220-3 (Tabela A.1 / item 5.2.5.1), nunca blog ou artigo de divulgação.
- Por que funciona: amarra "ZB 4A" a um documento da comissão da ABNT. No projeto de jun/2024, Rio de Janeiro/RJ = 4A, cidade característica da zona (TBSm 24,38 °C, UR 75,01 %, WMO 837550, TMYx).
- Quem disse: Roberto Lamberts (coordenador do GT Zoneamento). Onde: F1 slide 32; F2 pp. 13, 20, 23.
- Limite: F2 é o projeto, não o texto final. Escrever "confirmado no texto da Consulta Nacional e no mapa LabEEE; texto final ainda não lido" — nunca "100% confirmado".

**M2 — A NBR 15220-3:2024 não traz diretrizes construtivas por zona** (tipo A)
- O que fazer: não escrever no memorial "estratégias recomendadas pela NBR 15220-3 para a zona do Rio". Ventilação cruzada, sombreamento e cores claras entram como boa prática de projeto; a comprovação de desempenho é pela NBR 15575 (procedimento simplificado ou simulação).
- Por que funciona: a versão 2005 trazia aberturas/vedações/sombreamento por zona (ex.: ZB 8); a 2024 não. Segundo Lamberts, as diretrizes "existiam na primeira consulta pública, mas a indústria pediu para retirar"; diretrizes para HIS ficaram com o projeto Hab.LabEEE. Coerente com F2, que só define as zonas (escopo, termos, zonas, tabelas).
- Quem disse: Roberto Lamberts. Onde: F1 slide 33.
- Limite: vale para a 2024. Diretrizes da 2005 só como referência histórica, citadas como tal ("NBR 15220-3:2005, versão anterior").

**M3 — Microclima da Barra/Recreio vira premissa, não troca de zona** (tipo A)
- O que fazer: a zona é a do município (Rio = 4A). Na Barra/Recreio (beira-mar e lagoas, longe da estação de referência), registrar o microclima (brisa marinha, umidade, ilha de calor) como premissa do partido ou da simulação e manter margem de desempenho.
- Por que funciona: Lamberts mostra que estações diferentes na mesma cidade e a ilha de calor urbana podem dar classificações diferentes; o zoneamento é por município (F2 p. 13 conta municípios por zona).
- Quem disse: Roberto Lamberts. Onde: F1 slides 37, 41, 44.
- Limite: o projeto não pode adotar outra zona para fugir de requisito. Microclima entra como premissa declarada, nunca como reclassificação.

Tipo B (fabricante): busca de Wallenberg em 01/10/2026 não achou guia de fabricante com autor credenciado para zona 4A — nenhum macete B.

## Escopo, crescimento e manutenção
Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.

## Histórico
- v1.0 — 01/09/2026 (convertida em Skill 03/09/2026).
- v1.1 — 28/09/2026 — coerência aprovada por Claudemberg: "O que fazer" item 1 deixou de mandar trocar ZB 8 por ZB 4A; tabela e notas por Agente marcam ZB 4A como indício não confirmado. Alinhada com `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj` v1.1. Backup: `01_CEO/Decisoes_Autonomas/_backups/2026-09-28/nbr15220-3_SKILL_pre-coerencia.md`.
- v1.2 — 01/10/2026 — Rotina de Macetes v1.2 (Wallenberg), validada e aplicada por Lúcio. **Cardozo é co-dono desta Skill** (cross Complementares/Arquitetura). Seção "Macetes de quem faz" nova (M1-M3, Lamberts/LabEEE). Ressalva da zona rebaixada de "indício não confirmado" para "confirmada no texto da Consulta Nacional jun/2024 e no mapa LabEEE; texto final não lido" (Lúcio conferiu F2 pp. 1, 13, 20-21, 23). Limbo ganhou a cláusula de transição do prefácio do projeto (marco = data de protocolo, 180 dias), marcada como texto de projeto. Fontes F1/F2 incluídas. Backup: `01_CEO/Decisoes_Autonomas/_backups/2026-10-01/macetes_ANTES_nbr15220-3-bioclimatica-rj_SKILL_instalada.md`.
