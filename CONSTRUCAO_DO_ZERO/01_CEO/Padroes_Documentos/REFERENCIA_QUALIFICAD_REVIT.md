# Referência — Tudo sobre Revit (QualifiCAD), visão geral (resumo)

> **Substituído para o Oscar por `REFERENCIA_QUALIFICAD_REVIT_OSCAR.md`**, que traz os passos transcritos. Este arquivo continua como índice dos 110 cards, com resumos curtos.

**Origem:** https://qualificad.com.br/tudo-sobre-revit/ (índice com 110 artigos, lidos em 17/10/2026).
**Natureza:** método geral de Revit, não norma e não regra da casa. Não substitui a Skill `oscar-revit-projetista-vitruvius`, as regras R1–R6/F1–F8 de Claudemberg nem as normas brasileiras.
**Uso:** consulta de método. Quando um artigo contradisser a Skill ou a norma do Rio, prevalece a Skill e a norma.

## Atenção: fontes de outra cidade ou sem norma citada

- **Taxa de ocupação e área permeável:** cita a LPUOS, Lei 16.402/2016, que é de **São Paulo**. Para o Rio, use LC 270/2024 e COES (LC 198/2019), via a Skill de vaga/COES e a base legislativa do Kelsen. O percentual de 30% de área permeável é premissa do autor, não regra.
- **Vaga PCD:** usa o Manual de Sinalização da **CET** e a cartilha do **CREASP**, ambos de São Paulo, com 2,40 m de largura, em conflito com 2,50 m do próprio artigo. Para o Rio, a vaga segue o COES: 2,50 × 5,00 m.
- **Escada espiral e escada em leque:** o autor afirma que NBR 9077 e NBR 9050 não tratam de escada espiral e usa a BS 5395-2 britânica. Também cita espelho máximo 0,18 m e piso mínimo 0,28 m como "NBR 9050". **Não verificado** na norma brasileira. Não usar sem conferir.
- **Guarda-corpo NBR 9050/9077:** cita valores (0,70 m, 0,92 m, 30 a 45 mm, 2,40 m, 1,20 m) sem indicar item normativo. Não usar sem conferir.
- **Linhas conforme NBR 16861:** valores de espessura (0,18 a 2,0 mm, proporção 1:√2 e grupos 1:2:4) são da norma citada pelo autor. Conferir na norma antes de usar.

## Ambientes e áreas (serve ao Oscar)

- **Ambientes no Revit — guia básico:** ambiente é volume delimitado por paredes, pisos, forros e telhados. Use "Colocar automaticamente" e "Realçar limites". Em paredes que não delimitam, desmarque "Delimitação de ambiente". Separador de ambiente divide um espaço em dois. Limite superior no nível, com deslocamento zero. **Área e volume dependem da referência da parede** (face de acabamento, centro, núcleo), definida em "Cálculos de área e volume". Número de ambiente é único; nome pode repetir.
- **Ambientes em espaços irregulares:** em terraço, escada ou pé-direito duplo sem fechamento, use o separador. Em telhado inclinado, troque o cálculo de volume para "Áreas e volumes" e ajuste a altura de cálculo. Em multinível, altura de cálculo acima do piso mais alto. Área e perímetro usam o piso; só o volume depende desses ajustes.
- **Tabela de ambientes:** categoria "Ambientes" (plural). Campos sugeridos: Nome, Área, Perímetro e Nível. Agrupar por nível com totais, depois por nome.
- **Ambientes irregulares:** ver acima.
- **Setorização de ambientes:** parâmetro "Departamento" como setor, legenda de cor com esquema por departamento.
- **Tabela chave (key schedule):** define valores padrão de acabamentos; alterar a chave atualiza todos os elementos vinculados. Útil para padronizar.
- **Parâmetro de contagem em fórmulas** (card completo lido em 17/10/2026): o parâmetro nativo "Contagem (Count)" não pode entrar em fórmulas de tabela, e o Revit mostra alerta. Motivo em três etapas: (1) coleta uma linha por elemento; (2) calcula as fórmulas linha a linha; (3) ao desmarcar "Itemizar cada instância", agrupa os iguais, e o valor já calculado por linha fica errado. Exemplo: duas portas tipo A a 500,00 cada; a tabela mostra "2 Porta A" com 500,00, quando o correto é 1.000,00. Alternativa, passo a passo: Propriedades > Editar em "Campos" > "Adicionar parâmetro calculado" (ex.: "Valor total", tipo moeda) > fórmula apenas "Custo" > confirmar > Formatação: trocar "Nenhum cálculo" por "Calcular os totais". Para Oscar: vale para quantitativo de esquadrias, não para área.
- **Taxa de ocupação e área permeável:** método: área de projeção ÷ área do terreno. Usa "Índices urbanísticos" como esquema de área. Ver alerta de São Paulo acima.
- **Criar peças:** divide paredes, pisos, telhados e forros em camadas independentes, para quantitativo por camada.
- **Marcenaria e quantitativos:** móveis planejados com família aninhada e parâmetros; tabela filtrada por material. Método útil para quantitativo de chapas, não para custo.

