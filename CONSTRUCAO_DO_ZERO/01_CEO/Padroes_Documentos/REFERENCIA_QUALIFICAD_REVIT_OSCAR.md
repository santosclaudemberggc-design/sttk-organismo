# Referência QualifiCAD para o Oscar — leitura com transcrição de passos (17/10/2026)

**Substitui, para o Oscar, o resumo `REFERENCIA_QUALIFICAD_REVIT.md`.** Os cards aqui foram relidos pedindo a transcrição dos passos, com caminhos de menu.
**Natureza:** método de Revit, não regra. Não substitui a Skill `oscar-revit-projetista-vitruvius`, as regras de Claudemberg (R1–R6, F1–F8) nem as normas.
**Atenção:** cada passo abaixo é do Revit. Quem executa no projeto é o Vitruvius. Antes de usar um passo, o Oscar precisa saber qual ferramenta do Vitruvius faz o equivalente. Isso está pendente no catálogo das ferramentas.

## 1. Ambientes e áreas

### Ambientes no Revit — guia básico
- **Caminho:** Arquitetura > Ambiente e área > Ambiente.
- **Opções:** "Colocar ambientes automaticamente" (um em cada espaço fechado da vista), "Realçar limites" (paredes que delimitam, em laranja), "Identificar na colocação".
- **Parede que não delimita:** selecionar a parede > Propriedades > desmarcar "Delimitação de ambientes". Conferir com "Realçar limites".
- **Dividir ambiente:** Arquitetura > Ambiente e área > Separador de ambiente; uma linha divide em dois.
- **Altura:** padrão é limite superior no Nível 1 com deslocamento de 4,00 m. Recomendado: limite superior em um nível de piso e deslocamento zero, para o ambiente acompanhar o nível. Não é possível associar o ambiente ao forro.
- **Área, perímetro e volume:** área e perímetro vêm dos delimitadores; o volume confere o limite superior e depende do cálculo de volume.
- **Cálculo de área e volume:** Arquitetura > Ambiente e área > seta > Cálculos de área e volume. Referência da parede: acabamento, centro, núcleo ou centro do núcleo. A padrão (acabamento) é a recomendada.
- **Número:** automático e único; repetido gera alerta. Nome repetido agrupa em legendas de cor.
- **Acabamentos (piso, parede, forro, base):** são campos de texto, não materiais reais. Indicados para projetos grandes e padronizados.
- **Alerta:** "Altura não delimitada" não é a altura do chão ao teto; é a altura do ambiente pelos níveis e deslocamentos.

### Ambientes em espaços irregulares
- Terraço, escada ou pé-direito duplo sem fechamento: usar Separador de ambiente para fechar o espaço.
- Paredes inclinadas: Cálculo de volume = "Áreas e volumes". Cálculo de altura do nível um pouco abaixo da altura do nível (ex.: 3,49 m para nível de 3,50 m; igual dá erro).
- Telhado: mesmo caminho; o ambiente só fecha se houver delimitadores.
- Multinível: nível mais baixo com "Cálculo de altura" zerado vaza. Definir cálculo de altura maior que o piso mais alto (ex.: 3,50 m para piso de 3,00 m). Todo nível precisa de piso.
- Mezanino: desmarcar "Delimitação de ambiente" do piso do mezanino para ignorá-lo.
- Área e perímetro usam o piso; só o volume depende desses ajustes.

### Tabela de ambientes
- **Criar:** Vista > Criar > Tabela/Quantidades, ou botão direito em Tabelas/quantidades > Nova. Categoria "Ambientes" (plural).
- **Campos:** Nome, Área, Perímetro (ponto de partida); Nível se houver vários pisos. Adicionar com duplo clique ou seta verde.
- **Ordenar:** Propriedades > Outros > Classificar/Agrupar > Nome.
- **Separar por nível:** Campos > adicionar Nível; Classificar por Nível (Rodapé, Títulos e totais), depois Nome.
- **Ocultar coluna Nível:** Propriedades > Formatação > Nível > Oculto, ou botão direito no cabeçalho > Ocultar coluna (mantém o agrupamento).

### Setorização de ambientes
- Criar ambientes (Ambiente, clique em cada espaço). Renomear com duplo clique no título.
- Propriedades > Dados de identidade > Departamento: nome do setor (o Revit memoriza os já criados).
- Anotar > Preenchimento de cores > Legenda de preenchimento de cor > tipo "Ambientes" e esquema "Departamento".
- Editar esquema: Modificar | Legenda > Editar esquema > Título e esquema de cor. Duplicar a vista para outro esquema.

### Tabela chave
- Criar: Vista > Criar > Tabela/Quantidades > categoria Ambiente > marcar "Chaves da tabela" > nomear > campos > OK.
- Preencher: Modificar tabela | quantidades > Linhas > Inserir linha de dados; valores repetidos podem ser reaproveitados.
- Atribuir: selecionar o ambiente (pelo X) > Propriedades > "Estilo do Ambiente" > escolher a chave. Campos incluídos ficam cinza com "=" e só mudam pela tabela.
- Luminárias: mesma lógica, com parâmetros próprios (potência, fluxo, temperatura de cor) e grupo "Fotométrica".

