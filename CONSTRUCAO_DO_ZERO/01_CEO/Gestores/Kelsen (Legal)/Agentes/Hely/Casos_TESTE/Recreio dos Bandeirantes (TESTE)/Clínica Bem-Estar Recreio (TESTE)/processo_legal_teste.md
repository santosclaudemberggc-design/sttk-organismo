---
status: TESTE — não é cliente real
caso: 3
data_teste: 2026-07-15
gestor: Kelsen
executor: Hely
finalidade: teste de confirmação oficial do Hely (julgamento próprio, não só execução mecânica)
---

# ⚠️ CENÁRIO DE TESTE — NENHUM DADO AQUI É REAL

Todo conteúdo deste arquivo — requerente, imóvel, matrícula, CPF/CNPJ, ARTs, respostas da prefeitura — é fictício, usado para validar o Hely (Agente executor do Gestor Legal, Kelsen). **Nunca copiar para `000_CLIENTES` real, nem tratar como caso verdadeiro.** Terceiro caso-teste da série, independente dos dois anteriores (Bittencourt / Kowalski Andreatta), mesmo bairro de teste.

## Requerente e imóvel (fictícios)
- **Requerente**: Clínica TESTE-QA Bem-Estar Recreio Serviços Médicos LTDA. — sócia-administradora Dra. Camila Herzog Prestes
- **Imóvel**: Rua Escritor Elie Wiesel, nº 215, Recreio dos Bandeirantes, RJ — CEP 22790-672 (rua/CEP reais, CL 476218; número/lote/matrícula fictícios)
- **Matrícula RGI**: 000.002-TESTE | **Terreno**: 500,00 m² (16,00 x 31,25 m)
- **Situação atual**: casa residencial térrea existente, averbada 140,00 m² (Alvará nº 00000-TESTE/2005) — **A SER DEMOLIDA**
- **Natureza da obra**: DEMOLIÇÃO + CONSTRUÇÃO NOVA (unidade nova) — uso comercial/institucional de saúde

## Projeto arquitetônico de origem
- PRPA candidato: Estúdio Bruma Arquitetura (parceiro externo), Arqto. Fábio Noronha Salgueiro, CAU A000001-1-TESTE, ART-TESTE-2026-0031 já emitida
- PREO: **NÃO CONFIRMADO** — "a definir, em processo de contratação"; pré-indicação informal (Constrular Engenharia TESTE Ltda., Eng. Thiago Meireles Falcão, CREA RJ-000000-2-TESTE), sem ART/RRT

---

## ITEM 1 e 3 — Legislação vigente e enquadramento de uso (pesquisa própria, fonte oficial)

**Regra aplicada, confirmada em teste anterior**: fonte oficial (SMDU) sempre vence fonte secundária. Não reaproveitei cegamente o zoneamento dos 2 casos anteriores do mesmo bairro (Rua Claude Monet e Rua Athos Bulcão, ambos confirmados como ZRM3 **D**/AP4) — consultei de novo, para este lote específico.

### Fonte oficial consultada
Como o sistema `mapas.rio.rj.gov.br` (RIU) não é operável por busca textual (exige clique em mapa/lote), usei o serviço de geoprocessamento da própria SMDU que sustenta aquele sistema — API pública ArcGIS REST da Prefeitura (`pgeo3.rio.rj.gov.br/arcgis/rest/services/Urbanismo`), consultando por coordenada geográfica do logradouro (lat/long via CEP oficial 22790-672). Consulta feita e conferida em duas camadas oficiais separadas, em 15/07/2026:
- `LBB_Zoneamento_urbano_vigente` (parâmetros dimensionais)
- `IU_Usos_e_atividades` (enquadramento de uso, base do Decreto nº 56.561/2025)

**⚠️ CORREÇÃO REGISTRADA EM 15/07/2026 — ERRO DE CONSULTA CONFIRMADO POR CLAUDEMBERG (print oficial do RIU, `mapas.rio.rj.gov.br`, mesmo CL 476218).** O que este item registrava originalmente (14/07/2026) como "ZRM3 subzona O" **estava errado** — não existe zona-mãe ZRM3 neste lote. A zona/subzona real, confirmada por fonte oficial assinada (RIU), é **ZRM2 subzona G**. Mantenho abaixo o registro do erro original (rastreabilidade, Princípio 8), não apago — apenas marco como corrigido. Ver investigação de causa raiz e regra de processo atualizada em `Fontes_Legislacao/_indice_fontes.md`.

**Achado real (corrigido): este lote está numa subzona diferente das 2 anteriores, mas em zona-mãe também diferente — não é mais "mesma ZRM3, subzona distinta", é ZRM2 vs. ZRM3.** Comparação agora entre 3 subzonas no mesmo bairro (Recreio), incluindo o registro do erro:

| Parâmetro | ZRM2 **G**/AP4 (este lote — REAL, confirmado via RIU oficial 15/07/2026) | ZRM3 **O**/AP4 — ⚠️ ERRO de consulta de 14/07/2026, corrigido em 15/07/2026 (nunca existiu de fato para este lote) | ZRM3 D/AP4 (2 casos anteriores) |
|---|---|---|---|
| CAB | 0,6 | ~~1,0~~ (errado) | 0,8 (não localizado em texto, só via RIU) |
| CAM | 1,0 | ~~2,0~~ (errado) | 1,0 |
| Taxa de Ocupação | 50% | ~~70%~~ (errado) | 50% |
| Lote mínimo | 360 m² (bateu com o valor errado também) | 360 m² | 600 m² |
| Testada mínima | 10 m (bateu com o valor errado também) | 10 m | 12 m |
| Gabarito afastado das divisas | 4pav/14m | ~~8pav/26m~~ (errado) | 6pav/20m |
| Gabarito não afastado | 4pav/14m — **igual ao afastado, sem vantagem de gabarito por se afastar** | ~~3pav/11m~~ (errado) | 4pav/14m |
| Afastamento frontal | 5 m (bateu com o valor errado também) | 5 m | 5 m |
| ICS (índice de compensação social) | 0,3, obs. "0,3 do CAM" | ~~0,8, obs. "0,4 do CAM"~~ (errado) | não registrado nos casos anteriores |
| SMD (permeabilidade) | 20% da área livre mínima (regra geral, Art. 351-353 — não conferido em detalhe neste lote) | não conferido | não conferido |

**Itens que bateram entre a versão errada e a real (não eram o problema): lote mínimo 360 m², testada mínima 10 m, afastamento frontal 5 m.** O erro estava concentrado nos parâmetros de aproveitamento e gabarito (CAB, CAM, TO, gabarito nos dois regimes, ICS) — exatamente os que definem o mérito do caso.

Fonte primária real: Lei Complementar nº 270/2024 (Plano Diretor/LUOS), legislação "6.270/2024" conforme o próprio atributo retornado pela camada oficial (confirmado tanto pela consulta ArcGIS refeita em 15/07/2026 quanto pelo print do RIU de Claudemberg). **A regra de Kelsen segue confirmada, de forma ainda mais forte**: "um mesmo bairro pode ter regime totalmente distinto do que parece à primeira vista" — aqui a diferença não é só de subzona dentro da mesma zona-mãe, é de **zona-mãe inteira** (ZRM2 vs. ZRM3) entre lotes próximos do mesmo bairro.

### Enquadramento de uso — achado central deste caso (item 3)
Fui além do zoneamento dimensional e busquei o enquadramento de USO, que o pacote não me deu pronto. Usei a mesma API oficial (camada `IU_Usos_e_atividades`) e, complementarmente, o **Decreto Rio nº 56.561/2025** (que regulamenta o Anexo XVIII da LC 270/2024 — tabela de usos por CNAE e por zona, por Área de Planejamento), extraindo o Anexo IV do decreto (o que corresponde à AP4).

**Resultado concreto, com fonte**: na tabela de usos do Decreto 56.561/2025 (Anexo IV/AP4), Seção Q "Saúde Humana e Serviços Sociais", Grupo 86.3 — **"Atividades de atenção ambulatorial executadas por médicos e odontólogos"** — a classificação na coluna **ZRM3 é S-II**.

- **S-II = Uso de Serviços II**, conforme a própria LC 270/2024, Art. 338, inciso VIII: *"serviços de atendimento à população em geral cuja implantação poderá estar sujeita a avaliação de impactos"*.
- **Não é** "Uso Institucional de interesse público" (Art. 338, XVI) — essa categoria é reservada, por texto expresso da lei, a instituições de governo (municipal/estadual/federal) ou a entidades de cunho **assistencial e religioso** — a clínica é uma LTDA privada com fins lucrativos, não se encaixa aqui.
- Classificação "Adequado" (Art. 339, I) na ZRM3 — não é "Vedado".

**Sinalização de risco/pendência para Kelsen (julgamento, não decisão minha):** a resposta simulada da SMDU no item 8 pede reclassificar como "institucional de saúde (ou equivalente)". Pela lei real, **não existe** categoria formal "institucional de saúde" aplicável a uma clínica privada com fins lucrativos — a nomenclatura correta e tecnicamente defensável é **Uso de Serviços II (S-II)**, CNAE 86.3, conforme Decreto 56.561/2025 (Anexo IV) c/c LC 270/2024 Art. 338 VIII. Recomendo (não decido) que o Anexo III revisado use essa nomenclatura técnica exata, e não a expressão coloquial da SMDU — risco de a própria prefeitura aceitar um enquadramento tecnicamente errado (Uso Institucional) que na prática seria mais favorável mas juridicamente frágil se um dia questionado. Isso toca o **Princípio 18 (Ética e conformidade em primeiro lugar)** — prefiro a classificação certa, ainda que dê mais trabalho, a uma classificação favorável mas errada.

**⚠️ REAVALIAÇÃO DE MÉRITO — CORRIGIDA EM 15/07/2026, com os parâmetros reais (ZRM2 G): isto deixou de ser "uso de faixa de contrapartida" e passou a ser ESTOURO DE CAM.**

