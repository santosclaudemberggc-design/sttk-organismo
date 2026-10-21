---
name: oscar-revit-projetista-vitruvius
description: Procedimento passo a passo para o Oscar modelar, documentar, montar folhas e conferir um projeto de arquitetura no Revit pelas ferramentas Vitruvius (mcp__vitruvius__*), com as regras de Claudemberg de 14/10/2026 (níveis antes das paredes, ponto 0, parede pelo macete do nível acima com base −espessura do piso, vistas do template primeiro, corte pelo meio do edifício, limpeza visual, salvar como uma vez e depois só salvar), conferência pela imagem (export_view_image + Read) antes de qualquer "atende", tabela de defeitos conhecidos das ferramentas com contorno seguro, e a representação NBR 6492 exigida no EP e no AP. Use SEMPRE que o Oscar (ou qualquer Agente) for abrir, salvar, modelar paredes, pisos, aberturas, ambientes, criar ou ajustar níveis, elevações, cortes, plantas, cotas, etiquetas, folhas, carimbo, exportar imagem de vista, ou conferir um desenho no Revit — mesmo que o pedido só diga "desenhar", "modelar", "montar a prancha", "fazer o EP no Revit", "cotar", "elevação" ou "Vitruvius".
version: v1.3.0
status: ativa
dona: Lúcio (Gestor Arquitetura)
usuario: Oscar (Coordenador de Projeto Arquitetônico)
data: 2026-10-15
fontes: "D:\\011_VITRUVIUS\\PEDIDOS_OSCAR\\06_regras_claudemberg_niveis_vistas_carimbo_14-10.md (R1-R4); 07_feedback_claudemberg_teste_bloco1_14-10.md (F1-F8, R5, R6 — prevalece); 05_analise_prints_EP_v2_14-10.md; 08_resultado_teste_bloco1_14-10.md (D1-D12); D:\\011_VITRUVIUS\\BLOCO1_ENTREGA.md (contratos, build 2026-10-14-bloco1-v7); STATUS_PROJETO.md; parecer_bardi_v2.md da Etapa 05 do Ensaio 003; Skills nbr6492-2021-memoriais-por-etapa-projeto v1.1 e nbr6492-representacao-grafica."
changelog:
  - "v1.3.0 (15/10/2026, Lúcio, relatório conjunto Lúcio + Oscar sobre o diagnóstico Bardi, `Gestores/Lúcio (Arquitetura)/relatorio_oscar_vitruvius_15-10/02_relatorio_conjunto.md`, PARTE A): §6 e §11 com linha 'Atende' amarrada ao PNG (A1); §9 EP desenha 5.4.2 a–d mesmo em esquema (A8); §3 e §10 com prova de porta por pavimento, eixos e escada-lacuna (A9); §2 e §10 com tolerância de área do lote e justificativa de partido (A10); §10 acessibilidade só com Skill nbr9050 lida inteira (A11); §5 texto do template é limpeza do Oscar (C2); §8-bis: recursos que as descrições atuais das tools prometem (salvar, ajustarExistente, base_deslocamento) ficam 'não testado' até reconferência em cópia. Regras de leitura, citação, diferença entre versões e estado (A2–A7, A13) foram para .claude/agents/oscar.md."
  - "v1.2.2 (14/10/2026, Wallenberg): D16–D21 a partir de P1–P11."
  - "v1.2.1 (14/10/2026, Wallenberg): tabela de defeitos D13–D15 (listagem de folhas, ID de vista × nível, macete sem tipoPiso); build atual v8; nenhuma regra alterada."
  - "v1.2 (14/10/2026, Wallenberg, padrão v1): formato only, regras intactas. Gate de entrada explícito; formato de entrega fixo (seção 11); checklist final exige prova colada; evals em evals/evals.json (3 casos)."
  - "v1.1 (14/10/2026, Lúcio, após teste de leitura do Oscar, nota 9,50): §0.5 e D/F6 dizem que não há ação salvar; §1.3 e §2 citam o teste de 14/10 como prova; §3.10 cotas verticais (mode=nivel) e cota de nível."
  - "v1.0 (14/10/2026, Lúcio): criação por ordem de Claudemberg via Wallenberg ('configure bem as habilidades do Oscar para usar o Revit e ser um bom projetista; espero não repetir os erros')."
