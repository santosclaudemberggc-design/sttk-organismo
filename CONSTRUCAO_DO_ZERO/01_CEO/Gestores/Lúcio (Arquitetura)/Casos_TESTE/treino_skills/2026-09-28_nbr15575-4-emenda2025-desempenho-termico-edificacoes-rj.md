# TREINO DE SKILL — CASO FICTÍCIO (não é cliente real)

**Skill:** `nbr15575-4-emenda2025-desempenho-termico-edificacoes-rj`
**Data:** 28/09/2026 — decisão de Claudemberg: treino obrigatório em caso fictício antes do caso real.
**Montado por:** Lúcio | **Executado por:** Oscar

## Caso (FICTÍCIO)
Cliente inventado "Sr. Arpoador Neto", lote inventado de 15 x 40 m na Barra da Tijuca, casa térrea nova. Restrição inventada: cliente exige Light Steel Frame (obra rápida). O fornecedor fictício declara parede externa LSF com CT = 40 kJ/(m²·K) e "U = 0,6 W/(m²·K), atende ZB 8". Fachada Oeste com 70% de vidro, sem proteção. Cobertura em laje com telha metálica escura (absortância 0,8). O arquiteto parceiro quer escrever no memorial "atende NBR 15575-4 pelo método simplificado, ZB 8, U conforme tabela".
Pergunta: o memorial pode sair assim? O que ajustar?

## Gabarito do Lúcio (pela Skill)
1. Zona: RJ passou de ZB 8 para ZB 4A (NBR 15220-3:2024) — citar ZB 8 está errado (§1). Confirmar ZB 4A antes de simular (§6).
2. CT 40 < 130 kJ/(m²·K) referência ZB 4A (§3) — LSF exige massa/EPS/bloco extra, verificar com Baumgart (§5). Valor é referência a confirmar (R3).
3. U não pode ser citado como "conforme tabela": limite de U para ZB 4A não está na Skill, está na Emenda ABNT 2025 (R1 crítica).
4. Método simplificado não serve para obra nova; simulação anual obrigatória com cargas internas (§4) — se o LICIN exige como condicionante está em aberto (R4). R2: versão consolidada da Emenda não publicada.
5. Oeste 70% vidro = caso crítico, proteção solar externa (§5, Skill de proteção solar).
6. Cobertura: absortância 0,8 acima da referência ≤ 0,6 (§3) — trocar telha/cor clara.
7. Memorial não sai assim; nada vai sem Gate do Maurício.

## Resposta do Oscar (resumo fiel)
Memorial não sai. ZB 8 errado, mas sinalizou que a Skill irmã NBR 15220-3 chama ZB 4A de "indício não confirmado" (§1); simplificado não serve para obra nova, R4 em aberto (§4); U não pode ser citado sem a Emenda paga (R1, R2); CT 40 < 130 referência, LSF exige massa/EPS, Baumgart via Lúcio (§3, §5, R3); Oeste crítico → proteção solar; absortância 0,8 > 0,6 (§3). Propôs texto "verificação pendente: simulação anual ZB 4A" e citou REGRA-ARQ-01 contra pressão de prazo.

## Veredito do Lúcio: OK
Bateu com os 7 pontos do gabarito e ainda achou uma inconsistência da própria Skill.

## Correção sugerida à Skill (não editada)
- §1 afirma ZB 8 → ZB 4A como fato; a Skill `nbr15220-3-bioclimatica-rj` trata como indício não confirmado. Alinhar: rebaixar para "a confirmar em fonte primária" ou confirmar e atualizar a irmã.
- §3: linha de absortância de cobertura está dentro da tabela de Paredes; mover para Coberturas.
- Todas as fontes são secundárias; registrar isso no cabeçalho (`fonte_primaria_lida: não`), como a Skill do COE faz.