## Vistas, folhas e anotações (serve ao Oscar)

- **Vistas em planta:** nível só tem planta se "Criar vista da planta" estiver marcado. Faixa de vista padrão 1,20 m. Plantas estruturais usam corte de 0,30 m. "Região da planta" dá faixa diferente a uma área (ex.: janela de banheiro a 1,60 m).
- **Filtros gráficos:** selecionam elementos por regra (E/OU) e aplicam cor e hachura só nesses elementos. Ex.: destacar pisos com desnível abaixo de 0,00 m.
- **Sobrepor gráficos na vista:** altera a aparência de elementos só na vista atual. Remove com "Reinicializar".
- **Visibilidade/Gráficos (VG):** liga e desliga categorias por vista; sobreposições valem só na vista.
- **Ocultar elemento, categoria e por filtro:** afetam só a vista atual. Ocultar por filtro exige reativar o filtro para voltar.
- **Recorte de profundidade:** em elevação, "Recorte afastado". Em planta, o plano de corte da faixa de vista afeta a faixa inteira.
- **Chamada de detalhe:** cria vista de detalhe vinculada ao balão. Várias chamadas podem referenciar a mesma vista.
- **Editar texto da cota:** o artigo alerta para não alterar valores para representar medidas falsas. Corrija a geometria. Use o campo de texto para dúvidas de campo.
- **Identificador com pé-direito:** parâmetro compartilhado e identificador de ambiente com pé-direito. Método trabalhoso.
- **Marca e marca de tipo:** marca identifica cada instância; marca de tipo identifica o tipo. Use marca para porta individual e marca de tipo para especificação.
- **Tabela de revisão na folha:** campos fixos (sequência, número, descrição, data, emitido para, emitido por). **Não permite campos personalizados.** Construir de baixo para cima, texto 2,0 a 2,5 mm.
- **Nuvem de revisão:** preencher revisões antes; desenhar perímetro fechado; atribuir revisão; alterar ordem de numeração depois gera conflito; "Emitido" trava a revisão.
- **Linha coincidente (matchline):** divide planta grande em folhas com vistas dependentes e referência de vista nas extremidades. ISO 128-20 sugere linha traço-ponto grossa; não há norma brasileira específica citada.
- **Chamada de detalhe e caminho da escada:** NBR 6492 pede seta de sentido ascendente e circunferência de 3 mm no primeiro degrau, com numeração dos degraus no mesmo sentido. No Revit: anotação "Caminho da escada", símbolo inicial "Ponto aberto 3mm", categoria "Setas para cima" em VG.
- **Bloco de notas e símbolo de anotação genérica:** notas em tabela e símbolos paramétricos (acessos, norte, desníveis). Útil para anotação de projeto.
- **Nota-chave:** código CSI MasterFormat para elementos, tipos e materiais. Útil para especificação.
- **Perfil de corte e símbolo de corte personalizado:** muda a aparência de um corte só na vista. Não altera a geometria nem os quantitativos.
- **Estilo de linha e subcategorias:** subcategorias valem para todas as vistas; sobreposição de vista só para a atual.
- **Renomear famílias e tipos:** tabelas se atualizam; o nome do tipo deve refletir os parâmetros.
- **Navegador de projeto personalizado:** agrupamento por disciplina, fase ou família; filtros de vista.
- **Transferir padrões de projeto:** copia estilos de cota, filtros e tipos de sistema de um arquivo para outro. Duplicar a família de sistema antes.
- **Atualizar arquivo de versões anteriores:** atualizar em degraus; guardar cópia da versão original; revisar textos, guarda-corpos e tabelas depois.
- **Unidades:** configurar formato por disciplina; símbolo de unidade desligado nas cotas. Cuidado com pés e polegadas.
- **Norte do projeto e localização:** rotacionar norte do projeto por linha de referência; norte verdadeiro para estudo solar; localização por endereço.
- **Interface, ViewCube, medir, câmera:** operação básica. Câmera a 1,60–1,80 m de altura para perspectiva de olho humano.
- **Vista 3D — anotações e cotas:** plano de trabalho para cotas em face; vista bloqueada.
- **Linhas ocultas:** tracejado segue NBR 16861 no artigo; escala muda o tamanho do tracejado.
- **Renderização e materiais PBR:** rascunho para testar, região para recorte, 200–300 DPI na versão final. Materiais PBR a partir do Revit 2019. Procedurais só em baixa resolução.
- **Cores personalizadas e livros de cores:** Pantone, RAL e outros por arquivo de cor.
- **Texto 3D e logotipos:** texto do modelo com fonte TrueType; logos complexos por família genérica.

