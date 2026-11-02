# Correções do Briefing Único v2: parte de Paisagismo (Glaziou, 31/10/2026)

> Pedido de Claudemberg, via Cardozo. Base: `briefing_revisao_final_8_agentes_31-10.md` (ALTO 1, D6, MÉDIOS e BAIXOS) e `briefing_modelo_v2_proposta.md`.
> **Não editei o Briefing.** O Oscar junta. Não toquei no Ensaio 003, no Drive nem em commit.
> **Meu nível:** Autonomous provisório. Esta proposta passa pela auditoria do Cardozo antes de qualquer uso.
> Números de linha = linhas do `briefing_modelo_v2_proposta.md` como estava em 31/10.

---

## G-1. ALTO 1: a C-11 não tinha efeito (C-1 e C-3)

**Problema.** A C-11 diz que a PAI-01 e a PAI-02 são obrigatórias, mas o Gate (C-3) confere só a lista da C-1, e a C-1 não cita as duas. Resultado: o Briefing pode ir para o EP sem elas. Solução: pôr as duas **dentro da C-1**, do mesmo jeito que a AUT-01 já está ("quando a seção aparecer"), e deixar a C-3 dizer que confere também essas obrigatórias condicionais. Assim existe uma lista só, e o Gate a confere.

### G-1a. C-1 (linha 180)

- **Texto atual:** "e AUT-01 quando a seção de automação aparecer."
- **Texto novo:** "e AUT-01 quando a seção de automação aparecer; e PAI-01 e PAI-02 quando a seção de Paisagismo (6-bis) aparecer (motivo na C-11)."
- **Motivo:** é a C-1 que o Gate confere. Sem isso, a C-11 fica sem efeito. Troco só esse trecho; o resto da C-1 (inclusive a saída da MED-01 pela D1) é com o Oscar.

### G-1b. C-3 (linha 201)

- **Texto atual:** "depois de conferir C-1 completa, cada C disparado listado e TI-01, TI-05, TI-09 anexadas."
- **Texto novo:** "depois de conferir C-1 completa (inclusive as obrigatórias que só valem quando a seção aparece: AUT-01 com Automação e PAI-01 e PAI-02 com Paisagismo), cada C disparado listado (C-2 e, com Paisagismo, C-12) e TI-01, TI-05, TI-09 anexadas."
- **Motivo:** deixa escrito que o Gate confere as obrigatórias condicionais e os disparos de Paisagismo. Hoje a C-3 fala em "cada C disparado", mas a C-12 é uma tabela separada e pode ficar de fora.

### G-1c. C-11 (linha 217)

- **Texto atual:** "São obrigatórias a **PAI-01** e a **PAI-02**. Sem elas não dá para escolher as espécies nem dividir o lote."
- **Texto novo:** "São obrigatórias a **PAI-01** e a **PAI-02** (estão na lista da C-1, que o Gate confere na C-3). Sem elas não dá para escolher as espécies nem dividir o lote."
- **Motivo:** liga a C-11 à C-1. Quem ler só a C-11 sabe onde a regra é cobrada.

**O que eu NÃO proponho:** pôr as TI-PAI no Gate da C-3. Elas são necessárias antes do **meu** estudo de paisagismo, não antes do EP de arquitetura. Se o Gate exigisse, por exemplo, o ensaio de infiltração (TI-PAI-01), travaria o EP inteiro por causa do jardim.

---

## G-2. D6: regras do escritório ditas ao cliente

Decisão de Claudemberg (31/10): recusar planta invasora e seguir as regras de playground (NBR 16071) em casa particular são **regras do escritório**, e o Briefing diz isso ao cliente. O aviso tem de ficar **na pergunta que o cliente vê**, e não só nas regras internas (C-12), que ele não lê.

### G-2a. PAI-04 (linha 129): aviso da planta invasora

- **Texto atual (coluna Pergunta):** "Plantas: há alguma que vocês querem muito, ou que não querem de jeito nenhum?"
- **Texto novo (coluna Pergunta):** "Plantas: há alguma que vocês querem muito, ou que não querem de jeito nenhum? **Regra do escritório:** não colocamos no projeto plantas invasoras, que são plantas vindas de fora que se espalham sozinhas e tomam o lugar da mata nativa (exemplos: leucena, espatódea, jaqueira). Isso é regra nossa, não da lei: nenhuma lei obriga uma casa particular a seguir essa regra. Se vocês pedirem uma delas, explicamos o motivo e sugerimos outra parecida."
- **Texto atual (coluna Decisão que muda):** "Uma planta pedida pelo cliente que seja invasora (IBAMA/INEA-RJ) é recusada com explicação, nunca entra calada"
- **Texto novo (coluna Decisão que muda):** "Uma planta pedida pelo cliente que seja invasora é recusada com explicação, nunca entra calada. Regra do escritório (D6, C-13), avisada na própria pergunta"
- **Motivo:** D6. A PAI-04 é respondida em casa (C), sem ninguém da equipe ao lado, então o aviso precisa estar escrito. Os três exemplos vêm da Skill `nbr16636-paisagismo-predial` (linha 30: *Leucaena leucocephala*, *Spathodea campanulata*, *Artocarpus heterophyllus*). Pus a jaqueira de propósito: é o pedido "da casa da avó" mais provável, e a pergunta convida esse tipo de lembrança.

