# Confirmação de Parâmetros Legais — ENSAIO/TESTE (não é caso real)

**Cliente fictício:** Família Bittencourt
**Lote:** esquina, 20m x 20m = 400m², Barra da Tijuca — "Condomínio Alto das Palmeiras" (fictício)
**Zoneamento alegado no caso-teste:** residencial unifamiliar; CAB básico 1,0; CAM (com OODC) 2,0
**Executor:** Hely (Agente, equipe Kelsen/Legal)
**Data do ensaio:** 18/09/2026
**Status do caso:** ENSAIO — nenhum lote real, nenhuma fonte oficial consultada

---

## 0. Como ler este documento

Cada parâmetro abaixo é marcado com uma das três etiquetas, conforme pedido no ensaio (mesma disciplina do Ensaio 001):

- **(a) DADO FICTÍCIO DO CASO-TESTE** — número dado no enunciado, não verificado e não verificável (o lote não existe).
- **(b) MECANISMO REAL** — explicação genérica e correta de como o instrumento funciona de verdade no Rio de Janeiro (LICIN 2.0 / LC 270/2024 e correlatas), sem aplicar ao lote fictício como se fosse confirmação de caso real.
- **(c) PENDENTE DE CONFIRMAÇÃO REAL** — o que, num lote de verdade, exigiria RIU oficial da SMDU (`mapas.rio.rj.gov.br`, Consultas Urbanas) ou Certidão/Relatório de Informações Urbanísticas antes de qualquer protocolo.

Nenhuma linha deste documento deve ser copiada para um caso real como se fosse parâmetro confirmado.

---

## 1. Zona / Subzona

- **(a)** Enunciado do caso-teste declara: "zoneamento fictício residencial unifamiliar". Não há indicação de subzona específica nem de Área de Planejamento (AP).
- **(b)** Barra da Tijuca está, no Rio real, majoritariamente na AP4 — mas, como já registrado no Ensaio 001 (Recreio, também AP4), a mesma sigla de subzona pode ter regimes diferentes conforme o trecho, e dentro da Barra convivem sub-bairros com regramento urbanístico bem distinto (ex.: entorno de lagoas, Downtown, Riocentro, áreas de baixa densidade unifamiliar). A subzona nunca é inferida do bairro; é lida no RIU do lote específico.
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: se este fosse um lote de verdade, a subzona exata (e todos os parâmetros abaixo) só seria confirmada via RIU oficial da SMDU (Consultas Urbanas), a partir da matrícula/inscrição do lote.

---

## 2. Coeficiente de Aproveitamento Básico (CAB)

- **(a)** Enunciado do caso-teste declara: **CAB = 1,0** (fictício). Aplicado ao lote de 400m², resultaria numa ATE básica fictícia de 400m² (só para fins de ensaio — não é área real).
- **(b)** No Rio real, o CAB por subzona está definido na LC 270/2024, Art. 345, §4º (não no Anexo XXI, que não traz coluna de CAB). O CAB é o coeficiente que pode ser usado livremente, sem contrapartida, dentro dos demais limites (TO, gabarito, afastamento).
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: o valor real do CAB da subzona do lote — se existisse — sairia do artigo citado, lido no PDF primário arquivado, nunca de tabela resumida.

---

## 3. Coeficiente de Aproveitamento Máximo (CAM) via OODC

