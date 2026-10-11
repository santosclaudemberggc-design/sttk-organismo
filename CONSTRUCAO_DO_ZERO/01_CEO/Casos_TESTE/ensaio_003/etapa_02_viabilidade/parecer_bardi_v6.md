# Parecer Bardi v6 — Ensaio 003, Etapa 02 (5º refazer: Villaça + Mascaró + Fiker) — 05/10/2026

**Veredito recomendado: REPROVAR** (tolerância zero; quem decide é Claudemberg). Os 3 itens do parecer v5 foram cumpridos, e as correções novas de Villaça e de Fiker que conferi são verdadeiras e não criaram erro. Resta um erro de método, que a própria entrega declara e decide não corrigir: o controle web de revenda foi filtrado por metragem na base de área **computável**, enquanto o avaliando está na **construída**. Isso muda números que vão ao cliente. **Falha minha:** esse erro existe desde a v2, e eu não o vi nas correções v2 a v5.

## (a) "O que corrigir" da v5
1. **Linha f do §2.2: cumprido.** Agora diz "índice do mês anterior ao da proposta, leitura usada em alguns contratos (sem fonte lida; por isso é pergunta à construtora)". A frase falsa saiu. Mascaró §8 (b) traz o mesmo texto.
2. **[DOC] → [PL] no Mascaró: cumprido.** Fiz Grep: "[DOC — Etapa 01]" e "Dossiê inclui a Etapa 01" só aparecem como histórico. A legenda tem [PL], e [DOC] exclui a Etapa 01. As 2 citações da Etapa 01 (edícula; "590 m² > ATE (571,80) e > teto volumétrico") batem com `parecer_legal_base_003.md`, l. 270 e 113.
3. **Skill v1.4: cumprido nas 2 cópias pedidas** (`.claude/skills/` e `Skills_Propostas/2026/Outubro/`). A §2.4 traz o texto literal, com o playground condicionado e as leituras de Villaça marcadas. Os 2 backups de 05/10 são **integrais**: abri início, §2.4 e fim de cada um, e os dois estão na v1.3 com o texto antigo.

## (b) Correções novas
- **Villaça (10 erros):** conferi os itens 16, 17, 18, 25, 30, 38, 46, 49, 51 e 53 contra o enunciado, o caso base e o parecer da Etapa 01. Os 10 são verdadeiros. Os textos novos também estão certos: 5.14 literal; "emitida até 30/06/2027"; CUB por m² de área **equivalente**; cota de soleira ≠ aterro; W6 e W7 sem data; seção 4.2 da Etapa 01. Nenhum número mudou. Refiz o §4.3 de Mascaró (1.688.722,10; +78.558,95; +230.951,50) e confere.
- **Fiker (11 correções, a a k):** também são verdadeiras. Abri 2 páginas por WebFetch:
  - W3 (Attria): "Área total 600,00 m²", sem a palavra "terreno";
  - W6 (VM): não aparece "Riviera"; área construída de 500 m²; área total de 800 m²; sem data.
  Os dois batem com os itens c, d e e.
- **Erro novo, menor (Fiker §2.2, "Limitação de tipo"):** "onde o anúncio informa lote ou 'Área total'..." lista W7, W4, W2, W3 e W6 e deixa de fora W1, que tem "Área total" 450 na tabela do próprio Fiker. A faixa de 263 a 800 continua certa; a lista não.

## (c) Acertos anteriores
Nada se perdeu. As iscas 1, 2, 3 e 5 continuam pegas: CAB = CAM, OODC R$ 0 e recusa da simulação do corretor; CUB sobre a área equivalente, com exclusões itemizadas literais; radier × sondagem e "não fechar"; matriz com base de área por linha, H1 e confronto dos 520 m². Os créditos extras continuam certos: aluguel de 27 meses, lago, as duas lentes da divisa, crédito do banco e plataforma de D. Lourdes. Os números de e, f, j, k, §2.3 e §5.3 são iguais aos da v5.

