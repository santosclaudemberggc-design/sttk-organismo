---
name: selca-decreto50473-2026-licenciamento-ambiental-estadual-obra-residencial-rj
description: O novo SELCA, o sistema estadual de licenciamento ambiental do RJ (Decreto Estadual 50.473, de 15/09/2026, que revogou o Decreto 46.890/2019 e incorporou a Lei Geral do Licenciamento, Lei Federal 15.190/2025). Cobre quando uma obra residencial na Barra/Recreio esbarra no INEA, além da LMS municipal da SMAC; quais instrumentos estaduais continuam exigíveis (outorga ou uso insignificante de água, FMP, APP, supressão); como se regulariza uma obra iniciada sem o instrumento estadual (procedimento corretivo); e a regra de transição para processos em curso. Use sempre que Hely (ou Kelsen) for checar exigência ambiental de lote perto de lagoa, canal, restinga ou APP; for orientar rebaixamento de lençol, aterro, terraplenagem ou canteiro; ou for responder se o "INEA precisa entrar", mesmo que o pedido só mencione "licença ambiental", "INEA", "FMP", "faixa marginal" ou "lagoa", sem citar o decreto pelo nome.
version: v1.2
status: ativa-com-ressalva
validacao: "Kelsen 01/10/2026 — PROCEDE COM RESSALVA (R1-R6, seção 12). Todos os artigos conferidos por Kelsen contra o texto integral extraído do DOERJ (selca.txt). Corrigidos: alcance do Art. 41 (só dispensas dos Arts. 38-39), base da multa no corretivo (Art. 91, não Art. 94), prazos de licença (Arts. 46-52, não Art. 57), condição do Art. 74, Certificado de Uso Insignificante (Art. 102). Sem contradição de valor com Skill ativa."
changelog:
  - "v1.0 (01/10/2026, Wallenberg) — proposta, Rotina Diária de Skills v3.5.0"
  - "v1.1 (01/10/2026, Kelsen) — validação de Gestor dono: 6 correções factuais, prazos novos conferidos nos Arts. 46-52, leitura da seção 8 reescrita como tese condicionada, exceção APP/alagadiça do Dec. 51.503/2022 incluída, ressalvas R1-R6"
  - "v1.2 (05/10/2026, Kelsen) — LC Federal 140/2011 lida no Planalto (Art. 9º, XIV e XV; Art. 12; Art. 13, §§ 1º-2º). R1 passa a PARCIALMENTE FECHADA (CONEMA de impacto local continua pendente); ressalva (2) do topo reescrita; nova R7 (lote em APA: a APA não define competência, Art. 9º, XIV, b, e Art. 12). Backup: 01_CEO/Decisoes_Autonomas/_backups/2026-10-05/selca_SKILL_ANTES_v1.2.md"
fonte_primaria_lida: "Decreto Estadual 50.473/2026, texto integral do DOERJ de 16/09/2026 (Arts. 5º-13, 27, 37-52, 74, 89-94, 101-102, 116-120 e Anexo I, Grupo XXVI), conferido por Kelsen em 01/10/2026; LC Federal 140/2011, texto do Planalto (Arts. 9º, XIV-XV; 12; 13), conferido por Kelsen em 05/10/2026"
data: 2026-10-01
tipo: Inteligência (Trilha A)
gestor_alvo: Kelsen (Legal)
agente_principal: Hely (Projeto Legal)
agentes_cross: Baumgart (rebaixamento, contenção, aterro), Saturnino (uso de água em obra), Glaziou (supressão de vegetação)
---

# Skill: SELCA (Decreto Estadual 50.473/2026) e a obra residencial na Barra/Recreio: quando o INEA entra

