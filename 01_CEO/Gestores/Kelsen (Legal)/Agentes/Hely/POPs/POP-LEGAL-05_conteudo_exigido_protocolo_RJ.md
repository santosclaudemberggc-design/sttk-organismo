---
codigo: POP-LEGAL-05
titulo: Conteúdo exigido para protocolo de Projeto Legal — LICIN 2.0, Município do Rio de Janeiro
autor: Hely (Agente executor, equipe do Gestor Legal — Kelsen)
data: 21/07/2026 (1ª redação) · 21/07/2026 — 2ª rodada, vigência e hierarquia normativa (Seções 16 a 19)
escopo: Construção do Zero, uso residencial, subzonas de Recreio dos Bandeirantes e Barra da Tijuca
status: fonte de verdade do que se entrega à prefeitura; sujeito a ratificação de Kelsen
vigencia_verificada_em: 21/07/2026, contra a base oficial Busca Fácil (SMU) — Decreto 55.622/2025 com status "Válido"
---

# POP-LEGAL-05 — O que realmente se entrega à prefeitura do Rio (LICIN 2.0)

## 0. Como ler este documento

Este POP é **fonte de verdade do conteúdo de protocolo**. Regras de leitura:

1. **Toda afirmação aponta artigo e anexo.** Se não aponta, não é afirmação — é lacuna, e está na Seção 12.
2. **Texto literal da norma aparece em citação (`>`) ou entre aspas.** Tudo que não estiver assim é nosso.
3. **Interpretação nossa vem marcada `[INTERPRETAÇÃO]`.** Interpretação nunca é apresentada como texto de lei.
4. **Paráfrase não é fonte** — nem a deste POP, nem a do `_indice_fontes.md`, nem a da Skill. Antes de usar um número ou uma exigência numa decisão real, abra o PDF arquivado.

**Fonte primária deste documento:** `Fontes_Legislacao/Decreto55622_2025_LICIN2.0.pdf`, `..._AnexoI_ModelosDULI.pdf`, `..._AnexoII_TermosDeclaracoes.pdf`, todos baixados de fonte oficial em 21/07/2026 (ver Seção 1). Tudo abaixo foi conferido contra o texto extraído desses arquivos, e os anexos em imagem foram **rasterizados e lidos visualmente**, não inferidos.

---

## 1. Fonte, método e integridade da extração

| Item | Dado |
|---|---|
| Norma | Decreto Rio nº 55.622, de 1º de janeiro de 2025 |
| Ementa | "Dispõe sobre o procedimento de Licenciamento Integrado de Edificações 2.0 - LICIN 2.0, e dá outras providências." |
| Publicação | D.O. RIO 01/01/2025 |
| Autoria do PDF (metadado) | PCRJ/SMU/SUBU/CGPP/GNIU |
| Fonte oficial | Portal SMDU — página "Licenciamento Integrado – LICIN 2.0" (URLs completas abaixo) |
| Método | `curl` direto + `pdftotext -layout -enc UTF-8`; anexos em imagem rasterizados com `pdftoppm -r 200` e lidos visualmente |
| Baixado em | 21/07/2026 |

### Arquivos arquivados

Todos em `Fontes_Legislacao/`, todos com HTTP 200 na data:

1. **Decreto55622_2025_LICIN2.0.pdf** — corpo do decreto — 14 pp. — texto extraível **sim**, exceto pp. 9-11 (imagens).
2. **Decreto55622_2025_AnexoI_ModelosDULI.pdf** — modelos gráficos do DULI — 2 pp. em **A0** — texto extraível **NÃO: imagem pura**.
3. **Decreto55622_2025_AnexoII_TermosDeclaracoes.pdf** — Termos e Declarações — 3 pp. — texto extraível **sim**.
4. **Decreto55622_2025_PublicacaoDO.pdf** — publicação no D.O. de 01/01/2025 — 5 pp. — texto extraível **sim**.

**URLs oficiais.** Host: `desenvolvimentourbano.prefeitura.rio`; página de origem: `/licenciamento-integrado-licin/`; prefixo dos arquivos: `/wp-content/uploads/sites/52/2025/05/`. Nomes de arquivo na origem, na mesma ordem da lista acima:

1. `ato_55622.pdf`
2. `LICIN-2.0-Anexo-I.pdf`
3. `Decreto-RIO-LICIN-2024-Anexo-II-C.pdf`
4. `Decreto-55.622-Versao-DO.pdf`

### Advertências de integridade — ler antes de confiar em qualquer trecho

- **O corpo do decreto sozinho é insuficiente.** Os modelos gráficos do DULI (Anexo I, incisos I e II) **não estão embutidos** no arquivo `ato_55622.pdf`: a p. 5 traz apenas os títulos "I. Modelo padrão..." e "II. Modelo ... para grupamentos:" sem imagem. Os modelos só existem no arquivo separado `LICIN-2.0-Anexo-I.pdf`. Quem baixar só o decreto **não tem os modelos**.
- **O Anexo I (modelos) é imagem pura.** `pdftotext` devolve **2 bytes**. Todo o conteúdo dos modelos transcrito neste POP (Seção 6) foi lido **visualmente** em rasterização a 200 dpi. É transcrição de leitura visual, não extração automática — margem de erro de leitura existe, especialmente em rótulos pequenos.
- **As pp. 9-11 do decreto são imagens** (JPEG em tons de cinza, ~118 ppi) e reproduzem o **Anexo II**, que também existe como arquivo próprio, este sim extraível. Usei o arquivo próprio como fonte do Anexo II.
- **Erro de flate stream** ao processar o Anexo I (`Bad block header in flate stream`, offsets 496241 e 1181876). A rasterização funcionou apesar disso, mas o arquivo tem defeito estrutural. Se um trecho do modelo parecer faltando, suspeitar disso antes de concluir que a norma é omissa.
- **Verificação de identidade:** o PDF baixado hoje tem MD5 `63e5274003eae0c2b29ad60f9bb36cdb`, idêntico ao que já havia sido obtido em 21/07/2026 na compilação da prancha. Mesmo documento, sem divergência de versão.

---

## 2. Arquitetura do procedimento — o que a prefeitura analisa e o que ela não analisa

Esta seção condiciona todo o resto. Sem ela, as exclusões da Seção 4 parecem arbitrárias.

**Art. 2º** define três etapas:

> I - 1ª etapa: preenchimento de requerimento on-line pelo interessado, com a apresentação do Documento Único de Licenciamento Integrado - DULI e documentação indicada no requerimento on-line;
> II - 2ª etapa: validação por técnico habilitado da Secretaria Municipal de Desenvolvimento Urbano e Licenciamento - SMDU do atendimento aos parâmetros projetados e sua compatibilidade com o projeto apresentado; e
> III - 3ª etapa: emissão da Minuta da Licença e Documento de Arrecadação Municipal - DARM, por técnico habilitado da SMDU, quando atendida a legislação.

**Art. 3º** — a lista **fechada** do que o técnico analisa:

> Art. 3º Serão objeto de análise por técnico responsável pelo licenciamento urbanístico, os seguintes parâmetros:
> I - dimensões do lote; II - alinhamento incidente; III - cota de soleira da edificação; IV - taxa de ocupação - TO; V - superfície mínima drenante; VI - área total edificável - ATE; VII - gabarito; VIII - afastamentos; IX - limite de profundidade; X - área coletiva; XI - uso e tipologia; XII - número de unidades permitidas; e XIII - índice de comércio e serviços.

E o parágrafo único transfere todo o resto:

> Parágrafo único. As demais informações sobre o projeto de construção serão de exclusiva responsabilidade do profissional responsável pelo projeto arquitetônico - PRPA, do profissional responsável pela execução das obras - PREO e do requerente do processo de licenciamento, devendo ser objeto de declaração de responsabilidade assinadas por eles.

**Art. 11** é o que torna os anexos vinculantes:

> Art. 11. Todos os pedidos de licença ou legalização formalizados na Subsecretaria de Controle e Licenciamento Urbanístico deverão seguir os padrões de apresentação de projetos e declarações previstos nos Anexos deste Decreto, a partir do momento de sua publicação.

**[INTERPRETAÇÃO]** Os treze incisos do Art. 3º são todos parâmetros de **implantação e volumetria** — nenhum é de arquitetura interna. Isso é a chave de leitura do decreto inteiro: a SMDU deixou de analisar o interior da edificação e passou a analisar o envelope. É por isso que o Anexo I pede contorno cotado e projeção, e não layout. Quem entrega layout não está entregando "a mais" — está entregando o que o Art. 3º diz que não será analisado, e o que a Condição Geral IV.1 diz que não será aceito (Seção 4).

---

## 3. Peças gráficas que entram — Anexo I, inciso III

O Anexo I abre com:

> III. Deverão constar de:

E lista **cinco** rubricas, nesta ordem: **TÍTULO**, **QUADRO DE ÁREAS**, **PLANTA DE SITUAÇÃO**, **PLANTAS DOS PAVIMENTOS**, **CORTES**.

**Não há rubrica de FACHADAS. Não há rubrica de MEMORIAL DESCRITIVO.** Ver Seções 4 e 5.

### 3.1 TÍTULO

> 1- O título do DULI deve conter o tipo de licença, tipo de edificação, uso proposto, número de pavimentos e endereço da obra.
>
> 2- Constará do título a proposição de numeração suplementar e os favores de legislação concessoras de condições especiais, conforme o caso.

O modelo oficial (Anexo I, imagem) traz o título já formatado no carimbo — transcrição literal na Seção 6.3.

### 3.2 QUADRO DE ÁREAS

> 1- A prancha que incluir a planta de situação deve possuir um quadro com os dados do lote, informações do empreendimento e parametrização urbanística conforme o modelo padrão do Documento Único de Licenciamento Integrado - DULI;
>
> 2- O quadro deve ser preenchido com os dados gerais relativos a todo o empreendimento;
>
> 3- O quadro pode ser adaptado e reduzido para conter apenas informações pertinentes ao caso concreto.

> **[ATENÇÃO]** O item 1 fala em **"a prancha que incluir a planta de situação"**. É a única referência do decreto à palavra "prancha" como unidade física, e ela pressupõe que o conjunto possa ter mais de uma. O item 3 autoriza **adaptar e reduzir** o quadro — não autoriza acrescentar campo nem trocar de modelo.

### 3.3 PLANTA DE SITUAÇÃO — 13 itens obrigatórios

> 1- Dimensões do terreno conforme título averbado no Registro de Imóveis, ou de acordo com o PAL de loteamento, desmembramento ou remembramento e as medidas locais quando houver divergência;
>
> 2- Alinhamento, com indicação do nº do PAA e representação do passeio, com indicação da largura;
>
> 3- Indicação de afastamento frontal, limite máximo de profundidade e área coletiva, quando houver;
>
> 4- Nos casos com incidência de recuo e/ou investidura: cotas do lote de origem, do lote remanescente, do recuo, da investidura e áreas correspondentes.
>
> 5- Indicação dos imóveis confrontantes e suas respectivas numerações;
>
> 6- Projeções das edificações, com respectivas cotas, indicando todos os afastamentos em relação às divisas do lote e entre as edificações, PVIs e PVs;
>
> 7- Indicações das projeções das varandas e sacadas balanceadas;
>
> 8- RN do meio-fio do logradouro na testada do terreno e curvas de nível;
>
> 9- Indicação dos acessos à edificação, incluindo solicitação de numeração complementar, se for o caso.
>
> 10- Via interior para acesso de pedestres e veículos, dispensadas as demarcações de vagas;
>
> 11- Em caso de grupamento, deve acompanhar a planta de situação um corte geral do terreno com sua implantação e uma planta de localização do empreendimento;
>
> 12- Cada uma das edificações/blocos do empreendimento devem ser identificados, inclusive existentes, ou qualquer outra construção complementar à edificação principal (guaritas, edículas, telheiros, etc);
>
> 13- Deve acompanhar a planta de situação um quadro descritivo das edificações/blocos integrantes do empreendimento conforme o modelo padrão do Documento Único de Licenciamento Integrado - DULI.

Notas operacionais, todas com endereço:
- O item 1 amarra a dimensão do terreno ao **título averbado no RI ou ao PAL**, e manda representar **medida local quando divergir**. Divergência não impede protocolo — impede omissão.
- O item 6 exige cota de **todos** os afastamentos, inclusive entre edificações, PVIs e PVs. É a peça onde a conferência de afastamento do COES se materializa.
- O item 7 destaca varanda e sacada em projeção — coerente com o COES Art. 8º §3º (1,50 m das divisas no regime não afastado), que é a armadilha já registrada na nossa base.
- O item 11 só se aplica a grupamento; o modelo próprio está na Seção 6.2.

### 3.4 PLANTAS DOS PAVIMENTOS — 8 itens obrigatórios

Rubrica literal, com a enumeração de pavimentos que o próprio decreto faz:

> PLANTAS DOS PAVIMENTOS - Subsolo, embasamento, térreo, pavimento garagem, jirau, PUC, tipo, Cobertura e telhado:

> 1- Limite do lote;
>
> 2- Perímetro do pavimento cotado;
>
> 3- Perímetro da área sujeita a cálculo de ATE;
>
> 4- Projeção do pavimento imediatamente superior;
>
> 5 - Demonstrativo de área de ATC, ATE, varandas e terraços descobertos;
>
> 6- Deve acompanhar a planta dos pavimentos um quadro descritivo do pavimento representado conforme o modelo padrão do Documento Único de Licenciamento Integrado - DULI;
>
> 7- A ocupação do pavimento deve ser descrita seguindo um ou mais dos seguintes tipos:

Os **15 tipos**, literais e na ordem do decreto (no original cada um é precedido de um marcador de círculo preto (Unicode U+25CF)):

| # | Tipo de ocupação, literal |
|---|---|
| 1 | Leitos; |
| 2 | Lojas; |
| 3 | Lojas com dependências; |
| 4 | Quartos; |
| 5 | Salas; |
| 6 | Salas com dependências; |
| 7 | Sobreloja; |
| 8 | Subloja; |
| 9 | Unidades hoteleiras; |
| 10 | Unidades residenciais; |
| 11 | Vagas; |
| 12 | Dependências do condomínio; |
| 13 | Área técnica; |
| 14 | Recreação; |
| 15 | Partes comuns; |

