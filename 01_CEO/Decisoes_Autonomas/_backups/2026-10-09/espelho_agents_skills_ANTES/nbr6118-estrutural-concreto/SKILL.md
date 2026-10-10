---
name: nbr6118-estrutural-concreto
description: NBR 6118:2026 (Emenda 1) — projeto de estruturas de concreto armado e protendido, classes de consequência CC1/CC2/CC3, exigência de ATP (Avaliação Técnica de Projeto), armadura de balanços/marquises, emendas de armadura e detalhamento. Use sempre que Baumgart (ou qualquer Agente) for definir a classe de consequência de uma estrutura, decidir se ATP é exigível, dimensionar armadura de laje em balanço ou marquise, especificar emenda de barra acima de Ø32mm, ou checar se um projeto cai na janela de transição da norma 2023→2026 — mesmo que o pedido não mencione "NBR 6118" explicitamente, dispare esta Skill para qualquer memorial, cálculo ou revisão de estrutura de concreto armado residencial.
---

# NBR 6118:2026 (Emenda 1) — estruturas de concreto armado

Skill de Inteligência Técnica da área Estrutural, equipe de Cardozo (Gestor Complementares). Quem consome na prática: **Baumgart** (Agente Estrutural). Quem retém e decide quando aplicar: **Cardozo**.

## O que esta Skill é — e o que ela deliberadamente não é

**É um mapa e um checklist de processo — não é o texto normativo.** O texto oficial completo da NBR 6118:2026 é pago (ABNT) e **não foi lido por nenhuma fonte que originou esta Skill** — apenas blogs técnicos especializados (APL Engenharia, Master em Modelagem, Sienge) que resumem a Emenda 1. Trate todo valor numérico abaixo como **ponto de partida a confirmar**, não como resposta pronta para memorial de cálculo real — mesma disciplina já estabelecida pela Skill irmã de Legal (`legal-base-legislativa-bairro`): o número final sai da norma, não do resumo.

## ⚠️ Divergência aberta — confirmar antes de aplicar em caso real

Duas pesquisas independentes do organismo (19/07/2026 e 28/08/2026) chegaram a conclusões **diferentes** sobre a exigência de ATP (Avaliação Técnica de Projeto — revisão por profissional independente) na **Classe de Consequência 2 (CC2)**:

- Uma diz que ATP é regra geral para CC2/CC3, sem dispensa possível em CC2.
- A outra diz que ATP só é obrigatória para CC3 — CC2 segue verificação padrão, sem ATP em regime normal.

**Nenhuma das duas confirmou contra o texto oficial ABNT.** Antes de decidir se um projeto CC2 precisa de ATP, **pare e confirme na norma oficial ou escale a Cardozo** — não escolha uma das duas versões por parecer mais provável. Isso é exatamente o tipo de erro que já aconteceu antes no organismo (Legal, 20/07/2026: parâmetro errado sobreviveu 3 rodadas de análise por paráfrase de paráfrase).

## Classes de Consequência (CC) — primeira pergunta de todo projeto

| Classe | Exemplos | ATP obrigatória? |
|---|---|---|
| CC1 | Residências unifamiliares até 2 pavimentos | Não (ver ressalva acima para limites — confirmar) |
| CC2 | Edifícios até 5 pavimentos, pequenas reformas | **Divergente — ver aviso acima** |
| CC3 | Edifícios >5 pavimentos, subsolos, marquises, protendidas, reformas com eliminação de pilares | Sim, com revisor independente |

Na dúvida entre classes, prevalece a mais conservadora (CC3) até confirmação.

## Janela de transição — vigência

Projetos protocolados **antes de março/2026**, ou nos **180 dias seguintes**, podem continuar sob NBR 6118:2023. Projetos novos após esse prazo: obrigatoriamente NBR 6118:2026 (Emenda 1). Confirme a data de protocolo antes de escolher a versão da norma a citar.

## Pontos técnicos da Emenda 1 (tratar como direção, não como valor final)

- **Emendas de armadura:** traspasse proibido acima de Ø32mm — usar luvas mecânicas com resistência mínima 15% superior à resistência de escoamento da barra.
- **Redistribuição de esforços:** limite geral δ ≥ 0,75 (redução máxima de 25% dos momentos elásticos) — verificar se o detalhamento suporta a redistribuição adotada.
- **Lajes em balanço e marquises:** nova armadura inferior de segurança, dimensionada para suportar ações permanentes — mecanismo residual contra colapso total (resposta normativa a colapsos reais de marquises no Brasil). Não é opcional.
- **Punção em lajes:** armadura inferior deve atravessar a laje e ancorar além do contorno crítico; estribos suplementares com ganchos de 135° a 180°.
- **Durabilidade/CAA:** o contratante (cliente) deve fornecer explicitamente a Classe de Agressividade Ambiental antes do início do projeto — não é o projetista que arbitra.
- **Frequência natural mínima de pisos:** 3 Hz (conforto de vibração) — verificar em projetos com vãos maiores.

## Como usar esta Skill

1. Ao receber Briefing de Lúcio (via Cardozo), a primeira pergunta é: qual a Classe de Consequência desta estrutura?
2. Se CC2 ou CC3: **pare no ponto da divergência de ATP acima** antes de prosseguir — confirme com Cardozo ou fonte primária, não presuma.
3. Confirme a data de protocolo contra a janela de transição 2023→2026.
4. Para valores de cobrimento, dimensionamento de condutores de armadura, tabelas completas: **não estão aqui** — consulte a norma na íntegra (ver Fontes) ou os arquivos de referência que Cardozo mantiver.
5. Se não der para confirmar um valor com confiança, diga isso explicitamente na entrega — não arredonde para "parece razoável" (mesma regra da Skill de Legal).

## O que esta Skill NÃO cobre

- Cálculo de fundações (NBR 6122 — assunto separado)
- Estruturas metálicas (NBR 8681) e de madeira (NBR 7190)
- Detalhamento completo de todos os elementos — a norma na íntegra tem o resto

## Fontes (todas secundárias — nenhuma é o texto oficial ABNT)

- blog.apl.eng.br — "NBR 6118:2026: o que mudou com a revisão"
- masteremmodelagem.com.br — "NBR 6118:2026 — Principais mudanças, Emenda 1"
- sienge.com.br/blog/nbr-6118
- Registro completo da pesquisa original: `01_CEO/Skills_Propostas/2026/Agosto/baumgart_nbr6118-2026-emenda1-estrutural-concreto.md` (mantida como referência histórica) e a versão de Julho, removida por duplicidade em 03/09/2026 mas preservada no histórico do índice — é a origem da divergência sobre CC2/ATP.

## Escopo, crescimento e manutenção

Lacuna ou divergência nova encontrada **não vira conhecimento oficial por decisão do Agente**. Reporte a Cardozo; ele avalia e leva a Wallenberg, que formaliza. Se algum dia o texto oficial ABNT for lido e a divergência de CC2/ATP for resolvida, atualize esta Skill e remova o aviso — não deixe o aviso morrer sozinho por desuso.
