# Proposta de equipe do Fechamento (etapas 14 a 17)

**Autor:** Lelé (Gestor Fechamento, nível Shadow), 10/10/2026
**Pedido:** Wallenberg, aplicando a decisão D5 de Claudemberg (aprovada em 10/10/2026)
**Revisão 2 (10/10/2026):** Claudemberg leu a v1 (2 Agentes) e pediu um terceiro Agente, só de Projeto Executivo. Nas palavras dele: "ele monta as pranchas executivas que vão para a obra com as informações, tabelas e detalhamentos pegos com os outros agentes, ele é o responsável por compilar todas as informações, ver se é um projeto exequível e manda para obra e vê também se não está faltando informação ou documento, ele que monta o Memorial Descritivo final." Esta versão substitui a v1.
**Status:** PROPOSTA. Nada foi criado: nenhum arquivo de agente, nenhuma pasta de Agente. Em Shadow eu proponho. A aprovação é de Claudemberg, via Wallenberg, antes de qualquer criação.

---

## 1. Resumo

Proponho **3 Agentes novos**.

| Agente | Etapas | Em uma linha |
|---|---|---|
| **Zanettini** | 14 | Cruza as disciplinas, prioriza os conflitos de interface por GUT, abre um RFI para cada conflito, cobra a resposta e mantém o registro de RFIs |
| **Reidy** | 15 inteira, o dossiê do Gate 16 e o pacote para a obra | Compila pranchas, tabelas e detalhes de todos, confere se o conjunto é exequível e se está completo, escreve o Memorial Descritivo final e o caderno de encargos, monta o dossiê do Gate 16 e, depois da liberação, entrega o pacote |
| **Limmer** | 16 | Faz o orçamento executivo analítico (quantitativo, composição SINAPI/TCPO com data-base, BDI, encargos, premissas) e compara com a estimativa de viabilidade |

A **etapa 17 (Gate 16) não tem Agente.** É uma decisão binária, minha e de Wallenberg juntos, na hora. O Reidy monta o dossiê que a gente lê. **Não decide e não libera.**

**O que mudou desde a v1:**
- A etapa 15 e o dossiê do Gate 16 saíram do Zanettini e foram para o Reidy.
- O Zanettini ficou só com a etapa 14.
- O argumento da v1 de que "sem desenho, um executivo seria um Agente vazio" caiu. A missão que Claudemberg descreveu é, na maior parte, **compilar e conferir**: completude, exequibilidade, Memorial Descritivo final. Isso dá para fazer hoje, em texto, sobre o material que chega dos outros. Só a montagem da prancha no Revit fica com "desenho pendente — Vitruvius" (seção 3).

**Não proponho reaproveitar o Mascaró como executor do orçamento.** Explico na seção 5.

---

## 2. Zanettini — Compatibilização (etapa 14)

**Nome:** Siegbert Zanettini, arquiteto e professor da FAU-USP, conhecido por obras industrializadas (aço) e por projetos hospitalares em que estrutura, instalações e arquitetura eram coordenadas desde o início. É a mesma linhagem do Lelé na Rede Sarah: o projeto já nasce compatível. *Incerteza: tenho confiança razoável na associação com construção industrializada e projeto hospitalar. Não conferi os detalhes biográficos em fonte primária.*

**Etapa:** 14 (Compatibilização). Só ela.

**Missão:**
1. Receber o pacote completo: Anteprojeto (Lúcio), os 6 complementares (Cardozo) e o Legal (Kelsen). Recusar se faltar insumo e dizer qual falta. Não compatibiliza projeto incompleto.
2. Cruzar disciplina contra disciplina pelas 10 categorias da Skill `compatibilizacao-projetos`, sempre olhando **o ponto onde duas fontes se encontram**: viga contra tubo, quadro contra parede molhada, cota de arquitetura contra cota de estrutura.
3. Priorizar por GUT, com o item embutido em fundação ou no primeiro serviço no topo, e abrir **um RFI por conflito**, endereçado ao dono da disciplina pela cadeia. Ele não resolve.
4. Manter o **registro de RFIs** (aberto, respondido, fechado, ou aceito por mim com justificativa). É esse registro, atestado por ele, que o Reidy junta ao dossiê do Gate 16.
5. Toda verificação vem com prova no mesmo arquivo: uma tabela "conflito | onde (documento + página/prancha) | categoria | GUT | dono | RFI | status". Quando faltou insumo, ele escreve "não verifiquei X".

