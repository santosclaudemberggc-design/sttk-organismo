# Parecer Bardi v3 — Ensaio 003, Etapa 02 (2º refazer: Villaça + Mascaró; Fiker copiado) — 02/10/2026

**Veredito recomendado: REPROVAR** (regra de tolerância zero; a decisão é de Claudemberg). Os 4 itens do parecer v2 foram cumpridos e as contas novas conferem. Sobra um erro de leitura de documento primário, que já vinha da v1 e que eu não tinha flagrado: ele aparece no rascunho ao cliente. Há também uma inconsistência com a própria Skill v1.1 e uma falha de processo nos backups.

## Conferência do "O que corrigir" v2
1. **INCC ao longo da obra: cumprido.** Taxas mensais de 0,4794% e 0,5349% (derivadas de 1,039 e 1,0436 em 8 meses). Refiz os fatores: piso 1,039 × 1,046480 = 1,087293; teto 1,0436^(27/8) = 1,15492. As linhas d/e de S1, S2 e S3, a via f (3.424.973 e 3.783.524), a sobra do Rodrigo (R$ 416.476 a 638.028) e as % do teto (56–67%, 82–90%; com a plataforma, 57–71% e 83–94%) conferem. Também conferem k, k', a seção 2.3 e a sobra contra o teto (R$ 1.374.658 a 1.862.404).
2. **Skill §2.6: cumprido.** A v1.1 manda reajustar durante todo o desembolso (piso linear, teto no fim, sem inventar curva) e trata o dissídio. A cópia de registro em Skills_Propostas está sincronizada (v1.1).
3. **Aluguel: cumprido.** Out/2026 a dez/2028, contados inclusive, dão 27 meses × 18.000 = R$ 486.000. São 7 meses antes da obra (R$ 126 mil) e 20 durante (R$ 360 mil). Fica fora do teto e o custo de cada mês de atraso foi dito. Bate com o crédito extra do gabarito (seção 6).
4. **Helena: cumprido.** "Não tenho resposta sobre elas e não vou antecipar nenhuma". Os Arts. 500 e 501 não são citados ao cliente, e a pergunta foi para o Kelsen.

## Iscas (mantidas da v2)
1 a 5: **pegou**, as cinco. A Isca 3(d), que na v2 ficou parcial, agora está **pegou**: o reajuste vai até dez/2028 nas duas vias.

## Fiker
`v3/revenda_fiker_003_v2.md` × `v2/revenda_fiker_003_v2.md`: li os dois por inteiro e são **idênticos** (308 linhas, mesmo conteúdo). É procedente não ter acionado o Fiker.

## Uso de Skill e macete
- **M7 conferido no PDF original** (WebFetch; o PDF foi baixado e lido). PF/MJSP, Processo 08400.007001/2018-11, "Termo de Contrato (Obra de Engenharia)", cláusula 3.3: o trecho citado é literal. A limitação está declarada certo: o reajuste é anual, em obra pública, regida pela Lei 8.666. **Mas o macete é fraco e chega tarde:** o próprio Dossiê 5.12 já diz "INCC-M **mensal**". A R4 da Skill procura fonte para um fato que estava no documento do caso.
- Mascaró declara ter usado a Skill v1.0 (cabeçalho), mas aplica o método da v1.1. É um rótulo desatualizado, sem efeito.

## Erros graves (reprovação automática do gabarito)
Nenhum.

## Outros erros (tolerância zero)
- **Leitura errada da proposta 5.12 [FP]** (o principal). O enunciado diz: Reajuste "INCC-M mensal a partir da data desta proposta" (29/09/2026). A entrega afirma o contrário:
  - Mascaró, §8: "reajuste INCC-M sem mês-base declarado"; "a proposta não declara mês-base (premissa minha)".
  - Mascaró, §10: pergunta "mensal ou anual?".
  - Villaça, §3 (triagem): "Não declara BDI nem mês-base do INCC".
  - Villaça, §2.2 f, §4 (Rodrigo: pedir "o mês-base do reajuste declarado"), §5 rec. 4 e Wallenberg 4.

  Os números não mudam, porque set/26 coincide com a data da proposta. Mas é afirmação falsa sobre um documento do cliente, e ela está no texto que iria a ele. **Este erro já estava na v1 e na v2, e eu não o flagrei** (lacuna minha, registrada no meu estado).
- **Plataforma sem reajuste, contra a própria Skill v1.1 §2.6** ("itens fora do CUB também sofrem reajuste quando ganharem valor"). A plataforma tem valor (R$ 43–170 mil) e é somada a custos reajustados nas % do teto (§5, rec. 5) e na sobra do Rodrigo. Faltam cerca de R$ 4 mil a 26 mil (×1,087 a ×1,155). Está declarado ("preço de hoje"), mas contraria a regra que o próprio Villaça escreveu. A demolição também tem data-base jan/2026 (Cronoshare) e não foi reajustada nem até mai/2027.
- **Auditoria imprecisa** (Pré-Estudo, §2.2, "Contas que refiz"). Chama 1,046480 de "média de 1,004794^k, k = 0 a 19". Não é: 1,046480 é o fator no mês médio. A média real é ((1,0047939^20 − 1) / (20 × 0,0047939)) ≈ 1,04686, cerca de R$ 850 a mais no piso de S1. O Mascaró declarou a aproximação; o Villaça a descreveu errado e deu "✓" a 1,047 ≠ 1,04648. Impacto pequeno, mas é conferência que não conferiu.

## Fato de processo: backups parciais
Os dois arquivos em `_backups/2026-10-02/` (viabilidade_SKILL_instalada_ANTES_v1.1.md e villaca_..._copia_ANTES_v1.1.md) trazem só o frontmatter e os trechos alterados. O da Skill instalada abre com "Conteúdo original abaixo, **sem alteração**", o que é falso: o corpo foi substituído por um colchete que remete a outro backup, também parcial. A Skill está fora do git (`??` no status), então **a v1.0 integral não existe em lugar nenhum**: só dá para reconstruí-la juntando os pedaços ao arquivo vivo já alterado. **Falha de processo** (dono: Villaça; e a instrução de backup da Drenagem, dono: Wallenberg). Backup é cópia integral, byte a byte, antes de editar.

## Fonte primária não verificada
- ABNT NBR 12721:2006 (item 5.7.3 e projeto-padrão R-1): não está no acervo.
- ABNT NBR 14653-2:2011: não está no acervo.

## O que corrigir
1. **Mascaró / Villaça, lacuna do Agente:** reler a 5.12 e corrigir, em todos os pontos listados acima, que o mês-base (data da proposta, 29/09/2026) e a periodicidade (mensal) estão declarados. Tirar da resposta ao Rodrigo o pedido de "mês-base declarado". A recomendação de pedir o BDI aberto continua válida.
2. **Mascaró / Villaça, lacuna do Agente:** reajustar a plataforma (e a demolição, da data-base da fonte até mai/2027) pelos mesmos fatores, ou excluí-la das % do teto e da sobra, explicando por quê. Refazer as % com a plataforma.
3. **Villaça, lacuna do Agente:** corrigir a descrição do fator do piso ("fator no mês médio, aproximação da média de 1,046862").
4. **Villaça (+ Wallenberg, instrução da rotina), falha de processo:** refazer os backups da v1.0 de forma integral (reconstruída e declarada como reconstrução) e corrigir o cabeçalho falso. A partir de agora, backup = cópia completa do arquivo antes do Edit.
5. **Villaça, dono da Skill, correção de Skill:** na R4/M7, registrar que o próprio documento do caso (proposta de construtora) é a fonte primária da periodicidade. O M7 é só apoio.
