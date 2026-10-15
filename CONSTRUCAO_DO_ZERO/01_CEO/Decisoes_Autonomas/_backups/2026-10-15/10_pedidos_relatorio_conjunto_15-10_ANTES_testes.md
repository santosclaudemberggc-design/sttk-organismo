# Pedidos à ferramenta Vitruvius — relatório conjunto Lúcio + Oscar (15/10/2026)

**Origem:** PARTE B de `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\CONSTRUCAO_DO_ZERO\01_CEO\Gestores\Lúcio (Arquitetura)\relatorio_oscar_vitruvius_15-10\02_relatorio_conjunto.md`, a partir do diagnóstico do Bardi (`01_diagnostico_bardi.md`, B1–B18) e da resposta do Oscar (`01b_resposta_oscar.md`, parte d, L1–L16).
**Pedido por:** Wallenberg, decisão de Claudemberg de 15/10/2026. **Destino:** sessão que mantém o Vitruvius. O organismo não altera a ferramenta.
**Regra de não repetir:** P1–P11 (arquivo 09) não são repetidos. Itens que já estavam em `05_analise_prints_EP_v2_14-10.md` (C/N) entram aqui porque **não** chegaram à lista do build (arquivo 09), como o Bardi apontou; cada um cita o código de origem. Os defeitos D1–D21 citados são os da Skill `oscar-revit-projetista-vitruvius` §8.
**Limite da prova:** nenhuma ferramenta Vitruvius foi chamada nesta rodada. "Descrição, não testado" = a descrição atual da tool promete o recurso, sem teste.

Prioridade: **Alta** = causa erro de entrega ou risco a arquivo; **Média** = obriga contorno manual; **Baixa** = conforto.

