---
name: viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj
description: Pré-Estudo de Viabilidade de casa unifamiliar no Rio — como estimar custo de obra pelo CUB (NBR 12721) sobre a base de área certa (área real, área equivalente, nunca área computável), o que o CUB exclui (fundação especial, elevador/plataforma, piscina, paisagismo, AC, projetos, demolição, BDI), como tratar casa de 2 pavimentos com o projeto-padrão R-1 (térreo), e como estimar valor de revenda pelo método comparativo direto da NBR 14653-2 (homogeneização, fator de oferta anúncio x venda, base de área IGUAL entre comparável e avaliando). Use sempre que Villaça, Mascaró ou Fiker forem montar custo de obra, valor de revenda, comparação CAB x CAM ou cenários de área — mesmo que o pedido só mencione "quanto custa construir", "CUB", "R$/m²", "quanto vale a casa pronta", "comparáveis", "anúncio" ou "área construída", sem citar a norma pelo nome.
version: v1.2
status: ativa-com-ressalva
fonte_primaria_lida: "Nenhuma das duas normas (ABNT NBR 12721:2006 e NBR 14653-2:2011) foi lida no texto oficial — são pagas e não estão em D:\\008_Normas ABNT\\. Lido no primário: PDF do CUB/m² Sinduscon-Rio set/2026 (lista de exclusões, por Mascaró em 02/10/2026). O resto vem de fontes secundárias citadas na seção 7."
data: 2026-10-02
validacao: "Villaça (Gestor dono), 02/10/2026. Criada após a reprovação da Etapa 02 do Ensaio 003 (custo e revenda aplicados sobre área computável). Coerência conferida por Grep em .claude/skills (CUB, 12721, 14653, OODC): complementa legal-oodc-mais-valera-mais-valia (custo da OODC continua lá), complementa ia-orcamento-executivo-obra (aquela trata de ferramenta e de orçamento executivo; esta de estimativa paramétrica), complementa legal-art-crea (CUB usado lá como base de ART). Nenhuma contradição encontrada."
changelog:
  - "v1.0 (02/10/2026, Villaça): criada."
  - "v1.1 (02/10/2026, Villaça): §2.2 e §2.6 corrigidas — o reajuste pelo INCC-M vale durante todo o cronograma de desembolso (curva de medição), não só até o início da obra (erro apontado no parecer_bardi_v2 do Ensaio 003). Nova §2.7: custo de moradia (aluguel) durante todo o período pré-obra + obra, contado desde hoje. Roteiro item 2 ajustado. Macete M7 (minuta de contrato da PF, cláusula 3.3, lida no original). Backup da v1.0 em 01_CEO/Decisoes_Autonomas/_backups/2026-10-02/ (PARCIAL; a v1.0 integral não foi preservada)."
  - "v1.2 (02/10/2026, Villaça): nova regra na §2.6 e nova §2.8 — ler a cláusula de reajuste do documento do cliente e citá-la literalmente (data-base e periodicidade); conferir toda citação do Dossiê contra o texto literal; distinguir dado do documento de premissa (ex.: fim da obra). M7 rebaixado a apoio: a fonte primária da periodicidade é o próprio documento do caso. R4 ajustada; R5 nova. Origem: parecer_bardi_v3 (a v1-v3 afirmaram que a proposta 5.12 'não declara mês-base', quando ela diz 'INCC-M mensal a partir da data desta proposta'). Backup INTEGRAL da v1.1 em 01_CEO/Decisoes_Autonomas/_backups/2026-10-02/*_v1.1_INTEGRAL_ANTES_v1.2.md."
tipo: Inteligência (Trilha A)
gestor_alvo: Villaça (Viabilidade)
agente_principal: Mascaró (custo) e Fiker (revenda)
agentes_cross: Lúcio/Oscar (fornecem área real por tipo), Kelsen/Hely (área computável e TO), Lelé (orçamento executivo depois)
---

> **CÓPIA DE REGISTRO.** O arquivo vivo está em `.claude/skills/viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj/SKILL.md`. Toda mudança é feita lá e espelhada aqui.

# Skill: Viabilidade — CUB/NBR 12721 sobre a área certa e revenda pela NBR 14653-2 na mesma base

