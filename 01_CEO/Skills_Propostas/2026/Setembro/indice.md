# Índice — Skills Propostas Setembro 2026

**Status:** Ativo  
**Mês:** Setembro 2026  
**Atualização:** 03/09/2026

---

## Skills Criadas (Semana 01-05/09)

| Data | Título | Tipo | Para Quem | Status |
|------|--------|------|-----------|--------|
| 01/09 | NBR 15220-3:2024 — Reclassificação Bioclimática RJ (ZB 8 → ZB 4A) | Inteligência (Trilha A) | Tenreiro, Baumgart, Glaziou (cross-disciplina Complementares) | proposta |
| 01/09 | LC 281/2025 — Condições Especiais Licenciamento e Legalização RJ | Inteligência (Trilha A) | Kelsen/Hely (Legal) | proposta |
| 02/09 | NBR 9575:2024 — Impermeabilização: Seleção e Projeto | Inteligência (Trilha A) | Saturnino, Baumgart, Tenreiro (cross-disciplina Complementares) | proposta |
| 03/09 | Resolução SMDU Nº 10/2026 — Consulta Prévia de Diretrizes Territoriais e RDT | Inteligência (Trilha A) | Kelsen/Hely (Legal) + Lúcio/Oscar (Arquitetura) | proposta |
| 03/09 | NBR 15575:2025 — Desempenho Acústico de Sistemas de Pisos | Inteligência (Trilha A) | Baumgart, Saturnino, Tenreiro (cross-disciplina Complementares) | proposta |

---

## Estatísticas

- **Skills Propostas (semana atual):** 5 (Trilha A: 5, Trilha B: 0)
- **Skills Propostas (acumulado setembro):** 5
- **Skills Testadas:** 0
- **Cobertura Trilha A por Agente (desde agosto):**
  - Baumgart: 2 (NBR 6118:2026 + NBR 15220-3:2024 cross)
  - Saturnino: 2 (NBR 5626+8160 + NBR 9575:2024 cross)
  - Landell: 1 (NBR 5410)
  - Glaziou: 2 (NBR 16636-4 + NBR 15220-3:2024 cross)
  - Tenreiro: 2 (NBR 15575-4+8995-1 + NBR 15220-3:2024 cross)
  - Mindlin: 1 (NBR 6492:2021)
  - Kelsen/Hely: 3 (CAU-RJ 009/2026 + LC 281/2025 + Resolução SMDU 10/2026)
- **Achados Vitruvius:** +2 novos em 03/09 (BIMwright/rvt-mcp 229 tools + UV-Tech/revit-claude-mcp 40 tools — registrados em vitruvius_achados_candidatos.md). Total acumulado: 6 achados.
- **Próxima Prioridade:** (1) ~~NBR 9575:2024~~ CONCLUÍDA 02/09; (2) ~~NBR 15575:2025 pisos~~ CONCLUÍDA 03/09; (3) Apresentação interativa ao cliente (Portinari/Mindlin) — buscas 02-03/09 não encontraram ferramenta gratuita viável; (4) NBR 16280:2024 reformas (STTK = construção do zero, mas pode ser útil para Tenreiro em intervenções internas); (5) Passo 8 se lacuna real pedir

---

## Observações da Rodada 01/09/2026

1. **Pendência de 31/08 RESOLVIDA:** zoneamento bioclimático RJ confirmado como ZB 4A (era ZB 8). Impacto direto em CTpar ≥ 130 kJ/(m².K) para vedações.
2. **LC 281/2025 identificada:** lei de maio/2025 que altera LC 270/2024 (base LICIN 2.0) com condições especiais de legalização via contrapartida. Prazo para legalização (30/06/2026) já expirado — relevância para projetos em andamento que protocolaram antes.
3. **RevitMCPBridge2026 registrado:** 705+ endpoints, abordagem raw API (diferente do Vitruvius curado). Decisão: monitorar. Base de 113 arquivos como possível Skill de conhecimento.
4. **Descartados (Passo 1):** Leonardo AI, Runway ML, Midjourney, Finch 3D — freemium com limites, violam critério custo zero. Stable Diffusion + ControlNet e Dezgo são grátis mas já cobertos por Skills de render existentes (agosto).
5. **Não duplicados:** Blender MCP, Architecture MCP (404), NBR 5410, Demolinator (48 tools — já registrado e descartado em vitruvius_achados).

