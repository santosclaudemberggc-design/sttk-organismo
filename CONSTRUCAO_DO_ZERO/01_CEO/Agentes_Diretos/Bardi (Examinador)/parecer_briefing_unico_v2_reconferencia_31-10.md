# Parecer Bardi: reconferência do Briefing Único v2 depois das correções de 31/10 (noite)

- **Pedido:** Claudemberg, via Wallenberg. Fora do Ensaio 003. Nada lançado em `notas_assertividade.md` nem em `registro.json`.
- **Lido:** `briefing_revisao_final_8_agentes_31-10.md` (gabarito: CRÍTICOS, ALTOS e "Decisões de Claudemberg"), `briefing_modelo_v2_proposta.md` (406 linhas), `correcoes_31-10\auditoria_cardozo.md`, `correcoes_31-10\kelsen.md`, `correcoes_31-10\oscar_aplicacao.md` e `briefing_modelo_v2_diferencas.md`. Também conferi a Skill `coe-lc198-...` (ALTO 11). As linhas citadas são da proposta, salvo outra indicação.
- **Não editei nada.** Não toquei no Ensaio 003 nem no Drive. Não fiz commit.

## Nota e veredito

**Nota do Briefing (executor: Oscar): 8,25.**
**Veredito recomendado:** APROVAR o conteúdo. **Não usar com cliente real** até fechar as 5 pendências bloqueantes da última seção. A decisão é de Claudemberg.

O que tirou ponto: 6 achados MÉDIOS (−1,40) e 7 BAIXOS (−0,35). Nenhum é CRÍTICO ou ALTO. Todos os números declarados batem com a minha contagem.

## 1. Gabarito: CRÍTICOS, ALTOS e decisões de Claudemberg

| Item | Resolvido? | Prova (linha e trecho) |
|---|---|---|
| K1 Forms | Sim | L293, C-4: "O Briefing não vai para o Google Forms nem para pasta de Drive". O Grep de "Forms\|Drive\|link" acha só negações e histórico (L3, L4, L293, L361), o "links de casas" da EST-02 (L134) e os formulários de origem (L7, L20, L209). Parte D em L365-405 |
| K1 A Parte D basta? | Basta como contrato mínimo, com 2 lacunas MÉDIAS (M1 e M2) | D-1 campos (L369-383); D-2 condições e listas (L385-390); D-3 guarda (L392-399); D-4 isolamento: "Nenhum cliente vê a sessão, as respostas ou os arquivos de outro" (L403) |
| K2 LGPD MOR-02 | Sim | L72 CON-01 "vem desmarcada"; L73 MOR-02 "só se a CON-01 estiver marcada" e "prefiro não informar" |
| ALTO 1 | Sim | L265: "PAI-01 e PAI-02 quando a Seção 6-bis aparecer"; L291 C-3 confere |
| ALTO 2 | Sim, com a lacuna M5 | L211: "o Oscar fica com ela no Levantamento, só para o fato de campo" |
| ALTO 3 | Sim | L157 HID-03: "ESC-01 contém Hidrossanitário **OU** Elétrico" |
| ALTO 4 + decisão de Arquitetura | Sim | L46 CAS-01 na Seção 0; L50 [A CONFERIR] sobre o campo do Pré-Briefing |
| ALTO 5 + elevador e plataforma | Sim | L75 ACE-01; L272, choque C5 × C4: "a sala sobe para o andar de cima" |
| ALTO 6 | Sim (com pendências) | L52-61 PRV-01 |
| ALTO 7 | Sim | L80-85 RES-01 |
| ALTO 8 | Sim, conforme a decisão | L361 C-17: "Se o sistema for hospedado fora do Brasil, incluir aviso" |
| ALTO 9 | Sim | L195-203 DEC-01: quatro caixas, uma por contratante, versão e data |
| ALTO 10 | Marcado, não resolvido na fonte | L299: "Os números 2,50 m e 2,30 m só ficam firmes depois de alguém ler a edição de 2025" (ver M6) |
| ALTO 11 | Sim, na Skill | Skill COES L93: "Casa unifamiliar ou bifamiliar: mínimo de 1,50 m (COES Art. 31, parágrafo único)" |
| ALTO 12 | Sim | L228 TI-14; L289 disparo na C-2; L291 TI-14 na C-3 |
| ALTO 13 (Estrutural) + decisão | Sim | sondagem preliminar L215 e complemento L247; CAA/CC L248; disparos C-14 L325-340; piscina TER-01 linha 5 (L109); mais um andar TER-01 linha 6 |
| ALTO 14 (Elétrica) + decisão | Sim | L254 TI-ELE-01 (Light); L255 TI-ELE-02 (falta de luz), "Respondidas pelo Landell logo depois da visita" (L250) |
| ALTO 15 (Hidro) + decisão | Sim | L148 SUS-01 (chuva e água do banho); L149 SUS-02 (para que serve); L151 HID-04; L257 nota da piscina |
| ALTO 16 (Interiores) + decisão | Sim | L161 ILU-02; L136 EST-06; L168 INT-04; L165 INT-01 com "banheiros" e "área gourmet" |
| D1 | Sim | L126 MED-01 retirada; L283 NIV-01 define a folga |
| D2 | Sim | L166: "Aconchegante / Sofisticado / Minimalista / Contemporâneo (opções do FORM-INT)" |
| D3 | Sim | L321 C-13; L47 "Automação (inclui o projeto Elétrico)" |
| D4 | Sim | L121, L299 e L202: "no mínimo nessas referências e, salvo pedido seu por escrito, acima delas" |
| D5 | Sim (e-mail e prazo pendentes, como decidido) | L63: "microempresa ou EPP, sem encarregado obrigatório, com canal de contato" |
| D6 | Sim | L179 PAI-02, L181 PAI-04 e L104 PRG-01 com "regra do escritório"; C-16 (L354-359) |