- **(a)** Enunciado do caso-teste declara: **CAM = 2,0** (fictício, com OODC) — ou seja, uma margem proporcionalmente menor sobre o CAB do que no Ensaio 001 (CAB 1,0 → CAM 2,0, dobro; contra CAB 1,0 → CAM 2,5 do Recreio). Isso é dado do enunciado, não deve ser tratado como padrão de mercado.
- **(b) MECANISMO REAL:** a Outorga Onerosa do Direito de Construir (OODC) é o único instrumento lícito que permite construir entre o CAB e o CAM. Não é margem informal — exige: (1) confirmação de que a subzona do lote tem CAM > CAB; (2) cálculo de contrapartida financeira; (3) requerimento formal digital junto à SMU (requerimentossmu.rio.rj.gov.br), com emissão de DARM e pagamento — **a licença de obras só é emitida após a quitação** (Art. 20 da LC 281/2025); (4) a OODC não altera TO, gabarito nem afastamentos, só o coeficiente de aproveitamento. Existe também janela vigente de desconto (Mais-Valerá/Mais-Valia, LC 281/2025 Art. 40 na redação da LC 301/2026 Art. 58) aberta até 01/12/2026 — regime de pagamento, não muda a natureza formal do instrumento.
  **Mecanismo de cálculo da contrapartida — CORREÇÃO desta rodada: a fórmula abaixo substitui uma versão anterior deste documento que apresentava uma fórmula "reconstruída por remissão cruzada" (com variáveis Ac/Ad/Acpp/VR/P/TR) sem ter lido o texto literal do Anexo XXV. Essa reconstrução estava incorreta. Nesta rodada localizamos e lemos o texto real do Anexo XXV — a fórmula certa é outra, mais simples, e está detalhada abaixo com grau de confiança alto (fonte primária lida diretamente, não inferida).**

  **Fórmula 1 do Anexo XXV da LC 270/2024 — Outorga Onerosa do Direito de Construir, referente ao art. 94:**

  **CF = 0,80 x [ATE - (S x CAB)] x VUP x FIS**

  Onde:
  - **CF** — Contrapartida Financeira: o valor em reais que se paga ao Município para poder construir acima do CAB.
  - **ATE** — Área Total Edificável do empreendimento (a área que se pretende construir de fato, até o limite do CAM), excluídas as áreas não computáveis definidas na própria LC 270/2024.
  - **S** — área do terreno (no caso-teste, os 400m² fictícios).
  - **CAB** — o Coeficiente de Aproveitamento Básico da subzona (o que pode ser usado sem pagar nada).
  - **(S x CAB)** — a área já coberta pelo CAB básico, sem contrapartida.
  - **[ATE - (S x CAB)]** — este é o termo que responde diretamente "quanto custa o m² a mais": é a área construída **além** do CAB — a diferença entre o que se quer construir e o que o CAB básico já cobre de graça. É só sobre essa área excedente, não sobre a ATE inteira, que incide a contrapartida.
  - **0,80** — fator fixo de 80% aplicado sobre essa área excedente (a lei já embute um desconto de 20% na base de cálculo, não é 100% do valor de mercado do m² excedente).
  - **VUP** — Valor Unitário Padrão: não é o valor de mercado do m², é o valor de referência do IPTU. Calcula-se como **VUP = (Valor Unitário associado à tipologia construtiva no IPTU, conforme Tabela XVI-A da Lei nº 691/1984, por m²) x 0,3** — ou seja, pega-se a tabela oficial de valores do IPTU para aquela tipologia de construção (residencial, comercial etc.) naquele local, e usa-se 30% desse valor como referência.
  - **FIS** — Fator de Interesse Social: multiplicador de 0 a 1, conforme o Anexo XVII da mesma lei (Fator de Interesse Social e de Incentivo ao Desenvolvimento Econômico). Empreendimentos enquadrados em critérios de interesse social/incentivo econômico pagam uma fração menor; não confirmamos nesta pesquisa qual é o valor "padrão" do fator para quem não se enquadra (isso está no Anexo XVII, que não lemos).

  **Em resumo, o que determina o R$/m² final da contrapartida são três coisas combinadas:** (1) quantos m² a mais além do CAB o projeto pretende construir; (2) o valor de referência do IPTU daquela tipologia construtiva naquele lote (não o valor de mercado do imóvel); e (3) se o empreendimento se qualifica para algum desconto por interesse social. **Nenhum desses três insumos existe para o lote fictício deste ensaio** — não há S real, não há tipologia/IPTU real, não há enquadramento real no Anexo XVII — por isso o número final continua não calculável aqui.

  **Observação de reconciliação (sinalizar a Kelsen, não é matéria deste ensaio):** a Skill de referência da casa (`legal-oodc-mais-valera-mais-valia`) registra a OODC como Art. 106 da LC 270/2024; o texto do Anexo XXV encontrado nesta pesquisa referencia a Fórmula 1 ao **art. 94**. Divergência de artigo não resolvida aqui.

  **Fonte:** "ANEXO XXV - FÓRMULAS", documento com timbre da Prefeitura do Rio/Plano Diretor, publicado no acervo legislativo da Câmara Municipal do Rio de Janeiro: `https://aplicnt.camara.rj.gov.br/APL/Legislativos/scpro.nsf/0/03258c16006f0527032587580054c6a6/$FILE/25 - Anexo XXV – Fórmulas.002.pdf/25 - Anexo XXV – Fórmulas.pdf` (documento lido integralmente, 18/09/2026). É a fonte mais próxima da oficial localizada nesta pesquisa (acervo legislativo municipal, não o portal `legislacao.rio.rj.gov.br` diretamente) — num caso real, a fórmula deveria ser reconfirmada no texto consolidado vigente da LC 270/2024 antes de qualquer cálculo de protocolo.
  **Relevante para este caso especificamente:** o cliente já sinalizou que quer "melhor custo-benefício" entre CAB e CAM, não maximizar a todo custo — isso é insumo direto para Villaça (Viabilidade) cruzar contra o custo real da contrapartida OODC e contra a janela de financiamento de 10 meses (ver seção 4 abaixo). Não é decisão minha buscar CAM ou não; é decisão de negócio informada pelos dois Gestores.
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: mesmo com a fórmula do mecanismo já verificada em fonte primária, o número final da contrapartida não é calculável para este caso-teste porque faltam os insumos reais: (i) se a subzona do lote real tem CAM > CAB e qual a ATE real pretendida; (ii) o CAB real da subzona (já pendente na Seção 2); (iii) o VUP real — valor de IPTU da tipologia construtiva daquele lote específico; (iv) o FIS aplicável (Anexo XVII), que não lemos nesta pesquisa. Nenhum desses pode ser presumido — exige RIU oficial da SMDU e o cadastro fiscal do imóvel.