> RESSALVA DE FONTE. (1) As normas ABNT NBR 12721:2006 e NBR 14653-2:2011 **não foram lidas no texto oficial**. Os coeficientes da seção 2.3 vêm de fontes secundárias que reproduzem o item 5.7.3 e de um orçamento paramétrico público que os aplica (seção 7). Tratar como "texto provável da norma, a confirmar". (2) A lista de exclusões do CUB (seção 2.4) foi lida no PDF primário do Sinduscon-Rio. (3) As duas normas entram na **lista de compra** do acervo. (4) Nenhum número desta Skill é custo fechado ou valor de venda garantido.

## 1. POR QUE ESSA SKILL EXISTE

No Ensaio 003 (Etapa 02), custo e revenda foram calculados sobre a **área computável** (a da lei) porque era a única área disponível. Isso subestima o custo (a obra constrói também varanda, garagem, área técnica) e mistura bases na revenda (os comparáveis falam em área construída). A regra que faltava ao organismo: **cada conta tem a sua base de área, e ela precisa ser declarada linha por linha.**

## 2. CUSTO DE OBRA PELO CUB (NBR 12721)

### 2.1 As três áreas — nunca trocar uma pela outra

| Área | O que é | Quem fornece | Serve para |
|---|---|---|---|
| **Área computável** | A que conta no limite legal (ATE, CAB, TO). Exclui o que a lei manda excluir (varandas nas condições do COES, vagas, etc.) | Kelsen/Hely | Teto legal. **Não serve** de base de custo nem de revenda |
| **Área real (construída total)** | Toda superfície coberta e descoberta com custo de execução perceptível | Lúcio/Oscar (quadro de áreas por tipo) | Base da área equivalente; base da revenda (se o comparável também for construída total) |
| **Área equivalente** | Σ (área real de cada tipo × coeficiente de equivalência). Área "virtual" de custo igual ao do padrão | Mascaró, sobre o quadro de Lúcio | **Base do CUB** |

Regra prática (macete M1): as áreas do quadro da NBR **não são** as da prefeitura. Toda área com custo de execução perceptível entra no quadro de custo, inclusive a que a prefeitura não computa.

### 2.2 Fórmula

Custo parcial (só o que o CUB mede) = **área equivalente × CUB/m² do projeto-padrão e do mês**.
Custo de obra estimado = custo parcial + **itens fora do CUB** (seção 2.4) + **BDI/remuneração do construtor** + reajuste pelo INCC-M **ao longo de todo o cronograma de desembolso** (do mês do CUB até cada medição, não só até o início da obra; ver §2.6).

Sem quadro de áreas por tipo, faça **faixa**: piso = área computável × 1,00 + área não computável × menor coeficiente provável; teto = área construída total × 1,00. Declare a premissa.

### 2.3 Coeficientes médios de equivalência (item 5.7.3 da NBR 12721, conforme fontes secundárias)

| Tipo de área | Coeficiente |
|---|---|
| Área privativa / interna com acabamento (unidade padrão) | 1,00 |
| Salas sem acabamento | 0,75 a 0,90 |
| Lojas sem acabamento | 0,40 a 0,60 |
| **Garagem (subsolo)** | **0,50 a 0,75** |
| **Varandas** | **0,75 a 1,00** |
| **Terraços ou áreas descobertas sobre laje** | **0,30 a 0,60** |
| Estacionamento sobre terreno | 0,05 a 0,10 |
| Áreas de serviço, barrilete, casa de máquinas, caixa d'água | 0,50 a 0,75 |
| Quintais, calçadas, jardins | 0,10 a 0,30 |

Fonte: reprodução secundária do item 5.7.3 (busca de 02/10/2026; ver seção 7, F1) e aplicação real em orçamento paramétrico público (macete M2: interno 1,00; externo coberto 0,70; externo descoberto sobre laje ou solo 0,30; cobertura externa 0,60; barrilete/casa de máquinas 0,70). A norma admite coeficiente próprio quando houver demonstração; os médios valem **na falta** dela.

Garagem coberta **no térreo** de casa não é "subsolo": o coeficiente aplicável não está na lista acima de forma literal. Usar a faixa 0,50 a 0,75 por analogia, **declarando que é analogia**, ou a de "externo coberto" (0,70 do M2).