Com CAM real = **1,0** (não 2,0): **CAM 1,0 × 500 m² de terreno = 500 m² máximo permitido pela lei.** O projeto pretende **980 m² brutos** — **quase o dobro do limite legal (980 ÷ 500 = 1,96x)**. Isso não é mais "dentro do limite, com folga pequena" (como o registro original, feito sobre o CAM 2,0 errado, concluía) — é **não conformidade grave de coeficiente de aproveitamento**, não uma questão de ajuste fino de projeto.

**Efeito sobre o ICS/contrapartida (pendência que eu já tinha sinalizado antes do erro ser corrigido) — reavaliada:** com o CAB real 0,6 (não 1,0) e o CAM real 1,0 (não 2,0), a "faixa de contrapartida" entre CAB e CAM é de **300 m² a 500 m²** (0,6×500 até 1,0×500), não de 500 a 1.000 m² como no cálculo errado. **A área pretendida de 980 m² está muito acima até do próprio teto do CAM (500 m²)** — ou seja, praticamente todo o excedente relevante (500 m² a 980 m², os 480 m² que excedem o CAM) está **fora da faixa CAB-CAM e fora do próprio CAM**, não é mais uma situação de "contrapartida a pagar dentro da faixa permitida". O **ICS real é 0,3** ("0,3 do CAM", não 0,8/"0,4 do CAM" como constava). Mesmo que a isenção de 5 anos da LC 270/2024 (que eu já havia sinalizado como não confirmada com confiança suficiente) se aplicasse ao ICS, isso resolveria no máximo a contrapartida da faixa 300-500 m² — **não tem como "comprar" ou compensar o estouro de CAM acima de 500 m²** por meio de ICS; isso exigiria outro instrumento (ex: transferência de potencial construtivo, se aplicável e disponível) ou redução do projeto. **Não decido qual caminho — sinalizo a Kelsen que a natureza do problema mudou**: de "confirmar se paga contrapartida" para "o projeto proposto excede o coeficiente de aproveitamento máximo do lote e precisa ser redimensionado ou buscar instrumento legal de aumento de potencial construtivo, se existir e for aplicável — o que eu não pesquisei ainda, por ser um problema novo exposto pela correção".

**Contradição exposta pela correção — para Kelsen resolver, não decido sozinho:** o item 9 abaixo (2ª submissão) trata este caso como "aprovado" na simulação de teste definida por Kelsen. Com o CAM real, a conclusão de mérito de "dentro do limite" que sustentava (em parte) aquele desfecho **não se sustenta mais** — ver observação registrada no item 9.

---

## ADENDO 15/07/2026 — ITEM 1/3-B — Operação Urbana Consorciada do Parque do Legado Olímpico Rio 2016 (Seção 6 do RIU, LC 284/2025)

**Não apaga a conclusão anterior (estouro de CAM na ZRM2 G, regime base) — camada adicional de pesquisa, mesmo lote (CL 476218).**

### Contexto do adendo
Claudemberg trouxe mais uma seção do print oficial do RIU que ainda não havíamos considerado — Seção 6, "Área de Abrangência de Operação Urbana": o lote está na **Área Receptora Setor III-H** da Operação Urbana Consorciada do Parque do Legado Olímpico Rio 2016 (LC 284/2025), com parâmetros divulgados no RIU: CAM 3 | TO 30% | Gabarito 12pav/36m | uso admitido "residencial multifamiliar, não limitado aos núcleos e sem limitação de área máxima para núcleos" — condicionados, por texto do próprio RIU, "ao atendimento das regras da legislação específica de cada Operação Urbana".

### Pesquisa realizada — fonte oficial
Busquei o texto integral da LC 284/2025 (Lei Complementar nº 284, de 17/07/2025, sancionada por "EDUARDO PAES, Prefeito"). Duas tentativas em agregadores de terceiros (leis.org, leismunicipais.com.br) retornaram erro 403. Consegui o texto oficial completo direto do **portal legislativo da Câmara Municipal do Rio de Janeiro** (`mail.camara.rj.gov.br/APL/Legislativos/contlei.nsf`) — baixei o HTML bruto via requisição direta (não só resumo de IA do WebFetch) e conferi artigo por artigo, arquivado em `Fontes_Legislacao/LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf` (ver entrada completa em `_indice_fontes.md`).

### Resposta 1 — Restrição de uso: LITERAL e EXCLUI este caso
**Art. 12, VI** (parâmetros do Setor III-H) confirma CAM=3, TO=30%, Gabarito 12pav/36m (bate com o RIU), mas a alínea **"d"** define o uso permitido como, **textualmente e sem mais nada**: *"uso residencial multifamiliar, não limitado aos núcleos e sem limitação de área máxima para núcleos"*.

Comparando com outros subsetores da mesma lei (mesmo artigo):
- **III-C/III-D e III-E**: "uso residencial multifamiliar, **comercial e serviços**" — têm abertura explícita para uso não residencial.
- **III-A**: "uso residencial multifamiliar **ou os previstos pela Lei Complementar nº 270, de 2024** e legislações correlatas" — tem cláusula de abertura para os usos já previstos na LUOS geral.
- **III-H**: **nenhuma das duas aberturas existe no texto** — só "residencial multifamiliar, não limitado aos núcleos e sem limitação de área máxima para núcleos".

