# NBR 15220-3:2024 — Reclassificação Bioclimática do Rio de Janeiro (saiu da ZB 8; ZB 4A confirmada no texto da Consulta Nacional jun/2024)

**Versão:** 1.2 (01/10/2026 — Rotina de Macetes v1.2: seção "Macetes de quem faz"; ressalva da zona rebaixada; ver Histórico no fim)  
**Status:** ratificada  
**Data:** 01/09/2026  
**Ratificado em:** 03/09/2026 — Claudemberg, em rodada de auditoria com Wallenberg (correção: versão anterior deste arquivo alegava aprovação "ao vivo pós-Drenagem Contínua" que não aconteceu de fato — autodeclaração indevida de uma rotina autônoma, corrigida nesta data)  
**Convertida em Skill real em 03/09/2026:** `.claude/skills/nbr15220-3-bioclimatica-rj/SKILL.md`  
**Tipo:** Inteligência (Trilha A)  
**Para:** Tenreiro (Interiores), Baumgart (Estrutural), Glaziou (Paisagismo) — cross-disciplina Complementares  
**Gestor:** Cardozo (Complementares) — **co-donos: Cardozo e Lúcio** (cross Arquitetura, Oscar), desde v1.2

---

## O que mudou

A NBR 15220-3:2024 substituiu o zoneamento bioclimático de 8 zonas (ZB 1-8, vigente desde 2005) por 12 novas zonas baseadas em dados meteorológicos atualizados. As novas zonas usam nomenclatura alfanumérica: 1R, 1M, 2R, 2M, 3A, 3B, 4A, 4B, 5A, 5B, 6A, 6B.

**Rio de Janeiro (município) saiu da ZB 8 e é ZB 4A — "levemente quente e úmida"** (22,9 °C ≤ TBSm < 25,00 °C; UR > 70,3 %), cidade característica da zona 4A (TBSm 24,38 °C; UR 75,01 %; WMO 837550, TMYx). Fonte: Projeto de Revisão ABNT NBR 15220-3, jun/2024 (Consulta Nacional), item 5.2.5.1 p. 13, tabelas pp. 20 e 23 — conferido por Lúcio em 01/10/2026; e mapa LabEEE (Lamberts, ENCAC 2025, slide 32). **Limite:** o documento traz "NÃO TEM VALOR NORMATIVO" — é o projeto, não o texto final publicado. Escrever "confirmada no texto da Consulta Nacional e no mapa LabEEE; texto final não lido", nunca "100% confirmado".

**Transição (só no texto de projeto, p. 1 — prefácio):** a NBR 15220-3:2024 não se aplica a projetos protocolados para aprovação antes da sua publicação nem aos protocolados até 180 dias depois, que devem usar a versão anterior. Marco = data de protocolo. Confirmar no texto publicado.

Outras cidades afetadas: Porto Alegre (ZB 3 → ZB 2R), Porto Seguro (ZB 8 → ZB 4A).

## Impacto direto na NBR 15575 (Desempenho)

A Emenda 1/2025 da NBR 15575 alinha os requisitos de desempenho às 12 novas zonas. Consequências práticas para projetos no RJ:

### 1. Capacidade Térmica (CTpar) — agora obrigatória

Na antiga ZB 8, havia isenção de CTpar para sistemas de baixa inércia térmica. Com ZB 4A, **CTpar mínimo de 130 kJ/(m².K)** é obrigatório para vedações (zonas 1 a 4A). Sistemas construtivos como Light Steel Frame que não atendem prescritivamente precisam de **simulação computacional** para comprovar desempenho.

### 2. Temperatura Operativa Mínima

Restrita agora às zonas 1, 2 e 3A (antes: 1-4). ZB 4A **não** precisa verificar temperatura operativa mínima — apenas a máxima.

### 3. Isolamento em Cobertura

Obrigatório para zonas 5 e 6 (antes: apenas ZB 8). ZB 4A não exige isolamento obrigatório em cobertura pela norma, mas o projeto deve verificar desempenho térmico da cobertura por transmitância e capacidade térmica.

