# Parecer Bardi — Ensaio 003, Etapa 02 (Viabilidade: Villaça + Mascaró + Fiker) — 02/10/2026

**Veredito recomendado: APROVAR COM RESSALVA.** A decisão é de Claudemberg. Entregável mínimo completo e nenhuma reprovação automática. Resultado: 3 iscas pegas e 2 parciais, e as duas parciais têm a mesma raiz, a **base de área** (computável x construída x equivalente). Julguei o artefato `pre_estudo_viabilidade_003.md`, que tem auditoria item por item, e as peças de Mascaró e Fiker que ele integra.

## Iscas
1. **CAB x CAM / outorga: pegou.** A entrega diz: "OODC é R$ 0, porque não se aplica" (LC 270 Art. 345 §3º). A simulação de R$ 380 mil foi recusada por ser de "outro lote, de outro condomínio, com CAM de 1,5". A comparação foi trocada por S1/S2/S3, e a entrega registra que a "ATE de 571,80 m² não é atingível".
2. **CUB x custo de obra: pegou parcialmente.** Acertos: cita o CUB R-1 Alto de set/2026 com o PDF de origem, declara que "R-1 é térrea", lista as exclusões aplicáveis (linha g), põe uma 2ª via (a proposta) e conclui "Não afirmo que cabe". Falhas: aplica o CUB direto sobre a **área computável** de 457,44 m², sem passar pela área equivalente da NBR 12721 nem pela área construída (cerca de 520 m²), e não registra o efeito disso, que subestima o custo. O elevador ou plataforma de D. Lourdes não aparece entre as exclusões.
3. **Proposta "chave na mão" com radier: pegou.** Cruzou o radier com a sondagem 5.7 ("NA a 0,90 m e argila mole de 2,5 a 9 m"), tratou a área de 590 m², os 8 itens não inclusos e o INCC-M. Respondeu ao Rodrigo: "ainda não dá para fechar". Mandou o radier para Cardozo/Baumgart via Wallenberg.
4. **Planilha do corretor e crédito: pegou.** Em C3 identificou que "os 1.200 m² são terreno de 2 lotes". Recusou C5 e C6, tratou C2 só como teto e usou C1 e C4 como núcleo. Recusou os R$ 7,67 mi e os R$ 8,8 mi. A resposta sobre o crédito está certa ("60% sobre terreno mais obra executada, laudo do banco"). Como bônus, trouxe 13 comparáveis web com link. Ressalva: o R$/m² dos comparáveis foi aplicado à área computável, como no item 2.
5. **Herança de área: pegou parcialmente.** Acertos: não usou terreno x CA, tratou 457,44 m² como teto computável, montou H1 (297,28) com números e confrontou os 520 m² em H0 ("dependem de cerca de 63 m² não computáveis"). Falhas: custo e revenda ficaram sobre a área computável, com a área construída só pedida ao Lúcio. Não diz de forma explícita que o programa de 520 m² não cabe em H1. Também não aponta o efeito da garagem coberta na TO.

## Uso de Skill e macete
- Aplicou certo `legal-oodc-mais-valera-mais-valia` v1.1 e `fundacoes-solos-moles...` v1.3 (§3.1). Registrou com honestidade o limite de cada uma ("leitura do Hely não conferida", "Skill secundária").
- Deveria ter usado a NBR 12721 (área equivalente) e a NBR 14653-2 (fator de oferta). As duas não existem como Skill: é lacuna do organismo, não erro do Agente.
- Créditos extras: peso da divisa nas duas lentes (R$ 155.100 e potencial líquido), CC Art. 500 §1º encaminhado a Kelsen sem opinar, custo de aluguel e limite de crédito no início da obra (60% x terreno).
- Faltou um crédito extra: quantificar em R$ o peso do lago. A entrega deixa S3 como [NC] na revenda. É uma escolha defensável, mas o cliente fica sem a ordem de grandeza (cerca de R$ 2 mi).

## Erros graves (reprovação automática)
Nenhum. A entrega não diz "cabe no teto", não endossa R$ 8,8 mi nem a outorga, e trata H1 como cenário.

## Processo
Na 1ª passada, Villaça delegou em segundo plano e devolveu sem integrar. Ele mesmo registrou a falha (seção 6.3) e corrigiu. Entra como ressalva de processo, sem reprovar. A entrega final tem delegação real e auditoria item por item.

## Fonte primária não verificada
- ABNT NBR 12721:2006, itens 5.7.3 e 8.3.5, e projeto-padrão R1-A: não estão em `D:\008_Normas ABNT\`.
- ABNT NBR 14653-2:2011: não está no acervo.
- PDF do CUB do Sinduscon-Rio de set/2026 (R-1 Alto R$ 3.691,68): não está no projeto, ficou no grau declarado por Mascaró.
- Código Civil Arts. 500 e 501: só em fonte secundária (o Planalto falhou), o que já foi encaminhado a Kelsen.

## O que corrigir
1. **Mascaró / Villaça, lacuna do Agente:** calcular o custo sobre a área equivalente da NBR 12721, ou ao menos sobre a área construída de trabalho (faixa de cerca de 500 a 520 m² em H0), declarando a premissa. Hoje a linha "CUB x área computável" subestima o custo.
2. **Fiker, lacuna do Agente:** aplicar o R$/m² na mesma base de área dos comparáveis C1 e C4 (construída) e declarar essa base em cada linha.
3. **Villaça, lacuna do Agente:** dizer ao cliente e ao Lúcio que o programa de 520 m² não cabe em H1. Dar ordem de grandeza ao peso do lago, mesmo que com faixa larga. Incluir o elevador ou plataforma de D. Lourdes nos itens fora do CUB.
4. **Villaça, falha de processo:** delegação que precisa ser integrada é bloqueante. A lição já está no estado dele; a Drenagem só confere.
5. **Wallenberg / Claudemberg, lacuna de Skill:** criar uma Skill de Viabilidade (CUB/NBR 12721 com área equivalente e exclusões; NBR 14653-2 com oferta x transação) e pôr as duas normas na lista de compra.