**Conclusão, com fonte**: o pacote de parâmetros ampliados (CAM 3/TO 30%/gabarito 12pav-36m) do Setor III-H está atrelado, pelo texto literal do Art. 12, VI, "d", exclusivamente ao uso residencial multifamiliar. A clínica deste caso é **Uso de Serviços II (S-II), CNAE 86.3** (item 3 já registrado) — não é residencial multifamiliar. **A restrição de uso é literal e exclui este caso** — não encontrei, no texto da LC 284/2025, nenhuma hipótese de uso misto/comercial/institucional aplicável especificamente ao Setor III-H.

Nota à parte (não muda a conclusão acima, mas registro por transparência): o **Art. 11** da mesma lei — regra geral de elegibilidade de um lote para *receber* TDC, não específica de III-H — lista "serviços" entre os usos de zoneamento de base que habilitam um lote a ser receptor. Isso é sobre a elegibilidade abstrata do lote (o zoneamento de base, ZRM2 G, já permite uso de Serviços II conforme item 3), não sobre o uso final do pacote ampliado, que o Art. 12, VI, "d" restringe especificamente para III-H. Ou seja: o lote em tese poderia ser elegível a receber TDC pela via do Art. 11 (base permite "serviços"), mas o pacote de parâmetros ampliados que a TDC ativa para este subsetor específico (III-H) só é utilizável com uso residencial multifamiliar — não resolve o uso de clínica.

### Resposta 2 — Condições de aplicação: NÃO é automático, e há uma condição de vigência não confirmada
Não é automático só por estar na área receptora. Encontrei, com fonte:
- **Art. 9, §1º e Art. 14**: a Transferência do Direito de Construir (TDC) do Setor II (área cedente) para o Setor III (onde está III-H) exige **registro por escritura pública** e emissão, pela SMDU, de **Certidão de Potencial Construtivo Transferido**, mediante comprovação de pagamento ao proprietário cedente — é uma transação formal de aquisição de potencial construtivo, não um bônus automático do lote.
- **Art. 23**: para obter a licença de construção usando esse potencial construtivo, o requerente recolhe **contrapartida financeira própria desta OUC**, nos termos do art. 17 da LC 272/2024 e art. 17 da LC 273/2024, paga em 3 parcelas (20% na emissão da licença, 40% no início da obra, 40% no Habite-se/conclusão), destinada ao Fundo de Mobilidade Urbana Sustentável (FMUS). **Isso é distinto e adicional à ICS geral (0,3 do CAM) já registrada para o regime-base ZRM2 G** — são dois mecanismos de contrapartida diferentes, não alternativos.
- **Achado adicional relevante, não solicitado mas encontrado durante a pesquisa — Art. 51 (vigência)**: a lei entra em vigor de forma escalonada. Só os arts. 21, 22 e 49 (regras gerais de contrapartida institucional/cronograma/regulamentação) valem desde a publicação (17/07/2025). **"Nos demais casos e artigos" — o que inclui o Art. 12 (parâmetros por subsetor, inclusive III-H) e todo o mecanismo de TDC dos Arts. 9 a 11 — só entram em vigor "na data em que forem satisfeitas todas as condicionantes previstas no art. 21, incisos I e III"**, ou seja: (I) aprovação do *Masterplan* do Parque do Legado Olímpico e (III) aprovação dos PAA/PAL substitutivos do PAA 12.379/PAL 48.085. **Não pesquisei nem confirmei se essas duas condicionantes já foram satisfeitas até hoje (15/07/2026)** — isso é uma pendência de pesquisa adicional que fica em aberto, registrada abaixo.

### Isso muda a conclusão de mérito (estouro de CAM)? — NÃO muda, com uma pendência lateral registrada
**Não decido isso sozinho — mas o resultado da pesquisa, com fonte, é**: como o uso do projeto é clínica (Uso de Serviços II, S-II) e o Art. 12, VI, "d" da LC 284/2025 restringe literalmente o pacote ampliado do Setor III-H a "uso residencial multifamiliar" (sem abertura para outros usos, diferente de outros subsetores da mesma lei), **esta Operação Urbana não muda a conclusão de estouro de CAM já registrada no item 1/3 para este caso específico**. O regime aplicável ao mérito do caso continua sendo o regime-base da ZRM2 G (CAM 1,0, CAB 0,6, TO 50%), com os 980 m² pretendidos excedendo em quase o dobro o limite de 500 m² (CAM 1,0 × 500 m²).

**Pendência explícita para Kelsen (não decido sozinho)**: mesmo que, hipoteticamente, o uso fosse compatível (o que não é o caso aqui), ainda haveria a condição de vigência do Art. 51 (Masterplan e PAA/PAL substitutivos aprovados) não confirmada — não pesquisei isso porque a exclusão de uso (Resposta 1) já é suficiente, isoladamente, para não mudar a conclusão de mérito deste caso. Registro essa lacuna apenas para o caso de o julgamento de Kelsen precisar revisitar esta OUC num cenário futuro com uso residencial.

---

