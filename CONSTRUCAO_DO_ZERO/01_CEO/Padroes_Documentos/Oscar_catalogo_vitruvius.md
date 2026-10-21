# Catálogo das ferramentas Vitruvius para o Oscar

**Fonte:** schemas reais das ferramentas `mcp__vitruvius__*`, carregados com ToolSearch em 17/10/2026. Build de referência: `2026-10-14-bloco1-correcao-v8`.
**Uso:** o Oscar consulta este catálogo antes de chamar qualquer ferramenta. Quando o schema real divergir daqui, vale o schema e este arquivo deve ser corrigido.
**Regras gerais (valem para todas):**
- **Unidades:** coordenadas, comprimentos, alturas e elevações em **metros**, salvo indicação. A ferramenta `get_parameter` pode devolver pés (×0,3048). Conferir a unidade do campo antes de comparar com o EP.
- **Escritas exigem `requestId`** (create_sheet em `criar`, document em `salvar_*`, manage_types em escritas). Repetir o mesmo `requestId` não grava de novo. Usar um id novo por ação.
- **Lote:** a maioria aceita `itens: [...]`. Cada item executa em ordem, e uma falha não interrompe os demais. Conferir o resultado de cada item.
- **Conferência:** toda escrita devolve releitura. Mesmo assim, a prova visual é `export_view_image` + Read. `success:true` não é prova (D2, D3, D19).
- **IDs:** nível, vista e folha têm IDs diferentes. Confirmar o tipo antes de usar (D14).
- **Ferramentas de listagem:** `list_elements` cobre qualquer categoria e substitui `get_walls`, `get_doors`, `get_windows`, `get_floors` e `get_rooms` (o próprio schema diz isso).

## 1. Estado e documento

| Ferramenta | Para que serve | Parâmetros principais | Conferência / cuidado |
|---|---|---|---|
| `get_revit_status` | Gate de entrada: plugin, documento, versão, estatísticas, build | — | Passo 0.1. Ler `buildVersion`, `documentPath`, `isModified`. Sem caminho certo, parar. |
| `get_document_info` | Metadados do documento aberto | — | Confirmar caminho. |
| `document` | Abrir, fechar, listar, salvar | **`acao`**: abrir, fechar, listar_abertos, salvar, salvar_copia, salvar_como_template, info. `caminho`, `caminhoDestino`, `requestId` (salvar_*), `confirmar_nova_copia`, `descartar_alteracoes`, `somente_leitura` | Regra R6: salvar_copia uma vez, depois só salvar. `abrir` com documento ativo é recusado (E-23). Não gravar em `D:\007_MATERIAIS`. Com cópia de teste, nunca salvar sem ordem. |
| `list_categories` | Categorias do modelo | — | Saída pode ser grande (excedeu limite em teste). |

## 2. Níveis, vistas e folhas