## Modelagem (útil de forma geral, não substitui a ferramenta Vitruvius)

- **Paredes:** função (Interior, Exterior, Fundação, Retenção, Sofito e Shaft-núcleo) muda o comportamento e aparece em tabelas. Virada de revestimento em vista de planta. Paredes inclinadas (ângulo de -90° a 90°), cônicas (Revit 2022+) e por perfil incorporado (molduras). Paredes irregulares por edição de perfil ou massa.
- **Parede cortina:** colunas contínuas com duas famílias (só verticais, só horizontais). Parede curva por painel de vidro curvo. Montante personalizado a partir de perfil métrico. Vidraça inclinada por telhado. Limite: perímetro único e fechado.
- **Pisos, lajes e vigas:** vigas por nível e offset; faixa de vista com profundidade negativa para ver as vigas do piso. Sistema de vigas com regra de layout.
- **Escadas:** escada por croqui (limite, espelhos, caminho); degrau em leque e espiral com parâmetros do autor (ver alerta de norma); encontro da escada com a laje por deslocamento superior; escada que não encosta na laje precisa de ajuste em corte.
- **Portas e famílias:** família de porta com batente e guarnição por varredura; família de template com planos de referência e cotas EQ; alças de manipulação com parâmetros de instância; família aninhada para quantitativo; família que fura face (vazio) para cuba, nicho e ralo.
- **Telhados:** calha, borda (fascia) e sofito com perfis; sofito no beiral com seta de inclinação; caimento mínimo de 5% em vidraça.
- **Guarda-corpo e corrimão:** duplicar tipo e editar famílias aninhadas; corrimão de parede com suporte circular. Alturas do autor não verificadas.
- **Fórmulas e parâmetros:** operadores aritméticos e trigonométricos; sem "≥" e "≤"; nomes sem hífen ou espaço; arredondar com IF. Fórmulas de parâmetro de família.
- **Eixos, linhas de referência e planos de referência:** plano é infinito e serve a restrições; linha é finita e serve a rotação (folha de porta).
- **Fixar, desafixar e cadeado:** fixar bloqueia mover e excluir; cadeado cria restrição geométrica, revelável pela barra de status.
- **Operações de edição:** painel Modificar (alinhar, deslocar, espelhar, matriz, dividir); "Colocar por segmento" para paredes hospedadas.
- **Terreno e sólido topográfico:** sólido topográfico por esboço ou importação CSV/TXT (X, Y, Z separados por vírgula). Corte e aterro por tabela de quantidades (exemplo: 52,81 m³ de aterro; escavação com saldo de -912,28 m³). Configurações de curva de nível e material de corte. Arquivo de pontos com ponto e vírgula deve ser trocado por vírgula antes da importação.
- **Iluminação:** luminotécnica no Revit (lúmen, lux, candela, Kelvin); famílias com arquivo IES. O artigo não mostra cálculo de lux dentro do Revit.
- **Vaga e rampa:** rampa por inclinação em "1/x"; até 25% é o máximo citado para garagem, com cautela acima de 23%. Confirmar COES e NBR 9050 no caso do Rio.