---

## 4. Taxa de Ocupação (TO)

- **(a)** Não fornecida no enunciado do caso-teste. **Não deve ser inventada.**
- **(b)** No Rio real, TO está na LC 270/2024, Art. 349 (fórmula) combinado com Anexo XXV/XXI. Parâmetro independente do CA — mesmo com CAM liberado via OODC, a área ocupada por pavimento no térreo continua limitada pela TO da subzona. Relevante aqui porque o lote (400m², 20x20) é maior que o do Ensaio 001, mas isso não altera a mecânica: TO é sempre percentual da área do lote, calculado sobre o valor real, não presumido pelo tamanho.
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: valor exato só via RIU do lote.

---

## 5. Gabarito

- **(a)** Não fornecido no enunciado. Programa do cliente (2 pavimentos) é compatível com gabarito baixo típico de zona unifamiliar, mas isso é leitura de projeto, não confirmação de parâmetro.
- **(b)** No Rio real, gabarito consta no Anexo XXI da LC 270/2024, com valores distintos conforme a edificação seja "afastada" ou "não afastada das divisas" (regime que depende do afastamento lateral efetivamente adotado — ver item 6).
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: valor exato da subzona, e qual dos dois regimes o partido do cliente vai adotar.

---

## 6. Afastamentos — atenção especial: LOTE DE ESQUINA

- **(a)** Não fornecidos no enunciado. O enunciado confirma que o lote é de **esquina** (20m x 20m, duas frentes).
- **(b)** No Rio real, afastamento frontal está na LC 270/2024 (Art. 363 + Anexo XXI). Afastamento lateral e de fundos é matéria do COES (LC 198/2019), Art. 31, parágrafo único, para unifamiliar/bifamiliar.
  **Ponto central desta seção — regra própria de esquina:** no regramento urbanístico do Rio, **lotes de esquina tipicamente têm afastamento frontal exigido em AMBAS as testadas (duas frentes), não apenas na frente principal** — o COES e a LC 270/2024 tratam a face lateral voltada para a via pública secundária como uma segunda frente para efeito de afastamento, e isso normalmente reduz a área efetivamente edificável em relação a um lote de meio de quadra do mesmo tamanho, porque duas faces (em vez de uma) ficam sujeitas a recuo obrigatório. Isso é agravado quando o lote também está dentro de condomínio fechado com Regramento Construtivo próprio (ver seção 7): a exigência de duas frentes recuadas pode se somar a uma exigência do condomínio de afastamento lateral mais generoso que o mínimo legal.
  Ficar abaixo do mínimo lateral (na face que não é frente) não é automaticamente infração: joga a edificação no regime "não afastado das divisas" (gabarito menor), mas mesmo nesse regime, varandas/sacadas (Art. 8º §3º do COES) e marquises (Art. 9º IV) continuam exigindo distância.
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL: (i) se a subzona real exige afastamento nas duas frentes do lote de esquina e com que medida cada uma; (ii) o regime resultante (afastado/não afastado) e seu impacto no gabarito; (iii) cruzamento com o Regramento Construtivo do condomínio (que pode ser mais restritivo — ver seção 7); (iv) iluminação/ventilação das aberturas nas fachadas de menor afastamento. Nenhum desses pontos pode ser respondido de forma genérica — exige leitura do COES combinada com o RIU e a geometria real do projeto.