> ⚠️ RESSALVA DE FONTE. (1) **Lido no texto primário:** o Decreto Estadual 50.473, de 15/09/2026 (PDF do DOERJ de 16/09/2026, assinado digitalmente, obtido da cópia publicada por Mattos Filho). Todos os artigos citados abaixo foram conferidos no texto por Kelsen em 01/10/2026. (2) **Competência Município × Estado, lida em parte (05/10/2026):** a LC Federal 140/2011 (texto do Planalto) foi conferida por Kelsen. Art. 9º, XIV: o Município licencia o que causar impacto ambiental **de âmbito local**, "conforme tipologia definida pelos respectivos Conselhos Estaduais de Meio Ambiente" (alínea a), ou o que estiver em UC instituída pelo Município, "**exceto em Áreas de Proteção Ambiental (APAs)**" (alínea b). Art. 9º, XV, b: supressão de vegetação em empreendimento licenciado pelo Município é aprovada pelo Município. Art. 12: em APA não vale o critério do ente que criou a UC, vale o de impacto local. Art. 13: **um único ente** licencia; os demais se manifestam de forma **não vinculante** (§ 1º); a supressão é autorizada pelo **ente licenciador** (§ 2º). **Continua não lida:** a resolução do CONEMA com a tipologia de impacto local. Sem ela, a LC 140 diz **quem** faz a lista, mas não **se** a casa está nela. O decreto só cita a LC 140 nos considerandos e **não traz** artigo de competência municipal. A conclusão de que "casa unifamiliar se licencia na SMAC, não no INEA" vem da Skill `legal-base-legislativa-bairro` (LMS, Dec. Municipal 51.503/2022), **não deste decreto**. (3) As normas operacionais do INEA que o decreto manda editar (custos, LAC por tipologia, inexigibilidade por CNAE, critérios de prazo) **ainda não existem ou não foram lidas**. (4) A obrigação de outorga para uma casa licenciada na SMAC vem da legislação de recursos hídricos (Lei Federal 9.433/1997, Lei Estadual 3.239/1999, Res. CERHI-RJ 221/2020), **não lida aqui**: este decreto só define o instrumento.

## 1. POR QUE ESSA SKILL EXISTE

Desde 29/09 está aberta a pendência "SELCA: o que muda para obra residencial perto de lagoa na Barra/Recreio" (Hely). A Skill de rebaixamento citava o decreto **só pelo LegisWeb**, e só um artigo sobre rede elétrica. Agora o texto foi lido inteiro nos pontos que importam ao escritório. A pergunta real de Hely é: **"além do licenciamento ambiental municipal da SMAC, o INEA precisa entrar nesta obra?"**

## 2. O QUE O DECRETO É (texto primário)

- **Decreto 50.473, de 15/09/2026**, publicado no DOERJ de 16/09/2026. Revoga as disposições em contrário, **"em especial o Decreto Estadual nº 46.890/2019 e suas alterações"** (Art. 120), e entra em vigor na publicação (Art. 119). As exceções são a fila cronológica (Art. 8º) e o Art. 24, §§ 1º-2º (despacho virtual), para os quais o INEA tem **180 dias** de adaptação de sistema.
- O decreto incorpora a **Lei Geral do Licenciamento (Lei Federal 15.190/2025)** e a **LAE (Lei Federal 15.300/2025)** (ementa).
- **Instrumentos do SELCA (Art. 5º):** licença, autorização, certidão, certificado, **outorga de direito de uso de recursos hídricos**, termo de encerramento e documento de averbação.
- **Quatro procedimentos (Art. 44):** ordinário (trifásico); simplificado (bifásico, fase única ou **por adesão e compromisso, a LAC**); especial (LAE); e corretivo. **O empreendedor pode optar** entre ordinário, simplificado e especial. Havendo incompatibilidade fundamentada, a autoridade converte a licença na mais adequada, respeitado o contraditório (Art. 44, parágrafo único).
- **Onze tipos de licença (Art. 45):** LAI, LP, LI, LIO, LO, LAC, LAU, LOR, LAR, LAE e LOC.
- **Prazos máximos de vigência (conferidos no texto):** LAI até 6 anos (Art. 46, § 4º); LP até 6 anos (Art. 47, p.ú.); LI até 6 anos (Art. 48, § 3º); LIO até 10 anos (Art. 49, § 1º); LO de 5 a 10 anos (Art. 50, § 1º); LAC de 4 a 8 anos (Art. 51, § 4º); LAU de 5 a 10 anos (Art. 52, § 1º). Dentro do intervalo, o INEA fixa o prazo por critérios de sustentabilidade em norma própria (Art. 57).

