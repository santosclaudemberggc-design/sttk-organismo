# Kinocut MCP — Edição de Vídeo Local (Ferramenta)

## Para qual Gestor/Agente serve

**Lúcio (Arquitetura) → Burle** (pós-produção do render/vídeo gerado) e **Portinari** (montagem final da apresentação ao cliente). Preenche uma lacuna diferente da que o WAN 2.2 tentava resolver: WAN 2.2 era **geração** de vídeo (abandonado 03/09/2026 — GPU real, RTX 2060 SUPER 8GB, insuficiente); Kinocut é **edição/pós-produção** do vídeo já gerado (pelo D5 Render ou qualquer fonte) — corte, legenda, redimensionamento, upscale, versão vertical para redes sociais.

## Tipo

**Ferramenta (Trilha B)** — MCP server real, não conhecimento normativo.

## Status

ratificada — 03/09/2026, Claudemberg (rodada de auditoria com Wallenberg)

## O que a ferramenta faz

**Kinocut** (KyaniteLabs/mcp-video) é um servidor MCP "guardrailed" (com validação antes de cada operação) que dá a agentes de IA uma superfície de edição de vídeo local. Expõe **196 ferramentas MCP** e 167 comandos CLI, incluindo:

- **Edição core:** trim, merge, resize, crop, rotate, convert, subtitles (legendas)
- **IA:** ai_transcribe (transcrição automática), upscale, stem_separation (separação de áudio), scene_detection
- **Hyperframes:** init, render, website_capture, remove_background
- **Reparação/QA:** video_preflight, video_verdict, video_salvage (checagem de qualidade antes de entregar)
- **Fluxos:** workflow_validate, workflow_plan, workflow_render

## Evidência de segurança (Princípio 3)

- **Custo:** zero. Apache-2.0, open-source.
- **Vazamento de dado:** zero — roda 100% local (macOS/Linux/Windows), sem upload para nuvem, sem conta, sem API key. Só exige FFmpeg no PATH.
- **Idoneidade:** 136 stars, 32 forks, 1.362 commits na branch master, versão 1.15.1 publicada 31/08/2026, CI ativo (Forgejo + GitHub) — desenvolvimento maduro e contínuo, não projeto abandonado ou de fim de semana.
- **Sem exigência de GPU dedicada para as operações core** (edição via FFmpeg é majoritariamente CPU) — diferente do WAN 2.2 e do ComfyUI/Stable Diffusion local, que precisam de GPU forte e esbarrariam na mesma limitação de hardware (RTX 2060 SUPER 8GB) já confirmada nesta rodada.

## Por que interessa ao organismo agora

Depois do abandono do WAN 2.2 (limitação de GPU), o gap de "vídeo conceitual" do Burle não tem mais candidato de geração viável no hardware atual. Kinocut não gera vídeo do zero — mas **transforma o que o D5 Render já produz** (renders estáticos/sequências) em algo entregável de verdade: cortar, legendar, redimensionar pra formato vertical (redes sociais/apresentação mobile), verificar qualidade antes de mandar pro cliente. É um degrau de produção real que falta hoje entre "D5 gera o render" e "Portinari apresenta ao cliente".

## Limitações honestas

- Não gera vídeo — só edita o que já existe. Não substitui uma ferramenta de geração (D5 Render continua sendo a única fonte de imagem/vídeo em uso).
- Algumas funções de IA (upscale, scene_detection) podem exigir mais recursos que edição pura — não testado nesta rodada se rodam bem na GPU atual (RTX 2060 SUPER 8GB); recomendado testar com arquivo pequeno antes de assumir capacidade plena.
- Não clonado nem instalado nesta rodada — achado por leitura de README/documentação pública, seguindo o mesmo protocolo de segurança das demais Skills de ferramenta (nunca clonar/instalar sem aprovação).

## Ação proposta

Se aprovada: (1) Lúcio testa instalação local (FFmpeg + Kinocut) num ambiente de teste, com 1 arquivo de vídeo já existente (ex.: material do D5 Render do caso Daniel-OB); (2) confirmar quais das 196 tools rodam bem na GPU atual sem sobrecarga; (3) se confirmado, Burle passa a usar Kinocut como etapa de pós-produção antes de entregar a Portinari.

## Fontes
- [Kinocut (KyaniteLabs/mcp-video) — GitHub](https://github.com/KyaniteLabs/mcp-video) — verificado por WebFetch (README), 03/09/2026
- Achados relacionados descartados/deprioritizados nesta rodada por limitação de GPU (não repetir esforço): ComfyUI MCP (gist AndrewAltimit, 17 stars, exige "GPU poderosa"), sd-webui-mcp (boxi-rgb), comfyui-mcp (Peleke) — mesma classe de bloqueio do `lucio-wan22-burle-sem-shell`, RTX 2060 SUPER 8GB é insuficiente para geração local pesada.
- Upscayl (upscayl/upscayl) — grátis, maduro, mas SEM wrapper MCP encontrado nesta rodada; monitorar se surgir integração MCP.

## Governança
Proposta pendente — Wallenberg (Função 5), pesquisa de 03/09/2026, rotina de busca contínua de ferramentas de render/vídeo. Aguarda ratificação de Claudemberg antes de qualquer teste real.
