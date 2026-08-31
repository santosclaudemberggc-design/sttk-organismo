---
titulo: POP-COMPL-01 — Validação do Briefing de Arquitetura antes de despachar os 6 Agentes
dono: Cardozo (Gestor Complementares)
criado_em: 2026-08-31
gatilho_de_criacao: Varredura de melhoria (Passo 7) da rotina wallenberg-drenagem-continua v2.3, 31/08/2026. Padrão recorrente sem POP — a validação de Briefing é a função central de Cardozo, foi o que o Exame 1 (caso Vilela, 14/08/2026) testou, e a única referência escrita eram as "Dependências obrigatórias" espalhadas no documento de nomeação da equipe (_nomeacao_equipe_2026-08-26.md), não um checklist operacional.
precedente_de_forma: POP-LEGAL-06 (Kelsen, checagem preventiva de glifo) e REGRA-ARQ-01 (Lúcio, pressão comercial) — Gestor formaliza POP próprio para padrão recorrente.
status: ativo
autonomia: POP próprio de Gestor (Função 6 ampliada 27/07/2026) — não altera escopo comercial nem hierarquia, apenas operacionaliza a Regra de Ouro da Validação já fixada em 14/08/2026.
---

# POP-COMPL-01 — Validação do Briefing de Arquitetura

## 1. Objetivo

Garantir que o Briefing aprovado que Lúcio (Gestor Arquitetura) entrega via Drive cobre **todos** os
requisitos técnicos que cada um dos 6 Agentes de Complementares precisa para executar sua disciplina.
Nenhum Agente é despachado antes desta validação passar.

## 2. Quando aplicar

- Sempre que um Briefing aprovado de Arquitetura chegar para Complementares (via Drive).
- Sempre que o Briefing for revisado/reemitido por Lúcio (revalidar do zero, não só o delta).
- Antes de qualquer acionamento dos Agentes Baumgart, Landell, Saturnino, Glaziou ou Tenreiro.

## 3. Regra-mãe (não negociável)

**Briefing incompleto para uma disciplina = não despacha aquela disciplina.** A lacuna é escalada a
Wallenberg com o **item específico que falta**, para Wallenberg levar a Lúcio esclarecer com o cliente.
Nunca se preenche a lacuna por suposição, nem se manda o Agente "começar com o que tem".

Precedente: Exame 1 (caso Vilela, 14/08/2026) — Briefing dizia só "paisagismo moderno, sem drenagem
complexa" (vago). A resposta correta foi recusar a distribuição a Glaziou e escalar pedindo
especificação técnica de paisagismo, não deixar Glaziou "interpretar".

## 4. Checklist de validação — por Agente

Para cada disciplina, confirmar que o Briefing responde a TODOS os itens. Marcar `OK` / `FALTA`.

### 4.1 Baumgart — Estrutural
- [ ] Tipo de estrutura definido: steel frame / concreto armado / misto / outro
- [ ] Número de pavimentos e pé-direito
- [ ] Existência de subsolo / contenção
- [ ] Tipo de fundação pretendido OU dado de sondagem do solo (se já houver)
- [ ] Cargas especiais conhecidas (piscina elevada, laje técnica, telhado verde, etc.)
- [ ] Classe de agressividade ambiental / proximidade do mar (orla)
> Sem "tipo de estrutura" o Briefing está incompleto para Baumgart — este é o item que o Exame 2
> Caso 1 (14/08/2026) fixou como requisito de Briefing, não decisão técnica livre do Agente.

### 4.2 Landell — Automação + Elétrica
- [ ] Lista de pontos elétricos por ambiente (tomadas, iluminação, pontos de força)
- [ ] O que deve ser automatizado (iluminação, climatização, cortinas, segurança, irrigação...)
- [ ] Existência de geração fotovoltaica / carregador de veículo elétrico
- [ ] Padrão de entrada de energia pretendido / concessionária
- [ ] Integração desejada com o projeto hidrossanitário (aquecimento, bombas, reuso)