---

# Oscar no Revit — procedimento de projetista (Vitruvius)

**Regra mãe:** cada passo termina com uma **conferência** (releitura pela ferramenta ou imagem aberta com `Read`). Passo sem conferência = passo não feito. As regras de Claudemberg (R1–R6, F1–F8) **prevalecem** sobre qualquer contrato de ferramenta ou hábito anterior.

**Gate de entrada:** nenhuma escrita no modelo antes do passo 0.1 (`get_revit_status`) passar. Falhou → pare e reporte (ver §11).

**Três palavras proibidas sem prova:** "atende", "conferido", "pronto". Só se escrevem com a saída da ferramenta colada **e**, para qualquer coisa visual, o PNG aberto com `Read` nesta execução. A ferramenta responder `success:true` ou "conferida" **não é prova** (D2, D3, D5 mostraram sucesso falso).

---

## 0. Preparação (antes de tocar no modelo)

| # | Faça | Confira |
|---|---|---|
| 0.1 | `get_revit_status` | Plugin conectado. Se "Plugin não está conectado" ou "No such tool": **pare**, cole o erro, reporte a Lúcio. Não simule desenho. |
| 0.2 | Ler o build no log `%APPDATA%\VITRUVIUS\logs\revit-plugin-AAAA-MM-DD.log` ("BUILD VERSION") quando tiver como ler; senão declare "build não verificado" | Build anotado na entrega |
| 0.3 | `document` → `listar_abertos` / `get_document_info` | Qual documento está ativo e o caminho. **Se for arquivo de cliente aberto por Claudemberg, não altere nada** — só leitura, e pergunte a Lúcio. |
| 0.4 | **Salvar como UMA vez** (`document.salvar_copia`) no caminho do caso que Lúcio deu (ex.: `...\Casos_TESTE\...\entrega\vN\NOME.rvt`) | `get_document_info` mostra o novo caminho como ativo |
| 0.5 | Daí em diante, **só salvar** no mesmo arquivo (R6). Nada de `_v2`, `_v3` por conta própria. Nova cópia só se Lúcio pedir por escrito. **Hoje (build v8) a ferramenta `document` não tem ação "salvar"** (só abrir, fechar, listar_abertos, salvar_copia, salvar_como_template, info): até existir, **não grave cópia nova**; ao fim, declare "alterações não salvas no arquivo X, pedir a Claudemberg Ctrl+S" e reporte a Lúcio | Ao fim: um único `.rvt` por entrega; `isModified` declarado |
| 0.6 | **Caminhos proibidos:** qualquer coisa dentro de `D:\007_MATERIAIS` (inclusive templates `.rte`) e qualquer `.rte`. A ferramenta **não bloqueia** hoje (D1/F8): o bloqueio é você | Caminho conferido letra a letra antes de chamar |

## 1. Níveis antes das paredes (R1)

1. `get_levels` e cole a lista (id, nome, elevação).
2. Ajuste às alturas do caso:
   - **Terreno = rua = 0,00.**
   - **Térreo = 0,30 a 0,50** acima da rua (o template ARQ.Sttk traz 0,30; use o valor do caso).
   - **Pavimento seguinte = nível de baixo + pé-direito + espessura da laje** (ex.: 0,30 + 2,80 + 0,15 = 3,25). Cobertura idem.
   - **[19/10/2026, decidido por Claudemberg] Padrão Sttk: piso a piso de 3,15 m em todos os pavimentos** (pé-direito de referência mínimo 3,00 m). Níveis: térreo 0,30 → superior 3,45 → cobertura 6,60. Outro valor só com decisão escrita do cliente ou de Claudemberg.
3. Ajuste com `set_parameter` "Elevação" no id do nível (o Vitruvius ainda não tem ação própria). Usado assim no teste de 14/10 (08_resultado, R1: 694 → 3,25 e 323714 → 6,20, relidos); se o nome do parâmetro falhar, liste os parâmetros do nível com `get_element` e cole.
4. **Releia** com `get_levels` e cole a conta de cada nível. Só siga se todos baterem.
5. Pé-direito e laje **iguais** aos do texto da entrega (Bardi v2: texto 6,40 × cotas 6,55/6,70 — não repetir). Divergência de pé-direito entre pavimentos só com justificativa escrita.

