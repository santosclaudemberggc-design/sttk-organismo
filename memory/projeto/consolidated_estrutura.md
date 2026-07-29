---
name: consolidated-estrutura
description: "Estrutura STTK — Gestores (Kelsen aprovado), Agentes, Arquivo de Estado, Reuniões, Modelo Leilão, Fluxo (Autônomo vs. Determinístico)"
metadata: 
  node_type: memory
  type: project
  scope: "Implantação, Governança Operacional"
  updated: 2026-07-27
  originSessionId: 5bb7d99f-8636-4ada-948a-86139f91b2df
  modified: 2026-07-27T18:51:02.139Z
---

# Sistema STTK — Estrutura Consolidada

## Status Atual (27/07/2026)

**Wallenberg:** Ativo (esta conversa)  
**Kelsen (Legal):** Aprovado 13/07/2026  
**Hely (Executor Legal):** Ativo, Nivel Assisted  
**Lúcio (Arquitetura):** Novo agente disponível (27/07)  
**Complementares, Fechamento:** Planejado

---

## Hierarquia Completa

```
CLAUDEMBERG (Decisão final)
    ↓↑
WALLENBERG (CEO)
    │
    ├── KELSEN (Gestor Legal) ✅ 13/07/2026
    │    └── HELY (Executor)
    │         └─ Nível: Assisted (cria ação, Kelsen aprova)
    │         └─ Capacidade: LICIN 2.0, Compilação Prancha, Pesquisa Legislação
    │         └─ Acesso: Drive Legal, RIU API, md_to_pdf.py, gerar_prancha_legal.py
    │         └─ Arquivo de Estado: _estado_hely.md (4 seções)
    │
    ├── LÚCIO (Gestor Arquitetura) 🆕 27/07/2026
    │    └── Agentes (futuros)
    │         └─ Dependência: Consulta base legislativa de Kelsen antes de Levantamento
    │
    ├── ??? (Gestor Complementares) ⏳
    │    └── Agentes (futuros)
    │         └─ Coordenam: Estrutural, Elétrico, Hidro, Automação, Paisagismo
    │
    ├── ??? (Gestor Fechamento) ⏳
    │    └── Agentes (futuros)
    │         └─ Coordenam: Orçamento, Cronograma, Pós-venda
    │
    ├── Agente da Proposta (direto a Wallenberg) ⏳
    │    └─ Função: Leilão de preços + Certificação de parceiros
    │    └─ Acesso: Figma Canvas (MCP), Google Drive Propostas
    │
    └── Agente de Mentoria (direto a Wallenberg) ⏳
         └─ Função: Feedback de Maurício Costa → Skills do organismo
         └─ Acesso: Conversa externa, reprocessamento em Skills
```

---

## Kelsen (Gestor Legal) — Aprovado 13/07/2026

**Identidade:**
- **Nome:** Hans Kelsen (jurista, Teoria Pura do Direito, hierarquia normativa)
- **Papel:** Retentor de conhecimento legislativo + Decisor de conformidade
- **Princípios:** 18 (Ética/Conformidade), 8 (Rastreabilidade), 9 (Padronização)

**Conhecimento:**
- Base legislativa municipal **por bairro/sub-prefeitura** (não genérica)
- POPs/Memoriais da pasta "Legal" (Drive 001_MATERIAL)
- Pesquisa externa curada por Wallenberg
- Fornece Skill cross-Gestor obrigatória: Arquitetura consulta antes de Levantamento

**Capacidade:**
- Produz de verdade (um dos 3 com Agente Executor real, junto de Interiores e Compatibilização)
- ART/RRT coberto pelo CAU de Claudemberg (a partir de 2026)

**Equipe:**
- **Hely** (Executor do Projeto Legal) — Único agente, nível Assisted

**Arquivo de Estado:**  
`01_CEO\Gestores\Kelsen (Legal)\_estado_kelsen.md` (4 seções fixas)