## 2. Números: minha contagem por Grep (padrão `^\| ~?~?[A-Z]{2,3}-\d\d`)

| Item | Oscar declarou | Minha contagem | Bate? |
|---|---|---|---|
| Códigos ativos | 63 (68 − 5) | S0 6 (L43-48) · S1 10 (L69-78) · S2 10 (12 linhas − VIS-01/VIS-03) · S3 1 · S4 5 (6 − EST-04) · S5 8 · S6 12 · 6-bis 6 · S7 5 = **63**; 5 retiradas (L112, L114, L126, L127, L137) | Sim |
| Só Arquitetura | até 45 | S0+S1+S2+S3+S4+S5+S7 = 45; condicionais: RES-01, MOR-02, ACE-01, HID-02, SUS-02, GOU-01 e HID-04 = 7; fixas = 38 | Sim |
| Completo sem Paisagismo | até 56 | 45 + 12 − ELE-02 (some com Automação, L159) = 56 | Sim |
| Completo com Paisagismo | até 62 | 56 + 6 | Sim |
| Tarefas internas | 24 | TI-01 a TI-14 (L215-228) = 14; TI-PAI 6 (L236-241); TI-EST 2 (L247-248); TI-ELE 2 (L254-255) | Sim |
| Regras | C-1 a C-17 | Grep `^\*\*C-\d+\.`: 17 títulos, de L265 a L361, sem falha nem repetição | Sim |
| Tempo | 46,5 / 34; 54 / 53 | refiz as somas: 28 itens R = 46,5; 17 itens C = 34; complementares 15 − 1 = 14; 46,5 + 2 + 5,5 = 54; 34 + 14 + 5 = 53 | Sim (faixa: ver B1) |

Nenhum código de pergunta está duplicado no banco (as repetições do Grep em L271-351 são linhas de regra, não perguntas).

## 3. Achados por gravidade

**CRÍTICOS:** nenhum. **ALTOS:** nenhum.

