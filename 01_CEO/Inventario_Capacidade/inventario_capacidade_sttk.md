# Inventário de Capacidade — Sistema Orgânico STTK

**Dono:** Wallenberg · **Criado:** 08/09/2026 (Item 5 da lista de melhorias do organismo)

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
| **`Agent` (spawn de subagente)** | Wallenberg→Gestor; Kelsen→Hely; Lúcio→Oscar; Cardozo→6 Agentes | ✅ cadeia Kelsen/Lúcio | 07-08/2026 | Kelsen→Hely e Lúcio→Oscar rodaram ponta a ponta. Cardozo tem `Agent` no frontmatter; cadeia Cardozo→6 Agentes ainda não exercida em caso real. |
| **WebSearch / WebFetch** | Kelsen, Lúcio, Cardozo | ✅ Gestores / ❌ 6 Agentes de Cardozo | 08-09/2026 | Gestores usam nas rotinas. Os 6 Agentes de Complementares (Baumgart et al.) **não têm** web tools nem Bash — trava fechamento autônomo de lacuna de fonte primária (achado 31/08, decisão pendente). |
| **`/watch:watch` (plugin)** | Wallenberg (Learning Agent, Passo 1) | ✅ | 09/2026 | Usado nas rotinas para assistir vídeo de verdade (download + transcrição). |
| **Vitruvius — MCP Revit (35 tools)** | Oscar | ⚠️ nunca em caso real | — | Presente na lista de tools. Nunca exercido num projeto real. Catálogo de achados/alternativas em `vitruvius_achados_candidatos.md`. |
| **Higgsfield — MCP imagem/vídeo** (`371ab963-…`) | Burle | ⚠️ conectado, pausado | 17/08/2026 | UUID na lista de tools. Geração real de render/vídeo do projeto **não validada**. Pausado por orçamento (Claudemberg). |
| **Claude in Chrome (extensão)** | Wallenberg, Kelsen | ⚠️ intermitente | 03/08/2026 | Leu Google Forms renderizado (família "Validação da Coordenação") — contorna mime `google-apps.form`. Frequentemente "indisponível na sessão automática". |
| **`md_to_pdf.py` / `gerar_prancha_legal.py`** | Kelsen/Hely, rotinas | ✅ | 07-08/2026 | Geração de PDF gêmeo e prancha legal A1 rodando; acentuação/latin-1 corrigidas. |
| **`medir_tokens.py` / `custo_por_agente.py`** | Wallenberg (Semanal, Passo 2.5) | ✅ | 03/09/2026 | Leem transcripts reais (128 sessões), geram `token_metrics.json` + `custo_por_agente.json`. |
| **Painel do Fundador (Artifact)** | Wallenberg | ✅ | 09/2026 | Republicação no mesmo `url` (`…/artifact/3c28ec0d-1817-4e7a-9a22-a4c16c570f27`) com `WebFetch` antes. |
| **Tarefas agendadas (`scheduled-tasks` MCP)** | Wallenberg | ✅ | 28/08/2026 | Drenagem registrada como cron `15 10 * * 1-5`, `enabled:true` confirmado. |

---

## Pendências de verificação (próxima janela)

- Vitruvius: primeiro uso em caso real (fica pronto quando houver projeto de Arquitetura ativo).
- Higgsfield/Burle: teste de render real quando orçamento reabrir.
- Cadeia Cardozo→6 Agentes: exercer em caso real (ligada ao Exame 2, 08–12/09).
- Web tools para os 6 Agentes de Complementares: decisão de Claudemberg (conceder read-only ou formalizar que Cardozo faz a pesquisa).