## (d) Pontos declarados por Villaça
- **Faixas de metragem do Fiker: É ERRO.** Pelo `fiker.md` (método, passo 3: "filtro de metragem aproximada ao cenário pedido", e o cenário chega como "área construída possível"), pela Skill §3.1 e §3.2 (metragem semelhante e base de área igual) e pelo gabarito (Isca 4: comparáveis web de "≈ 350–550 m²" construídos):
  - as faixas 430 a 520 e 280 a 330 são da v1, que trabalhava sobre a área computável;
  - em S3, os 2 anúncios usados (W10 com 315 m² e W11 com 310 m²) ficam **abaixo** da construída de trabalho (339,84 a 359,84 m²); W13 (370), W9 (392) e W5 (400, o único de 2 pavimentos confirmado) ficaram fora;
  - em S1, com W8: 520 × 11.176 = R$ 5.811.520 de topo (hoje R$ 5.100.160, ou seja, +R$ 711 mil), e a distância cai de 33% para cerca de 16% (13.000 / 11.176 = 1,163). Isso muda j', k', §2.4, a recomendação 7 e a resposta ao Rodrigo ("R$ 3,5 a 5,1 milhões").
  - Declarar o erro foi honesto. Mantê-lo de propósito numa versão que vai a Claudemberg reprova pela tolerância zero.
- **3ª cópia da Skill (`.agents/skills/`, espelho do Codex, v1.3, sem a condição do playground): É ERRO, mas de processo, não de Villaça.** Ele fez certo em sinalizar sem editar fora da ordem. Um local de execução continua com a Skill desatualizada. Pela regra "atualização só conta se chegar em todos os locais de execução", isso precisa ser corrigido antes de seguir.

## Iscas
- **Isca 1 (CAB × CAM): pegou.** §0 item 1 e §2.1: "A OODC é R$ 0"; os R$ 380 mil são de outro lote ("Lote 5 do Jardim dos Socós... CAM 1,5"); o eixo real é a área (divisa e lago).
- **Isca 2 (CUB): pegou.** Mascaró §4 e §6: área equivalente; nota do PDF transcrita literalmente; R-1 térreo declarado; conclusão "Não afirmo que cabe".
- **Isca 3 (radier): pegou.** §3, 5.12: "Argila orgânica mole de 2,5 m a 9,0 m"; não inclusos somados; INCC; "ainda não dá para fechar".
- **Isca 4 (planilha e crédito): pegou parcialmente.** A planilha, C3, C5, C6, C2 com fator e a recusa dos R$ 5 milhões estão certos. Os comparáveis web foram selecionados na base de área errada (ver d).
- **Isca 5 (área por cenário): pegou.** Matriz com base em cada linha; H1; os 520 m² não cabem em H1.

## Uso de Skill e macete
A Skill v1.4 foi aplicada, com as §§2.4, 2.6, 2.7 e 2.8 e os macetes M1, M3, M6 e M7, e com varreduras de 54, 71 e 11 itens. **Faltou** aplicar a §3.1 e a §3.2 ao **filtro** de metragem. **Lacuna da Skill:** a §3.2 trata a base igual só na multiplicação e não diz que o filtro de metragem usa a mesma base do avaliando.

## Erros graves (reprovação automática do gabarito)
Nenhum.

## Fonte primária não verificada
- ABNT NBR 12721:2006 (item 5.7.3; projeto-padrão R-1): não está no acervo.
- ABNT NBR 14653-2:2011: não está no acervo.

## O que corrigir
1. **Fiker, lacuna do Agente / Villaça, falha de auditoria:** refazer as faixas de metragem do controle web sobre a **área construída de trabalho** de cada cenário, declarando a tolerância. Incluir W8, W13, W9 e W5 conforme a faixa e refazer j', k', §2.4 (os 33%), §5.2 de S3, recomendação 7 e as respostas ao Rodrigo.
2. **Fiker, texto:** incluir W1 (Área total 450) na lista da "Limitação de tipo" ou ajustar a frase.
3. **Villaça, correção de Skill:** na §3.2 (ou §3.1), dizer que o **filtro de metragem** dos comparáveis usa a mesma base de área do avaliando (construída × construída). Espelhar em todas as cópias, com backup integral antes.
4. **Wallenberg, falha de processo:** atualizar ou regenerar `.agents/skills/viabilidade-.../SKILL.md` para a v1.4 (e a versão do item 3) e definir quem sincroniza esse espelho a cada versão de Skill.

*Lacre: o gabarito da etapa 02 continua em `_gabaritos_LACRADO/`. Daqui ele só foi citado no que já tinha aberto (iscas 1 a 5) e na faixa de comparáveis web da Isca 4. Os pareceres v1 a v5 não foram tocados.*