**MÉDIOS**
- **M1. A Parte D se contradiz sobre a INT-04.** L388: "CLI-01, INT-01 e INT-04 usam os cômodos da PRG-01 [...]; a INT-02 e a INT-04 usam os cômodos marcados na INT-01". A linha da INT-04 (L168) diz "os cômodos do INT-01". Quem montar o sistema recebe duas fontes para a mesma lista. Dono: Oscar.
- **M2. A MOR-01 é texto livre, mas alimenta condições e listas.** L70: "TXT (uma linha por pessoa)". Dependem dela a RES-01 ("alguém com menos de 18 anos", L71), a C-2 ("60 anos ou mais", L271), a C-12 ("criança", L313) e a MOR-02 ("quem (só o parentesco da MOR-01)", L73). A D-2 (L388) não lista a MOR-01 como origem de lista, e a D-1 não pede que ela seja estruturada (parentesco + idade em número). O sistema não consegue aplicar essas condições sobre texto livre. A D-2 também não cita a PRG-02 ("por cômodo", L105) nem a AUT-02 ("sistema × cômodos", L163). Dono: Oscar.
- **M3. Códigos e notas internas aparecem nas colunas que o cliente lê.** A legenda diz (L37): "O cliente não vê os códigos". Mesmo assim: na ELE-02, na coluna Pergunta (L159), "(câmeras e alarme já estão em SEG-01)"; na ROT-02 (L77), "o pet (se houver, PET-01)"; na HID-03 (L157), "(O sol já foi perguntado em SUS-01 [...])"; na AUT-02 (L163), "Itens de SEG-01 e a irrigação do ESC-02 entram sozinhos"; na CAS-01 (L46), "são as linhas 1 e 6 da TER-01". O Cardozo já tinha condenado esse padrão no "C-13" da ESC-01 (auditoria, L29), e ele continua em outras 5 linhas. Para o sistema (D-1, L375: "Texto ao cliente | o texto da coluna 'Pergunta'"), não há como separar a opção da nota interna. Dono: Oscar.
- **M4. O cabeçalho ainda diz APROVADO, com uma pendência só.** L3: "**APROVADO por Claudemberg em 31/10/2026** [...] Pendências abertas: medir o tempo na 1ª aplicação". L4 diz o contrário: "Precisa de nova conferência do Bardi [...] antes de qualquer uso". Hoje existem pelo menos 13 marcas de pendência (seção 4). Quem lê só a L3 acha que pode usar o Briefing. Dono: Oscar.
- **M5. A TI-01 fica sem dono técnico quando o Estrutural não é contratado.** L215: "O Baumgart define quantos furos, onde e até que profundidade antes de a sondagem ser contratada". A regra geral da L211 manda o Oscar só registrar o fato de campo, e a especificação vira nota. Só que a C-3 (L291) exige a "TI-01 [...] anexada" para começar o EP, e a TI-14 (L228) usa a sondagem como entrada. Sem Estrutural contratado, não está escrito se a sondagem preliminar é feita nem quem a especifica. A lista de "exemplos já escritos" da L211 não inclui a TI-01. Dono: Oscar, com o Cardozo (a auditoria não pegou).
- **M6. O texto ao cliente afirma números que o próprio Briefing diz não estarem firmes.** L121 (cliente): "exige pé-direito [...] de no mínimo 2,50 m, ou 2,30 m". L299 (C-7): "Os números 2,50 m e 2,30 m só ficam firmes depois de alguém ler a edição de 2025". Uma afirmação ao cliente se apoia numa edição não vigente (NBR 15575-1:2024), e a vigente (2025) não foi lida. Dono: Kelsen/Hely (ler a de 2025); Oscar (tirar os números do texto até lá, ou manter com a ressalva).

**BAIXOS**
- **B1.** Faixa de tempo incoerente. L27: "53 min, **cerca de 50 a 55 min**". Nas outras linhas, a faixa fica acima da soma (34 → "35 a 40").
- **B2.** "C5" (regra da Skill) e "C-5" (regra do Briefing) se confundem. Exemplos: L98 "não dispara a C5 pela MOR-02" e L271 "C5 suíte principal", contra C-5 "Proposta por cômodo" (L295).
- **B3.** Página do COES sem o nome da cópia. L299 cita "Art. 31, p. 21" (cópia `D:\008`) e "Art. 17, §3º (p. 9)" (paginação da cópia SMU do Kelsen, `kelsen.md` L5). São duas cópias com paginações diferentes, sem dizer qual é qual.
- **B4.** "Criança" sem idade na C-12 (L313), enquanto a RES-01 usa "menor de 18 anos" (L82) e "idoso" ganhou definição (L271).
- **B5.** Termos sem explicação no que o cliente ouve ou lê: "cooktop" e "cubas" (L144); "nobreak" (L255, pergunta 4 da visita); "quadros" (L323, texto da C-13).
- **B6.** A D-1 não tem campo para texto sem código: o texto informativo da Seção 3 (L119-121), o texto da C-13 ao cliente (L323) e a "Ajuda ao cliente" da SUS-01 (L148) não têm onde entrar no sistema.
- **B7.** A D-3 (L395) guarda a data em que a autorização foi retirada, mas não diz o que acontece com a MOR-02 já respondida (apagar ou esconder; refazer os disparos C5 e C-12). LGPD Art. 8º, §5º e Art. 18, IX (de memória, não reaberto).