### Taxa de ocupação e área permeável (método; legislação do Rio é outra)
- Esquema de área "Índices urbanísticos" (Cálculos de área e volume > Esquemas de área > Novo).
- Planta de área do mesmo tipo (Ambiente e área > Área > Planta da área).
- Limite de área no terreno (Ambiente e área > Limite de área), linhas fechadas e sem sobreposição; usar levantamento topográfico.
- Áreas com Área (Ambiente e área > Área > Área), depois a legenda de cor opcional.
- Tabela: Navegador > Tabelas/Quantidades > Nova > categoria "Área (Índices urbanísticos)" com Nome e Área; parâmetro calculado "Percentual".
- Definições: taxa de ocupação = projeção da construção ÷ terreno; área permeável = área livre de edificação ÷ lote. Fórmulas são implícitas; o autor não as escreveu.
- **Alerta:** o artigo cita a LPUOS (Lei 16.402/2016), que é de **São Paulo**. Os 30% de permeável são premissa do exemplo. Para o Rio, valem a LC 270/2024 e o COES.

### Criar peças
- Selecionar parede > Modificar > Criar > Criar peças > Enter. Cada camada vira peça.
- Visibilidade de peças: Mostrar peças, Mostrar original ou Mostrar ambos (Propriedades).
- Dividir: Modificar | Peças > Dividir peça; Editar croqui; confirmar duas vezes. Mesclar: selecionar duas ou mais e "Mesclar peças". Excluir e "Restaurar peça". Forma: alças e "Redefinir forma". Material: desmarcar "Material original" e escolher o material.
- Quantitativo por camada: Nova Tabela/quantidades > categoria Peças > campos Material, Área e Contagem > Classificar por Material e **desmarcar** "Itemizar todas as instâncias".
- **Alertas:** para editar o tipo da parede, usar "Mostrar original". Ao alterar a forma, a peça indica "A forma foi modificada". Peças excluídas continuam selecionáveis no local.

## 2. Vistas, folhas e anotações

### Vistas em planta
- Nível (LL): "Criar vista da planta" ativo gera a planta; desativado, o nível fica preto e sem vista. "Tipos de vista da planta" escolhe quais criar (Piso, Forro refletido, Estrutural).
- Vista > Criar > Vistas de planta: a janela só oferece níveis sem planta. "Não duplicar vistas existentes" desmarcado cria duplicata.
- **Tipos:** Planta de piso (plano de corte 1,20 m; ajuste em Faixa de vista); Planta de forro refletido (corte 2,30 m; portas e janelas não aparecem); Planta estrutural (disciplina Coordenação; faixa de vista -1,20 m, profundidade -1,80 m, corte 0,30 m; janelas não aparecem).
- **Região da planta:** Vista > Criar > Vista da planta > Região da planta; desenhar perímetro fechado; Propriedades > Faixa da vista (ex.: 1,60 m para janela de banheiro); Editar limite; a caixa tracejada verde marca a área e não imprime.
- Planta da área: setorização; tipo próprio no Navegador.

### Filtros gráficos
- Visibilidade/Gráficos (VG) > Filtros > Editar/Novo > Novo (nome) > categoria > regras.
- Regras: E (todas verdadeiras) ou OU (uma basta); "Adicionar regra" e "Adicionar conjunto".
- Aplicar: na janela, Adicionar > filtro > coluna "Cortar" (paredes) ou "Projeção/Superfície" (pisos) > Padrões > Sobrepor (cor e hachura).
- Exemplo: paredes com Comentário igual a "Hidráulica" (improvisado; o autor prefere parâmetro próprio). Pisos com "Altura do deslocamento do nível" menor que 0,00 m.
- Texto do critério precisa ser idêntico ao valor. Desativar com "Ativar filtro" sem apagar.

### Sobrepor gráficos na vista
- Selecionar > botão direito > Sobrepor gráficos na vista > "Por elemento" ou "Por categoria".
- Campos: Visível; Meio-tom; Linhas de projeção (subjacência); Padrões de superfície (Primeiro plano e Plano de fundo); Transparência 0–100%; Linhas de corte; Padrões de corte.
- Remover: "Reinicializar" na janela, ou campo em "Por estilo de objeto" ou "Sem sobreposição".
- Vale só para a vista atual.

### Visibilidade/Gráficos (VG)
- Vista > Gráficos > VG (ou Propriedades > Gráficos > Visibilidade/sobreposição).
- Abas: Categorias do modelo, Modelo, Anotação, Modelo analítico, Categorias importadas, Filtros.
- Colunas: Visibilidade (caixa), Projeção/Superfície (Linha, Padrão com Primeiro plano e Plano de fundo, Transparência), Cortar (Linha, Padrões).
- Limpar tudo: canto inferior esquerdo > "Limpar Sobreposições". Vale só para a vista.

