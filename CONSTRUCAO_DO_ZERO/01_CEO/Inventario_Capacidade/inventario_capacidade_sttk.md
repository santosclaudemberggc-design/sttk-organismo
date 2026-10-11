# Inventário de Capacidade — Sistema Orgânico STTK

**Dono:** Wallenberg · **Criado:** 08/09/2026 (Item 5 da lista de melhorias do organismo) · **Revisado:** 09/10/2026 (análise do organismo — linhas marcadas [09/10])

## Para que serve

Fonte única do que o organismo **realmente tem** e **realmente funciona**. Existe porque o organismo repetidamente errou aqui: plugin marcado `enabled` sem instalação, ferramenta reportada ativa que nunca foi conectada, limitação alegada de memória que não era real.

## Regras

1. **Sem linha de "testado assim, nesta data" → a capacidade é tratada como INDISPONÍVEL.** Ninguém escreve "ativo" num relatório sem entrada aqui.
2. Uma linha só é atualizada quando a ferramenta é **testada de verdade** (rodou, com resultado observado) — não "deveria funcionar".
3. Verificação acontece em momento fixo: na Reunião Semanal/Quinzenal, ou quando um Agente esbarra numa dúvida de ferramenta. Não é auditoria mensal de tudo.
4. `⚠️` = presente mas nunca validado em uso real. `❌` = confirmado que NÃO faz. `✅` = testado funcionando, com data.

---

## Capacidades

