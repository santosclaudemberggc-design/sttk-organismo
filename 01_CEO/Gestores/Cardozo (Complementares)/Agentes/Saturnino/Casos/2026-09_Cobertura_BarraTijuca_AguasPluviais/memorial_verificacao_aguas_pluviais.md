# Memorial de Verificação — Cobertura Barra da Tijuca/RJ, Águas Pluviais NBR 10844 (Exame 2, Caso 3 complementar)

**Agente:** Saturnino (Hidrossanitário). **Caso-teste:** Exame 2 (Shadow → Assisted), Caso 3 complementar retroativo — `Casos_TESTE/Exame2_Saturnino_Caso3_TESTE/caso.md`.

Revisão item a item da proposta técnica preliminar de projetista terceirizado. Cobertura de laje plana de 180 m² + trecho de telhado metálico de 30 m² sobre pergolado (mesma calha), Barra da Tijuca/RJ, região de alta intensidade pluviométrica.

**Ressalva de fonte (herdada da Skill `nbr10844-1989-aguas-pluviais`):** o texto integral da ABNT NBR 10844:1989 não foi lido por mim (norma paga); apoio-me em fonte secundária (GreenGold Engenharia, 07/2026) já com ressalva registrada. Os valores numéricos de IDF (intensidade pluviométrica) para o Rio de Janeiro não foram obtidos por mim em nenhuma fonte — trato como pendência estrutural do organismo, não como dado que eu possa presumir.

---

### Item 1 — Intensidade pluviométrica fixa de 60 mm/h, "independente da localização e do tempo de retorno"
**NÃO CONFORME.** NBR 10844:1989 exige que a intensidade pluviométrica de cálculo (I) seja obtida da curva IDF (intensidade-duração-frequência) **do local do terreno**, combinada com um tempo de retorno (T) definido conforme a natureza e criticidade da área drenada — não um valor fixo replicado entre projetos. Usar "60 mm/h, valor padrão... independente da localização e do tempo de retorno" é exatamente a armadilha documentada na minha Skill (`nbr10844-1989-aguas-pluviais`, seção "Armadilhas Frequentes #2 — Intensidade pluviométrica 'média' sem conferir IDF local"). Fonte: Skill, seção "Sequência de Projeto" item 1, e "Fórmula Principal" (Q = I×A/60, onde I é explicitamente "obter da equação IDF Rio-Águas para a zona do terreno").

**PENDÊNCIA BLOQUEANTE anexa:** não tenho o valor real de I para Barra da Tijuca/RJ — nem eu, nem a Skill, temos essa curva IDF conferida em fonte primária. **A cobrar:** (a) da Rio-Águas/Prefeitura do Rio (equação IDF oficial do município, por zona) ou do INMET (série pluviométrica), o valor de I correto; (b) de Cardozo/cliente, confirmação do tempo de retorno T a adotar — padrão STTK é T=5 anos para coberturas/terraços residenciais, mas o próprio caso descreve "região de alta intensidade pluviométrica", o que pode justificar T=25 anos (áreas onde transbordo é crítico) — não presumo qual dos dois se aplica sem essa definição. Enquanto I e T não forem confirmados, nenhum dimensionamento a jusante (calha, condutor, item 5) pode ser considerado fechado — inclusive o "100 mm necessário" citado no item 5 está sob suspeita, pois foi calculado com o I genérico ora reprovado.

### Item 2 — Área de contribuição do condutor vertical excluindo os 30 m² de telhado metálico
**NÃO CONFORME.** A área de contribuição de um trecho de drenagem é definida pela conexão **hidráulica**, não pela separação **estrutural**. Como o próprio parceiro descreve, o trecho de telha metálica "deságua na mesma calha" da laje — logo, toda a vazão desse telhado converge para o(s) mesmo(s) condutor(es) vertical(is) alimentado(s) por aquela calha, e deve entrar no somatório de área. O cálculo mínimo correto é 180 + 30 = 210 m², mais eventual parcela de parede exposta que contribua para aquele trecho (dado ainda não informado — ver pendência abaixo). Excluir área por "ser pequena e separada estruturalmente" é a armadilha documentada na Skill ("Armadilhas Frequentes #1 — Área de contribuição subestimada — não incluir parcela de parede exposta"; o mesmo princípio se aplica a área de telhado hidraulicamente conectada). Fonte: Skill, "Sequência de Projeto" item 2.