## Versões, licença e atualizações

- **Revit 2024, 2025, 2026 e 2027 (novidades):** os resumos trouxeram recursos de paredes em camadas paralelas, paredes hospedadas por segmento, sólido topográfico reformulado e sol em perspectiva. **A atribuição de cada recurso a um ano não foi confirmada** (a leitura cruzou as páginas de novidades); antes de citar um ano, abrir a página correspondente. Use para saber o que existe no Revit da casa, não como regra.
- **Service packs e atualizações:** instalar só as que afetam as ferramentas usadas; reiniciar e conferir versão em Ajuda > Sobre.
- **Revit LT:** versão limitada, sem sistemas MEP, worksets, massas, filtros e Dynamo. Não recomendada para projeto em equipe.

## Lista completa dos artigos (110), por assunto

Ambientes: ambientes guia básico; ambientes em espaços irregulares; tabela de ambientes; setorização; tabela chave; parâmetro de contagem em fórmulas; taxa de ocupação e área permeável; criar peças; marcenaria e quantitativos.

Vistas e anotações: vistas de planta; filtros gráficos; sobrepor gráficos; visibilidade e sobreposição; ocultar elementos; recorte de profundidade; chamada de detalhe; editar texto da cota; identificador com pé-direito; marca e marca de tipo; tabela de revisão; nuvem de revisão; matchline; caminho da escada NBR 6492; bloco de notas; símbolo de anotação genérica; nota-chave; perfil de corte; corte com símbolo personalizado; estilo de linha; subcategorias; renomear famílias; transferir padrões; navegador personalizado; unidades; norte do projeto; localização geográfica; ViewCube; câmera e vistas 3D; anotações e cotas na vista 3D; linhas ocultas; exportar tabelas para Excel; linhas conforme NBR 16861; ferramenta medir; painel modificar; interface do Revit.

Modelagem: paredes (funções, virada, irregulares, perfis incorporados, cortina colunas, cortina curva, montante, vidraça inclinada, corrimão, guarda-corpo, guarda-corpo personalizado, balaústre clássico, guarda-corpo NBR 9050/9077); pisos e vigas (vigas guia básico, sistema de vigas, eixos, linhas e planos de referência, iluminação guia básico); escadas (espiral, leque, croqui, encontro com laje, caminho da escada); telhados (calha, borda, sofito); famílias (template básico, porta, aninhada, furar face, alças, fixar, cadeado, subcategorias, peças, renomear); fórmulas (guia básico, básicas, trigonométricas); terreno (configurações, arquivo de pontos, sólido topográfico, sólido corte e aterro, texto 3D e logotipos, vaga PCD, rampa para veículos, vigas, parâmetro de contagem).

Materiais e render: cores personalizadas; materiais realistas PBR; visualizador; materiais personalizados; materiais procedurais; materiais de alta e baixa resolução; renderização.

Versões e atualizações: Revit 2024, 2025, 2026, 2027; service packs; Revit LT; atualizar arquivo de versões anteriores.

Total: 110 artigos.

## Pedidos ao Vitruvius que saem deste material

Ver `D:\011_VITRUVIUS\PEDIDOS_OSCAR\10_pedidos_adicionais_qualificad_17-10.md`.

## Changelog
- 17/10/2026: criação. Leitura de 110 artigos do índice QualifiCAD. Alertas de fonte de São Paulo e de normas não verificadas.