### 2.4 O que o CUB NÃO inclui (PDF Sinduscon-Rio, lido no primário)

Fundações (inclusive especiais: estacas, blocos), submuramentos, paredes-diafragma, tirantes, **rebaixamento de lençol freático**; **elevador(es)** — a **plataforma elevatória** de acessibilidade entra junto, por ser equipamento de elevação (leitura de Villaça: o PDF diz só "elevador(es)"; na dúvida, ela fica fora do CUB, que é o lado conservador); equipamentos e instalações (fogões, aquecedores, bombas de recalque, **ar-condicionado**, ventilação e exaustão); playground; obras e serviços complementares; urbanização, **piscinas**, **ajardinamento/paisagismo**; impostos, taxas e emolumentos; **projetos** (arquitetura, estrutura, instalações, especiais); **remuneração do construtor (BDI)** e do incorporador.

Também fora: **demolição** de construção existente e destinação de entulho; **automação**; ligações definitivas; sondagem; terreno.

Checklist obrigatório na entrega: cada item acima aparece **com valor ([ECF]) ou como [NC] com o que faltaria**. Nenhum pode sumir.

### 2.5 Projeto-padrão R-1 é TÉRREO — casa de 2 pavimentos

- Na NBR 12721, o R-1 é residência unifamiliar de **1 pavimento**. Não existe projeto-padrão CUB de sobrado unifamiliar.
- Para casa de 2 pavimentos: usar **R-1 do padrão certo (Alto, para alto padrão) como proxy**, declarando que é extrapolação. Não aplicar padrão Normal a casa de alto padrão (macete M3).
- O sobrado tem custo que o R-1 não mede (escada, laje de piso entre pavimentos, estrutura mais carregada). Sem fonte citável de percentual, **não aplicar acréscimo inventado**: registrar como item [NC] "efeito 2 pavimentos" e indicar o sentido (custo real tende a ser maior).
- Não usar R8-N (edifício multifamiliar) como base de casa: R8-N serve de indexador de mercado (ver Skill `ia-orcamento-executivo-obra`), não de custo de casa.

### 2.6 BDI e reajuste

- O CUB não é preço de construtora: falta a remuneração do construtor. Usar referência citável (ex.: faixas de BDI do TCU para edificações), **declarando que é obra pública** e só ordem de grandeza.
- **Reajuste pelo INCC-M (FGV) durante TODO o cronograma de desembolso, pela curva de medição — não só até o início da obra.** A obra é paga em parcelas ao longo da execução, e cada parcela é reajustada até o mês em que é medida/paga (propostas de construtora costumam reajustar pelo INCC durante a execução; ver M7). Parar no início da obra subestima o custo e superestima qualquer "sobra".
- Como fazer, em faixa (extrapolação do passado, não previsão), declarando a taxa mensal usada:
  - **Piso:** desembolso linear do início ao fim da obra (equivale a reajustar até o mês médio da obra).
  - **Teto:** tudo reajustado até o último mês de desembolso (limite superior), ou curva em S, se houver cronograma físico-financeiro que a sustente.
  - Sem cronograma físico-financeiro, não inventar curva: usar piso linear e teto no fim, e dizer que é isso.
- O reajuste vale para **toda conta que dependa do custo**: via CUB, via proposta de construtora, sobra contra o teto do cliente, % do teto. Itens fora do CUB também sofrem reajuste quando ganharem valor.
- Atenção ao mês de dissídio (maio no RJ, observado em 2026): se a obra atravessa maio, declarar se o salto foi modelado ou se está diluído na taxa média.
- **(v1.2) Primeiro o documento do caso.** Se há proposta de construtora, leia a cláusula de reajuste e **cite-a literalmente**, entre aspas: índice, **data-base** e **periodicidade**. Só o que a cláusula de fato não disser vira premissa ou pergunta (ex.: se incide por medição ou sobre o saldo). Nunca escreva "não declara" sem transcrever a cláusula ao lado. Fonte externa (M7) é só apoio, nunca substitui o documento.
- Se o fator do piso for calculado no mês médio, chame-o assim ("fator no mês médio, aproximação da média dos fatores") e diga o tamanho da diferença para a média exata ((1+r)^n − 1)/(n·r). Não o chame de "média".

### 2.8 Citação de documento do cliente (v1.2)