| Capacidade | Quem usa | Estado | Última verificação real | Como foi testado |
|---|---|---|---|---|
| **Google Drive — conector MCP** (create / update / trash / search / read) | Wallenberg, Kelsen, Cardozo | ✅ | 08/09/2026 | Criou Google Doc novo + `trash_file` + `get_file_metadata` depois = "not found". Auth OAuth `santosclaudemberggc@gmail.com`. Não apaga em definitivo (trash ≠ delete). |
| **Google Drive — Service Account (Python SDK)** | Kelsen/Hely | ✅ editar / ❌ criar | 30/07/2026 | Editou POP-LEGAL-04 real (timestamp confirmado). Criar arquivo novo = 403 (sem quota). Deletar/trashear = 403 nesse caminho — usar o MCP acima. |
| **Notion — conector MCP** (query data sources, fetch) | Wallenberg, Kelsen, Cardozo | ✅ | 07/09/2026 | `notion-query-data-sources` na base "Treinos e Testes" (SQL direto), retorno OK. `notion-fetch` exige ID exato salvo no estado. |
| **`Agent` (spawn de subagente)** | Wallenberg→Gestor; Kelsen→Hely; Lúcio→Oscar; Villaça→Mascaró/Fiker; Cardozo→6 Agentes; Lelé | ✅ Kelsen, Lúcio, Villaça / ⚠️ Cardozo / ❌ Lelé | [09/10] 01–08/10/2026 | Kelsen→Hely, Villaça→Mascaró+Fiker e Lúcio→Oscar rodaram no Ensaio 003 (etapas 1–3). Cadeia Cardozo→6 Agentes nunca exercida depois de 12/09. **Lelé não tem Agente nenhum** — etapas 14–17 sem executor. |
| **WebSearch / WebFetch** | Gestores, Fiker, Mascaró, Bardi | ✅ Gestores, Fiker, Mascaró, Bardi / ⚠️ Hely / ❌ 6 Agentes de Cardozo | [09/10] 09/10/2026 (leitura dos `tools:`) | **Hely ganhou WebSearch + WebFetch em 09/10** (aplicado com autorização de Claudemberg, fora do modo automático). Ainda não usado numa tarefa real: vira ✅ no 1º uso com resultado. Os 6 Agentes de Cardozo continuam sem web. |
| **`/watch:watch` (plugin)** | Wallenberg (Learning Agent, Passo 1), Macetes | ⚠️ | [09/10] 08/10/2026 | YouTube bloqueou o motor local em 08/10; plugin trocado para o motor Gemini no mesmo dia. **Ainda não testado num vídeo do YouTube depois da troca.** Rotina Macetes pausada até esse teste. |
| **Vitruvius — MCP Revit (51 tools)** | Oscar | ✅ ligação / ✅ desenho básico (paredes, piso, porta, janelas, ambientes, folha) / ❌ cotas de parede e de ambiente (valor errado com "sucesso") / ⚠️ dentro de rotina agendada não testado | **[09/10, 2º teste, "Projeto2"]** Oscar desenhou casa 10×8 m: 6 paredes, 1 piso 80 m², 1 porta, 2 janelas (cada uma na parede certa), 3 ambientes (45,92 / 14,82 / 14,82 m²), folha TESTE-01 com a planta. Conferido por Wallenberg lendo o modelo direto. Cotas: só `dimension_facade` certa; `dimension_wall` pega jamba de porta ou dá 0; `dimension_room` mede paredes inteiras. Lacunas no `_estado_oscar.md`. · [09/10] 09/10/2026 — **teste de fumaça PASSOU (sessão ao vivo, Lúcio→Oscar):** `get_revit_status` → `get_levels` (3) → `create_level` TESTE_OSCAR 9,00 m (id 16746401) → `get_levels` (4) → `delete_element` 16746401 (totalRemovidos 1) → `get_levels` (3, mesmos ids). Conferido por Wallenberg com `get_levels` direto: OSSO 4265590, ACAB 389985, LAJE 3682174. Projeto de teste "Projeto1" não salvo. Diagnóstico original: | O servidor tem 51 tools validadas visualmente por Claudemberg (até 10/09). Mas: (1) o `tools:` do Oscar usa nomes antigos (`mcp__vitruvius__create_wall`) e o servidor expõe `mcp__vitruvius__vitruvius_create_wall` — **o Oscar não tem nenhuma tool que funcione**; 10 nomes da lista nem existem mais; (2) `~/.claude/settings.json` aponta o MCP para `D:\011_VITRUVIUS_V3\src\Server\mcp-server.js`, pasta que não existe (só o app desktop usa o caminho certo `D:\011_VITRUVIUS\MCP_Server\dist\index.js`). **[Resolvido 09/10 à noite]** Pela documentação oficial (code.claude.com/docs/en/desktop e /mcp), a aba Code e as tarefas agendadas locais leem o `claude_desktop_config.json`; `mcpServers` no `settings.json` não é fonte documentada. A chave foi removida do `settings.json` (cópia antes). Fonte única: `%APPDATA%\Claude\claude_desktop_config.json` → `D:\011_VITRUVIUS\MCP_Server\dist\index.js`. Plano: `D:\011_VITRUVIUS\PLANO_AGENTE_GUIADO.md`. |
| **Higgsfield — MCP imagem/vídeo** (`371ab963-…`) | Burle | ❌ na prática | [09/10] 01/09/2026 | Pausado por orçamento. Em 01/09 o Burle não conseguiu gerar render: faltam as tools de envio da imagem-base (`media_upload_widget`/`media_import_url`) e de recuperação (`show_generation_by_ids`). |
| **Bardi — gabarito lacrado** | Bardi, Wallenberg | ✅ por instrução | [09/10] 30/09–08/10/2026 | Gabarito em `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi/` (fora de `CONSTRUCAO_DO_ZERO/01_CEO`), SHA256 conferido antes/depois. O lacre é por regra, não por permissão: qualquer agente com `Read`/`Glob` conseguiria abrir. |
| **Claude in Chrome (extensão)** | Wallenberg, Kelsen | ⚠️ intermitente | 03/08/2026 | Leu Google Forms renderizado (família "Validação da Coordenação") — contorna mime `google-apps.form`. Frequentemente "indisponível na sessão automática". |
| **`md_to_pdf.py` / `gerar_prancha_legal.py`** | Kelsen/Hely, rotinas | ✅ | 07-08/2026 | Geração de PDF gêmeo e prancha legal A1 rodando; acentuação/latin-1 corrigidas. |
| **`medir_tokens.py` / `custo_por_agente.py`** | Wallenberg (Semanal, Passo 2.5) | ✅ | 03/09/2026 | Leem transcripts reais (128 sessões), geram `token_metrics.json` + `custo_por_agente.json`. |
| **Painel do Fundador (Artifact)** | Wallenberg | ✅ | 09/2026 | Republicação no mesmo `url` (`…/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`) com `WebFetch` antes. |
| **Tarefas agendadas (`scheduled-tasks` MCP)** | Wallenberg | ✅ | 28/08/2026 | Drenagem registrada como cron `15 10 * * 1-5`, `enabled:true` confirmado. |

---

## Pendências de verificação (próxima janela)

- [09/10] Vitruvius: Fase 0 do `PLANO_AGENTE_GUIADO.md` (consertar caminho do MCP + nomes no `tools:` do Oscar), depois 1º teste do Oscar desenhando.
- Higgsfield/Burle: teste de render real quando orçamento reabrir.
- Cadeia Cardozo→6 Agentes: exercer nas etapas 8–13 do Ensaio 003.
- [09/10] `/watch` motor Gemini: 1 vídeo do YouTube de verdade antes de religar a Rotina Macetes.
- Web tools para Hely (pedido desde 01/10) e para os 6 Agentes de Complementares: decisão de Claudemberg na Reunião de 12/10.
