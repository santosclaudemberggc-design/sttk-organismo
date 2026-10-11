---
name: skills-propostas-indice-2026-08
description: "Índice mensal das Skills propostas pela rotina diária do Wallenberg — Agosto/2026, alimenta a Reunião Mensal ao Conselho"
metadata:
  type: indice_mensal
  mes: Agosto
  ano: 2026
---

# Índice — Skills Propostas de Agosto/2026

Todas as entradas abaixo são **propostas**, produzidas pela rotina diária do Wallenberg (Funções 3 e 5). Nenhuma foi aprovada ainda — decisão de Claudemberg na Reunião Mensal ao Conselho (Princípio 13). Continuação do índice de [Julho/2026](../Julho/indice.md).

| Data | Skill | Gestor-alvo | Resumo | Fonte principal |
|---|---|---|---|---|
| 01/08/2026 | [Conector MCP de render/vídeo — ScanBIM Labs/Twinmotion via APS](arquitetura_mcp-render-video-twinmotion-scanbimlabs.md) | Lúcio (Arquitetura) — não implantado, futuro Agente de Renders/Vídeos | Primeiro candidato concreto da busca contínua determinada em 31/07: conector MCP real (GitHub verificado) liga Revit->Twinmotion, renderiza still 8K e exporta vídeo MP4/MOV/WebM — mas estágio comunitário/inicial, sem tour 360, não pronto para produção | PulseMCP, GitHub ScanBIM-Labs |

## Observações desta rodada (01/08/2026)
- Pesquisa cobriu: busca contínua de conectores MCP de render/vídeo/tour 360 para a equipe do Lúcio (instrução de 31/07/2026), tendências de escritórios internacionais com eixo reformulado (ferramenta nomeada, não conceito genérico — feedback de 31/07/2026: Gensler/BIG/Foster+Partners), precificação/honorários de escritórios de arquitetura no Brasil 2026, LICIN 2.0/SMDU, boletim CBIC de normas técnicas (jun/jul 2026), e revisão da ABNT NBR 5671 (participação dos intervenientes em obras).
- **Único achado que virou Skill:** conector MCP `twinmotion-mcp` da ScanBIM Labs — resolve parcialmente (render + vídeo, não tour 360) o gap identificado por Claudemberg em 31/07/2026. Verificado em 3 fontes independentes (PulseMCP, GitHub da organização, site oficial) antes de virar achado — Princípio 3. Explicitamente registrado como estágio comunitário/inicial, não recomendação de uso imediato.
- **Busca de tendências de escritórios reformulada, mas sem achado novo aproveitável:** aplicando o critério dos 6 eixos concretos (ferramenta nomeada, fluxo, entrega, posicionamento, precificação, IA nomeada — `feedback_tendencias_escritorios_mundo`), a busca sobre Gensler/BIG/Foster + Partners retornou só discurso institucional de alto nível ("IA como parceira de colaboração", "otimização de eficiência energética"), sem nome de ferramenta/modelo específico além do que já está coberto pela Skill de 16/07 (IA generativa — caso Gensler). **Descartado por ausência de nome de ferramenta verificável**, não por falta de tentativa — a pergunta já veio formulada nos termos corretos do feedback, mas a fonte não respondeu com o nível de detalhe pedido.
- **Achado sobre precificação de escritórios brasileiros, avaliado e não transformado em Skill:** confirmados os 4 modelos de cobrança usados no Brasil em 2026 (percentual da obra 3-8% padrão/até 15% projetos complexos, R$/m² R$60-140 residencial e R$80-180 interiores, hora técnica R$180-380, cobrança por etapa) e a referência à Tabela CAU/BR — mas é informação de mercado genérica (blogs/agregadores de preço), sem fonte primária (CAU/BR) nem processo específico de um escritório nomeado, e não há Gestor de Fechamento/Comercial implantado hoje a quem atribuir com precisão. Mesmo padrão de descarte de rodadas anteriores para conteúdo de mercado sem verificabilidade primária.
- **Achado avaliado e descartado por falta de conteúdo concreto:** revisão da ABNT NBR 5671:1990 (participação dos intervenientes em obras de engenharia/arquitetura) tinha prazo de consulta nacional até 08/07/2026 (já vencido hoje) segundo o boletim CBIC jun/jul — mas nenhuma fonte confirma o teor da revisão nem sua publicação; sem Gestor específico a quem atribuir hoje (toca RRT/ART de forma indireta, mas não é norma de licenciamento). Fica anotado para revisitar se a revisão for publicada e o teor mudar responsabilidade de interveniente de forma concreta.
- **Achados descartados por redundância (Princípio 15):** boletim CBIC jun/jul 2026 repete as 2 normas já descartadas em rodadas anteriores de julho (NBR 11702 tintas, ISO 19650-6 BIM, agora com prazo 05/08/2026); LICIN 2.0/SMDU sem decreto/LC novo além do já conhecido (Decreto 55.622/2025).
- **Continuidade obrigatória, não encerrada:** a busca de conector MCP de render/vídeo/tour 360 continua nas próximas rodadas — D5 Render, Enscape, Veras, Lumion e Matterport ainda não têm conector MCP localizado (ver `feedback_render_video_mcp_lucio`).
