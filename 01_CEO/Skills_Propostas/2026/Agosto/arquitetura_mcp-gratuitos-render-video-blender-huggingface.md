---
name: skill-proposta-arquitetura-mcp-gratuitos-render-video-blender-huggingface
description: "PROPOSTA — resposta a pedido explícito de Claudemberg por conectores MCP GRATUITOS (não freemium) de render/vídeo/360; achado principal é Blender MCP (ahujasid/blender-mcp, 25,2k estrelas, MIT, 100% gratuito para sempre), complementado por Hugging Face MCP oficial (conta grátis + créditos ZeroGPU) e mcp-video-gen/CogVideoX (vídeo grátis, qualidade irregular); nenhum resolve tour 360 multi-ponto tipo Matterport de graça"
metadata:
  type: skill_proposta
  status: proposta_pendente_criacao_do_gestor
  gestor_alvo: Lúcio (Arquitetura) — não implantado
  agente_alvo: futuro Agente de Renders/Vídeos (equipe de Lúcio, função já aprovada em pendencias.json id lucio-agentes-nao-nomeados)
  data: 2026-08-01
---

# Skill proposta: stack de conectores MCP gratuitos — render, vídeo e panorama 360

## Para quem é
Gestor **Lúcio (Arquitetura)** — ainda não implantado — para o futuro Agente de Renders/Vídeos. Terceira Skill do dia sobre o mesmo gap (`feedback_render_video_mcp_lucio`), depois de Twinmotion (achado da manhã, comunitário/pago) e Magnific (achado da tarde, oficial/pago) — esta responde ao pedido explícito de Claudemberg de focar em **gratuito**, não freemium.

## O que ensina/entrega

### 1. Achado principal: Blender MCP (ahujasid/blender-mcp)
**Gratuito de verdade, não "trial de produto pago"** — Blender é software livre, o conector é open source (MIT). Verificado direto no GitHub: **25.200 estrelas, 2.400 forks**, 168 commits — de longe o MCP de 3D mais adotado encontrado em toda a busca desta rotina (mais popular que qualquer conector de render já registrado, pago ou gratuito).

- **O que faz de fato**: cria/edita objetos e cena via linguagem natural, aplica material/luz/câmera, baixa HDRI e textura grátis do Poly Haven, gera modelo 3D por IA (Hyper3D Rodin, Hunyuan3D), tira screenshot do viewport, busca modelo no Sketchfab.
- **Render/vídeo/360 não são tools nomeadas** — a documentação não lista `render_still`/`render_animation`/`render_panorama` como comandos dedicados. A capacidade existe via uma tool genérica ("executar qualquer código Python no Blender"), que dá acesso à API completa do Blender (`bpy`) — incluindo o motor de render Cycles, a timeline de animação e a câmera equirretangular nativa (panorama 360°). **Funciona, mas exige prompt mais específico/técnico, não é botão único** — diferença importante em relação a um produto comercial com comando pronto.
- **Requisitos**: Blender 3.0+, Python 3.10+, gerenciador `uv`. Documentação confirma Claude Desktop, Cursor, VS Code, OpenCode — **não confirma explicitamente Claude Code**, precisa testar na prática antes de assumir compatibilidade.
- **Gap de entrada**: não lê modelo Revit direto — precisa exportar para FBX primeiro. Existe exportador FBX gratuito via plugin do Twinmotion (grátis) e exportadores dedicados com trial (30 exports/15 dias, ProtoTech). Materiais/texturas frequentemente quebram na conversão Revit->FBX->Blender e precisam ser reatribuídos manualmente — fricção real, não zero-esforço.
- **360° real**: é uma **foto panorâmica única** (câmera equirretangular), visualizável em qualquer viewer 360 — não é tour multi-ponto clicável como Matterport. Nenhuma opção gratuita ou paga encontrada até hoje faz isso.

### 2. Complemento para entrada 2D: Hugging Face MCP (oficial)
Conector **oficial** da própria Hugging Face (`huggingface.co/mcp?login`), mesmo fluxo do achado da tarde (Magnific: imagem de referência -> versão fotorrealista), mas sem custo de assinatura. Conta gratuita dá créditos via "ZeroGPU-powered Spaces" para rodar modelos como Flux e Qwen-Image (imagem) e Spaces de geração de vídeo. Limite exato da camada gratuita não veio especificado na fonte oficial (só que conta Pro amplia o limite) — **checar na prática antes de depender disso em caso real** (Princípio 3).