- Toda citação de documento do Dossiê (escritura, proposta, planilha, carta, mensagem, caso base) entre aspas precisa ser **literal**; se for resumo, sem aspas e dito como resumo.
- Nunca atribuir a um documento o que ele não diz. Dado do documento leva [FP]/[DOC]; o que eu deduzo dele leva [PV]/[INF] (ex.: "mudar até dezembro/2028" é prazo de mudança, não data de fim de obra; "1.200 m²" sem base declarada não é "terreno").
- Antes de gravar, conferir cada citação contra o texto literal e listar a conferência na auditoria.

### 2.7 Custo de moradia durante o período pré-obra + obra

- Se o cliente paga aluguel (ou outro custo de moradia) até se mudar para a casa nova, o custo de tempo conta **desde hoje até a mudança**, não só os meses de obra: período pré-obra (projeto, licença) + obra.
- Conta: meses de hoje até a mudança × valor mensal [fonte: o dado do cliente]. Mostrar também quanto custa cada mês de atraso.
- Esse custo fica **fora do teto de obra**, mas entra na leitura do caixa total da família e deve ser dito à parte.

## 3. REVENDA PELO MÉTODO COMPARATIVO DIRETO (NBR 14653-2)

### 3.1 Método

Comparar o avaliando com dados de mercado semelhantes (tipo, padrão, localização, metragem, data), **homogeneizar** as diferenças por fatores ou por tratamento científico e só então tirar o R$/m² do avaliando. Pouca amostra e dados heterogêneos pedem tratamento por fatores com cautela (macete M4).

### 3.2 Regra da base de área IGUAL (sem exceção)

- O R$/m² do comparável é **preço ÷ área do comparável**. Ele só pode multiplicar a **mesma espécie de área** do avaliando.
- Comparável em "área construída" → avaliando em **área construída total**. **Nunca** em área computável.
- Comparável em área privativa → avaliando em área privativa.
- Se a base do comparável é desconhecida, **declarar a premissa** (ex.: "construída total, como informado pelo corretor") e o sentido do erro se a premissa falhar.
- Declarar a base **em cada linha** da tabela de revenda.
- Área de terreno nunca divide preço de casa para comparar com R$/m² construído.

### 3.3 Fator de oferta (anúncio x transação)

- Anúncio é preço pedido, não preço fechado. Antes de entrar na amostra, o anúncio recebe **fator de oferta** (redutor). Na Norma do IBAPE/SP o fator oferta é obrigatório (macete M4, que usa 0,90 em todos os elementos de oferta do exemplo).
- Referência de mercado para calibrar: Raio-X FipeZAP — desconto médio de 9% sobre todas as transações e cerca de 14% nas que tiveram desconto (2T2026, via reportagem; macete M6). Faixa de trabalho: **0,86 a 0,91**, declarada como referência nacional, não local.
- Venda fechada (escritura) **não** recebe fator de oferta.
- Não somar anúncio com venda sem aplicar o fator.

### 3.4 Outros fatores e cuidados

- **Fator área:** em geral, quanto maior a área, menor o R$/m² (macete M5). Casa muito menor que os comparáveis tende a ter R$/m² maior, mas pode perder valor por destoar do padrão do condomínio: declarar os dois sentidos.
- **Restrição nova (ex.: APP)**: comparável vendido antes de a restrição ser conhecida não precifica o imóvel depois dela.
- **Terreno + benfeitoria:** quando der, separar valor do terreno e da edificação (como no exemplo do M4).
- **Peso de um cenário em R$:** mesmo sem comparável na metragem, dar **ordem de grandeza com faixa larga e premissa declarada** (ex.: aplicar a faixa do condomínio à área construída do cenário e mostrar o sentido do erro). Deixar o cliente sem número é pior que um número largo e honesto.

## 4. ROTEIRO DE ENTREGA (Villaça)