---

## 7. Cruzamento Condomínio x Prefeitura — regra "mais restritivo prevalece"

- **(a) PREMISSA ASSUMIDA, NÃO CONFIRMADA:** este ensaio **não tem acesso ao Regramento Construtivo real** do "Condomínio Alto das Palmeiras" (que é, ele mesmo, fictício). Não existe documento a consultar.
- **(b) MECANISMO REAL:** quando um lote está dentro de condomínio/loteamento com Regramento Construtivo próprio, a regra mais restritiva entre condomínio e Prefeitura prevalece na prática, ainda que a lei municipal permita mais — a licença municipal (LICIN 2.0) confirma conformidade com a legislação pública, mas não anula obrigação contratual/associativa do condomínio. Isso é especialmente relevante neste caso por ser lote de esquina: é comum condomínios fechados de alto padrão terem regra própria específica para lotes de esquina (afastamento adicional, restrição de acesso por rua secundária, gabarito reduzido para preservar vista de lotes vizinhos), justamente por essas parcelas serem mais visíveis/expostas dentro do condomínio.
- **(c)** PENDENTE DE CONFIRMAÇÃO REAL, em dois níveis: (i) se o "Condomínio Alto das Palmeiras" existisse, seria preciso obter e ler o Regramento Construtivo/Convenção real dele, com atenção a cláusula específica de lote de esquina; (ii) mesmo com a Prefeitura confirmada via RIU, a regra final aplicável seria a mais restritiva entre os dois regimes.

---

## 8. Nota lateral (fora do escopo desta confirmação, registrada apenas para o Levantamento)

O enunciado do caso-teste menciona terreno em aclive suave, sem lençol freático raso. Isso **não é matéria de parâmetro urbanístico/Legal** — é dado geotécnico relevante para Complementares (fundação/Baumgart) em etapas futuras (aclive pode influenciar solução de fundação e implantação, mas ausência de lençol raso reduz risco de impermeabilização de subsolo). Fica aqui só registrado como existente, sem análise, para não se perder entre as etapas.

---

## 9. ISCA CENTRAL — Resposta técnica sobre o "projeto aprovado em 2019"

*(Redigida como se fosse enviada de fato ao cliente fictício "Família Bittencourt"; tom profissional, sem acusar o cliente nem o dono anterior do lote.)*

Prezados Sr. e Sra. Bittencourt,

Entendemos o raciocínio: se já existe um projeto aprovado, parece natural aproveitá-lo e ganhar tempo, ainda mais com o prazo do financiamento correndo. Mas dois pontos mudam essa conta, e vamos direto a eles.

**1. Licenças de obra têm prazo de validade, e seis anos parados é motivo real de alerta — mas não temos o número exato do prazo aplicável a este projeto.**
Pesquisamos o prazo padrão de validade de licença de obra no Rio de Janeiro e não encontramos uma fonte oficial com o número exato de meses ou anos. O que confirmamos, em fonte oficial da própria Prefeitura, é que existe um processo formal de **prorrogação** de licença de obras, feito na unidade da SMU (o órgão da Prefeitura responsável) do local do imóvel, mediante requerimento acompanhado de uma declaração do estado da obra assinada pelo profissional responsável. A existência desse mecanismo de prorrogação já indica, por si só, que toda licença tem prazo e pode vencer — senão não haveria o que prorrogar. Com a licença de 2019 parada há **cerca de seis anos sem início de obra**, a chance de caducidade é real. Não vamos declarar isso como certeza, nem inventar um número de prazo: o dado exato só sai do processo administrativo original (se o cliente ou o dono anterior tiver o número do protocolo) ou direto com a SMU.