> 8- Em caso de uni/bifamiliar, identificar com o n° da unidade que ocupa o pavimento (casa 1, casa 2, apt. 101, apt. 201, etc).

> **[ATENÇÃO]** **Os oito itens são todos de contorno, área e ocupação. Nenhum deles é de arquitetura interna** — não há exigência de parede interna, porta, janela, mobiliário, cota de compartimento ou nome de ambiente. A lista de "tipos de ocupação" do item 7 é uma classificação de área, não um rótulo de cômodo. Isso é o que sustenta a leitura da Seção 4.

### 3.5 CORTES — 8 itens obrigatórios

> 1- Altura total da edificação, altura do embasamento e altura da lâmina, para efeito do cálculo dos afastamentos, de acordo com o COES;
>
> 2- Altura entre pisos dos pavimentos, até o topo da última laje;
>
> 3- Perfil natural do terreno;
>
> 4- Nível do meio-fio do terreno e cota de soleira;
>
> 5- Desnível do pavimento de subsolo aflorado em relação ao terreno natural no ponto onde a maior porção do subsolo esteja aflorada;
>
> 6- Cota de cortes e aterros nas posições onde estas cotas sejam as maiores previstas;
>
> 7- Deve acompanhar o corte de cada edificação um quadro descritivo das unidades e vagas de cada um dos pavimentos representados conforme o modelo padrão do Documento Único de Licenciamento Integrado - DULI;
>
> 8- O quadro pode ser adaptado e reduzido para conter apenas informações pertinentes ao caso concreto.

Nota: o item 1 é o único ponto do Anexo I que remete **expressamente ao COES** para cálculo de afastamento (embasamento × lâmina). O corte é a peça que prova o afastamento, não a planta.

---

## 4. A Condição Geral IV.1 — o achado central

### 4.1 Texto literal, com o que vem antes e depois

O item não pode ser lido isolado. Transcrição da rubrica inteira, na ordem do documento:

> **IV. Condições gerais:**
>
> 1- Não serão aceitas plantas baixas dos pavimentos, fachadas, e plantas com informações que não interfiram na análise da implantação e volumetria do prédio.
>
> 2- Todo projeto de modificação deverá ser apresentado em cores convencionais, sendo: amarelo para indicar demolição, vermelho para indicar construção nova ou existente a legalizar e preto para indicar existente sem modificação.
>
> 3- Nos casos de projetos de grupamentos, o DULI obedecerá o modelo do inciso I para os projetos das edificações.
>
> 4- Nos casos de modificação sem acréscimo de área em prédio existente, que envolvam ou não desdobramento e/ou unificação de unidades autônomas, ou casos exclusivamente de transformação de uso que não impliquem em adequações com acréscimos de áreas, ficam dispensadas do DULI as plantas e cortes.
>
> 5- Os modelos do DULI serão disponibilizados para consulta através do canal oficial da Secretaria Municipal de Desenvolvimento Urbano e Econômico.

**O que vem imediatamente antes** é a rubrica CORTES, item 8 (Seção 3.5) — ou seja, IV.1 vem logo após o fim da lista de peças exigidas, e funciona como filtro do que **não** entra no mesmo conjunto.

**Varredura de controle.** Contagens no corpus formado pelo decreto integral + Anexo II (32.008 bytes de texto):

| Termo | Ocorrências | Onde |
|---|---|---|
| `fachada` (qualquer flexão) | **1** | exclusivamente em IV.1 |
| `plantas baixas` | **1** | exclusivamente em IV.1 |
| `memorial` | **0** | — |

O termo "fachada" aparece **uma única vez em todo o decreto, e é para recusá-la**. Não há nenhuma outra passagem, em nenhum anexo, exigindo, admitindo ou regulando fachada.

### 4.2 As duas leituras sintáticas

O texto admite, em tese:

- **Leitura (i) — três recusas autônomas:** não se aceita [plantas baixas dos pavimentos] + [fachadas] + [plantas com informações que não interfiram na análise da implantação e volumetria].
- **Leitura (ii) — recusa condicionada:** o critério final ("que não interfiram na análise da implantação e volumetria") qualifica os três itens, de modo que planta baixa e fachada só seriam recusadas quando não interferissem na análise volumétrica.

### 4.3 Qual leitura o contexto sustenta

**A leitura (i) é a que se sustenta.** Quatro fundamentos, do mais formal ao mais sistemático:

**a) Sintático — a oração relativa está encaixada dentro do terceiro item.** A relativa é "que não interfiram", e seu antecedente imediato é "informações", com quem concorda em número. Ela está **dentro** do sintagma "plantas com informações que não interfiram...", não anexada à coordenação como um todo. Uma relativa encaixada no terceiro conjunto não tem alcance sobre o primeiro e o segundo. Para a leitura (ii) valer, o texto precisaria ser algo como "não serão aceitas plantas baixas dos pavimentos, fachadas e plantas, com informações que não interfiram..." — com a relativa destacada da coordenação. Não é o que está escrito. A vírgula antes do "e" reforça o isolamento do terceiro conjunto.

**b) Sistemático — não há rubrica de FACHADAS no inciso III.** As peças exigidas são cinco (Seção 3), e fachada não é uma delas. Sob a leitura (ii), a fachada seria admissível sempre que "interferisse na análise da volumetria" — mas fachada é, por definição, representação de volumetria. A leitura (ii) tornaria a menção a "fachadas" **inerte**: nunca recusaria nada. Norma não se lê de modo a esvaziar as próprias palavras.

**c) Modelo oficial — as plantas do DULI não têm arquitetura interna, e não há fachada nenhuma.** No modelo padrão (Anexo I, inciso I, lido visualmente a 200 dpi), as plantas de pavimento são **contornos hachurados** classificados pela legenda em ATC / ATE / VARANDA / TERRAÇO DESCOBERTO, com cotas de perímetro. Não há parede interna, porta, janela, mobiliário nem nome de ambiente. As vistas presentes são: SITUAÇÃO, PLANTA 1º PAV., PLANTA 2º AO 4º PAV., PLANTA 5º PAV., TELHADO e **um único CORTE**. **Nenhuma fachada.** Como o Art. 11 vincula o pedido ao "padrão de apresentação previsto nos Anexos", o modelo é evidência normativa, não ilustração.

**d) Teleológico — Art. 3º + parágrafo único.** A análise se limita a treze parâmetros de implantação e volumetria, e tudo o mais vira responsabilidade declarada do PRPA/PREO/requerente. Recusar planta baixa e fachada é exatamente coerente com esse desenho: a SMDU não quer receber o que decidiu não analisar.

### 4.4 A objeção séria, e por que ela não derruba a leitura (i)

Há uma tensão aparente: o inciso III **exige** "PLANTAS DOS PAVIMENTOS", e IV.1 **recusa** "plantas baixas dos pavimentos". Contradição?

**Não — os dois termos não são sinônimos no vocabulário do próprio decreto.** "Planta do pavimento", como o inciso III a define (Seção 3.4), é peça de **contorno, área e ocupação**: limite do lote, perímetro cotado, perímetro de ATE, projeção do pavimento superior, demonstrativo de áreas, quadro descritivo e tipo de ocupação. "Planta baixa" é o desenho arquitetônico de distribuição interna. O decreto exige a primeira e recusa a segunda, e o modelo oficial (fundamento "c") mostra exatamente essa peça: pavimento representado sem interior.

**Honestidade sobre o que sobrevive da leitura (ii).** Para o **primeiro** conjunto ("plantas baixas dos pavimentos"), a leitura (ii) não é absurda e produz, na prática, a **mesma regra operacional**: entregue planta de pavimento apenas com informação que interfira na análise volumétrica. As duas leituras **convergem** aqui — não precisamos resolver a sintaxe para saber o que desenhar. Para **fachadas**, as leituras **divergem**, e aí os fundamentos (b), (c) e (d) resolvem contra a admissão da fachada.

**Conclusão operacional:**

| Peça | Entra no DULI? | Base |
|---|---|---|
| Planta de pavimento com contorno, cotas, ATE/ATC, projeção e ocupação | **Sim** | Anexo I, III, PLANTAS DOS PAVIMENTOS, itens 1-8 |
| Planta baixa arquitetônica (layout interno, paredes, aberturas, mobiliário, nome de ambiente) | **Não** | Anexo I, IV, 1 |
| **Fachadas / elevações** | **Não** | Anexo I, IV, 1 + ausência de rubrica no inciso III + ausência no modelo oficial |
| Qualquer planta com informação alheia à implantação/volumetria | **Não** | Anexo I, IV, 1 |
| Cortes | **Sim** | Anexo I, III, CORTES, itens 1-8 |

**[INTERPRETAÇÃO] Risco residual, declarado:** a conclusão sobre fachadas é sólida no texto, no modelo e na finalidade, mas é **nossa leitura** — não há decisão, parecer ou manual da SMDU no nosso acervo confirmando-a. O risco prático de omitir fachada é baixo (a peça não é exigida em lugar nenhum), mas **não é zero** enquanto não houver confirmação da própria SMDU. Recomendo a Kelsen obter essa confirmação antes do primeiro protocolo real (Princípio 18).

> **[RESOLVIDO]** **ATUALIZAÇÃO 21/07/2026 — a recusa foi testada contra a hierarquia normativa e SOBREVIVE.** A pergunta "decreto pode recusar peça que a lei exige?" foi levantada por Claudemberg e investigada. Resposta: o COES (LC 198/2019) e a LUOS/Plano Diretor (LC 270/2024) **não exigem** planta baixa nem fachada como peça do pedido de licenciamento — e a LC 270/2024, **Art. 276, parágrafo único**, delega expressamente ao Poder Executivo os procedimentos de licenciamento. O decreto exerce delegação; não extrapola. **Ver Seção 17**, que é a análise completa. A conclusão da Seção 13 (Planilha de Enviáveis) **não se inverte** — se confirma.

### 4.5 Dispensa adicional — IV.4

Para **modificação sem acréscimo de área**, com ou sem desdobramento/unificação de unidades, e para **transformação de uso** sem acréscimo de área, o item IV.4 dispensa **as plantas e os cortes** do DULI. Restam título, quadro de áreas e planta de situação. Não é o nosso cenário padrão (Construção do Zero), mas é o cenário de menor entrega possível e deve estar mapeado.

---

## 5. Documentos que acompanham

### 5.1 O que o decreto de fato lista

| Documento | Base | Obrigatoriedade |
|---|---|---|
| **DULI** (peça gráfica, modelo do Anexo I) | Art. 2º §2º; Art. 6º p.ú. | **Sempre** |
| **Anexo II — Termos e Declarações** | Art. 6º p.ú. | **Sempre** |
| **Anexo III — Quadro Explicativo de Áreas e Termo de Responsabilidade** | Art. 10, caput | Sempre, **salvo** unifamiliar/bifamiliar |
| **Anexo IV — Quadro Explicativo de Áreas, uni/bifamiliar** | Art. 10, p.ú. | Sempre que unifamiliar ou bifamiliar |
| **Anexo V — Declaração de compatibilidade** | Art. 4º §4º | Condicional, **e não é do protocolo** — é "para o início das obras" |
| "documentação indicada no requerimento on-line" | Art. 2º, I | **Conteúdo não determinável pelo decreto** — ver Seção 12 |

**Art. 10 é o critério escrito de III vs. IV**, e é inequívoco:

> Art. 10. Na análise para o licenciamento de projetos de construção ou modificação de prédio, de acordo com o LICIN 2.0, será adotado Quadro Explicativo de Áreas e termo de responsabilidade, conforme modelo previsto no Anexo III deste Decreto.
> Parágrafo único. No caso de análise para o licenciamento de projetos de construção ou modificação de prédio residencial unifamiliar ou bifamiliar não se aplicam as disposições do caput do art. 10 deste Decreto, devendo ser adotado o Quadro Explicativo de Áreas e termo de responsabilidade, previstos no Anexo IV deste Decreto.

Sobre o **Anexo V**, atenção ao momento — não é peça de protocolo:

> Art. 4º § 4º Para o início das obras, deve ser apresentado, quando for o caso, declaração do PRPA, do PREO e do requerente, informando que as liberações obtidas nos órgãos consultados correspondem ao projeto licenciado, conforme modelo previsto no Anexo V.

### 5.2 O que o decreto **não** exige — resultados negativos

Varredura no corpus (decreto integral + Anexo II):

| Termo | Ocorrências | Leitura |
|---|---|---|
| `RRT` | **0** | O decreto **não menciona RRT em lugar nenhum** |
| `certid` (certidão/certidões) | **0** | Nenhuma certidão é exigida pelo decreto |
| `matríc` (matrícula) | **0** | — |
| `memorial` | **0** | **Memorial descritivo não é peça do LICIN 2.0** |

Sobre **título de propriedade**: a única menção ao Registro de Imóveis no decreto é como **origem da cota do terreno**, não como documento a protocolar:

> 1- Dimensões do terreno conforme título averbado no Registro de Imóveis, ou de acordo com o PAL de loteamento, desmembramento ou remembramento e as medidas locais quando houver divergência; *(Anexo I, III, PLANTA DE SITUAÇÃO, item 1)*

Sobre **responsabilidade técnica**: o decreto não cita RRT nem ART. O que existe é o campo de assinatura no **carimbo do modelo oficial**, com a inscrição do conselho — transcrito na Seção 6.3: "O AUTOR DO PROJETO — CAU/CREA xxxxxxxxxx" e "O RESPONSÁVEL PELA EXECUÇÃO — CAU/CREA xxxxxxxxxx".

**[INTERPRETAÇÃO]** A ausência de RRT/certidão/título na lista do decreto **não significa que não sejam pedidos**: o Art. 2º, I remete expressamente a "documentação indicada no requerimento on-line", que é onde essa lista de fato vive e que não conseguimos ler (Seção 12, L-1). O correto é dizer que **o decreto não é a fonte da lista de documentos anexos** — e não que a lista seja curta. Registrar RRT como "não exigido" seria erro grave; o certo é "não determinável por esta fonte".

### 5.3 Anexo II — conteúdo integral (texto extraível, arquivado)

O Anexo II tem cinco partes. Estrutura e itens:

