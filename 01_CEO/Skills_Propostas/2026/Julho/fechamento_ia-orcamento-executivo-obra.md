---
name: skill-proposta-fechamento-ia-orcamento-executivo
description: "PROPOSTA — panorama de ferramentas de IA para orçamento executivo de obra (quantitativo automático, base SINAPI/CUB/TCPO) relevante para o futuro Gestor Fechamento"
metadata:
  type: skill_proposta
  status: proposta_pendente_reuniao_mensal
  gestor_alvo: Gestor Fechamento — não implantado
  data: 2026-07-19
---

# Skill proposta: IA para Orçamento Executivo de Obra

## Para quem é
**Gestor Fechamento**, ainda não implantado — primeira proposta de Skill dirigida a esse Gestor desde que a rotina diária começou (16/07/2026 só cobriu Legal, Arquitetura e Complementares). "Orçamento Executivo de Obra" é um dos 11 serviços do catálogo real da Sttickler (ver [[sttickler_negocio_leilao]]) — fica pronta para quando esse Gestor e seu Agente forem criados.

## O que ensina/entrega
Mercado de ferramentas de IA para orçamento de obra amadureceu em 2026, com dois padrões que valem a pena registrar:

1. **Quantitativo automático a partir de planta.** Ferramentas como Togal.AI leem plantas em PDF e medem automaticamente áreas, perímetros e volumes — o que levava um orçamentista um dia inteiro passa a ser feito em minutos. Isso é diretamente aplicável ao fluxo da Sttickler, já que o Projeto Legal/Arquitetura já produz as plantas compiladas (Hely já compila prancha A1 com quadro de áreas — ver histórico do Kelsen/Hely) — um Agente de Fechamento poderia consumir essas mesmas plantas como entrada do orçamento, sem trabalho duplicado.
2. **Base de referência nacional consolidada.** Softwares brasileiros (ex.: i9 Orçamentos, Korvi, OrçaFascio) trabalham sobre bases públicas — **SINAPI, CUB (Sinduscon) e TCPO** — como referência de custo unitário, atualizadas mensalmente. Para o Rio de Janeiro especificamente, o CUB é publicado pelo Sinduscon-Rio até o dia 5 de cada mês (categoria mais usada como indexador no mercado fluminense é a R8N — residencial padrão médio). Vale a pena o futuro Agente de Fechamento manter essa referência sempre atualizada, no mesmo espírito da base legislativa por bairro do Hely (não confiar em número desatualizado).

## Ação proposta
Quando o Gestor Fechamento for criado, considerar esta Skill como ponto de partida para o Agente que vai produzir o orçamento executivo: (a) consumir o quantitativo direto da prancha já compilada pelo Legal/Arquitetura, em vez de remedir do zero; (b) manter referência de custo unitário atualizada mensalmente contra SINAPI/CUB-Sinduscon-Rio/TCPO, não uma tabela fixa.

## Fonte da pesquisa
- [IA para orçamento de obra: tudo o que você precisa saber](https://blog.obraprima.eng.br/ia-para-orcamento-de-obra/)
- [Orçamento de Obras Online com IA e Base SINAPI/CUB – Korvi](https://korvi.com.br/orcamento-de-obras/)
- [Sinduscon Rio de Janeiro — Custo Unitário Básico](https://www.sinduscon-rio.com.br/wp/servicos/custo-unitario-basico/)
- Valores de CUB RJ (R8N, maio/2026) obtidos por fontes secundárias de mercado imobiliário (myside.com.br, invexo.com.br) — **confiança baixa/indicativa**, não confirmados na fonte primária Sinduscon-Rio; qualquer uso real precisa reconfirmar direto no site do Sinduscon
- Pesquisado em 19/07/2026, rotina diária do Wallenberg

## Governança
Proposta pendente — não cria o Gestor Fechamento nem qualquer Agente (isso é decisão estrutural, fora do escopo desta rotina). Fica arquivada para quando Claudemberg decidir avançar a construção desse Gestor (Princípio 13).