## 3. A OBRA RESIDENCIAL ESTÁ NA LISTA? (Anexo I, Grupo XXVI, "Construção Civil")

O Anexo I lista como sujeitas a licenciamento, entre outras: "**Construções novas e acréscimos de edificações**", "Implantação de **loteamentos** residenciais", "**Corte e aterro** para nivelamento de greide (terraplenagem)", "Realização de **aterro sobre espelho d'água** (hidráulico)", "Realização de **serviços geotécnicos**" e "Implantação e operação de **canteiro de obras**".

**Leitura correta (não confundir):** estar no Anexo I não significa que o INEA licencia a casa. A lista diz **o que é licenciável** (Art. 37, § 1º). **Quem** licencia (Município ou Estado) é questão de competência (LC 140/2011), que o decreto não trata (ressalva 2). Para a casa unifamiliar padrão na Barra/Recreio, o trâmite ambiental é a **LMS na SMAC** (Skill `legal-base-legislativa-bairro`). **Atenção ao cenário desta Skill:** lote com APP ou área alagadiça sai da LMS e cai no rito ordinário municipal **LMP + LMI** (Dec. Municipal 51.503/2022, Art. 27, p.ú., II e IV, conforme a mesma Skill). Continua municipal, mas não é mais simplificado. O SELCA entra pelos **instrumentos que continuam estaduais**, listados na seção 4.

## 4. INSTRUMENTOS ESTADUAIS QUE PODEM INCIDIR NA OBRA RESIDENCIAL

| Situação na obra | Instrumento estadual | Base no decreto |
|---|---|---|
| Rebaixamento de lençol, poço ou captação na obra | **Outorga** (Art. 5º, V), ou, se o uso for insignificante, **Certificado de Uso Insignificante** (Art. 102, § 1º, VI) ou **Certidão de inexigibilidade de uso insignificante** (Art. 101, X). Para reservar vazão antes da obra: **Outorga Preventiva** (Art. 102, § 1º, I, até 3 anos) | O decreto define o instrumento; a obrigação vem da lei de recursos hídricos (ressalva 4). Detalhe técnico e limite de vazão na Skill `rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio` |
| Lote junto a lagoa, canal ou rio (Marapendi, Jacarepaguá, Tijuca, canais do Recreio) | **Certidão Ambiental de demarcação da Faixa Marginal de Proteção (FMP)** | Art. 101, IX |
| Dúvida se o lote toca APP, reserva legal ou unidade de conservação **estadual** | **Certidão de conformidade** com APP, reserva legal e UC estaduais | Art. 101, V |
| Atividade dispensada de licença **pelos Arts. 38 ou 39** (emergência, rede elétrica, manutenção, agropecuária etc.) | A dispensa **não** afasta os instrumentos de supressão de vegetação nativa, de uso de recursos hídricos e outros (Art. 41, I). **Não confundir:** o Art. 41 vale só para essas dispensas, não para a casa licenciada na SMAC | Art. 41, I |
| Prova de que a atividade dispensada (Arts. 38-39) não precisa de licença | **Certidão de inexigibilidade**: facultativa; sem ela não há sanção, salvo notificação prévia do INEA; gratuita quando automática no portal (Art. 41, II e p.ú.; Art. 101, IV). Para atividade fora do caput do Art. 37: **declaração eletrônica de inexigibilidade por CNAE**, que depende de resolução do INEA (Art. 37, § 3º) | Arts. 37, § 3º; 41, II; 101, IV. O decreto **não** tem certidão de "competência municipal" para a casa |

**Regra prática para Hely:** lote residencial perto de corpo hídrico na Barra/Recreio → pedir a **certidão de FMP** (Art. 101, IX) **antes** de fixar a implantação. A faixa demarcada muda o afastamento real e, portanto, o partido de Lúcio. A largura da FMP não está neste decreto.

## 5. OBRA JÁ INICIADA SEM O INSTRUMENTO ESTADUAL: PROCEDIMENTO CORRETIVO