## 2. Ponto 0 (R2)

- `list_elements` na categoria do ponto base do projeto (OST_ProjectBasePoint) e do ponto de levantamento (OST_SharedBasePoint); cole as coordenadas (a posição sai pela bbox; `location` vem nula). Funcionou no teste de 14/10 (ids 111429 e 111426, ambos em 0,0,0).
- O canto de referência do lote (ou o eixo combinado com Lúcio) fica em **(0,0)**. Todas as coordenadas que você passar às ferramentas partem daí.
- Lote: dimensões e área **iguais ao dossiê** (Bardi v2: 571,60 desenhado × 571,80 do dossiê — não repetir). Se o polígono não fecha a área, pergunte; não arredonde lado. **Prova (A10):** cole a conta da área pelos vértices (em metros, convertida se vier em pés — D20); diferença máxima de 0,01 m² contra o dossiê.

## 3. Ordem de modelagem

Siga nesta ordem; cada item com releitura (`get_walls`, `get_floors`, `get_doors`, `get_windows`, `get_rooms`, `list_elements`) e ids colados.

1. **Eixos** (`create_grid`) — sempre; a ferramenta existe (Bardi v2: "eixos não criados" descontou).
2. **Paredes externas** — pelo macete de Claudemberg (R5, abaixo).
3. **Lajes/pisos** (`create_floor`) — ler a espessura do tipo (`get_floor_types`).
4. **Paredes internas** — base no nível do pavimento, **sem** deslocamento; topo no nível acima (decidido por Claudemberg, 19/10/2026).
5. **Aberturas** (`create_door`, `create_window`) — **todo pavimento tem porta**; todo ambiente de permanência tem janela; porta de entrada com lógica de acesso pelo afastamento frontal.
6. **Escada e vão de laje — `criar_escada` (19/10/2026, decidido por Claudemberg em sabatina):** sempre de um nível para o imediatamente acima. Você define `espelho`, `piso` e `largura` (mínimo 0,90 m; o tipo "ESCADA PROJETO" exige 1,00 m); o Revit calcula os degraus. Formato reta, `l` ou `u` (no L/U: `espelhosPrimeiroLance` e `virar`). A ferramenta abre o vão na laje de cima, põe guarda-corpo no vão e mantém o corrimão do tipo nos lados sem parede. Antes: meça o ambiente com `list_elements` (paredes com `location`) e confira se a escada cabe sem atravessar parede **do pavimento de cima** (a ferramenta só confere as paredes entre os dois níveis). Depois: imagem da planta dos dois pavimentos e de um corte que passe pela escada. Tipo de escada sempre o padrão; escada personalizada é do Tenreiro. Exemplo testado: `EP_diagnostico_19-10.rvt`, escada 450118 em U, 18 espelhos, 9+9.
7. **Cobertura** (`create_roof`) — hoje só plana; inclinada = lacuna declarada.
   **Prova de acesso (A9):** cole `get_doors` filtrado por nível mostrando ao menos 1 porta em cada pavimento, `list_elements` dos eixos (ao menos 1 em cada direção) e a escada (`list_elements` category "Escadas") ligando os pavimentos. Faltou um dos três = passo não feito.
8. **Ambientes** (`create_room`) — nome e número separados (o "8" do "SALA 8" era o Número; conferir com `get_parameter Nome`).
9. **Etiquetas** (`annotate acao=ambientes|portas|janelas`).
10. **Cotas** (`dimension`) — por último na modelagem, já nas vistas de apresentação (a limpeza da §5 vem depois delas). Plantas: `parede_total`/`cadeia`. Cortes e elevações: `mode=nivel` (pé-direito, piso a piso) — **sem a conferência nova**, então confira o valor pela conta dos níveis e pela imagem. Cota de nível de piso/laje: `create_spot_elevation`.

### Paredes — macete de Claudemberg (R5)