## ITEM 2 — Demolição prévia: PENDÊNCIA DE PESQUISA, não resolvida com confiança suficiente

Não tratei a demolição como trivial. Pesquisei o procedimento oficial (Portal Carioca Digital, serviço "Licença de demolição de edificação") e confirmei:
- É hoje descrito como **serviço próprio, separado** do LICIN de construção — prazo de 30 dias corridos, documentação própria (fotos 5x12, ART/RRT do responsável pela demolição, declaração Art. 3º Decreto 23235/2003, certidão de matrícula).
- **"A licença ou legalização é sempre para a totalidade do imóvel"** — o pacote deste caso (demolição total da casa de 140 m²) se encaixa nessa hipótese, não na de demolição parcial (que seria tratada como modificação).
- **O que eu NÃO consegui confirmar com fonte oficial suficiente**: se, no LICIN 2.0 (Decreto 55.622/2025), demolição total + construção nova no mesmo lote podem tramitar **dentro de um único processo/DULI** (com convenção de cores no desenho — amarelo para demolir, vermelho para construir, como um resumo de busca sugeriu) ou se **precisam ser dois processos formalmente separados** (1º a licença de demolição, só depois o LICIN da obra nova). Uma busca indicou essa convenção de cores; ao tentar confirmar acessando a página oficial diretamente, não consegui reproduzir essa informação com segurança — resultado inconclusivo entre as duas consultas.

**Registro como pendência ativa, não invento procedimento**: preciso que você (Kelsen) decida se isso exige checagem direta com a SMDU/1746 antes de eu redigir o DULI deste caso, ou se você já tem essa resposta na sua base retida. Não vou presumir um dos dois caminhos.

---

## ITEM 4 — Vagas e elevador: não repliquei os números do Anteprojeto

### Vagas (10 propostas, padrão residencial — não confirmado se serve)
Fonte: LC 270/2024, Art. 368 (Do Estacionamento e guarda de veículos):
- **Regra geral do Município**: dispensada exigência de vagas (§ caput).
- **Exceção — imóveis na AP4 (este é o caso)**: **exigida 1 vaga para cada 4 unidades residenciais, comerciais e/ou de serviços** (Art. 368, §1º, I).
- **Segunda exceção, que entendo prevalecer aqui**: **empreendimentos não residenciais considerados "polos geradores de viagens" (PGV) têm as vagas calculadas pelo próprio órgão municipal de trânsito** (CET-Rio), não por fórmula fixa da LUOS (Art. 368, §1º, II).

**Minha avaliação (julgamento próprio, não decisão final)**: uma clínica de 980 m², com subsolo de garagem, recepção/farmácia e 2 pavimentos de consultórios, tem porte e natureza de uso típicos de PGV — não encontrei, nas fontes que tive acesso, o critério exato (m² ou vagas-limite) que a CET-Rio usa para enquadrar um estabelecimento de saúde como PGV no Rio. **Não vou inventar um número de vagas.** O que posso afirmar com segurança:
- As **10 vagas em "padrão residencial" do Anteprojeto não têm base legal aplicável a este uso** — a regra de 1 vaga/4 unidades (Art. 368 §1º I) não foi pensada para um único imóvel de uso de saúde com múltiplos consultórios (não fica claro o que conta como "unidade" aqui), e se o empreendimento for PGV (bem provável dado o porte), a régua correta não é a LUOS, é a CET-Rio.
- **Adicional, independente do total**: Art. 368 §2º I exige vagas para pessoas com deficiência "na proporção que a norma específica determinar" — e o COES (LC 198/2019), Art. 29 §2º III, fixa **2% do total de vagas reservadas para PcD, com mínimo garantido de 1 vaga**.
- **Sinalizo como pendência real de pesquisa** (não é lacuna que eu resolvo sozinho): o número exato de vagas exigido depende de análise específica da CET-Rio como PGV — não é um parâmetro que uma tabela geral da LUOS me dá. Isso é diferente de "não pesquisei" — pesquisei e a resposta correta, tecnicamente, é "depende de órgão externo específico", não um número.

### Elevador (1 unidade, cabine 1,00 x 1,25 m — padrão residencial)
Fonte: ABNT NBR 9050:2020 (c/c NBR NM 313:2008, norma técnica específica de elevadores acessíveis) — **cabine mínima de 1,10 m x 1,40 m para elevador acessível em edificação de uso público/coletivo**.

**Avaliação**: a cabine de 1,00 x 1,25 m proposta **está abaixo do mínimo exigido para este tipo de uso** (não residencial/institucional de saúde, com atendimento ao público) — 1,00x1,25 m é dimensão típica de elevador residencial padrão, não do "Tipo 2" que a NBR 9050:2020 exige para uso público/coletivo. **Não recalculo aqui um número final "aprovado"** porque, tratando-se de estabelecimento de saúde, pode haver exigência adicional de vigilância sanitária (transporte de maca/paciente deitado) que vai além da própria NBR 9050 — não encontrei fonte oficial específica de vigilância sanitária municipal/estadual sobre isso neste caso, então **não afirmo um tamanho de cabine "correto e final"**, só que 1,00x1,25 m está comprovadamente abaixo do piso mínimo geral (1,10x1,40m) e precisa ser refeito — sinalizo a possível exigência extra de vigilância sanitária como pendência de pesquisa adicional, não decido isso sozinho.