| Ferramenta | Para que serve | Parâmetros principais | Conferência / cuidado |
|---|---|---|---|
| `get_levels` | Lista níveis com id e elevação | `filter` opcional | Passo 1 (R1). Conferir elevação em metros. |
| `create_level` | Cria nível | `elevation` (m), `name`, `itens` | Preferir ajustar nível existente (R1). |
| `list_elements` | Lista qualquer categoria, com filtros | **`category`** (ex.: "Paredes", "Vistas", "Folhas"), `className` (ex.: "ViewPlan", "ViewSection", "ViewSheet"), `levelId`, `where` [{param, op, value}], `fields` (location, bbox, parameters), `limit`, `offset` | D13: para folhas usar `category:"Folhas"`; "Vistas" + ViewSheet voltou vazio. Usar `fields:["location"]` para coordenadas. |
| `find_elements` | Busca por categoria enumerada | **`category`** ∈ Walls, Doors, Windows, Floors, Rooms, Levels; `levelId`, `nameFilter` | Versão simples de `list_elements`. |
| `get_element` | Lê um elemento por id, com parâmetros | **`elementId`** | Usar para conferir Elevação de nível e tipo de elemento. |
| `get_parameter` | Lê um parâmetro | **`elementId`**, **`paramName`** | Pode vir em pés (D20). |
| `set_parameter` | Escreve um parâmetro | **`elementId`**, **`paramName`**, **`value`**, `itens` | D19: responde sucesso e pode não gravar. Sempre reler com `get_parameter` ou `get_element`. Comprimentos em metros. |
| `get_category_parameters` | Lista parâmetros de uma categoria | **`categoryName`** | Descobrir o nome exato do parâmetro (ex.: "Sub Etapa Projeto", D8). |
| `list_element_types` | Lista tipos de uma categoria | **`category`**, `includeParameters`, `limit` | Obter `typeId` para criar elementos. |
| `manage_types` | Lista, renomeia, duplica tipos; limpa não usados | **`acao`**: listar, renomear, duplicar, limpar_nao_usados; `categoria`, `filtro`, `typeIdBase`, `novoNome`, `espessura`, `largura`, `altura`, `requestId` | `limpar_nao_usados` tem confirmação em duas etapas (`listaConferida`). Não usar sem ordem. |
| `view_setup` | Ajusta vista: escala, detalhe, recorte, categorias, marcadores, etapa | **`viewId`**; `escala`, `nivelDetalhe`, `recorte` {ativo, visivel, ajustar, margem}, `ocultarCategorias`, `mostrarCategorias`, `etapa`, `sub_etapa`, `niveisCotovelo`, `ajustarExistente` {fachada, distancia, margem, alvo}, `conferirLimpeza` | Tudo ou nada: qualquer falha desfaz. `niveisCotovelo` falha (D5), e a falha desfaz o resto. |
| `export_view_image` | Exporta PNG de vista ou folha | **`viewId`** ou **`sheetId`** ou `viewIds`; `pixels` (padrão 2000); `pasta` (padrão `D:/011_VITRUVIUS/_imagens`) | Única prova visual. Abrir o caminho devolvido com Read. ID de nível dá erro (D14). Falha de conexão (D17): reconferir o status e repetir no máximo 2 vezes. |
| `create_sheet` | Lista selos e cria ou carimba folha | **`acao`**: listar_selos, criar, carimbo. Em `criar`: **`requestId`**, `selo` ou `seloId` (ex.: "SI_FOLHA_ ABNT : A3"), `numero`, `nome`, `reservaCarimbo` (nenhum, direita, inferior), `areaUtil` {xMin, xMax, yMin, yMax} (m), `carimbo` {campos} | D16: se não ler a moldura, devolve erro de areaUtil e a folha pode ser criada mesmo assim. Conferir `areaUtil` na resposta. Em `carimbo`: `sheetId`. |
| `place_view_on_sheet` | Coloca vistas numa folha dentro da área útil | **`sheetId`**, **`viewId`** ou `viewIds`, `escala` (número ou "ajustar"), `reorganizar` (padrão true), `areaUtil`, `reservaCarimbo`, `espacamento`, `point` (só com 1 vista e reorganizar=false) | Não cabendo, devolve erro com a escala que caberia, sem gravar. A resposta traz a caixa de cada vista. A palavra "conferidas" não é prova: exportar a folha. |
| `create_section` | Cria corte | `auto_position`, `startPoint`/`endPoint` {x,y}, `orientacao`, `escala` (100), `depth`, `top`, `bottom`, `front_depth`, `recorte_auto`, `nivelDetalhe`, `etapa`, `sub_etapa`, `alvo` | D10: `auto_position` cai na borda. Dar `startPoint`/`endPoint` pelo meio da casa. Corte vazio é desfeito. |
| `create_elevation` | Cria elevação de uma fachada | **`fachada`** ∈ norte, sul, leste, oeste; `position` {x,y}, `distancia` (1,5), `margem`, `escala`, `alvo` (edificio/modelo), `permitirMuroNaFrente` | R3: usar a elevação do template primeiro (`view_setup ajustarExistente`). Criar só com autorização. Conferir pela imagem (D3). |
| `create_spot_elevation` | Cota de nível sobre piso ou laje | **`elementId`**, `viewId`, `x`, `y` | Para cota de piso (Passo 10 do Oscar). |
| `create_group` | Agrupa elementos | **`elementIds`**, `name` | — |
| `dimension` | Cota | **`mode`** ∈ parede_total (`wallId`), parede_aberturas (`wallId`), ambiente (`roomId`, `eixo`), cadeia (`elementIds`, `eixo`, `referencia`), nivel (`elementIds`, `side`, `offset`); `viewId`, `afastamento`, `espacamento`, `lado`, `tipoCota`, `requestId` | Confere cada segmento: divergência acima de 2 mm desfaz e dá erro. Cota de ambiente pode cair sobre etiqueta (D7). Parede com abertura sem largura de tipo: D6, usar `cadeia`. |
| `annotate` | Etiquetas, textos e norte | **`acao`** ∈ ambientes, portas, janelas, texto, norte, listar_tipos; `ids`, `viewId`, `posicao` {x,y}, `texto`, `angulo`, `tipoEtiqueta`, `tipoTexto`, `simbolo`, `itens` | Texto com `posicao` em metros. Norte: `angulo` em graus. Conferir pela imagem. |
| `view_setup` | ver seção 1 |  |  |