**PENDÊNCIA complementar:** não há informação sobre existência de parede/platibanda exposta na cobertura que receba respingo/vento-chuva e deva somar à área de contribuição. **A cobrar:** do projetista terceirizado ou de Oscar, planta de fachada/corte da cobertura mostrando se há parede vertical exposta acima do plano da laje.

### Item 3 — Dispensa da caixa de areia por "não haver jardim ou área com terra"
**NÃO CONFORME.** A caixa de areia antes do lançamento não existe apenas para reter sedimento de jardim/terra — sua função é reter qualquer material sólido que possa obstruir a tubulação fechada a jusante (folhas, poeira atmosférica, detritos de manutenção, partículas de desgaste da manta de impermeabilização, areia carregada pelo vento). Uma laje plana impermeabilizada não está isenta desse tipo de detrito. A Skill lista isso como obrigação, não opção: "Armadilhas Frequentes #5 — Ausência de caixa de areia — obrigatória antes do lançamento" e "Sequência de Projeto" item 7 ("Especificar caixas de areia (obrigatórias antes do lançamento)"). A justificativa apresentada pelo parceiro confunde "ausência de solo exposto" com "ausência de sedimento", que são coisas diferentes.

### Item 4 — Condutor pluvial conectado à mesma prumada de esgoto sanitário
**NÃO CONFORME — grave, bloqueante.** O Rio de Janeiro opera sistema separador absoluto: águas pluviais e esgoto sanitário devem correr em redes fisicamente independentes, do predial até o logradouro. Interligar as duas é proibido tanto pela NBR 8160:1999 (rede coletora de esgoto sanitário não recebe água pluvial) quanto pela NBR 10844:1989 e pela legislação municipal de saneamento (Rio-Águas/CEDAE). O risco prático não é só normativo: em chuva de pico, a vazão pluvial pode sobrecarregar a prumada de esgoto e causar refluxo de esgoto pela própria calha/ralo pluvial — risco sanitário direto para os usuários. "Simplificar a execução" reduzindo o número de tubulações não é justificativa válida para essa interligação. Fonte: Skill `nbr10844-1989-aguas-pluviais`, seção "Regra Fundamental — Sistema Separador Absoluto" e "Armadilhas Frequentes #4 — Lançamento em rede de esgoto — proibido, infração grave"; aprendizado já registrado no meu estado desde o Caso E2 do Exame 2 ("Interligar = proibido por NBR 8160/10844").

**PENDÊNCIA anexa:** corrigido o erro, falta definir o destino correto do lançamento (rede pública de águas pluviais, infiltração no lote, jardim de chuva ou corpo receptor). **A cobrar:** de Kelsen/Hely, confirmação se o logradouro na Barra da Tijuca tem rede pluvial separativa disponível (a Skill exige essa verificação antes de fechar o projeto — bairros mais antigos do Rio podem ter rede unitária, o que muda a solução).

### Item 5 — Diâmetro do condutor vertical reduzido de 100 mm (calculado) para 75 mm ("diferença pequena")
**NÃO CONFORME.** A capacidade de escoamento de um condutor vertical não varia linearmente com o diâmetro — varia com uma potência maior que 2 do diâmetro nominal (relação típica de escoamento por gravidade em tubo circular parcialmente cheio). Reduzir de 100 mm para 75 mm não é "uma diferença pequena": pode cortar a capacidade de vazão do trecho em proporção muito superior à redução linear de diâmetro (25 mm), aumentando risco real de transbordamento da calha na chuva de projeto. O diâmetro especificado deve ser igual ou maior que o resultante do cálculo pela NBR 10844 — nunca menor por conveniência de espaço no shaft. Se o shaft é insuficiente para 100 mm, a solução tecnicamente correta é revisar o layout do shaft com Oscar/Baumgart ou redistribuir a vazão entre mais de um condutor — não subdimensionar o tubo. Fonte: Skill, "Sequência de Projeto" item 5 (DN mínimo por cálculo) e "Armadilhas Frequentes #6 — Condutor vertical único para área grande — distribuir conforme cálculo", mesmo princípio de não comprometer capacidade por conveniência de leiaute.

**Observação que já registro como pendência, não para repetir prova:** mesmo o valor de referência "100 mm calculado" citado pelo parceiro precisa ser recalculado depois que os itens 1 (I) e 2 (área de 210 m² mínimo) forem corrigidos — o número real necessário pode ser maior que 100 mm.