---

## ITEM 5 — Anexo III (edificação nova), confirmado

Como há demolição total seguida de construção nova (não modificação de edificação existente), o quadro de áreas correto é o **Anexo III (edificação nova)**, não o Anexo IV (usado nos 2 casos anteriores, que eram modificação/ampliação). Consistente com o próprio pacote do caso.

---

## ITEM 6 — Pendência de PREO (bloqueio documental ativo)

LICIN 2.0 exige Requerente + PRPA + PREO identificados e assinando a Declaração de Responsabilidade (Anexo II). Neste caso:
- **PRPA**: identificado — Arqto. Fábio Noronha Salgueiro (Estúdio Bruma), CAU A000001-1-TESTE, ART-TESTE-2026-0031 já emitida. Regra fixa (Claudemberg): assinatura é de quem produziu o projeto arquitetônico — parceiro externo aqui, então a assinatura é dele, não da Sttickler. **Isso eu só registro, não decido.**
- **PREO**: **NÃO CONFIRMADO.** "Construtora executora: A DEFINIR — em processo de contratação", com pré-indicação informal (Constrular Engenharia TESTE Ltda., Eng. Thiago Meireles Falcão, CREA RJ-000000-2-TESTE) **sem ART/RRT emitida**.

**Registro como pendência ativa (não finjo resolvido)**: sem PREO formalmente identificado e com ART/RRT emitida, a Declaração de Responsabilidade (Anexo II) não pode ser assinada de forma completa, e o protocolo formal do processo real não pode avançar além da simulação deste teste. Isso é bloqueio documental, independente de qualquer mérito técnico já resolvido acima.

---

## ITEM 7 — Risco de ausência de AVCB/Corpo de Bombeiros (sinalizado desde já)

Nenhum documento do pacote menciona AVCB (Auto de Vistoria do Corpo de Bombeiros) ou qualquer interlocução com o CBMERJ. Isso não bloqueia o LICIN em si (que é competência da SMDU), mas **é relevante desde já**, não só na hora da Declaração de Compatibilidade (Anexo V, antes da obra): uso de saúde (clínica com atendimento ao público, elevador, múltiplos pavimentos) tende a se enquadrar em exigências mais rígidas de segurança contra incêndio do que uma residência unifamiliar — o projeto de prevenção e combate a incêndio (PPCI) tipicamente precisa estar compatibilizado com o projeto arquitetônico **antes** da obra avançar, não depois. Registro isso como risco ativo desde já, não como surpresa de última hora.

---

## ITEM 8 — Simulação fixa do acompanhamento SMDU (dado fixo do teste, não pesquisado)

- Processo: **LICIN-TESTE-2026-0000789**
- 18 dias depois: **PEDIDO DE AJUSTE**
- Motivo (texto dado por Kelsen): DULI apresenta uso como "comercial genérico", sem enquadramento correto conforme a LUOS. Reclassificar como "institucional de saúde" (ou equivalente) e reapresentar Anexo III com vagas recalculadas para uso não residencial — as 10 vagas atuais estão abaixo do exigido para 980 m² nesse enquadramento.

## ITEM 9 — Reenvio (2ª submissão) — considerado aprovado

**⚠️ CONTRADIÇÃO EXPOSTA PELA CORREÇÃO DE 15/07/2026 — registro, não decido sozinho.** Esta simulação de 2ª submissão foi definida por Kelsen como "aprovada" no cenário de teste original (14/07/2026), numa época em que o registro de mérito do CAM (item 1/3) apontava "dentro do limite, com folga pequena" (base: CAM errado de 2,0). Com o CAM real (1,0) confirmado por fonte oficial, **500 m² é o máximo permitido e o projeto pretende 980 m²** — quase o dobro do limite legal (ver reavaliação de mérito no item 1/3). **Isso torna a simulação de "aprovado na 2ª submissão" logicamente inconsistente com o dado real**: um projeto que estoura o CAM em quase 100% não seria, no mundo real, aprovável apenas reclassificando o uso e recalculando vagas — o problema de coeficiente de aproveitamento continuaria de pé, independente do enquadramento de uso. **Não decido sozinho se o caso "teria sido reprovado de verdade"** — isso é julgamento de Kelsen (e, se for o caso, de Wallenberg): pode ser tratado como (a) a simulação de teste permanece como estava, por ser cenário fictício fixado antes da correção, só com a ressalva de inconsistência registrada; ou (b) o desfecho do caso-teste precisa ser reaberto/refeito à luz do dado real. Registro a contradição, não escolho o caminho.

Reclassifiquei o uso com o enquadramento tecnicamente correto levantado nos itens 1/3 (**Uso de Serviços II — S-II, CNAE 86.3**, não "institucional de saúde" literal) e registrei que as vagas não podem ser simplesmente "recalculadas" por uma fórmula da LUOS — o caminho correto é análise de PGV pela CET-Rio (item 4). Para efeito desta simulação de teste (Kelsen definiu a 2ª submissão como aprovada), o Anexo III revisado assume o enquadramento de uso correto e registra a vaga PGV como pendência resolvida administrativamente **fora** deste teste (análise CET-Rio simulada como concluída, sem o número exato ter sido fornecido a mim — sinalizo que, num caso real, eu não teria como fechar isso sozinho).

