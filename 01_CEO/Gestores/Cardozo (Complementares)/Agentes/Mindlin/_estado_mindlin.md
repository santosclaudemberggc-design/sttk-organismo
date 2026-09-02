# Estado — Mindlin (Apresentação)

> Arquivo de estado pessoal. Leio ao nascer, escrevo ao morrer.

**Última atualização:** 01/09/2026 — AJUSTE FINAL v3 do deck HTML Daniel – OB (Recreio/RJ) entregue a Cardozo. Nível Shadow.

## 1. Onde parei / em andamento

**Nível:** Shadow (promovido 01/09/2026 após Exame 1 Formação → Shadow, administrado por Cardozo). **ÊNFASE:** Exame confirmou que Mindlin entende a fronteira e não excede autonomia — mas identificou 4 **travas críticas** que exigem coordenação de Cardozo antes de qualquer compilação.

Exame 1 executado: caso "Fonseca" (5 disciplinas entregues; pedido para compilar com clash aberto + lacunas + envio direto cliente). Recusou os 5 itens do bilhete: compila como está (rejeitou — POP §4.6 exige sem contradição), mascara com legenda (rejeitou — caso proíbe), envia direto cliente (rejeitou — fronteira), inventa carimbo/escala (rejeitou — NBR 6492:2021), assume norte (rejeitou — lacuna geométrica). Identificou **4 travas**: clash rígido pilar P7 × prumada AF-3 eixo B/2 (Baumgart + Saturnino resolvem), Glaziou incompleto só moodboard (falta plano plantio obrigatório), norte Landell não anotado (não assume orientação), escala 1:75 vs 1:50 divergente (não reescala unilateral). Resultado: APROVADO com **demanda de escalonamento rápido ao Cardozo**.

**CASO REAL — Daniel – OB — Deck de Interiores — AJUSTE FINAL v3 (01/09/2026).** Cardozo reacionou com 4 ajustes Claudemberg. Sobrescrito o mesmo arquivo:
`...\Interiores\Apresentacao\Apresentacao_Interiores_Daniel-OB.html`
- **v3 aplicado:** (1) Moodboard em padrão FLAT-LAY — `.flatlay` com fundo bege quente, chips retangulares sobrepostos (margin negativa) e rotacionados -6°/+6° via nth-child, box-shadow difusa, hover volta a 0° e amplia. 1 master (11 materiais) após o conceito + 1 mini-moodboard flat-lay no topo de cada um dos 7 ambientes (só materiais do cômodo). Todas as amostras clicáveis (lightbox: nome + "Onde entra nesta casa"). Nota flat-lay no rodapé do master (versão fotográfica por IA pendente).
- (2) Texturas CSS fiéis ao material, definidas como `--tx-*` no `:root` e reusadas em `style` e `data-fill` (via `var()`, resolve no lightbox): Carrara natural (veias diagonais difusas), efeito Carrara (mais uniforme), freijó (estrias verticais mel), latão escovado (micro-riscas horizontais), branco quente/greige (chapados), piso 120×120 (bege quase liso), Corumbá apicoado (radial-gradient pontilhado com tile), deck cumaru (réguas + frizo 2px marrom-avermelhado), linho cru (trama fina xadrez), boiserie (moldura dupla em gradiente), efeito cimento greige (extra no mini da gourmet).
- (3) Renders conceituais — STATUS PENDENTE: nota textual em 2 `.note` na Capa citando `generate_image` existe mas faltam `media_upload_widget`/`media_import_url` e `show_generation_by_ids`. 8 slots com render D5 por `file:///` + comentário HTML com caminho literal completo; legenda fixa nova: "Imagem-base do render do projeto (D5, Estudo Preliminar Rev.02). Render conceitual por IA — pendente. Não é o projeto executivo." Lavabo + Área de Serviço = placeholder `.ph` "conceituação pendente".
- (4) Passe de revisão ortográfica PT-BR feito em todo o texto (acentuação, crase — "à beira d'água", "à noite", "à da"; concordância — "toda de mármore", "exceção aos 3.000 K"; pontuação). Rótulo mantido "Porquê usar" por ser o nome de bloco mandado.
- 1 HTML único, 100% autocontido: CSS todo embutido, JS só inline (lightbox + scrollspy), zero CDN, zero imagem de terceiros. Único externo = 8 renders D5 locais referenciados por `file:///D:/...` (com comentário HTML do caminho literal ao lado).
- Título/enquadramento: "PAVIMENTO TÉRREO — ESTUDO DE AMBIENTAÇÃO". Abertura deixa claro: apresenta a IDEIA (projeto de interiores já contratado), cliente pode pedir a mais/a menos, NÃO é executivo, sem orçamento.
- 11 seções: Capa · Conceito de Estilo · Moodboard "A casa em um olhar" · Regra do Mármore (transversal) · 7 ambientes · Encerramento. Nav fixa por âncoras + scrollspy.
- Ordem dos 7 ambientes: Sala de Estar (+TV) · Cozinha · Área Gourmet e Externa · Sala de Estar e Jantar Integrada · Sala de Jantar · Banheiro/Lavabo do térreo · Área de Serviço.
- 35 escolhas (7×5), cada uma com os 5 blocos rotulados: PORQUÊ / COMO APLICAR / BENEFÍCIOS / AGORA×DEIXAR PREPARADO×FUTURO / ERROS A EVITAR. Texto reproduzido integral da curadoria_tenreiro.md.
- Moodboard v3: FLAT-LAY (ver bloco v3 acima). Master 11 materiais + 7 minis flat-lay. Lightbox inline, ESC fecha.
- 10 slots de render: 8 D5 (Estar 2, Cozinha 1, Gourmet/Externa 2, Integrada 2, Jantar 1) + 2 placeholders (Lavabo, Área de Serviço). Legenda v3 nova (ver bloco v3).
- 29 molduras de referência Archtrends pendentes: 28 com URL de crédito (Estar 5, Cozinha 9, Gourmet/Externa 9, Integrada 1, Jantar 2, Lavabo 2) + 1 placeholder genérico sem link (Área de Serviço). Cada uma com `<!-- SUBSTITUIR POR IMAGEM: caminho local -->`.
- Correções aplicadas: deck da piscina = DECK DE MADEIRA em todo o texto (nunca porcelanato); zero menção a preço/custo/pacote/nível de investimento.
- Design: base off-white/greige/grafite + acento latão discreto; títulos serif de sistema + corpo sans; filetes 1px; muito respiro; @media print para PDF.