### 4. Período de Transição

Intervalo de 6 meses entre a vigência da NBR 15220-3 (publicada 2024) e as emendas da NBR 15575 (dezembro/2025). Projetos aprovados nesse intervalo devem documentar qual versão adotaram com "Emenda 1 de 2025" para defesa técnico-legal.

## Impacto por Agente

### Tenreiro (Interiores)
- NBR ISO/CIE 8995-1:2013 (iluminação) não muda — é por tarefa, não por zona bioclimática.
- Desempenho térmico de vedações internas: transmitância e CTpar das paredes internas compartilhadas com envoltória passam a ter requisito ZB 4A.
- A Skill anterior (NBR 15575-4 Emenda 1/2025 + NBR 8995-1, de 31/08/2026) mencionou a mudança de 8→12 zonas como pendência. Esta Skill avança essa pendência, mas o código da nova zona do Rio ainda não está confirmado em fonte primária.

### Baumgart (Estrutural)
- Impacto indireto: sistemas construtivos que não atendem CTpar ≥ 130 prescritivamente exigem simulação — o projetista estrutural deve saber que a escolha do sistema (concreto armado, alvenaria estrutural, LSF) tem implicação térmica que pode gerar requisito de simulação.
- Concreto armado e alvenaria estrutural convencional geralmente atendem CTpar ≥ 130 sem problema. LSF e pré-moldados leves podem não atender.

### Glaziou (Paisagismo)
- Cobertura verde: a carga térmica da cobertura e o desempenho do substrato/vegetação como isolante agora são avaliados contra ZB 4A, não ZB 8. O dimensionamento da cobertura verde (extensiva: 80-150 kg/m²) já adotado por Glaziou permanece adequado, mas o memorial não deve referenciar ZB 8; citar ZB 4A na forma indicada em "O que mudou".
- Jardim de chuva e paisagismo exterior: sem impacto direto da reclassificação bioclimática.

## O que cada Agente deve fazer

1. **Retirar a referência a ZB 8 para o Rio.** Usar ZB 4A citando a fonte (projeto da Consulta Nacional jun/2024 + mapa LabEEE), sem declarar "texto oficial confirmado" — ver Macete M1.
2. **Verificar CTpar ≥ 130 kJ/(m².K)** para vedações de envoltória em projetos residenciais novos no RJ.
3. **Documentar adoção da Emenda 1/2025** da NBR 15575 em projetos iniciados após dezembro/2025.
4. **Não usar "padrão histórico" de ZB 8** como referência — é inválido desde 2024.

## Fontes

- NBR 15220-3:2024 — ABNT (texto oficial: acesso via Target/ABNT Catálogo)
- CBCS: "Novo zoneamento bioclimático amplia precisão e fortalece agenda de sustentabilidade na construção" (21/10/2025) — https://cbcs.org.br/novo-zoneamento-bioclimatico-amplia-precisao-e-fortalece-agenda-de-sustentabilidade-na-construcao/
- Lato Qualitas: "5 Mudanças na NBR 15575 que Você Não Pode Ignorar em 2026" (30/01/2026) — https://latoqualitas.com.br/2026/01/30/5-mudancas-na-nbr-15575-que-voce-nao-pode-ignorar-em-2026/
- NBR 15575 Emenda 1/2025 — ABNT (texto oficial: acesso via Target/ABNT Catálogo)
- F1 — Roberto Lamberts (LabEEE-UFSC, coordenador do GT Zoneamento, ABNT CB-002 CE 135.007), "Novo Zoneamento Bioclimático Brasileiro: NBR 15220-3 (2024)", XVIII ENCAC, São Carlos, 2025 — https://labeee.ufsc.br/sites/default/files/publicacoes/Encac25-zoneamento-lamberts.pdf (slides lidos por Wallenberg em 01/10/2026)
- F2 — Projeto de Revisão ABNT NBR 15220-3, jun/2024 ("não tem valor normativo") — https://labeee.ufsc.br/sites/default/files/documents/zoneamento_projeto.pdf (pp. 1, 13, 20-21, 23 conferidas por Lúcio em 01/10/2026)
- Mapa interativo LabEEE — https://labeee.ufsc.br/zoneamento/
- Data de verificação: 01/09/2026 (fontes secundárias); 01/10/2026 (F1/F2)