## 4. LGPD (item 5 do pedido)

| Ponto | Resultado | Prova |
|---|---|---|
| Consentimento livre (CON-01 fora da C-1) | Sim | L265: "CON-01 e RES-01 nunca são obrigatórias" |
| Caixa desmarcada | Sim | L72: "Caixa única, que **vem desmarcada**"; L71 RES-01: "vêm desmarcadas" |
| "Prefiro não informar" | Sim | L73, com a regra de não marcar junto com outra opção |
| MOR-02 depende da CON-01 | Sim | L73: "só se a CON-01 estiver marcada; sem ela, registra 'não informado'" |
| Risco que fica | A pergunta 1 da TI-ELE-02, feita na visita, usa a CON-01 cujo texto diz "A próxima pergunta é sobre saúde" (L90) | L98 e L255: "A confirmar pelo Kelsen" |

## 5. Pendências que restaram (Grep `PENDENTE|A CONFERIR|[Aa] confirmar|a conferir|acredito`)

| Linha | Pendência | Impede usar com cliente real? |
|---|---|---|
| L55 | [PENDENTE: Claudemberg (razão social e CNPJ)] | **Sim.** O aviso de privacidade sem o nome de quem responde pelos dados não cumpre a função dele (LGPD Art. 9º) |
| L60, L399 | [PENDENTE: Claudemberg (prazo de guarda)] | **Sim.** O aviso promete informar a duração |
| L61, L95 | [PENDENTE: Claudemberg (e-mail de privacidade)] | **Sim.** É o canal de contato que a D5 exige |
| L63 | Res. CD/ANPD nº 2/2022, Art. 11: "acredito que", "a conferir no texto antes do 1º cliente real" | **Sim**, pelo próprio texto (a dispensa do encarregado pode não valer para dado de saúde e de criança) |
| L361 | [PENDENTE: Claudemberg] Art. 33 para a IA; Res. CD/ANPD nº 19/2024 "a conferir" | **Sim, para dado de saúde.** O PRV-01 (L58) diz que a IA lê as respostas. Se ela processar fora do Brasil, a MOR-02 sai do país sem a autorização específica (Kelsen, "acredito") |
| L299 (sem marca) | NBR 15575-1:2025 não lida | Sim, para o texto da Seção 3 como está (M6). Não impede se os números saírem do texto |
| L50 | [A CONFERIR: opções do campo "Tipo de residência"] | Não: se o campo não servir, o cliente responde |
| L98, L255 | A confirmar pelo Kelsen: a CON-01 cobre a visita? | Não, se a visita usar só a versão neutra até a confirmação |
| L216 | Lei Estadual 9.164/2020 "a confirmar" | Não (interno, TI-02) |
| L227, L259 | [PENDENTE: Claudemberg] dono do projeto de gás | Não para aplicar o Briefing: a regra de transição existe (L259). É preciso decidir antes do EP de cliente que marcar "a gás" |
| L241 | NBR 9575:2010 "a conferir no catálogo da ABNT" | Não |
| L248 | CAA confirmada pelo cliente: "interpretação a confirmar no Gate" | Não (trava só o AP estrutural) |
| L348 | Res. Conj. 001/2005, Art. 6º: "A confirmar com o Kelsen" | Não (fica como opção comparada até lá) |
| L357 | [PENDENTE: Claudemberg] G-9, planta tóxica ou com espinho | Não (a proteção continua valendo como disparo da C-12) |
| L355 (sem marca) | Lista de invasoras: o Hely confere antes de citar | Não (a PAI-04 não cita a lista) |

**Observação para Claudemberg:** com o Forms fora (K1) e o Sistema de Gestão ainda no futuro, o Briefing não tem hoje um meio de aplicação escrito. Usar o Briefing com cliente real antes de o sistema existir exige uma decisão sua: por exemplo, aplicar na reunião com o documento em mãos. Não é erro do Oscar; ele seguiu a decisão K1.