### G-2b. PAI-02 (linha 127): aviso do playground

- **Texto atual (coluna Pergunta):** "Para que vocês querem usar o jardim?"
- **Texto novo (coluna Pergunta):** "Para que vocês querem usar o jardim? (Se marcarem "crianças brincarem": **regra do escritório** é seguir a norma técnica de playgrounds, a NBR 16071, com piso que amortece a queda e espaço seguro em volta dos brinquedos. Isso é regra nossa, não da lei: em casa particular nenhuma lei obriga a seguir essa norma. Seguimos porque são as crianças de vocês que vão brincar ali.)"
- **Motivo:** D6. A PAI-02 é feita na reunião (R), mas o texto escrito garante que o aviso não dependa da memória de quem conduz. Só citei o que já está nos meus registros: piso dimensionado pela altura de queda e zona de segurança. Não pus nenhum número da norma: a Skill não tem esses parâmetros (lacuna já sinalizada ao Cardozo em 12/09).

### G-2c. C-12, 1ª linha (linha 223)

- **Texto atual (coluna Dispara):** "Se a PAI-02 tiver "crianças brincarem", entram as regras de playground (NBR 16071)"
- **Texto novo (coluna Dispara):** "Se a PAI-02 tiver "crianças brincarem", ou a PRG-01 tiver "playground", entram as regras de playground (NBR 16071), como regra do escritório (C-13)"
- **Motivo:** D6, e também o achado G-6 abaixo (a PRG-01 já tem "playground" como cômodo).

### G-2d. Regra nova C-13 (depois da C-12)

- **Texto atual:** não existe.
- **Texto novo:**

> **C-13. Regras do escritório que vão além da lei (decisão de Claudemberg, D6, 31/10/2026).** Duas regras de Paisagismo não são exigência legal para casa particular. São regras nossas, e o cliente é avisado na própria pergunta, com a frase "é regra nossa, não da lei":
> 1. **Planta invasora não entra no projeto.** Aviso ao cliente na PAI-04. Pedido do cliente por planta invasora é recusado com explicação e com sugestão de outra espécie parecida. Lista de referência: a lista oficial de espécies exóticas invasoras. A revisão de 31/10 cita a Res. SMAC 492/2011, e o Briefing citava "IBAMA/INEA-RJ". **O Hely confere qual é a lista e o número certo na fonte antes que qualquer um dos dois seja citado ao cliente.**
> 2. **Área de criança segue a NBR 16071 (playgrounds).** Aviso ao cliente na PAI-02 e na PRG-01. Vale quando a PAI-02 tiver "crianças brincarem" ou a PRG-01 tiver "playground".
>
> Quem conduz a reunião não chama essas regras de "exigência da lei" nem de "a norma obriga".

- **Motivo:** concentra a D6 num lugar só, para o Bardi e o Gate conferirem. Não pus o número da resolução no texto ao cliente porque não o li na fonte: ele aparece só no relatório de revisão, e não há nenhuma outra menção a ele no projeto. A Skill de remoção de árvores (R3) já manda conferir resoluções SMAC no portal oficial antes de citar ao cliente.

---

## G-3. "Usado por": incluir o Glaziou

### G-3a. MOR-02 (linha 52)

- **Texto atual (Usado por):** "Oscar, Tenreiro"
- **Texto novo (Usado por):** "Oscar, Tenreiro, Glaziou"
- **Motivo:** a C-12 usa "MOR-02 com alergia" para evitar plantas de muito pólen. Também entra na base do consentimento da K2 (LGPD): quem usa o dado precisa estar listado.

### G-3b. SUS-01 (linha 100)

- **Texto atual (Usado por):** "Oscar, Saturnino, Landell"
- **Texto novo (Usado por):** "Oscar, Saturnino, Landell, Glaziou"
- **Motivo:** a C-12 usa "SUS-01 com água de chuva" para a cisterna de irrigação com o extravasor indo para o jardim de chuva.

### G-3c. EST-01 e EST-03 (linhas 86 e 88), achado BAIXO meu

