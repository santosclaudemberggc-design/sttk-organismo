---
name: criando-skills-sttk
description: Padrão de construção e de revisão de Skills do organismo STTK — cabeçalho obrigatório, nome curto, descrição em terceira pessoa com o que faz e quando usar, corpo com até 500 linhas, detalhes em references/, casos de uso com quando usar e quando não usar, e 3 avaliações em evals/ com gabarito escrito antes e nota dada pelo Bardi. Use sempre que Wallenberg, um Gestor ou um Agente for criar Skill nova, revisar ou consertar Skill existente, ou conferir se uma Skill está bem construída, mesmo que o pedido só diga "nova skill", "melhorar a skill", "padronizar" ou "skill quebrada".
version: v1.0
status: proposta-em-treino
data: 2026-10-30
origem: "Sabatina Wallenberg × Claudemberg, 28 a 30/10/2026: auditoria achou 4 Skills sem cabeçalho ou sem descrição, 3 nomes acima de 64 caracteres, nenhuma Skill com avaliações e nenhum Agente pré-carregando Skills. Padrão baseado nas boas práticas oficiais da Anthropic para Skills."
dono: Wallenberg
---

# Padrão de Skill STTK

Toda Skill nova segue este padrão. Toda Skill revisada é ajustada a ele.
Uma Skill só passa a valer depois do treino em caso fictício e do sim de Claudemberg.

## 1. Pasta

```
.claude/skills/<nome>/
  SKILL.md          ← obrigatório, até 500 linhas
  references/       ← tabelas, fontes longas, exemplos (um nível só a partir do SKILL.md)
  evals/            ← 3 casos fictícios, só o enunciado (obrigatório; gabarito lacrado, ver seção 4)
```

`.claude/skills` é a única original. A cópia em `.agents/skills` é refeita por script; nunca edite a cópia.

## 2. Cabeçalho (frontmatter)

| Campo | Regra |
|---|---|
| `name` | só minúsculas, números e hífen; até 64 caracteres; igual ao nome da pasta |
| `description` | terceira pessoa; diz **o que faz** e **quando usar**, com as palavras que o pedido costuma trazer; até 1024 caracteres |
| `version`, `status`, `data` | `status`: proposta-em-treino → vigente (só com o sim de Claudemberg) |
| `origem` | quem decidiu e quando (sabatina, erro, ensaio) |
| `dono` | Gestor dono; Agente principal |

Sem cabeçalho ou sem `description`, a Skill não é encontrada pelo agente. É erro grave.

## 3. Corpo

1. **Por que existe** — o problema real, com data.
2. **Lei antes** — que Skill legal vem antes; esta não repete lei, aponta.
3. **Passos** — numerados, na ordem em que o agente trabalha.
4. **Casos de uso** — cada regra escrita assim:
   - **Regra:** o que fazer.
   - **Quando usar:** o perfil ou a condição.
   - **Quando não usar:** a exceção.
   - **Força:** obrigatória, padrão, opção comparada ou meta (com justificativa quando não cumprir).
5. **Conferência** — checklist "faz, confere, corrige, repete".
6. **Erros já cometidos** — tabela data, erro, regra.
7. **Fontes** — com documento, artigo ou página. Norma vence fonte genérica; termo do Rio vence termo nacional.

Regras de escrita: português simples, um termo por coisa (não trocar sinônimos), nada que envelheça no texto principal (datas de vigência vão em `references/`), ferramenta MCP citada pelo nome completo, número sem fonte marcado "interpretação — Gate".

## 4. Avaliações (evals/)

- 3 casos fictícios diferentes, cada um com **gabarito escrito antes** da execução.
- Em `evals/` fica só o enunciado. O gabarito fica lacrado em `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi/skills/<nome-da-skill>/` (regra do Bardi de 06/10/2026). Nunca descreva em `evals/` o que o caso testa.
- O Bardi monta os casos, corrige e dá a nota (mínimo 8,00).
- Claudemberg faz a avaliação visual e dá a aprovação final.
- Reprovou: o Gestor dono corrige a Skill e o Agente refaz.

## 5. Ligar ao agente

O Agente principal recebe a Skill no campo `skills:` do seu arquivo em `.claude/agents/`, para já começar com ela carregada.

## 6. Checklist antes de entregar

- [ ] Nome ≤ 64, igual à pasta
- [ ] Descrição em 3ª pessoa, o que faz + quando usar
- [ ] SKILL.md ≤ 500 linhas
- [ ] Regras como casos de uso, com força definida
- [ ] Não contradiz outra Skill (complementa, difere ou substitui, escrito)
- [ ] 3 avaliações com gabarito
- [ ] Pré-carregada no Agente principal
- [ ] Sim de Claudemberg registrado