## 6. O que corrigir (cada item com dono, tipo e fonte)

| # | Item | Dono | Tipo | Fonte |
|---|---|---|---|---|
| 1 | M1, M2, B6, B7 (Parte D) | Oscar | lacuna do Agente | o próprio Briefing (linhas citadas) |
| 2 | M3 (separar o texto ao cliente das notas internas) | Oscar | lacuna do Agente | legenda L37; auditoria do Cardozo L29 |
| 3 | M4 (cabeçalho) | Oscar | falha de processo | L3 × L4 |
| 4 | M5 (TI-01 sem Estrutural) | Oscar, com o Cardozo | lacuna do Agente e da auditoria | Skill `fundacoes-solos-moles-...` e NBR 8036 (fonte primária, fora do acervo) |
| 5 | M6 e pendência L299 (ler a NBR 15575-1:2025) | Kelsen/Hely | lacuna do organismo | catálogo ABNT; a norma comprada para o acervo |
| 6 | LGPD: Res. 2/2022, Res. 19/2024, Art. 33 para a IA | Kelsen | fora do organismo | texto oficial da ANPD e do Planalto |
| 7 | B1 a B5 | Oscar | lacuna do Agente | o próprio Briefing |

## 7. Fonte primária não verificada

- LGPD (Lei 13.709/2018): Arts. 5º, 8º, 9º, 11, 14, 18, 19 e 33. Não reabri; julguei pela coerência do Briefing com o parecer do Kelsen.
- Res. CD/ANPD nº 2/2022 e nº 19/2024: não estão no acervo.
- NBR 15575-1:2025: não está no acervo `D:\008` (só a de 2024).
- NBR 8036 e NBR 6484:2020: não verificadas.

## Adendo 02/11

**Pedido:** Wallenberg, conferência por amostragem dos 6 médios que o Oscar diz ter aplicado. **Lido:** `oscar_aplicacao_medios_02-11.md` e a proposta inteira (416 linhas). As linhas citadas são da proposta de 02/11. Não editei o Briefing. Não toquei no Ensaio 003 nem no Drive. Sem commit.

**Nota nova: 9,12 (era 8,25).** Ela sobe porque 4 médios fecharam, o M2 passou a baixo e o B4 fechou junto. Ela não chega a 10 por causa do resto do M3 e de 6 baixos novos. Sigo recomendando APROVAR o conteúdo. **Continua proibido usar com cliente real:** as pendências bloqueantes não mudaram, e agora a L8 lista todas.

| Achado | Situação | Prova |
|---|---|---|
| M1 | Resolvido | L397: "a INT-02 e a INT-04 usam só os cômodos marcados na INT-01". Bate com a L176 |
| M2 | Resolvido no essencial; sobra um resto baixo | L76: "GR [...] faixa de idade → 0 a 11 / 12 a 17 / 18 a 59 / 60 anos ou mais". L398 traz as condições sobre a MOR-01. Resto: a D-2 ainda não diz de onde vêm os cômodos da PRG-02 e da AUT-02. O Oscar declarou isso e deixou com o Lúcio |
| M3 | **Parcial: segue médio** | As 5 linhas citadas estão limpas (L52, L83, L165, L167, L171). A legenda (L43) passou a tratar como nota interna o que está entre parênteses. Só que o sistema não consegue separar isso, porque ainda há códigos e regras nas colunas que o cliente lê: L54 "(esta opção só aparece se Automação **não** estiver no ESC-01)"; L154 "(esta opção só aparece se o ESC-02 contém...)"; L159 e L84, regras em negrito fora de parênteses; L173 "Só aparecem cômodos que a PRG-01 ou o ESC-02 trouxeram"; L155 "CX (cômodos de PRG-01)". Na L169, os parênteses servem às duas coisas: "os parênteses são leitura do Tenreiro". Isso contradiz a D-1 (L383: "sem códigos e sem notas internas") |
| M4 | Resolvido | L3: "ESTADO EM 02/11/2026 — NÃO USAR COM CLIENTE REAL"; L8 lista PRV-01, Res. 2/2022, Art. 33 e NBR 15575-1:2025 |
| M5 | Resolvido | L223: "Sem Estrutural contratado [...] o Oscar orienta o cliente a contratar uma empresa de sondagem [...] O Oscar não dimensiona nada". L299 e L219 acompanham |
| M6 | Resolvido como controle | L129: nota interna "[A CONFERIR: números da NBR 15575-1:2024; confirmar na edição 2025...]". O cliente continua lendo os números, mas a L8 bloqueia o uso até a edição de 2025 ser lida |

