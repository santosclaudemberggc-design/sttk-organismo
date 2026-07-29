---
name: sttickler-fluxograma-oficial
description: Como ler o fluxograma oficial de execução de projetos da Sttickler (PDF/Figma) — legenda de cores e o que cada uma linka
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9b871edb-c4ae-4f0d-86fe-beca2ea0c055
---

# Fluxograma Oficial de Execução dos Projetos — Sttickler

**Fonte:** `DP - FLUXOGRAMA DE EXECUÇÃO DOS PROJETOS` (originado no Figma, exportado como PDF, salvo em `C:\Users\santo\Downloads\DP - FLUXOGRAMA DE EXECUÇÃO DOS PROJETOS.pdf`). É o fluxograma que a empresa já usa hoje, confirmado pelo usuário — é a referência que o CEO Wallenberg usa pra auditar se a equipe de agentes de cada Gestor faz sentido (ver função 4 "Organizador" em [[sttickler_ceo_wallenberg]]).

## Legenda de cores (cada etapa tem os 3 blocos, sempre)
- 🟡 **Amarelo** = "Desenvolvimento do X" → linkado ao **POP** (Procedimento Operacional Padrão) daquela etapa.
- 🟢 **Verde** = "X Desenvolvido" → linkado ao **Formulário de Validação da Coordenação** (Google Forms, interno).
- 🔵 **Azul** = "X Desenvolvido" → linkado ao **Formulário de Aprovação do Cliente** (Google Forms, externo).

**Importante:** essa é a leitura correta confirmada pelo usuário. Uma leitura anterior (de que Hidrossanitário/Paisagismo seriam etapas terceirizadas por causa da cor amarela) estava **errada** — amarelo é universal em toda etapa, é sempre o bloco de execução linkado ao POP, não um marcador de terceirização.

## Estrutura do fluxo (corrigida em 13/07/2026)
Sequencial em Arquitetura (Levantamento → Briefing → Estudo Preliminar → Anteprojeto) → bifurca em duas linhas paralelas e **independentes**:
- **Projeto Legal** (Kelsen) → protocolado na prefeitura → se aprovado, segue direto pra fila de espera de **Liberação de Obra (Gate 16)**, já com o Habite-se; se recusado/precisa de ajuste, as alterações são feitas e reenviado à prefeitura (laço iterativo até aprovar). **Não passa por Compatibilização** — Compatibilização é checagem de interferência entre modelos técnicos, e Legal não tem modelo, é aprovação documental.
- **6 Complementares** (Estrutural, Elétrico, Automação, Interiores, Hidrossanitário, Paisagismo) → convergem em Compatibilização → Projeto Executivo → Orçamento Executivo e Premissas → também alimentam Liberação de Obra.

As duas linhas se encontram só no Gate 16 (Liberação de Obra) — Legal contribui a documentação/Habite-se, os Complementares contribuem o Projeto Executivo compatibilizado. Confirmado por Claudemberg em 13/07/2026, corrigindo a leitura anterior desta memória (que colocava Legal dentro da convergência de Compatibilização).

Cada etapa = 3 documentos reais linkados (POP + form coordenação + form cliente), o que bate exatamente com o inventário de 37 formulários (14 Validação Coordenação + 14 Aprovação Cliente + 9 Briefing) descrito nos .md mestres — ver [[sttickler_visao_geral]].