### Ocultar elemento, categoria e filtro
- Ocultar elemento: selecionar > Modificar > Vista > Ocultar (lâmpada) > Ocultar elemento.
- Ocultar categoria: mesmo caminho, com "Ocultar categoria"; itens de outras categorias continuam visíveis.
- Ocultar por filtro: definir característica (ex.: Comentário); VG > Filtros > Novo; categoria; regra; Adicionar ao VG; desmarcar Visibilidade.
- Revelar: barra de controle de vista > lâmpada; "Desocultar elemento" ou "Desocultar categoria". Para filtro, reativar a Visibilidade do filtro.

### Recorte de profundidade
- Elevação: Propriedades > Extensões > "Recorte afastado" > Sem recorte, Recortar sem linha ou Recortar com linha. Ajustar a caixa de recorte no símbolo de elevação.
- Planta: Propriedades > "Recorte de profundidade" (mesmas opções) e Faixa de vista > Plano de corte. Afeta a faixa inteira.

### Chamada de detalhe
- Vista > Criar > Chamada de detalhe; tipo Retângulo ou Croqui; alças azuis ajustam o balão; ícone de rotação.
- "Referenciar outra vista" (marcado antes de desenhar): mostra "SIM" quando a vista é semelhante.
- Acesso: Navegador ou duplo clique no cabeçalho. Cabeçalho sem preenchimento antes da folha é normal.
- Excluir a chamada exclui a vista de detalhe (alerta).

### Editar texto da cota
- Duplo clique no valor > janela "Texto da cota". Valor: "Usar valor real" (padrão) ou texto. Campos de texto em volta do número.
- "Mostrar a legenda na vista" só com parâmetro global atribuído.
- "Visibilidade da chamada de detalhe" da cota: por elemento, sempre ou nunca.
- **Alerta do autor:** não altere valores para mostrar medidas falsas; corrija a geometria. Trocar ponto por vírgula contorna o alerta, mas o valor deixa de ser real.

### Marca e marca de tipo
- Marca: parâmetro incorporado, único por instância (portas nº 1, nº 2). Na paleta Propriedades. Número repetido gera erro.
- Marca de tipo: por tipo; todas as instâncias compartilham. Em Editar tipo.
- Identificador de categoria: porta mostra a marca (cápsula); janela mostra a marca de tipo (hexágono).
- Marca não é fabricante, que tem campo próprio.

### Identificador com pé-direito (método trabalhoso)
- Gerenciar > Parâmetros compartilhados > Criar TXT > grupo "Forro" > parâmetro "Pé-direito" (Comprimento).
- Gerenciar > Parâmetros do projeto > Adicionar > Parâmetro compartilhado > categoria Ambientes > tipo Instância.
- Identificador: Editar tipo > Duplicar > campos; Editar família > Criar > Texto > Legenda > parâmetro Pé-direito (metros, 2 casas, símbolo) > "Parâmetro de família associado" (novo).
- Forro: "Altura do deslocamento do nível" > Novo parâmetro global. Ambiente > Pé-direito > Associar parâmetro global.
- **Alertas:** o valor mostrado é o do forro. Um global por altura. Cada forro novo precisa do global; usar filtro para lote.

### Tabela de revisão na folha
- Abrir a família da folha (Blocos de margem e carimbo > Editar Tipo).
- Vista > Criar > Tabela de revisão > campos: Sequência, Número, Descrição, Data, Emitido para, Emitido por. **Não há campos personalizados.** Mover parâmetro para ordenar.
- Classificar por Sequência de revisão. Aparência: construir "De baixo para cima"; texto 2,0 a 2,5 mm.
- Salvar a família, Carregar no projeto, arrastar a tabela para a folha.

### Nuvem de revisão
- Vista > Composição da folha > Emissões/Revisões de folhas: preencher revisões (Número, Descrição, Data, Emitido para/por; "Exibir": Nenhum, Identificador ou Nuvem e identificador).
- Organizar por projeto ou por folha. Alterar numeração depois gera conflito. "Comprimento do arco" é global; na vista acompanha a escala, na folha é fixo.
- Anotar > Detalhe > Nuvem de revisão: desenhar perímetro fechado; Espaço inverte arcos; Propriedades > Revisão > Concluir.
- Identificar: Anotar > Identificador > Identificar por categoria.
- "Emitido" trava a revisão.

### Linha coincidente (matchline)
- Vista > Composição da folha > Linha coincidente; desenhar; Concluir (tracejada por padrão).
- Duplicar como dependente duas vezes (ex.: "Nível 1 – A" e "Nível 1 – B").
- Em cada cópia: Exibir região de recorte > deixar só o lado da folha > Ocultar região.
- Folhas novas (A1 métrico) com cada vista. Referência da vista (Composição da folha) nas extremidades, com Vista de destino. Duplo clique leva à outra vista.
- Norma: não há brasileira; o artigo cita ISO 128-20 (traço-ponto de 0,5 a 0,7 mm).