1. Pedir a Kelsen a área computável e a TO; pedir a Lúcio a área real por tipo. Sem Lúcio, usar **área construída de trabalho** em faixa, declarada.
2. Mascaró: área equivalente (faixa) × CUB R-1 do padrão + itens fora do CUB (checklist 2.4) + BDI + INCC ao longo do cronograma de desembolso (§2.6). Villaça soma à parte o custo de moradia do período pré-obra + obra (§2.7).
3. Fiker: comparáveis com base de área declarada linha por linha; fator de oferta nos anúncios; mesma base no avaliando; ordem de grandeza para todo cenário.
4. Villaça: refaz as contas, confere bases iguais, e diz explicitamente quando um programa **não cabe** num cenário.
5. Efeito da **garagem coberta na TO**: vaga coberta fora da área computável pode **ocupar a projeção** (taxa de ocupação). Cada m² de garagem coberta dentro da projeção tira 1 m² da área computável do térreo. Mostrar isso em m² e em R$.

## 5. MACETES DE QUEM FAZ

| # | Tipo | Fonte (acesso 02/10/2026) | O que fazer | Por que funciona | Limite |
|---|---|---|---|---|---|
| M1 | A (profissional: Ricardo M. Trevisan, arquiteto) | "Quais áreas entram no quadro NBR 12721?", 21/02/2015: https://ricardotrevisan.com/2015/02/21/quais-areas-entram-no-quadro-nbr-12721/ | Montar o quadro de custo com **toda área de custo perceptível**, sem confundir com a área da prefeitura | A prefeitura exclui áreas que custam para construir; usar a área dela subestima o custo | Texto de blog, voltado a incorporação em condomínio |
| M2 | B (entidade pública: Prefeitura de Santos Dumont/MG, orçamento paramétrico, Volpi Soluções Municipais, 25/06/2025) | https://www.santosdumont.mg.gov.br/arquivos/files/1-%20ORCAMENTO-PARAMETRICO-REV03%20-%20ASSINADO.pdf | Converter o quadro de áreas em área equivalente (interno 1,00; externo coberto 0,70; externo descoberto 0,30; cobertura externa 0,60) e só então multiplicar pelo R$/m²; somar BDI à parte (25% no caso) | Mostra o método da NBR 12721 aplicado e auditável num orçamento oficial | Obra pública (creche), coeficientes escolhidos pelo autor dentro das faixas; não é residência de alto padrão |
| M3 | B (empresa: Sienge, blog "NBR 12721") | https://sienge.com.br/blog/nbr-12721/ | Listar à parte fundações especiais, elevadores, legalizações e projetos; não aplicar CUB de padrão Normal a projeto de alto padrão | O CUB não inclui esses itens; padrão errado subestima o custo global | Blog de fornecedor de software, não substitui a norma |
| M4 | A (profissional: Eng. Luiz Henrique Cappellano, IX Seminário Nacional de Engenharia de Avaliações e Perícias, IBAPE) | https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2026/03/ix-seminario-nacional-de-engenharia-de-avaliacoes-e-pericias-desmistificando-o-uso-de-fatores-cappellano.pdf | Aplicar o fator oferta a todo elemento de oferta (exemplo usa 0,90); separar terreno e edificação; validar cada fator (só usar o que reduz a dispersão) | Na Norma IBAPE/SP o fator oferta é obrigatório; a validação evita fator que piora a amostra | Fatores calibrados para São Paulo; não transpor números para o Rio sem fundamento |
| M5 | A (profissional: Marcos Mansour Chebib Awad, XIX COBREAP, IBAPE, 2017) | https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2017/08/085.pdf | Considerar o fator área: quanto maior a área, menor o R$/m² | Evita extrapolar o R$/m² de casa grande para casa pequena (e vice-versa) sem correção | Estudo de apartamentos; para casas, só o sentido, não o expoente |
| M6 | B (empresa: FipeZAP, Raio-X 2T2026, via reportagem do Portas de 18/08/2026) | https://portas.com.br/noticias/desconto-medio-venda-imoveis-fipezap/ | Calibrar o fator de oferta pelo desconto médio observado (9% em todas as transações; ~14% nas com desconto) | É dado de transação real comparando anúncio e fechamento | Nacional, sem recorte de casa em condomínio nem de cidade; PDF primário não lido |
| M7 | B (entidade pública: Polícia Federal/MJSP, CPL/SELOG/SR/PF/PE, Minuta de Contrato de obra de engenharia, Processo 08400.007001/2018-11) | Cláusula 3.3, lida no PDF original em 02/10/2026: o valor "poderá ser corrigido anualmente [...] contado a partir da data limite para a apresentação da proposta, pela variação do Índice Nacional de Custo da Construção – INCC, coluna 35 [...] FGV": https://www.gov.br/pf/pt-br/assuntos/licitacoes/2018/pernambuco/concorrencias/licitacao-para-reforma-da-sede-da-sr-pe/anexo-ii-minuta-do-contrato.pdf | Tratar o reajuste pelo INCC como algo que corre **durante a execução**, contado da data-base da proposta, e não como correção única até o início | Contrato de obra real prevê o reajuste ao longo da vigência; logo o custo pago depende de quando cada parcela é medida | Obra pública (Lei 8.666/93, hoje substituída pela 14.133/21); reajuste **anual**, não mensal por medição; não cobre contrato privado nem a curva de desembolso — a regra da curva em §2.6 é método de Villaça, não desta fonte. **(v1.2) Só apoio:** quando o caso tem proposta de construtora, a fonte primária da periodicidade e da data-base é a cláusula da própria proposta (§2.6) |

