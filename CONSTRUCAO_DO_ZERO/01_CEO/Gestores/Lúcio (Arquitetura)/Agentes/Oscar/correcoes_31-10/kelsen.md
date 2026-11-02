# Correções do Kelsen para o Briefing Único v2 (31/10/2026)

Parte do Kelsen na revisão final: K2, ALTOS 6 a 12, D4 e D5, e os médios e baixos que achei relendo.
**Eu não editei o Briefing.** O Oscar junta tudo. Cada item traz: onde fica, o texto atual citado, o texto novo pronto para colar e o motivo com artigo e lei.
Lei citada como "LGPD" = Lei 13.709/2018. "COES" = LC 198/2019, cópia consolidada da SMU (`Agentes/Hely/Fontes_Legislacao/COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf`), que eu reli no PDF hoje nas pp. 3, 4, 9 e 17.
A pesquisa da edição das normas foi feita pelo Hely; a leitura da LGPD é minha, de memória do texto da lei, sem reabrir o Planalto nesta rodada. Onde não tenho certeza, escrevi "acredito que".

Decisões de Claudemberg que este arquivo segue: K1 (sai o Forms, entra uma sessão por cliente no futuro Sistema de Gestão), K2, D1 (a MED-01 sai), D4 e D5.

---

## 1. K2 + ALTO 6: aviso de privacidade na abertura (código novo PRV-01)

**Onde:** Seção 0, primeira linha, antes da ID-01.
**Texto atual:** não existe. A Seção 0 começa em "ID-01 | Confirme seu nome, telefone e e-mail."
**Texto novo (linha da tabela):**

| PRV-01 | Aviso de privacidade (leia antes de começar) | Texto, sem resposta, com uma caixa "Li o aviso" | sempre | todos | R |

**Texto que o cliente lê:**

> **Como cuidamos dos seus dados**
> **Quem cuida:** Sttickler Empreendimentos [PENDENTE: razão social e CNPJ], responsável pelos dados que você informar aqui.
> **Para que usamos:** só para fazer o projeto da sua casa que você contratou, cumprir o contrato e as obrigações legais e profissionais ligadas a ele (por exemplo, a aprovação na prefeitura e a responsabilidade técnica).
> **Que dados:** o que você responder aqui: contato, endereço do terreno, quem vai morar, rotina, gostos, fotos e referências. Dado de saúde só com uma autorização separada, mais adiante, e você pode não informar.
> **Com quem compartilhamos:** só com a equipe que trabalha no seu projeto, incluindo os profissionais parceiros contratados para ele (como o arquiteto responsável e os projetistas), e com a prefeitura quando a lei exigir. Não vendemos seus dados e não os usamos para propaganda. Usamos ferramentas de computador, inclusive inteligência artificial, para organizar e analisar as respostas, sempre para o seu projeto.
> **Onde ficam:** na área do seu projeto, que só você e a equipe acessam. Nenhum outro cliente vê.
> **Por quanto tempo:** [PENDENTE: definir com Claudemberg].
> **Seus direitos:** saber quais dados temos, corrigir, pedir para apagar o que não formos obrigados a guardar, retirar uma autorização que você deu e tirar dúvidas. Fale com a gente pelo [PENDENTE: definir com Claudemberg (e-mail de privacidade)]. Respondemos em até 15 dias.

**Motivo:**
- LGPD Art. 9º: o titular tem direito a informação clara sobre finalidade, forma e duração do tratamento, quem é o controlador e seu contato, uso compartilhado e seus direitos.
- LGPD Art. 18 (direitos do titular) e Art. 19, II (resposta completa em até 15 dias).
- D5 (Claudemberg, 31/10): porte microempresa ou EPP, sem encarregado obrigatório, mas com canal de contato. Base: Resolução CD/ANPD nº 2/2022, Art. 11 (o agente de pequeno porte não precisa indicar encarregado, mas precisa dar um canal de comunicação ao titular).
- Ressalva: acredito que a mesma Resolução não dá a dispensa a quem faz tratamento "de alto risco", e dado de saúde e de criança entram nos critérios específicos de alto risco. Acredito que o escritório não chega ao critério geral (larga escala), e então a dispensa vale, mas isso precisa ser conferido no texto da Resolução antes do primeiro cliente real. Também acredito que a Resolução dá prazo em dobro ao pequeno porte para responder ao titular; prometer 15 dias é mais exigente do que a lei pede, e a escolha é de Claudemberg.
- Nada de razão social, e-mail ou prazo de guarda foi inventado: ficam como PENDENTE.

