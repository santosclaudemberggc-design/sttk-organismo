# Livro-Razão de Decisões Autônomas — Agosto/2026

Registro de tudo que o Wallenberg decidiu e executou **sem aprovação prévia** de Claudemberg, sob o modelo de ratificação posterior instituído em 20/07/2026 (ver regra de ouro no `CLAUDE.md`). Continuação de [Julho/2026](Julho.md).

**Para que serve:** é a pauta da Reunião Semanal. Claudemberg lê, ratifica ou manda desfazer — item por item. Decisão executada que não está aqui é falha de processo.

**Regra de preenchimento:** registrar no **mesmo dia** da execução. Nunca em lote no fim da semana — o objetivo é que Claudemberg possa intervir antes da segunda se algo estiver claramente errado.

---

### [2026-08-01] Rotina diária (Funções 3+5) — primeiro achado concreto da busca contínua de MCP de render/vídeo para Lúcio, abertura do mês

- **O que decidi:** rodar a pesquisa externa do dia priorizando a instrução de busca contínua de Claudemberg (31/07/2026 — conectores MCP de render/vídeo/tour 360 para a equipe do Lúcio) e a busca de tendências de escritórios reformulada com os 6 eixos concretos (mesma data — ferramenta/IA nomeada, não conceito genérico), além dos itens de rotina (LICIN 2.0/SMDU, boletim CBIC).
- **O que executei:** criei a proposta `arquitetura_mcp-render-video-twinmotion-scanbimlabs.md` — localizei e verifiquei em 3 fontes independentes (PulseMCP, GitHub da organização ScanBIM Labs, site oficial) um conector MCP real chamado `twinmotion-mcp`, que liga Revit a Twinmotion via Autodesk Platform Services e expõe 5 tools: importar modelo Revit, configurar clima/hora, renderizar still até 8K, exportar vídeo de passeio (MP4/MOV/WebM), listar cenas salvas. Registrei com honestidade o estágio real: classificado como servidor "comunidade" (não oficial) pelo diretório PulseMCP, popularidade baixa (#12.169 global), lançado em abril/2026, sem tour 360 confirmado. Não é solução pronta — é o primeiro candidato real encontrado para um gap que antes não tinha nenhum.
- **Por quê:** Gestor Arquitetura ainda não foi criado, então a Skill fica arquivada como proposta (mesmo tratamento das demais deste ano) — só as Skills do **Legal**, único Gestor implantado, são ativadas de fato. Função 3 (Cérebro) e Função 5 (Criador de Skills), em resposta direta a instrução registrada em `memory/feedback/feedback_render_video_mcp_lucio.md`.
- **Abri o mês:** este é o primeiro arquivo do livro-razão de Agosto/2026 (continuação de `Julho.md`) e a primeira pasta `01_CEO/Skills_Propostas/2026/Agosto/` com `indice.md` próprio (continuação do índice de Julho) — nenhum conteúdo de Julho foi apagado ou movido, é só a virada natural de mês.
- **Achado sobre tendências de escritórios, reformulado mas sem resultado aproveitável:** apliquei os 6 eixos concretos do feedback de 31/07 (ferramenta nomeada, fluxo, entrega, posicionamento, precificação, IA nomeada) nas buscas sobre Gensler/BIG/Foster + Partners — a pergunta veio formulada corretamente, mas as fontes só devolveram discurso institucional de alto nível, sem nome de ferramenta específico além do que a Skill de 16/07/2026 (caso Gensler) já cobre. **Descartado por ausência de nome de ferramenta verificável na fonte, não por busca malformulada** — diferença importante do erro de 31/07 que gerou o feedback.
- **Achado sobre precificação de escritórios brasileiros, avaliado e descartado:** confirmados os modelos de cobrança vigentes em 2026 (percentual 3-15%, R$/m², hora técnica, por etapa) mas é conteúdo de mercado agregado (blogs de preço), sem fonte primária CAU/BR nem escritório nomeado, e sem Gestor Comercial/Fechamento implantado a quem atribuir com precisão hoje.
- **Achado sobre ABNT NBR 5671 (participação de intervenientes em obras), avaliado e descartado:** prazo de consulta pública venceu em 08/07/2026 (já passado), mas nenhuma fonte confirma teor da revisão nem publicação — sem conteúdo concreto para virar Skill, e sem Gestor específico a quem atribuir hoje. Fica anotado no índice para revisitar se a revisão for publicada.
- **Achados descartados por redundância (Princípio 15):** boletim CBIC jun/jul 2026 repete as 2 normas já descartadas (NBR 11702 tintas, ISO 19650-6 BIM, agora com novo prazo 05/08/2026); LICIN 2.0/SMDU sem decreto/LC novo desde o já conhecido Decreto 55.622/2025.
- **Continuidade obrigatória, não encerrada:** a busca de MCP de render/vídeo/tour 360 continua — D5 Render, Enscape, Veras, Lumion e Matterport ainda não têm conector MCP localizado nesta rodada.
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_mcp-render-video-twinmotion-scanbimlabs.md` (+ PDF)
  - Criado: `01_CEO/Skills_Propostas/2026/Agosto/indice.md` (+ PDF)
  - Criado: este arquivo (`01_CEO/Decisoes_Autonomas/2026/Agosto.md`)
  - Painel do Fundador: **não alterado** — mesmo padrão de julho: só entrou Skill de Gestor não implantado (proposta arquivada), sem mudança de card/capacidade real do organismo hoje (Princípio 15).
- **Backup em:** não aplicável — nenhum arquivo pré-existente foi alterado hoje (todos os arquivos tocados são novos: nova pasta de mês, novo índice, nova Skill, novo livro-razão).
- **Como desfazer:** apagar a pasta `01_CEO/Skills_Propostas/2026/Agosto/` inteira e este arquivo `Agosto.md`.
- **Status:** Aguardando ratificação (sobe para a Semanal de 03/08/2026).

---

### [2026-08-01] Achado ao vivo trazido por Claudemberg — Magnific MCP (conector oficial), checagem de D5 Render/Veras/Matterport

- **O que aconteceu:** Claudemberg trouxe, na conversa, um post do Instagram (perfil "sobre.arq", conteúdo promocional de terceiro) mostrando o fluxo Claude + MCP + Google Drive + Magnific renderizando imagens automaticamente, e perguntou se dava para usar D5 Render no lugar do Twinmotion (achado da manhã), e se havia outros conectores MCP equivalentes para o organismo.
- **O que fiz:** (1) Verifiquei D5 Render antes de responder — não tentei alegar bloqueio sem checar (feedback [[feedback-verificar-ferramenta-antes-de-alegar-bloqueio]]): confirmei em 3 fontes (registro oficial MCP, PulseMCP/Glama/Smithery, GitHub oficial da D5 Renders) que **não existe conector MCP para D5 Render hoje** — só o plugin LiveSync, interativo, não automatizável por agente. (2) Não tratei o post do Instagram como fonte técnica — verifiquei a alegação do Magnific em 4 fontes próprias (docs.magnific.com, magnific.com/mcp, busca agregada, Scopeful sobre a mudança de cobrança de 2026) antes de registrar qualquer coisa (Princípio 3). Confirmado: **Magnific MCP é conector oficial de 1ª parte** (Freepik/Magnific), conecta ao Claude Code em 1 comando (`claude mcp add --transport http magnific https://mcp.magnific.com`), OAuth sem chave de API, 40+ tools (imagem, vídeo, TTS, 3D). (3) Também checei Veras (Evolve Lab, ferramenta de render mais citada do mercado de arquitetura) e Matterport (tour 360) — nenhum dos dois tem conector MCP encontrado em nenhuma fonte.
- **O que executei:** criei a segunda Skill do dia, `arquitetura_mcp-magnific-render-video-3d.md`, e atualizei `indice.md` de Agosto (nova linha da tabela + adendo documentando a checagem de D5 Render/Veras/Matterport, todos sem conector hoje).
- **Por quê:** mesma resposta à busca contínua de Claudemberg (31/07/2026) — o Magnific não substitui o Twinmotion, resolve uma entrada diferente (imagem 2D em vez de modelo BIM), e ambos ficam registrados como candidatos distintos para quando o Gestor Lúcio existir.
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_mcp-magnific-render-video-3d.md` (+ PDF)
  - Alterado: `01_CEO/Skills_Propostas/2026/Agosto/indice.md` (nova linha + adendo)
  - Alterado: este arquivo (`Agosto.md`, esta entrada)
  - Painel do Fundador: **não alterado** — mesmo padrão do dia, Skill de Gestor não implantado.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-08-01/indice_pre_magnific.md` e `Agosto_pre_magnific_entry.md` (antes desta edição).
- **Como desfazer:** apagar `arquitetura_mcp-magnific-render-video-3d.md` e `.pdf`; restaurar `indice.md` a partir do backup; remover esta entrada do `Agosto.md` a partir do backup `Agosto_pre_magnific_entry.md`.
- **Status:** Aguardando ratificação (sobe para a Semanal de 03/08/2026).

---

### [2026-08-01] Terceiro achado do dia — stack de MCPs gratuitos (Blender MCP + Hugging Face + CogVideoX), a pedido explícito de Claudemberg

- **O que aconteceu:** depois dos achados de Twinmotion (comunitário, camada gratuita limitada) e Magnific (oficial, mas pago), Claudemberg pediu explicitamente para focar em conectores **gratuitos** — um MCP que resolvesse tudo, ou vários que somados resolvessem, com o critério sendo custo zero, não freemium.
- **O que fiz:** busquei e verifiquei candidatos genuinamente gratuitos, não "trial de produto pago". Achado principal: **Blender MCP** (`ahujasid/blender-mcp`) — confirmei direto no GitHub 25.200 estrelas, 2.400 forks, licença MIT — o MCP de 3D mais adotado de toda a busca desta rotina, hoje. Cobre render, vídeo (animação) e panorama 360 via a API Python nativa do Blender (não são comandos dedicados, mas a capacidade existe). Complementei com Hugging Face MCP (oficial, créditos grátis via ZeroGPU) para o fluxo de imagem 2D->fotorrealista sem custo, e mcp-video-gen/CogVideoX para vídeo curto gratuito (qualidade irregular, uso só como rascunho). Avaliei e descartei ComfyUI MCP (grátis mas exige GPU local — fica anotado como opção futura) e Vivideo MCP (cobrança por crédito real, não atende ao critério de gratuito contínuo).
- **Limitação registrada com honestidade, não escondida:** nenhuma fonte confirma que o Blender MCP funciona com Claude Code especificamente (só cita Claude Desktop/Cursor/VSCode/OpenCode) — fica como item a testar, não como fato assumido. Também confirmei de novo que **tour 360 multi-ponto (tipo Matterport) não tem solução gratuita nem paga** até hoje — pedido de Claudemberg não muda esse resultado, é limitação real de mercado.
- **O que executei:** criei a terceira Skill do dia, `arquitetura_mcp-gratuitos-render-video-blender-huggingface.md`, e atualizei `indice.md` de Agosto (nova linha + observação da rodada).
- **Por quê:** resposta direta ao pedido ao vivo de Claudemberg, dentro da mesma busca contínua já registrada em `feedback_render_video_mcp_lucio` — três ângulos do mesmo gap no mesmo dia (comunitário/gratuito limitado, oficial/pago, e agora gratuito de verdade), todos arquivados como propostas distintas para quando o Gestor Lúcio existir.
- **O que foi criado/alterado:**
  - Criado: `01_CEO/Skills_Propostas/2026/Agosto/arquitetura_mcp-gratuitos-render-video-blender-huggingface.md` (+ PDF)
  - Alterado: `01_CEO/Skills_Propostas/2026/Agosto/indice.md` (nova linha + observação)
  - Alterado: este arquivo (`Agosto.md`, esta entrada)
  - Painel do Fundador: **não alterado** — mesmo padrão do dia, Skill de Gestor não implantado.
- **Backup em:** `01_CEO/Decisoes_Autonomas/_backups/2026-08-01/indice_pre_gratuitos.md` e `Agosto_pre_gratuitos_entry.md` (antes desta edição).
- **Como desfazer:** apagar `arquitetura_mcp-gratuitos-render-video-blender-huggingface.md` e `.pdf`; restaurar `indice.md` a partir do backup; remover esta entrada do `Agosto.md` a partir do backup `Agosto_pre_gratuitos_entry.md`.
- **Status:** Aguardando ratificação (sobe para a Semanal de 03/08/2026).

---
