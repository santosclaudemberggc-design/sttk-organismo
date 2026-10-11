---
name: ensaio-sombra-checagem-gabarito-antes-lacre
description: Checklist obrigatório que o examinador (Bardi) cumpre antes de lacrar qualquer gabarito do Ensaio Sombra — refazer toda conta da isca, conferir se o inciso ou artigo se aplica à situação da isca, e testar a isca contra a fonte primária com página. Use sempre que um examinador ou revisor for escrever, revisar ou lacrar um gabarito de etapa do Ensaio Sombra, ou corrigir um gabarito já lacrado — mesmo que o pedido só mencione "gabarito", "isca", "lacre" ou "checagem", sem citar a Skill pelo nome.
version: v1.0
status: proposta
data: 2026-10-09
origem: "Pendência skill-nova-bardi-checagem-gabarito-08-10 (Drenagem Contínua, 09/10/2026). Erros de gabarito da Etapa 03 (G1, G2, G4), registrados em CONSTRUCAO_DO_ZERO/01_CEO/Agentes_Diretos/Bardi (Examinador)/checagem_gabarito_etapa3_09-10-2026.md."
tipo: Processo (Examinador)
validacao: "PROPOSTA. Não instalada em .claude/skills. Ativação depende de validação de Claudemberg. Caso de treino fictício na seção 6."
---

# Skill — Checagem de Gabarito Antes de Lacrar (Ensaio Sombra)

## 1. Para que serve

Um gabarito errado reprova o executor por erro do examinador. Na Etapa 03 (08/10/2026), três iscas tinham conta ou leitura erradas: uma aplicava um inciso que não era o da situação, outra tinha conta que se contradizia e outra tinha área errada. Esta Skill existe para que nenhuma isca seja lacrada sem passar por três checagens que deixam prova escrita.

Regra da casa (Claudemberg, 08/10/2026): erro de gabarito é do examinador. Não desconta do executor. O examinador corrige a própria checagem.

## 2. Quando usar

- Antes de lacrar qualquer gabarito de etapa do Ensaio Sombra.
- Ao corrigir um gabarito já lacrado, para registrar erro. O lacre não é reescrito sem ordem de Claudemberg.

## 3. Checklist obrigatório (as três checagens são cumulativas)

**Checagem 1 — Refazer toda conta da isca.**
- Escreva a conta com a área, o pavimento e o regime de medição explícitos (construída, computável, projeção, área útil).
- Refaça a conta do começo, sem copiar o resultado do gabarito.
- Confirme que a conclusão ("cabe", "não cabe", "ultrapassa", "falta") bate com o número. Se a conta dá 407 e o gabarito diz "cabe em 520", a isca está errada.
- Número sem fonte não vira conta. Se não há artigo lido, o número entra como "ponto de julgamento", não como resultado.

**Checagem 2 — Conferir se o inciso ou artigo se aplica à situação da isca.**
- Leia o dispositivo inteiro, incluindo o último período. Muitos incisos terminam com remissão a outro inciso ("será aplicado o disposto no inciso X").
- Confirme o tipo de edificação, a zona e a subzona, e se a exceção ou a remissão muda o caso.
- Pergunte: a regra que eu cito proíbe, permite ou manda aplicar outra regra? Se for permissão, não use como restrição.

**Checagem 3 — Testar a isca contra a fonte primária, com página.**
- Abra o PDF da lei ou norma na página citada e confirme o texto. Página citada de memória não vale.
- Se a fonte não está no acervo, registre "não verificado" na checagem. Não use como gabarito.
- Compare a isca com as ERRATAS das etapas já aprovadas e com o dossiê. Se o dossiê diz uma medida e a conta do gabarito usa outra, a isca está contaminada.

## 4. Verificações extras (obrigatórias quando se aplicam)

- **Premissa de área:** confirme a base (matrícula, levantamento, RIU). Dossiê com dois números para a mesma área é inconsistência do enunciado, a corrigir antes de lacrar.
- **Fórmula impressa:** a fórmula escrita no gabarito é a mesma que dá o resultado. Refaça a fórmula, não só o número.
- **Dois limites do mesmo lote:** quando há teto de taxa e envelope geométrico, calcule os dois e diga qual vale (o menor). Não compare um número com o outro sem fixar o regime.
- **Parâmetro de condomínio ou regulamento:** não é primário. Registre como premissa do dossiê.
- **Remissão de página em cada citação:** cada "p. X" do gabarito é conferida no PDF.

## 5. Registro obrigatório

A checagem sai em arquivo, com tabela isca a isca: conta refeita, saída, fonte e página, e o status (confirmado, contradito ou não verificado). Sem arquivo, não há lacre. O arquivo fica na pasta do examinador, fora da pasta do ensaio.

## 6. Treino em caso fictício

Caso fictício, sem relação com as etapas do Ensaio 003. Lote de 10,00 m de frente × 30,00 m de profundidade (área 300 m²). Afastamento frontal de 4,00 m, laterais de 1,50 m cada, fundos de 3,00 m. Taxa de ocupação de 40% (premissa do caso, não primário).

Isca proposta (com erro de propósito): "Taxa de ocupação de 40% de 300 m² dá projeção máxima de 120 m². Com frente de 9,50 m, o envelope de afastamentos cai para 9,50 − 3,00 = 6,50 m de largura por 30 − 4 − 3 = 23 m de profundidade, ou seja 149,50 m². Portanto a projeção máxima passa a ser 149,50 m²."

Checagem 1 (conta): taxa = 0,40 × 300 = 120 (correto). Largura útil = 9,50 − 2 × 1,50 = 6,50 (correto). Profundidade = 30 − 4 − 3 = 23 (correto). Envelope = 6,50 × 23 = 149,50 (correto). A conta fecha.

Checagem 2 (regime e aplicação): a taxa é teto de projeção, e o envelope é limite geométrico de implantação. Os dois valem ao mesmo tempo, e prevalece o menor. Com envelope de 149,50 e teto de 120, prevalece 120 m². A conclusão "passa a ser 149,50" ignora o teto e está errada, mesmo com a conta certa.

Checagem 3 (fonte): a taxa de 40% é premissa do caso fictício, sem artigo lido. Registrar "premissa do caso, não primário" e não usar como número de regra.

Resultado do treino: a isca não é lacrável. O erro não está na conta, e sim na conclusão, que ignora o limite que de fato prevalece. Aprendizado: calcular todos os limites do mesmo lote e declarar qual vale, antes de escrever "passa a ser".

## 7. O que esta Skill não faz

- Não define critério de nota. Quem decide nota é `ensaio-sombra-criterios-aprovacao-por-etapa` (mínimo 8,00, erro de gabarito não desconta do executor).
- Não substitui a leitura da fonte primária.
- Não aprova nem reprova gabarito. Quem aprova é Claudemberg.