---

## 2. K2: consentimento destacado antes da MOR-02 (código novo CON-01)

**Onde:** Seção 1, entre a MOR-01 e a MOR-02.
**Texto atual:** não existe. A MOR-02 vem direto: "MOR-02 (B2) | Alguém tem hoje: | CX: dificuldade para andar ou subir escada / recomendação médica para evitar esforço · alergia (poeira, mofo etc.) · outra necessidade especial · ninguém. Se marcar: quem (sem diagnóstico) | sempre | Oscar, Tenreiro | R"
**Texto novo (linha da tabela):**

| CON-01 | Autorização para usar informação de saúde (bloco separado, opcional) | Caixa única, que **vem desmarcada** | sempre | todos (registro) | R |

**Texto que o cliente lê:**

> **Antes da próxima pergunta**
> A próxima pergunta é sobre saúde e mobilidade de quem vai morar na casa. A lei chama isso de dado sensível, e só podemos usar com a sua autorização.
> **Para que serve:** só para adaptar o projeto. Por exemplo: um quarto no térreo, uma casa sem degraus, passagens mais largas, plantas com pouco pólen perto dos quartos.
> **Quem vê:** só a equipe que projeta a sua casa.
> **Não pedimos diagnóstico.**
> Você pode não autorizar, ou responder "prefiro não informar". O projeto continua do mesmo jeito; só não vamos adaptar a casa a uma necessidade que não conhecemos.
> Você pode retirar a autorização quando quiser, pelo [PENDENTE: definir com Claudemberg (e-mail de privacidade)].
> ☐ Autorizo o uso destas informações de saúde só para o projeto desta casa.

**Regra (vai para a coluna Condição da MOR-02 e para a C-1):** se a caixa da CON-01 ficar desmarcada, a MOR-02 não aparece e fica registrada como "não informado". "Não informado" conta como resposta para a C-1 e não dispara a C5 pela MOR-02 (a C5 ainda dispara por idoso na MOR-01).

**Motivo:**
- LGPD Art. 5º, II: dado referente à saúde é dado pessoal sensível.
- LGPD Art. 11, I: dado sensível só com consentimento "de forma específica e destacada, para finalidades específicas". Nenhuma das hipóteses sem consentimento do Art. 11, II serve para projeto de arquitetura.
- LGPD Art. 8º, §5º: o consentimento pode ser revogado a qualquer momento.
- Caixa desmarcada: consentimento é "manifestação livre, informada e inequívoca" (Art. 5º, XII); caixa que vem marcada não prova isso.
- LGPD Art. 6º, III (necessidade): só o mínimo; por isso "sem diagnóstico".

---

## 3. K2: MOR-02 com "prefiro não informar"

**Onde:** linha da MOR-02, Seção 1.
**Texto atual:** "CX: dificuldade para andar ou subir escada / recomendação médica para evitar esforço · alergia (poeira, mofo etc.) · outra necessidade especial · ninguém. Se marcar: quem (sem diagnóstico) | sempre | Oscar, Tenreiro | R"
**Texto novo:**

| MOR-02 (B2) | Alguém que vai morar na casa tem hoje: | CX: dificuldade para andar ou subir escada / recomendação médica para evitar esforço · alergia (poeira, mofo etc.) · outra necessidade especial · ninguém · prefiro não informar. Se marcar: quem (só o parentesco da MOR-01, sem nome e sem diagnóstico). "Prefiro não informar" não pode ser marcada junto com outra opção | só se a CON-01 estiver marcada; sem ela, registra "não informado" | Oscar, Tenreiro, Glaziou | R |