## Observações da Rodada 02/09/2026

1. **NBR 9575:2024 — Impermeabilização** criada (Trilha A). Cross-disciplina: Saturnino (principal — sistemas, arremate em tubulações, caimentos), Baumgart (juntas de dilatação, carga de cobertura), Tenreiro (compatibilização de revestimento em áreas molhadas). Resolve a 1ª prioridade listada na rodada anterior.
2. **NBR 15575 Emenda 1/2025 — dado novo confirmado:** Upar ≤ 2,7 W/(m².K) para paredes em ZB 4A (RJ). Light Steel Frame no RJ agora exige simulação computacional. Dado incorporado à Skill existente (01/09) — sem Skill nova, apenas complemento.
3. **Apresentação interativa ao cliente:** pesquisa rodou mas não encontrou ferramenta gratuita viável (MeuPasseioVirtual = trial limitado, Augment = SaaS, ARki = limitado). Nenhuma Skill criada (Princípio 15).
4. **Passo 8:** nenhum achado novo. Burle continua bloqueado por config (falta media_upload_widget), não por ferramenta inexistente. Portinari sem ferramenta gratuita de apresentação self-hosted. RevitCortex (173 tools) e revit-mcp-plugin (48 tools, Demolinator) já registrados — não duplicados.
5. **Descartados (Passo 1):** Luw.ai (cloud, watermark, sem MCP, viola critério 2 — vazamento de dados de projeto); CAU-RJ Deliberação 008/2026 ATHIS (habitação social, fora escopo STTK); DPOBR 0168-09/2026 (calendário eleitoral, informativo); NBR 16280:2024 (reformas, STTK = construção do zero).

---

## Observações da Rodada 03/09/2026

1. **Resolução SMDU 10/2026 — achado principal Legal:** nova resolução de 03/07/2026 que cria Consulta Prévia de Diretrizes Territoriais e RDT obrigatório antes de Licença de Obras para terrenos > 40.000 m², testada > 200m ou quadra com testada > 200m. Baseada na LC 270/2024 (LICIN 2.0). Impacto direto no fluxo Kelsen/Hely, embora projetos típicos STTK (lotes urbanos < 1.000 m²) geralmente não atinjam os limites.
2. **NBR 15575:2025 — desempenho acústico de pisos:** publicada dez/2024, vigente desde jun/2025. Principal novidade: critérios M/I/S agora obrigatórios para ambientes SEM dormitório (salas, cozinhas, banheiros). DnT,w ≥ 45 dB (mín.) e L'nT,w ≤ 80 dB (mín.) para pisos entre unidades sobrepostas. Cross-disciplina Baumgart/Saturnino/Tenreiro.
3. **Vitruvius achados +2:** BIMwright/rvt-mcp (229 tools, 166 commits, Apache-2.0, Revit 2022-2027) — candidato mais maduro e equilibrado; UV-Tech/revit-claude-mcp (40 tools, 5 commits, MIT, Revit 2026) — monitorar. Ambos registrados em vitruvius_achados_candidatos.md.
4. **Apresentação interativa ao cliente:** 3ª busca consecutiva sem ferramenta gratuita viável. BIMx = Archicad (pago), pCon.planner = só interiores/mobiliário, Unreal Engine = muito pesado para uso leve. Nenhuma Skill criada (Princípio 15).
5. **Render/vídeo:** nada novo. Remodel AI = cloud, Redraw = cloud, Leonardo.ai = cloud — todos violam critério 2. Stable Diffusion + Blender já cobertos.
6. **Descartados:** CAU-RJ Deliberações 002/003 (fora escopo direto STTK), DPOBR 0168-09/2026 (já descartado 02/09), NBR 16280:2024 reformas (STTK = construção do zero, monitorar).

---

**Próxima Atualização:** 04/09/2026 ou próxima rodada