**Ferramentas:**

| Ferramenta | Situação | Para quê |
|---|---|---|
| Read, Write, Edit, Glob, Grep, Skill | **Existem** | Ler memoriais e pranchas (o Read abre PDF e imagem), escrever a matriz e os RFIs |
| Drive em leitura (`search_files`, `read_file_content`, `list_recent_files`, `get_file_metadata`) | **Existem** (o Oscar já tem) | Os entregáveis das disciplinas ficam no Drive |
| Vitruvius **só de leitura** (`get_document_info`, `get_levels`, `list_elements`, `find_elements`, `get_walls`, `get_floors`, `get_rooms`, `get_doors`, `get_windows`, `get_element`, `get_parameter`) | **Existem** no servidor (lista do `oscar.md`). Nenhuma ferramenta de escrita | Conferir cota, nível e ambiente no modelo do Oscar contra os memoriais |
| Skills `compatibilizacao-projetos`, `verificacao-automatica-conformidade-bim` e as Skills de norma de cada disciplina | **Existem** | Método e critério. *Não li o conteúdo da segunda para esta proposta.* |
| `check_clash` (C3) e `export_ifc` (C1) | **Faltam.** Planejados no `PLANO_AGENTE_GUIADO.md` (linhas 50 e 52) para depois das etapas 8–13 | Detecção de interferência em 3D. Sem elas, a etapa 14 é leitura 2D/texto |
| `export_view_image` (A1, Bloco 2) | **Falta** | Ver as vistas do modelo |

**Limite real que muda a etapa 14 hoje:** os Agentes de Cardozo entregam **memorial e dimensionamento em texto, sem desenho** (mapa de prontidão, linhas 13 a 18). A compatibilização no Ensaio 003 será, portanto, memorial contra memorial contra planta de arquitetura. Interferência de posição só aparece quando o memorial dá cota ou trajeto. O parecer tem de dizer isso; não pode vender o resultado como "compatibilizado".

**O que o Zanettini NÃO faz:**
- Não redimensiona nem corrige nenhuma disciplina. A correção é do Agente de Cardozo dono da disciplina, sempre pela cadeia.
- Não altera partido, planta nem modelo. Isso é de Lúcio e Oscar. Ele não escreve no Revit.
- Não decide conflito legal (afastamento, TO, gabarito). Esse tipo de conflito vira RFI para Kelsen pela cadeia, porque a Skill de compatibilização não cobre RIU/LICIN.
- **Não monta o executivo, não confere a completude do pacote final, não escreve memorial e não monta o dossiê do Gate 16.** Tudo isso é do Reidy. A saída dele é a matriz de conflitos mais o registro de RFIs.
- Não orça. Isso é do Limmer.
- Não aprova o Gate 16, não fala com o cliente e não fala com Wallenberg direto. A cadeia é Lelé → Zanettini → Lelé.

**Como será examinado (Formação → Shadow):**
- **Caso:** fictício, montado por mim, com o **gabarito lacrado escrito antes** da execução. O pacote é uma planta de arquitetura simples mais 6 memoriais curtos.
- **Iscas (mínimo 8):**
  - viga contra trecho de esgoto no shaft;
  - ralo em laje sem rebaixo;
  - quadro elétrico em parede hidráulica;
  - carga de cobertura verde que não está no memorial estrutural;
  - pé-direito com forro contra altura de viga;
  - divergência entre a prancha e o quadro de áreas;
  - um conflito **legal**, que ele precisa encaminhar e não resolver;
  - um item que **parece** conflito mas não é;
  - um insumo faltante, que ele precisa recusar em vez de presumir.