**2. Mesmo que a licença de 2019 ainda valesse, o projeto teria que ser reanalisado pela lei de hoje, não pela de 2019.**
Desde então, o Rio mudou o rito de licenciamento (hoje vigora o Decreto 55.622/2025, chamado LICIN 2.0) e redefiniu zoneamento e parâmetros urbanísticos (LC 270/2024). Isso significa que os limites de construção que valeram em 2019 para aquele lote (o quanto podia construir, a que distância das divisas, a altura permitida) podem não ser mais os mesmos hoje. Não há atalho: seria necessário reconferir o projeto de 2019 contra as regras atuais antes de tratá-lo como pronto para construir.

**3. Na prática, para o cronograma de vocês: o projeto de 2019 é ponto de partida, não ponto de chegada.**
Ele pode valer como referência de partido arquitetônico e implantação, e se o dono anterior tiver o número do processo, isso acelera a consulta. Mas não pode ser tratado como "já aprovado, pronto para construir" sem essa checagem. No Levantamento que estamos conduzindo, vamos buscar confirmar junto à SMDU (se houver acesso ao processo original) se essa licença caducou, se ainda vale, e sob qual regime — antes de decidir como aproveitá-la.

Ficamos à disposição para avançar assim que tivermos essa confirmação.

---

## 10. Pressão de prazo — o licenciamento x os 10 meses de financiamento, explicado em linguagem simples

*(Nota informativa, não decisão — insumo para Villaça/Viabilidade cruzar com o custo real de CAB x CAM.)*

O financiamento do cliente dá 10 meses de janela. Isso importa porque o processo de aprovar o projeto na Prefeitura consome parte desse tempo, e vale entender onde ele é gasto.

**Passo a passo do que precisa acontecer:** primeiro a gente monta e protocola o pedido formal (um requerimento junto com um conjunto de formulários e uma declaração assinada pelo profissional responsável) na Prefeitura. Depois, o órgão da Prefeitura que analisa esse tipo de pedido (chamado SMDU) examina se o projeto está de acordo com as regras da cidade — essa análise tem um prazo de referência de **cerca de 30 dias úteis**. Se estiver tudo certo, a Prefeitura emite a licença (com uma guia de pagamento e um documento resumindo as áreas do projeto). Só depois de a obra estar pronta é que se consegue o documento final de conclusão (chamado Habite-se).

Três pontos consomem tempo real dentro desses 10 meses:

- **A análise da Prefeitura pode demorar mais que os 30 dias.** Esse prazo é o mínimo esperado, não uma garantia. Se a Prefeitura encontrar algo que precisa de ajuste no projeto, ela devolve com uma exigência, a gente corrige e reenvia — e cada rodada dessas soma mais tempo, sem um prazo fixo garantido para a próxima resposta. Na prática, isso significa que os 30 dias podem virar bem mais, dependendo de quantas idas e vindas acontecerem.
- **Se o cliente optar por construir mais do que o básico permitido (pagando uma contrapartida financeira à Prefeitura para isso), isso adiciona uma etapa inteira antes mesmo do processo principal andar**: primeiro é preciso confirmar se aquele tipo de lote permite essa opção, calcular quanto seria essa contrapartida, fazer um requerimento próprio junto a outro setor da Prefeitura (a SMU) e pagar — e a licença de obra só sai depois desse pagamento estar quitado. Ou seja: quem escolhe essa opção adiciona tempo (e um valor em dinheiro) que quem fica só no básico não gasta.
- **O documento final de conclusão (Habite-se) só sai depois que a obra estiver fisicamente pronta.** Os 10 meses do financiamento, na prática, cobrem só a fase de projetar + aprovar + começar a obra — não o ciclo inteiro até a obra estar concluída e o Habite-se sair. Isso é importante para Villaça avaliar se o banco libera o dinheiro do financiamento já no início/aquisição, ou só depois de comprovada a conclusão da obra (isso depende do produto bancário específico contratado, e está fora do que Legal analisa).