**I – Declarações gerais** (2 itens): atendimento à legislação em geral, com fundamento no *"§ 2º do art. 281 da LC 270/2024 (Plano Diretor)"*; e número de vagas, com fundamento na LC 270/2024 e LC 198/19 (COES).

**II – Declarações vinculadas à análise do órgão competente** (8 itens, em pares "não se enquadra / se enquadra", com opção **N.A.**), sobre quatro temas:
1. **Sombra sobre o calçadão e/ou areal na orla marítima** — Dec. nº 20504/2001, que regulamentou a Lei nº 47/2000 (itens 1 e 2).
2. **Localizado a menos de 50 metros de curso d'água** (itens 3 e 4).
3. **Remoção de cobertura vegetal passível de autorização e/ou manejo de fauna silvestre** (itens 5 e 6).
4. **Área de alta suscetibilidade a processos geológicos, cortes ou aterros com altura superior a três metros, contenção de taludes, intervenções em depósitos de tálus, ou terrenos com declividade superior a vinte graus** — Art. 457 da LC 270/2024 (itens 7 e 8).

> **[ATENÇÃO]** **Relevância direta para Recreio e Barra:** o tema 1 (sombra sobre calçadão/areal da orla) e o tema 2 (50 m de curso d'água) são geograficamente sensíveis e ambos os bairros são orla e cortados por canais/lagoas. Este é o **único ponto de todo o decreto onde a localização do lote altera o que se entrega** — e ainda assim não por bairro, mas por condição física do terreno. Ver Seção 8.

**III – Declarações específicas** (9 itens), com os respectivos fundamentos citados no próprio anexo:
1. Reservatórios de retardo e acumulação de águas pluviais — Decreto nº 23940 de 30/01/2004 e Resolução Conjunta SMG/SMO/SMU Nº 001/05.
2. Normas de segurança e saúde do trabalho — inciso IV do § 3º do Art. 1º da LC 198/19 (COES).
3. Varanda que ultrapassa 20% da área útil computada na ATE — §5º do Art. 8º da LC 198/19 (COES).
4. Acessibilidade — Decreto nº 22705/2003.
5. Passivo ambiental — § 2º do Art. 1º da Resolução SMAC nº 605/2015.
6. Normas da Secretaria Municipal de Saúde — Decreto nº 45585/2018.
7. Cortes e aterros em encosta — Inciso I do Art. 456 da LC 270/2024.
8. Condições de sustentabilidade — § 4º do Art. 1º da LC 198/19 (COES) e LC 270/2024.
9. Vias interiores e viradouros de grupamento — Seção II do Capítulo IV da LC 270/2024.

**IV – Declarações de responsabilidade** (2): responsabilidade civil do proprietário; termo de responsabilidade profissional. Assinam: **Proprietário, PRPA e PREO**.

**V – Instrução de preenchimento e apresentação** (3 itens). Os dois que mudam a operação:

> 2 - Nas declarações vinculadas a parecer, deve-se selecionar uma única opção para cada tema, indicando se o projeto se enquadra ou não nas situações descritas, e, quando aplicável, comprometer-se a apresentar a análise correspondente.

> 3 - Ao marcar "Não se Aplica (N.A.)", o proprietário, o Profissional Responsável pelo Projeto de Arquitetura (PRPA) e o Profissional Responsável pela Execução da Obra (PREO) declaram, sob as penas da lei, que o projeto não se enquadra em nenhuma das situações previstas na respectiva declaração e que atende completamente à legislação específica referente ao tema, assumindo, ainda, total responsabilidade pelas implicações técnicas e legais decorrentes dessa afirmação.

> **[ATENÇÃO]** **Uma única opção por tema.** Marcar as duas, ou deixar em branco, é vício formal. E "N.A." **não é campo neutro** — é declaração de responsabilidade plena sob as penas da lei. Isso é ponto de conferência antes de qualquer assinatura (Princípio 18).

---

## 6. O modelo oficial do DULI — transcrição por leitura visual

> **[ATENÇÃO]** **Toda esta seção é transcrição de leitura visual** de `Decreto55622_2025_AnexoI_ModelosDULI.pdf`, rasterizado a 200 dpi. O arquivo não tem camada de texto. Rótulos foram lidos ampliados; erros de leitura são possíveis e devem ser conferidos contra o PDF antes de uso em protocolo real.

O Anexo I tem **dois** modelos, ambos em **uma única prancha** cada, numeradas "N. PRANCHA 01":
- **Inciso I** — modelo padrão (edificação);
- **Inciso II** — modelo para projetos de grupamentos.

### 6.1 Modelo padrão (inciso I)

**Vistas presentes e escalas indicadas no próprio modelo:**

| Vista | Escala indicada |
|---|---|
| 1 SITUAÇÃO | 1:200 |
| 2 PLANTA 1º PAV. | 1:100 |
| 3 PLANTA 2º AO 4º PAV. | 1:100 |
| 4 PLANTA 5º PAV. | (não legível na rasterização) |
| 5 TELHADO | 1:100 |
| 6 CORTE | 1:100 |

**LEGENDA** (quatro hachuras): `ATC` · `ATE` · `VARANDA` · `TERRAÇO DESCOBERTO`

**Caixa que acompanha cada planta de pavimento:**

> OCUPAÇÃO:
> (PREENCHER CONFORME O TEXTO PADRÃO DO ANEXO I)
> ÁREAS (m²): | ATE: | ATC: | VARANDAS: |

**Tabela DADOS DO LOTE** — linhas, na ordem: `TERRENO ORIGINAL (m²)` · `RECUO (m²)` · `INVESTIDURA (m²)` · `REMANESCENTE (m²)`

**Tabela INFORMAÇÕES DO EMPREENDIMENTO** — quatro blocos:

| Bloco | Colunas | Linhas |
|---|---|---|
| ÁREAS | EXISTENTE / ACRÉSCIMO / DECRÉSCIMO / TOTAL | ATC (m²) · ATE (m²) |
| UNIDADES | EXISTENTE / PROJETADO | RESIDENCIAIS · SALAS · LOJAS |
| VAGAS | COBERTAS / DESCOBERTAS | (linha única) |
| VIA INTERNA | LARGURA (m) / CUMPRIMENTO (m) | (linha única) |

> **[ATENÇÃO]** `CUMPRIMENTO (m)` está assim no original — erro de grafia da própria Prefeitura para "COMPRIMENTO". Transcrito literalmente. Não "corrigir" ao reproduzir o quadro sem decisão de Kelsen.

**Tabela PARAMETRIZAÇÃO URBANÍSTICA** — cabeçalho `ZONEAMENTO` / `SIGLA DA ZONA`; depois `PARÂMETRO` com colunas `PERMITIDO` e `PROJETADO`:

`T.O. (%)` · `S.M.D. (%)` · `ATE (m²)` · `ATE MÁXIMO DE USO COMERCIAL` · `Nº MÁXIMO DE UNIDADES RESIDENCIAIS`

> **[ATENÇÃO]** **Este quadro tem apenas cinco parâmetros — e o Art. 3º analisa treze.** Não há linha para gabarito, afastamentos, cota de soleira, limite de profundidade, área coletiva ou ICS. Ver Seção 12, L-4.

**Tabela EDIFICAÇÕES/BLOCOS** — colunas: `IDENTIFICAÇÃO` | `UNIDADES (Nº)` [`RES.` `SAL.` `LOJ.`] | `PAV.` | `VAGAS (Nº)` [`COB.` `DESC.`] | `ATE (m²)` | `ATC (m²)`. Linha de exemplo rotulada `(IDENTIFICAR BLOCO)`, mais linha final `VAGAS EXTERNAS`.

**Tabela UNIDADES / VAGAS** (junto ao corte) — linhas por pavimento no formato `RESIDENCIAIS: Nº`, e ao final `SALAS: Nº` / `COBERTAS: Nº`, `LOJAS: Nº` / `COBERTAS: Nº` e `DESCOBERTAS: Nº`, encerrando em `TOTAL:` / `TOTAL:`.

### 6.2 Modelo de grupamento (inciso II)

Vistas: **1 SITUAÇÃO**, **2 LOCALIZAÇÃO**, **3 CORTE** (corte geral do terreno). Confirma na prática o Anexo I, III, PLANTA DE SITUAÇÃO, item 11. Blocos identificados individualmente (BLOCO 1 a 4), além de `GUARITA`, `EDÍCULA` e `CASTELO D'ÁGUA` — o que materializa o item 12 ("guaritas, edículas, telheiros, etc"). Traz as mesmas tabelas do modelo padrão, com a EDIFICAÇÕES/BLOCOS preenchida por bloco.

Título do carimbo neste modelo:

> PROJETO PARA CONSTRUÇÃO DE GRUPAMENTO (ESPECIFICAR O TIPO) SITUADO NA (INCLUIR NOME DO LOGRADOURO) (INCLUIR Nº) - (NOME DO BAIRRO) - (Nº DA R.A.)

### 6.3 Carimbo — transcrição literal

Título, no modelo padrão:

> PROJETO PARA CONSTRUÇÃO DE PRÉDIO (ESPECIFICAR O TIPO) COM (INCLUIR Nº) PAVIMENTOS SITUADO NA (INCLUIR NOME DO LOGRADOURO) (INCLUIR Nº) - (NOME DO BAIRRO) - (Nº DA R.A.)

Faixa de identificação:

> ESCALA: INDICADA | DATA: / / | N. PRANCHA: **01** | **DULI - ANEXO I - LICIN 2.0**

Assinaturas — **três**, nesta ordem (o modelo preenche os nomes com `xxxxx`):

| # | Rótulo, literal | Inscrição no conselho |
|---|---|---|
| 1 | O PROPRIETÁRIO | (sem campo) |
| 2 | O AUTOR DO PROJETO | CAU/CREA xxxxxxxxxx |
| 3 | O RESPONSÁVEL PELA EXECUÇÃO | CAU/CREA xxxxxxxxxx |

Campos finais: `N. DO PROCESSO` | `OBSERVACOES` *(sem cedilha e sem acento no original)*.

> **[ATENÇÃO]** **O carimbo tem três assinaturas — proprietário, autor do projeto e responsável pela execução.** Não há campo de RRT/ART, apenas o número de inscrição no conselho. E a existência do campo "O RESPONSÁVEL PELA EXECUÇÃO" no próprio DULI significa que **o PREO precisa estar definido já no protocolo**, não só no início da obra. Ponto de atenção para o nosso fluxo, onde o construtor pode ainda não estar contratado.

---

## 7. Anexo III — as três subtabelas, transcritas na íntegra

Conferido **visualmente** contra a p. 12 do decreto rasterizada: a extração de texto é fiel e completa; o Anexo III é curto mesmo. Cabeçalho literal:

> **ANEXO III**
> **Quadro Explicativo de Áreas e Termo de Responsabilidade.**

> **Nota de transcrição:** no original, cada campo é precedido de um marcador de círculo vazado (Unicode U+25E6). Reproduzo os campos em tabela, uma linha por campo, para preservar **ordem, rótulo e pontuação exatos** — o marcador em si não é conteúdo. Nada foi resumido, agrupado ou reordenado.

### Subtabela 1 — título literal: `1. PROJETO RESIDENCIAL MULTIFAMILIAR / GRUPAMENTO / MISTO`

| # | Campo, literal |
|---|---|
| 1 | Área privativa de cada unidade (com paredes externas); |
| 2 | Terraços descobertos; |

### Subtabela 2 — título literal: `2. PROJETO DE USO EXCLUSIVO / INDUSTRIAL`

| # | Campo, literal |
|---|---|
| 1 | Edificação principal / Galpões; |
| 2 | Telheiro / Cobertura Bombas Gasolina; |
| 3 | Quadras de esportes (Cobertas ou Descobertas); |
| 4 | Piscina |
| 5 | Estacionamento coberto |

> **[ATENÇÃO]** Os campos 4 e 5 **não têm ponto e vírgula final no original** — os três primeiros têm. Transcrito como está.

### Subtabela 3 — título literal: `3. PROJETO DE EDIFICAÇÃO COMERCIAL`

| # | Campo, literal |
|---|---|
| 1 | Área privativa de cada unidade; |
| 2 | Jirau / Mezanino; |
| 3 | Terraços descobertos; |
| 4 | Varandas / Sacadas; |
| 5 | Estacionamento Coberto. |

### Termo de Responsabilidade do Anexo III — literal

> Os abaixo assinados, respectivamente, proprietário ou adquirente e autor do projeto, declaram que assumem, cada um, individualmente, total responsabilidade pela veracidade das informações contidas no quadro explicativo de áreas, sujeitando-se à aplicação das leis e regulamentos pertinentes, em caso de inexatidão dos dados declarados.

Seguem, no original, duas linhas de assinatura:

| Linha de assinatura | Rótulo, literal |
|---|---|
| `_______________________________` | PROPRIETÁRIO OU ADQUIRENTE |
| `_______________________________` | AUTOR DO PROJETO |

> **[ATENÇÃO]** Assinam **dois** — proprietário/adquirente e autor do projeto. **O PREO não assina o Anexo III**, embora assine o Anexo II e conste do carimbo do DULI. Três peças, três conjuntos de signatários diferentes.

### 7.1 Observação estrutural sobre as três subtabelas

As listas são curtas demais para serem quadros de áreas completos — a subtabela 1 tem **dois** campos, e não contempla ATE, ATC, vagas nem partes comuns, que são indispensáveis a um multifamiliar.

**[INTERPRETAÇÃO]** As três subtabelas do Anexo III **não são quadros de áreas autônomos**: são listas dos itens de área **adicionais** que devem constar do quadro conforme o tipo de projeto. O quadro-base é o do modelo padrão do DULI (Seção 6.1: DADOS DO LOTE + INFORMAÇÕES DO EMPREENDIMENTO + PARAMETRIZAÇÃO URBANÍSTICA), para o qual o Anexo I, III, QUADRO DE ÁREAS, item 1 remete expressamente. Contra a leitura de que seriam quadros completos: nenhuma das três lista ATE ou ATC, e sem esses dois não há como analisar o Art. 3º, VI. Isso é leitura nossa — o decreto não diz isso com essas palavras.

### 7.2 Critério de escolha entre as três — **não está escrito na norma**

Procurei critério de seleção em todo o corpus. **Não existe.** O Art. 10 resolve apenas **Anexo III vs. Anexo IV** (Seção 5.1); dentro do Anexo III, os três títulos são rótulos de tipo de projeto sem definição, sem regra de prevalência e sem remissão a nenhuma classificação de uso. Especificamente:

- O decreto **não define** "uso exclusivo".
- O decreto **não remete** à classificação de usos da LC 270/2024 nem ao Decreto 56.561/2025 para escolher a subtabela.
- **Não há** regra para o caso em que mais de uma subtabela caiba.

> **[RESOLVIDO]** **CORREÇÃO 21/07/2026 — o decreto não define, mas o COES define, e isso muda o status desta seção.** Ao varrer o COES para a Pergunta 2 (Seção 17), localizei a definição legal que faltava. **LC 198/2019 (COES), Art. 2º, III:**
>
> > III - Edificação não residencial: destinada a abrigar os usos industrial, comercial, de armazenagem e de serviços, podendo ser: a) **edificação de uso exclusivo: destinada a abrigar um único uso ou atividade não residencial por lote, apresentando uma única numeração**; b) **edificação constituída por unidades autônomas: edificação destinada a abrigar usos e atividades não residenciais, apresentando mais de uma unidade autônoma.**
>
> O COES parte a edificação não residencial em exatamente **duas** espécies, e os nomes coincidem com os rótulos das subtabelas 2 e 3 do Anexo III. O critério que eu havia proposto abaixo como interpretação nossa — **estabelecimento único -> subtabela 2; unidades autônomas -> subtabela 3** — **é o critério legal do COES**, não invenção nossa. Deixa de ser [INTERPRETAÇÃO] pura e passa a ter endereço: **COES Art. 2º, III, "a" e "b"**.
>
> **Ressalva honesta, que impede fechar a lacuna por completo:** o Decreto 55.622/2025 **não remete** expressamente ao Art. 2º do COES para escolher a subtabela. A ponte entre os dois textos continua sendo nossa. Mas agora é ponte entre dois textos legais que usam o mesmo vocabulário, e não critério construído do zero — o que é qualitativamente diferente. **A lacuna L-6 fica rebaixada, não eliminada** (ver Seção 12).
>
> Aplicado ao caso S-II (clínica): clínica que ocupa sozinha toda a edificação, com numeração única -> **uso exclusivo -> subtabela 2**. Clínica em sala de edifício de salas -> **unidades autônomas -> subtabela 3**. O desempate que a norma "não dava" passa a existir por remissão sistemática.