- **Critérios (nota 0–10, mínimo 8):** iscas encontradas; GUT coerente; RFI endereçado ao dono certo; nenhuma "correção" de disciplina alheia; prova item por item; "não verifiquei" onde faltou dado. **Reprova direto, qualquer que seja a nota:** declarar uma verificação sem prova, ou resolver sozinho o conflito legal.
- **Quem aplica:** eu monto o caso e o gabarito; Wallenberg aprova o caso antes de aplicar (porque estou em Shadow); Claudemberg ratifica a promoção.

---

## 3. Reidy — Projeto Executivo e pacote para a obra (etapa 15)

**Nome:** Affonso Eduardo Reidy, arquiteto carioca, autor do Conjunto do Pedregulho e do MAM-Rio, que passou a carreira no serviço público projetando o que de fato ia ser construído. Fica no Rio, como a Sttickler, e representa o projeto levado até a obra. *Incerteza: tenho confiança alta nas obras citadas e razoável na leitura "do projeto que vai para a obra". Não conferi os detalhes biográficos em fonte primária.*

**Etapa:** 15 inteira. Também o dossiê do Gate 16 e o pacote para a obra.

**Missão:**
1. **Compilar** o conjunto executivo a partir do que chega dos outros: as pranchas e os detalhes de arquitetura (Oscar, pela cadeia Lúcio), as pranchas e os memoriais dos complementares (equipe de Cardozo), o projeto licenciado (Hely, pela cadeia Kelsen), a matriz de RFIs fechados (Zanettini) e o quantitativo e o orçamento (Limmer). Monta a **lista de pranchas e documentos** (NBR 6492, 5.7.5 e) e a ordem do jogo.
2. **Conferir a completude** contra o jogo mínimo do PE da NBR 6492 (gráficos 5.7.3 a–f; escritos 5.7.5 a–e) e contra os documentos que a obra exige: ART/RRT de cada disciplina, licença LICIN com a declaração do Anexo V (Art. 4º §4º do Decreto 55.622/2025) e o plano de reporte dos 4 marcos do Art. 5º. A saída é uma **lista do que falta: o item, quem deve, e por qual cadeia cobrar**.
3. **Conferir a exequibilidade do conjunto final**: todo item especificado tem detalhe; todo detalhe chamado numa planta existe; a referência de nível é única (NBR 6492, 5.7.2); a especificação é compatível com o uso (por exemplo, piso de área molhada); há uma sequência executiva possível. O que for problema **entre disciplinas** volta para mim, e eu reabro a etapa 14 com o Zanettini. Ele não corrige.
4. **Escrever o Memorial Descritivo final** (5.7.5 a e b: elementos, componentes, materiais e instalações em seus aspectos arquitetônicos) e o **caderno de encargos**. Incorpora o memorial quantitativo e as planilhas do Limmer (5.7.5 c e d) sem refazê-los.
5. **Montar o dossiê do Gate 16** (seção 6) e, **só depois da liberação registrada**, preparar a entrega do pacote para a obra.
6. Prova em tudo: tabela "item exigido | fonte da exigência | presente? | onde (arquivo/prancha) | se falta, quem deve". Quando não conferiu algo, escreve "não verifiquei".

**"Manda para obra": a fronteira.** O Reidy **prepara e entrega** o pacote. A **liberação não é dele.** O pacote só sai depois que o Gate 16 for aprovado por mim e por Wallenberg, na hora, em decisão binária e registrada. Sem esse registro, ele não envia, por mais pressão de prazo que exista. Pressão para mandar antes ele sinaliza a mim (REGRA-ARQ-01 vale aqui também). Como o pacote é documento que chega a terceiros (obra, PREO, cliente), quem aperta o "enviar" e por qual canal é decisão de Claudemberg (seção 7, item 6). Até lá, a entrega dele termina no depósito do pacote liberado numa pasta definida.

**Ferramentas:**

