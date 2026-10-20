# Propostas do dia — 20/10/2026 (terça)

Registro de Erros e Acertos, Passo 0.6 da Rotina Diária v3.5.0 (pipeline linear). Máximo de 3 propostas por dia, por ordem de impacto.
**Nenhuma destas soluções foi aplicada.** O campo `aprovacao` só é preenchido por Claudemberg.
Propostas de ontem (19/10) continuam aguardando decisão: E-2026-10-19-03, E-2026-10-19-01 e P-2026-10-19-04.

## 1. P-2026-10-19-05 — gabaritos lacrados dentro do repositório
- **Problema (1 frase):** a pasta `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi` está dentro da árvore do repositório, e o git rastreia 3 arquivos com "LACRADO" no nome (aparecem no `git status`, e o Oscar já viu o nome).
- **Prova verificada hoje:** `Test-Path` confirma a pasta em `CONSTRUCAO_DO_ZERO/_gabaritos_LACRADO_bardi` (12 arquivos dentro); `git ls-files` lista 3 caminhos com "LACRADO". Origem da queixa: `_estado_bardi.md`, linhas 74 e 83.
- **Dono:** Wallenberg (organismo).
- **Solução:** mover a pasta para fora do repositório (ex.: `D:\_gabaritos_LACRADO_bardi`) e atualizar o gancho de bloqueio e o estado do Bardi. Mexe na estrutura: passa pela sabatina antes de construir.
- **Como será testada:** `Glob` na raiz do repositório não lista nenhum nome de gabarito, e `git status` não mostra "LACRADO". Bardi confirma que o gancho ainda bloqueia leitura por subagente.

## 2. E-2026-10-19-02 — Skill de acessibilidade contradiz o habite-se
- **Erro (1 frase):** `arquitetura-nbr9050-acessibilidade` (v1.2) ainda diz nas linhas 20 e 90 que a NBR 9050 é exigida para habite-se, contra as linhas 15 e 21 e o COES Art. 31 V (unifamiliar dispensada).
- **Prova verificada hoje:** `Grep` em `.claude/skills/arquitetura-nbr9050-acessibilidade/SKILL.md` mostra o resíduo nas linhas 20 e 90.
- **Gestor dono:** Lúcio. **Lúcio confirmou a contradição e a solução (com ajuste) em 20/10** (subagente Lúcio, sem edição): corrigir as linhas 20 e 90 para valer só para tipologias não unifamiliares/bifamiliares, marcadas como pendentes de confirmação com Kelsen/Hely, e citar o COES Art. 31 V na linha 20.
- **Solução ajustada:** atualizar as cópias `.claude/skills` e `.agents/skills`. A cópia em `Skills_Propostas` não foi localizada por Glob hoje; confirmar o caminho antes de editar.
- **Como será testada:** Bardi faz duas perguntas: "casa unifamiliar precisa de acessibilidade para habite-se?" (caso dispensado) e "condomínio de casas precisa?" (caso não coberto pelo COES Art. 31 V lido na p. 17; alcance não confirmado no primário). Esta segunda pergunta é o teste de regressão proposto por Lúcio.

## 3. P-2026-10-19-02 — Bardi não confere hash nem conta palavras
- **Problema (1 frase):** o Bardi não tem shell; o lacre SHA256 não é recalculado e as contagens de palavras ficam "não medidas" nas correções.
- **Prova verificada hoje:** `_estado_bardi.md`, linha 10: "SHA256 NÃO recalculado (sem shell)".
- **Dono:** Wallenberg (organismo).
- **Solução:** script só de leitura em `_ferramentas/` (hash SHA256 e contagem de palavras), liberado ao Bardi por um comando único, sem shell aberto. Passa pela sabatina antes de construir.
- **Como será testada:** rodar o script num arquivo com hash conhecido e conferir o valor; Bardi registra o hash no parecer sem o marcador "não recalculado".

## Pesquisa de hoje (Passo 1) — registro para o Passo 0.6
- Lúcio: layout residencial em lote estreito (caso Yamada / SIAA). Tentativa de ler a fonte primária (PDF UFRGS) falhou por conexão (ECONNRESET). Sem proposta de nova versão, até a fonte ser lida. Bloqueio registrado, não resolvido.