## 3. Paredes, portas e janelas

| Ferramenta | Para que serve | Parâmetros principais | Conferência / cuidado |
|---|---|---|---|
| `create_wall` | Parede reta entre dois pontos | **`startPoint`** {x,y}, **`endPoint`** {x,y}, **`levelId`**, **`type`** (nome exato do tipo), `macete` (true = topo no nível acima e base −espessura do piso), `tipoPiso` (obrigatório se o nível não tem piso, D15), `height` (desconectada), `topo` {levelId, deslocamento}, `base_deslocamento`, `name` (vai a Comentários), `marca`, `itens` | R5: `macete=true` é o padrão Sttk. Sem piso no nível e sem `tipoPiso`: erro. Confere altura e restrição na releitura e desfaz se divergir. |
| `criar_elemento_linha` | Parede reta ou curva pelo caminho novo | **`categoria`** ∈ parede, parede_curva; **`inicio`** {x,y}, **`fim`** {x,y}, `meio` (só curva), **`levelId`**, **`tipo`** (nome do tipo), **`altura`** (m, a partir do nível base), `nome`, `itens` | Nome novo para o mesmo papel de `create_wall` com `height`. Confere comprimento e altura. Usar um ou outro, não os dois para a mesma parede. |
| `create_arc_wall` | Parede curva por 3 pontos | `startPoint`, `endPoint`, `midPoint`, `levelId`, `height`, `type`, `name` | Preferir `criar_elemento_linha` com `parede_curva`. |
| `create_rectangular_room` | 4 paredes e 1 ambiente retangular | **`levelId`**, **`name`**, **`width`**, **`depth`**, **`wallType`**, `origin` {x,y} | Atalho para sala. Conferir área no resultado. |
| `create_door` | Porta em parede existente | **`wallId`**, **`doorTypeId`**, **`offset`** (m do início da parede ao centro), `itens` | Porta na parede. Conferir pela imagem. |
| `create_window` | Janela em parede existente | **`wallId`**, **`windowTypeId`**, **`offset`**, `sillHeight` (peitoril, m), `itens` | Idem. |
| `criar_elemento_ponto` | Porta, janela ou família de ponto | **`categoria`** ∈ porta, janela, familia; para porta/janela: `hostWallId`, `offset`, `typeId` ou `tipo`, `peitoril`, `inverterLado`, `inverterAbertura`; para familia: **`ponto`** {x,y}, `rotacao` (graus), `levelId`, `tipo` ("Família : Tipo") | Único jeito de inserir mobília e louças pelo Vitruvius. Confere posição. |
| `get_walls` / `get_doors` / `get_windows` | Listagem antiga | `filter`, `levelId`, `wallId` | Substituídos por `list_elements`. Manter só por compatibilidade. |
| `get_wall_types` / `get_door_types` / `get_window_types` / `get_floor_types` | Tipos disponíveis | — | Pegar nome exato ou `typeId`. Floor types não trazem espessura (P9); usar `get_element` no tipo. |
| `resize_element` | Muda comprimento ou altura da parede | **`elementId`**, `newLength`, `newHeight` (só se não houver restrição superior) | Parede com restrição superior não muda de altura por aqui. |
| `move_element` | Move por deslocamento | **`elementId`**, **`delta`** {dx, dy, dz} (m) | Relativo, não absoluto. |
| `change_type` | Troca tipo mantendo a instância | **`elementId`**, **`newTypeId`** | — |
| `copy_element` | Copia com deslocamento | **`elementId`**, `vector` {x,y,z} (m) | — |
| `delete_element` | Apaga um elemento | **`elementId`** | Confirmar lista antes. Apagar remove dependentes (portas na parede). |
| `operar_elementos` | Operações em lote sobre elementos e vistas | **`acao`** ∈ apagar, mover, copiar, trocar_tipo, definir_parametro, inverter_lado, inverter_abertura, ocultar, mostrar, isolar, limpar_isolamento, colorir, limpar_cor; **`elementIds`**, `delta`, `typeId`, `paramName`, `value`, `viewId` (ações de vista), `cor` {r,g,b} | Usar para lote. Apagar pede conferência da lista `elementosRemovidos`. |
| `batch_modify` | Lote de move, resize, changeType, setParameter | **`operations`** [{type, elementId, ...}] | Alternativa a `operar_elementos`. Cada item tem seu resultado. |

