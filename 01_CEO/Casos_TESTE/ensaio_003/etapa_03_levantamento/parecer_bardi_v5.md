# Parecer Bardi — Etapa 03 (Levantamento), REFAZER v5 — Ensaio Sombra 003 — 07/10/2026
Li a `entrega\v5\` inteira (nota, Peças 1–3, anexo) contra o gabarito lacrado, o enunciado e a v4. Fiz o diff da Peça 2, da Matriz e das tabelas F e G do anexo com a v4. Contagem de Wallenberg (`wc -w`): Peça 2 = 2.058 palavras (≤ 2.500, atende). Conferi no primário o COES consolidado (p. 15, Art. 29) e o Dec. 3.046 (p. 4, XXI–XXIII).

**Veredito recomendado: REPROVAR** (tolerância zero, 02/10). Os 3 erros da v4 foram corrigidos e nenhum número mudou, como mandava a ordem. Ainda assim, a etapa não pode seguir para o Briefing: há um erro de forma novo e dois erros de mérito que a nova Skill de vaga e o primário tornam visíveis. Um deles nasceu do meu próprio gabarito. A decisão é de Claudemberg.

## Iscas (gabarito lacrado): 4/4 pegas, sem mudança desde a v3
1. Varanda frontal: PEGOU (P2 §3.2; C-10). 2. Muro do Lote 16: PEGOU (P2 §3.1; C-1, C-2). 3. Edícula: PEGOU (P2 §5.1; C-14). 4. Garagem: PEGOU pelo critério do gabarito, mas o critério estava errado (ver o erro 2).

## Os 3 pontos da v4: corrigidos
- A nota declara E-6/E-7 (v3→v4) e faz o diff da v5 arquivo por arquivo. O diff que fiz da P2, da Matriz, da F e da G confere com o declarado.
- G, linha do crédito: "—", com o fato remetido a C-16/E-16. Bate com o corpo.
- A Peça 1 §9 tem declaração de leitura nova e a nota não se contradiz. As 5 remissões novas da Matriz (l. 6, 7, 8, 12, 16) conferem com P2 §3.4, §5.2, §6, §7 e com E-14/I-3.

## Erros que reprovam
1. **A tabela G viola a regra que a própria v5 escreveu** (anexo G, l. 268, e Skill de levantamento v1.5: "a célula só cita a seção que afirma a frase inteira; afirmação parcial = —"). Exemplos: a linha "520 em H0 só com as 3 condições…" cita Matriz "linhas 5, 9, 21, 24", mas a l. 9 nem fala do 520 e as l. 5 e 21 trazem só uma parte. A linha "Piso térreo: soleira = implantação…" cita a Matriz l. 10, que não diz "soleira = implantação". Pelo mesmo motivo de parcialidade, a v5 trocou a varanda da Matriz l. 20 por "—". A regra foi aplicada a umas células e não a outras, e a nota diz que as 27 células foram conferidas duas vezes. *Dentro do organismo* (Skill v1.5). Dono: Oscar (execução) e Lúcio (auditoria).
2. **"a = 12,50–15,00 m²/vaga" conta só a vaga, sem a manobra.** O COES Art. 29 I–III (p. 15, que li) exige vaga de 2,50×5,00, mais área de manobra de 2,50×5,00, e usa 25 m²/vaga como proporção de referência. A faixa entra na condição (3) do "cabe", na Matriz l. 9, 22 e 24, em C-5/C-7/C-8/C-9/C-15 e na P2 §1, §3.3, §5.3 e §8. Com ela, o cliente escolheria entre 4 e 6 vagas no Briefing com a garagem subestimada em até metade. **A origem é minha:** o gabarito da Isca 4 usou "~15 m²/vaga", e C-4 cita "parecer do Bardi, Isca 4". *Fora do organismo* até 06/10 (nenhuma Skill tratava do tema). Desde 07/10 está *dentro*: a Skill `vaga-estacionamento-…` v1.0, §1 e §3.
3. **A alternativa A (vagas descobertas no afastamento frontal) contraria o Dec. 3.046, Disp. Gerais XXII** (p. 4). O inciso permite estacionamento na área livre "excetuada aquela do afastamento frontal mínimo obrigatório". A entrega apoia a alternativa no LC 270 Art. 363 §2º XII (P2 §2; P2 §3.3 A; C-8), sem registrar a tensão. É o mesmo tipo de conflito que ela tratou bem no VII × XI. Some-se a geometria: vaga de 5,00 m mais manobra de 5,00 m não cabem num frontal de 6,00 m sem usar a rua, e a Skill nova, R5, diz para não presumir isso. A premissa veio do parecer Legal aprovado da Etapa 01 (l. 181, "(b)"), e é herança que ninguém pegou, nem eu em 4 correções. *Fora do organismo* até 06/10 (a Skill `decreto3046` não traz o XXII). Desde 07/10 está *dentro* (Skill nova, R3).

**Resposta à pergunta de Wallenberg sobre a Matriz l. 22:** numa v5 "só forma", manter a pendência declarada era o certo, porque a ordem proibia mexer em número. Mas a Skill nova e o primário mudam o juízo. A faixa deixou de ser uma pendência honesta e passou a ser um parâmetro sabidamente incompleto. Etapa com parâmetro sabidamente errado não segue, nem com a pendência declarada. A reprovação dos erros 2 e 3 não é falha de conduta do Oscar na v5: ele cumpriu a ordem.

## Uso de Skill e macete
Skill de levantamento v1.5 §5-bis aplicada em parte (ver o erro 1). As Skills `vaga-estacionamento-…` (v1.0) e `decreto3046` (sem o XXII) são obrigatórias na v6. Processo: o espelho `.agents/skills/levantamento-…` ainda está na v1.1, e a Skill de vaga não tem espelho.

## Erros graves (reprovação automática do gabarito)
Nenhum.

## Fonte primária não verificada
NBR 13133 e NBR 8036 (não estão no acervo). Dec. 45.917 Art. 10 (vaga paralela): não reli.

## Lacunas do organismo
- **Manobra na conta de m²/vaga (COES Art. 29 II–III).** Fonte: COES consolidado SMU, p. 15. Dono: Kelsen. Lacuna já fechada pela Skill de 07/10; falta aplicar na Etapa 03 e nas contas de Viabilidade (Villaça).
- **Dec. 3.046 XXII: estacionamento vedado no afastamento frontal mínimo da ZE-5.** Fonte: Dec. 3.046/1981, p. 4. Dono: Kelsen. Coberta pela Skill nova (R3), mas ausente da Skill `decreto3046` e do parecer da Etapa 01, l. 181, que precisam de errata.

## O que corrigir (v6)
1. Oscar: refazer as contas da garagem com a Skill de vaga (vaga e manobra separadas, com artigo) e rever a alternativa A contra o XXII e a geometria do frontal. Depois, propagar para a Matriz, a P2 e o Anexo G/E. Tipo: lacuna do organismo, já fechada.
2. Oscar/Lúcio: aplicar a regra da G a todas as 27 células. Tipo: lacuna do Agente e de auditoria.
3. Kelsen: errata ao parecer da Etapa 01 (l. 181) e inclusão do XXII na Skill `decreto3046`, com remissão cruzada à Skill de vaga (R3). Tipo: correção de Skill.
4. Drenagem: atualizar o espelho `.agents/skills` (levantamento v1.5; vaga v1.0). Tipo: falha de processo.
5. Bardi: registrar o erro do gabarito da Isca 4 (sem reescrevê-lo) e cobrar, na Etapa 04, a herança corrigida. Tipo: erro do examinador.