### 3. Complemento de vídeo gratuito: mcp-video-gen (CogVideoX)
Projeto comunitário (`kevinten-ai/mcp-video-gen`) que empacota CogVideoX como "gratuito ilimitado" via MCP, ao lado de provedores pagos (Kling, Vidu, MiniMax). CogVideoX é modelo aberto (Apache 2.0) real, mas avaliações de terceiro mostram qualidade irregular — falha em rosto/mão, artefatos de flicker, clipes curtos (6-10s, 720p). Serve para rascunho/preview, não para entrega final a cliente sem revisão.

### 4. Avaliado e descartado: ComfyUI MCP e Vivideo MCP
- **ComfyUI MCP** (múltiplos projetos, ex. `Peleke/comfyui-mcp`): gratuito de verdade (Stable Diffusion/Flux locais, sem limite de uso), mas exige computador com GPU rodando ComfyUI localmente — não é solução de zero instalação, fica registrado como opção futura se o organismo tiver máquina dedicada.
- **Vivideo MCP** (`@vivideo/mcp`): código aberto (MIT) mas cobrança real é por crédito de uso ("usage-based pricing") — só o primeiro vídeo é gratuito. **Não atende ao critério de gratuito contínuo** pedido por Claudemberg, descartado desta rodada.

## Ação proposta
Não instalar/testar ainda — achado de pesquisa, não recomendação de uso imediato em caso real. Quando o Gestor Lúcio e o Agente de Renders/Vídeos forem formados: (1) testar Blender MCP com Claude Code especificamente (compatibilidade não confirmada na fonte); (2) testar o pipeline Revit->FBX->Blender com um caso de baixo risco antes de confiar em material/textura automática; (3) usar Hugging Face MCP como alternativa gratuita ao Magnific para renders 2D rápidos, checando o limite real de uso na prática; (4) tratar mcp-video-gen/CogVideoX como rascunho, não entrega final; (5) tour 360 multi-ponto **continua sem solução gratuita ou paga** — vigilância contínua mantida.

## Fonte da pesquisa
- [Blender MCP — GitHub oficial (ahujasid/blender-mcp)](https://github.com/ahujasid/blender-mcp) — 25,2k estrelas, 2,4k forks, MIT, lista de features, requisitos.
- Busca agregada citando `blendermcp.org`, `blender-mcp.com`, `a2a-mcp.org` e Glama — confirmação cruzada de que é "o" MCP de Blender de referência, gratuito, compatível com Claude/Cursor/VSCode/Ollama.
- [Generate Images with Claude and Hugging Face — Hugging Face Blog](https://huggingface.co/blog/claude-and-mcp) — confirma créditos grátis via ZeroGPU Spaces, cobertura de imagem e vídeo, sem detalhar limite exato.
- [mcp-video-gen — GitHub (kevinten-ai)](https://github.com/kevinten-ai/mcp-video-gen) — CogVideoX listado como "free unlimited"; busca agregada sobre CogVideoX confirma modelo aberto real (Apache 2.0) mas qualidade irregular em uso real.
- [comfyui-mcp — GitHub (Peleke)](https://github.com/Peleke/comfyui-mcp) e demais implementações — confirma requisito de ComfyUI local + GPU.
- Busca sobre Vivideo MCP (`vivideo.ai/features/mcp`, Capterra) — confirma cobrança por crédito de uso, não gratuito contínuo.
- Busca sobre exportação Revit->FBX->Blender (ProtoTech Solutions, OSArch, RapidPipeline) — confirma exportador FBX gratuito via Twinmotion e limitação conhecida de material/textura na conversão.
- Pesquisado em 01/08/2026, mesma sessão dos achados de Twinmotion e Magnific, em resposta a pedido explícito de Claudemberg por opções gratuitas.

## Governança
Proposta pendente — Lúcio (Arquitetura) ainda não foi criado como Gestor; esta Skill fica arquivada para quando ele for aprovado e a equipe for formada. Não altera nenhuma Skill oficial hoje, e não autoriza instalação/uso real de nenhum conector — é registro de candidatos encontrados e verificados, sujeitos a teste técnico no momento do uso real (Princípio 3), inclusive a checagem ainda pendente de compatibilidade do Blender MCP com Claude Code especificamente. Sob o modelo de ratificação posterior (20/07/2026), a criação do Gestor Arquitetura e a ativação desta Skill passam a ser decisão do próprio Wallenberg quando o teste de contratação for aplicado — mas seguem sujeitas a ratificação na Reunião Semanal. Busca de render/vídeo/tour 360 **continua aberta**, incluindo a lacuna confirmada de novo hoje: nenhuma opção gratuita ou paga resolve tour 360 multi-ponto (ver `feedback_render_video_mcp_lucio`).
