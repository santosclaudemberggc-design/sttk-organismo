---
name: legal-base-legislativa-bairro
description: Base legislativa urbanística do Rio de Janeiro por bairro/subzona — onde encontrar e como confirmar zona, subzona e parâmetros (CAB, CAM, TO, gabarito, afastamentos, lote mínimo, ICS, SMD) de um lote específico, com a hierarquia de confiabilidade das fontes e as armadilhas já confirmadas. Use sempre que um caso de Projeto Legal exigir parâmetro urbanístico de um endereço, antes de montar DULI/Anexos, quadro de áreas ou prancha, e sempre que a equipe de Arquitetura pedir a consulta obrigatória desde o Levantamento.
---

# Base legislativa por bairro/subzona — Rio de Janeiro

Skill da área Legal do Sistema Orgânico STTK. Quem consome na prática: **Hely** (Agente executor). Quem retém e decide quando aplicar: **Kelsen** (Gestor Legal).

## O que esta Skill é — e o que ela deliberadamente não é

**É um mapa: onde está a fonte, como confirmar, e o que costuma dar errado.**

**Não é um repositório de parâmetros.** Você não vai encontrar aqui o CAB da ZRM3 D, o afastamento da sua zona nem o mínimo em metros de nada. Isso é intencional, e a razão é cara: em 20/07/2026 esta Skill nasceu com um erro material sobre afastamento lateral, copiado do nosso próprio `_indice_fontes.md` — que também estava errado, e cujo erro sobreviveu a **três rodadas de análise** do mesmo caso antes de alguém abrir o artigo. Paráfrase de paráfrase.

No mesmo dia descobrimos o outro lado do problema: quando esta Skill guardava os parâmetros, ela virava a **terceira cópia** da mesma regra (briefing do Gestor, arquivo de estado do Agente, e ela) — três lugares para desatualizar em vez de um (Princípio 15, Redundância zero).

**Regra que decorre disso, e vale contra este documento inclusive: o número final sai do texto legal ou do RIU, nunca de um resumo nosso.** Esta Skill te leva até lá e te avisa onde há armadilha. A resposta você lê na fonte.

## Hierarquia entre as normas — diferente de confiabilidade da fonte

São duas hierarquias distintas, e confundi-las produz erro grave. Esta aqui é **jurídica**: quem manda em quem.

**Lei Complementar > Lei Ordinária > Decreto > Resolução/Portaria.**

- **Decreto regulamenta lei; não a altera.** Não pode criar obrigação nova, restringir direito nem contrariar o que a lei estabeleceu. Decreto que extrapola é ilegal e contestável.
- **Onde decreto e lei conflitarem, a lei vence.** Antes de aceitar uma exigência ou uma recusa que só aparece em decreto, **cheque se a lei diz o contrário**. Exemplo vivo, e **já testado até o fim**: o Decreto 55.622/2025 (Anexo I, Condições Gerais, 1) diz que "não serão aceitas plantas baixas dos pavimentos, fachadas...". **RESOLVIDO em 21/07/2026: a recusa do decreto SE SUSTENTA.** Nem o COES nem a LUOS exigem essas peças (varredura: `planta baixa` = 0 nos dois; as ocorrências de `fachada` são todas materiais, não procedimentais), e a **LC 270/2024, Art. 276, parágrafo único delega expressamente o procedimento de licenciamento a ato do Poder Executivo** — o decreto exerce delegação, não extrapola. Consequência comercial: nossa Planilha de Enviáveis vende "fachadas legais" e "memorial para protocolo legal", peças que a prefeitura não recebe no DULI — correção dos documentos do Drive é decisão de Claudemberg.
- **"Planta do pavimento" ≠ "planta baixa" no vocabulário do decreto.** O Anexo I, III exige a primeira (contorno, cotas, ATE, projeção, ocupação); o IV.1 recusa a segunda (layout interno). O modelo oficial confirma: contornos hachurados, sem parede interna, porta, janela ou nome de ambiente.
- **Resolução de secretaria é o degrau mais baixo** e regulamenta um decreto específico. Quando aquele decreto é substituído, a resolução fica em situação incerta — não some sozinha, mas perde a âncora. Verifique caso a caso; não presuma nem que morreu, nem que sobreviveu.