**Autoridade:**
- Autônomo em decisões internas (criar/alterar POP, método de trabalho)
- Contrata seus próprios Agentes (aplica teste, informa Wallenberg, vai pra Mensal)
- Contínuo: sinaliza a Wallenberg tudo que exige julgamento estrutural

---

## Hely (Executor do Projeto Legal) — Assisted

**Identidade:**
- **Nome:** Hely Lopes Meirelles (jurista, Direito Administrativo e Municipal)
- **Papel:** Executa o processo LICIN 2.0, mantém base legislativa, compila prancha
- **Nível:** Assisted (cria ação, Kelsen aprova antes de protocolo)

**Missão:**
- Licenciamento LICIN 2.0 (Decreto Rio nº 55.622/2025)
- Pesquisa legislação por bairro/subzona (quando acionado)
- Compilação de prancha legal em PDF (formato conforme norma/órgão)
- Manutenção da base legislativa que sustenta a Skill cross-Gestor

**Conhecimento:**
- POPs de Legal (POP-LEGAL-01 até 04, incluso POP-LEGAL-RIU-01)
- Memoriais Descritivos
- Base de legislação municipal (origem: base legislativa de Kelsen)
- Norms + CAU/CREA + Legislação RJ (LC 270/2024, LC 274/2024, Decretos)

**Capacidade:**
- ✅ Consulta API RIU (geocoding, zoneamento) — com trava: validar coordenada vs. lote real
- ✅ Valida parâmetros urbanísticos (CAB, CAM, TO, afastamentos, gabarito)
- ✅ Monta DULI + Anexos I-V (LICIN 2.0)
- ✅ Compila prancha legal (plantas, cortes, fachadas, quadro de áreas, memorial)
- ✅ Sinaliza pendências bloqueantes (não inventa valores)
- ❌ Não decide quem assina como PRPA (segue autoria do Anteprojeto)
- ❌ Não assina como PREO (Kelsen sinaliza quando PREO está undefined)

**Arquivo de Estado:**  
`01_CEO\Gestores\Kelsen (Legal)\Agentes\Hely\_estado_hely.md` (4 seções fixas)

**Cadeia de Comando:**
- Recebe de: Kelsen
- Reporta a: Kelsen
- **Nunca** reporta direto a Wallenberg/Claudemberg (desvio de processo = sinalize e redirecione)

**Princípio de Design:**
- Autônomo (com julgamento real) mas operacional
- Dentro da execução, aplica julgamento — não é canalizado
- Sinaliza a Kelsen tudo que exija decisão estrutural (pendência, risco, lacuna, PRPA undefined)

**Acesso MCP:**
- Read: Google Drive (POPs, Memoriais, Clientes)
- Write: Google Drive (Documentos de caso, Drive cliente)
- ❌ Nunca altera compartilhamento/acesso de arquivo

**Integração Técnica:**
- API RIU (ArcGIS pgeo3.rio.rj.gov.br)
- Script Python: `_ferramentas\md_to_pdf.py` (MD→PDF)
- Script Python: `_ferramentas\gerar_prancha_legal.py` (JSON caso→PDF A1)
- Skill: `legal_base_legislativa_bairro` (consulta local, não input de Hely)

**Trava Obrigatória:**
- Geocoder padrão: `Geocode_composto_SIURB` (em vez de outros)
- Validação lote: `CadParcel/GeoPAL/MapServer/0` (evita coordenada cair na via)
- Fonte oficial sempre vence: RIU mapas.rio.rj.gov.br > API ArcGIS > Compilações de terceiros

---

## Modelo Leilão — 3 Próprios + Leilão Parceiros

**Serviços próprios (Sttickler cobra, produz ou coordena):**
1. Projeto Legal — **Produz** (Kelsen + Hely)
2. Projeto de Interiores — **Produz** (Agente futuro)
3. Compatibilização de Projetos — **Produz** (Agente futuro)