**Emissão (simulada, 2ª submissão aprovada):**
- Minuta da Licença — construção nova, uso Serviços II (saúde)
- Guia de arrecadação (DARM)
- Anexo III revisado — uso reclassificado (S-II, CNAE 86.3, conforme Decreto 56.561/2025), vagas conforme análise PGV (não recalculadas por fórmula simples da LUOS)
- Termo de Responsabilidade

---

## ITEM 10 — O que falta para a Declaração de Compatibilidade (Anexo V) — NÃO dou como pronto

Antes de considerar este processo pronto para a obra começar, faltam, no mínimo:
1. **PREO formalmente confirmado, com ART/RRT emitida** (item 6) — hoje "a definir".
2. **Situação do AVCB/Corpo de Bombeiros resolvida** (item 7) — hoje nenhuma menção no pacote.
3. Como consequência direta de 1 e 2: a Declaração de Responsabilidade (Anexo II) e a futura Declaração de Compatibilidade (Anexo V) **não podem ser fechadas** com o pacote atual.

---

## ITEM 11 — Roteamento pós-aprovação

- Não passa por Compatibilização (fluxo é de Arquitetura, não de Legal) — segue direto para a fila de espera do **Gate 16 (Liberação de Obra)** quando aprovado.
- Fechamento de obra: **Habite-se** (não Aceitação de Obras) — porque a edificação existente foi demolida e o resultado é unidade nova, diferente de reforma/modificação.

---

## ITEM 12 — Compilação da prancha do Projeto Legal (A1) — ver arquivo separado

Ver `prancha_A1_compilacao_TESTE.md` nesta mesma pasta — descrição completa do layout, folhas e conteúdo, seguindo POP-ARQ-PL-01 e o Memorial Descritivo — Projeto Legal.

---

## Pendências e sinalizações consolidadas (para Kelsen auditar)