**Motivo:**
- O pedido de K2 (Claudemberg, 31/10) inclui "prefiro não informar".
- "Quem" pelo parentesco e não pelo nome: LGPD Art. 6º, III (necessidade). A casa muda pelo que a pessoa precisa, não pelo nome.
- "Usado por" ganha o Glaziou, porque a C-12 usa a alergia (achado médio da revisão). Pela LGPD Art. 6º, I (finalidade), quem usa o dado sensível tem de estar coberto pelo que foi dito ao cliente; o texto da CON-01 diz "a equipe que projeta a sua casa", o que cobre o Glaziou.

---

## 4. ALTO 7: declaração sobre crianças e outros adultos (código novo RES-01)

**Onde:** Seção 1, logo depois da MOR-01 e antes da CON-01.
**Texto atual:** não existe.
**Texto novo (linha da tabela):**

| RES-01 | Sobre os dados das outras pessoas da casa | Duas caixas, que vêm desmarcadas; cada uma só aparece se a MOR-01 tiver aquele caso | aparece se a MOR-01 tiver alguém com menos de 18 anos ou outro adulto além de quem responde | Oscar (registro) | R |

**Texto que o cliente lê:**

> ☐ (se houver menor de 18 anos) Sou pai, mãe ou responsável legal das crianças e adolescentes que listei. Autorizo o uso dos dados deles (parentesco, idade e, se eu informar mais adiante, saúde) só para o projeto desta casa.
> ☐ (se houver outro adulto) Os outros adultos que listei sabem que informei o parentesco e a idade deles para o projeto. Informação de saúde de outro adulto só entra na pergunta seguinte se ele mesmo concordar.

**Regra:** sem a primeira caixa marcada, a MOR-02 não pode ser respondida sobre a criança.

**Motivo:**
- LGPD Art. 14, caput: o tratamento de dados de crianças e adolescentes deve ser feito no seu melhor interesse.
- LGPD Art. 14, §1º: o dado de criança precisa de consentimento específico e em destaque de pelo menos um dos pais ou do responsável legal. Acredito que a ANPD, no Enunciado CD/ANPD nº 1/2023, admitiu outras bases legais para dados de criança, além do consentimento. Mesmo assim, o dado de saúde da criança continua exigindo consentimento pelo Art. 11, I. Por isso a caixa fica.
- Outro adulto: idade e parentesco podem ser tratados para executar o contrato (Art. 7º, V). Já o dado de saúde é do próprio adulto, e o consentimento do Art. 11, I tem de ser dele. Quem responde não pode consentir por outro adulto. **Risco que fica:** a frase "se ele mesmo concordar" depende da palavra de quem responde. O jeito mais seguro é o próprio adulto marcar uma caixa na sessão dele. Isso é recomendação para quando existir o Sistema de Gestão; a escolha é de Claudemberg.

---

## 5. ALTO 8 + K2: transferência internacional vira só nota interna

**Onde:** Parte C, regra nova C-13 (nunca aparece ao cliente).
**Texto atual:** não existe.
**Texto novo:**

> **C-13. Transferência de dados para fora do Brasil (nota interna, não aparece ao cliente).** O Briefing não vai mais para o Google Forms. Ele vai para uma sessão por cliente no futuro Sistema de Gestão, com hospedagem ainda não definida. **Se o sistema for hospedado fora do Brasil, incluir aviso** no PRV-01 e, para o dado de saúde, pedir a autorização na própria CON-01. Base: LGPD Art. 33. Antes de ligar o sistema, conferir também onde roda a inteligência artificial que lê as respostas (ver observação).