Vale quando o que falta é instrumento **estadual** (ex.: outorga). Falta de LMS/LMP-LMI é assunto municipal, fora deste decreto.

- Quem iniciou ou prosseguiu com instalação ou operação sem o instrumento regulariza pelo **corretivo** (Art. 9º; Capítulo IV).
- **Obra instalada ou em instalação** → **Certidão de Regularização**, precedida de **termo de compromisso** (Art. 89, I; Art. 92, que inclui "obras hidráulicas").
- **Brecha válida (Art. 89, § 2º):** o termo de compromisso **pode ser dispensado** quando a instalação, mesmo sem licença, **não tiver causado nenhum dano** e **não houver necessidade de qualquer obra ou intervenção** para adequação. Documentar a ausência de dano (laudo de RT) é o que abre esse caminho.
- A **LOC** (Arts. 56, 89-II e 93) só serve para atividade que **já operava em 08/12/2025** sem licença, e só a pedido espontâneo. Não é caminho para obra nova.
- **Regularizar não apaga a responsabilidade:** os instrumentos do corretivo não afastam a apuração da responsabilidade administrativa e criminal nem a reparação do dano (Art. 91), e a autoridade define medidas compensatórias pela falta de licença (Art. 89, § 5º). (O auto de infração do Art. 94, I é do rito específico da LOC.)

## 6. PROCESSO EM CURSO: REGRA DE TRANSIÇÃO

- O decreto vale para processos iniciados **após** a entrada em vigor (Art. 117, caput).
- Processo anterior: as obrigações e cronogramas já fixados valem **até concluir a etapa atual**, salvo decisão específica e fundamentada da autoridade; as **etapas seguintes** seguem o decreto novo (Art. 117, § 1º, I e II).
- **Brecha válida (Art. 117, § 2º):** a aplicação do decreto aos processos em curso **não deve** implicar reinício de análise, novos estudos ou complementações adicionais (salvo risco ambiental relevante fundamentado), "**assegurada a adoção do procedimento mais simples e favorável quando compatível com a proteção ambiental**".

## 7. REGRAS DE TRÂMITE QUE O ESCRITÓRIO USA A SEU FAVOR

- **Complementação uma única vez (Art. 6º, § 1º):** o INEA pode exigir, fundamentadamente, documentação suplementar **uma única vez**, ressalvados fatos novos. Segunda exigência sem fato novo é contestável. A exigência **suspende** os prazos do Art. 27, que voltam a correr após o atendimento integral (Art. 6º, § 4º).
- **Arquivamento não é derrota (Art. 6º, § 3º):** indeferimento por exigência não atendida ou custo não pago permite **novo protocolo** de mesmo teor, com novo custo de análise.
- **Conversão de instrumento (Art. 7º):** o INEA pode converter o instrumento pedido em outro, ajustando os custos, mas precisa avisar antes. O empreendedor tem **15 dias para se opor**.
- **Boa-fé (Art. 11):** estudos e informações do empreendedor e do RT têm **presunção de boa-fé e veracidade**. Omissão ou informação falsa gera responsabilização, e o INEA comunica o **Conselho de Classe** (CAU/CREA) e o Ministério Público (p.ú.). É risco direto para a RRT de Claudemberg: nada de declarar "sem dano" sem laudo.
- **RT obrigatório (Art. 12, § 1º, I):** **loteamentos, condomínios e marinas sujeitos a licenciamento** exigem responsável técnico de acompanhamento, com relatórios periódicos das condicionantes (§ 2º). Na baixa do RT, o empreendedor tem **30 dias** para indicar outro, sob pena de suspensão da licença (§ 3º).
- **Certidão municipal de uso do solo (Art. 74):** o INEA **pode** exigir certidão do Município sobre uso e ocupação do solo **quando a viabilidade ambiental estiver indissociavelmente ligada a essas normas** (ou em hipóteses de norma do INEA). Quando não exige, a conformidade urbanística vira **condicionante** (§ 1º). O LICIN/SMDU e o INEA andam juntos, um não substitui o outro (§ 2º).
- **LAC ainda não serve para obra civil:** a implantação é gradual por tipologia, e a norma operacional a editar em até 6 meses cobre só **abastecimento de água, esgotamento sanitário e silvicultura econômica** (Art. 116). E a LAC não se aplica a quem já começou sem licença (Art. 51, § 5º, I). Não prometa LAC para construção.