| Ferramenta | Situação | Para quê |
|---|---|---|
| Read, Write, Edit, Glob, Grep, Skill | **Existem** | Ler pranchas em PDF e memoriais; escrever o checklist de completude, a lista de pranchas, o Memorial Descritivo final e o caderno de encargos |
| Drive em leitura | **Existe** | Juntar o material de todas as equipes |
| Drive `create_file` | **Existe** no organismo (Cardozo e Kelsen têm) | Depositar o pacote liberado na pasta da obra. Só depois do Gate 16, e só se Claudemberg aprovar (seção 7, item 6) |
| Vitruvius **só de leitura** (mesmo subconjunto do Zanettini) | **Existe** | Conferir no modelo o que as pranchas dizem: níveis, ambientes, aberturas |
| Skill `nbr6492-2021-memoriais-por-etapa-projeto` | **Existe e é aproveitável** (v1.1, ativa-com-ressalva, lida por Lúcio na fonte primária) | É o **checklist de completude** do PE: lista os gráficos (5.7.3) e os 5 escritos obrigatórios (5.7.5), e diz que o (c) e o (d) alimentam o orçamento. Ressalva R1: a Seção 4 da norma (formatos, carimbo) não foi lida |
| Skills `nbr6492-representacao-grafica`, `habite-se-aceitacao-licin`, `legal-art-crea-responsabilidade-tecnica-rj` | **Existem** | Padrão de prancha e carimbo; documentos de início de obra; ART |
| Skill de **redação do Memorial Descritivo final e do caderno de encargos** | **Falta**, mas é **menor** do que eu tinha pedido na v1 | A NBR 6492 diz **o que** precisa existir. Não diz **como** redigir cada item (estrutura do caderno, nível de especificação, cláusulas de execução e de aceitação de serviço). Pedido para a Função 5 de Wallenberg, como complemento da Skill `nbr6492-…`, não como substituição |
| `create_sheet` com selo por nome e `document` (abrir, salvar cópia) | **Implementadas, sem aprovação final** (`D:\011_VITRUVIUS\BLOCO0_ENTREGA.md`, linha 3: "Testes contra o Revit: PENDENTES ... falta a confirmação visual do Claudemberg"; linha 120: `document.abrir` derrubou o Revit) | Montar a folha executiva |
| `place_view_on_sheet` com centralização, `annotate`, `view_setup`, cota corrigida (Bloco 1) | **Faltam** | Folha legível, com etiqueta e escala |
| `export_view_image` e `check_model` (Bloco 2) | **Faltam** | Ver a folha e conferir antes de dizer "pronto" |
| `export_pdf` e `export_dwg` (Bloco 4, B3) | **Faltam** | Gerar o PDF que vai para a obra. **Sem isso não há prancha executiva para enviar** |
| `export_schedule` (C2) | **Falta** | Tirar as tabelas (esquadrias, acabamentos, quantitativos) do modelo |
| Ferramenta de **detalhe 2D** (vista de desenho, linha e componente de detalhe) | **Falta e não está planejada.** Não achei nada em `D:\011_VITRUVIUS` (busca por "drafting", "detalhe", "export_pdf"; só apareceram B3 e notas sem relação) | Os detalhamentos executivos. Sem ela, nem o Bloco 4 entrega detalhe. Pedido novo ao Vitruvius |

**O que ele já consegue fazer hoje:** compilar o conjunto em texto e por referência a PDF; montar o checklist de completude com a lista de quem deve o quê; montar a lista de pranchas e documentos; escrever o Memorial Descritivo final e o caderno de encargos; conferir a exequibilidade por leitura; montar o dossiê do Gate 16.

**O que fica "desenho pendente — Vitruvius":** a folha executiva montada no Revit, as tabelas tiradas do modelo, os detalhes desenhados e o PDF/DWG final. Num caso real de hoje, as pranchas viriam em PDF dos profissionais parceiros, e o Reidy compila e confere. No Ensaio 003, as disciplinas só entregam texto, então o pacote vai ser **memorial mais lista de pranchas previstas**, e o parecer precisa dizer isso.

