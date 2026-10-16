# Errata e checagem pré-lacre — Etapa 04 (Briefing) — Bardi, 16/10/2026

**Rodada:** agendada, Drenagem Contínua (item `bardi-gabarito-etapa4-erros-09-10`). Sem Claudemberg presente.
**Gabarito checado:** `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi/ensaio_003/etapa_04_gabarito.md` (versão corrigida GB-1 a GB-4, 13/10/2026). Não alterado.
**Local:** fica nesta pasta do examinador, e não em `etapa_04_briefing/`, porque cita conteúdo do gabarito e a pasta do ensaio é lida pelos Gestores e Agentes.
**Origem das checagens:** `ensaio-sombra-checagem-gabarito-antes-lacre` (proposta, `Skills_Propostas/2026/10/`, ainda não instalada em `.claude/skills/`).

## 0. Lacre (SHA256)

- **Não verificado nesta rodada.** Bardi não tem shell (PowerShell/Get-FileHash indisponível). Nada foi calculado aqui.
- Hash registrado no estado (`_estado_ensaio_003.json`, evento `gabarito_corrigido_pos_reprovacao`, 13/10): `1CC0A6B5FB4688DA26A747B3310212D213821B0A35F205D1ACDA71FE5DA13262`.
- Registro de Wallenberg (`parecer_bardi_v4.md`, linha 4): conferido às 20:54:38. Não recalculado por Bardi.
- Não houve divergência constatada. Mas a conferência independente pede `Get-FileHash` de Wallenberg no arquivo. Até lá: **lacre não confirmado por esta checagem**.
- O cabeçalho do gabarito (linhas 6 e 185) ainda diz "PENDENTE". Pedido de registro, sem alteração do arquivo.

## 1. Conferência dos erros registrados (GE-1 a GE-6) e das correções (GB-1 a GB-4)

Fonte primária lida nesta rodada (página do PDF):

| Item | Verificação | Resultado |
|---|---|---|
| GE-1 (páginas COES) | Cópia SMU `Hely/Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` p. 17 = Art. 31, inciso V "atendimento às normas técnicas de acessibilidade" e parágrafo único (1,50 m). Cópia do acervo `D:\008_Normas ABNT\002_Prefeitura_RJ\COE LC 198-2019 ...pdf`: p. 17 = Art. 28; Art. 29 na p. 19; **Art. 31 na p. 21**. | Corrigido no GE-1 (gabarito cita só a cópia SMU). **Resíduo: E-1 abaixo.** |
| GE-2 (Art. 215 §2º) | LC 270 p. 80: "com superfície inferior a dez mil metros quadrados, fica dispensada a reserva da faixa de proteção ... vedada nova supressão de áreas de vegetação nativa, salvo autorização do órgão ambiental". | Confirmado. |
| GE-3 (LC 270 Art. 19 II → LC 281) | LC 281 consolidado p. 7, Art. 19 II: "parcelado em até sessenta cotas ... desconto de trinta por cento ... AP3 e AP5 ... RA XVI (Jacarepaguá) e XXXIV (Cidade de Deus) e no bairro de Rio das Pedras". Busca no gabarito: nenhum "LC 270 Art. 19 II" restante. | Confirmado. |
| GE-4 ("vedada") | Dec. 3.046/1981 Disp. Gerais XXII, p. 4: "excetuada aquela do afastamento frontal mínimo obrigatório". Gabarito (Isca 4) usa "não é solução até o Gate decidir". | Confirmado. Ver nota N-2 sobre o alcance da palavra. |
| GE-5 (herança) | Pré-Estudo v9 (`etapa_02_viabilidade/entrega/v9/pre_estudo_viabilidade_003_v9.md`) linhas 38–40: S1 457,44 | 500–520; S3/H1 297,28 | 340–360. Etapa 01 (`parecer_legal_base_003.md`) linha 36, item 14: "daria 10%". Enunciado linha 21: "SMD: 10% do terreno (Etapa 01, quadro, item 14)". | Confirmado. |
| GE-6 (Art. 363 §2º X) | LC 270 p. 130: "X - áreas em subsolo não aflorado" (§2º, faixa frontal). LC 270 p. 126: "§ 4º Não será admitida nas SMD a implantação de subsolos." | Confirmado. Isca 3, item 1, cita os dois. |
| GB-1 (LC 301 Art. 58) | LC 301 p. 38, Art. 58: Art. 40 da LC 281 com prazo "até 1º de dezembro de 2026" e "desconto de trinta por cento para pagamento à vista". | Confirmado. |
| GB-2 (14,29 × 14,30) | Caso `caso_sombra_003.md` §5.2 (frente 14,30; fundos 14,29) — não reaberto nesta rodada. | Não reconferido (dado de caso, não de fonte). |
| GB-3 (TO 50%) | Caso §5.3, linha 70: "Taxa de ocupação máxima | 50%" (RIU). Etapa 01 item 14: "20% ... daria 10%", o que equivale a TO 50%. | Ver N-3. |
| GB-4 (297,28 computável) | Pré-Estudo v9 linha 29 e Etapa 01 (teto computável). | Confirmado para a fonte. **Enunciado não corrigido: ver N-1.** |