**Serviços em leilão (Cliente escolhe entre parceiros, Sttickler não faz markup):**
- Projeto de Arquitetura
- Projeto Estrutural
- Projeto Elétrico
- Projeto Hidrossanitário
- Projeto de Automação
- Projeto de Paisagismo

**Catálogo:** 11 serviços totais (3 próprios + 6 leilão + Projeto Executivo + Orçamento Executivo + Levantamento base)

**Margem:** Concentrada em **Compatibilização** (coordenação real dos projetos), não espalhada.

**Transparência ao cliente:** Não mostra qual é próprio vs. leilão (distinção é interna, Wallenberg/Gestores).

---

## Reuniões — Logística

| Reunião | Quando | Evento ID | Duração | Participantes |
|---------|--------|-----------|---------|---|
| **Semanal** | Seg 10:30 (America/Sao_Paulo) | 8idk6tq4mblmea6d14j22lp6jo | 1h | Wallenberg + Claudemberg |
| **Mensal (Conselho)** | 1ª seg do mês, 09:00 | inujhgm0kd5a3ecngrfer3cb14 | 1h 30m | Wallenberg + Gestores aprovados + Claudemberg |

**Conteúdo Semanal:**
- Leitura de `01_CEO/Decisoes_Autonomas/{Ano}/{Mês}.md` (livro-razão da semana)
- Wallenberg apresenta cada decisão autônoma: data, o que decidiu, por quê (princípios), como desfazer
- Claudemberg ratifica ou manda reverter, item por item

**Conteúdo Mensal:**
- Síntese estratégica (padrões emergentes, saúde do organismo)
- Equipes que Gestores já aprovados contrataram por conta própria (autonomia delegada)
- Relatório consolidado: `003_RELATORIOS_CONSELHO/{Ano}/{Mês}`

**Agendamento:** Evento recorrente já criado no Google Calendar (conectado a santosclaudembergg@hotmail.com)

---

## Fluxo — Determinístico vs. Autônomo

### Determinístico (Nunca Autônomo)

| O quê | Autoridade | Por quê |
|-------|-----------|--------|
| **Gates 13 & 16** | Wallenberg + Gestor (dupla aprovação, na hora) | Pontos críticos: incompatibilização × liberação obra |
| **Documento cliente/prefeitura** | Claudemberg antes | CAU/RRT responsabilidade técnica |
| **Protocolo em prefeitura** | Claudemberg antes | Ato externo, irreversível |
| **Eliminar Gestor/Agente** | Claudemberg antes | Destrutivo |

**Via de urgência (Função 11):** Gates 13/16 não esperam reunião; Wallenberg valida na hora + registra + reporta depois.

### Autônomo (Dentro de Fronteira)

| O quê | Autoridade | Mecanismo |
|-------|-----------|-----------|
| **Execução operacional** | Agente/Gestor | Executa, auditoria por contexto independente |
| **Decisão estrutural do CEO** | Wallenberg | Backup + livro-razão, ratifica na Semanal |
| **Contratação de Agente** | Gestor já aprovado | Testa, informa Wallenberg, vai pra Mensal |
| **Criação/Alteração de Skill** | Wallenberg | Testa, registra, ratifica na Semanal |
| **Alteração POP própria** | Gestor | Coordena com equipe, registra, ratifica depois |

---

## Drenagem de Fila — Contínua, Não Agendada

**Regra:** Pendência parada = falha de processo. Wallenberg está vivo quando a pasta é acessada → testa na hora.

**Operação:**
1. Wallenberg abre **Gestor** → Reconcilia fila, julga o que é dele, executa
2. Wallenberg abre **Agente** → Produz o que precisa
3. Wallenberg **carrega artefato** → Gestor audita o que não escreveu (auditoria por contexto)

**Anti-represamento:** Pendência marcada "esperando Wallenberg" que cabe no próprio agente volta com autonomia, não fica represada.