## 4. Pisos, coberturas, topografia, escadas e outros

| Ferramenta | Para que serve | Parâmetros principais | Conferência / cuidado |
|---|---|---|---|
| `create_floor` | Piso por contorno | **`boundary`** [{x,y}], **`floorTypeId`**, **`levelId`**, `itens` | Ler a espessura do tipo antes (`get_element` no tipo). Macete depende dela. |
| `criar_elemento_superficie` | Piso ou cobertura por contorno, pela via nova | **`categoria`** ∈ piso, cobertura; **`contorno`** [{x,y}] sem repetir o primeiro, **`typeId`** (obrigatório em piso), **`levelId`**, `nome` | Equivalente a `create_floor`. Usar uma das duas. |
| `create_roof` | Cobertura plana por contorno | **`boundary`**, **`levelId`**, `roofTypeId`, `name` | Só plana (v1). Inclinada: lacuna declarada. |
| `create_topography` | Topografia por pontos | **`points`** [{x,y,z}] (m), `levelId`, `name` | Contorno é o retângulo dos pontos. Para terreno real, ver `levantamento`. |
| `create_shaft_opening` (`criar_abertura_shaft`) | Furo vertical em pisos e forros | **`contorno`** [{x,y}], **`levelId`** (base), `topLevelId` ou `altura`, `deslocamentoBase` | Escada não tem ferramenta; o furo serve para vão de escada. Declarar a lacuna. |
| `criar_guarda_corpo` | Guarda-corpo ao longo de caminho | **`caminho`** [{x,y}], **`levelId`**, `tipo` ou `typeId`, `fechar`, `deslocamentoBase` | Tipo sem nome exato: a resposta lista os disponíveis. |
| `criar_linha_separacao_ambiente` | Linha que fecha ambiente sem parede | **`caminho`** [{x,y}], **`viewId`**, `fechar` | Para varanda aberta e cozinha integrada. A área do ambiente recalcula. |
| `criar_pilar` | Pilar em ponto | **`ponto`** {x,y}, **`levelId`**, `altura` ou `topLevelId`, `estrutural` (true/false), `tipo` ou `typeId`, `rotacao` (graus) | Confere a altura e desfaz se divergir. |
| `criar_familia_pilar` | Cria família de pilar de concreto | **`largura`**, **`profundidade`** (m), `material`, `nome` | Salva em `D:/011_VITRUVIUS/_familias_vitruvius/`. Depois, `criar_pilar`. |
| `carregar_familia` | Carrega .rfa do disco | **`path`** (com barra normal), `sobrescrever` | Devolve `typeId` dos tipos. |
| `editar_familia` | Edita família carregada | **`acao`** ∈ listar, tamanho_texto, parametro; **`familia`**; `tamanhoMm`, `tipoTexto`, `nome`, `valor`, `tipoFamilia` | Só neste projeto. Listar antes de alterar. |
| `create_linked_model` | Vincula .rvt externo | **`modelPath`**, `origin` {x,y,z} | — |
| `create_grid` | Eixo reto | **`startPoint`**, **`endPoint`** {x,y}, `name`, `itens` | Eixo numérico não aparece em elevações Leste/Oeste (Revit). |
| `create_schedule` | Tabela de categoria | **`category`**, `fields` [], `name` | — |
| `import_image` | Importa imagem de referência | **`path`**, **`viewId`**, **`origem`** {x,y}, `larguraM`, `pxA`/`pxB`/`distanciaM` (calibração) | Para desenhar por cima de planta de referência. |
| `criar_elemento_ponto` | ver seção 3 |  |  |

## 5. Anotações e cotas

Ver `annotate` e `dimension` na seção 2.

## 6. Lacunas (sem ferramenta hoje)