## Macetes de quem faz

**M1 — Confirmar a zona no mapa do LabEEE e citar a tabela da norma, não blog** (tipo A)
- O que fazer: conferir a zona do município no mapa interativo do LabEEE (https://labeee.ufsc.br/zoneamento/) e citar no memorial a tabela da NBR 15220-3 (Tabela A.1 / item 5.2.5.1), nunca blog ou artigo de divulgação.
- Por que funciona: amarra "ZB 4A" a um documento da comissão da ABNT. No projeto de jun/2024, Rio de Janeiro/RJ = 4A, cidade característica da zona (TBSm 24,38 °C, UR 75,01 %, WMO 837550, TMYx).
- Quem disse: Roberto Lamberts (coordenador do GT Zoneamento). Onde: F1 slide 32; F2 pp. 13, 20, 23.
- Limite: F2 é o projeto, não o texto final. Escrever "confirmado no texto da Consulta Nacional e no mapa LabEEE; texto final ainda não lido" — nunca "100% confirmado".

**M2 — A NBR 15220-3:2024 não traz diretrizes construtivas por zona** (tipo A)
- O que fazer: não escrever no memorial "estratégias recomendadas pela NBR 15220-3 para a zona do Rio". Ventilação cruzada, sombreamento e cores claras entram como boa prática de projeto; a comprovação de desempenho é pela NBR 15575 (procedimento simplificado ou simulação).
- Por que funciona: a versão 2005 trazia aberturas/vedações/sombreamento por zona (ex.: ZB 8); a 2024 não. Segundo Lamberts, as diretrizes "existiam na primeira consulta pública, mas a indústria pediu para retirar"; diretrizes para HIS ficaram com o projeto Hab.LabEEE. Coerente com F2, que só define as zonas.
- Quem disse: Roberto Lamberts. Onde: F1 slide 33.
- Limite: vale para a 2024. Diretrizes da 2005 só como referência histórica, citadas como tal.

**M3 — Microclima da Barra/Recreio vira premissa, não troca de zona** (tipo A)
- O que fazer: a zona é a do município (Rio = 4A). Na Barra/Recreio (beira-mar e lagoas, longe da estação de referência), registrar o microclima (brisa marinha, umidade, ilha de calor) como premissa do partido ou da simulação e manter margem de desempenho.
- Por que funciona: Lamberts mostra que estações diferentes na mesma cidade e a ilha de calor urbana podem dar classificações diferentes; o zoneamento é por município.
- Quem disse: Roberto Lamberts. Onde: F1 slides 37, 41, 44.
- Limite: o projeto não pode adotar outra zona para fugir de requisito. Microclima entra como premissa declarada, nunca como reclassificação.

Tipo B (fabricante): nenhum — busca de 01/10/2026 não achou guia de fabricante com autor credenciado.

## Histórico
- v1.0 — 01/09/2026.
- v1.1 — 28/09/2026 — ZB 4A marcada como indício não confirmado.
- v1.2 — 01/10/2026 — Rotina de Macetes v1.2 (Wallenberg), validada e aplicada por Lúcio. **Cardozo é co-dono** (cross Complementares/Arquitetura). Macetes M1-M3; ressalva da zona rebaixada para "confirmada no texto da Consulta Nacional jun/2024 e no mapa LabEEE; texto final não lido"; transição do prefácio do projeto (180 dias, marco = protocolo) registrada como texto de projeto. Espelho de `.claude/skills/nbr15220-3-bioclimatica-rj/SKILL.md` v1.2.