### Caminho da escada (NBR 6492)
- Ao criar a escada, anotação "Caminho da escada" automática. Tipo: "Direção para cima / para baixo automática" ou "Direção fixada para cima".
- Tipo de símbolo inicial: "Ponto aberto 3mm" (circunferência de 3 mm exigida no primeiro degrau). Extensão inicial: não recomendada.
- Percurso completo: VG > Categorias de anotação > Caminhos da escada > marcar "<Acima> Setas para cima" > Aplicar.
- Linha de interrupção: tipo da escada > Editar tipo > Tipo de marca de corte (zigue-zague, extensão ~3 mm, ângulo 25°).
- Numeração de degraus: Anotar > Identificador > Piso da escada / número do espelho; Tipo de marcação (espelhos ou pisos); Exibir regra (todos, ímpares, pares ou primeiro e último).
- Fonte da numeração não muda. Limpeza: VG > Categorias de modelo > Escadas > desmarcar <Acima> linhas de bocel e de espelho.
- O artigo cita a NBR 9077 para o arco no patamar e a linha tracejada de interrupção.

### Exportar tabela para Excel
- Arquivo > Exportar > Relatório > Tabela > CSV ou TXT (só esses dois).
- Excel: Arquivo > Abrir > Procurar > "Arquivos de texto" > Assistente: delimitador vírgula (CSV) ou tabulação (TXT).
- Sem vínculo: mudanças no Revit exigem nova exportação. Sem fórmula, sem formatação.
- Comentário do artigo: com ponto e vírgula, Dados > De Texto/CSV.