- **Vão livre na parede (19/10/2026, plugin v62):** `criar_abertura_parede` — wallId, centro {x,y}, largura, altura e base, todos obrigatórios (medida = decisão de projeto). Recusa parede estrutural, vão cortando porta/janela e vão a menos de 0,10 m de encontro com outra parede. Integrar é o padrão; porta só com motivo escrito (Skill posicionamento-escada-residencial, seção 2-bis).
- **Quadro de áreas (20/10/2026, plugin v68):** `criar_quadro_areas` — areaLote (obrigatória), fatores (Skill quadro-de-areas-rj, por índice TO/CA/PERM, vale a primeira regra que casar), manuais ({esquema, nome, fator, contorno}), limites {toMax, caMax, tpMin}, baseIndices (menor/informada/medida). Traz do template ARQ.Sttk - 2026 os esquemas TAXA DE OCUPACAO, COEFICIENTE DE APROVEITAMENTO e PERMEABILIDADE e as tabelas QUADRO - X; cria PLANTA DE TAXA DE OCUPACAO, PLANTA DE COEFICIENTE DE APROVEITAMENTO - <pavimento> e PLANTA DE PERMEABILIDADE, com etiqueta em cada área; apaga áreas soltas; rodar de novo refaz. Primeiro uso: partido B do Ensaio 003, auditado pelo Hely (confirma com ressalvas).
- **Escada — limite (19/10/2026):** no máximo 10 espelhos por lance; reta com mais de 10 é recusada.
- **Escada (atualizado 19/10/2026):** ferramenta `criar_escada` criada (plugin v59). Sobe sempre para o nível imediatamente acima; formato reta, l ou u; o Oscar dá `inicio` (centro da largura no 1º espelho), `direcao`, `espelho`, `piso`, `largura` (mínimo 0,90; o tipo "ESCADA PROJETO" exige 1,00), e no L/U `espelhosPrimeiroLance` e `virar`. O Revit calcula os degraus. Junto: vão na laje de cima, guarda-corpo do vão (menos a borda de chegada e bordas com parede) e corrimão do próprio tipo, sem o lado encostado em parede. Recusa e desfaz se bater em parede ou se o tipo não aceitar. Conferir pela imagem da planta dos dois pavimentos e de um corte pela escada. **Só aparece para os agentes numa conversa nova** (o servidor MCP é recarregado ao abrir a sessão).
- **Cobertura inclinada:** só plana (`create_roof`).
- **Caminho da escada e linha de corte personalizada (NBR 6492):** sem ferramenta.
- **Tabela de revisão e nuvem de revisão:** sem ferramenta.
- **Matchline:** sem ferramenta.
- **Filtros gráficos por regra e sobreposição por filtro:** sem ferramenta (só `operar_elementos` por lista).
- **Sólido topográfico com corte e aterro:** sem ferramenta.
- **Peças (divisão por camada):** sem ferramenta.
- **Unidades do projeto:** sem ferramenta. Conferir a unidade de cada campo.
- **Mover marcador de elevação existente:** sem ferramenta (D12). **[19/10/2026, decidido por Claudemberg]** a elevação tem marcador **e** vista (linha tracejada com os limites); as duas precisam ir para fora da face. Enquanto o servidor não fizer isso, `create_elevation` está autorizado. Conserto pedido ao servidor Vitruvius.
- **Elevação de fachada (19/10/2026, decidido por Claudemberg):** marcador fora do lote, depois do muro (`create_elevation alvo: "modelo"`); duas vistas por fachada, COM MURO e SEM MURO (mesma `position`, `alvo: "edificio"`, `permitirMuroNaFrente: true`, `view_setup ocultarIds` nos muros); elevação nova substitui a antiga: apagar a vista antiga e o marcador vazio.
- **Ferramentas novas no `tools:` do Oscar (19/10/2026, autorizado por Claudemberg):** carregar_familia, editar_familia, criar_abertura_shaft, criar_elemento_linha/ponto/superficie, criar_familia_pilar, criar_pilar, criar_guarda_corpo, criar_linha_separacao_ambiente, import_image, operar_elementos.

## 7. Duplicidades e nomes antigos

Algumas ferramentas aparecem em dois nomes. Usar a forma indicada na coluna da seção:
- Parede: `create_wall` (macete, tipoPiso) ou `criar_elemento_linha` (categoria parede). Não usar os dois para a mesma parede.
- Porta e janela: `create_door`/`create_window` ou `criar_elemento_ponto`. Mesma função.
- Piso: `create_floor` ou `criar_elemento_superficie`.
- Listagem: `list_elements` no lugar de `get_walls`/`get_doors`/`get_windows`/`get_floors`/`get_rooms`.
- Cota: `dimension` (modo) substitui as antigas `dimension_wall`, `dimension_room` e similares.

## 8. Changelog
- 17/10/2026: criação a partir dos schemas carregados. Nomes exatos em português e inglês conforme o schema. Lacunas e duplicidades marcadas.
- **Pendente:** conferir cada parâmetro com uma chamada real de leitura (`get_levels`, `list_elements`) antes de usar para escrita. Atualizar a Skill do Oscar para apontar para este catálogo, depois de aprovação.
