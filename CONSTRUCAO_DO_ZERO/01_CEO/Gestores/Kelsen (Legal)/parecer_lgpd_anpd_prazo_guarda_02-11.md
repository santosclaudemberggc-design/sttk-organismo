# Parecer Kelsen — Encarregado (ANPD) e prazo de guarda do Briefing Único v2

**Data:** 02/11/2026 · **Frente:** Construção do Zero · **Pedido:** Wallenberg, para a sabatina de Claudemberg
**Alvo:** `Lúcio (Arquitetura)/Agentes/Oscar/briefing_modelo_v2_proposta.md`, PRV-01 (l. 59-70) e CON-01 (l. 94-105). Não editei o Briefing.
**Quem fez:** pesquisa do Hely (fontes primárias por curl e WebFetch). Eu conferi por conta própria a Res. 2/2022 no gov.br (arts. 3º, 4º e 11) e o Guia do Encarregado da ANPD, pp. 9-13 (lidas por imagem).
**Status:** análise preliminar. Passa pelo Gate da Coordenação (Claudemberg) antes de virar texto para cliente.

---

## Ponto 1 — A Sttickler pode deixar de nomear encarregado?

### Resposta curta
**Não com segurança.** Com a MOR-02 coletando saúde de crianças e idosos, a própria ANPD trata um caso parecido como **alto risco**. Alto risco tira a empresa pequena da dispensa. **Recomendo nomear um encarregado.**

### O que a norma diz (texto oficial)
Fonte: Res. CD/ANPD nº 2/2022. Texto original no DOU de 28/01/2022, Seção 1, p. 6 (https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-2-de-27-de-janeiro-de-2022-376562019). Texto consolidado no gov.br (https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022).

1. **Art. 11, caput:** "Os agentes de tratamento de pequeno porte não são obrigados a indicar o encarregado pelo tratamento de dados pessoais exigido no art. 41 da LGPD." É a dispensa.
2. **Art. 3º, I:** "Não poderão se beneficiar do tratamento jurídico diferenciado previsto neste Regulamento os agentes de tratamento de pequeno porte que: I - realizem tratamento de alto risco para os titulares, ressalvada a hipótese prevista no art. 8º". A única exceção é o art. 8º, que trata de mediação de reclamações. **Não há exceção para o art. 11.** Então, com alto risco, a dispensa cai.
3. **Art. 4º, caput:** é alto risco o tratamento que atende "cumulativamente a pelo menos um critério geral e um critério específico".
   - **Critérios gerais (I):** a) larga escala; b) tratamento que "possa afetar significativamente interesses e direitos fundamentais dos titulares".
   - **Critérios específicos (II):** a) tecnologias emergentes ou inovadoras; b) vigilância; c) decisão só automatizada; d) "utilização de dados pessoais sensíveis ou de dados pessoais de crianças, de adolescentes e de idosos".
   - **§ 2º:** o "afetar significativamente" inclui, "dentre outras situações", causar "danos materiais ou morais aos titulares, tais como discriminação".

### Aplicação à Sttickler
- **Critério específico: presente.** A MOR-02 trata saúde, que é dado sensível pelo art. 5º, II, da LGPD, e trata dados de crianças e idosos (art. 4º, II, d). A IA que lê as respostas pode contar também como "tecnologia emergente" (II, a). O Exemplo 7 do guia da ANPD trata IA assim, mas o guia não diz se "só organizar" conta. Esse ponto é **não confirmado**.
- **Critério geral "larga escala": provavelmente ausente**, porque são poucos clientes por ano. A norma não dá número, então nenhum limite está **confirmado**.
- **Critério geral "afetar significativamente": não dá para afastar.** O Guia Orientativo "Atuação do Encarregado" da ANPD (v1.0, dez/2024, pp. 11-12, https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_da_atuacao_do_encarregado_anpd.pdf) traz o **Exemplo 2**: empresa de pequeno porte, faturamento de R$ 2,5 milhões, que trata dados de saúde de idosos. A ANPD concluiu: "o tratamento realizado poderá afetar significativamente os interesses e direitos fundamentais dos titulares [...] Uma vez atendido um dos critérios gerais e um critério específico, tem-se a caracterização de um tratamento de alto risco [...] ainda que o controlador seja classificado como agente de tratamento de pequeno porte, deverá indicar um encarregado." **Eu li esse trecho no PDF, p. 12.** A ANPD chegou ao alto risco **sem larga escala**.
- **Conclusão:** a leitura "somos pequenos e poucos, então não é alto risco" vai contra o exemplo oficial. A dispensa é arriscada.