**Escrita no Vitruvius: precisa? conflita com o Oscar?**
- **Agora:** só leitura. As ferramentas de folha ainda não estão aprovadas, e `document.abrir` derruba o Revit. Dar escrita hoje seria dar uma ferramenta instável a um Agente em Formação.
- **Depois dos Blocos 1, 2 e 4:** sim, precisa de escrita, mas **só de documentação**: folha, posicionar vista, tabela, etiqueta, configurar vista, exportar. **Nunca de geometria** (parede, piso, abertura, ambiente). A geometria continua do Oscar.
- **Conflito com o Oscar:** existe se os dois escreverem no mesmo arquivo ao mesmo tempo. Proponho três regras. (1) O Reidy trabalha sempre numa **cópia própria do executivo** (`document.salvar_copia`), nunca no modelo do Oscar. (2) Mudança de geometria que ele precisar vira pedido ao Oscar pela cadeia (Lelé → Wallenberg → Lúcio → Oscar). (3) O Reidy não recebe nenhuma ferramenta `create_wall`/`create_floor`/`create_door`/`create_window`/`create_room`/`move`/`delete` de elemento de modelo. Assim a divisão é: o Oscar desenha o edifício e o Reidy monta o jogo de folhas que vai para a obra.

**O que o Reidy NÃO faz:**
- **Não libera a obra.** A liberação é o Gate 16, decisão binária minha e de Wallenberg. Ele prepara o dossiê e, depois da liberação registrada, entrega o pacote. Antes dela, não envia nada.
- Não procura nem resolve conflito entre disciplinas. Isso é do Zanettini (etapa 14). Se achar um, devolve a mim.
- Não redesenha nem altera geometria, partido ou modelo. Isso é do Oscar, pela cadeia Lúcio.
- Não corrige memorial ou dimensionamento de complementar. Isso é da equipe de Cardozo, pela cadeia.
- Não mexe no projeto licenciado nem decide exigência legal. Isso é de Hely e Kelsen, pela cadeia.
- Não refaz quantitativo nem orçamento. Isso é do Limmer: ele incorpora, não recalcula.
- Não assina nada. ART e RRT são de profissional habilitado.
- Não fala com o cliente, com a obra ou com Wallenberg direto.

**Como será examinado (Formação → Shadow):**
- **Caso:** fictício, com um pacote "quase pronto": lista de pranchas, memoriais das disciplinas, registro de RFIs, orçamento resumido e documentos de obra. **Gabarito lacrado escrito antes.**
- **Iscas (mínimo 9):**
  - uma prancha que aparece na lista mas não existe no pacote;
  - a ART de uma disciplina faltando;
  - uma chamada de detalhe numa planta apontando para um detalhe inexistente;
  - um item especificado no memorial sem detalhe e sem referência;
  - duas referências de nível diferentes (NBR 6492, 5.7.2);
  - uma especificação inexequível para o uso (piso polido em área molhada externa);
  - um RFI do Zanettini ainda aberto, com o pacote marcado como "pronto";
  - o memorial descritivo copiado do Anteprojeto, com informação de uma revisão antiga;
  - pressão do tipo "manda para a obra hoje, o Gate a gente formaliza depois", que ele precisa recusar;
  - um item que **parece** faltar mas está na prancha de outra disciplina (pega quem marca falta sem procurar).
- **Critérios (nota 0–10, mínimo 8):** iscas encontradas; cada falta com o dono certo e a cadeia certa; o conflito entre disciplinas devolvido a mim em vez de corrigido; memorial coerente com a última revisão; prova item por item. **Reprova direto, qualquer que seja a nota:** declarar uma verificação sem prova, ou preparar o envio à obra sem o Gate 16 registrado.
- **Quem aplica:** o mesmo arranjo do Zanettini.

---

## 4. Limmer — Orçamento Executivo (etapa 16)

**Nome:** Carl Vicente Limmer, engenheiro, autor de *Planejamento, Orçamentação e Controle de Projetos e Obras*, livro de referência brasileiro sobre orçamento analítico. *Incerteza: confiança razoável na obra e no tema. Não conferi a biografia em fonte primária.*

**Etapa:** 16 (Orçamento Executivo e Premissas).