**Vigência — armadilha registrada em 21/07/2026:** decreto **não** expira no fim do ano em que foi assinado. Vale até ser revogado ou substituído. O que expira com prazo são atos com vigência declarada (licença, alvará, portaria temporária). Confira sempre o artigo de vigência e a cláusula de revogação do próprio texto — não presuma por idade do documento.

## PASSO OBRIGATÓRIO — cheque o status do ato antes de citá-lo

**A base oficial Busca Fácil da SMU** (`www2.rio.rj.gov.br/smu/buscafacil`) entrega **status jurídico por ato** e texto consolidado, sem login. É a única fonte que diz se uma norma ainda está de pé.

**Antes de citar qualquer lei, decreto ou resolução numa peça, confirme o status ali.** Não é etapa opcional nem "quando houver dúvida" — é passo do processo (Princípios 9 e 20).

Por que virou obrigatório, em 21/07/2026: uma auditoria descobriu que o organismo conhecia **1 de 6** normas que alteram a LC 270/2024, e vinha operando **quatro artigos revogados** da LC 274/2024 (derrubados pela LC 281/2025, Art. 42, II). Nenhum deles apareceu por leitura de texto — só apareceriam pela consulta de status. **Citar artigo revogado num protocolo é vício grave.**

Dois usos distintos, não confunda:
- **Status do ato** — "esta lei/artigo ainda vale?" Busca Fácil.
- **Texto do artigo** — "o que ele diz exatamente?" PDF primário arquivado.

**Cadência:** a base envelhece rápido. A LC 301/2026 saiu doze dias antes desta auditoria, e a própria SMU alerta na ficha da LC 270/2024 para verificá-la. **Base parada uma semana já pode estar errada.** Reverifique status a cada caso real, não a cada trimestre.

## Hierarquia de confiabilidade das fontes

Da mais forte pra mais fraca. Fonte mais forte sempre vence a mais fraca, sem exceção:

1. **RIU oficial da SMDU** (`mapas.rio.rj.gov.br`, Consultas Urbanas) — Certidão/Relatório de Informações Urbanísticas do lote. Palavra final. Exige localização em mapa/lote; Hely não acessa direto, então quando for necessário confirmar visualmente, **sinalize a Kelsen** em vez de contornar.
2. **API ArcGIS oficial da SMDU** (`pgeo3.rio.rj.gov.br/arcgis/rest/services/`) — fonte forte, **mas somente sob o pipeline do `POP-LEGAL-RIU-01`**. Fora do POP, é fonte fraca.
3. **Texto de lei baixado e arquivado** (PDFs em `Fontes_Legislacao/`) — leia o artigo, não o resumo.
4. **Compilação de terceiro** — site, PDF de terceiro, resumo de IA, **e também qualquer paráfrase interna nossa**. Indicativo de baixa confiança. Nunca vira parâmetro final.

## Onde procurar cada coisa — endereços, não valores

| O que você precisa | Onde está definido |
|---|---|
| **CAB** | LC 270/2024 **Art. 345, §4º** — o CAB por subzona está aqui. **Não está no Anexo XXI**, que não tem coluna de CAB (erro corrigido em 20/07/2026, depois de a base interna ter declarado essa informação como "lacuna não localizável") |
| **CAM** | LC 270/2024 Art. 103-104, 107; Anexo XXI, por Área de Planejamento |
| Taxa de Ocupação | LC 270/2024 Art. 349 (fórmula) + Anexo XXI (máximo por zona) |
| Gabarito | LC 270/2024 Anexo XXI — valores distintos para "afastado" e "não afastado das divisas" |
| Afastamento **frontal** | LC 270/2024 Art. 363 + Anexo XXI |
| Afastamento **lateral e de fundos** | **Não está na LC 270/2024** — Art. 364 delega ao COES (LC 198/2019). Ver bloco próprio abaixo |
| SMD / permeabilidade | LC 270/2024 Art. 351-353 |
| ATE (Área Total Edificável) | LC 270/2024 Art. 346-347, com as exclusões listadas |
| Usos permitidos por zona | LC 270/2024 Art. 338 (categorias) + Decreto 56.561/2025 (detalhe por CNAE e por AP) |
| Outorga onerosa (CAB->CAM) | **LC 281/2025, Arts. 18-19** — primário **arquivado** (`LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`). Art. 18 traz as fórmulas por tipologia; Art. 19, o parcelamento e os descontos; Art. 20 condiciona a licença à quitação. `POP-LEGAL-02` foi reescrito em 28/07/2026 sobre a LC 281/2025 (verbatim, auditado por Kelsen) — quarentena encerrada, pode ser usado como fundamento novamente |
| Janela de contrapartida com desconto | **LC 281/2025 Art. 40**, na redação da **LC 301/2026 Art. 58** — janela **aberta até 01/12/2026**, com 30% de desconto à vista sobre acréscimos além da legislação ordinária. **Verbatim conferido em 24/07/2026 direto no PDF arquivado da LC 301/2026** (`Art. 58. O art. 40 da Lei Complementar nº 281 [...] passa a vigorar com a seguinte redação [...]`) — não há ambiguidade de artigo; "Art. 58" é o dispositivo da LC 301 que altera, "Art. 40" é o dispositivo alterado da LC 281. Ainda assim, confirme o status (Válido) no Busca Fácil antes de prometer ao cliente |
| Zoneamento do lote | `POP-LEGAL-RIU-01` — obrigatório, sem pular a trava GeoPAL |