Todos os macetes complementam a norma; nenhum a contraria.

## 6. ONDE ESTA SKILL PARA

- Custo da OODC e regra CAB/CAM: `legal-oodc-mais-valera-mais-valia`.
- Fundação em solo mole: `fundacoes-solos-moles-lencol-freatico-barra-recreio` (aqui, só entra como item [NC] fora do CUB).
- Poço de elevador/plataforma e escavação abaixo do NA: `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`.
- Orçamento executivo com quantitativo: `ia-orcamento-executivo-obra` (Lelé), depois do projeto.

## 7. FONTES E O QUE NÃO FOI LIDO

| # | Fonte | Situação |
|---|---|---|
| F1 | ABNT NBR 12721:2006, item 5.7.3 (coeficientes médios) e projetos-padrão R-1 | **Não lida no oficial.** Coeficientes conferidos em reprodução secundária (busca de 02/10/2026) e no M2 |
| F2 | ABNT NBR 14653-2:2011 (método comparativo, item 8.2.1.4.2 sobre fatores) | **Não lida no oficial.** Requisitos do item 8.2.1.4.2 vistos só na apresentação do M4 |
| F3 | Sinduscon-Rio, CUB/m² set/2026 (lista de exclusões) | Lida no primário (Mascaró, 02/10/2026) |
| F4 | Norma do IBAPE/SP para Avaliação de Imóveis Urbanos (2011) | Não lida; citada pelo M4 e pelo M5 |
| F5 | NBR ISO 9386-1 (plataformas de elevação) | Não lida; citada só para nomear a norma da plataforma (título visto em busca de 02/10/2026) |

**Lista de compra (acervo D:\008_Normas ABNT\):** NBR 12721:2006 (versão corrigida vigente) e NBR 14653-2:2011.

## 8. RESSALVAS

- R1: coeficientes e regras da NBR 12721 e da 14653-2 sem leitura do texto oficial.
- R2: fator de oferta calibrado com dado nacional, não local.
- R3: não há fonte citável para o acréscimo de custo do sobrado sobre o R-1: fica [NC].
- R4 (v1.1): não foi achada fonte verificável que descreva literalmente o reajuste por medição mensal na curva de desembolso; o M7 sustenta só o reajuste pelo INCC durante a execução (anual, obra pública). A curva linear/teto no fim é método declarado. (v1.2) No caso concreto, a periodicidade vem da cláusula da proposta do cliente quando ela existe (§2.6).
- R5 (v1.2): a v1.0 desta Skill não tem cópia integral preservada (backups parciais); a partir da v1.1, backup é sempre cópia integral do arquivo antes de editar.

---
*v1.2 (02/10/2026, Villaça): leitura literal da cláusula de reajuste do documento do cliente e conferência de citações do Dossiê (§2.6, §2.8); M7 só apoio; R4 ajustada; R5. Origem: parecer_bardi_v3, Ensaio 003, Etapa 02.*
*v1.1 (02/10/2026, Villaça): reajuste pelo INCC ao longo de todo o cronograma de desembolso (§2.2, §2.6, roteiro item 2); nova §2.7 de custo de moradia pré-obra + obra; macete M7; ressalva R4. Origem: parecer_bardi_v2, Ensaio 003, Etapa 02.*