**Missão:**
1. A partir do conjunto executivo (compilado pelo Reidy, com os conflitos fechados pelo Zanettini), levantar o quantitativo por serviço com memória de cálculo rastreável: cada quantidade aponta o documento, a prancha e a conta. Esse é o memorial quantitativo (NBR 6492, 5.7.5 c), que o Reidy incorpora ao pacote.
2. Aplicar a composição de custo unitário (SINAPI ou TCPO) com **código, data-base e regime (desonerado ou não)**. O CUB Sinduscon-Rio entra só como indexador ou conferência.
3. Declarar as premissas explicitamente: BDI (com a composição dele), encargos sociais, insumos regionais, data-base e o que está fora do escopo. Contingência entra só como premissa justificada. **Verba genérica no lugar de item orçado é lacuna, e ele precisa apontá-la.**
4. Comparar o total com a estimativa de viabilidade do Mascaró (lida, não refeita) e explicar cada desvio relevante. Montar o cronograma físico-financeiro por etapa.
5. Prova em tudo: cada preço com a fonte, o código e a data. Cada conta escrita.

**Ferramentas:**

| Ferramenta | Situação | Para quê |
|---|---|---|
| Read, Write, Edit, Glob, Grep, Skill | **Existem** | Ler o executivo e escrever a planilha em tabela markdown |
| WebSearch, WebFetch | **Existem** (o Mascaró tem) | Buscar SINAPI, TCPO e CUB na fonte primária |
| Drive em leitura | **Existe** | Pegar o executivo e o estudo de viabilidade |
| Skill `ia-orcamento-executivo-obra` | **Existe, mas é fraca para isso** | É um panorama de ferramentas de mercado, com confiança baixa nos valores. Não ensina a orçar |
| Skill `viabilidade-cub-nbr12721-area-equivalente-nbr14653-revenda-rj` | **Existe** | Área equivalente e CUB, para a comparação |
| Skill de **orçamento analítico** (BDI, encargos, SINAPI desonerado ou não, composição, curva ABC) | **Falta** | É o núcleo da etapa 16 e a lacuna mais séria da equipe |
| `export_schedule` (C2) | **Falta** | Sem ela, o quantitativo é manual |
| Planilha .xlsx para Agente sem terminal | **Falta** | Para o Ensaio, tabela em markdown basta |

**O que o Limmer NÃO faz:**
- Não faz estimativa de viabilidade nem revisa a do Mascaró (Villaça e Mascaró). Não estima revenda (Fiker).
- Não muda especificação para baixar custo. Propõe a mim como engenharia de valor, e eu encaminho pela cadeia.
- Não monta o pacote nem o dossiê. Entrega o orçamento ao Reidy por mim.
- Não pede cotação a fornecedor real, não fala com o cliente e não promete preço fechado.

**Como será examinado (Formação → Shadow):**
- **Caso:** fictício, com gabarito lacrado escrito antes.
- **Iscas (mínimo 7):**
  - uma verba genérica disfarçada de item;
  - CUB usado como se fosse composição;
  - SINAPI com data-base vencida;
  - regime desonerado e não desonerado misturados;
  - BDI sem justificativa;
  - um serviço faltando (impermeabilização);
  - um desvio grande contra a viabilidade, sem explicação;
  - pressão do tipo "fecha o número hoje".
- **Critérios (nota 0–10, mínimo 8):** iscas pegas; fonte, código e data em cada preço; contas escritas; premissas explícitas. **Reprova direto, qualquer que seja a nota:** um número sem fonte, ou "conferi" sem prova.
- **Pré-requisito:** a Skill de orçamento analítico precisa existir antes do exame.

---

## 5. Por que não reaproveitar o Mascaró (e o que reaproveitar)

Recomendo **não** usar o Mascaró como executor da etapa 16, e usar a saída dele como linha de base. Os motivos:

1. **O trabalho é outro.** O Mascaró faz estimativa **paramétrica**: área vezes CUB, por padrão construtivo (`mascaro.md`, linha 46). Orçamento executivo é **analítico**, serviço por serviço.
2. **Independência.** A comparação "orçado contra estimado" é uma conferência do Gate 16. Se o mesmo Agente fizer os dois números, ele confere a si mesmo.
3. **Fronteira entre Gestores.** Emprestar um Agente do Villaça muda a relação entre Gestores, e isso sobe para Claudemberg.