## Armadilhas confirmadas — cada uma custou um erro real

Estas são checagens a fazer, não respostas a copiar. Em toda elas, **abra o artigo citado**.

### Ler tabela do Anexo XXI
- **O mesmo nome de zona existe em Áreas de Planejamento diferentes, com valores completamente diferentes.** "ZRM3 D" aparece na AP2 e na AP4. Um `grep` devolve a AP2 primeiro. **Confira o cabeçalho do bloco de AP antes de ler qualquer linha.** Near-miss real em 20/07/2026 — parâmetro de lote da Zona Sul quase foi aplicado a uma casa no Recreio.
- `pdftotext -layout` **desalinha** essas tabelas. Use `pdftotext -table`.

### Afastamento lateral — quatro artigos, não um
O erro histórico foi tratar isso como uma regra só. São quatro perguntas independentes, e cada uma tem artigo próprio no COES:
1. **Qual é o mínimo aplicável a esta tipologia?** Art. 4º II e §1º II dão a regra geral — mas **unifamiliar/bifamiliar tem número próprio no Art. 31, parágrafo único**, que é diferente. Nunca aplique o do Art. 4º a uma casa sem passar pelo Art. 31 antes.
2. **Ficar abaixo do mínimo é infração?** Não necessariamente — joga a edificação no regime **"não afastado das divisas"** (Art. 4º §1º II), que é categoria legal e cujo preço é gabarito menor.
3. **O regime "não afastado" libera tudo na divisa?** Não. **Art. 8º §3º** (varandas e sacadas) e **Art. 9º IV** (marquises) continuam exigindo distância. É aqui que projetos reprovam.
4. **Aquela fachada tem abertura?** Faixa estreita pode não se qualificar como afastamento nem como prisma (Art. 5º §1º) — e então **nenhum compartimento de permanência prolongada pode iluminar ou ventilar por ali** (Art. 17 §1º e §3º; proporção mínima no Art. 18). Sem saber a geometria e as aberturas, a resposta honesta é condicional.

### Preexistente vs. obra nova
- **Não existe direito adquirido de afastamento** — nem no COES, nem na LC 270/2024 (verificado em busca no texto integral). O que existe é caminho **oneroso** de legalização por contrapartida do que já foi executado. **[ATENÇÃO] O FUNDAMENTO ANTIGO CAIU (21/07/2026):** a base citava **LC 274/2024 Art. 38**, **revogado** pela **LC 281/2025, Art. 42, II** — que derrubou os arts. 5º-14, 17-23, 26 e 38 daquela lei. A conclusão segue válida; **o endereço mudou**. Reconstrua sobre a **LC 281/2025, Arts. 18-19** (primário arquivado). **Citar artigo revogado em protocolo é vício grave.**
- **Obra nova não herda tolerância do preexistente.** Responde pela regra ordinária por conta própria.
- **Contrapartida compra área, não compra habitabilidade** — leitura correta; o fundamento antigo (LC 274/2024 Art. 12 §2º) caiu no mesmo bloco revogado. Reconstrua também sobre a **LC 281/2025, Arts. 18-19**.
- **Em modificação de preexistente, a outorga incide só sobre o que ultrapassa o preexistente** — LC 270/2024 Art. 108.