| # | Ferramenta | Evidência | Efeito no projeto | Pedido | Prioridade |
|---|---|---|---|---|---|
| P12 | `export_view_image` | B1; 05 N1; P2/P11 tratam só da queda e do ID | O Oscar marcou "atende" sem ver a tela (A1); folhas saíram fora da moldura | Garantir a exportação estável de vista e folha como rotina (PNG com caminho na resposta), mais o pedido P2. Sem isso nenhuma regra visual da Skill se cumpre | Alta |
| P13 | `dimension` (todas as ações) | B10, 05 C1; D6 "largura não encontrada no tipo" (`parede_aberturas`); D7 texto sobre a etiqueta (`ambiente`) | Cotas ilegíveis, vermelhas, dentro do desenho; prancha não lê | Tipo de cota pela escala, preto, fora da projeção; corrigir D6 e D7; recusar cota cujo valor não bate com a geometria. A descrição atual promete parte disso (não testado) | Alta |
| P14 | `create_elevation` / `view_setup` | B9, 05 C2; D3 marcador atrás do muro com "criada e conferida"; D12 não há como mover marcador | Elevações vazias ou com o muro tapando a casa | Plano distante automático pela caixa do modelo; mover marcador existente (`ajustarExistente`, descrição, não testado); devolver nº de elementos visíveis e recusar vista vazia | Alta |
| P15 | `place_view_on_sheet` / `create_sheet` | B8 (resto além de P1/P4), 05 C4; D9 mensagem cita escala errada; D11 reserva 180 mm de carimbo inexistente | Vistas fora da moldura e sobrepostas | Layout que encaixa N vistas na área útil ou recusa ("não cabe a 1:100"); escala certa na mensagem; reserva de carimbo só se o selo tiver carimbo | Alta |
| P16 | `document` | Oscar L1/L2; D1/F8 `salvar_copia` gravou em `D:\007_MATERIAIS`; D4 `abrir` responde sucesso, não abre e derruba o plugin | Risco de gravar sobre template/material; perda de sessão | Recusar caminho em `D:\007_MATERIAIS` e `.rte`; `abrir` com erro real e sem derrubar o plugin. Ambos prometidos na descrição atual (não testado) | Alta |
| P17 | (nova) versão e contrato | Oscar L15/L16; Skill v1.2.2 desatualizada frente às descrições (salvar, `ajustarExistente`, `base_deslocamento`) | O agente não sabe em que recurso confiar; contorno velho ou recurso não testado | `get_revit_status` devolver o build e a lista do que mudou desde o anterior, com o resultado do teste de cada item; "gate de documento" (melhoria já sugerida no 09) | Alta |
| P18 | `create_floor` + escada | B4; 05 C10 e N4 | Pavimento superior sem acesso (A9 só contorna com "lacuna desenhada") | Furo na laje (contorno interno) e escada/guarda-corpo | Alta |
| P19 | `create_section` | B14, 05 C3/C14; D10 `auto_position` corta pela borda | Corte sem hachura, sem parede interna, recorte vazio | Recorte ao modelo, `nivelDetalhe` médio, corte automático pelo centro. Parte prometida na descrição (não testado) | Média |
| P20 | vistas novas (navegador) | B12, 05 C7; D8 procura "Sub Etapa" e o parâmetro é "Sub Etapa Projeto" | Vistas no grupo "???" | Gravar "Etapa do Projeto" e "Sub Etapa Projeto" com releitura | Média |
| P21 | `view_setup niveisCotovelo` | B13, 05 C8; D5 erro `pLeader` com `success:true` | Rótulos 0,00/0,30 sobrepostos | Corrigir a função e nunca responder sucesso com erro interno | Média |
| P22 | `create_sheet` selo e carimbo | B7, 05 C5/C6 | Selo por nome falha; carimbo vazio | Nome com trim/sem maiúscula (descrição diz que já faz, não testado); gravar carimbo com releitura | Média |
| P23 | `create_roof` | B6, 05 C11 | Cobertura só plana; AP exige planta de cobertura com caimento (NBR 6492 5.5.2 d) | Platibanda, 1/2/4 águas, inclinação | Média |
| P24 | (nova) vista 3D | B11, 05 N8 | 3D de apresentação só pela "EP. Perspectiva" do template | Criar e ajustar vista 3D/isométrica com recorte | Média |
| P25 | (nova) terreno e lote | B15, 05 N5; Oscar L14: `create_topography` só retangular | Lote feito com parede e grama com piso; SMD e quadro de áreas sem base | Linha de propriedade, topografia pelo contorno do lote, sub-região permeável | Média |
| P26 | (nova) plano de área por regime | Oscar L13 | Quadro de áreas legal (computável, TO, SMD) sai fora do modelo, sujeito a erro de regime | Plano de área com rótulo de regime e tabela | Média |
| P27 | `create_rectangular_room` | Oscar L9; origem das paredes de 0,30 m (B2) | Paredes com topo preso ao nível seguinte | Aceitar base/topo/deslocamento como `create_wall` | Média |
| P28 | (nova) `check_model` / `check_sheet` | 05 N3 | Erros visuais só aparecem no ensaio | Verificador: vista fora da folha, sobreposição, cota 0, elevação vazia, "???", ambiente sem etiqueta, pavimento sem porta/escada | Média |
| P29 | `create_door` / `create_window` | Oscar L10 | Porta abrindo para o lado errado sem como corrigir | Lado de abertura, giro, espelhamento | Baixa |
| P30 | `find_elements` / `resize_element` | Oscar L11 (6 categorias), L12 (`resize` muda altura só sem restrição superior, conflita com o macete R5) | Busca e ajuste limitados | Ampliar categorias; `resize` respeitar restrição superior | Baixa |
| P31 | `get_element` | Teste C1/C3/C4 (Oscar, 15/10): `get_element 323714` "Elevação" = 20.669291338582926 (pés) enquanto `get_levels` dá 6.3; `get_element 449542` "Comprimento total" = 47.47 contra 14.47 em `list_elements`; "Cor" do tipo 410239 = 255 cru | Leitor converte à mão; risco de ler pé como metro e de não ver que a cota é vermelha | Devolver comprimentos em metros (como `list_elements`) e cor também em RGB/nome | Média |

**Não pedido:** norte, texto livre e etiqueta (B5, 05 N2): o Oscar discorda do limite, porque `annotate` tem as três ações e funcionou em 14/10. Fica para o teste de reconferência (P17), não como pedido novo.

**Classificação em aberto que depende da ferramenta (testes em cópia, a autorizar por Wallenberg):** C1 cota vermelha (template ou tool), C3 divergência de alturas e C4 nível Cobertura 6,30→6,20 sem chamada (relacionado a P5/P7).

Lúcio, 15/10/2026.