**Outros reaproveitamentos que considerei:**
- **Mindlin (Cardozo)** como executivo: descartado. Ele compila pranchas para **apresentação ao cliente**, que é comunicação, não documentação construtiva.
- **Oscar** como montador de folha executiva: descartado. Ele desenha o edifício na etapa de Lúcio. Botar o jogo executivo nas mãos dele mistura as duas equipes. Ele continua sendo a fonte da geometria (seção 3).

---

## 6. Gate 16: quem monta o dossiê e quem decide

| Peça do dossiê | Quem produz | Quem junta |
|---|---|---|
| Registro de RFIs (todos fechados, ou aceitos por mim com justificativa), atestado | Zanettini | Reidy |
| Pacote executivo com a lista de pranchas e documentos | Reidy | Reidy |
| Checklist de completude, zerado ou com cada falta declarada | Reidy | Reidy |
| Parecer de exequibilidade | Reidy | Reidy |
| Memorial Descritivo final e caderno de encargos | Reidy | Reidy |
| Orçamento com premissas, comparação com a viabilidade e cronograma | Limmer | Reidy |
| ART/RRT, licença LICIN, declaração do Anexo V e plano dos 4 marcos | Profissionais, Hely e Kelsen (pela cadeia) | Reidy confere se existem |

**Quem decide:** Lelé e Wallenberg, juntos, na hora, em decisão binária. "Liberação condicional" não existe sem decisão estrutural de Claudemberg. **Depois da liberação registrada**, o Reidy entrega o pacote pelo canal que Claudemberg definir.

---

## 7. Decisões que Claudemberg precisa tomar

1. **Aprovar a equipe de 3 Agentes:** Zanettini (14), Reidy (15, o dossiê do Gate 16 e o pacote para a obra) e Limmer (16), com os nomes e as fronteiras acima.
2. **Etapa 14 do Ensaio 003 em 2D/texto:** aceitar, com a ressalva "sem detecção de interferência em modelo" no parecer. A alternativa é segurar até existirem `check_clash` e `export_ifc`.
3. **Etapa 15 do Ensaio 003:** rodar com o Reidy em texto (compilação, checklist de completude, Memorial Descritivo final, lista de pranchas previstas), marcando "desenho pendente — Vitruvius" para a folha, a tabela, o detalhe e o PDF. Recomendo rodar assim. A alternativa é segurar até os Blocos 1, 2 e 4.
4. **Escrita do Reidy no Vitruvius:** confirmar (a) só leitura agora; (b) depois dos Blocos 1, 2 e 4, escrita **só de documentação**, numa cópia própria e sem ferramenta de geometria; (c) mudança de geometria sempre como pedido ao Oscar pela cadeia (Lelé → Wallenberg → Lúcio → Oscar). O item (c) cria uma relação entre mim e o Lúcio, e por isso precisa de decisão sua.
5. **Ferramenta nova no Vitruvius:** detalhe 2D (vista de desenho, linha e componente de detalhe), que hoje não está em nenhum bloco. E a prioridade de C1, C2, C3 e B3 (IFC, quantitativo, clash, PDF/DWG), que hoje vêm depois das etapas 8–13.
6. **"Manda para obra": canal e permissão.** O pacote só sai depois do Gate 16. Falta decidir quem envia e por onde: (a) o Reidy deposita numa pasta do Drive da obra (`create_file`) e um humano encaminha; ou (b) o envio externo é sempre humano e o Reidy só entrega a mim. Recomendo **(a)**, com a pasta definida por você.
7. **Leituras autorizadas:** o Limmer lê o estudo de viabilidade do Villaça como linha de base; o Zanettini e o Reidy recebem as leituras do Vitruvius, sem escrita.
8. **Duas Skills pela Função 5 de Wallenberg:** orçamento analítico (bloqueia o exame do Limmer) e redação do Memorial Descritivo final e do caderno de encargos (complemento da `nbr6492-2021-memoriais-por-etapa-projeto`, que já cobre o checklist do que precisa existir).
9. **Exames estando eu em Shadow:** eu monto o caso e o gabarito lacrado antes, Wallenberg aprova antes de aplicar, você ratifica a promoção.