- **Texto atual (Usado por), nas duas:** "Oscar, Tenreiro"
- **Texto novo (Usado por), nas duas:** "Oscar, Tenreiro, Glaziou"
- **Motivo:** a lista "Não repete" da Seção 6-bis (linha 122) diz que eu uso a EST-01, a EST-02 e a EST-03, mas só a EST-02 me cita. O estilo da casa orienta o estilo do jardim, e a EST-03 ("o que não querem de jeito nenhum: estilo, material, cor") vale também para piso externo, pérgola e cores de floração.

---

## G-4. Pergunta de água de chuva do Saturnino

Se o Saturnino criar uma pergunta de sustentabilidade sobre água de chuva (decisão de Claudemberg: "reuso e água de chuva entram como pergunta de sustentabilidade"), **eu também uso essa pergunta. Não crio outra.**

- **O que muda no meu lado, só se o código mudar:** na C-12, a linha "SUS-01 com água de chuva" passa a citar o código novo do Saturnino, e o "Usado por" da pergunta nova inclui o Glaziou (pelo mesmo motivo de G-3b). Se ficar na própria SUS-01, vale só o G-3b.

---

## G-5. MÉDIO: ano da NBR 9575 na TI-PAI-06 (linha 174)

- **Texto atual:** "a impermeabilização com anti-raiz segue a NBR 9575:2024"
- **Texto novo:** "a impermeabilização com anti-raiz segue a NBR 9575 na edição vigente (ano conferido pelo Hely no catálogo da ABNT)"
- **Motivo:** a revisão de 31/10 diz que a edição é de 2010, confirmada em 2024. A Skill `nbr9575-impermeabilizacao` (linha 49) diz "edição vigente jul/2024". As duas fontes discordam, e eu não li a norma: ela não está no acervo `D:\008_Normas ABNT`. Tiro o ano até o Hely conferir. Vou sinalizar ao Cardozo a possível correção da Skill (não é coisa para o Briefing).

---

## G-6. MÉDIO: "playground" na PRG-01 sem regra

- **Linha:** PRG-01 (linha 62) tem "playground" na lista de cômodos, que todos veem. A regra NBR 16071 (C-12) só dispara com Paisagismo contratado **e** com "crianças brincarem" na PAI-02.
- **Texto atual (PRG-01, coluna Pergunta):** "Quais cômodos vocês querem?"
- **Texto novo (PRG-01, coluna Pergunta):** "Quais cômodos vocês querem? (Se marcarem "playground": regra do escritório é seguir a norma técnica de playgrounds, a NBR 16071. Isso é regra nossa, não da lei.)"
- **Motivo:** quem contrata só Arquitetura e marca "playground" não recebe o aviso da D6, e a regra não teria dono. Para o dono, proponho a mesma solução do ALTO 2: **com Paisagismo contratado, o Glaziou; sem Paisagismo, o Oscar**, como nota no estudo. A escolha do dono é do Oscar/Lúcio, não minha. A troca na C-12 está em G-2c.

---

## G-7. BAIXO: PET-01 com "ainda não sei" (se o Oscar criar a opção)

- **Linha:** C-12, 1ª linha (linha 223).
- **Texto atual:** "PET-01 = "sim" ou "pretendemos ter""
- **Texto novo (só se a opção "ainda não sei" entrar na PET-01):** "PET-01 = "sim", "pretendemos ter" ou "ainda não sei""
- **Motivo:** tirar planta tóxica e com espinho das áreas de uso custa pouco, e "ainda não sei" pode virar um pet depois da obra. Na dúvida, fica a escolha que protege.

---

## G-8. BAIXO: MOR-02 depois do consentimento da LGPD (K2)

- **Linha:** C-12, linha "MOR-02 com alergia" (linha 225).
- **Texto atual (coluna Resposta):** "MOR-02 com alergia"
- **Texto novo (coluna Resposta):** "MOR-02 com alergia (só com o consentimento da K2 marcado; "prefiro não informar" não dispara nada e não se presume alergia)"
- **Motivo:** a K2 cria o consentimento destacado e a opção "prefiro não informar". O meu disparo não pode usar o dado de saúde sem esse consentimento, nem adivinhar a resposta.

---

## G-9. Pergunta para Claudemberg (não é correção)

A C-12 também tira **planta tóxica ou com espinho** das áreas de uso quando há criança ou pet. Isso também é regra nossa, não da lei, mas a D6 não fala dela. Fica a pergunta: ela entra na C-13 com o mesmo aviso ao cliente? Não incluí sem a decisão dele.

---

## Tempo

Os avisos G-2a, G-2b e G-6 somam três frases de leitura. O efeito no tempo deve ser pequeno, mas não foi medido; fica para medir na primeira aplicação, como o resto da tabela de tempo.
