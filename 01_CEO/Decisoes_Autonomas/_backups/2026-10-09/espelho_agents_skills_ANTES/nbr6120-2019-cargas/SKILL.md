---
name: nbr6120-2019-cargas
description: NBR 6120:2019 — ações para o cálculo de estruturas de edificações (cargas permanentes e acidentais/variáveis por tipo de uso). Use sempre que Baumgart (Estrutural) for definir carga de dimensionamento — mesmo que o pedido só mencione "sobrecarga", "peso próprio", "carga de uso" ou "guarda-corpo", sem citar a norma pelo nome. Cross-disciplina: Saturnino (cargas de reservatório/tubulação), Tenreiro (revestimentos pesados), Glaziou (cobertura verde), Landell (equipamentos elétricos).
---

# NBR 6120:2019 — Ações para o Cálculo de Estruturas de Edificações

Skill de Inteligência Técnica, equipe de Cardozo (Gestor Complementares). Uso principal: **Baumgart** (Estrutural). Fecha a tríade fundamental com **NBR 6118** (superestrutura) e **NBR 6122** (fundações) — a 6120 define QUANTO as outras duas precisam resistir.

Publicada out/2019, substitui a NBR 6120:1980 (39 anos sem atualização).

## Classificação das ações

**Permanentes (cargas mortas):** peso próprio + elementos fixos (forro, telhado, revestimentos, alvenaria). Tabela 1 da norma (pesos específicos).

Armadilha comum: esquecer peso de revestimento cerâmico em laje de banheiro/cozinha (0,8-1,2 kN/m² a mais).

**Variáveis (cargas acidentais):** uso/ocupação — pessoas, móveis, veículos.

| Ocupação | Carga (kN/m²) | Observação |
|---|---|---|
| Dormitórios, salas, cozinhas, banheiros (residencial) | 1,5 | Sem acesso público |
| Varandas (residencial) | 2,0 | Acesso restrito |
| Escritórios | 2,0 | Sem arquivo pesado |
| Escadas (sem acesso público) | 2,5 | Residencial |
| Escadas (com acesso público) | 3,0 | Comercial/misto |
| Garagem — veículos leves | 3,0 | + carga concentrada por eixo |
| Coberturas inacessíveis | 0,5 | Só manutenção eventual |
| Coberturas com painéis solares | ≥ 1,5 | + carga de manutenção |
| Terraços/coberturas acessíveis | 3,0 | Acesso de público |

⚠️ Valores de fontes secundárias — confirmar texto integral ABNT antes de dimensionamento real.

**Especiais:** paredes divisórias móveis (mín. 1,0 kN/m²), compartimentos especiais (+3,0 kN/m²), guarda-corpo horizontal (0,8 kN/m), guarda-corpo vertical (mín. 2,0 kN/m), degrau isolado (2,5 kN concentrado).

## Sequência de uso

1. Levantar cargas permanentes (Tabela 1)
2. Levantar cargas variáveis por uso
3. Somar cargas especiais (divisórias, guarda-corpo, equipamentos)
4. Aplicar combinações/fatores de ponderação (NBR 8681)
5. Alimentar NBR 6118 (superestrutura) e NBR 6122 (fundações)

## Interface com outras normas

| Norma | Relação |
|---|---|
| NBR 6118:2026 Em.1 | Recebe as cargas como dado de entrada |
| NBR 6122:2019 Em.1 | Recebe o somatório para dimensionar fundação |
| NBR 8681 | Fatores de combinação e ponderação |
| NBR 9575:2024 | Peso de sistema impermeabilizante em cobertura → carga permanente |
| COSCIP/CBMERJ Decreto 42/2018 | Compartimentação/TRRF pode afetar espessuras → afeta carga permanente |

## Erros comuns

1. Usar valores da NBR 6120:1980 (CANCELADA) — mudaram significativamente, especialmente garagens/coberturas.
2. Esquecer peso de revestimento pesado (mármore, porcelanato grande formato) — pode chegar a 2,0+ kN/m².
3. Ignorar paredes divisórias mesmo sem especificação na planta — mínimo 1,0 kN/m² é exigido.
4. Subestimar cobertura com painéis solares (mín. 1,5 kN/m² + manutenção).
5. Misturar categoria de garagem residencial com comercial — norma trata diferente.

## Lacunas conhecidas

Texto integral ABNT não lido (fontes secundárias: portais de engenharia). Tabela 1 completa de pesos específicos não disponível. Fatores de combinação dependem da NBR 8681 (não lida — próxima prioridade sugerida). Nenhuma emenda encontrada até 08/09/2026 (versão vigente confirmada: 2019).

**Fonte primária:** ABNT NBR 6120:2019. **Confiança:** média (fontes secundárias). **Avaliada e aprovada por Cardozo em 08/09/2026. Ratificada por Claudemberg em 09/09/2026 (Reunião Semanal).**
