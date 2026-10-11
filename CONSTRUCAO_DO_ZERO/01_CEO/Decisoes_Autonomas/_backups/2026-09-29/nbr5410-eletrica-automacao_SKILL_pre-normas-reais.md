---
name: nbr5410-eletrica-automacao
description: NBR 5410:2004 (instalações elétricas de baixa tensão, vigente) + revisão 2026 em consulta pública + protocolos de automação residencial (KNX, Zigbee/Z-Wave, Modbus). Use sempre que Landell (ou qualquer Agente) for dimensionar circuito elétrico, definir DR/DPS, calcular corrente/condutor, especificar aterramento, ou escolher protocolo de automação — mesmo que o pedido só mencione "elétrica", "circuito", "disjuntor" ou "automação", sem citar a norma pelo nome.
---

# NBR 5410 — Elétrica e Automação Residencial

Skill de Inteligência Técnica da área Elétrica+Automação, equipe de Cardozo (Gestor Complementares). Quem consome: **Landell** (Agente Automação+Elétrica).

## Norma vigente vs. revisão em consulta

| Norma | Situação |
|---|---|
| NBR 5410:2004 | **Vigente — única com força normativa hoje.** Usar em todo projeto atual. |
| NBR 5410 (revisão 2026) | Em segunda consulta pública, publicação prevista fim de 2026. **Ainda NÃO tem força normativa.** |
| NBR 5419 | Vigente (SPDA — proteção contra descargas atmosféricas), vinculada ao projeto elétrico |

**⚠️ A "NBR 5410 2026" ainda não foi publicada. Todo projeto protocolado hoje segue a versão 2004 — não cite a revisão como exigência atual.**

## 1. Parâmetros fundamentais (NBR 5410:2004 vigente)

**Divisão de circuitos obrigatória:** iluminação (exclusivo por cômodo/área) · TUG (tomadas gerais, circuito separado da iluminação) · TUE (tomada de uso específico, circuito exclusivo por equipamento — chuveiro, ar-condicionado, forno). Potência máxima por circuito monofásico: 1.500W em TUG; TUE sem limite fixo, definido pelo equipamento.

**Condutores:** dimensionar por método de referência (forma de instalação) + corrente de projeto, com fatores de correção (temperatura, agrupamento de cabos, isolação PVC/EPR/XLPE). Cabos LSHF recomendados em áreas de escape.

**Aterramento e proteção:** sistema TN-S recomendado em obra nova. DPS obrigatório com equipamentos sensíveis. **DR (30mA) obrigatório em banheiro, área de serviço e cozinha.**

## 2. O que muda na revisão 2026 (monitorar, não aplicar ainda)

- Tabelas de corrente alinhadas à IEC 60364-5-52 (métodos B1, B2, C, D, E, F, G) — dimensionamento mais preciso, seções de cabo podem mudar
- Harmonização com NBR 5419 — elimina contradições de aterramento entre as duas normas
- Novas tecnologias: infraestrutura de recarga de VE, geração distribuída (solar), iluminação pública/equipamentos urbanos

## 3. Automação residencial

Pontos que precisam estar definidos no Briefing antes de projetar:

| Aspecto | Definir antes |
|---|---|
| Protocolo | KNX (robusto, padrão europeu) · Zigbee/Z-Wave (sem fio, residencial) · Modbus (industrial) |
| Topologia | Barramento centralizado vs. mesh distribuído |
| Integração elétrica | Atuadores precisam de circuito dedicado — planejar junto |
| BMS | Em projetos maiores, checar com Cardozo se cliente exige BMS integrado |

## Checklist prático ao receber Briefing

1. Tipo de edificação + carga total estimada (kVA)
2. Planta com pontos de tomada/iluminação + lista de TUE
3. Fornecimento da concessionária (mono/bi/trifásico)
4. Sistema de aterramento (TN-S em obra nova)
5. Corrente de projeto por circuito, fator de demanda, dimensionar condutores (NBR 5410:2004)
6. Disjuntores (curva B/C), DRs 30mA em circuitos úmidos, DPS em painel
7. VE, solar ou automação previstos? → reservar circuitos/dutos agora
8. Compatibilizar shafts elétricos com Saturnino — separação mínima 30cm
9. Confirmar se nova versão da norma foi publicada antes do protocolo

**Erros comuns:** não separar TUG de TUE · omitir DR em banheiro/cozinha · dimensionar cabo sem fator de agrupamento · omitir DPS em painel geral · compartilhar shaft com esgoto sem separação.

## Coordenação com outros Agentes de Cardozo

Saturnino (shafts, 30cm de distância) · Baumgart (passagem de eletrodutos previstas no memorial estrutural antes da concretagem) · Glaziou (circuito TUE separado + IP65 para jardim) · Tenreiro (posição de tomadas/interruptores validada antes de finalizar prumadas).

## O que esta Skill NÃO cobre

Média tensão (ANEEL + concessionária) · telecomunicações/cabeamento estruturado (NBR 14565) · CFTV/segurança eletrônica · SPDA detalhado (NBR 5419).

## Limitações honestas

- A revisão 2026 está em segunda consulta pública (junho/2026) — mudanças listadas são previstas, não confirmadas. Todo projeto protocolado agora segue 2004.
- Tabelas completas de corrente admissível da versão 2004 não estão reproduzidas aqui — consultar a norma diretamente para dimensionamento real.
- Texto oficial ABNT não foi lido diretamente — fontes técnicas secundárias verificadas em 28/08/2026.

## Escopo, crescimento e manutenção

Lacuna ou divergência nova não vira conhecimento oficial por decisão do Agente — reporte a Cardozo, que avalia e leva a Wallenberg para formalizar.
