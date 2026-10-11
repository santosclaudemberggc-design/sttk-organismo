# POP — Autonomia Contínua de Treino/Teste entre Gestores e Agentes

**Criado por Wallenberg em 27/07/2026.**

Define como qualquer Gestor autônomo (Autonomous) treina e testa continuamente seus agentes, sem esperar ordem explícita de Wallenberg. Padrão estabelecido com Kelsen e Hely; aplicável a qualquer novo Gestor/Agente que for criado no organismo.

---

## Princípio

**Autonomia contínua, não automática.** Um Gestor Autonomous não espera um cron ou uma ordem. Sempre que ele roda (por qualquer razão), verifica se há treino/teste pendente de seus agentes, e **executa de fato** — orquestra o agente, audita, registra. O teste é costurado dentro do trabalho, sempre.

---

## Estrutura Técnica

### 1. Notion Database: "Treinos e Testes"

**Local:** Workspace Notion Claudemberg / Organismo STTK

**Schema:**
- `Agente` (título): nome do agente a ser treinado
- `Gestor` (texto): nome do Gestor responsável pelo treino
- `Status` (select): pendente / em execução / aprovado / reprovado
- `Exame` (texto): tipo de exame (ex: "Formação→Shadow", "Shadow→Assisted", "Assisted→Autonomous")
- `Caso-teste` (texto): referência ao arquivo local (ex: `Casos_TESTE/Recreio/Benatti`)
- `Resultado` (texto longo): evidência do exame (iscas barradas, falhas, etc.)
- `Criado em` (data): quando o treino foi criado
- `Atualizado em` (data): quando foi revisado pela última vez

**Data source ID (para consultas Notion):** `collection://7b0728a8-fd57-419c-8a51-d5fe3794d165`

---

## Fluxo — Como Funciona

### Do lado do Gestor Autonomous (ex: Kelsen)

Quando você (Gestor) inicia uma execução:

1. **Ao nascer:** leia seu arquivo de estado (como sempre).

2. **Antes de qualquer outra ação:** consulte a Notion database "Treinos e Testes".
   - Filtre por `Gestor = seu nome` E `Status = pendente`
   - Se há resultado: há treino designado para você orquestrar

3. **Se há treino pendente:**
   - Mude o `Status` para "em execução" (você marca; diz ao Hely que está começando)
   - Abra o agente como subagente (`Agent, subagent_type: nome_do_agente`) com contexto completo:
     - Exame e critérios (leia da linha Notion)
     - Caso-teste (arquivo local, ex: `Casos_TESTE/Recreio/Benatti`)
     - Iscas plantadas (se for teste maldoso; veja `POP-FORMACAO-01`)
     - O que você espera de retorno (artefato + resultado)

4. **Agente executa:** retorna o artefato (arquivo `.md` do parecer, resultado, etc.)

5. **Você audita:** 
   - **Inspecione o artefato**, não leia o relatório do agente
   - Use `POP-FORMACAO-01` (exames de nível) como gabarito
   - Compare contra o caso-teste: o agente barrou as iscas? acertou com rigor?

6. **Você registra:**
   - **Seção 0 do arquivo de estado do agente:** escreva "REGISTRO DE EXAME" com veredito e evidência
   - **Notion database:** atualize a linha:
     - `Status = aprovado` (se passou) ou `Status = reprovado` (se reprovou)
     - `Resultado = [evidência concisa]` (ex: "5 iscas barradas", "falhou em isca 1: aceitou fonte vencida")
     - `Atualizado em = hoje`

7. **Você reporta a Wallenberg:** a auditoria entra no Registro Diário, como sempre.

---

### Do lado do Agente (ex: Hely)

Quando você (Agente) é acionado:

1. **Ao nascer:** leia seu arquivo de estado (como sempre).

2. **Logo depois:** consulte a Notion database "Treinos e Testes".
   - Filtre por `Agente = seu nome` E `Status = em execução` (o Gestor já mudou de "pendente" para "em execução" antes de acionar você)
   - Se houver resultado: há treino seu pendente agora

3. **Se há treino designado para você:**
   - Abra o arquivo de caso-teste (ex: `Casos_TESTE/Recreio/Benatti_TESTE/parecer_projeto_legal.md`)
   - Execute o exame com rigor — é igual a qualquer outro trabalho seu, mas sob supervisão de exame:
     - Leia o enunciado e as iscas
     - Processe e analise
     - Retorne o artefato (seu parecer, análise, resultado)
     - O Gestor audita (você não decide se passou ou não)