Isso confirma, contra o texto, a pendência aberta de Kelsen sobre o caso S-II (clínica, CNAE 86.3): as subtabelas 2 e 3 são ambas defensáveis e **a norma não desempata**.

**[INTERPRETAÇÃO] — critério que eu defenderia, marcado como interpretação e não como texto de lei:**

O discriminante não é o CNAE nem a categoria de uso, e sim a **estrutura de ocupação da edificação**, porque é isso que os campos de cada subtabela revelam:

1. A subtabela 3 (comercial) pede *"Área privativa de cada unidade"*, *"Jirau / Mezanino"*, *"Varandas / Sacadas"* — vocabulário de edificação **subdividida em unidades autônomas** (salas/lojas), destinadas a titulares distintos.
2. A subtabela 2 (uso exclusivo/industrial) pede *"Edificação principal / Galpões"*, *"Telheiro"*, *"Quadras de esportes"*, *"Piscina"* — vocabulário de edificação **ocupada por um único estabelecimento**, descrita por corpos construídos, não por unidades.

Critério proposto: **se a edificação é ocupada integralmente por um único estabelecimento, aplica-se a subtabela 2; se é subdividida em unidades autônomas comercializáveis, aplica-se a subtabela 3.** Aplicado ao caso da clínica: clínica que ocupa sozinha toda a edificação -> subtabela 2; clínica que ocupa uma sala dentro de um edifício de salas -> subtabela 3 (e o quadro é do edifício, não da clínica).

**Regra prática de segurança, também interpretação:** havendo dúvida real, declarar a **união** dos itens aplicáveis. Nada no decreto proíbe declarar item de área a mais, e o Termo de Responsabilidade do Anexo III versa sobre **veracidade**, não sobre economia de campos. Omitir área é risco; declarar área verdadeira a mais, não.

**Este critério é nosso, não da Prefeitura.** Kelsen decide se adotamos como padrão interno (Princípio 9) e se vale confirmar com a SMDU.

---

## 8. Anexo IV — e a diferença de uso entre III e IV

**O Anexo IV não tem subtabelas.** É **uma única tabela**, com dois blocos. Verificado visualmente na p. 13 rasterizada — necessário, porque a extração `pdftotext -layout` **embaralhou a ordem** dos rótulos neste anexo (o campo "Unidade" e o cabeçalho "Número de Compartimentos" saíram fora de posição). A transcrição abaixo é a da imagem, que é a correta.

Cabeçalho literal:

> **ANEXO IV**
> **Quadro Explicativo de Áreas e Termo de Responsabilidade - Edificações Uni ou Bifamiliares.**

**Bloco 1 — cabeçalho `Área (m²)`, com campo `Unidade:______________`**, linhas na ordem:

| # | Linha, literal |
|---|---|
| 1 | Edificação principal |
| 2 | Varanda / Sacada |
| 3 | Terraços descobertos |
| 4 | Terraços cobertos |
| 5 | Garagem coberta |
| 6 | Edículas |
| 7 | Telheiro |
| 8 | Quadra coberta |
| 9 | Quadra descoberta |
| 10 | Subsolo |
| 11 | Piscina |

**Bloco 2 — cabeçalho `Número de Compartimentos`**, linhas na ordem:

| # | Linha, literal |
|---|---|
| 1 | Sala |
| 2 | Quarto |
| 3 | Banheiro |
| 4 | Cozinha |
| 5 | Outros |
| 6 | Vaga de veículo |

Segue o mesmo Termo de Responsabilidade do Anexo III, com os mesmos dois signatários.

### Diferença de uso entre III e IV

| | Anexo III | Anexo IV |
|---|---|---|
| Quando | Construção ou modificação de prédio, **regra geral** | Residencial **unifamiliar ou bifamiliar** |
| Base | Art. 10, caput | Art. 10, parágrafo único |
| Forma | Três listas de itens por tipo de projeto | Tabela única, dois blocos |
| Subtabelas | Três | Nenhuma |
| Pede nº de compartimentos | Não | **Sim** (Sala, Quarto, Banheiro, Cozinha, Outros, Vaga) |
| Signatários | Proprietário/adquirente + autor | Idênticos |

> **[ATENÇÃO]** **Para o nosso escopo (Construção do Zero, residencial), o Anexo IV é o caso padrão** — casa unifamiliar. O Anexo III entra quando o projeto for multifamiliar, grupamento ou misto.

**[INTERPRETAÇÃO] — e uma ironia operacional que vale registrar:** o Anexo IV é o único lugar do procedimento que pede **número de compartimentos por tipo** (quantas salas, quantos quartos, quantos banheiros). Ou seja: a informação sobre o interior da casa é prestada **em tabela declaratória**, não em desenho — exatamente coerente com a recusa da planta baixa em IV.1 (Seção 4). A Prefeitura quer o dado, não o desenho do dado. Isso reforça a leitura (i).

---

## 9. O que muda por subzona em Recreio dos Bandeirantes e Barra da Tijuca

**Não muda nada. O Decreto 55.622/2025 é integralmente neutro quanto a bairro, zona e subzona.**

Evidência da varredura, no corpus decreto integral + Anexo II (32.008 bytes de texto extraído):

| Termo buscado | Ocorrências |
|---|---|
| `Recreio` | **0** |
| `Barra da Tijuca` | **0** |
| `Barra` | **0** |
| `AP4` / `AP-4` / `AP 4` | **0** / **0** / **0** |
| `subzona` | **0** |
| `bairro` | **0** |
| `zona` | **0** |
| `zoneamento` | **0** |

**Nenhuma ocorrência de nenhum dos termos.** Não há regra de protocolo diferenciada por localização, nem para Recreio, nem para a Barra, nem para qualquer outro bairro.

**Duas ressalvas honestas, que não alteram a conclusão mas precisam constar:**

1. **A palavra "bairro" e o vocabulário de zoneamento aparecem nos modelos em imagem**, que não entram na contagem de texto: o carimbo tem o campo `(NOME DO BAIRRO) - (Nº DA R.A.)` e a tabela PARAMETRIZAÇÃO URBANÍSTICA tem `ZONEAMENTO` e `SIGLA DA ZONA`. São **campos a preencher**, não regras diferenciadas. O bairro é identificação; a zona é um dado declarado. **O que se entrega é idêntico em toda a cidade — o que se preenche é que muda.**
2. **A única sensibilidade geográfica real do procedimento está no Anexo II, II** (Seção 5.3): os temas de **sombra sobre calçadão/areal da orla** e **50 m de curso d'água** são condicionantes fáticas, e Recreio e Barra são orla marítima cortada por canais e lagoas. Não é regra por subzona — é regra por **condição física do lote**, que ali se realiza com frequência. Na prática, é o ponto do Anexo II que mais exige atenção nos nossos dois bairros.

**Consequência para o processo — resultado negativo que simplifica:** não precisamos manter variação de checklist de protocolo por bairro. **O conteúdo do que se entrega é único.** A variação por subzona permanece inteira do lado dos **parâmetros urbanísticos** (CAB, CAM, TO, gabarito, afastamentos, lote mínimo, ICS, SMD — LC 270/2024 e COES), que são o que se **declara dentro** das peças, e continuam regidos pela Skill `legal-base-legislativa-bairro` e pelo POP-LEGAL-RIU-01. Um checklist, muitos parâmetros.

---

## 10. Convenção gráfica de cores — e o que vale para obra nova

Texto literal, íntegro (Anexo I, IV, item 2):

> 2- Todo projeto de modificação deverá ser apresentado em cores convencionais, sendo: amarelo para indicar demolição, vermelho para indicar construção nova ou existente a legalizar e preto para indicar existente sem modificação.

| Cor | Significado (literal) |
|---|---|
| Amarelo | demolição |
| Vermelho | construção nova **ou** existente a legalizar |
| Preto | existente sem modificação |

**Varredura de controle** — no corpus inteiro: `cores` = 1, `convencion` = 1, `amarelo` = 1, `demoli` = 1. **A regra de cor aparece uma única vez em todo o decreto.** Não há segunda regra gráfica em outro anexo, com outra redação. Também confirmei no **COES** (LC 198/2019, arquivado): `cores convencionais` = 0, `amarelo` = 0 — o COES não tem convenção de cor.

### Resposta à pendência: obra nova

**A norma é SILENTE quanto à obra nova.** A hipótese de incidência do item 2 é expressa e restrita: *"Todo projeto de **modificação**"*. Um projeto de construção nova em lote sem preexistência não é projeto de modificação, e **nenhum dispositivo do decreto lhe impõe convenção de cor**.

"Silente" é a resposta correta, e é resposta legítima — não é lacuna de pesquisa minha.

**[INTERPRETAÇÃO]**, com o raciocínio à mostra: a convenção de cores é **diferencial** — existe para distinguir três estados (o que sai, o que entra, o que fica) numa mesma peça. Em obra nova não há preexistência a diferenciar: **tudo** seria "construção nova", logo tudo seria vermelho, e uma prancha inteiramente vermelha não transmite informação alguma. A ausência de regra para obra nova é coerente com a função do dispositivo, não um esquecimento do legislador.

**Aplicação ao nosso cenário de demolição total + obra nova.** Conforme já registrado no **POP-LEGAL-03**, demolição total é **processo próprio**, separado do licenciamento da edificação nova. Nesse arranjo o DULI da obra nova **não representa demolição alguma** — a demolição é objeto do outro processo. Logo não há amarelo a aplicar, e a pendência **se resolve**: obra nova, ainda que precedida de demolição total em processo apartado, não atrai o item IV.2.

**A pendência só permanece em um cenário:** demolição **parcial** com acréscimo — aí há preexistência, há demolição e há construção nova na mesma peça, e o projeto é de **modificação**: o item IV.2 incide integralmente, com as três cores. Fora do nosso escopo padrão de Construção do Zero, mas mapeado.

**Recomendação a Kelsen:** adotar, em obra nova, representação monocromática preta, por ser o padrão de desenho técnico e por não haver regra em contrário. **[INTERPRETAÇÃO]** — o decreto não determina isso; determina apenas que a regra das três cores não se aplica. Kelsen ratifica.

**Propagado em 08/08/2026:** esta seção já estava alinhada com a decisão formal de Kelsen no `POP-GESTOR-LEGAL-01`, seção 3.6 (23/07/2026) — que decidiu no mesmo sentido (obra nova não atrai a convenção de cores; demolição total é processo apartado via `POP-LEGAL-03`) e resolveu, adicionalmente, o cenário de demolição total + obra nova no mesmo caso, que esta seção não cobria explicitamente. Nenhuma mudança de conclusão, só referência cruzada formal entre os dois documentos.

---

## 11. Formato de prancha, escala e nomenclatura

**O decreto não fixa formato de papel.** Varredura no corpus: `escala` = 0, `formato` = 0, `A1` = 0, `A0` = 0, `NBR` = 0, `ABNT` = 0. **Zero ocorrência de todos.** Isso confirma, agora com fonte primária arquivada, a pendência que estava aberta desde 20/07/2026: **não há base normativa para "A1 obrigatório" — nem para nenhum outro formato.**

O que **existe**, e é o mais próximo de uma referência de formato:

- O arquivo oficial dos modelos (`LICIN-2.0-Anexo-I.pdf`) tem página de **2383,94 × 3370,39 pt = 841 × 1189 mm = A0**, nas duas páginas.
- O carimbo do modelo traz **`ESCALA: INDICADA`** e **`N. PRANCHA 01`**.
- As escalas usadas no modelo padrão são **1:200 na situação** e **1:100 nas plantas, telhado e corte** (Seção 6.1).