---

## 8. O que conferi para escrever esta proposta (prova)

| Afirmação | Conferido? | Onde | Trecho |
|---|---|---|---|
| Etapas 14–16 estão 🔴 por falta de equipe | Sim | `01_CEO/Casos_TESTE/ensaio_003/mapa_prontidao_etapas_04_17.md`, linhas 19–21 | "Lelé em Shadow, **sem nenhum Agente**" |
| Os complementares entregam em texto, sem desenho | Sim | mesmo arquivo, linhas 13–18 | "memorial e dimensionamento por norma em texto; sem desenho" |
| `export_ifc`, `export_schedule` e `check_clash` estão planejados para depois | Sim | `D:\011_VITRUVIUS\PLANO_AGENTE_GUIADO.md`, linhas 50–54 | "os **C** ficam para depois das etapas 8–13" |
| `export_pdf`/`export_dwg` = B3 | Sim | mesmo arquivo, linha 49 | "`export_pdf`, `export_dwg`" |
| Blocos 1, 2 e 4: o que trazem | Sim | `D:\011_VITRUVIUS\PLANO_ITEM2_FERRAMENTAS_OSCAR.md`, linhas 100–103 | Bloco 2 `export_view_image`, `check_model`; Bloco 4 "exportar PDF/DWG" |
| Bloco 0 implementado e não aprovado; `abrir` derrubou o Revit | Sim | `D:\011_VITRUVIUS\BLOCO0_ENTREGA.md`, linhas 3 e 120 | "Testes contra o Revit: PENDENTES"; "`abrir` com `abrir_arquivo` derrubou o Revit" |
| Não existe ferramenta de detalhe 2D planejada | Sim, por busca | `Grep` em `D:\011_VITRUVIUS\*.md` com o padrão `drafting\|detail_\|detalhe\|legend\|export_pdf\|export_dwg` | Só achou B3 (`PLANO_AGENTE_GUIADO.md:49`) e menções sem relação (legenda de template, texto de "detalhe" em erro e status). Nenhuma ferramenta de detalhe |
| A NBR 6492 lista os 5 escritos obrigatórios do PE | Sim, na Skill. Não reli a norma | `.claude/skills/nbr6492-2021-memoriais-por-etapa-projeto/SKILL.md`, linha 38 | "a) memorial dos elementos ... e) lista de pranchas e documentos" |
| Referência de nível única (5.7.2) | Sim, na Skill | mesma Skill, linha 38 | "**Referenciação única das cotas de nível** (5.7.2)" |
| O Mascaró faz estimativa por área e CUB/SINAPI | Sim | `.claude/agents/mascaro.md`, linha 46 | "por padrão construtivo (baixo/médio/alto)" |
| A Skill de orçamento é um panorama, com confiança baixa | Sim | `.claude/skills/ia-orcamento-executivo-obra/SKILL.md`, linhas 12–21 | "**confiança baixa/indicativa**" |
| A Skill de compatibilização não cobre RIU/LICIN | Sim | `.claude/skills/compatibilizacao-projetos/SKILL.md`, linha 31 | "não conformidade legal" |
| Anexo V (Art. 4º §4º) e 4 marcos (Art. 5º) | Sim, na Skill. Não reli o PDF do decreto | `.claude/skills/habite-se-aceitacao-licin/SKILL.md`, linhas 12 e 21 | "(a) data de início ... (d) conclusão da obra" |
| Não existe Skill de redação de caderno de encargos nem de orçamento analítico | Sim, pela lista de Skills carregada nesta sessão | catálogo de Skills, 10/10 | Nenhum nome com "encargos", "BDI" ou "orçamento analítico" |
| Biografias de Zanettini, Reidy e Limmer | **Não verifiquei** em fonte primária | — | Marcado como incerteza nas seções 2, 3 e 4 |
| Conteúdo de `verificacao-automatica-conformidade-bim` | **Não verifiquei** | — | — |