### Enquadramento e vigência
- **Clínica privada com fins lucrativos não é "Uso Institucional de interesse público"** (Art. 338 XVI, reservado a entidades sem fins lucrativos), mesmo que a SMDU use "institucional de saúde" informalmente. Confirme o CNAE no anexo da AP correta do Decreto 56.561/2025.
- **Lote abaixo do mínimo NÃO aumenta CAB/CAM.** Loteamento fechado legaliza o parcelamento (PAL/direito adquirido), não o coeficiente.
- **ICS = Índice de Comércio e Serviços** — não "Compensação Social" (`POP-LEGAL-04`).
- **Decreto 3.046/1981 não está revogado.** A LC 270/2024 o referencia em pontos específicos (Art. 363 §1º III; Art. 435). Cheque se o lote cai numa dessas exceções — sem presumir que nunca vale nem que é a regra geral.
- **Operação Urbana Consorciada tem vigência escalonada.** Na LC 284/2025, os parâmetros ampliados só valem satisfeitas as condicionantes do Art. 21. **Parâmetro ampliado que aparece no RIU não é automático** — pode exigir TDC por escritura pública, Certidão da SMDU e contrapartida própria. Confirme vigência antes de usar.
- **Sempre cheque se a lei foi substituída.** Se um texto aparece como "substituído por", busque o que substituiu e traga resultado concreto com fonte.

### Risco que não barra o protocolo, mas não some
**Código Civil art. 1.301** (janela/varanda perto da divisa) é matéria **civil**: a SMDU não indefere por isso, mas o Alvará não blinda o cliente contra ação do vizinho, e o **COES Art. 39 §1º** joga a responsabilidade no autor do projeto. **Sinalize sempre** (Princípio 18) — sobretudo quando o PRPA for Claudemberg. Um projeto pode estar 100% conforme e ainda deixar o cliente exposto.

## Como usar esta Skill

1. Identifique o lote real (endereço + número + lote/quadra), não só a rua. **Nunca geocodifique por CEP de terceiro** — o centroide da faixa pode cair a mais de 1 km e mudar a zona; já aconteceu duas vezes no Recreio.
2. Rode o `POP-LEGAL-RIU-01` de ponta a ponta, sem pular a trava do `GeoPAL`.
3. Cheque restrições sobrepostas: AEI, AEIS, Áreas Protegidas, APAC, APP. **Todo caso unifamiliar padrão precisa da Licença Municipal Ambiental Simplificada (LMS), trâmite paralelo ao LICIN 2.0, não coberto por ele** (ver "Trâmite paralelo obrigatório — Licenciamento Ambiental Municipal (LMS)" acima).
4. Vá aos artigos da tabela acima e **leia o texto**. Passe pelas armadilhas da seção anterior.
5. Registre coordenada literal, parâmetros da requisição e **fonte de cada número** no arquivo do caso (Princípio 8).
6. **Se não der pra confirmar com confiança, diga isso.** Não invente parâmetro, não arredonde pra "parece razoável", não complete lacuna geométrica. Sinalize a pendência a Kelsen.

## Escopo, crescimento e manutenção

Cobertura atual: **Recreio dos Bandeirantes, Barra da Tijuca, Vargem Grande** (AP4). Cresce **por demanda** — só entra bairro novo quando houver cliente real dele (Princípio 19).

Lacuna que você encontrar **não vira conhecimento oficial por decisão sua**. Reporte a Kelsen; ele avalia e leva a Wallenberg, que formaliza (Função 5).

**Se você encontrar uma armadilha nova, ela pertence aqui** — armadilha não expira do mesmo jeito que parâmetro. Reporte para inclusão.

## Fontes arquivadas

Em `01_CEO/Gestores/Kelsen (Legal)/Agentes/Hely/Fontes_Legislacao/`, com índice comentado (data de download, proveniência e **status jurídico**) em `_indice_fontes.md`. A seção COES do índice **foi corrigida em 20/07/2026** contra o texto literal, com o histórico do erro preservado — mas a regra de sempre continua: **o número final sai do PDF primário, não do índice**.