**Motivo:**
- Decisão de Claudemberg (31/10, K1 e K2): o aviso do Art. 33 só volta se o Sistema de Gestão ficar hospedado fora do Brasil.
- LGPD Art. 33: a transferência internacional só pode ocorrer nos casos ali listados; para dado comum, o inciso IX remete ao Art. 7º, V (execução do contrato); para dado sensível, o caminho seguro é o consentimento específico e em destaque (inciso VIII).
- **Observação (recomendação, não decisão):** acredito que o Art. 33 também se aplica se a inteligência artificial que lê as respostas processar os dados fora do Brasil, mesmo com o sistema hospedado aqui. Os agentes do organismo usam IA, e eu não sei onde ela processa. Sinalizo para Claudemberg decidir; não mudei a decisão dele. Acredito também que a ANPD regulou a transferência na Resolução CD/ANPD nº 19/2024 (cláusulas-padrão); não conferi o texto.

---

## 6. ALTO 9 + D4: DEC-01 completa

**Onde:** linha da DEC-01, Seção 7.
**Texto atual:** "DEC-01 | Declaro que as informações estão corretas e de acordo com o que desejo. | caixa + nome + data (uma vez só, no fim) | sempre | Oscar (Gate do cliente) | C"
**Texto novo:**

| DEC-01 | Declaração final (uma para cada pessoa que assinou o contrato) | Quatro caixas, que vêm desmarcadas, + nome completo; data, hora e versão das respostas preenchidas pelo sistema | sempre; o Briefing só vale com a DEC-01 de todos os contratantes | Oscar (Gate do cliente) | C |

**Texto que o cliente lê (repetido para cada contratante):**

> ☐ Li minhas respostas. Elas estão corretas e de acordo com o que desejo.
> ☐ Sei que, nas perguntas não obrigatórias que deixei em branco, a equipe vai usar a resposta padrão do escritório, e que isso fica escrito no Estudo Preliminar.
> ☐ Sei que os projetos marcados no início deste Briefing servem só para abrir as perguntas certas. O que foi contratado é o que está no contrato assinado; este Briefing não muda o contrato.
> ☐ Sei que projetamos no mínimo nas referências da lei e das normas e, salvo pedido meu por escrito, acima delas. Se eu pedir algo abaixo de uma referência que não é obrigatória, isso só vale por escrito, depois de a equipe me explicar o que muda. Abaixo do mínimo obrigatório da lei e das normas, a equipe não projeta, mesmo a meu pedido.
> Nome completo: ______ · Data e hora: (automático) · Versão das respostas: (automático: código do projeto + número da versão)

**Regras (vão para a C-3):** cada contratante tem a sua DEC-01. Se o cliente mudar uma resposta depois de assinar, a versão sobe e a DEC-01 é assinada de novo.

**Motivo:**
- ALTO 9 da revisão: faltavam a ciência das respostas padrão, o aviso de que o ESC-01 não muda o contrato, o registro do "aceito o mínimo", versão e data, e um campo por contratante.
- CDC (Lei 8.078/1990) Art. 6º, III: direito à informação clara. Art. 46: o consumidor não se obriga ao que não teve chance de conhecer antes. Por isso a ciência das respostas padrão e do contrato.
- **"Aceito o mínimo":** com a MED-01 retirada (D1), a opção "aceito o mínimo" sumiu do Briefing. O que sobra é a regra: abaixo de referência não obrigatória, só por escrito. Abaixo do mínimo obrigatório, nunca: CDC Art. 39, VIII proíbe colocar no mercado serviço em desacordo com as normas técnicas, e o COES Art. 1º, §3º, III manda seguir as normas técnicas (como já está no meu parecer de 31/10). O cliente não pode dispensar isso.
- D4 (Claudemberg, 31/10): frase "no mínimo nessas referências e, salvo pedido seu por escrito, acima delas".
- Versão e data: LGPD Art. 8º, §2º (cabe ao controlador provar que o consentimento foi obtido) e rastreabilidade (Princípio 8).

---

## 7. D4 + pé-direito e salubre explicados: frase ao cliente na C-7