**Registro:** Toda drenagem entra no livro-razão no mesmo dia + Registro Diário.

---

## Cascata de Promoção de Nível

| Transição | Exame | Administrador | Ratificação |
|-----------|-------|---|---|
| Formação → Shadow | Teste sandbox | Wallenberg | Wallenberg (durante prox. Semanal) |
| Shadow → Assisted | Teste real supervisionado | Wallenberg | Wallenberg (durante prox. Semanal) |
| Assisted → Autonomous | Teste real autônomo | Wallenberg (se Agente de CEO), Gestor (se Agente de Gestor) | Wordenberg/Gestor (sem passar por Claudemberg) |

**Critério:** Quanto trabalho sobra para Claudemberg (quanto menos, mais pronto pra subir).

**Novo (27/07):** Promoção de nível não volta mais a Claudemberg caso a caso (último foi Hely Formação→Autonomous em cliente). Daqui: Examiner (Wallenberg ou Gestor) decide, registra no livro-razão, Claudemberg toma ciência no Painel/Semanal (não aprova antes).

---

## Capacidade Real — Resumo

### Produzem (Agentes Executores)
- ✅ **Legal** — Hely (Assisted) executa LICIN 2.0
- ✅ **Interiores** — (Agente futuro)
- ✅ **Compatibilização** — (Agente futuro, MCP Revit oficial da Autodesk)

### Coordenam (Agentes Coordenadores)
- 🔄 **Arquitetura** — Lúcio coordena parceiro externo (produção ainda não em-house)
- 🔄 **Complementares** — Estrutural/Elétrico/Hidro/Automação/Paisagismo coordenam parceiros
- 🔄 **Fechamento** — Orçamento/Cronograma coordenam parceiros

**Limite de ART/RRT:** CAU de Claudemberg (2026) cobre Legal, Estrutural (fundação rasa), Elétrico baixa tensão (residencial), Hidrossanitário. Fundação profunda + fora de padrão residencial exigem CREA externo.

---

## Serviços Intra-Organismo (Cross-Gestor)

**Dependência obrigatória:** Arquitetura **deve** consultar base legislativa de Legal antes do **Levantamento** (não Estudo Preliminar como era antes).

**Mecanismo:** Wallenberg prepara "snapshot" da base legislativa de Recreio (ex.) → carrega para Lúcio → Lúcio executa com dependência garantida.

**Sem competição:** Kelsen não interfere na execução de Lúcio; Lúcio não interfere em Legal.

---

## Arquivo de Estado — Estrutura Padrão

Cada Gestor/Agente novo nasce com seu arquivo no mesmo molde:

```markdown
# _estado_[nome].md

## 1. Onde parei / Em andamento
- [Caso A]: status
- [Caso B]: status

## 2. Pendências abertas
- [BLOQUEANTE] Causa: Efeito
- [PENDENTE] Causa: Efeito

## 3. Aprendizados que não posso esquecer
- Descoberta 1 (com referência)
- Descoberta 2 (com referência)

## 4. Como escrever nele
- Substitua seções, não append
- Apague o que virou passado
- Aponte pra docs em vez de copiar
```

**Convive com Registro Diário:** Estado é privado ("de onde parei"); Registro Diário é entrada/saída pra Claudemberg.

**Não gera PDF** (é arquivo de máquina, reescrito toda execução).

---

## Onboarding de Novo Cliente

Dentro da Função 6 (Padronizador de Documentos):

1. Verificar se existe pasta do bairro em `000_CLIENTES`; se não, criar
2. Criar pasta com nome do cliente dentro da pasta do bairro
3. Dentro da pasta do cliente, criar as 12 pastas de etapa
4. ID do projeto (`PRJ-XX-XX-NNN-YYYY`) serve só pra identificação, não governa a estrutura

**Execução:** Wallenberg (com decisão conjunta com Claudemberg) ou Gestor (depois de aprovado).