### Item 6 — Posição da calha com boca coletora (degrau) exatamente na transição laje/telhado metálico
**CONFORME.** Posicionar o ponto de coleta exatamente na transição entre dois materiais/planos de cobertura é prática tecnicamente correta e é a solução recomendada para evitar exatamente o problema mais comum em transições de cobertura: acúmulo/empoçamento no ponto de mudança de nível ou material. Isso é coerente com o princípio geral da NBR 10844 de que calhas devem ser posicionadas e dimensionadas para não permitir acúmulo (ver Skill, "Armadilhas Frequentes #3 — Calha sem declividade — empoça mesmo sem chuva intensa", que é o problema exatamente evitado por esse posicionamento). Não há dado faltante que me impeça de validar este item especificamente.

Ressalvo que a validação **completa** desse trecho de calha ainda depende da declividade mínima (0,5%) ser mantida ao longo de todo o percurso — isso é tratado no item 7, não aqui — e que a vedação/junta de dilatação na própria transição de materiais é uma questão de execução/impermeabilização (cross com Baumgart/projeto de cobertura), fora do escopo de dimensionamento hidráulico que eu valido.

### Item 7 — "Calha ao longo do perímetro da cobertura", sem outros dados
**PENDÊNCIA BLOQUEANTE — dado insuficiente para julgar.** A frase "terá calha ao longo do perímetro" não permite verificar conformidade nenhuma: dimensionamento de calha pela NBR 10844 é feito por **trecho**, considerando a vazão acumulada progressivamente da boca coletora mais distante até a mais próxima do condutor. Faltam, no mínimo:
- **(a)** comprimento de cada trecho de calha entre bocas coletoras (não só o perímetro total);
- **(b)** número e posição das bocas coletoras/condutores verticais ao longo do perímetro;
- **(c)** seção transversal e material da calha;
- **(d)** declividade efetivamente adotada (mínimo normativo de 0,5%, conforme Skill).

**A cobrar:** do projetista terceirizado (autor da proposta), planta detalhada de cobertura com esses quatro elementos. Esse recálculo só pode ser fechado depois de resolvidas as pendências dos itens 1 (I) e 2 (área de contribuição), pois a vazão de cada trecho depende diretamente desses dois valores.

---

## Notas técnicas de partida do projeto (Saturnino)
- Intensidade pluviométrica (I) e tempo de retorno (T): **pendentes** — sem valor confirmado de IDF Barra da Tijuca/RJ nem definição de T (5 ou 25 anos), nenhum dimensionamento a jusante está fechado.
- Área de contribuição mínima do condutor vertical: 210 m² (180 + 30), sujeita a acréscimo por parede exposta a confirmar.
- Caixa de areia: obrigatória, deve ser reincluída no projeto antes do ponto de lançamento.
- Lançamento final: não pode ser na prumada de esgoto sanitário — destino correto (rede pública pluvial/infiltração/corpo receptor) a confirmar após checagem de rede disponível no logradouro (Kelsen/Hely).
- Diâmetro do condutor vertical: manter no mínimo o valor resultante do cálculo (a recalcular com I e área corretos); não reduzir por conveniência de shaft.
- Posição da boca coletora na transição de materiais: correta como proposta.
- Dimensionamento de calha por trecho (comprimento, nº de bocas, seção, declividade): pendente de planta detalhada do projetista terceirizado.

## Pendências bloqueantes
1. Valor real de I (IDF) para Barra da Tijuca/RJ — cobrar de Rio-Águas/Prefeitura do Rio ou INMET.
2. Tempo de retorno (T) a adotar — 5 ou 25 anos — cobrar confirmação de Cardozo/cliente, dada a descrição de "região de alta intensidade pluviométrica".
3. Confirmação de existência de parede exposta na cobertura (área de contribuição adicional) — cobrar planta de fachada/corte de Oscar ou do projetista terceirizado.
4. Correção da conexão do pluvial (hoje ligado à prumada de esgoto sanitário) e definição do destino correto de lançamento — cobrar confirmação de rede pluvial disponível no logradouro junto a Kelsen/Hely.
5. Reinclusão da caixa de areia antes do ponto de lançamento.
6. Diâmetro do condutor vertical: manter o mínimo calculado (a recalcular após pendências 1-3), nunca reduzir por espaço de shaft — se necessário, revisar layout de shaft com Oscar/Baumgart.
7. Planta detalhada da calha (comprimento por trecho, nº/posição de bocas coletoras, seção, declividade adotada) — cobrar do projetista terceirizado.

Não assino ART — aponto a necessidade de engenheiro civil/sanitarista licenciado para o memorial final; Cardozo registra o encaminhamento.