**Onde:** Parte C, C-7, a frase entre aspas. Como a MED-01 saiu (D1), a frase não tem mais pergunta própria. Sugiro ao Oscar mostrá-la como texto informativo no começo da Seção 3, junto da NIV-01. A decisão do lugar é dele.
**Texto atual:** "Para casa, a lei do Rio (Código de Obras, Art. 31) não exige área mínima nem tamanho mínimo de cômodo, corredor ou janela, desde que a casa seja salubre. Os quartos e salas continuam precisando de ventilação e luz natural direta. A norma de desempenho NBR 15575, que somos obrigados a seguir, exige pé-direito mínimo de 2,50 m (2,30 m em banheiros, corredores e despensas) e sugere, num anexo, os espaços para o mobiliário de cada cômodo. Nós projetamos acima dessas referências."
**Texto novo:**

> "Para casa, a lei do Rio (Código de Obras, Art. 31) não exige área mínima nem tamanho mínimo de cômodo, corredor ou janela, desde que a casa seja salubre, isto é, saudável e higiênica para morar. Os quartos e as salas continuam precisando de ventilação e luz natural vindas direto de fora. A norma de desempenho NBR 15575, que somos obrigados a seguir, exige pé-direito (a altura do piso até o teto) de no mínimo 2,50 m, ou 2,30 m em banheiros, corredores e despensas, e sugere, num anexo, os espaços para os móveis de cada cômodo. Nós projetamos no mínimo nessas referências e, salvo pedido seu por escrito, acima delas."

**Motivo:**
- D4 (Claudemberg, 31/10): troca do fim da frase.
- Revisão final, médio/baixo: "pé-direito" e "salubre" precisam ser explicados ao cliente. CDC Art. 6º, III (informação clara).
- "Salubre": COES Art. 31, caput (p. 17), "desde que mantidas as condições de salubridade e higiene da habitação".
- "Ventilação e luz natural vindas direto de fora" (era "direta"): COES Art. 17, §3º (p. 9), os compartimentos de permanência prolongada têm ventilação e iluminação natural, "que não poderão ser feitas através de outro compartimento". Só o §3º; o §4º é dos compartimentos de permanência transitória.
- 2,50 m e 2,30 m: NBR 15575-1, item 16.1.1, na edição de 2024 do acervo. Ver o item 9 sobre a edição.

**Ajuste junto, na mesma C-7:** trocar "Saúde: só o que muda a casa, sem diagnóstico; dado sensível, uso só no projeto." por "Saúde: só o que muda a casa, sem diagnóstico, e só com a autorização da CON-01 (LGPD Art. 11, I); dado sensível, uso só no projeto."

---

## 8. ALTO 12: tarefa interna para APP, faixa marginal, área alagadiça e terreno de marinha (código novo TI-14)

**Onde:** Parte B, depois da TI-13.
**Texto atual:** não existe. Hoje a lei só chega ao Kelsen pela TI-05 ("lei via Lúcio → Kelsen") e pela TI-PAI-05 (permeabilidade, só com Paisagismo).
**Texto novo (linha da tabela):**

| TI-14 | Restrições ambientais e de domínio do terreno: APP (margem de rio, canal, lagoa, mangue, restinga), faixa marginal de proteção (FMP, INEA), área alagadiça ou brejo, terreno de marinha ou acrescido (SPU), unidade de conservação ou APA, árvores protegidas. Diz se há faixa onde não se pode construir e qual licenciamento ambiental municipal vale: o simplificado (LMS) ou o ordinário (LMP + LMI) | revisão final 31/10 (ALTO 12) | Kelsen (pesquisa pelo Hely), acionado via Lúcio. Entradas do Oscar: ID-02, matrícula e certidões (TI-07), campo e árvores (TI-08), topografia e sondagem (TI-01); com Paisagismo, lençol e alagamento (TI-PAI-03) | Levantamento, antes do EP |

**Ajustes junto:**
- C-3, onde diz "TI-01, TI-05, TI-09 anexadas": trocar por "TI-01, TI-05, TI-09 e TI-14 anexadas".
- C-2, linha nova:

| TI-14 com APP, FMP, área alagadiça ou marinha | faixa não edificável marcada no partido antes do EP; licenciamento ambiental pelo rito ordinário | obrigatória |

**Motivo:**
- Lei 12.651/2012 (Código Florestal), Art. 4º: APP em faixas marginais de cursos d'água, entorno de lagoas, manguezais e restingas, também em zona urbana.
- Decreto-Lei 9.760/1946, Arts. 2º e 3º: terrenos de marinha e acrescidos, da União (SPU).
- Decreto Rio 51.503/2022, Art. 27, parágrafo único (incisos II e IV): terreno com APP ou área alagadiça sai do licenciamento simplificado (LMS) e cai no rito ordinário (LMP + LMI). Isso muda prazo e custo da obra.
- Na Barra, no Recreio e em Vargem Grande (AP4), lagoa, canal e brejo são comuns. Sem a TI-14, o EP pode desenhar onde não se pode construir.

---

## 9. ALTO 10: edição da NBR 15575-1

**Resultado da conferência (Hely, 31/10/2026; eu não abri as páginas):** **confirmado só em fonte secundária. A edição vigente é a NBR 15575-1:2025 (12/2025)**, que incorpora a Emenda 1 de 12/2025 e substitui a de 2024.
- Target (revendedor das normas ABNT), https://www.target.com.br/produtos/normas-tecnicas/40674/nbr15575-1-edificacoes-habitacionais-desempenho-parte-1-requisitos-gerais, acesso 31/10/2026: "NBR15575-1 DE 12/2025", status "Vigente"; histórico "12/2025 Publicada nova edição (inc.em.)", "12/2025 Publicada Emenda".
- standards.ie, https://shop.standards.ie/en-ie/standards/abnt-nbr-15575-1-2025-773110_saig_nbr_nbr_3780480: "ABNT NBR 15575-1:2025", "Supersedes: ABNT NBR 15575-1:2024".
- **Não conferido no catálogo da ABNT:** a busca do abntcatalogo.com.br não devolveu resultado sem navegador.
- **O que não sabemos:** se a emenda de 2025 mexeu no item 16.1.1 (pé-direito), no 16.2 ou no Anexo F. O acervo só tem a edição de 2024.

**Onde muda no Briefing:**
- C-7, onde diz "A régua técnica é a NBR 15575-1:2024 Anexo F (informativo, ...)": trocar "NBR 15575-1:2024" por "NBR 15575-1 (texto lido na edição de 2024 do acervo; a edição vigente é a de 2025, segundo fonte secundária ainda não conferida na ABNT)".
- Cabeçalho, linha 3, onde diz "NBR 15575-1 item 16.2 mantém o Anexo F informativo": acrescentar "(na edição de 2024; a de 2025 não foi lida)".
- A frase ao cliente (item 7) não cita ano e pode ficar, mas os números 2,50 m e 2,30 m só ficam firmes depois de alguém ler a edição de 2025.

**Motivo:** Princípio 8 (rastreabilidade) e regra da casa de sempre usar a legislação mais atual. **Recomendação a Wallenberg:** obter a NBR 15575-1:2025 para o acervo e conferir os três trechos antes do primeiro cliente real. As Skills `layout-mobiliario-dimensoes-residencial` (L21) e `coe-lc198-...` (§1) também citam a edição de 2024; não as alterei nesse ponto.

---

## 10. NBR 9575: a edição é de 2010, confirmada em 2024

**Onde:** Parte B, TI-PAI-06.
**Texto atual:** "a impermeabilização com anti-raiz segue a NBR 9575:2024"
**Texto novo:** "a impermeabilização com anti-raiz segue a NBR 9575:2010 (edição vigente, confirmada pela ABNT em 07/2024)"
**Motivo:** conferência do Hely (31/10/2026), fonte secundária: Target, https://www.target.com.br/produtos/normas-tecnicas/36659/nbr9575-impermeabilizacao-selecao-e-projeto, "NBR 9575 DE 09/2010", "Vigente", histórico "07/2024 Publicada confirmação". Não existe edição de 2024; houve confirmação. Não conferido no catálogo da ABNT. **Sinalização:** a Skill `nbr9575-impermeabilizacao` também se chama "NBR 9575:2024". Ela não é minha; o dono corrige.