**Núcleo:**
- `LC270_2024_PlanoDiretorLUOS.pdf` — Plano Diretor / LUOS (384 p.)
- `COES_LeiComplementar198_2019_CONSOLIDADO_SMU.pdf` — **use esta versão**, consolidada pela SMU. As outras duas cópias do COES na pasta são anteriores às alteradoras
- `Decreto55622_2025_LICIN2.0.pdf` + `_AnexoI_ModelosDULI.pdf` + `_AnexoII_TermosDeclaracoes.pdf` — o procedimento e as peças. **O Anexo I é imagem pura; só se lê rasterizando**

**Alteradoras da LC 270/2024 e correlatas** (conhecíamos 1 de 6 até 21/07/2026):
- `LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf` — **outorga/contrapartida vigente (arts. 18-19)**; revogou blocos da LC 274/2024
- `LC283_2025_AlteraCOES_Art35.pdf` — inclui o §7º: **dutos no passeio obrigatórios em toda nova edificação**
- `LC291_2025_SupermercadosShoppingsHospitais.pdf` — **confirmado no primário** (inclui o Art. 2º §7º, parcelamento de lote bifamiliar)
- `LC292_2025_RiscoEstrutural.pdf`, `LC299_2026_AlteraLC270_Art371.pdf`, `LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf`
- `LC274_2024_CONSOLIDADO.pdf` — **leia com o mapa de revogações ao lado**; grande parte caiu
- `LC284_2025_OperacaoUrbanaLegadoOlimpico.pdf` — OUC Parque do Legado Olímpico
- `Decreto56561_2025_UsosPorZona_AnexosICES.pdf` — usos por CNAE e por zona

**Resoluções:** `ResolucaoSMDEIS03_2023_SubstituicaoPREO.pdf` (Válido — permite protocolar com PREO inicial e substituir depois); `ResolucaoSMDEIS27_2021_LICIN_BaixaComplexidade_SEM_EFEITO.pdf` — **sem efeito, não use**: não existe rito de baixa complexidade, unifamiliar segue as três etapas.

POPs em `.../Agentes/Hely/POPs/`: `POP-LEGAL-RIU-01` (zoneamento), `POP-LEGAL-02` (outorga — **em reescrita, fundamento revogado**), `POP-LEGAL-03` (demolição), `POP-LEGAL-04` (rótulo ICS), `POP-LEGAL-05` (**conteúdo exigido para protocolo — o mais completo**).

## Trâmite paralelo obrigatório — Licenciamento Ambiental Municipal (LMS), todo unifamiliar

**Incorporado como conhecimento ativo em 28/07/2026, decisão de Claudemberg.** Achado auditado três vezes por Kelsen contra o texto primário (27/07, 2ª e 3ª passagens; 28/07 zona cinzenta fechada) antes de virar regra de trabalho — não é mais lacuna, é exigência confirmada.