**[INTERPRETAÇÃO]** O tamanho A0 é o formato em que a Prefeitura **distribui o modelo**, e não uma exigência declarada — não há artigo que o imponha ao projeto do administrado. O que o Art. 11 vincula é o *"padrão de apresentação"* dos anexos, expressão que o decreto não define e que tanto pode alcançar o formato quanto limitar-se ao conteúdo e à diagramação. Sustento que a evidência **mais forte** disponível hoje aponta para A0 — é o formato do próprio modelo oficial, e não temos nenhuma fonte apontando A1. Mas isto é inferência a partir do arquivo, não texto de norma.

> **[ATENÇÃO]** **Isto contradiz a premissa operacional usada na prancha gerada em 21/07/2026**, que saiu em **A1 paisagem** por NBR 10068 e prática de mercado, com a ausência de base declarada na época. Agora sabemos que o único indício documental existente aponta **A0**, não A1. **Não alterei a prancha nem o caso-teste** — a decisão é de Kelsen. Registro como divergência a resolver antes de qualquer protocolo real.

**Nomenclatura de arquivo:** o decreto é silente. O carimbo do modelo rotula a prancha como **`DULI - ANEXO I - LICIN 2.0`**, o que é o mais próximo de uma identificação padronizada que a norma oferece.

---

## 12. LACUNAS EXPLÍCITAS

O que **não** consegui confirmar. Registrar lacuna é entrega; preencher com plausível seria defeito.

**L-1 — A lista de documentos do requerimento on-line é inacessível. É a maior lacuna deste POP.**
O Art. 2º, I remete a *"documentação indicada no requerimento on-line"*. Essa lista **não está no decreto nem em nenhum anexo**. A página oficial do LICIN diz apenas que "o pedido de licença e a documentação necessária para a abertura dos processos" estão no sistema. Tentei `https://requerimentossmu.rio.rj.gov.br/` — devolve HTTP 200 com **957 bytes**, aplicação JavaScript sem conteúdo público; a lista está atrás de autenticação. **Consequência: não sei, por fonte primária, se RRT/ART, título de propriedade, certidões, procuração ou documento de identidade são exigidos no protocolo, nem em que hipóteses.** As zero ocorrências dessas palavras no decreto (Seção 5.2) provam que **o decreto não é a fonte** dessa exigência — não provam que a exigência não exista. Precisa de acesso autenticado ao sistema, ou de um protocolo real observado.

**L-2 — Os modelos do DULI só existem como imagem, e o arquivo tem defeito estrutural.**
Toda a Seção 6 é leitura visual, não extração. Rótulos pequenos podem ter sido lidos errado. A escala da vista "PLANTA 5º PAV." não foi legível na rasterização. Além disso o PDF acusa `Bad block header in flate stream` em dois offsets. Não descarto que haja conteúdo no modelo que eu não tenha visto.

**L-3 — **[RESOLVIDO]** FECHADA em 21/07/2026. Não há norma posterior alterando o Decreto 55.622/2025.**
Verificado em **fonte oficial da própria SMU** — base "Busca Fácil" da Subsecretaria de Planejamento Urbano (`www2.rio.rj.gov.br/smu/buscafacil`), que publica **status jurídico** e serve **texto consolidado** de cada ato. Resultados na data:

| Ato | Status oficial | Observação registrada pela SMU |
|---|---|---|
| **Decreto 55.622/2025 (LICIN 2.0)** | **Válido** | sem nota de alteração |
| Decreto 48.719/2021 (LICIN 1.0) | **Sem efeito** | "SEM EFEITO EM FUNÇÃO DA PUBLICAÇÃO DO DECRETO 55622 DE 1º DE JANEIRO DE 2025 (LICIN 2.0)" |
| Resolução SMDEIS 27/2021 (baixa complexidade) | **Sem efeito** | mesma nota, literalmente idêntica |

Além disso, **busca por texto integral** sobre toda a base legislativa urbanística municipal (145 leis complementares e o acervo de decretos e resoluções cadastrado) devolveu, para o termo `DULI`, **um único ato: o Decreto 55.622/2025**; e para `LICIN`, 17 atos, **nenhum deles posterior a 01/01/2025**. Não há resolução, decreto ou lei posterior regulando o LICIN 2.0.

**Resolvida também a suspeita sobre o nome do arquivo:** `Decreto-RIO-LICIN-2024-Anexo-II-C.pdf` é apenas nome de arquivo mal rotulado no servidor da SMDU. O conteúdo confere com o Anexo II do Decreto 55.622/2025 e o MD5 do corpo do decreto é estável. **Não há versionamento oculto.**

> **[ATENÇÃO]** O que esta lacuna fechada **não** cobre: a lista de documentos do requerimento on-line (L-1) continua fora do decreto e fora desta verificação. Vigência confirmada não é o mesmo que conteúdo conhecido.

**L-4 — O quadro PARAMETRIZAÇÃO URBANÍSTICA do modelo tem 5 parâmetros; o Art. 3º analisa 13.**
Faltam no quadro: gabarito, afastamentos, cota de soleira, limite de profundidade, área coletiva, dimensões do lote, alinhamento, uso e tipologia, ICS. **Não sei como esses oito são declarados** — se em campos livres da prancha, se pela cotagem das peças gráficas, se no requerimento on-line (L-1), ou se o Anexo I, III, QUADRO DE ÁREAS, item 3 ("pode ser adaptado e reduzido") admite a leitura oposta, de que também pode ser **ampliado**. O item 3 fala em "adaptado e reduzido"; ampliação não está escrita. Lacuna real e operacionalmente relevante.

**L-5 — "Padrão de apresentação" do Art. 11 não é definido.**
Sem definição, não sei se a vinculação alcança formato de papel, espessura de linha, fonte, ou apenas o conteúdo e a diagramação dos quadros. É a lacuna que sustenta a indefinição de formato da Seção 11.

**L-6 — FECHADA COMO DECISÃO ADOTADA em 08/08/2026 (propagada do `POP-GESTOR-LEGAL-01`, seção 3.5, decidido por Kelsen em 23/07/2026). Deixa de ser lacuna aberta e passa a ser critério de trabalho da casa, com a ressalva mantida.**
O Decreto 55.622/2025 continua sem regra de escolha entre as três subtabelas do Anexo III — a varredura negativa da Seção 7.2 permanece válida. O COES, Art. 2º, III, "a" e "b", define legalmente "edificação de uso exclusivo" (um único uso/atividade por lote, numeração única) em oposição a "edificação constituída por unidades autônomas", e esses são exatamente os dois vocabulários das subtabelas 2 e 3. **Decisão adotada por Kelsen:** no escopo declarado da Sttickler (Construção do Zero, residencial unifamiliar), a pergunta nem se coloca — o Art. 10, parágrafo único, manda usar o Anexo IV, sem subtabelas; peça montada sobre o Anexo III num caso unifamiliar é erro de enquadramento e barra a etapa. **Fora do escopo padrão** (caso não residencial), o critério é o COES Art. 2º, III, "a"/"b": uso exclusivo -> subtabela 2; unidades autônomas -> subtabela 3. **A ressalva não foi eliminada pela decisão, só deixou de bloquear o trabalho:** o decreto não manda ler o Art. 2º do COES — a ponte entre os dois textos continua sendo nossa, defensável mas não é a norma desempatando. Por isso a decisão exige **declarar o enquadramento escolhido na própria peça**, e todo caso não residencial real sobe como ressalva (seção 5 do `POP-GESTOR-LEGAL-01`), nunca em silêncio. Ver Seção 7.2.

**L-6-b — Falta saber se a SMDU aceita a "união de itens" do Anexo III que recomendo em caso de dúvida (Seção 7.2).** Não há vedação no texto, mas também não há autorização expressa. **Não coberta pela decisão de 23/07/2026** (que resolveu só o critério de escolha entre subtabelas, não a possibilidade de uni-las) — continua aberta.

**L-7 — A conclusão sobre fachadas não tem confirmação da SMDU.**
A leitura (i) da Seção 4 é sólida em texto, modelo e finalidade, mas não há parecer, manual ou decisão administrativa no nosso acervo confirmando. Ver Seção 13.

**L-8 — Não localizei o "texto padrão do Anexo I" citado pelo próprio modelo.**
A caixa OCUPAÇÃO do modelo instrui: *"(PREENCHER CONFORME O TEXTO PADRÃO DO ANEXO I)"*. **[INTERPRETAÇÃO]** a remissão é, muito provavelmente, à lista de 15 tipos de ocupação do Anexo I, III, PLANTAS DOS PAVIMENTOS, item 7 (Seção 3.4) — é a única lista fechada de tipos de ocupação do anexo. Não é dito com essas palavras.

**L-9 — ESTREITADA em 21/07/2026. O PREO não pode faltar no protocolo, mas pode ser TROCADO depois — e o procedimento de troca é regulado e está vigente.**
Continua sem resposta a pergunta "posso protocolar sem PREO?" — nada no decreto, no Anexo II ou no carimbo admite dispensa, e os três exigem a assinatura dele. **O que descobri, e resolve o problema comercial por outro caminho:** a **Resolução EIS-REN/SMDEIS nº 3, de 03/03/2023** (status oficial **Válido**, arquivada nesta data) regula a **substituição do PREO** em processo eletrônico já aberto. Exige quatro documentos, e a ausência de qualquer um impede a efetivação:

> Art. 1º [...] I - Requerimento informando a baixa do atual PREO e a inclusão do novo profissional, conforme Anexo I do Decreto 5726/1986, modificado pelo Decreto 8417/1989, devidamente assinado pelo proprietário; II - Cópia da carteira expedida pelo Conselho Regional de Engenharia (CREA/RJ) ou do Conselho de Arquitetura (CAU/RJ) [...] do novo profissional responsável pela obra (PREO); III - **Anotação de Responsabilidade Técnica (ART) ou Registro de Responsabilidade Técnica (RRT) quitado** referente ao serviço de execução das obras do novo PREO; IV - Termo de Responsabilidade Técnica conforme modelo do Anexo I desta Resolução.
>
> Parágrafo único. A ausência de qualquer um dos documentos listados nos incisos I a IV implicará na não efetivação do requerimento.

**[INTERPRETAÇÃO] Consequência operacional para o nosso fluxo:** a saída não é protocolar sem PREO — é protocolar **com um PREO inicial** e substituí-lo quando o construtor definitivo for contratado, por procedimento próprio e barato. Isso tira o licenciamento do caminho crítico da contratação da obra. **Não é dispensa; é substituição.** Kelsen decide se isso vira regra comercial.

> **[ATENÇÃO]** **Achado colateral que impacta a L-1:** o inciso III prova que **ART/RRT quitado é documento exigido** no licenciamento de obras da SMU — ao menos na substituição de PREO. Isso é a primeira evidência oficial, em texto normativo, de que RRT circula no procedimento, e reforça que "RRT = 0 ocorrências no decreto" (Seção 5.2) significa apenas que **o decreto não é a fonte** dessa exigência. Continua valendo em absoluto: **nunca registrar RRT como "não exigido".**

**L-10 — Não sei onde vive a fronteira entre "norma geral de licenciamento" (reserva de lei) e "procedimento" (delegado ao Executivo).**
É o único flanco real contra a validade da Condição Geral IV.1 (Seção 17.5). A LC 270/2024, Art. 276, faz a partilha mas **não define nenhum dos dois termos**, e não localizei a "lei específica" de normas gerais que o caput anuncia no futuro. **Consequência prática: baixa.** Mesmo que a fronteira fosse discutível, ninguém tem interesse jurídico em exigir que a Prefeitura **aceite** uma peça que ela não analisa. Registro por honestidade analítica, não como risco operacional.

**L-11 — Projeto de fachada em lote situado em APAC: exigência legal real que a nossa base inteira ignora.**
LC 270/2024, **Art. 280, III** exige, em **nova construção** em lote em Área de Proteção do Ambiente Cultural classificado como passível de renovação, que o **projeto da fachada com as especificações dos materiais de acabamento** seja aprovado pelos órgãos de tutela do patrimônio cultural **antes da construção da primeira laje**. Não é peça do DULI e não conflita com IV.1 (Seção 17.3) — é processo paralelo, em outro órgão, com outro prazo. **Não sei o procedimento, o prazo de análise nem o formato exigido pelo órgão de tutela.** Não é o cenário padrão de Recreio e Barra, mas se um lote nosso cair em APAC, **existe uma fachada a produzir e a aprovar, e um marco de obra atrelado a ela**. Precisa de pesquisa própria antes de acontecer.

**L-12 — Não sei se as seis normas alteradoras da LC 270/2024 esgotam a lista.**
O levantamento da Seção 18.3 cobriu as **145 leis complementares** cadastradas na base oficial da SMU e é confiável para esse universo. Mas **decretos e resoluções também regulamentam a LC 270** — o RDT da Resolução SMDU 10/2026 é exemplo — e não varri esse universo inteiro com o mesmo rigor. **A base está muito mais atual do que estava, não está provada completa.**

---

## 13. O que a Condição Geral IV.1 implica para a Planilha de Enviáveis

Implica, e é uma divergência frontal. A **Planilha de Enviáveis Externos** e o **POP-ARQ-PL-01** listam, entre os entregáveis do Projeto Legal, itens que o Decreto 55.622/2025 **não pede — e, em um caso, recusa**:

| Item da nossa base interna | Situação no LICIN 2.0 | Base |
|---|---|---|
| Plantas legais de todos os pavimentos (cotadas) | **Entra**, mas só com contorno, cotas, ATE/ATC, projeção e ocupação — **sem layout interno** | Anexo I, III, PLANTAS DOS PAVIMENTOS + IV, 1 |
| Implantação legal / Planta de situação do lote | **Entra** — e os dois itens da nossa lista são **uma peça só** no decreto | Anexo I, III, PLANTA DE SITUAÇÃO |
| Cortes legais | **Entra** | Anexo I, III, CORTES |
| **Fachadas legais** | **NÃO ENTRA — expressamente recusada** | Anexo I, IV, 1 |
| Quadro de áreas legal | **Entra** — Anexo III ou IV conforme Art. 10 | Art. 10 e p.ú. |
| **Memorial descritivo** | **Não é peça do LICIN 2.0** — `memorial` = 0 ocorrências no decreto | Seção 5.2 |
| RRT(s) do Projeto Legal | **Não determinável pelo decreto** — `RRT` = 0 ocorrências; pode ser exigido pelo requerimento on-line | Seção 5.2 + L-1 |