---

## 11. Médio: idade de "idoso"

**Onde:** C-2, primeira linha.
**Texto atual:** "MOR-01 com idoso ou MOR-02 com dificuldade para andar"
**Texto novo:** "MOR-01 com pessoa de 60 anos ou mais (idosa, pela Lei 10.741/2003, Art. 1º) ou MOR-02 com dificuldade para andar"
**Motivo:** a revisão final apontou que "idoso" estava sem idade. A Lei 10.741/2003 (Estatuto da Pessoa Idosa), Art. 1º, define pessoa idosa como a de idade igual ou superior a 60 anos. Usar a definição da lei evita que cada agente escolha uma idade.

---

## 12. Médio: C-1 com os códigos novos e com a MED-01 retirada

**Onde:** C-1.
**Texto atual (trecho):** "ID-01, ID-02, ESC-01, ESC-02, OBJ-01, MOR-01, MOR-02, MOR-03, ... NIV-01, MED-01, PRZ-02, DEC-01"
**Texto novo (só a minha parte):** incluir PRV-01 (caixa "Li o aviso") na lista de obrigatórias. MOR-02 continua obrigatória, mas "não informado" (CON-01 desmarcada) e "prefiro não informar" contam como resposta. CON-01 e RES-01 **não** são obrigatórias: a autorização não pode ser exigida para o projeto andar. A retirada da MED-01 (D1) é do Oscar.
**Motivo:** LGPD Art. 8º e Art. 5º, XII: consentimento tem de ser livre. Se a autorização de saúde fosse condição para o Briefing seguir, ela deixaria de ser livre. Acredito que o Art. 9º, §3º vai na mesma linha: quando o consentimento é condição para um serviço, o titular tem de ser avisado com destaque.

---

## 13. Baixo: fotos da EST-02

**Onde:** EST-02, coluna Tipo / opções.
**Texto atual:** "UP/TXT: até 10 fotos ou links de casas, cômodos, materiais e cores (Pinterest, Instagram)"
**Texto novo:** acrescentar no fim: "Prefira fotos sem pessoas."
**Motivo:** LGPD Art. 6º, III (necessidade). Rosto é dado pessoal, e o projeto não precisa dele.

---

## 14. Para o Oscar recontar

Entram 4 códigos novos: PRV-01, CON-01 e RES-01 (cliente) e TI-14 (interna), mais a regra C-13. Mudam os números da tabela "Números" (códigos ativos, perguntas por pacote, tarefas internas) e o tempo da reunião. Estimativa minha, não medida: PRV-01 1 min, CON-01 0,5 min, RES-01 0,5 min.

---

## O que eu editei fora do Briefing (arquivos meus)

- Parecer `Kelsen (Legal)/parecer_coes_art31_lc270_31-10.md`: Art. 17 citado como §3º (era §§3º e 4º), nas duas ocorrências; a linha "Fica aberta só a ressalva 3" virou "as quatro ressalvas estão fechadas"; entrou a seção "Correções de 31/10", com o aviso da edição 2025 da NBR 15575-1.
- Skill `coe-lc198-2019-ventilacao-iluminacao-pe-direito-residencial-rj` v1.3 → v1.4, nas duas cópias (`.claude` e `.agents`), iguais: prisma da casa = 1,50 m, sem H/4 (COES Art. 31, parágrafo único, p. 17, lido no PDF); 3,00 m fica para as demais edificações (Art. 5º, §1º, I, p. 4); PV da casa em 1,50 m marcado como interpretação para o Gate; citação do Art. 17 corrigida para §3º; registro de erro novo.
