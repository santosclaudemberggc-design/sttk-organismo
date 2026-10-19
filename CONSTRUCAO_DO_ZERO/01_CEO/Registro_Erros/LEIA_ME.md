# Registro de Erros e Acertos — como usar

Criado em 19/10/2026 por decisão de Claudemberg (sabatina de 18-19/10/2026). Arquivo de dados:
`registro.json`, nesta pasta. **Dono: Wallenberg.** Não confundir com `Pendencias/pendencias.json`
(pendência = falta fazer; erro = fizemos errado e por quê).

## Para que serve
1. Ver o padrão: quais Skills, ferramentas e Agentes erram mais.
2. Não repetir erro já corrigido: todo erro corrigido vira **acerto protegido**, com o teste que o prova.

## Quem escreve o quê
| Quem | Pode | Não pode |
|---|---|---|
| Claudemberg, Bardi, Gestores | criar linha (erro de entrega) | mudar status |
| Wallenberg | criar linha (erro de entrega ou problema do organismo), mudar status | registrar sem prova |
| Gestor dono do Agente | escrever `solucao_proposta` de erro de entrega | aprovar a própria solução |
| Wallenberg | escrever `solucao_proposta` de problema do organismo | aprovar a própria solução |
| Claudemberg | aprovar a solução (`aprovacao`) | — |

**Sem prova, não entra.** `prova` = arquivo + linha (ou commit, ou registro da rotina) onde o erro aparece.
Isso vale em dobro para o Wallenberg: rotina já escreveu "ratificado por Claudemberg" sem ter acontecido.

## Campos de cada linha
- `id`: `E-AAAA-MM-DD-NN` (erro de entrega) ou `P-AAAA-MM-DD-NN` (problema do organismo); a data é a do registro.
- `data_do_erro`, `apontado_por`, `tipo` (`erro_entrega` | `problema_organismo` | `acerto_de_primeira`)
- `agente`, `gestor_dono`, `skill_ou_ferramenta`
- `o_que_errou`, `causa`: `falta_skill` | `skill_errada` | `falta_ferramenta` | `ferramenta_falhou` | `instrucao_confusa`
- `prova`
- `solucao_proposta`: `{ texto, proposta_por, data }` — como resolver, de forma plausível e testável
- `aprovacao`: `{ por, data }` — só Claudemberg
- `prova_correcao`: o teste refeito (normalmente pelo Bardi) que passou
- `teste_de_regressao`: o teste que roda de novo sempre que a Skill/ferramenta/Agente mudar
- `status`: `aberto` → `em_correcao` → `corrigido` → `acerto_protegido`

## Ciclo
1. Alguém aponta, com prova → `aberto`.
2. Dono propõe a solução → Wallenberg leva para Claudemberg na Rotina Diária (**no máximo 3 propostas por dia**,
   por ordem de impacto) → aprovada → `em_correcao`.
3. Correção aplicada → Bardi refaz o teste que pegou o erro → passou → `corrigido`, com `prova_correcao`.
4. Wallenberg grava o `teste_de_regressao` → `acerto_protegido`.

## Acerto protegido (regra contra regressão)
Antes de mudar uma Skill, ferramenta ou Agente, quem muda procura aqui as linhas `acerto_protegido` daquele
item e roda de novo cada `teste_de_regressao`. **Se algum falhar, a mudança não entra.**

Entrega aprovada de primeira (por Claudemberg ou pelo Gate) também entra, como `acerto_de_primeira`, com a prova.

## Formato
JSON, para o painel e o futuro app de gestão lerem direto. Claudemberg lê pelo painel, não pelo arquivo.
A ligação com o painel e com o app fica para depois.