- **O quê:** todo lote **unifamiliar padrão** — mesmo **sem nenhum gatilho ambiental do Anexo II do LICIN 2.0** (sem vegetação a remover, sem curso d'água próximo, sem risco geológico) — está **sujeito** à **Licença Municipal Ambiental Simplificada (LMS)**. Fundamento: **Decreto 51.503/2022, Arts. 26-27** (Capítulo VI, baixa complexidade). É **obrigação, não faculdade** — decisão fechada em 28/07/2026 por acúmulo de 4 pontos textuais/estruturais (Art. 13 §2º trata o enquadramento como status, "sujeitos"; o Art. 17/CMI é o único instrumento do decreto inteiro qualificado expressamente como "facultativo"; o Art. 24/LAC usa a mesma fórmula "passível de" e o Art. 25 esclarece que é roteamento automático, não escolha; os Capítulos V/VI são desvio obrigatório de rito, não alternativa eletiva ao regime geral do Art. 20). Ver `_indice_fontes.md`, seção "DECISÃO DE KELSEN — 28/07/2026 (3ª passagem) — ZONA CINZENTA DO ART. 27 FECHADA", para a citação verbatim completa.
- **Órgão e trâmite:** **SMAC**, não SMDU. **É trâmite paralelo ao LICIN 2.0, não absorvido por ele** — o Decreto 55.622/2025 não menciona PGRCC nem LMI em nenhuma linha; sua única ponte com a SMAC é a autodeclaração de "passivo ambiental" do Anexo II (Res. SMAC 605/2015, resolução diferente da que trata de PGRCC, a 512/2012). O LICIN 2.0/SMDU termina em Habite-se; o LAM/SMAC termina em **LMS** — são dois processos, dois protocolos, dois resultados.
- **O que a LMS dispensa:** lote unifamiliar padrão fica **dispensado só do regime pleno (LMP/LMI) e do PGRCC**, que só incide acima de ATC 10.000 m²/movimento de terra 5.000 m³ (Res. SMAC 512/2012, Art. 1º). Não fica dispensado da LMS em si.
- **Impacto no nosso trabalho:** novo entregável/trâmite que **nenhuma peça hoje contempla** (Projeto Legal, Planilha de Enviáveis, proposta comercial). Ao mapear escopo de um caso real, **inclua a LMS na lista de trâmites do projeto**, sinalizando a Kelsen se ela ainda não estiver prevista no orçamento/cronograma do caso.
- **Ressalvas que seguem de pé, sem afetar a obrigação em si:** (a) Decreto 52.712/2023 não indexado no Busca Fácil, só citação cruzada; (b) identidade do "PGRCC" do achado original com o da Res. SMAC 512/2012 não confirmada em primário adicional (não muda a conclusão sobre a LMS).

**Lacunas conhecidas:** Decreto 45.917/2019 (regulamento do COES) não lido — agregadores devolvem HTTP 403; tentar pela Busca Fácil. Lista de documentos do protocolo inacessível (requerimento on-line atrás de login).

**Segurança contra incêndio e pânico (CBMERJ/COSCIP) — trâmite ESTADUAL paralelo ao LICIN 2.0, identificado em 28/07/2026.** O Decreto Estadual nº 42/2018 (COSCIP-RJ), administrado pelo CBMERJ (órgão estadual, não municipal), regula Auto de Vistoria e regularização contra incêndio — matéria ausente do Decreto 55.622/2025 (zero menção a bombeiro/incêndio no corpo municipal). Mesma família estrutural do achado SMAC/LAM acima: lei central muda sobre um trâmite não prova que ele não incide.

- **Endereço:** `Art. 3º, §2º, I` do Decreto 42/2018 — *"Estão isentas de regularização junto ao CBMERJ: I - edificação residencial privativa unifamiliar [...]"* — isenta a edificação residencial privativa unifamiliar de regularização junto ao CBMERJ, sem condicionante adicional no texto do inciso.
- **Como confirmar:** o texto oficial consolidado (`cbmerj.rj.gov.br`) foi lido do Art. 1º ao 71 por Wallenberg em 28/07/2026 — nenhum outro artigo reintroduz obrigação de regularização para unifamiliar puro (Art. 20 trata de quem NÃO está regularizado; Art. 41 é poder de fiscalização, não cria obrigação nova). **Falta ler a NT 1-07** do CBMERJ (Nota Técnica à parte, fora deste decreto, editada sob Art. 3º §3º/Art. 7º) antes de tratar a isenção como "nenhuma obrigação resta".
- **Pendência aberta (B10, fila do Kelsen):** localizar e ler a NT 1-07 — só ela pode confirmar se edificação isenta de regularização formal ainda deve cumprir medida mínima de segurança contra incêndio.
- **Armadilha:** não confundir "isento de regularização formal junto ao CBMERJ" com "dispensado de toda medida de segurança contra incêndio" — são perguntas diferentes; a segunda depende do texto da NT 1-07, ainda não lida. Fontes secundárias (blogs) citam uma ressalva ("sem áreas comuns") que **não aparece** no texto do inciso I conforme lido — não usar essa ressalva sem confirmação primária.
- **Fonte primária:** a arquivar em `Fontes_Legislacao/Decreto42_2018_COSCIP_CBMERJ_COMPILADO.pdf`, com entrada correspondente no `_indice_fontes.md` (data/URL/método de download, no mesmo padrão das demais normas já arquivadas) — download já feito por Wallenberg em 28/07/2026, falta ao Hely arquivar formalmente e concluir B10.