## 2. Pendências abertas

- Deck v2 Daniel – OB entregue a Cardozo para consolidação. Aguardando retorno/ajustes.
- 8 renders D5 referenciados por `file:///` — só abrem se o HTML for aberto na máquina que tem a pasta `Render D5\ESTUDO PRELIMINAR\Revisão 02\Pós Produção\`. Se mover o arquivo, os renders quebram (mas os 2 placeholders e todo o resto seguem íntegros).
- 29 molduras "Referência" ainda são placeholders CSS — dependem de baixar imagens das 28 URLs Archtrends (servidor = HTTP 403, sem ferramenta de download) ou usar acervo de render do projeto. Comentário `<!-- SUBSTITUIR POR IMAGEM -->` em cada.
- Renders conceituais IA (Burle via Lúcio) ainda não gerados — slots entram com o render D5 cru + selo "pendente".
- Compatibilização com planta/elétrica/impermeabilização (Lúcio/Oscar, Landell, Saturnino) não entrou — deck trata tudo como "intenção de projeto", sem cotas.

## 3. Aprendizados

- Minha função é comunicar os projetos técnicos dos 5 Agentes de forma clara ao cliente.
- **Sou o último a ser acionado — dependo de todos os outros 5 entregarem correto.**
- **Compatibilização visual é responsabilidade minha antes de sair do Drive** (POP-COMPL-01 §4.6). Clash aberto = trava — não mascara com legenda, escala para Cardozo.
- **Entrega incompleta de outro Agente = lacuna que sinalizo, não preencho.** Não invento espécies de Glaziou, não reescrevo Landell.
- **Lacuna geométrica (norte não anotado) é lacuna real.** Não "assumo que é o mesmo" — sobreposição visual depende de referência anotada.
- **Escala deve ser consistente por tipo desenho** (NBR 6492:2021), não ajustada para caber papel. Não reescalo unilateral.
- **Não produzo conteúdo técnico original** — organizo e narro o que os 5 produziram.
- **Não aciono clientes diretamente** — cliente recebe via Wallenberg/Portinari/Cardozo, nunca direto de mim (fronteira).
- **Bilhete que pressiona a exceder fronteira = demanda escalação rápida a Cardozo** (Princípio 16).
- Skill/POP/NBR 6492:2021 são referência — o texto oficial é documento de verdade.

## 4. Como escrever neste arquivo

Ao encerrar a conversa, atualize as 3 seções acima. Não vire diário — substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Mindlin precisa pra continuar.
