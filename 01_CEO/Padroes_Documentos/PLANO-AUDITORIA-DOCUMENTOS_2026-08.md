---
plano: PLANO-AUDITORIA-DOC-01
titulo: Auditoria completa dos documentos-base do organismo (Drive), por Wallenberg, com delegação por Gestor
autor: Wallenberg (CEO)
criado: 2026-08-08
status: RASCUNHO — para aprovação na Reunião Semanal de 10/08/2026, ainda não executado
origem: Diretriz de Claudemberg, 08/08/2026 — análise completa inicial feita pelo CEO Wallenberg, que depois delega adição/melhoria/exclusão a cada Gestor, registrando as pendências no Painel do Fundador e no Notion, com identificação do Gestor responsável em cada uma.
---

# Plano — Auditoria completa dos documentos-base do organismo

## 1. Objetivo
Antes de qualquer Gestor reescrever documentos autonomamente, Wallenberg faz **uma varredura completa, uma vez**, de todos os documentos-base do Drive por departamento — o que existe, o que serve, o que está desatualizado, o que falta. Só depois disso vira pendência delegada, Gestor por Gestor.

## 2. Escopo desta 1ª rodada
Documentos-base = templates/POPs/planilhas de controle/modelos que o organismo usa entre casos, **não** documentos de um caso real específico (esses continuam fora da fronteira desta auditoria, mesma regra de sempre).

Departamentos cobertos hoje: Legal (Kelsen) e Arquitetura (Lúcio) — os únicos com Gestor implantado. Complementares e Fechamento entram quando existirem.

## 3. Passo a passo
1. **Levantamento** — Wallenberg lista, por Gestor, todo documento no Drive que se enquadra como "base" (via `search_files`/`list_recent_files`, cruzando com o que cada Gestor já sabe que usa).
2. **Checagem de dado real** — cada documento passa pelo `PROTOCOLO-DADO-CLIENTE-EM-DOCUMENTO-BASE.md` antes de qualquer julgamento de conteúdo.
3. **Julgamento** — para cada documento, Wallenberg registra um veredito: **manter** (já serve, sem ação), **melhorar** (existe mas precisa ajuste — desatualizado, fora do padrão, incompleto), **criar** (falta um documento que deveria existir), ou **excluir/arquivar** (obsoleto, substituído, redundante — nunca exclusão permanente, mesma regra já usada para arquivos locais: mover para subpasta de arquivo).
4. **Registro da pendência** — cada veredito "melhorar/criar/excluir" vira um item em `pendencias.json` com `owner` = o Gestor da área, mais espelho no Painel do Fundador (via `sync_painel_pendencias.py`) e na nova base Notion **"Pendências de Documentos"** (campos: Documento, Gestor, Tipo de ação, Status, Link do Drive) — separada de "Treinos e Testes" para não alterar o filtro que a drenagem já usa.
5. **Delegação** — na rotina de drenagem contínua, cada Gestor passa a consultar também essa base nova (mesmo mecanismo do passo 2.5 já usado para `pendencias.json`) e executa o que estiver na própria alçada (`alc:"auto"`), seguindo o `PADRAO-DOC-POP_google-docs.md` quando o item for um POP.
6. **Auditoria de fechamento** — Wallenberg confere cada item concluído antes de marcar `resolvida`, mesmo modelo já usado para PDFs (conferência real, não só "Gestor disse que terminou").

## 4. O que este plano NÃO faz
- Não decide sozinho o conteúdo técnico de cada documento — isso é do Gestor da área.
- Não toca documento de caso real de cliente.
- Não cria a base Notio nem executa a varredura antes de aprovação de Claudemberg na Semanal — este arquivo é a proposta, não o registro de execução.

## 5. Dependências ainda em aberto
- Base Notion "Pendências de Documentos" ainda não existe — criar depende de ferramenta de escrita Notion (checar se já disponível, mesma classe de gap já resolvida para consulta em 07/08).
- `PADRAO-DOC-POP_google-docs.md` cobre só o tipo "POP" — outros tipos (Memorial, Planilha, Quadro de Áreas) precisam do próprio padrão antes de a auditoria julgar "fora do padrão" nesses tipos.
