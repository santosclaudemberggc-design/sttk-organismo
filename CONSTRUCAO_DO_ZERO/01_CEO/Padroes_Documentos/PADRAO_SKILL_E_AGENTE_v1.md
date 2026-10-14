# Padrão de Skill e Agente — v1 (14/10/2026)

**Dono:** Wallenberg (função 5 — Criador de Skills), com ratificação de Claudemberg na Semanal.
**Aplica-se a:** toda Skill nova ou revisada (`.claude/skills/`) e todo Agente novo ou revisado (`.claude/agents/`).
**Status:** v1 — padrão proposto. Agentes e Skills já existentes migram aos poucos (seção 8), não de uma vez.

---

## 1. Por que os agentes erram (diagnóstico com evidência)

Lido em 14/10/2026: `_template_gestor.md`, `oscar.md`, `hely.md`, `oscar-revit-projetista-vitruvius/SKILL.md`, `CLAUDE_wallenberg_slice.md`.

| # | Causa | Evidência nos arquivos | Efeito |
|---|---|---|---|
| E1 | **Sem contrato de saída.** O agente não tem formato fixo de entrega nem campo obrigatório de prova. | `oscar.md`: checklist de 5 itens só foi criado **depois** da reprovação da Etapa 04 do Ensaio 003. | Entrega "pronta" sem prova; o erro só aparece no ensaio. |
| E2 | **"Atende" sem prova.** Afirmação de conformidade não vem com a saída da ferramenta colada. | `oscar-revit...SKILL.md` §0: "Três palavras proibidas sem prova"; D2/D3/D5 mostraram sucesso falso (`success:true` sem efeito). | Ferramenta mente com `success:true`; agente repete o relato. |
| E3 | **Regra escrita em prosa, não em passo verificável.** Regras ficam espalhadas em parágrafos longos. | `oscar.md` tem ~80 linhas de prosa antes da missão; `hely.md` tem ~115 linhas. | Regra importante fica soterrada; o agente não sabe qual passo é o gate. |
| E4 | **Contradição entre frontmatter e texto sobre ferramentas.** | `hely.md` frontmatter lista `WebSearch, WebFetch`; o texto (corrigido 01/10) diz que "não estão" na lista e manda usar `curl`. | O agente não sabe o que pode usar; tenta ferramenta inexistente ou deixa de pesquisar. |
| E5 | **Cópias desatualizadas do mesmo fato.** | `oscar.md` e `hely.md` ainda citam "Maurício" como validador em trechos que a decisão de 09/10 trocou para Claudemberg, com aviso no topo. | Duas versões da mesma regra no mesmo arquivo. |
| E6 | **Caminhos e nomes frágeis.** Pastas com acento e espaço, caminhos absolutos Windows, MCP com UUID. | Estado do Oscar em `Lúcio (Arquitetura)\Agentes\Oscar\`; MCP `mcp__014dedc9-...__search_files`. | Erro de "arquivo não encontrado" ao nascer; tool não encontrada. |
| E7 | **Ferramenta falha sem protocolo.** | Oscar: "Quando uma ferramenta falhar: cole o erro exato". Mas não há passo de *pré-checagem* (`get_revit_status`) nem parada obrigatória. | Agente simula desenho quando o plugin está desconectado. |
| E8 | **Sem teste antes de produzir.** Agente vai para caso real sem exame de regressão. | Oscar foi nomeado 07/08 e promovido por exames; o teste de leitura de 14/10 achou defeitos que a skill já deveria cobrir. | Defeito de ferramenta chega ao cliente. |

**Padrão de causa:** o agente não erra por falta de instrução; erra porque a instrução não tem **saída definida, gate verificável e prova obrigatória**. Cada erro virou um item novo no checklist depois do fato. O padrão v1 coloca esses três elementos antes do primeiro erro, não depois.

---

## 2. O que as melhores práticas dizem (fontes)

- Anthropic, *Skill authoring best practices* — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
  - SKILL.md com **menos de 500 linhas**; detalhe em arquivos separados, **referenciados a partir do SKILL.md, um nível só** (nada de referência dentro de referência).
  - `description` na **terceira pessoa**, dizendo **o que faz e quando usar**; máximo 1.024 caracteres.
  - Referências longas (>100 linhas) com **sumário** no topo.
  - **Checklist copiável** para fluxos de várias etapas, com passo de validação e "volte ao passo X se falhar".
  - **Ciclo validar → corrigir → repetir**, com validador explícito.
  - Scripts para tarefas determinísticas; erro tratado no script, não deixado para o modelo; caminhos com barra `/`.
  - Grau de liberdade conforme fragilidade: passo frágil = instrução exata; caso aberto = orientação.
  - **Avaliação antes da documentação**: no mínimo 3 cenários de teste, com linha de base sem a skill.
- Anthropic, `anthropics/skills` — repositório com `template/template-skill/SKILL.md` (frontmatter `name` + `description`, corpo em markdown). Padrão mínimo: uma pasta por skill.
- Skill-creator (skill local da casa) — ciclo rascunho → teste com e sem skill → avaliação com corrigido/aprovado → melhoria → repetir; regra de "explique o porquê, não grite MUSTs".

Pesquisa de skills de terceiros via `gh search` não foi possível nesta sessão (o `gh` não está instalado no ambiente Bash). Fica pendente como item de pesquisa.

---

## 3. Formato da SKILL.md (v1)

```
.claude/skills/<nome-em-gerundio-ou-substantivo>/
├── SKILL.md            (obrigatório, < 300 linhas de preferência, máximo 500)
├── references/         (docs carregados sob demanda, um nível só)
├── scripts/            (executados, não lidos; erro tratado dentro)
└── evals/evals.json    (casos de teste: entrada, saída esperada, asserções)
```

**Frontmatter**
```yaml
---
name: oscar-revit-projetista-vitruvius      # minúsculas, hífen, ≤ 64 caracteres
description: <terceira pessoa> <o que faz>. Use SEMPRE que <gatilhos concretos: verbos, ferramentas, pedidos reais>.   # ≤ 1.024 caracteres
version: vX.Y
status: ativa | rascunho | aposentada
dona: <Gestor>
data: AAAA-MM-DD
fontes: <documentos de origem, com caminho>
---
```

**Corpo, nesta ordem**
1. **Regra mãe** em uma frase (o que nunca pode faltar).
2. **Gate de entrada** — o que precisa estar verdadeiro antes de começar (ex.: plugin conectado, arquivo certo).
3. **Passos numerados**, cada um com coluna "Confira" ou "Prova" (saída que deve ser colada).
4. **Tabela de defeitos/exceções conhecidos** com contorno.
5. **Formato de saída** (template fixo, ver seção 4).
6. **Checklist final** marcado com prova.
7. **Relação com outras Skills** (complementa / difere / substitui — nunca contradiz).

**Escrita**
- Imperativo. Terceira pessoa na descrição.
- Explique o porquê de cada regra em uma frase. Evite CAPS e MUST sem razão.
- Um termo para cada coisa em todo o arquivo.
- Sem data relativa ("até agosto"); histórico vai em "Fontes" ou "Changelog".
- Caminhos com `/`. Nome de ferramenta MCP com prefixo do servidor (`vitruvius:get_levels`), não UUID.

---

## 4. Formato do Agente (v1)

Arquivo `.claude/agents/<nome>.md`. **Máximo ~150 linhas.** Regra e detalhe ficam em Skills; o agente aponta, não copia.

```markdown
---
name: <nome>
description: <Papel> do Sistema Orgânico STTK. Use quando <gatilho>. Não usar para <fora de escopo> — redirecionar para <dono>.
tools: <lista exata; só o que o agente de fato chama>
model: <opcional>
---

