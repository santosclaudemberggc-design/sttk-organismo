# Propostas do dia — 19/10/2026 (segunda)

Registro de Erros e Acertos, Passo 0.6 da Rotina Diária v3.6.0. Máximo de 3 propostas por dia, por ordem de impacto.
**Nenhuma destas soluções foi aplicada.** O campo `aprovacao` só é preenchido por Claudemberg.

## 1. E-2026-10-19-03 — Oscar marcou "Atende" sem imagem
- **Erro (1 frase):** Etapa 05 v2 (Estudo Preliminar no Revit) marcou "Atende" com elevação vazia, com todos os ids válidos; nota 6,30, reprovado.
- **Prova:** `CONSTRUCAO_DO_ZERO/01_CEO/Agentes_Diretos/Bardi (Examinador)/_estado_bardi.md`, linhas 10 e 101.
- **Gestor dono:** Lúcio (confirma ou substitui a solução).
- **Solução:** todo "Atende" de vista (planta, corte, elevação, folha) vem com a imagem exportada por `vitruvius_export_view_image` anexada. Sem imagem, escreve "não verificado visualmente".
- **Como será testada:** Bardi refaz a etapa 5 (ou um caso novo) e confere que nenhum "Atende" de vista está sem imagem. Esse teste vira `teste_de_regressao`.

## 2. E-2026-10-19-01 — Etapa 04 v3 omitiu a SMD e a herança da Etapa 01
- **Erro (1 frase):** a SMD foi omitida (reprovação automática) e a herança da Etapa 01 (TO 50%) sumiu sem aparecer como erro.
- **Prova:** `_estado_bardi.md`, linhas 16 e 112; `errata_gabarito_etapa_04_16-10.md`, item N-3.
- **Gestor dono:** Lúcio.
- **Solução:** toda etapa começa com a tabela "herança recebida" (cada número das etapas aprovadas, com origem). Lúcio só aceita a entrega se cada linha da tabela aparecer nas premissas. Registrar isso na Skill de critérios do Lúcio.
- **Como será testada:** Bardi confere se a etapa 4 refeita traz a herança 50% de TO e a SMD, linha por linha.

## 3. P-2026-10-19-04 — As 3 cópias de cada Skill dessincronizam
- **Problema (1 frase):** `.claude/skills`, `.agents/skills` e `Skills_Propostas` ficam com versões diferentes (espelho de levantamento na v1.1; Skill de vaga sem espelho).
- **Prova:** `_estado_bardi.md`, linhas 77, 88 e 138.
- **Dono:** Wallenberg (organismo).
- **Solução:** script de conferência em `_ferramentas/` que compara as 3 cópias de cada Skill e lista as diferentes. Roda no fim de toda rotina que mexer em Skill. Antes de construir, passa pela sabatina (regra de 18/10).
- **Como será testada:** o script deve listar as divergências já conhecidas hoje (`arquitetura-nbr9050-acessibilidade` e `legal-base-legislativa-bairro`) e não listar nenhuma cópia igual.