- **Base** = nível do pavimento, **deslocamento da base = −(espessura do piso)** (ex.: −0,15) — o piso fica escondido na parede. **[19/10/2026, decidido por Claudemberg] Só nas paredes externas do térreo.** Paredes internas e todas as do superior: base no nível, deslocamento 0, topo no nível acima.
- **Topo** = **nível acima** (restrição superior), deslocamento 0.
- No `create_wall`: `topo {levelId: <nível acima>, deslocamento: 0}`; o deslocamento da base hoje se grava com `set_parameter` "Deslocamento da base" = −espessura (o `base_offset` direto é pedido em aberto, F4). **Nunca** `height` solto para parede de pavimento.
- **Releitura obrigatória:** altura esperada = (nível acima − nível do pavimento) + espessura do piso. Ex.: térreo 0,30, superior 3,25, piso 0,15 → 3,10. **Padrão de 19/10/2026 (0,30 / 3,45 / 6,60, laje 0,15):** externa do térreo = 3,30; interna do térreo = 3,15; todas do superior = 3,15.
- **Se a parede saiu com 0,30 m** (ou qualquer altura absurda), verifique, nesta ordem: (a) restrição superior caiu no nível errado (ex.: topo no "Páv. térreo" em vez do Superior); (b) a elevação dos níveis não foi ajustada (R1); (c) deslocamentos; (d) tipo de parede. Corrija com `set_parameter`, releia, cole. **Não recrie** sem antes listar se a parede já existe (risco de parede sobre parede).
- Sem piso no nível, o macete falha (D15): informe `tipoPiso` explicitamente. Não crie a parede com `height` solto para contornar.
- Filtro de paredes: por nível ou por tipo, não por nome (paredes herdam o nome do tipo; o `name` vai para Comentários).

## 4. Vistas — do template primeiro (R3, F1, F2)

1. **Liste as vistas existentes** (`list_elements` de vistas / navegador) e cole: elevações NORTE/SUL/LESTE/OESTE (marcador Sttk), plantas "EP. Terreno/Térreo/Superior", "EP. Perspectiva", cortes.
2. **Proibido criar elevação que o template já tem** (F1). Ajuste a existente: `view_setup recorte.ajustar=edificio`, plano distante cobrindo a casa, escala, detalhe.
   - **[19/10/2026, decidido por Claudemberg] Elevação tem duas partes e as duas se movem:** (1) o **marcador** da elevação e (2) a **vista da elevação**, a linha tracejada com os limites que aparece ao selecionar o marcador (plano e extensão da vista, igual à de um corte). Mover só o marcador deixa a vista cortando a casa (diagnóstico 19/10, item 6: imagem da SUL saiu como corte). Ordem: mover o marcador para fora da face, depois mover a vista para fora da face, depois exportar a imagem e conferir que é fachada.
   - **[19/10/2026, decidido por Claudemberg] `create_elevation` autorizado** quando o ajuste da elevação do template não conseguir mover marcador e vista. Registre o uso na entrega.
   - **[19/10/2026, decidido por Claudemberg] Elevação nova substitui a antiga:** criou elevação nova com a mesma função de uma existente, **apague a existente** (`delete_element` na vista) e depois apague o marcador que ficou vazio. Confira antes, com `list_elements` (category "Vistas", className "ViewSection"), que o marcador não guarda outra vista (ex.: LESTE/OESTE). Nada de duas vistas com a mesma função.
   - **[19/10/2026, decidido por Claudemberg] Marcador de fachada fica fora do lote**, depois do muro, nunca no quintal na frente da fachada. Como fazer: `create_elevation` com `alvo: "modelo"` (o alvo inclui os muros, então o marcador vai para fora deles), e confira a posição devolvida contra o contorno do lote.
   - **[19/10/2026, decidido por Claudemberg] Cada fachada tem duas vistas:** `… - COM MURO` (`alvo: "modelo"`) e `… - SEM MURO` (mesma `position` da com muro, `alvo: "edificio"`, `permitirMuroNaFrente: true`, e depois `view_setup ocultarIds` com os ids dos muros). Exemplo testado em 19/10 no `EP_diagnostico_19-10.rvt`: SUL e NORTE, marcadores em y −1,59 e 41,59, lote de y −0,05 a 40,05.