**A grade da MOR-01 quebrou alguma condição?** Não. Conferi por Grep (`MOR-01|crian|idos|menor de 18|idade`):
- RES-01 (L77): as duas caixas usam a faixa.
- MOR-02 (L79): usa a lista com parentesco e faixa, e os menores só entram com a 1ª caixa.
- Regra da CON-01 (L104) e C-2 (L279): usam "60 anos ou mais", o mesmo corte do Estatuto do Idoso, Art. 1º.
- C-12 (L321): usa "0 a 11".
- D-2 (L397-398): coerente com as linhas acima.
- C-1 (L273): a MOR-01 continua obrigatória.

A faixa "0 a 11" na C-12 resolve o B4, porque "criança" ganhou definição. Ela coincide com o ECA, Art. 2º, que cito de memória e não conferi. A contrapartida é que o adolescente de 12 a 17 anos deixa de disparar a proteção de planta tóxica e de espinho. O Oscar marcou isso como pendente do de acordo do Glaziou.

**Números (Grep `^\| ~?~?[A-Z]{2,3}-\d\d`, `^\| TI-` e `^\*\*C-\d+\.`):**
- Códigos ativos: 6 + 10 + 10 + 1 + 5 + 8 + 12 + 6 + 5 = **63**. Os 5 retirados estão nas L118, L120, L134, L135 e L145.
- Pacotes: **45 / 56 / 62**, sem mudança de código.
- Tarefas internas: 14 + 6 + 2 + 2 = **24**.
- Regras: C-1 a C-17, com **17** títulos.

Tudo confere.

**Problemas novos (todos BAIXOS):**
- N1. Na L88, o texto da 1ª caixa da RES-01 ainda diz "(parentesco, idade e...)". A 2ª caixa (L89) já diz "faixa de idade".
- N2. A MOR-01 supõe que quem responde mora na casa: a 1ª linha é "eu, quem responde", e a coluna "mora na casa" só tem "sempre / às vezes". Se um filho contratar a casa para os pais, a 1ª linha fica errada, e a 2ª caixa da RES-01 conta mal.
- N3. A TI-PAI-01 (L244) diz "sondagem lida por Baumgart em TI-01". Sem Estrutural contratado, a nova TI-01 manda a leitura virar nota. As duas linhas não combinam.
- N4. No ramo sem Estrutural (L223), a regra da Barra, do Recreio e de Jacarepaguá ("os furos descem até a camada firme") não chega à empresa de sondagem, que segue só "pela norma".
- N5. O relatório do Oscar diz que manter os números do M6 foi "decisão de Claudemberg". A L129 diz "até Claudemberg decidir". Não dá para saber se a decisão existe.
- N6. A C-12 mudou de alcance (adolescente saiu) numa regra que tinha o de acordo do Glaziou. Está marcada como pendente, mas a mudança foi feita antes do de acordo.

**Conta da nota:** 10 − M3 (0,23) − resto do M2 (0,05) − B1, B2, B3, B5, B6 e B7 (0,30) − N1 a N6 (0,30) = **9,12**.

**O que corrigir:**

| Item | Dono | Tipo |
|---|---|---|
| Resto do M3: tirar das colunas do cliente toda regra e todo código, ou criar marcador próprio | Oscar | lacuna do Agente |
| N1 a N5 | Oscar | lacuna do Agente |
| N6 e "às vezes" | Lúcio, com o Glaziou via Cardozo | falha de processo |
| Origem da lista da AUT-02 | Lúcio e Landell | lacuna do Agente |

A fonte em todos os itens é o próprio Briefing.

**Fonte primária não verificada (acréscimo):** ECA (Lei 8.069/1990), Art. 2º; Estatuto do Idoso (Lei 10.741/2003), Art. 1º.