4. **Você atualiza seu arquivo de estado:** registre brevemente onde parou, qual foi o treino.

5. **Você reporta ao Gestor:** o artefato é o retorno — ele audita de verdade.

---

## Exemplo Prático: Kelsen Treina Hely

**Cenário:** Wallenberg cria uma linha na Notion: "Hely / Kelsen / pendente / Formação→Shadow / 1 caso real com resposta conhecida / vazio / 27/07/2026 / 27/07/2026"

**O que Kelsen faz:**
1. Roda por qualquer motivo (nova demanda, drenagem de fila, rotina, etc.)
2. Lê seu arquivo de estado
3. **Consulta Notion:** vê a linha acima (Status = pendente, Gestor = Kelsen)
4. Muda Status para "em execução"
5. Aciona Hely: `Agent, subagent_type: hely` com contexto: "Você vai fazer Exame 1, Formação→Shadow. Caso: Benatti (arquivo local). Resposta certa: reprova (CAM 400 < 720 pretendidos). Retorne sua recomendação e as fontes de cada afirmação."
6. Hely executa, retorna parecer
7. Kelsen **audita o artefato**, não o resumo: "Hely recomendou reprova? Citou as fontes? Acertou?"
8. **Se aprovado:** Kelsen escreve Seção 0 em _estado_hely.md ("Exame 1, 27/07, Caso Benatti, APROVADO, precisão confirmada, todas as fontes corretas"). Muda Notion: Status = "aprovado", Resultado = "Recomendação precisa, 3 fontes verificadas"
9. **Se reprovado:** Kelsen escreve Seção 0 com evidência da falha. Muda Notion: Status = "reprovado", Resultado = "Completou lacuna em vez de marcar pendência"
10. Reporta a Wallenberg no Registro Diário (como faria com qualquer auditoria)

---

## Para Novos Gestores/Agentes

Quando for criado um novo Gestor (ex: Lúcio, Arquitetura) ou novo Agente:

1. **Leia este POP.**
2. Crie uma fila de treinos usando **a mesma Notion database** — não precisa criar outra. As linhas compartilham espaço: Kelsen usa `Gestor = Kelsen`, Lúcio usa `Gestor = Lúcio`, etc.
3. **Arquivo de estado do Gestor:** adicione a mesma seção que Kelsen tem (consulta Notion, descrição do fluxo)
4. **Arquivo de estado do Agente:** adicione a mesma seção que Hely tem (consulta Notion antes de executar)
5. **Ferramenta Agent:** confirme que o Gestor tem `Agent` na lista de tools (ele precisa conseguir abrir seus agentes como subagentes)

---

## Regra Importante: Autonomia Não Substitui Claudemberg

A autonomia contínua de treino/teste **não substitui** a aprovação de Claudemberg. O que muda:

- **Antes (27/07):** Kelsen espera Wallenberg dizer "treine o Hely agora"
- **Depois (27/07+):** Kelsen verifica a Notion, vê que há treino pendente, executa sozinho

Mas a aprovação de **promoção de nível** é sempre de Claudemberg (via Wallenberg, na Reunião Semanal). O Gestor recomenda (escreve Seção 0 do agente com o veredito), Wallenberg leva à reunião, Claudemberg aprova ou nega — e **quando aprova**, ativa a Notion com o treino para o próximo nível.

---

## Referências

- `POP-FORMACAO-01_exames_de_nivel.md` — critérios de cada exame
- `kelsen.md` — implementação do padrão (exemplo real)
- `_estado_kelsen.md` — seção 1.5 e seção 1 (histórico)
- `_estado_hely.md` — seção 0.5 (treino)
- Notion Database "Treinos e Testes" — data source `collection://7b0728a8-fd57-419c-8a51-d5fe3794d165`

---

## Histórico de Decisões

- **13/07/2026:** Kelsen aprovado como Gestor Legal, Autonomous (escopo cliente)
- **22/07/2026:** Regra de ouro estendida a Gestores — autonomia com ratificação posterior
- **23/07/2026:** Hely promovido a Autonomous no escopo cliente; primeira drenagem de pendências executada
- **27/07/2026:** Notion database "Treinos e Testes" criada; padrão de autonomia contínua de treino/teste implementado; este POP criado

