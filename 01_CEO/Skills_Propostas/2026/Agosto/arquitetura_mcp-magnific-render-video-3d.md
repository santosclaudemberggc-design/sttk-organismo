---
name: skill-proposta-arquitetura-mcp-magnific-render-video-3d
description: "PROPOSTA — Magnific MCP (mcp.magnific.com) é conector MCP oficial de 1ª parte (Freepik/Magnific) com mais de 40 tools de imagem/vídeo/áudio/3D, conecta ao Claude Code em 1 comando (sem chave de API, OAuth com plano web já existente); acionado por indicação de Claudemberg (post de terceiro no Instagram, verificado antes de virar achado) — resolve render fotorrealista a partir de imagem 2D (print/sketch/planta) e vídeo, mas não faz tour 360 nem lê modelo BIM diretamente como o Twinmotion"
metadata:
  type: skill_proposta
  status: proposta_pendente_criacao_do_gestor
  gestor_alvo: Lúcio (Arquitetura) — não implantado
  agente_alvo: futuro Agente de Renders/Vídeos (equipe de Lúcio, função já aprovada em pendencias.json id lucio-agentes-nao-nomeados)
  data: 2026-08-01
---

# Skill proposta: conector MCP Magnific — render fotorrealista/vídeo a partir de imagem 2D

## Para quem é
Gestor **Lúcio (Arquitetura)** — ainda não implantado — para o futuro Agente de Renders/Vídeos. Segunda Skill do dia sobre o mesmo gap (`feedback_render_video_mcp_lucio`), complementar à de hoje cedo (`arquitetura_mcp-render-video-twinmotion-scanbimlabs.md`) — não a substitui, são abordagens diferentes para entradas diferentes.

## Origem do achado
Claudemberg trouxe, ao vivo, um post do Instagram (perfil "sobre.arq", conteúdo promocional de terceiro, não fonte técnica) mostrando o fluxo Claude + MCP + Google Drive + Magnific gerando renders automaticamente a partir de imagens numa pasta. Como o post é material de marketing de terceiro (inclusive com call-to-action "comente RENDER" para um evento pago), **nada dele foi tomado como fato sem verificação própria** (Princípio 3) — o achado abaixo vem de checagem direta em 4 fontes independentes: `docs.magnific.com/modelcontextprotocol`, `magnific.com/mcp`, resultados de busca agregados citando a mesma documentação, e um artigo de terceiro (`scopeful.org`) sobre a mudança de cobrança da API do Magnific em 2026.

## O que ensina/entrega

1. **É conector oficial de 1ª parte, não projeto comunitário** — diferença central em relação ao achado da manhã (Twinmotion/ScanBIM Labs, "comunidade", popularidade baixa). O Magnific MCP é mantido pela própria empresa (Freepik/Magnific), com documentação própria e blog dedicado ao uso dentro do Claude.
2. **Conexão trivial no Claude Code**: `claude mcp add --transport http magnific https://mcp.magnific.com`. Autenticação por **OAuth** com a conta Magnific já existente — sem chave de API para gerenciar ou rotacionar. Também funciona em Claude Web, ChatGPT e Cursor.
3. **Mais de 40 tools**, cobrindo: geração/edição de imagem (texto->imagem, SVG, upscale, remoção de fundo, crop inteligente), **geração de vídeo**, síntese de voz (TTS), **geração de modelo 3D**, treinamento de personagem/estilo consistente ("Soul"), e gerenciamento de histórico/pastas/Spaces.
4. **Entrada é imagem 2D, não modelo BIM** — diferença de arquitetura em relação ao Twinmotion: o Magnific não lê um arquivo Revit/IFC; ele parte de uma imagem (print de SketchUp, sketch à mão, planta, foto de maquete, render bruto) e gera uma versão fotorrealista via modelos de imagem/vídeo (a documentação cita catálogos acessíveis via `images_models_list`/`video_models_list`, sem fixar nomes de modelo como fato permanente — evitar tratar isso como lista congelada). É exatamente o fluxo mostrado no post: pasta no Drive com imagens do projeto -> Claude localiza os arquivos -> chama o Magnific -> devolve a versão renderizada.
5. **Não resolve tour 360** — nenhuma das tools listadas na documentação gera passeio navegável; cobre render still e vídeo (possivelmente fly-through simples via geração de vídeo a partir de imagem), não substitui Matterport/equivalente.
6. **Custo mudou em 2026 e varia por fonte — checar ao vivo antes de comprometer orçamento (Princípio 3)**: a API antiga "pay-per-usage" foi descontinuada em 30/06/2026; hoje é por plano com créditos pré-comprados. Fontes de terceiro divergem nos números — uma cita Pro em ~US$39/mês (2.500 tokens) e Business em ~US$299/mês; outra cita Business a partir de ~US$55/usuário/mês (anual) para uso em equipe. **O MCP em si não tem custo adicional** — usa os créditos do plano web que a conta já tiver; então o gasto real depende de qual plano o organismo assinar, não da conexão MCP.