### Mudou alguma coisa depois?
- **Res. 2/2022:** a única alteração foi feita pela Res. CD/ANPD nº 15/2024, e só no art. 14, II (incidente de segurança). Os arts. 3º, 4º e 11 continuam iguais ao original. Fonte: lista oficial de regulamentações da ANPD (https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd), que marca a resolução como "Vigente com alterações pela Resolução CD/ANPD nº 15".
- **Res. CD/ANPD nº 18/2024 (encarregado):** DOU de 17/07/2024 (https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074). O art. 3º, § 3º só repete que o pequeno porte "dispensado" deve ter canal de comunicação, nos termos do art. 11 da Res. 2. **Não mudou a regra da dispensa.**
- **Não confirmado:** a ANPD não publicou guia próprio que diga o que é "larga escala" para empresa pequena.

### O que a Sttickler precisa fazer
**Caminho recomendado: nomear encarregado.**
1. Fazer um **ato formal escrito**, datado e assinado, que diga o que o encarregado faz (Res. 18/2024, art. 3º; guia, p. 13).
2. O encarregado pode ser o próprio Claudemberg ou alguém de fora (Res. 18/2024, art. 12, I: "pessoa natural, integrante do quadro organizacional do agente de tratamento ou externo a esse").
3. **Publicar o nome completo e o contato** do encarregado no site (Res. 18/2024, art. 9º, § 1º; guia, p. 13).
4. **Não precisa comunicar a ANPD.** O documento fica guardado para mostrar se ela pedir (guia, p. 13).
5. No PRV-01, o campo "e-mail de privacidade" vira o contato do encarregado, com o nome dele.

**Alternativa (decisão de Claudemberg):** tirar o dado de saúde do Briefing. A MOR-02 passaria a perguntar só a necessidade de projeto (por exemplo, "precisa de quarto no térreo, sem degrau?"), sem condição de saúde. Isso afasta o critério "dado sensível". O de crianças e idosos continua, porque a MOR-01 coleta a faixa de idade. Por isso, mesmo nesse caminho, nomear encarregado continua sendo o mais seguro. A Res. 2, art. 11, § 2º, conta a nomeação como boa prática.

**Vale em qualquer caminho:** canal de contato com o titular (LGPD art. 41, § 2º, I); consentimento específico e em destaque para dado sensível (LGPD art. 11, I), que a CON-01 já atende; consentimento de um dos pais para criança (LGPD art. 14, § 1º), que a RES-01 já atende; registro das operações (LGPD art. 37). Além disso, a ANPD pode pedir relatório de impacto (LGPD art. 38).

**Correção ao Briefing (proposta, não aplicada):** a l. 70 do Briefing diz "sem encarregado obrigatório [...] Res. CD/ANPD nº 2/2022, Art. 11". Pelo que foi conferido agora, isso deixa de valer enquanto a MOR-02 coletar saúde. Quem edita é o Oscar, por ordem de Claudemberg.

---

## Ponto 2 — Prazo de guarda

### Resposta curta
- **Dados gerais, "contrato + 5 anos": curto demais.** O prazo mais seguro é **10 anos contados do fim da obra** (ou da entrega do projeto, se a obra não acontecer). O pior caso pode passar disso. Ver a tabela.
- **Dados de saúde apagados ao fim do projeto, ficando só a decisão:** **tem base legal.** Recomendo guardar a decisão como **pedido do cliente**, sem diagnóstico.