3. **Exporte a imagem e abra** (seção 6). Confira se a vista mostra a face certa: a elevação SUL tem de mostrar a fachada sul (onde está a porta/janela do sul). **Se a elevação do template mostra a face errada ou o muro tapa a casa:** não há ferramenta para mover o marcador (D12). Faça: (a) registre com o PNG; (b) **não** crie elevação nova por conta própria; (c) pergunte a Lúcio — só com autorização escrita dele use `create_elevation fachada=<lado>` e, nesse caso, oculte/registre a do template para não haver duplicata; (d) confira a nova também pela imagem (D3: o marcador da nova pode cair atrás do muro).
- **[19/10/2026, decidido por Claudemberg] Família que o cliente ainda não escolheu** (portão, porta, janela, louça): na Arquitetura use uma família **padrão** que já exista no template ou no acervo. Não deixe o vão fechado nem espere a família definitiva. A família do jeito que o cliente quer é do **Tenreiro** (Interiores), que cria a partir de referência, caderno técnico e material.
4. **Corte (F2):** passa **pelo meio do edifício**, atravessando ambientes, aberturas e a laje (e a escada, se houver). Defina p1/p2 você mesmo a partir das coordenadas da casa; não confie no `auto_position` (D10). Escala **do EP = 1:100**. Detalhe médio (hachura). Confira pela imagem: tem de ler como corte (parede interna cortada, laje, pé-direito).
5. Parâmetros do navegador: "Etapa do Projeto" e **"Sub Etapa Projeto"** (não "Sub Etapa", D8) — grave com `set_parameter` se a ferramenta falhar. Nenhuma vista em "???".

## 5. Limpeza visual (F3)

- Plantas de apresentação: `view_setup ocultarMarcadores` e recorte ajustado; **nenhum marcador duplicado ou solto**, nenhuma linha de corte atravessando sem necessidade.
- **Sem texto solto dentro do desenho** (ex.: "TESTE ...", "NORTE" do template). Texto livre vai fora do desenho ou no carimbo. Texto que veio do template também é limpeza sua (C2, 15/10): remova ou oculte e cole o id; não o trate como defeito de ferramenta.
- **Cotas fora do desenho** e sem cair sobre etiqueta (D7: cota de ambiente cai sobre a etiqueta — prefira `parede_total`/`cadeia` externas; cota de ambiente só se a imagem mostrar legível).
- Rótulos de nível sem sobreposição (0,00 × 0,30). O `niveisCotovelo` falha (D5): registre como lacuna com o PNG.
- **Norte** em toda planta (`annotate acao=norte`); se o símbolo sair sem "N" legível, registre e acrescente texto "N" junto, fora do desenho. Norte de projeto ≠ norte verdadeiro: não afirme orientação real sem dado do caso.

## 6. Conferência pela imagem (obrigatória)

1. `export_view_image` da vista ou folha → caminho em `D:\011_VITRUVIUS\_imagens\...`.
2. **`Read` do PNG** nesta execução.
3. Escreva o que viu (ex.: "casa inteira visível, porta na fachada sul, níveis 0,00/0,30 sobrepostos").
4. "Atende" **só** depois disso. "Atende" sem imagem vista = **falso** (Bardi v2 descontou −1,50 do Oscar e −2,00 de Lúcio).
5. Sem a ferramenta ou com falha: escreva **"não verificado — sem imagem"**, nunca "atende".
6. **Formato da linha (A1, 15/10):** toda linha "Atende" traz, na mesma linha, o caminho do PNG aberto com `Read` nesta execução e uma frase do que se vê. Linha "Atende" sem caminho é tratada por Lúcio como falsa. Lúcio abre PNGs por amostragem.

## 7. Folhas e carimbo (F5, R4)

1. `create_sheet` com o selo **por nome** ("SI_FOLHA_ ABNT : A3" ou "a3"); confira o `seloId` (A3 = 449280 no teste de 17/10). Passe **sempre `requestId` novo** e **`areaUtil` explícita** (A3: xMin 0,025; xMax 0,410; yMin 0,010; yMax 0,287 m). Motivo: no build v40 a ferramenta não lê a moldura do selo e devolve "não consegui ler a moldura visível" (D16), mas cria a folha mesmo assim. Declare na entrega que a moldura é premissa, não leitura. Se o nome falhar, cole o erro e use o id.
   - **Folha de teste não se apaga pela ferramenta:** `delete_element` e `operar_elementos` respondem "ElementId cannot be deleted" (D22, pedido P22). Se criar folha por engano, apague pela interface do Revit e não salve.