## 8. MACETES DE QUEM FAZ

- **Revisar licenças e processos em curso agora, não na renovação.** Luiz Gustavo Bezerra, Gedham Gomes, Victor Rodrigues e Rodrigo de Avilez Demoro (Mayer Brown, nota de 24/09/2026) recomendam que empreendedores "avaliem os impactos das novas regras sobre suas licenças vigentes e seus processos em curso". A nota compara os prazos: **LAI e LI de 8 para 6 anos**, **LP de 5 para 6 anos**, **LO e LAU de 6-12 para 5-10 anos**. Os valores **novos** foram conferidos no decreto (seção 2). Os valores **antigos** (Dec. 46.890/2019) vêm só da nota: não lidos (R2).
- **Tese de Kelsen, sem fonte de profissional (não é regra):** Art. 117, § 2º (procedimento mais simples e favorável na transição) somado ao Art. 44, parágrafo único (opção do empreendedor pelo procedimento) sustenta, pelo texto, pedir a **conversão para o simplificado** de processo antigo enquadrado no ordinário. Limites do próprio texto: (a) a etapa em curso segue as obrigações já fixadas, então a conversão vale para as **etapas seguintes** (Art. 117, § 1º); (b) o INEA pode negar por incompatibilidade fundamentada (Art. 44, p.ú.) ou por risco ambiental relevante (Art. 117, § 2º); (c) não leva à LAC em obra civil (Art. 116; Art. 51, § 5º, I). Para a casa unifamiliar da Sttickler, licenciada na SMAC, a tese raramente se aplica. Uso em caso real só depois do Gate do Maurício.

## 9. CHECKLIST DE HELY

- [ ] O lote confronta ou fica próximo de lagoa, canal ou rio? → pedir **certidão de FMP** (Art. 101, IX) antes da implantação, e checar se o lote cai na exceção APP/alagadiça do Dec. 51.503/2022 (LMP+LMI em vez de LMS)
- [ ] A obra vai bombear água (rebaixamento, poço)? → **outorga**, ou **certificado/certidão de uso insignificante** (Art. 102, § 1º, VI; Art. 101, X); ver a Skill de rebaixamento
- [ ] Há vegetação nativa a suprimir, APP ou UC estadual? → instrumento próprio de supressão, ou **certidão de conformidade** (Art. 101, V); a parte municipal está na Skill de remoção de árvores
- [ ] Há aterro sobre espelho d'água ou terraplenagem relevante? → está no Anexo I, Grupo XXVI: confirmar competência (SMAC × INEA) antes de protocolar (R1)
- [ ] Obra já começou sem instrumento estadual? → corretivo; laudo de "sem dano" para dispensar o termo de compromisso (Art. 89, § 2º)
- [ ] Processo estadual iniciado antes de 16/09/2026? → Art. 117: etapa atual mantida; pedir o procedimento mais favorável nas seguintes
- [ ] Segunda exigência de complementação sem fato novo? → contestar com o Art. 6º, § 1º

## 10. RELAÇÃO COM OUTRAS SKILLS (coerência v3.4.0, Kelsen 01/10/2026)

- **`legal-base-legislativa-bairro`** (LMS/SMAC, trâmite paralelo ao LICIN): **Complementa**. A competência municipal da casa unifamiliar e a exceção APP/alagadiça moram lá. Esta Skill cobre só o que é estadual. Sem valor em conflito.
- **`rebaixamento-lencol-freatico-obra-outorga-inea-barra-recreio`**: **Complementa**. Lá estão o limite de vazão, a base de outorga (CERHI 221, Res. INEA 63) e a técnica. Aqui estão os instrumentos estaduais (Art. 5º, V; Art. 101, X; Art. 102, § 1º, I e VI). O Art. 38, IV que aquela Skill cita pelo LegisWeb foi conferido no primário e **está correto** ("travessia hidráulica ou rebaixamento freático", alínea "b"). A ressalva (6) daquela Skill passa de "não verificado" para "verificado no DOERJ". Sem valor em conflito.
- **`remocao-arvores-smac-fpj-autorizacao-compensacao-rj`**: **Diferente**. Aquela trata da supressão na esfera municipal (SMAC/FPJ). Esta só aponta o instrumento estadual (certidão de conformidade APP/UC, Art. 101, V). Sem valor em conflito.