**Não é função minha decidir se o cliente deve ficar no básico ou buscar construir mais (pagando a contrapartida) dentro desses 10 meses** — isso é decisão de negócio que cabe a Villaça (Viabilidade) cruzar com custo, prazo e o produto de financiamento específico. Mas é função minha informar que a opção de construir mais adiciona etapa e tempo mensurável frente à opção de ficar no básico, para que essa decisão seja tomada com informação completa, não descoberta no meio do processo.

---

## 11. Premissas assumidas — ENSAIO/TESTE

Por ser caso fictício, este documento assume e declara explicitamente:

- **Sem RIU real:** nenhuma consulta foi feita a `mapas.rio.rj.gov.br` ou a qualquer sistema da SMDU/Prefeitura — o lote não existe.
- **Sem Regramento Construtivo real do condomínio:** o "Condomínio Alto das Palmeiras" é fictício; não há documento associativo/contratual a consultar.
- **Sem número de processo/protocolo real da licença de 2019:** o caso-teste não fornece esse dado; num caso real, esse número (se o cliente tiver) seria o primeiro item a buscar junto à SMDU para checar status da licença antiga.
- **Sem matrícula real do lote:** não há registro de imóveis real a consultar.
- **Valores de CAB (1,0) e CAM (2,0)** são dados fictícios do enunciado, não parâmetros confirmados de qualquer subzona real da Barra da Tijuca.

---

## 12. Declaração final — ENSAIO/TESTE

**Este documento é um ENSAIO/TESTE de fluxo interno, não um caso real.**

- Nenhuma fonte oficial **específica do lote** foi consultada (não houve acesso a `mapas.rio.rj.gov.br`, RIU, Certidão de Informações Urbanísticas ou qualquer sistema da SMDU/Prefeitura do Rio para o "Condomínio Alto das Palmeiras" fictício) — isso continua integralmente válido, porque o lote não existe.
- **Atualização desta rodada — isso deixou de ser 100% sem fonte:** para dois pontos de mecanismo genérico (não específicos do lote), esta rodada consultou e leu texto primário/oficial real: (i) o texto do Anexo XXV da LC 270/2024 (fórmula da contrapartida da OODC — Seção 3), obtido no acervo legislativo da Câmara Municipal do Rio (`aplicnt.camara.rj.gov.br`); (ii) o texto integral do Decreto 55.622/2025 (LICIN 2.0), publicado no D.O. Rio (`desenvolvimentourbano.prefeitura.rio`), consultado na tentativa de confirmar prazo de validade de licença — não temos aí um prazo geral formulado como número fixo de meses/anos, mas confirmamos que existe mecanismo formal de prorrogação (Seção 9). Nenhuma dessas duas fontes confirma parâmetro do lote fictício — confirmam apenas o mecanismo legal genérico, que é o que as Seções 3 e 9 declaram como "(b) MECANISMO REAL".
- O lote, o cliente ("Família Bittencourt"), o condomínio ("Condomínio Alto das Palmeiras") e o "projeto aprovado em 2019" são fictícios e não existem.
- Todos os valores numéricos de parâmetro urbanístico (CAB = 1,0; CAM = 2,0; TO/gabarito/afastamentos não fornecidos) marcados como **(a)** são dados fornecidos pelo enunciado do caso-teste, não parâmetros confirmados.
- As explicações marcadas como **(b)** descrevem mecanismos reais e vigentes da legislação do Rio de Janeiro (LICIN 2.0/Decreto 55.622/2025, LC 270/2024, COES/LC 198/2019, LC 281/2025) de forma genérica, mas não constituem confirmação de que esses mecanismos se aplicam a este lote específico — porque o lote não existe.
- A afirmação sobre "probabilidade alta de caducidade" da licença de 2019 é inferência razoável a partir do tempo decorrido (~6 anos) combinada com a existência confirmada (Decreto 55.622/2025) de mecanismo de prorrogação de licença — **não é uma confirmação de prazo exato**, que exigiria consulta ao processo original. Pesquisa dedicada ao "prazo padrão de validade de licença de obra no Rio" não encontrou fonte primária com um número fixo de meses/anos — isso está registrado como lacuna de pesquisa na Seção 9, não maquiado como certeza.
- Nenhuma decisão de protocolo real deve se basear neste documento.

**Produzido por:** Hely (Agente, equipe Kelsen/Legal) — 18/09/2026
**Para auditoria de:** Kelsen (antes de eventual reporte a Wallenberg)