**Três consequências, para decisão de Kelsen — não são minhas para executar:**

1. **"Fachadas legais" precisa sair da lista de entregáveis à prefeitura**, ou ser reclassificada como entregável **ao cliente** (documentação do projeto), nunca como peça de protocolo. Hoje a Planilha induz a produzir e enviar peça que a norma recusa. É retrabalho e é risco de vício formal no protocolo.
2. **"Plantas legais cotadas" precisa de qualificação explícita** na Planilha: cotadas **de perímetro e de ATE**, não de compartimento. Sem essa qualificação, a equipe de Arquitetura entrega planta baixa arquitetônica — que é justamente o que IV.1 recusa. Esta é a divergência de maior impacto prático, porque não parece uma divergência: parece "planta cotada" nos dois documentos.
3. **"Memorial descritivo (para protocolo legal)" está mal rotulado.** Pode continuar existindo como peça interna ou contratual, mas o rótulo "para protocolo legal" é falso perante o decreto.

**Não alterei a Planilha, o POP-ARQ-PL-01 nem o Memorial.** São documentos do Drive, base oficial da casa, e a correção não é minha (Princípio 5). Sinalizo a Kelsen (Princípios 8, 9 e 18).

---

## 14. Checklist operacional — Construção do Zero, residencial unifamiliar, Recreio/Barra

Síntese do que este POP sustenta. **Cada linha tem endereço; nada aqui é acrescentado por hábito.**

**Peças gráficas — DULI (modelo do Anexo I, inciso I):**
1. Título conforme carimbo do modelo *(Anexo I, III, TÍTULO, 1-2)*
2. Quadro de áreas na prancha da situação *(Anexo I, III, QUADRO DE ÁREAS, 1-3)*
3. Planta de situação — **13 itens** *(Anexo I, III, PLANTA DE SITUAÇÃO)*
4. Plantas dos pavimentos — **8 itens, sem layout interno** *(Anexo I, III, PLANTAS DOS PAVIMENTOS)*
5. Cortes — **8 itens** *(Anexo I, III, CORTES)*

**Não incluir:** fachadas; planta baixa arquitetônica; qualquer planta alheia à implantação/volumetria *(Anexo I, IV, 1)*.

**Documentos:**
6. Anexo II — Termos e Declarações, **uma única opção por tema**, assinado por proprietário + PRPA + PREO *(Art. 6º p.ú.; Anexo II, V, 2-3)*
7. **Anexo IV** — Quadro Explicativo de Áreas uni/bifamiliar, assinado por proprietário/adquirente + autor *(Art. 10, p.ú.)*
8. Documentação do requerimento on-line — **conteúdo desconhecido, ver L-1**

**Depois, fora do protocolo:**
9. Anexo V — Declaração de compatibilidade, **para o início das obras** *(Art. 4º §4º)*
10. Informar no processo: início da obra, conclusão das fundações, conclusão da primeira laje, conclusão da obra *(Art. 5º, I-IV)*

**Antes de fechar — conferências que este POP não dispensa:**
- Parâmetros urbanísticos do lote pela Skill `legal-base-legislativa-bairro` + POP-LEGAL-RIU-01, **confirmando a AP antes de ler a linha do Anexo XXI** (colisão de código de zona entre APs).
- Afastamentos contra o COES, com atenção ao Art. 8º §3º (varandas e sacadas a 1,50 m mesmo no regime não afastado).
- Formato da prancha: **indefinido** — ver Seção 11 e L-5. Não protocolar sem decisão de Kelsen.
- **Status jurídico de cada norma citada**, na base Busca Fácil da SMU (Seção 18.1). Norma nossa não confere vigência sozinha, e já operamos com quatro artigos revogados sem saber.
- **COES Art. 35 § 7º** — dutos no passeio para enterramento de fiação de energia e telecomunicações. **Obrigatório em toda nova edificação** (LC 283/2025). Conferir se o projeto e o orçamento contemplam.

**O que este checklist NÃO oferece, e é bom saber que não oferece:**
- **Não há rito de baixa complexidade.** Casa unifamiliar segue as três etapas do Art. 2º como qualquer outro projeto. O único tratamento diferenciado vigente é o quadro de áreas do **Anexo IV** em vez do Anexo III (Art. 10, p.ú.). Ver Seção 16.

---

## 15. Rastreabilidade

- **Produzido por:** Hely, 21/07/2026, sob determinação de Claudemberg -> Wallenberg -> Kelsen.
- **Fontes primárias:** os quatro PDFs da Seção 1, arquivados em `Fontes_Legislacao/` nesta data; COES (LC 198/2019) já arquivado.
- **Método:** extração `pdftotext -layout -enc UTF-8` + rasterização `pdftoppm -r 200` e leitura visual dos anexos em imagem + varredura por termo sobre o corpus integral (não apenas sobre o anexo esperado).
- **Não toquei:** POPs existentes, casos-teste, Planilha de Enviáveis, POP-ARQ-PL-01, Memorial, estado de Kelsen, Drive. Nada foi gravado em pasta de cliente.
- **Princípios aplicados:** 18 (ética e conformidade — declarar lacuna em vez de preencher), 8 (rastreabilidade — artigo em cada afirmação), 9 (padronização — checklist único para toda a cidade), 3 (qualidade antes de velocidade — rasterizar e olhar antes de afirmar).

---

## 16. O rito de baixa complexidade para unifamiliar — **NÃO EXISTE HOJE**

> **Cenário: (c) — o rito perdeu a âncora normativa, e o rito aplicável hoje é o completo do LICIN 2.0.**
> **Confiança: ALTA.** Fundamento em fonte oficial da própria SMU, com status jurídico declarado por ela, e não por inferência nossa.

Esta seção é de peso desproporcional ao seu tamanho: **unifamiliar é o escopo padrão da Sttickler**, e a hipótese investigada era a de existir um caminho curto que nós desconhecíamos.

### 16.1 O que a Resolução SMDEIS 27/2021 criava

Ela é real, e era exatamente o que se supunha. Texto literal do que importa:

> **Art. 1º.** Será adotado o formulário em versão integrada e reduzida dos Anexo I e Anexo II do Decreto Rio Nº 48719, de 5 de abril de 2021, presente no Anexo I desta resolução, na análise para o licenciamento dos seguintes tipos de projetos:
> I - Construção de prédio residencial: a) Unifamiliar; b) Bifamiliar;
> II - Modificação com acréscimo de área em prédio existente;
> III - Modificação com acréscimo de área em prédio existente com criação de unidade autônoma;
> IV - Modificação sem acréscimo de área em prédio existente;
> V - Modificação sem acréscimo de área em prédio existente com desdobramento e/ou unificação de unidades autônomas;
> VI - Transformação de uso;
>
> Parágrafo único. O disposto no caput aplica-se aos projetos que envolvam mais de um tipo de solicitação descrita nos incisos.

> **Art. 2º.** Para os casos previstos nesta Resolução, permanecem os prazos estabelecidos no §6º do Art. 2º do Decreto Rio Nº 48719, de 5 de abril de 2021, sendo que **as etapas dispostas nos incisos I, II, III e IV, do mesmo artigo, serão unificadas em etapa única.**

> **Art. 5º.** Esta resolução entrará em vigor na data de sua publicação, e revoga as disposições em contrário.

Ou seja: formulário único e reduzido, e **quatro etapas colapsadas em uma**. Para casa unifamiliar seria o caminho mais curto existente.

### 16.2 O ponto de virada — o Decreto 55.622/2025 **não tem cláusula revogatória nenhuma**

Kelsen pediu a transcrição do artigo final inteiro. É esta, literal e completa:

> **Art. 12.** Este Decreto entra em vigor na data de sua publicação.
>
> Rio de Janeiro, 1º de janeiro de 2025, 460º ano de fundação da Cidade.
> EDUARDO PAES
> D.O. RIO 01/01/2025

**Não há mais nada depois.** O Decreto 55.622/2025 tem **exatamente 12 artigos** (contagem verificada no texto integral) e **nenhuma cláusula revogatória** — nem expressa, nem genérica. Varredura de controle no texto integral: `revog` aparece **1 única vez**, e é no Art. 6º, sobre revogação **da licença** em caso de falsidade nas declarações — não sobre revogação de norma. `48719` e `48.719` = **0 ocorrências**. **O decreto não menciona o Decreto 48.719/2021 em lugar nenhum.**

> **[ATENÇÃO]** **Armadilha real que quase entrou nesta análise, registrada para o próximo Hely.** O PDF da publicação no D.O. de 01/01/2025 **contém** a frase "Art. 4º Fica revogado o Decreto Rio nº 48.414, de 1º de janeiro de 2021". Ela é de **outro decreto na mesma edição** — o **Decreto 55.623/2025, que aprova o Manual de Marca da Prefeitura**, e o decreto revogado é o **48.414**, não o 48.719. Ler o D.O. como se fosse um documento só produz revogação falsa. **Sempre delimitar o ato antes de atribuir a cláusula.**

### 16.3 A resposta — e ela não veio da interpretação, veio do registro oficial

O raciocínio jurídico que Kelsen passou (resolução é ato derivado; caindo o decreto-âncora, cai por perda de fundamento de validade) estava correto — mas eu não precisei decidir isso por conta própria, e não decidi. **A Prefeitura já declarou o status dos dois atos**, na base "Busca Fácil" da Subsecretaria de Planejamento Urbano da SMU (`www2.rio.rj.gov.br/smu/buscafacil`), que publica status jurídico por ato:

| Ato | Status oficial | Nota de status, literal |
|---|---|---|
| Decreto 48.719/2021 (âncora) | **Sem efeito** | "SEM EFEITO EM FUNÇÃO DA PUBLICAÇÃO DO DECRETO 55622 DE 1º DE JANEIRO DE 2025 (LICIN 2.0)" |
| **Resolução SMDEIS 27/2021** | **Sem efeito** | "SEM EFEITO EM FUNÇÃO DA PUBLICAÇÃO DO DECRETO 55622 DE 1º DE JANEIRO DE 2025 (LICIN 2.0)" |
| Decreto 55.622/2025 | **Válido** | — |

As notas são **literalmente idênticas** para o decreto-âncora e para a resolução. A Administração aplicou, ela mesma, exatamente a lógica de perda de fundamento de validade: revogou tacitamente o decreto (o novo regula inteiramente a matéria) e arrastou junto a resolução derivada, **sem revogação expressa de nenhum dos dois**.

**[INTERPRETAÇÃO] — sobre o argumento de recepção, que Kelsen pediu que eu não descartasse por conveniência.** Ele existia e era o melhor argumento contrário: se o novo decreto reproduz a matéria sem conflitar, a resolução poderia ser recebida. **Ele não sobrevive**, por dois motivos, e nenhum deles é conveniência:
1. **A resolução é inaplicável por dependência formal.** Todos os seus quatro artigos operativos remetem a peças do decreto revogado — "Anexo I e Anexo II do Decreto 48719", "Anexo III do Decreto 48719", "§6º do Art. 2º do Decreto 48719", "Art. 13 do Decreto 48719". O Decreto 55.622/2025 tem outra estrutura de anexos (I a V) e outro desenho de etapas (três, no Art. 2º, não quatro). **Não há a que aplicar a resolução.** Recepção exigiria correspondência, e não há.
2. **A Administração declarou o contrário.** O órgão que aplicaria o rito registra o ato como sem efeito. Sustentar recepção contra o registro do próprio órgão licenciador seria, na prática, protocolar apostando numa tese — o oposto do Princípio 18.

### 16.4 Não há substituto — verificado, não presumido

Busquei norma posterior sob todas as siglas que a Secretaria já teve (SMDEIS -> SMDU -> SMDUE), por dois caminhos independentes:

| Verificação | Resultado |
|---|---|
| Todas as Resoluções da **SMDU** cadastradas | 4 — nenhuma sobre licenciamento simplificado (são: comissão de imóveis abandonados; dois Projetos de Alinhamento; e RDT) |
| Todas as Resoluções da **SMDUE** cadastradas | 4 — nenhuma sobre licenciamento simplificado (Reviver Cultural; Rua da Cerveja; e duas de licenciamento ambiental) |
| Busca por texto integral: `LICIN` | 17 atos, **nenhum posterior a 01/01/2025** |
| Busca por texto integral: `DULI` | **1 ato — apenas o Decreto 55.622/2025** |
| Busca por texto integral: `complexidade` | 31 atos; o único sobre complexidade no licenciamento é a Resolução SMDEIS 10/2021, de **grande** complexidade |

> **[ATENÇÃO]** **Assimetria que vale registrar:** a Resolução SMDEIS **10/2021**, que trata de *"projetos de **grande** complexidade"*, continua com status **Válido**. Caiu a de baixa complexidade e ficou a de grande. Não sei o porquê e não vou especular — mas isso afasta a hipótese de que a Prefeitura tenha feito uma limpeza indiscriminada de resoluções antigas de licenciamento. **A queda da 27/2021 foi específica.**

### 16.5 O que isso significa na prática para a Sttickler

**Para casa unifamiliar, hoje, vale o rito completo do LICIN 2.0** — as três etapas do Art. 2º, o DULI completo do Anexo I, o Anexo II integral e o Anexo IV. **Não existe formulário reduzido, não existe etapa única, e não há atalho normativo para o nosso escopo padrão.**

O único tratamento diferenciado que **de fato existe e está vigente** para unifamiliar/bifamiliar no LICIN 2.0 é o **Art. 10, parágrafo único**: o quadro de áreas é o do **Anexo IV** (tabela única, mais simples) em vez do Anexo III. Isso já está mapeado na Seção 8 deste POP e continua correto — mas é simplificação de **uma peça**, não de rito.

> **[ATENÇÃO]** **Não confundir a Seção 8 com um rito simplificado.** O Anexo IV é mais simples que o Anexo III; o **procedimento** é idêntico ao de qualquer outro projeto. Quem ler "existe tratamento próprio para unifamiliar" e concluir "existe rito rápido" erra por três etapas de análise.

---

## 17. Pode o decreto recusar fachada e planta baixa? — teste de hierarquia normativa

