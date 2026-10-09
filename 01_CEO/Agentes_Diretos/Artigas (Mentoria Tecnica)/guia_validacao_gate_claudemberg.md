# Guia de validação do Gate — Claudemberg

> Decisão de Claudemberg em 09/10/2026: **o Gate da Coordenação passa a ser dele** (antes, "Gate do Maurício"). Artigas continua sendo o canal: localiza o formulário, monta o pedido e registra o veredito. Este guia diz **onde olhar** para validar cada pedido aberto. Preparado por Wallenberg em 09/10/2026.
>
> Regra que não muda: silêncio não é aprovação. Sem o seu veredito escrito, o Gate continua aberto.

---

## Gate 1 — R6 da Skill de vaga (Kelsen/Hely, Ensaio 003, etapa 3)

**Pergunta:** a leitura R6 pode ser usada em caso real? A R6 diz que o COES Art. 29 III fixa 25 m² por vaga como **limite para dispensar a pintura (demarcação) das vagas**, e não como tamanho de garagem; e que somar vaga + manobra (12,50 + 12,50 = 25 m²) é uma **leitura**, não o texto da lei.

**Onde validar (3 passos, cerca de 10 minutos):**

1. Abra `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`, **página 15 do PDF**. Leia o Art. 29, incisos I, II e III.
   - Conferido por Wallenberg em 09/10 (extração do texto do PDF): o inciso III diz que as vagas "deverão estar obrigatoriamente demarcadas, exceto quando estiver atendida a proporção mínima de vinte e cinco metros quadrados de área de estacionamento por vaga". Ou seja, o texto fala de demarcação. A página certa é a 15 do arquivo (a "p. 19" citada no parecer do Bardi v6 não bate com este PDF).
2. Abra `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf`, Disposições Gerais, **inciso XXII** (p. 4 do PDF, conferido por Wallenberg em 09/10): a área livre do lote pode ser usada para estacionamento, "excetuada aquela do afastamento frontal mínimo obrigatório", **desde que seja plantada no mínimo 1 árvore por vaga**. Isso não muda a R6, mas é a regra que mais pesa no projeto real. A condição da árvore por vaga já está na Skill de vaga (tabela de fontes, l. 43 — conferido com `Grep` em 09/10). (A nota de revogação na p. 5 é dos incisos XXXII e XXXIII, não do XXII.)
3. Leia o pedido completo: `01_CEO/Agentes_Diretos/Artigas (Mentoria Tecnica)/pedido_gate_R6_2026-10-08.md` (seção 2 tem as 3 opções e o efeito de cada uma).

**Como responder:** escreva "Gate R6: aprovado / aprovado com ressalva (qual) / reprovado (motivo)" em qualquer conversa ou na Reunião. Artigas registra.

**Opinião de Wallenberg (você decide):** aprovar com ressalva. O texto do III sustenta "limiar de demarcação". A soma 12,50 + 12,50 = 25 é só coincidência aritmética e não deve ser citada como regra ao cliente. A garagem continua dimensionada pelos incisos I e II.

---

## Gate 2 — Interiores do Daniel-OB (Cardozo → Tenreiro + Mindlin), aberto desde 01/09

**Problema encontrado em 09/10:** o pedido aponta para `Apresentacao_Interiores_Daniel-OB.html`, que **não existe mais** na pasta. O entregável que ficou é outro arquivo:

`D:\001_STTICKLER\001_Projetos 2023 - Sttikler Empreendimentos\001_Clientes e Empreendimentos\001_Proj_I - PF\Rio de Janeiro\Recreio\Daniel - OB\01_Projeto\Interiores\Apresentacao\Daniel-OB_Interiores_Slides.html` (abre junto com a pasta `assets/` ao lado; última modificação 01/09).

**Onde validar:**

1. Abra o arquivo de slides acima no navegador.
2. Insumos na mesma pasta: `curadoria_tenreiro.md` (as 35 escolhas, com o porquê) e `_pesquisa_referencias_cardozo.md`.
3. Formulário oficial do fluxograma: Validação da Coordenação — Projeto de Interiores: https://docs.google.com/forms/d/1dVKTNuB44lZdbphH0TdRSUBEhS9x3MdtubfpAypRCRQ/edit (POP: https://docs.google.com/document/d/16cNSLB1Q2pqxtKcK1kTMTeHJEYlGiaVzRs3P-GAX4qk/edit).
4. Ressalvas já declaradas pelo Cardozo: renders por IA não gerados (o Burle não tem as ferramentas); 28 imagens de referência ainda são espaços vazios; compatibilização com planta, elétrica e impermeabilização não foi feita (medidas são intenção, não cota).

**Opinião de Wallenberg:** como peça de "estudo de ambientação" para conversa com o cliente, pode ser aprovada com ressalva. Como projeto de Interiores, não: falta compatibilização. Decida também se esse Gate ainda faz sentido, já que o cliente está parado desde meados de setembro.

---

## Onde ficam os pedidos daqui em diante

- Todo pedido novo: pasta `01_CEO/Agentes_Diretos/Artigas (Mentoria Tecnica)/`, arquivo `pedido_gate_{tema}_{data}.md`.
- Lista de Gates abertos: `_estado_artigas.md`, seção 2.
- 39 formulários oficiais do fluxograma: memória `referencia/sttickler_formularios_fluxograma_links.md`.