2. Carimbo: a família não tem carimbo desenhado (R4). Grave os campos que existem (`carimbo` {cliente, obra, endereco, data, desenhado_por, ...}) e liste os `naoEncontrados`. **Não declare carimbo pronto** até a família nova (caminho a) existir.
3. Área útil: até o carimbo existir, folha inteira menos margens — use `reservaCarimbo=nenhum` (D11).
4. `place_view_on_sheet` → **exporte a imagem da FOLHA e abra**. A vista tem de estar **dentro da moldura e centralizada**. Hoje a ferramenta põe a vista fora da moldura A3 dizendo "conferidas" (D2/F5): se a imagem mostrar isso, escreva **"não atende — vista fora da moldura (D2)"** e reporte; não entregue a folha como pronta.
5. Uma escala por vista, legível; título junto da vista, sem cair sobre o desenho.

## 8. Defeitos conhecidos das ferramentas (build atual bloco1-correcao-v8; tabela feita em v7, reconferir) — contorno seguro

| # | Ferramenta | Defeito | Contorno até ser corrigido |
|---|---|---|---|
| D1/F8 | `document.salvar_copia` | Grava em `D:\007_MATERIAIS` sem recusar | Você bloqueia: confira o caminho antes; nunca fora da pasta do caso |
| F6 | `document` | Não há ação `salvar` (pedido em aberto) | Salvar como uma vez; depois **não** faça nova cópia; declare as alterações não salvas e peça a Lúcio (Claudemberg salva no Revit) |
| D4 | `document.abrir` | Responde sucesso e não abre (erro "Switching active documents..."); pode derrubar o plugin | Não dependa de abrir/trocar documento; confira com `listar_abertos`; se cair, pare e reporte |
| D2/F5 | `place_view_on_sheet` | Vista fora da moldura A3 com "conferidas" | Conferir pela imagem da folha; não entregar folha sem a imagem certa |
| D3 | `create_elevation` | Marcador atrás do muro, casa tapada, "criada e conferida" | Só com autorização (seção 4); conferir pela imagem |
| D12 | `view_setup ajustarExistente` | Não move marcador nem vista da elevação (`movido_m: 0` com `success:true`; ou "elevação ficou vazia", diagnóstico 19/10) | Usar `create_elevation` (autorizado por Claudemberg, 19/10/2026), com marcador e vista fora da face; conferir pela imagem. Testado em 19/10: SUL e NORTE saíram como fachada. O plano de elevação existente não se move pela API (E-27/E-29); desde a v58 o `ajustarExistente` recusa em vez de dar sucesso falso |
| D5 | `view_setup niveisCotovelo` | Erro `pLeader` com `success:true` | Registrar lacuna com PNG |
| D6 | `dimension parede_aberturas` | "largura não encontrada no tipo" (porta/janela do template) | Use `cadeia` com os elementos, ou `parede_total`; declare |
| D7 | `dimension ambiente` | Texto cai sobre a etiqueta | Prefira cotas externas; conferir pela imagem |
| D8 | vistas novas | Procuram "Sub Etapa"; o parâmetro é "Sub Etapa Projeto" | `set_parameter` manual, releitura |
| D9 | `place_view_on_sheet` | Mensagem cita escala errada | Leia o valor, não a frase |
| D10 | `create_section auto_position` | Corte pela borda, sem parede interna | Dê p1/p2 pelo meio da casa |
| D11 | `create_sheet` | Reserva 180 mm de carimbo inexistente | `reservaCarimbo=nenhum` |
| — | `create_room` | Resposta mostra "SALA 8" (nome+número) | Confira `Nome` com `get_parameter` |
| — | `get_parameter` | Alguns valores em pés | Converta (×0,3048) e declare |
| D13 | `list_elements` categoria "Vistas" + classe ViewSheet | Retorna 0 folhas, embora existam | Listar folhas com categoria "Folhas"; registrar a inconsistência com a saída colada |
| D14 | `export_view_image` | Aceita ID de nível como vista e falha ("311 não é vista nem folha") | Antes de exportar, confirmar o ID da vista por `list_elements` (ex.: planta LV. Térreo = 312, não o nível 311) |
| D15 | `create_wall` com `macete=true` | Falha "sem piso no nível e sem tipoPiso" quando o nível não tem piso | Passar `tipoPiso` explícito (tipo e espessura conferidos em `get_floor_types`) antes de criar; sem tipoPiso, não criar a parede |
| D16 | `create_sheet` com selo | Não lê a moldura do selo: responde "não consegui ler a moldura visível na folha. Informe areaUtil." | Informar `areaUtil` manualmente e declarar na entrega que a moldura é premissa, não leitura (margens da NBR 10068 só se o caso disser) |
| D17 | `place_view_on_sheet`, `export_view_image` | `Error: Connection closed` em sequência, com plugin conectado no status | Reconferir `get_revit_status`; repetir no máximo 2 vezes; se persistir, "não verificado — sem imagem" e reporte com o erro colado |
| D18 | `list_elements` de folhas | Lista uma folha que ninguém criou no run, e o "Número da folha" da vista não bate com o da folha criada | Antes de criar folha, listar folhas e vistas e anotar IDs; depois de criar, reler e declarar qual ID recebeu a vista |
| D19 | `set_parameter` em "Elevação" de nível | Responde sucesso e a releitura mostra outro valor | Só aceitar o valor depois da releitura (`get_levels`/`get_element`); se diferir, "não atende" e reporte |
| D20 | coordenadas, comprimentos e elevações de elementos | Vêm em pés, sem rótulo de unidade | Converter (×0,3048) antes de comparar com o EP, e declarar a conversão na entrega |
| D21 | escritas (`set_parameter`, `create_wall`) | `Timeout na resposta do Plugin` em série; uma parede pode ficar com base e topo no mesmo nível | Parar após o primeiro timeout; reler o elemento afetado; não repetir em lote; reportar o estado exato |
| — | cobertura inclinada, terreno/subregião | Não existem | Lacuna desenhada + declarada (seção 3). Escada e vão de laje: `criar_escada` desde 19/10/2026 |
| — | quadro de áreas (TO, CA, permeabilidade) | Desde 20/10/2026 (plugin v68): `criar_quadro_areas` | Template ARQ.Sttk - 2026 já traz os 3 esquemas e as 3 tabelas com fórmula (a API não cria esquema nem fórmula). Informe `areaLote` do Levantamento, `fatores` da Skill `quadro-de-areas-rj` e `manuais` para o que o modelo não tem desenhado (ex.: faixa de concregrama, esquema PERM). Índices pela menor área de lote (`baseIndices` padrão `menor`); a outra base volta em `naOutraBase`. Conferir as 4 plantas de área pela imagem (etiqueta em cada área). Os números só valem depois da auditoria do Hely (via Kelsen). |

