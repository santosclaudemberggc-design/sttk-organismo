---
name: nbr8681-2025-seguranca-estruturas
description: NBR 8681:2025 — fatores de ponderacao (gf), coeficientes de combinacao (psi), combinacoes ELU/ELS para calcular esforcos de dimensionamento. Use sempre que Baumgart for montar combinacao de acoes, aplicar fator de seguranca, verificar ELU ou ELS — mesmo que o pedido so mencione "fator de seguranca", "combinacao de cargas", "gama-f" ou "psi", sem citar a norma pelo nome.
---

# NBR 8681:2025 — Acao e Seguranca nas Estruturas — Procedimento

> **RESSALVA DE FONTE** — Fatores gf e psi baseados no framework da versao 2003. A versao 2025 (pub. 29/09/2025) pode ter ajustado valores. Tratar como provisorios ate leitura do texto integral ABNT.

Skill de Inteligencia Tecnica, equipe de Cardozo (Gestor Complementares). Uso principal: **Baumgart** (Estrutural). Cross-disciplina: **Saturnino** (acoes em reservatorios/coberturas), **Landell** (acoes de equipamentos em salas tecnicas).

Ponte entre NBR 6120 (cargas) e NBR 6118 (dimensionamento): a 6120 diz QUANTO pesa, a 8681 diz COMO combinar e QUAL margem aplicar.

## Fatores de ponderacao (gf) — ELU Normal

| Acao | Desfavoravel | Favoravel |
|------|-------------|----------|
| Permanente (G) — peso proprio | 1,4 | 1,0 |
| Permanente (G) — empuxo terra | 1,2 | 0,9 |
| Permanente (G) — empuxo agua | 1,2 | 1,0 |
| Variavel (Q) — geral | 1,4 | 0 |
| Variavel (Q) — temperatura | 1,2 | 0 |

ELU Especial/Construcao: gf = 1,2 (desf.) / 1,0 (fav.) para ambos.
ELU Excepcional: gf = 1,2 (G) / 1,0 (Qexc) / 1,0 (demais Q com psi2).

## Coeficientes de combinacao (psi)

| Acao variavel | psi0 | psi1 | psi2 |
|--------------|------|------|------|
| Residencial | 0,5 | 0,4 | 0,3 |
| Escritorios (com concentracao) | 0,7 | 0,6 | 0,4 |
| Acesso de publico | 0,7 | 0,6 | 0,4 |
| Garagens/estacionamentos | 0,8 | 0,7 | 0,6 |
| Bibliotecas/almoxarifados | 0,8 | 0,7 | 0,6 |
| Vento | 0,6 | 0,3 | 0 |
| Temperatura | 0,6 | 0,5 | 0,3 |

## Combinacoes ELU

**Normal:** Fd = Sum(ggi x FGi,k) + gq x [FQ1,k + Sum(psi0j x FQj,k)]
**Especial:** mesma formula, gf reduzidos.
**Excepcional:** Fd = Sum(ggi x FGi,k) + FQexc + Sum(psi2j x FQj,k)

## Combinacoes ELS

**Rara:** Fd,ser = Sum(FGi,k) + FQ1,k + Sum(psi1j x FQj,k) — tensoes maximas
**Frequente:** Fd,ser = Sum(FGi,k) + psi1 x FQ1,k + Sum(psi2j x FQj,k) — fissuracao
**Quase-permanente:** Fd,ser = Sum(FGi,k) + Sum(psi2j x FQj,k) — flechas

## Erros comuns

1. Trocar psi0/psi1/psi2 (inverte seguranca)
2. Esquecer ELS (fissurar nao e colapsar, mas e patologia real)
3. Classificar Q1 errada (varia por elemento: viga de cobertura = vento; laje garagem = veiculo)
4. gf = 1,4 para tudo (empuxo agua e temperatura tem gf proprio)

## Lacunas

Texto integral ABNT 2025 nao lido. Valores provisorios. Fechar antes de uso em caso real.

Fonte completa: `01_CEO/Skills_Propostas/2026/Setembro/baumgart_nbr8681-2025-acao-seguranca-estruturas.md`