## 11. FONTES

- Decreto Estadual 50.473, de 15/09/2026, DOERJ de 16/09/2026, texto integral. Cópia lida: https://www.mattosfilho.com.br/wp-content/uploads/2026/09/decreto-estadual-no-50473-2026.pdf (texto extraído com pypdf em 01/10/2026; artigos conferidos por Kelsen no mesmo dia)
- Mayer Brown, "Rio de Janeiro decree amends environmental licensing to incorporate LGLA rules", 24/09/2026: https://www.mayerbrown.com/pt/insights/publications/2026/09/rio-de-janeiro-decree-amends-environmental-licensing-to-incorporate-lgla-rules

## 12. AVALIAÇÃO DO GESTOR (Kelsen, 01/10/2026)

**Veredito: PROCEDE COM RESSALVA (`ativa-com-ressalva`).** Fonte primária lida e conferida artigo a artigo. Sem duplicata e sem contradição de valor com Skill ativa.

- **R1 (PARCIALMENTE FECHADA em 05/10/2026):** competência SMAC × INEA. **Lido:** LC 140/2011, Art. 9º, XIV e XV, Art. 12 e Art. 13, §§ 1º-2º (ressalva 2 do topo). O que a LC 140 garante: um só ente licencia, e a supressão segue quem licencia. Se a SMAC licencia a casa, a autorização de supressão também é municipal (Art. 9º, XV, b; Art. 13, § 2º), o que reforça a remissão à Skill de remoção de árvores. **Pendente:** a resolução do CONEMA com a tipologia de impacto local, que é o que põe ou não a casa unifamiliar na competência municipal. Até lá, "casa unifamiliar = SMAC" continua apoiada na Skill `legal-base-legislativa-bairro` (LMS, Dec. 51.503/2022), não na LC 140.
- **R2:** os prazos **antigos** de licença (Dec. 46.890/2019) vêm só da nota da Mayer Brown. Os novos foram conferidos (Arts. 46-52).
- **R3:** a seção 8 traz tese de Kelsen (Art. 117, § 2º + Art. 44, p.ú.), sem fonte de profissional. Só serve para etapas seguintes e só entra em caso real depois do Gate do Maurício.
- **R4:** a obrigação de outorga vem da legislação de recursos hídricos, não lida aqui (ressalva 4 do topo; R1 da Skill de rebaixamento).
- **R5:** as normas operacionais do INEA (custos, LAC por tipologia, CNAE, critérios de prazo) não existem ou não foram lidas.
- ~~**R6:** treino em caso fictício com Hely~~ — retirada por Wallenberg em 01/10/2026: o treino em caso fictício foi extinto na Rotina Diária v3.5.0 (30/09/2026, decisão de Claudemberg). O teste em situação próxima do real agora é o Ensaio Sombra 003.
- **R7 (nova, 05/10/2026): lote em APA** (ex.: APA de Marapendi e outras APAs da Barra/Recreio). Estar em APA **não** muda quem licencia: a alínea b do Art. 9º, XIV exclui APA do critério de UC municipal, e o Art. 12 manda usar, em APA, o critério de impacto local (Art. 9º, XIV, a). A conclusão da Skill não muda, mas a competência em APA também depende da resolução do CONEMA (R1). **Não lidos:** a esfera de cada APA (municipal ou estadual), o zoneamento e o plano de manejo de cada uma, e a regra de manifestação do órgão gestor da UC no licenciamento. Em lote dentro de APA, Hely confirma esses três pontos antes da implantação. A manifestação de outro ente é não vinculante (Art. 13, § 1º), mas as restrições de uso da APA continuam valendo.