### Os prazos que existem (texto oficial, Planalto)
| Norma | O que diz | Prazo e quando começa |
|---|---|---|
| CDC (Lei 8.078/1990), art. 27 (https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm) | "Prescreve em cinco anos a pretensão à reparação pelos danos causados por fato do produto ou do serviço [...] a partir do conhecimento do dano e de sua autoria." | 5 anos, contados **de quando o cliente descobre o dano**, não do fim do contrato |
| CDC, art. 26 | Reclamar de vício: 90 dias (serviço durável); vício oculto conta "no momento em que ficar evidenciado o defeito" (§ 3º) | curto, mas também começa tarde |
| Código Civil, art. 618 (https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm) | O empreiteiro responde "durante o prazo irredutível de cinco anos, pela solidez e segurança do trabalho"; o dono da obra tem "cento e oitenta dias seguintes ao aparecimento do vício" (p.ú.) | garantia de 5 anos **depois da obra** |
| Código Civil, art. 205 | "A prescrição ocorre em dez anos, quando a lei não lhe haja fixado prazo menor." | **10 anos**, prazo geral |
| Código Civil, art. 206, § 3º, V | "Em três anos: [...] a pretensão de reparação civil" | 3 anos (fora de contrato) |
| CAU, Lei 12.378/2010, art. 23 (https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12378.htm) | "Prescreve em 5 (cinco) anos a pretensão de punição das sanções disciplinares, a contar da data do fato." | 5 anos, só para processo ético |
| CAU, Res. 52/2013 (Código de Ética), item 4.3.6, e Res. 91/2014 (RRT) | dever de preservar a documentação de projetos, **sem prazo** | **não há prazo expresso** |

**STJ:** fontes secundárias (Migalhas, Machado Meyer) dizem que o STJ entende que os 5 anos do art. 618 são de garantia e que a ação de indenização prescreve em 10 anos (art. 205), contados da ciência do vício. Citam o REsp 1.717.160/DF. **Não confirmado:** o site do STJ bloqueou o acesso (erro 403).

### Por que 5 anos não basta
1. O prazo do CDC (5 anos) começa **quando o cliente descobre o dano**, que pode ser anos depois do fim do contrato.
2. Se o entendimento do STJ se confirmar, o dono da obra tem **10 anos** (art. 205), contados da ciência do vício. Um vício que aparece no 5º ano da garantia pode gerar ação até cerca de 15 anos depois da obra.
3. Sem os documentos, a Sttickler não consegue provar o que foi pedido e decidido.

### O que proponho (interpretação minha, vai ao Gate)
- **Dossiê do projeto** (contrato, Briefing sem saúde, decisões, aprovações, RRT, pranchas): guardar por **10 anos depois do fim da obra**. Se Claudemberg quiser cobrir o pior caso, o prazo vai para **15 anos**. Nenhuma lei fixa esse número. Ele sai da soma do art. 618 com o art. 205 do Código Civil.
- **Base para guardar:** LGPD art. 7º, VI e art. 11, II, d ("exercício regular de direitos, inclusive em contrato e em processo judicial"). Atenção: o art. 16 da LGPD não lista "exercício regular de direitos" entre as hipóteses de conservação. Usar os arts. 7º e 11 para isso é leitura minha, não texto expresso.
- **Dado de saúde:** apagar ao fim do projeto. A base é a LGPD:
  - art. 15, I: "a finalidade foi alcançada";
  - art. 16, caput: os dados "serão eliminados após o término de seu tratamento";
  - art. 6º, III: necessidade, "mínimo necessário".
  - Se o cliente retirar a autorização antes do fim, apagar na hora (art. 15, III, com o art. 8º, § 5º).
- **O que fica no lugar do dado de saúde:** a decisão escrita como **pedido do cliente, aceito por ele**. Exemplo: "cliente pediu suíte no térreo, sem degrau". Nada de diagnóstico ou doença. Esse registro protege a Sttickler se o projeto for questionado e não guarda dado sensível.

### Texto sugerido para o PRV-01, "Por quanto tempo" (não aplicado; quem decide é Claudemberg)
> Guardamos os dados do seu projeto por 10 anos depois do fim da obra, porque a lei nos dá responsabilidade sobre o projeto nesse período. A informação de saúde é apagada quando o projeto termina, ou antes, se você retirar a autorização. Fica guardado só o que você pediu para a casa (por exemplo, "suíte no térreo").

---

## Não confirmado
1. Acórdãos do STJ sobre o art. 618 e o art. 205 (site do STJ bloqueado; só fonte secundária).
2. Número que define "larga escala" para empresa pequena (não existe em norma nem em guia lido).
3. Se IA usada "só para organizar" conta como tecnologia emergente (art. 4º, II, a).
4. Vigência atual da Res. CAU/BR 91/2014 (a página não mostra revogação, mas a lista oficial de status do CAU não foi conferida).
5. Data da Res. CD/ANPD 15/2024: a página do gov.br diz "25 de abril" na nota e "24 de abril" no texto. Não muda nada aqui.

## Princípios
- P18 (ética e conformidade): recomendo o caminho mais seguro, que é nomear encarregado.
- P8 (rastreabilidade): todo trecho citado tem artigo e link.