### Unidades do projeto
- Gerenciar > Unidades do projeto (atalho UN). Escolher a disciplina; clicar no Formato de cada grandeza.
- Campos: Unidades (métricas, pés e polegadas, "Metros e centímetros" não recomendada); Arredondamento (Personalizado para incremento); Símbolo de unidade (desligado por padrão; ligar em inclinações e rampas); Suprimir 0's à direita; Suprimir 0 pés e Suprimir espaços (só em pés e polegadas fracionais); agrupamento de dígitos.
- Digitar com unidade (cm, mm, ', ") é respeitado pelo Revit.
- Cota: Propriedades > Editar tipo > Unidades primárias e alternativas; desmarcar "Usar as configurações do projeto" só afeta aquele estilo.

### Norte do projeto e localização
- Norte: Gerenciar > Localização do projeto > Posição > seta > "Rotacionar norte do projeto" > "Alinha a linha ou plano selecionado" > clicar numa linha do lote.
- Conferir: Propriedades > Gráficos > Orientação (Norte do projeto ou Norte verdadeiro). A bússola do ViewCube mostra o norte verdadeiro.
- Autor desaconselha girar o arquivo de topografia.
- Localização: Gerenciar > Localização > "Lista de cidades padrão" (latitude, longitude, fuso) ou "Serviço de mapas" (endereço). Caminho do Sol > Configuração do sol.
- Precisão aproximada; limites e pontos exatos pedem levantamento geodésico.

### Câmera e ViewCube
- Câmera: Vista > Criar > seta de Vista 3D > Câmera. Primeiro clique = posição; segundo = alvo. Aparece em Vistas 3D.
- Elevação do olho entre 1,60 e 1,80 m; olho e alvo na mesma altura dão visão linear. Perspectiva, não ortogonal.
- Vista cortada: alça de profundidade. Círculo de navegação > Aumentar/Diminuir comprimento focal (com limite). Enquadramento: não ampliar demais.
- ViewCube: setas giram 90°; casinha volta à vista inicial ("Definir vista atual como a principal"); "Orientar para a vista"; "Definir frente para a vista".

### Vista 3D — anotações e cotas
- Duplicar a vista 3D; Caixa de seleção para isolar; ocultar a caixa; Salvar a orientação; bloquear.
- Cotas: Arquitetura > Plano de trabalho > Definir > "Selecionar um plano" > clicar na face. Cada direção pede um plano de trabalho.
- Vista explodida: Deslocar elemento. Vista bloqueada não orbita.

### Linhas ocultas
- Propriedades > Gráficos > "Mostrar linhas ocultas": Nenhum, Por disciplina (padrão: Arquitetura não exibe; Estrutural e instalações exibem), Todos. Vale só na vista.
- Vista > Gráficos > "Exibir linhas ocultas" por elemento (Seleção múltipla na barra de opções). Elemento totalmente oculto: estilo "Estrutura de arame".
- Tracejado segue NBR 16861 (artigo). Comentário diz que a NBR 8403 foi cancelada e incorporada pela 16861 — não verificado.
- Escala muda o tamanho do tracejado.

### Estilo de linha, subcategorias e perfil de corte
- Manipulação de estilo de linha: selecionar a linha > escolher o estilo; só na vista; "Por categoria" reinicia. Útil para linhas ocultas.
- Subcategorias: Família > Categoria; Gerenciar > Estilos de objeto > Nova (subcategoria); Propriedades > Dados de identidade > Subcategoria. Estilos de objeto valem em todas as vistas; VG só na atual.
- Perfil de corte: Vista > Gráficos > Perfil de corte > clicar no elemento > desenhar o trecho que falta > concluir. Só na vista; não muda geometria; quantitativos continuam com a geometria original.

### Criar linhas conforme NBR 16861
- Espessuras aceitas (mm): 0,18 | 0,25 | 0,35 | 0,5 | 0,7 | 1,0 | 1,4 | 2,0. Proporção 1:√2. Grupos fina:larga:grossa 1:2:4.
- Padrão de linha: Gerenciar > Configurações adicionais > Padrões de linha > Novo; traço = 24d, espaço = 3d, ponto = 1d, em que d é a espessura larga (ex.: d = 0,25 mm: traço 6 mm, espaço 0,75 mm, ponto 0,25 mm).
- Aplicar: Gerenciar > Estilos de objeto > Objetos de anotação > Linha de corte > Padrão de linha.
- O espaçamento impresso não muda com a escala.
- Tabela completa é imagem no artigo; não transcrita.

### Símbolo de corte personalizado
- Localizar: Editar tipo do corte > Identificador de corte; Navegador > Pesquisar; Editar a família.
- Planos de referência ligados em VG; desenhar com Linha (Arquitetura > Detalhe); preenchimento com Região preenchida.
- Salvar como (outro nome); Carregar no projeto; Editar tipo > Duplicar > Identificador do corte > três pontinhos > Extremidade da linha de corte > símbolo.
- Linha de corte: Estilos de objeto > Linha de corte > Traço-ponto.
- Norma citada: NBR 6492 prevê um único símbolo de corte para arquitetura; NBR 8403 para traço-ponto estreito (cancelada, segundo outro comentário — não verificado).

### Vistas de planta, nível e região — ver seção "Vistas em planta".

## 3. Paredes, portas, escadas e modelagem

### Funções de parede
- **Interior:** entre níveis; Altura desconectada bloqueada; restrição superior já preenchida, editável.
- **Exterior:** padrão; altura desconectada de 8 m; pode atravessar níveis ou ligar ao telhado.
- **Fundação:** para baixo do nível atual; geralmente com parede empilhada; profundidade bloqueada.
- **Retenção:** muro de arrimo, altura 2,00 m (ajustável).
- **Sofito:** segmento abaixo do teto, altura desconectada 0,25 m (ajustável).
- **Shaft núcleo:** atravessa pavimentos; 8,00 m (ajustável).
- Aparece em tabelas de quantitativos (coluna Função, filtro Igual / Não igual) e em filtros de vista (Visibilidade/Gráficos > Filtros > Função igual a).
- **Relevante ao Oscar:** a função errada muda o que entra no quantitativo. Ex.: shaft não é parede externa.

### Virada de revestimento
- Selecionar parede > Editar tipo > Estrutura > Editar > "Virada do revestimento padrão".
- Nas inserções: Não virar (padrão), Exterior, Interior, Ambos.
- Nas extremidades: Nenhum (padrão), Exterior (recobrimento mais completo no exemplo), Interior.
- Atalho: Editar tipo > Construção > "Virar nas inserções" e "Virar nas extremidades".
- Só aparece em planta, não em corte. Em peitoril, ativar nas extremidades corrige a exibição no vão.

### Paredes com perfis incorporados (molduras e frisos)
- Família de perfil: Arquivo > Novo > Família > modelo "Perfil métrico"; desenhar perfil fechado (um por arquivo); carregar no projeto.
- Molduras: Parede > Editar tipo > Duplicar > Estrutura > Editar > em corte: "Extrusão por percurso" > Adicionar. Opções: Perfil, Material, Distância e De (Base ou Topo; topo com valores negativos), Orientação (só em parede inclinada), Lado (interna ou externa), Deslocamento, Recuo (ao redor de portas e janelas), Cortar a parede, Cortável.
- Frisos: mesmo caminho com "Frisos". Opções parecidas, mais Inverter.
- O Revit não diferencia perfil de moldura e de friso: escolher o correto para cada função.

### Paredes irregulares e inclinadas (método geral)
- Inclinada: Propriedades > Seção transversal "Inclinada" > ângulo de -90° a 90°, a partir da vertical.
- Cônica (Revit 2022+): camada "Variável" em Editar montagem.
- Topo ou base irregular: anexar a telhado ou plano de referência.
- Perfil irregular: Editar perfil (croqui fechado); "Redefinir perfil" desfaz.
- Forma muito complexa: massa no local > converter faces em paredes (Parede por face).

### Escada por croqui
- Arquitetura > Circulação > Escada; família base (ex.: Monolítica) > Criar croqui.
- Desenhar Limite (laterais), Espelhos (degraus; autor usa 28 cm de piso), Caminho da escada. Concluir.
- Inverter: Modificar | Criar escada > Ferramentas > Inverter.
- Editar tipo > Construção > "Superfície da parte inferior" = Escalonado.
- Converter um lance: Ferramentas > Converter (irreversível) > Editar croqui só daquele trecho.
- **Alerta:** em escada por croqui do zero, quantidade de degraus e fórmula de Blondel ficam com o usuário; a conversão calcula automaticamente.
- Valores de espelho e piso citados pelo autor como ABNT e Bombeiros: não verificados.

### Escada que encontra a laje
- Em corte: Editar escadas; bolinha do lance superior para acrescentar degrau; "Ok".
- Alerta do Revit: ajustar "Deslocamento superior" (altura de degrau, ex.: 0,17 m, arredondado pelo autor).
- Piso: Editar limite; desenhar contorno com espaço para o degrau; Confirmar.
- **Alertas:** verificar viga de apoio, amarração da armadura antes de ajustar geometria, e não manter alertas no projeto (podem agravar na atualização).

### Escada espiral e escada em leque
- Espiral: "Espiral com degraus completos" (um lance) ou "Espiral por centro e extremidades" com "Manter concêntrico"; raio interno de 0,16 m (piso estreito em torno de 5 cm).
- Leque: duplicar tipo; calculador de escadas; estilo "Equilibrado" ou "Ponto único"; largura mínima 0,15 m; Converter para croqui.
- **Não verificado:** o autor afirma que NBR 9050 e 9077 não tratam de espiral e usa BS 5395-2. Espelho 0,18 m e piso 0,28 m atribuídos à NBR 9050 pelo autor. Não usar sem conferir.

### Portas, famílias e template
- Template básico (Modelo genérico métrico): quatro planos de referência com cotas EQ; cotas de largura e profundidade viram parâmetros de tipo; plano de altura com ALTURA. Salvar como .rfa e renomear .rft.
- Porta personalizada: modelo "Porta métrica"; marco e guarnição por varredura, alinhados a planos e travados com cadeados; folha por extrusão com folga de 1 mm; maçaneta como família aninhada; vista em planta com máscara e arco de abertura a partir da dobradiça; tipos por medida.
- Família aninhada: carregar uma família dentro de outra e restringi-la; marcar como compartilhada para quantificar.
- Família que fura face: vazio (geometria negativa) com "Cortar geometria" (cuba, nicho, ralo).
- Alças de manipulação: planos ou linhas de referência com cotas transformadas em parâmetros de instância.
- Linha de referência (finita, controla rotação) x plano de referência (infinito, alinha e restringe).
- Renomear: tipo em Editar tipo > Renomear; família pelo Navegador (botão direito > Renomear). Categoria não renomeia.
- Fixar: bloqueia mover, rotacionar e excluir, mas permite copiar. Desafixar temporário (alfinete) ou permanente.
- Cadeado: restrição geométrica; Revelar restrições na barra de status mostra e remove.

### Fórmulas
- Parâmetros de família e cotas. Operadores +, –, *, /, ^, parênteses; sqrt, sin, cos, tan, asin, acos, atan, IF, AND, OR, NOT; sem "≥" e "≤"; funções em inglês; maiúsculas diferem; nomes sem hífen, espaço ou caractere especial.
- Medidas em metros (0,01 = 1 cm). Arredondamento com IF.
- Trigonometria: "Altura / tan(Inclinação)"; Pitágoras com sqrt e ^. Unidade de ângulo não esclarecida pelo artigo.

### Eixos
- Arquitetura > Dados > Eixo: clique para início e direção; arco, linha, multissegmento; Deslocamento para eixos equidistantes.
- Numeração automática; para letra, editar o valor numérico do eixo e digitar a letra (a sequência continua).
- Bolha: caixa na extremidade; bolinha ajusta comprimento; cadeado liga eixos alinhados (desmarcar para mover um a um).
- 2D/3D: ícone 3D; quebra (cotovelo) para afastar bolhas; "Propagar extensões" para outras vistas.
- **Alerta:** eixo numérico não aparece em elevações Leste/Oeste (só em vistas alinhadas).

### Vigas e sistema de vigas
- Estrutura > Estrutura > Viga; tipo (aço, concreto, madeira); nível e offset nas restrições; faixa de vista com profundidade negativa (-0,10 m) para ver as vigas do piso.
- Sistema de vigas: limite fechado; "Regra do layout" (distância fixa, número fixo, espaçamento máximo, limpar); direção.

### Rampa para veículos (ver alerta de norma)
- Arquitetura > Circulação > Rampa, ou piso inclinado. Editar tipo: "Comprimento da inclinação máxima" e "Inclinação máxima da rampa (1/x)" (ex.: 9 m ÷ 2 m = 4,5).
- Garagem: até 25% em muitos municípios; cautela acima de 23%.
- Curvas: largura extra; recuo de 4 m para visibilidade da calçada.
- Escavar: rampa precisa de massa de vazio e Cortar no sólido; piso inclinado usa Escavar.
- Inclinação: anotação "Inclinação do ponto" em percentual.
- **Alerta:** o artigo manda conferir a NBR 9050 e as normas locais; não detalha.

### Vaga PCD (ver alerta de São Paulo)
- Família métrica com VAGA_LARGURA e VAGA_PROFUNDIDADE; faixas de 0,10 m; símbolo centralizado a 0,35 m da base; família aninhada.
- Dimensões citadas: paralela 5,80 m; perpendicular 2,40 m; oblíqua 3,30 m; profundidade 5,00 m (CREASP, com 2,50 m de largura). Fonte: CET (SP) e Lei 13.146/2015 (reserva de 2%).
- **Para o Rio, usar o COES: vaga 2,50 × 5,00 m (ver Skill de vaga).**

### Telhados
- Calha: Arquitetura > Telhado > Calha, clicar na borda; deslocamentos; perfil em Editar tipo; "tampa" nas extremidades. Caimento não tratado.
- Borda (fascia): Telhado > Borda; perfil em Editar tipo; duplicar para perfis diferentes; deslocamentos; Unir geometria.
- Sofito: Telhado > Sofito; duplicar família; contorno com cadeados; no trecho inclinado, seta de inclinação e deslocamento final zero.
- Vidraça inclinada: Telhado por perímetro com tipo "Vidraça inclinada"; caimento mínimo de cerca de 5%; unidade em percentual (UN).

### Guarda-corpo e corrimão
- Guarda-corpo personalizado: duplicar, editar famílias aninhadas (barra chata 20 x 5 mm; balaústre 3D); parâmetros de colocação.
- Balaústre clássico: alturas de corrimão 0,70 m e 0,92 m; planos em 600 mm e 820 mm; corrimão de 30 a 45 mm; afastamento de 40 mm da parede; corrimão intermediário duplo acima de 2,40 m.
- Corrimão de parede: duplicar guarda-corpo; remover balaústres; suporte "Suporte-Metal-Circular" em Corrimão 1.
- **Não verificado:** valores atribuídos à NBR 9050 e 9077 sem item normativo.

### Cadeados, fixar e restrições
- Ver seção "Famílias".

### Paredes cortina
- Colunas contínuas: duas famílias (só verticais; só horizontais); painel de vidro trocado pela família oposta.
- Vidro curvo: duplicar parede genérica; espessura 0,02 m; "Painel de parede cortina"; grade sem montantes horizontais.
- Montante personalizado: família de perfil "Perfil métrico-Montante"; tipo de montante por duplicação; limites: linha menor que 0,8 mm não aceita; um perímetro fechado.
- Vidraça inclinada: ver telhados.

### Criar família de template básico e porta — ver "Portas, famílias e template".

## 4. Terreno, topografia e quantitativo

### Sólido topográfico
- Massa e terreno > Modelar terreno > Sólido topográfico > Criar do esboço (limite) ou Criar da importação (CAD ou CSV/TXT).
- Modificar subelementos: alça ou aresta; cota positiva ou negativa; Base da elevação e Deslocamento. Novos pontos medidos a partir do clique, não de 0,00.
- Adicionar ponto, Adicionar linha divisória, Redefinir forma, Subdividir.
- Camadas padrão de 1000 mm para baixo (Editar tipo).
- Terreno antigo: Gerar sólido topográfico a partir da superfície.

### Sólido topográfico com corte e aterro (tabela de quantidades)
- Terreno em fase "Existente"; Massa e terreno > Análise > Região graduada (cópia idêntica) para a "Construção nova".
- Gerenciar > Fase > Fases > Sobreposição de gráficos (Existente, meio-tom se necessário).
- Filtro de fase do terreno original: "Mostrar Novo".
- Vista > Criar > Tabela de quantidades > Sólido topográfico > "CORTE E ATERRO", fase Construção nova; campos Corte, Preenchimento, Corte/Preenchimento líquido.
- Exemplo do autor: elevar pontos 0,50 m deu 52,81 m³ de aterro; piso de 15 × 15 m em Escavar deu saldo de -912,28 m³ (negativo = terra a remover).

### Terreno com arquivo de pontos
- Formato: CSV ou TXT, cada linha X, Y, Z separados por vírgula (ex.: 20,10,2.961), a partir da origem do levantamento.
- Ponto e vírgula: o Revit não lê; corrigir no Bloco de notas (Editar > Substituir ";" por ","), ou importar como "Texto delimitado por vírgula".
- Vista Terreno > Massa e terreno > Modelar Terreno > Superfície topográfica > Criar da importação > Especificar arquivo de pontos > Formatar (unidade) > ajustar malha > Confirmar.
- **Alertas:** unidade errada distorce o terreno; coordenadas devem bater com o levantamento e o ponto base.

### Configurações do terreno
- Massa e terreno > seta do painel Modelar terreno: intervalo de curvas de nível (com curvas adicionais), material do corte, profundidade do volume pela elevação de base poche, unidades das linhas de divisa.
- Subregião, nível e implantação: não tratados.

### Localização e norte — ver seção "Vistas e anotações".

### Iluminação (luminotécnica)
- Luz (lúmen, lux, candela, Kelvin) x elétrica. NBR 8995-1 citada para ambientes internos de trabalho.
- Luminárias métricas: formato da fonte (ponto, linha, retângulo, círculo) e distribuição; arquivos IES para fidelidade na renderização.
- Cálculo de lux dentro do Revit: não detalhado pelo artigo.

### Medir elementos
- Medir entre duas referências (Ctrl = perpendicular); Cadeia (medições seguidas); ao longo de um elemento (linha inclinada mostra ângulo em X); Tab antes do clique para segmentos.
- Serve para conferência rápida; cota some ao trocar de ferramenta ou Esc.

## 5. Renderização, materiais e cores (uso secundário para o Oscar)

- **Renderização:** Vista > Apresentação > Renderizar (RR). Qualidade: Rascunho (1 nível) a Melhor (20 níveis). Testar em Rascunho e região; 200–300 DPI na versão final.
- **Materiais PBR:** a partir do Revit 2019, alta resolução com mapas de textura; converter em Navegador de recursos (Biblioteca de aparência > Superfície fosca).
- **Baixa resolução:** tradicional, com alerta amarelo; procedurais só nesse tipo.
- **Visualizador de materiais:** Gerenciar > Materiais > Aparência; Cena, Ambiente e Qualidade. Qualidade não altera o projeto.
- **Materiais personalizados:** Gerenciar > Materiais; propriedades por tipo (metálico, não-metálico, transparente).
- **Cores:** Aparência; livros de cores (.acb: Pantone, RAL, Suvinil); bibliotecas .adsklib.
- **Texto 3D:** Arquitetura > Texto do modelo; fonte TrueType instalada; logos complexos por família genérica.

## 6. Versões, atualizações e padrões

- **Revit LT:** sem sistemas MEP, worksets, massas, filtros e Dynamo. Não recomendado para equipe ou projeto complementar.
- **Service packs:** instalar as que afetam as ferramentas usadas; reiniciar; conferir em Ajuda > Sobre.
- **Atualizar arquivo antigo:** Arquivo > Abrir (não dar duplo clique); prévia mostra a versão; marcar Auditar; Abrir. Guardar cópia do original (não abre mais na versão antiga). Atualizar passo a passo, uma versão por vez.
- **Alertas por versão** (ex.: 2017 — legendas de nota-chave, guarda-corpos no piso; 2018 — famílias com dimensão ligada à geometria, aumento de ~10% no arquivo; 2020 — materiais automáticos em superfícies analíticas; 2022 — macros Ruby; 2023 — linhas de dobra em pisos). Conferir textos, tabelas e famílias depois de atualizar.
- **Transferir padrões de projeto:** Gerenciar > Configurações > Transferir padrões de projeto > "Copiar de" > "Marcar nenhum" e escolher. Por padrão tudo vem marcado. Conflito de tipo: "Duplicar Tipos" > "Sobrescrever" ou "Somente novo". Duplicar a família de sistema antes.
- **Navegador personalizado:** agrupar por Disciplina, Fase ou Família; filtros de vista; esquemas com Novo.
- **Nota-chave:** código CSI MasterFormat (16 divisões); tipos: do elemento, do material e do usuário (por vista); configurar arquivo de dados e numeração.
- **Bloco de notas:** tabela de anotações genéricas (Vista > Tabelas).
- **Símbolo de anotação genérica:** estático (escala gráfica) ou paramétrico (Legenda com Item e Descrição); acessos, norte, desníveis.
- **Atualizar arquivo, pontos, unidade:** ver seções próprias.

## 7. Limites desta leitura

- Os passos foram transcritos com o conteúdo do artigo; menus podem mudar de nome conforme a versão do Revit (o próprio artigo alerta).
- **Não verificados:** valores normativos atribuídos a NBR 9050, 9077 e 6492 pelos autores; a versão do Revit usada em cada artigo; o capítulo de renderização em detalhe.
- **Fora do Rio:** LPUOS (SP), CET e CREASP (SP).
- Nenhum item substitui a Skill, as regras R1–R6 e F1–F8, nem a conferência pela imagem.

## 8. Ligação com o Vitruvius

Cada seção acima é um procedimento do Revit. Para o Oscar, o passo só vale quando houver a ferramenta do Vitruvius que faz o equivalente, com o contrato dela (parâmetros, unidades, IDs e leitura de conferência). O catálogo dessas ferramentas está pendente; ver `D:\011_VITRUVIUS\PEDIDOS_OSCAR\` e a proposta de catálogo.

## Changelog
- 17/10/2026: criação. Foram relidos com transcrição dos passos os cards de ambientes, tabela de ambientes, setorização, tabela chave, vistas, filtros, sobreposição, visibilidade, ocultar, recorte, chamada de detalhe, cota, marca, revisão, nuvem, matchline, caminho da escada, exportação, unidades, norte, localização, câmera, linhas ocultas, NBR 16861, perfil de corte, símbolo de corte, funções de parede, virada, perfis, escada por croqui, escada e laje, sólido com corte e aterro, terreno por pontos, transferir padrões, atualizar versões, eixos, peças, pé-direito e parâmetro de contagem.
- **Ainda em resumo (não relidos com transcrição):** portas e famílias, fórmulas, alças, fixar e cadeado, rampa, vaga PCD, telhados, guarda-corpo e corrimão, paredes cortina, sólido topográfico, configurações do terreno, iluminação, medição, renderização, materiais e cores, Revit LT, service packs, novidades por versão. As seções correspondentes acima trazem o conteúdo do resumo anterior. Antes de usar qualquer um deles para orientar o Oscar, reler com transcrição.