# <Nome> — <Papel> (equipe de <Gestor>)

## 1. Missão (3 linhas)
O que entrega, para quem, e o que NÃO faz.

## 2. Ao nascer
1. Ler `<caminho do estado>` (seção 1 e 2 apenas).
2. Ler a Skill `<nome>` antes de qualquer passo.
3. Conferir ferramentas: se a ferramenta exigida não responder, PARAR e reportar o erro colado.

## 3. Fluxo
Checklist copiável. Cada passo: ação → prova.
- [ ] 1. <ação> → prova: <saída colada>
- [ ] 2. ...
Falha em qualquer passo: parar, colar o erro exato, reportar ao <chefe>. Nunca "deu erro" sem o texto.

## 4. Autoridade
- Decide sozinho: <lista>
- Sinaliza ao chefe antes: <lista>
- Nunca: <lista>

## 5. Formato de entrega (obrigatório)
```
## Entrega — <assunto>
Status: PRONTO | PARCIAL | NÃO FEITO
Passos: [1 ✓ prova] [2 ✗ motivo]
Pendências: ...
Lacunas declaradas: ...
Provas anexas: ...
```
Sem este bloco, a entrega não é válida.

## 6. Ao morrer
Atualizar `<estado>` (substituir, não acumular) antes de devolver.
```

**Regras de agente (resumo)**
1. Uma Skill por função. A regra vive na Skill; o agente só chama.
2. Ferramentas: a lista do frontmatter é a verdade. Se o texto citar ferramenta fora dela, o texto está errado — corrigir.
3. Todo "atende/conferido/pronto" traz a prova colada.
4. Ferramenta com `success:true` não é prova. Prova é a releitura ou a imagem.
5. Versão única de cada regra no arquivo. Ao mudar uma decisão, substituir o trecho antigo (não deixar aviso ao lado).
6. Nome fixo para pastas e estados; sem acento em caminho que o agente precisa abrir (usar o caminho que já existe, copiado do Explorer).

---

## 5. Checklist antes de publicar Skill ou Agente

**Skill**
- [ ] Descrição diz o que faz **e** quando usar, com gatilhos concretos (≤ 1.024 caracteres)
- [ ] SKILL.md < 500 linhas; detalhe em `references/`, um nível só
- [ ] Regra mãe e gate de entrada no topo
- [ ] Cada passo com prova
- [ ] Formato de saída fixo
- [ ] Tabela de defeitos com contorno (se há ferramenta externa)
- [ ] Caminhos com `/`; MCP com prefixo do servidor
- [ ] Pelo menos 3 casos de teste em `evals/evals.json` (com e sem a skill)
- [ ] Testado com o modelo que vai executar (Haiku e Sonnet, se o agente rodar nos dois)

**Agente**
- [ ] Frontmatter `tools` = lista real; nenhum texto cita ferramenta fora dela
- [ ] Missão em 3 linhas; sem regra duplicada do slice ou da Skill
- [ ] Fluxo em checklist com prova
- [ ] Bloco de formato de entrega
- [ ] Caminho de estado existe e está escrito como no Explorer
- [ ] Sem "Maurício" onde a decisão atual é Claudemberg (ou qualquer nome superado)
- [ ] Backup em `Decisoes_Autonomas/_backups/AAAA-MM-DD/` e linha no livro-razão do mês

---

## 6. Como testar (ciclo da skill-creator, enxuto)

1. Escolher 3 tarefas reais do agente. Rodar **sem** a Skill nova (linha de base) e **com** ela.
2. Comparar: passos com prova, falhas, "atende" sem prova.
3. Anotar cada falha como: regra faltando / regra escondida / ferramenta errada / prova ausente.
4. Corrigir a Skill (não o agente) e repetir.
5. Só levar à Semanal quando as 3 tarefas passarem com prova.

---

## 7. Achado em aberto (decisão de Kelsen)

`hely.md`: frontmatter com `WebSearch, WebFetch`; texto dizendo que não estão. **Não alterei a lista de ferramentas** — quem confirma o que o runtime carrega é Kelsen, e o backup está em `_backups/2026-10-14/hely_agent_ANTES_padrao_v2.md`.

---

## 8. Plano de aplicação

| Ordem | O que | Quem | Quando |
|---|---|---|---|
| 1 | Confirmar tools do Hely (E4) | Kelsen | próxima rotina |
| 2 | Piloto: `oscar-revit-projetista-vitruvius` — criar `evals/evals.json` com 3 casos e medir | Lúcio + Wallenberg | até 21/10 |
| 3 | Reduzir os 4 Gestores (Kelsen, Lúcio, Cardozo, Lelé) ao formato da seção 4, sem mudar regra | cada Gestor, com backup | depois do piloto |
| 4 | Revisar Skills com mais de 500 linhas ou sem prova | Wallenberg | rotina de sexta |
| 5 | Pesquisa de skills de terceiros via `gh` (instalar `gh` no ambiente) | Wallenberg | pendente |

---

## Changelog
- v1 (14/10/2026, Wallenberg): criação. Diagnóstico E1–E8 a partir de `oscar.md`, `hely.md`, `_template_gestor.md` e `oscar-revit-projetista-vitruvius/SKILL.md`.