### 8-bis. Recursos que a descrição promete e ninguém testou (15/10/2026)

As descrições atuais das tools anunciam: `document acao=salvar` (F6), `view_setup ajustarExistente` para mover marcador de elevação (D12), `create_wall base_deslocamento` (R5/F4), `create_sheet` com nome de selo sem diferenciar espaço/maiúscula (B7), `create_elevation` com `distancia`/`alvo` (B9), `dimension` com tipo de cota pela escala (B10), `create_section` com `nivelDetalhe`/`recorte_auto` e `etapa`/`sub_etapa` (B12, B14). **Descrição não é prova.** Até a reconferência em cópia (uma escrita por vez, com releitura e PNG), o contorno das linhas acima continua valendo; se usar um desses recursos, declare "[descrição, não testado]" e confira pela releitura e pela imagem.

**Quando uma ferramenta falhar:** cole o **erro exato** (texto da resposta e, se houver, a linha do log), o id do elemento e o que você fez em seguida. Nunca "deu erro" sem o texto. Nunca repita uma escrita que "travou" sem antes listar se o elemento já foi criado (risco de duplicar). Esta tabela vale até Wallenberg informar o build corrigido; build novo = reconferir cada linha antes de confiar.

## 9. Representação NBR 6492:2021 por etapa

Fonte: Skill `nbr6492-2021-memoriais-por-etapa-projeto` (Seção 5) e `nbr6492-representacao-grafica` (escalas, norte, cotas).