> **Resposta: SIM, pode. A recusa da Condição Geral IV.1 se sustenta.**
> **Confiança: ALTA** quanto a "nenhuma lei exige a peça" (varredura sobre texto integral, resultado negativo robusto). **Confiança MÉDIA-ALTA** quanto ao enquadramento da delegação, porque há uma nuance no Art. 276 que declaro abaixo em vez de esconder.

### 17.1 O princípio invocado, e por que ele não resolve sozinho

O princípio levantado por Claudemberg está correto: **decreto regulamenta lei, não a altera**; não pode criar obrigação nem restringir direito além do que a lei estabeleceu; decreto que extrapola é ilegal. É o art. 84, IV da Constituição em desenho federal, reproduzido na competência regulamentar municipal.

Mas o princípio só produz consequência se houver **lei contrariada**. A pergunta operacional não é "o decreto pode restringir?", e sim: **existe lei que exija planta baixa ou fachada no licenciamento?** Se não existe, não há o que extrapolar. Foi essa a pergunta que investiguei.

### 17.2 Varredura no COES (LC 198/2019) — resultado

Corpus: texto integral do COES, 41 artigos mais o Anexo Único (glossário).

| Termo | Ocorrências | Alguma exige a peça no licenciamento? |
|---|---|---|
| `fachada` (todas as flexões) | **18** | **Nenhuma** |
| `planta baixa` | **0** | — |
| `plantas` | **0** | — |
| `peças gráficas` | **0** | — |
| `elevação` (como peça de desenho) | **0** | — |
| `requerimento` | **0** | — |

**As 18 ocorrências de "fachada" foram lidas uma a uma.** Todas são regra **material sobre a edificação**, nunca regra **documental sobre o pedido**. Distribuem-se em três grupos:
1. **Regra de volumetria e balanços** — varandas e sacadas "poderão ocupar toda a fachada" (Art. 8º §§1º e 2º); brises e fechamentos "de modo integrado à composição estética da fachada" (Art. 8º §6º); laje técnica de ar-condicionado a no máximo um metro "em relação ao plano da fachada" (Art. 8º §8º); pilares de varanda (Art. 8º §9º, III e V); equipamentos sobre marquise (Art. 9º, III); elementos de cobertura "limitados aos planos das fachadas" (Art. 10); "fachadas compostas de paramentos de vidro" (Art. 17 §5º); distância de elevador de veículos "até a linha de fachada" (Art. 30).
2. **Definição no glossário (Anexo Único)** — `FACHADA - Qualquer das faces externas de uma edificação [...]`; `LINHA DE FACHADA - É aquela que representa a projeção horizontal do plano da fachada [...]`; e a definição de afastamento, que se mede "entre o plano da fachada da edificação e o alinhamento".
3. **Nenhuma no capítulo de procedimento** — porque **o COES não tem capítulo de procedimento**. Seus oito capítulos tratam de classificação, elementos da edificação, compartimentos, circulação, instalações, obras/segurança/passeios, reconversão de tombados, retrofit e disposições finais. **Não há capítulo de licenciamento, não há lista de documentos, não há lista de peças gráficas.**

O que mais se aproxima de uma regra sobre a instrução do pedido é o **Art. 39 §2º**, e ele diz o oposto do que a tese da extrapolação precisaria:

> § 2º Esta Lei Complementar estabelece as condições que a Prefeitura da Cidade do Rio de Janeiro considera indispensáveis **às edificações**.

O COES define o que é indispensável **à edificação** — não ao processo.

**Sobre "o COES é expressamente um código simplificado que remete detalhamento a regulamento?"** — a resposta honesta é **parcialmente, e não da forma que ajudaria a tese**. "Simplificado" está no nome e no Art. 1º, e o COES de fato revogou em bloco o antigo Regulamento de Construções e Edificações do Decreto "E" nº 3.800/1970 e mais dezenas de normas (Art. 41). Mas suas remissões a regulamento são **pontuais e temáticas** — Art. 16 §4º (jiraus em shopping center), Art. 35 §5º (doação de mudas) — e **nenhuma delas trata do conteúdo do pedido de licenciamento**. O COES não contém uma cláusula geral do tipo "o procedimento será definido em regulamento".

### 17.3 Varredura na LUOS / Plano Diretor (LC 270/2024) — resultado

Corpus: texto integral, 538 artigos, versão republicada pós-rejeição de vetos.

| Termo | Ocorrências | Alguma exige a peça no licenciamento? |
|---|---|---|
| `fachada` | **17** | **Nenhuma** |
| `planta baixa` | **0** | — |
| `plantas` | **2** | **Não** — uma é botânica ("atividade biológica das plantas", Art. sobre faixa verde drenante); a outra é o rol de documentos que ficam à disposição do público **em audiência pública** de EIV, não peça do pedido |
| `peças gráficas` | **0** | — |
| `elevação` (peça de desenho) | **0** | — |

As 17 ocorrências de `fachada` também foram lidas. São de quatro tipos, todas materiais ou de competência, nenhuma documental: **fachada ativa** (Arts. 394 e correlatos — exigência de uso no térreo, não de desenho); **linha de fachada** e afastamento frontal (Arts. 363, 413 e Anexo XXIII — geometria); **reforma de fachada em bem tombado/APAC** (Arts. 278, II e IV, 280, III, 413 — hipóteses que **dependem de licença**, e uma delas, o Art. 280, III, exige que **o projeto da fachada** seja aprovado pelos órgãos de tutela do patrimônio em nova construção em APAC); e a lista de obras do Art. 477.

> **[ATENÇÃO]** **A exceção que confirma a regra, e que precisa ficar registrada: Art. 280, III da LC 270/2024.**
>
> > III - Nova construção em lote situado em Área de Proteção do Ambiente Cultural - APAC, classificado como passível de renovação, **exceto quanto ao projeto da fachada com as especificações dos materiais de acabamento, que deverá ser aprovada junto aos órgãos de tutela do patrimônio cultural** antes da construção da primeira laje.
>
> **Aqui a LEI exige projeto de fachada.** Mas exige que ele seja aprovado **pelo órgão de tutela do patrimônio cultural**, em processo próprio, **não que seja peça do DULI protocolado na SMDU** — e apenas em lote situado em APAC. Não há conflito com IV.1: são órgãos, processos e hipóteses diferentes. **[INTERPRETAÇÃO] Consequência prática: em lote em APAC existe, sim, um projeto de fachada a produzir — e a nossa base interna não registra isso em lugar nenhum.** Não é o caso de Recreio e Barra no padrão de Construção do Zero, mas é uma exigência legal real que passaria despercebida. Ver lacuna L-11.

### 17.4 O ponto decisivo — a lei delegou expressamente

Kelsen apontou que a resposta se decide aqui, e se decide mesmo. **LC 270/2024, Título sobre licenciamento e fiscalização, Seção I:**

> **Art. 276.** Lei específica aprovará as normas gerais de licenciamento e fiscalização de obras públicas e privadas de construção, modificação, transformação de uso, reforma, demolição e parcelamento, considerando o disposto nesta Seção.
>
> **Parágrafo único. Os procedimentos e demais regulamentações sobre licenciamento e fiscalização de obras públicas e privadas, complementares à lei, serão estabelecidos em ato do Poder Executivo.**

E o artigo imediatamente anterior faz a partilha de matérias entre as duas leis:

> § 1º As condições para as obras públicas e privadas de demolição, reforma, transformação de uso, modificação e construções estão definidas na Lei Complementar nº 198/2019 - Código de Obras e Edificações Simplificado - COES e suas regulamentações.
> § 2º O licenciamento e a fiscalização de obras públicas e privadas são regidos pelo disposto na Seção I deste Capítulo e por normas específicas.

**A arquitetura normativa fica explícita:** o COES define **condições da edificação**; a LC 270 define o **regime do licenciamento**; e o **procedimento** é expressamente entregue a **ato do Poder Executivo** — que é o Decreto 55.622/2025.

Definir quais peças gráficas instruem o pedido, e quais não serão aceitas, é **procedimento de instrução**. O decreto está **exercendo a delegação do Art. 276, parágrafo único**, não invadindo campo de lei.

### 17.5 A nuance que declaro em vez de esconder

O Art. 276 **caput** reserva a **lei específica** as *"normas gerais de licenciamento"*, e delega ao Executivo apenas *"os procedimentos e demais regulamentações [...] **complementares à lei**"*.

**[INTERPRETAÇÃO]** Sustento que "quais peças instruem o pedido" é procedimento complementar, não norma geral — norma geral seria *se* a obra depende de licença, *quem* licencia, *quais* obras são dispensadas, matérias que a própria LC 270 disciplina nos Arts. 277 a 281. Mas reconheço que a fronteira entre "norma geral" e "procedimento" não é definida em lugar nenhum do texto, e é o único flanco argumentativo real contra a validade de IV.1.

**Um dado que reforça a delegação, e que também registro:** o Art. 276 caput fala em lei específica **no futuro** — *"Lei específica **aprovará** as normas gerais"*. Não localizei, na base legislativa municipal, lei específica posterior à LC 270/2024 que tenha aprovado essas normas gerais de licenciamento. **[INTERPRETAÇÃO]** Enquanto ela não vem, o campo é ocupado pelo ato do Poder Executivo previsto no parágrafo único — o que **amplia**, e não reduz, o espaço regulamentar do Decreto 55.622/2025.

### 17.6 Conclusão, e o que ela decide de negócio

**A conclusão que Kelsen já levou a Wallenberg NÃO se inverte — ela se confirma, e agora com fundamento hierárquico testado.**

| Pergunta | Resposta | Base |
|---|---|---|
| O COES exige fachada ou planta baixa no licenciamento? | **Não** | 18 ocorrências de `fachada`, todas materiais; `planta baixa` = 0; sem capítulo de procedimento |
| A LUOS exige? | **Não** (salvo APAC, perante o órgão de patrimônio) | 17 ocorrências, todas materiais; `planta baixa` = 0; exceção do Art. 280, III |
| A lei delegou o procedimento ao Executivo? | **Sim, expressamente** | LC 270/2024, Art. 276, parágrafo único |
| O decreto extrapola ao recusar as peças? | **Não** | Exerce delegação; não contraria exigência legal, porque não há exigência legal |

**Consequência para o contrato e para a Planilha de Enviáveis:** a Seção 13 deste POP **permanece integralmente válida**. "Fachadas legais" continua sendo peça que a Prefeitura não aceita no DULI, e continua sendo item que a Planilha vende como entregável de protocolo. **A correção dos documentos do Drive segue necessária, e segue sendo de Kelsen.**

> **[ATENÇÃO]** **O que NÃO decidi, e não cabia a mim decidir:** se a Sttickler deve continuar **produzindo** fachada como entregável **ao cliente** (documentação do projeto, base para a obra, valor percebido). Isso é decisão comercial de Claudemberg. O que este POP afirma é apenas que **fachada não é peça de protocolo** — não que fachada seja inútil.

---

## 18. Vigência da base legislativa — o que estava desatualizado

Esta seção responde às Perguntas 3 e 4 e é a de maior impacto silencioso: **operávamos com quatro aprendizados registrados que hoje são lei revogada.**

### 18.1 Método novo, que muda a manutenção da base daqui pra frente

> **[RESOLVIDO]** **Descoberta de método, e talvez a mais reaproveitável desta tarefa.** A base **"Busca Fácil"** da Subsecretaria de Planejamento Urbano da SMU (`www2.rio.rj.gov.br/smu/buscafacil`) é fonte **oficial**, é consultável por HTTP simples (sem login, sem JavaScript, sem CAPTCHA) e entrega três coisas que nenhuma outra fonte nossa entregava:
>
> 1. **Status jurídico declarado por ato** — Válido / Revogado / Sem efeito / Suspenso / Sub judice / Declarado inconstitucional — com **nota textual explicando o motivo e citando a norma causadora**.
> 2. **Texto CONSOLIDADO em PDF**, com notas de alteração embutidas no corpo, no formato *"(Artigo 19 com redação dada pela Lei Complementar 291 de 01/12/2025.)"*.
> 3. **Busca por texto integral** sobre todo o acervo, que permite varredura negativa confiável.
>
> Isso resolve estruturalmente o feedback permanente "sempre atualizar legislação": deixa de depender de a gente lembrar de procurar. **Antes de usar qualquer norma, consultar o status dela aqui.** Recomendo a Kelsen que isto vire item da Skill `legal-base-legislativa-bairro` e do POP-GESTOR-LEGAL-01 (decisão dele — Função 5 é de Wallenberg).

### 18.2 Pergunta 3 — o COES: os dois arquivos são iguais, e **os dois estão desatualizados**

Comparação dos dois PDFs pedidos por Kelsen:

| | Versão de Claudemberg | Nossa versão (13/07) |
|---|---|---|
| MD5 | `6b6afbd71e15cb4ddb6687ab892594d9` | `c31013f801c05658027c006ba52e5148` |
| Páginas | 31 | 31 |
| Bytes de texto extraído | 90.187 | 81.984 |
| Origem (metadado) | impressão de página web via Chrome, em 21/07/2026 | Microsoft Word 2016, 18/01/2019 |
| Artigos | 41 | 41 |
| Notas de "redação dada por" | **nenhuma** | **nenhuma** |

**Diferem em hash, mas não em conteúdo normativo.** Comparei **artigo por artigo**, com normalização de espaços: os 41 artigos existem nos dois, e as 19 divergências detectadas são **todas tipográficas** — maiúscula/minúscula depois de "I -", presença ou ausência do ponto em "Art. 9" vs "Art. 9.", travessão `-` vs `–`, aspas retas vs curvas, e três casos de reordenação de trechos causada pela extração de layout, não pelo documento. **Nenhuma diferença de texto normativo.** A diferença de bytes se explica: a nossa traz o **Ofício GP nº 176/CMRJ** de sanção, que a de Claudemberg não tem.

**A conclusão relevante não é qual das duas vence — é que nenhuma das duas serve.** Ambas são o texto **original de 2019**. O COES foi alterado **duas vezes** desde então, e **nenhuma das duas alterações está em nenhum dos dois arquivos**:

| Norma alteradora | Data | O que fez ao COES |
|---|---|---|
| **LC 283/2025** | 14/07/2025 | acrescentou o **§ 7º ao Art. 35** |
| **LC 291/2025** | 01/12/2025 | acrescentou o **§ 7º ao Art. 2º** |