Fontes da Isca 3 e da Isca 6 também conferidas: LC 270 Art. 352 (p. 125): "A SMD corresponde a vinte por cento da área livre do terreno resultante da aplicação da Taxa de Ocupação máxima, definida no Anexo XXI". Confirmado.

Conta da SMD (refeita): com TO 50%, área livre = 571,80 × 0,50 = 285,90 m², SMD = 20% × 285,90 = **57,18 m²** (= 10% do terreno, valor da Etapa 01). Com TO 40% (régua do condomínio, não da zona), área livre = 343,08 m², SMD = **68,62 m²**. Conta confere com o gabarito.

## 2. Erros e pontos abertos achados nesta checagem

- **E-1 (resíduo de GE-1; erro do Bardi).** Isca 1 (linha 48) e Isca 2 (linha 59) citam "COES Art. 31 V (p. 17)" sem nomear a cópia. Na cópia do acervo D:\008, a p. 17 não tem o Art. 31. Quem conferir no acervo não acha a página. A cópia SMU é a que o gabarito usa; a "impressaoWeb_Claudemberg" existe em Hely/Fontes_Legislacao e **não foi conferida**. Correção: citar a cópia em toda página de COES. Erro do gabarito, não descontado do executor.
- **N-1 (enunciado contradiz o dossiê; erro do Bardi).** O enunciado v2 ainda diz, na linha 45 (Levantamento, Resumo): "Em H1 não cabe (construída máxima de 297,28 m²)". A Viabilidade v9 e as Etapas 01–03 tratam 297,28 como **computável**. O GB-4 reconhece o erro, mas o enunciado não foi corrigido, por ser lacrado. Isso é falha do enunciado, não do executor. Decisão de Claudemberg: corrigir em versão futura do enunciado ou registrar como nota de correção.
- **N-2 (alcance de "não é solução").** Dec. 3.046 XXII já exclui o afastamento frontal da área livre para estacionamento. Então "não é solução" vem do próprio texto, e não só da errata. O que fica com o Gate é a exceção, se houver. Mantém-se a redação do gabarito. Ponto de julgamento, não erro.
- **N-3 (GB-3 talvez não precise de decisão).** O gabarito diz "TO 50% depende da Etapa 01; decisão de Claudemberg pendente". Porém o RIU do caso (§5.3) já dá TO 50%, e a Etapa 01 aprovada (item 14, "daria 10%") aplica 50%. A pendência pode ser fechada por Claudemberg com essa evidência. **Não decidido aqui.**
- **N-4 (processo).** A checagem usada é proposta, não instalada em `.claude/skills/`. Pedido à Drenagem: pôr o status da Skill na pauta de ratificação.

## 3. Itens que não foram reconferidos nesta rodada (herdados, marcados no próprio gabarito)

LC 281 Art. 20 (p. 8); LC 270 Art. 345 §3º, Art. 278 XIV, Art. 458, Anexo XXI e Anexo XXV; Dec. 3.046 Disp. Gerais XV (p. 3); COES glossário "TELHADO" (p. 29); NBR 9050 edição 2020 (acervo só tem 2015); Código Civil Arts. 1.301–1.302; DL 9.760/1946 Art. 2º; Lei 12.651/2012 Art. 4º II "b".

## 4. Veredito da checagem (para a Drenagem gravar; não altera o estado)

- GE-1 a GE-6: **corrigidos com fonte confirmada**, com resíduo E-1 (citação de cópia do COES).
- GB-1, GB-2, GB-4: confirmados para as fontes. GB-3: ver N-3.
- Erro novo no enunciado: N-1 (297,28 "construída máxima"), não corrigido.
- Lacre: **não confirmado** (sem hash recalculado por Bardi).
- Erros do gabarito: Bardi. Não descontar dos executores (decisão de 08/10).

Nenhum arquivo do ensaio foi alterado. Gabarito não reescrito. Estado do ensaio não editado. Nenhum Gestor ou Agente acionado.