## Ação proposta
Não conectar/assinar ainda — é achado de pesquisa, não recomendação de compra. Quando o Gestor Lúcio e o Agente de Renders/Vídeos forem formados: (1) confirmar o preço vigente direto em `magnific.com/pricing` (não nos agregadores, que divergem) antes de qualquer decisão de assinatura; (2) testar o fluexo real (Drive -> Claude -> Magnific) com um caso de baixo risco, comparando qualidade/tempo contra o candidato do Twinmotion; (3) as duas Skills de hoje (Twinmotion e Magnific) não competem — avaliar se o organismo precisa das duas (uma para quando existe modelo BIM pronto, outra para referência 2D rápida) ou só uma, quando o Agente for formado; (4) continuar a busca por tour 360 (Matterport e equivalentes seguem sem conector MCP encontrado).

## Fonte da pesquisa
- Post no Instagram, perfil "sobre.arq", 06/07/2026 — **conteúdo de marketing de terceiro, indicado por Claudemberg**; usado só como pista inicial, não como fonte técnica (nenhuma afirmação dele foi usada sem checagem própria).
- [Magnific MCP — documentação oficial](https://docs.magnific.com/modelcontextprotocol) — URL do servidor, autenticação OAuth, lista de categorias de tools, comando de conexão no Claude Code.
- [Magnific MCP — página oficial](https://www.magnific.com/mcp) — confirma "Every agent runs Magnific", compatibilidade com Claude (Web e Claude Code), ChatGPT e Cursor (fetch direto bloqueado por 403; conteúdo confirmado via resultado de busca agregado e via docs.magnific.com).
- [Magnific API Pay-Per-Usage Discontinued — Scopeful](https://www.scopeful.org/blog/magnific-api-pay-per-usage-discontinued-2026) — mudança de modelo de cobrança em 30/06/2026, planos Business ~US$55/usuário/mês (anual), MCP como alternativa sem custo adicional para quem já tem plano web.
- Busca de preço agregada (Costbench e outros) citando Pro ~US$39/mês e Business ~US$299/mês — **divergência não resolvida entre fontes**, sinalizada explicitamente, não escolhida arbitrariamente.
- Pesquisado em 01/08/2026, mesma rotina/sessão do achado da manhã (Twinmotion), em resposta a indicação ao vivo de Claudemberg.

## Governança
Proposta pendente — Lúcio (Arquitetura) ainda não foi criado como Gestor; esta Skill fica arquivada para quando ele for aprovado e a equipe for formada. Não altera nenhuma Skill oficial hoje, e não autoriza assinatura/conexão do conector — é registro de candidato encontrado e verificado, sujeito a checagem de preço ao vivo e teste técnico no momento do uso real (Princípio 3). Sob o modelo de ratificação posterior (20/07/2026), a criação do Gestor Arquitetura e a ativação desta Skill passam a ser decisão do próprio Wallenberg quando o teste de contratação for aplicado — mas seguem sujeitas a ratificação na Reunião Semanal. Busca de render/vídeo/tour 360 **continua aberta** (ver `feedback_render_video_mcp_lucio`).