### 4.3 Saturnino — Hidrossanitário
- [ ] Água fria: fonte (rede / poço) e pontos de consumo
- [ ] Água quente: sistema pretendido (elétrico, gás, solar, bomba de calor) e pontos
- [ ] Esgoto: rede pública ou solução local (fossa/filtro/sumidouro)
- [ ] Reuso de água / captação de chuva: sim ou não, e usos previstos (NBR 16783)
- [ ] Louças e metais especiais, aquecimento de piscina, irrigação

### 4.4 Glaziou — Paisagismo
- [ ] Descrição da paisagem desejada (estilo, espécies, áreas de estar externas)
- [ ] Localização/clima do lote e zona bioclimática (para escolha de espécies e drenagem)
- [ ] Áreas permeáveis exigidas / taxa de permeabilidade do lote
- [ ] Drenagem sustentável: jardim de chuva, trincheira de infiltração, sim ou não
- [ ] Irrigação, iluminação de jardim, mobiliário externo
> "Moderno, sem drenagem complexa" NÃO é especificação técnica — é o erro do caso Vilela.

### 4.5 Tenreiro — Interiores
- [ ] Estilo desejado por ambiente
- [ ] Acabamentos: pisos, paredes, forros, marcenaria (nível de detalhamento esperado)
- [ ] Mobiliário: solto, planejado, ou ambos; peças-chave nomeadas
- [ ] Paleta de cores / referências visuais do cliente
- [ ] Iluminação interna: cenas, temperatura de cor, automação (cruzar com 4.2)
- [ ] Requisitos de desempenho de vedação interna (acústica entre ambientes, fixação de peças)

### 4.6 Mindlin — Apresentação
- Mindlin **não** consome o Briefing diretamente. Depende dos outputs dos outros 5 Agentes,
  já compilados por Cardozo. Só é acionado quando os 5 entregaram.
- [ ] Confirmar que os 5 outputs estão completos e sem contradição aberta entre disciplinas
      antes de acionar Mindlin.

## 5. Fluxo

1. Recebo o Briefing aprovado de Lúcio (Drive).
2. Rodo o checklist da Seção 4, disciplina por disciplina.
3. **Tudo OK nas 5 disciplinas executoras** → despacho os Agentes (Baumgart, Landell, Saturnino,
   Glaziou, Tenreiro em paralelo). Mindlin fica para depois.
4. **Qualquer `FALTA`** → NÃO despacho a disciplina afetada. Escalo a Wallenberg um bilhete curto:
   `Disciplina X — Briefing não cobre: <item específico 1>, <item específico 2>`. As disciplinas
   sem lacuna podem seguir; a com lacuna espera o esclarecimento de Lúcio.
5. Registro no meu arquivo de estado qual Briefing foi validado, data, e o que faltou (se faltou).
6. Coleto os outputs, organizo no Drive. **Não compilo Briefing Único — isso é de Wallenberg.**

## 6. Como escalar uma lacuna (modelo)

> Wallenberg — Briefing "<nome do caso>" validado em <data>. Pronto para 4 das 5 disciplinas.
> **Saturnino (Hidrossanitário) — Briefing não especifica:** (a) se há reuso de água / captação de
> chuva; (b) sistema de água quente pretendido. Sem isso não despacho Saturnino. Peço a Lúcio
> esclarecer com o cliente. Baumgart, Landell, Glaziou e Tenreiro seguem — Briefing os cobre.

Sempre item específico. Nunca "falta detalhe técnico".

## 7. Fora de escopo deste POP

- Compatibilização / clash detection entre disciplinas (não há Agente para isso hoje — lacuna
  estrutural registrada para Claudemberg desde 27/08/2026).
- Qualquer julgamento de mérito técnico dentro de uma disciplina — isso é do Agente, auditado
  por Cardozo no retorno.
- Documento de cliente real, Gates, protocolo.