1. **PREO** — não confirmado, sem ART/RRT. Bloqueio documental para Anexo II e protocolo real.
2. **AVCB/Corpo de Bombeiros** — ausência total de menção no pacote. Risco para Anexo V, sinalizado desde já.
3. **Demolição + construção nova no mesmo processo** — não confirmei com fonte oficial suficiente se tramitam juntas (1 DULI) ou separadas (2 processos). Pendência de pesquisa explícita — não inventei procedimento.
4. **Vagas (PGV)** — não é lacuna, é dependência de órgão externo (CET-Rio); não calculei um número, porque a LUOS não define esse número para este tipo de empreendimento.
5. **Elevador** — cabine proposta (1,00x1,25m) comprovadamente abaixo do mínimo NBR 9050:2020 (1,10x1,40m); tamanho final "correto" pode exigir norma adicional de vigilância sanitária que não tive como confirmar — não afirmei um número final.
6. **Contrapartida/ICS (CAM acima do CAB) — ATUALIZADO 15/07/2026, mudou de natureza.** Com os parâmetros reais (CAB 0,6/CAM 1,0/ICS 0,3), deixou de ser "uso de faixa de contrapartida" e passou a ser **estouro de CAM**: 980 m² pretendidos vs. 500 m² máximo (CAM 1,0 × 500 m²) — quase o dobro do limite legal. Não é mais uma pendência de "confirmar se paga ICS", é achado de **não conformidade grave de coeficiente de aproveitamento**, que expõe contradição com o desfecho simulado no item 9 (2ª submissão "aprovada"). Ver reavaliação completa no item 1/3 e a contradição registrada no item 9.
7. **Nomenclatura do enquadramento de uso** — a resposta simulada da SMDU usa termo ("institucional de saúde") que não corresponde à categoria formal correta da lei (Uso de Serviços II); sinalizo o risco de usar nomenclatura tecnicamente errada mesmo que a prefeitura a tenha sugerido.
8. **Erro de zoneamento corrigido (15/07/2026)** — este processo registrou originalmente "ZRM3 subzona O" para este lote, usando a API ArcGIS da SMDU geocodificada por CEP. Claudemberg confirmou via print oficial do RIU (`mapas.rio.rj.gov.br`) que a zona/subzona real é **ZRM2 G**, com parâmetros bem diferentes (CAM 1,0 não 2,0; TO 50% não 70%; ICS 0,3 não 0,8; gabarito 4pav/14m em ambos os regimes, não 8pav/26m e 3pav/11m). Investigação de causa raiz (evidência real, refeita em 15/07/2026): uma geocodificação correta do CEP/logradouro (2 fontes independentes convergentes) aponta exatamente para o ponto que a API oficial confirma como ZRM2 G a tolerância zero — ou seja, o método "geocodificar por CEP" não é, em si, a causa do erro. A zona ZRM3 O existe de fato no cadastro da SMDU, mas fica cerca de 10-14 km de distância do imóvel (região de Jacarepaguá/Freguesia/Taquara, não Recreio). Reproduzi uma consulta com tolerância de busca espacial superestimada (parâmetro `tolerance` desproporcional ao par `mapExtent`/`imageDisplay`) e ela de fato varre um raio de vários quilômetros, trazendo dezenas de zonas de toda a cidade — incluindo a ZRM3 O real, distante — misturadas na mesma resposta. Isso é evidência concreta de um mecanismo técnico real (consulta espacial mal configurada, tolerância efetiva de vários km) combinado com erro de extração (pegar a feature errada de uma resposta com múltiplas features), não de imprecisão de geocodificação por CEP em si. Ver detalhe completo em `Fontes_Legislacao/_indice_fontes.md`. **Regra de processo daqui pra frente**: essa API não deve mais ser tratada como fonte forte sozinha — sempre cruzar contra o RIU real antes de qualquer protocolo.
9. **Recuo lateral/gabarito — ATUALIZADO 15/07/2026, pendência mudou de natureza com o dado real.** Com a subzona real ZRM2 G, o gabarito é **4pav/14m nos DOIS regimes** (afastado e não afastado — não há vantagem de gabarito por se afastar das divisas, diferente do que constava no registro errado de ZRM3 O). O gabarito pretendido de 11,80 m cabe folgadamente sob o limite de 14 m em qualquer um dos dois regimes — deixou de existir a obrigatoriedade de adotar o regime "afastado das divisas" que o registro anterior (errado) apontava. Isso, em tese, **alivia** a urgência de confirmar o recuo lateral mínimo do COES (2,50 m ou 1/5 da altura) para fins de gabarito — mas não elimina a pendência em si: o pacote continua sem me dar o recuo lateral/de fundos proposto pelo Anteprojeto, e ele ainda precisa ser conferido por outros motivos (afastamento mínimo geral do COES, coerência de implantação). Fica como pendência de conferência antes de fechar a prancha (ver Seção 7.2 do POP no arquivo da prancha), agora com risco reduzido (não mais crítico para o gabarito), não eliminada.
10. **Operação Urbana Consorciada do Legado Olímpico (Setor III-H, LC 284/2025) — pesquisada e registrada em 15/07/2026, não muda a conclusão de estouro de CAM.** A Seção 6 do RIU trouxe parâmetros ampliados (CAM 3/TO 30%/gabarito 12pav-36m) para o lote, por estar na Área Receptora Setor III-H dessa Operação Urbana. Pesquisa em fonte oficial (LC 284/2025, texto integral obtido do portal da Câmara Municipal do Rio) confirma que o Art. 12, VI, "d" restringe **literalmente** o uso do pacote ampliado a "residencial multifamiliar" — sem abertura para comercial/serviços/institucional, diferente de outros subsetores da mesma lei. Como o uso deste caso é clínica (Serviços II), **a Operação Urbana não se aplica ao mérito deste caso** — a conclusão de estouro de CAM na ZRM2 G (regime-base) permanece de pé. **Pendência lateral registrada, não resolvida (irrelevante para este caso por causa da exclusão de uso, mas relevante para casos futuros com uso residencial no mesmo setor)**: o Art. 51 da LC 284/2025 condiciona a vigência do Art. 12 (parâmetros por subsetor) à aprovação prévia do Masterplan e dos PAA/PAL substitutivos (Art. 21, incisos I e III) — não pesquisei se essas condicionantes já foram cumpridas. Ver seção completa "ADENDO 15/07/2026 — ITEM 1/3-B" acima e entrada em `Fontes_Legislacao/_indice_fontes.md`.

## Dificuldades reais na execução (para avaliação de confirmação oficial)

- O sistema oficial `mapas.rio.rj.gov.br` (RIU) não é acessível por mim via WebFetch/WebSearch de forma direta (é um mapa interativo). Contornei isso usando a API pública de geoprocessamento da própria SMDU (ArcGIS REST, `pgeo3.rio.rj.gov.br`) por coordenada — **⚠️ atualizado em 15/07/2026: essa API foi rebaixada para "indicativo de baixa confiança"** depois do erro de zoneamento real confirmado neste mesmo caso (ver item 8 das pendências consolidadas e `Fontes_Legislacao/_indice_fontes.md`). Não trato mais como fonte forte — preciso cruzar sempre contra o RIU real antes de qualquer protocolo.
- Um WebFetch (resumo por IA de página de terceiros) me deu uma informação sobre convenção de cores (amarelo/vermelho) que não consegui reproduzir de forma confiável numa segunda tentativa direta na página oficial — preferi reportar a inconsistência a Kelsen (item 2) a decidir sozinho qual das duas está certa.
- O Decreto nº 56.561/2025 (tabela de usos por CNAE/zona) só ficou legível para mim depois de converter o PDF baixado para texto localmente (pdftotext) — o WebFetch direto não conseguiu extrair o conteúdo da primeira vez (arquivo tratado como binário/comprimido). Registro isso porque, num ambiente sem essa ferramenta de conversão local, eu não teria conseguido confirmar o enquadramento de uso (item 3) com a mesma confiança.