Baixei da SMU o **texto consolidado oficial** do COES (PDF gerado em 07/01/2026), que traz os dois parágrafos com as respectivas notas de alteração. Ele está arquivado como `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` e **passa a ser a nossa versão de referência**. Os dois arquivos antigos foram **preservados**, não sobrescritos (Princípio 8).

**As duas novidades, literais:**

> **Art. 2º § 7º** No licenciamento de loteamentos onde sejam permitidos lotes residenciais bifamiliares, fica facultado o parcelamento destes lotes com metade da área do lote mínimo previsto para o local e testada mínima de 6m (seis metros), com exceção dos lotes de 8ª e 9ª categorias previstos na Lei Complementar nº 270, de 16 de janeiro de 2024. *(Parágrafo 7º acrescentado pela Lei Complementar 291 de 01/12/2025)*

> **Art. 35 § 7º** É obrigatória a instalação de dutos nos passeios diante das novas edificações para enterramento da fiação de energia e de telecomunicações, obedecendo-se às regras e às normas técnicas definidas pelo órgão municipal responsável pelo licenciamento da obra. *(Parágrafo 7° do Artigo 35 acrescentado pela Lei Complementar 283 de 14/07/2025.)*

> **[ATENÇÃO]** **O Art. 35 § 7º é obrigação nova, incide em TODA nova edificação, e não estava em lugar nenhum da nossa base.** "Novas edificações" é exatamente o escopo Construção do Zero da Sttickler. É custo de obra e é item de projeto de passeio que ninguém orçou. **Sinalizo a Kelsen como impacto que atravessa Legal e vai para Complementares e para a proposta comercial** (Princípio 16).

**Sobre a pendência da LC 291/2025 — **[RESOLVIDO]** FECHADA, e a nossa suspeita estava certa.** Ela existe, é de **01/12/2025**, e o registro oficial confirma o que só tínhamos por fonte secundária (LegisWeb): ela altera o COES **no Art. 2º**, e não nos Arts. 4º/8º/31. Texto literal do dispositivo alterador:

> **LC 291/2025, Art. 8º** Adiciona novo parágrafo ao art. 2º da Lei Complementar nº 198, de 14 de janeiro de 2019: "Novo parágrafo. No licenciamento de loteamentos onde sejam permitidos lotes residenciais bifamiliares [...]"

> **[ATENÇÃO]** Note a redação: a lei diz literalmente **"Novo parágrafo"**, sem numerar. Foi a consolidação da SMU que o numerou como § 7º. Vício de técnica legislativa da própria Prefeitura — registrado para que ninguém suspeite de erro de transcrição nosso.

### 18.3 Pergunta 4 — a LUOS: o texto-base está certo, as alteradoras é que faltavam

**Boa notícia primeiro:** o nosso `LC270_2024_PlanoDiretorLUOS.pdf` **é a versão correta**. Confrontado contra o texto vigente do portal da Câmara Municipal (URL indicada por Claudemberg, HTTP 200):

- é a **versão republicada** pós-rejeição dos vetos parciais na sessão de 14/03/2024 — os dois textos trazem a mesma observação de republicação;
- **538 artigos** nos dois;
- artigos-chave conferidos por similaridade de texto: Art. 103, Art. 108, Art. 276, Art. 345, Art. 367 — **todos idênticos**.

**Má notícia:** conhecíamos **uma** das **seis** normas que alteram a LC 270/2024. Levantamento completo sobre as 145 leis complementares cadastradas na base oficial:

| Norma | Data | Status | Tínhamos? | O que faz de relevante |
|---|---|---|---|---|
| **LC 274/2024** | 17/07/2024 | Válido | **Sim** | alterações e instrumentos — **mas com 4 blocos de artigos revogados**, ver 18.4 |
| **LC 281/2025** | 30/05/2025 | Válido | **Não** | assume o cálculo e o pagamento da contrapartida; **revoga blocos da LC 274** |
| **LC 283/2025** | 14/07/2025 | Válido | **Não** | altera o **COES** (Art. 35 §7º) |
| **LC 291/2025** | 01/12/2025 | Válido | **Não** | altera COES, LC 270, LC 281 e outras |
| **LC 292/2025** | 02/12/2025 | Válido | **Não** | regulamenta Art. 284, III da LC 270 (imóveis com risco estrutural) |
| **LC 299/2026** | 09/01/2026 | Válido | **Não** | nova redação ao **Art. 371 § 5º** da LC 270 (grupamentos de interesse social) |
| **LC 301/2026** | **09/07/2026** | Válido | **Não** | AEIU Praça Onze; altera LC 270 e **LC 281** |

Todas as seis foram baixadas de fonte oficial e arquivadas nesta data.

> **[ATENÇÃO]** **A LC 301/2026 é de 12 dias atrás.** A própria SMU sinaliza na ficha da LC 270 o alerta literal: *"ATENÇÃO! VERIFICAR ALTERAÇÕES DA LEI COMPLEMENTAR Nº 301 DE 09/07/2026"*. **Uma base legislativa parada há uma semana já pode estar errada.**

**Impacto sobre o nosso escopo (Recreio e Barra, AP-4):** as alterações da **LC 301/2026** à LC 270 concentram-se em **Operação Interligada e Reviver Centro**, com áreas receptoras nas **AP-1, AP-2 e AP-3**, expressamente **exceto a XX RA**. **A AP-4 não é área receptora.** A **LC 299/2026** altera regra de **grupamento de interesse social**, que não é o nosso produto. **[INTERPRETAÇÃO] Nenhuma das duas muda parâmetro de Recreio ou Barra** — mas isso é conclusão minha por leitura das hipóteses de incidência, e **não substitui a consulta ao RIU para o lote concreto** (POP-LEGAL-RIU-01).

**Bônus pedido por Kelsen — **[RESOLVIDO]** a "falsa lacuna" do CAB está confirmada em fonte oficial.** O portal da Câmara traz, no **Art. 345 § 4º**, a lista de CAB inferior a 1. Para a AP-4, inciso III:

> e) CAB de 0,8 (zero vírgula oito): 1 - ZRU 1 A e B; e **2 - ZRM 3 A, B e D**
> d) CAB de 0,6 (zero vírgula seis): [...] **2 - ZRM 2 B, D, E, F, G, H e M**

**Correção de precisão sobre o que a nossa base registrava:** os valores estavam certos, **as alíneas estavam trocadas** — o CAB 0,8 está na alínea **"e"** (a base dizia "f") e o CAB 0,6 na alínea **"d"** (a base dizia "e"). Corrigido aqui.

> **[ATENÇÃO]** **Contradição interna da própria lei, que precisa ficar registrada.** O **Art. 345 § 2º** afirma: *"Os Coeficientes de Aproveitamento Básico – CAB e Máximo – CAM por zona e subzona estão dispostos por Área de Planejamento no Anexo XXI desta Lei Complementar."* Mas o **Anexo XXI não tem coluna de CAB** — só CAM, TO, lote mínimo, gabarito e afastamento frontal (verificado na leitura com `pdftotext -table`). **O § 2º promete no Anexo XXI um dado que só existe no § 4º.** Quem seguir a remissão do § 2º conclui que o CAB "não está na lei". Foi exatamente essa a origem da falsa lacuna. **Endereço correto do CAB: Art. 345 § 4º** (e Art. 103, parágrafo único, para a regra geral de 1,0).

**Bônus 2 — **[RESOLVIDO]** a LC 281/2025 está arquivada, em versão consolidada.** Os arts. 18 e 19 citados pelo POP-LEGAL-02 **existem e conferem**: o Art. 18 é o **cálculo** da contrapartida (percentual do Valor Unitário Padrão Predial do IPTU, com regra própria para unifamiliar/bifamiliar no inciso II) e o Art. 19 é o **pagamento**. Pela primeira vez o POP-LEGAL-02 tem fonte primária verificável na nossa pasta.

### 18.4 O achado mais grave — quatro aprendizados da nossa base são lei revogada

Este é o resultado que eu não esperava encontrar e que muda o POP-LEGAL-02. **A LC 281/2025, Art. 42, II, revogou blocos inteiros da LC 274/2024:**

> **Art. 42** Ficam revogados: I - A Lei Complementar nº 219, de 19 de agosto de 2020, e a Lei Complementar nº 260, de 22 de maio de 2023; e II - **Os artigos 5º ao 14; artigos 17 ao 23, 26 e artigo 38, da Lei Complementar nº 274, de 17 de julho de 2024.**

Confirmado no **texto consolidado oficial da LC 274**, que traz as notas embutidas: *"(Artigos 5º ao 14 revogados pela Lei Complementar 281 de 30/05/2025.)"*, *"(Artigos 17 ao 23 revogados [...])"*, *"(Artigo 26 revogado [...])"*, *"(Artigo 38 revogado [...])"*.

**O que isso derruba na nossa base:**

| Aprendizado registrado | Artigo | Situação real |
|---|---|---|
| "LC 274 Art. 19 abre caminho oneroso para o gabarito" (aplicar gabarito de afastado a não afastado, pagando contrapartida) | LC 274, Art. 19 | **REVOGADO** |
| "As fórmulas de contrapartida estão nos Arts. 21 e 22 da LC 274" | LC 274, Arts. 21 e 22 | **REVOGADOS** — matéria migrou para **LC 281, Arts. 18 e 19** |
| "LC 274 Art. 38 — legalização por contrapartida, janela de 3 anos até ~17/07/2027" | LC 274, Art. 38 | **REVOGADO** — a janela dos 3 anos **não existe** |
| "LC 274 Art. 12 §2º exclui os prismas do COES da contrapartida" (contrapartida compra área, não habitabilidade) | LC 274, Art. 12 | **REVOGADO** |

> **[ATENÇÃO]** **O quarto item é o mais perigoso, porque a conclusão continua provavelmente certa pelo fundamento errado.** "Contrapartida não compra habitabilidade" segue sendo a leitura correta do sistema — mas **o artigo que eu citava para sustentá-la não existe mais**. Citar artigo revogado em peça de protocolo é vício grave. **Não reusar nenhuma das quatro linhas acima sem reconstruir o fundamento na LC 281.**

**E há uma janela comercial ABERTA que a nossa base registrava como expirada.** O prazo do Art. 40 da LC 281 foi prorrogado duas vezes:

| Redação | Prazo | Fonte |
|---|---|---|
| original (30/05/2025) | 1º/12/2025 | LC 281, Art. 40 |
| dada pela **LC 291/2025** | 1º/06/2026 | consolidação SMU |
| dada pela **LC 301/2026, Art. 58** | **1º de dezembro de 2026** | LC 301 |

Texto vigente, literal:

> **"Art. 40.** Fica estabelecido o prazo de até 1° de dezembro de 2026 para requerimento de licenciamento de projetos a serem licenciados ou requerimentos de legalização, mediante aplicação de contrapartida por acréscimos não previstos na legislação ordinária **com desconto de trinta por cento para pagamento à vista**." (NR)

**Há hoje uma janela aberta, com desconto de 30% à vista, até 01/12/2026** — pouco mais de quatro meses. Nossa base registrava os descontos como expirados. **[INTERPRETAÇÃO]** Isso é matéria comercial e de prazo, não só técnica: qualquer projeto nosso que dependa de contrapartida por acréscimo além do parâmetro ordinário tem vantagem real em protocolar antes dessa data. **Sinalizo a Kelsen; não é minha decisão** (Princípios 14 e 16).

> **[ATENÇÃO]** Os descontos do **Art. 19** da LC 281 (50% à vista até 1º/12/2025; 30% à vista de 1º/12/2025 a 02/03/2026) estão **ambos expirados**. O que está vivo é o do **Art. 40**. São dispositivos diferentes — não confundir.

### 18.5 Consequência para o POP-LEGAL-02 — sinalizada, não executada

O **POP-LEGAL-02 (outorga onerosa)** é o documento mais afetado: seu conteúdo central se apoia em artigos hoje revogados. **Não o alterei.** Kelsen determinou que esta tarefa atualiza o POP-LEGAL-05, e a orientação foi explícita quanto a não propagar sozinho. **Registro aqui e reporto a ele** (Princípio 5).

---

## 19. Rastreabilidade da atualização de 21/07/2026 (2ª rodada)

- **Determinação:** Claudemberg -> Wallenberg -> Kelsen -> Hely. Quatro perguntas de vigência e hierarquia normativa.
- **Fonte oficial nova, decisiva:** base **Busca Fácil** da SMU/Subsecretaria de Planejamento Urbano (`www2.rio.rj.gov.br/smu/buscafacil`) — status jurídico por ato, texto consolidado e busca por texto integral. Complementada pelo portal legislativo da Câmara Municipal (`aplicnt.camara.rj.gov.br`) para a LC 270/2024.
- **Fontes secundárias:** nenhuma foi usada como fundamento. A confirmação da LC 291/2025, antes apoiada em LegisWeb, foi **substituída** por fonte oficial.
- **Método:** `curl` direto + `pdftotext -layout -enc UTF-8`; comparação artigo a artigo com normalização e `difflib`; varredura por termo sobre corpus integral com registro das contagens **zero**; hashes MD5/SHA-256 dos arquivos comparados.
- **Arquivado em `Fontes_Legislacao/` nesta data (nada sobrescrito):** COES consolidado SMU; COES impressão web de Claudemberg; LC 274 consolidada; LC 281 consolidada; LC 283; LC 291; LC 292; LC 299; LC 301; Resolução SMDEIS 27/2021 (sem efeito); Resolução SMDEIS 3/2023 (substituição de PREO).
- **Não toquei:** Planilha de Enviáveis, POP-ARQ-PL-01, Memorial, POP-LEGAL-02 e demais POPs, casos-teste, prancha, estado de Kelsen, Google Drive. Nada em pasta de cliente.
- **Princípios aplicados:** 18 (declarar lacuna e risco em vez de preencher; não escolher o cenário conveniente), 8 (rastreabilidade — artigo e status oficial em cada afirmação; arquivo antigo preservado), 9 (padronização), 16 (escalonamento — LC 283 e janela do Art. 40 sobem imediatamente), 20 (revisão periódica — a base tinha lei revogada em uso).