| Etapa | Peças gráficas obrigatórias | Representação mínima |
|---|---|---|
| **EP** (5.4.2) | a) implantação (norte, acessos, platôs/taludes, recuos e afastamentos, áreas cobertas, estacionamento, **permeáveis e impermeáveis**, cotas de nível); b) plantas dos pavimentos; c) cortes **com projeção da topografia natural**; d) elevações; e) detalhes se necessário | Escala 1:100 (implantação pode 1:200); norte em toda planta; cotas externas gerais; níveis de piso; corte AA e BB pelo edifício; escala junto do desenho |
| **AP** (5.5.2) | a) implantação geral **com eixos e ponto de referência**; b) **diretrizes de terraplenagem**; c) plantas dos pavimentos; d) **planta de coberturas** (escoamento, inclinação); e) cortes; f) elevações; g) detalhes principais | 1:100 ou 1:50; cotas completas (externas e internas), níveis, eixos cotados; cortes com cotas verticais (pé-direito, laje, peitoril); lista de pranchas; carimbo completo |

**EP sem programa fechado (A8, 15/10):** as peças a–d do 5.4.2 são desenhadas mesmo em esquema, com a lacuna escrita no título da vista (ex.: "IMPLANTAÇÃO — norte pendente"). Deixar uma de fora só com ordem escrita de Lúcio. Prova: id e PNG de cada uma das 4 vistas.

Tipos de linha, hachura de corte, cortes em letras maiúsculas (A-A, B-B) com seta de sentido; cota de nível com +0,00 = referência (o Terreno/rua do R1).

## 10. O que um bom projetista confere antes de entregar

- [ ] **Coerência planta × corte × elevação:** a porta/janela da planta aparece na elevação do lado certo e no corte que passa por ela.
- [ ] **Alturas batem com o texto:** níveis, pé-direito, laje e altura total iguais no modelo, nas cotas e no memorial.
- [ ] **Acesso a todos os pavimentos:** porta em cada pavimento; escada (`criar_escada`) ligando-os.
- [ ] **Aberturas em todos os ambientes de permanência** (sala, quartos, cozinha) — fachadas não cegas sem justificativa.
- [ ] **Lote igual ao dossiê** (lados e área, ±0,01 m², conta colada) e afastamentos iguais aos do Legal.
- [ ] **Partido justificado (A10):** uma frase por decisão (acesso social, aberturas por fachada, pé-direito diferente entre pavimentos).
- [ ] **Acessibilidade (A11):** porta, corredor e giro da suíte acessível cotados e vistos em PNG, com a Skill `arquitetura-nbr9050-acessibilidade` lida inteira (versão e linhas declaradas).
- [ ] Ambientes com nome e área; etiquetas visíveis.
- [ ] Nenhuma vista vazia, duplicada ou em "???"; nenhum texto solto; cotas fora do desenho.
- [ ] Toda folha vista em imagem, vistas dentro da moldura.
- [ ] Um único `.rvt` salvo no caminho do caso; nada em `D:\007_MATERIAIS`.
- [ ] Defeitos de ferramenta com erro colado; lacunas declaradas na parte (e) do checklist de entrega.

## 11. Formato de entrega (obrigatório)

Toda entrega do Oscar a Lúcio usa este bloco. Sem ele, a entrega não é válida.

```
## Entrega — <caso> — <etapa>
Build: <versão ou "não verificado">
Gate de entrada (0.1): <status colado do get_revit_status>
Passos: [1 ✓ prova] [2 ✗ motivo colado] ...
Imagens conferidas (§6): <caminho do PNG + o que foi visto>
Defeitos encontrados (§8): <código D + erro colado>
Lacunas declaradas (§3): <lista>
Pendências: <lista>
Status: PRONTO | PARCIAL | NÃO FEITO
```

Status **PRONTO** só se todos os itens do checklist abaixo tiverem prova colada.

## Relação com outras Skills

- `nbr6492-2021-memoriais-por-etapa-projeto` — **Complementa:** o que entregar por etapa; esta diz como produzir no Revit.
- `nbr6492-representacao-grafica` — **Complementa:** convenções gráficas.
- `levantamento-topografico-cadastral-orientado-duli-licin-rj` — **Complementa:** de onde vêm cotas do meio-fio, perfil natural e medidas do lote que entram no R1/R2.
- Checklist `Agentes/Oscar/checklist_entrega_oscar.md`, parte (f) — aponta para esta Skill.
