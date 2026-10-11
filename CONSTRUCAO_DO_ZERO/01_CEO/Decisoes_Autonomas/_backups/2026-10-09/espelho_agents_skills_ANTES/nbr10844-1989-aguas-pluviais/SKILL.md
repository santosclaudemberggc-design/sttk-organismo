---
name: nbr10844-1989-aguas-pluviais
description: "NBR 10844:1989 — Instalações Prediais de Águas Pluviais: dimensionamento de calhas, condutores, caixas de areia e lançamento final. Status: ativa-com-ressalva (fonte primária ABNT não lida). Principal: Saturnino. Cross: Glaziou, Baumgart."
metadata:
  type: skill
  gestor: Cardozo
  agente_principal: Saturnino
  agentes_cross: [Glaziou, Baumgart]
  trilha: A
  norma: "ABNT NBR 10844:1989"
  status: ativa-com-ressalva
  versao: "1.0"
  ativada_em: "2026-09-10"
  validada_por: "Cardozo (v2.9, 10/09/2026)"
  fonte_primaria_lida: false
---

> ⚠️ RESSALVA DE FONTE — conteúdo apoiado em fontes secundárias (GreenGold Engenharia 07/2026, portais técnicos). O texto integral da ABNT NBR 10844:1989 não foi lido (norma paga). Os valores de intensidade pluviométrica específicos para o município do Rio de Janeiro (i em mm/h por zona IDF) não foram obtidos. Ao aplicar em caso real, Saturnino é obrigado a:
> 1. Consultar as Equações IDF da Rio-Águas/Prefeitura RJ para obter o valor de i correto para o bairro do terreno.
> 2. Sinalizar esta lacuna no retorno a Wallenberg/Cardozo.
> 3. Tratar todos os parâmetros numéricos como provisórios até conferência contra a fonte primária.

# NBR 10844:1989 — Instalações Prediais de Águas Pluviais

## Para qual Agente serve

**Saturnino (Hidrossanitário)** — principal. O sistema de drenagem pluvial predial é parte do projeto hidrossanitário: calhas, condutores verticais, condutores horizontais, caixas de areia e ponto de lançamento.

**Glaziou (Paisagismo) — cross:** o ponto de lançamento do sistema pluvial (jardim de chuva, infiltração, vala, rede pública) precisa ser compatibilizado com o projeto paisagístico.

**Baumgart (Estrutural) — cross:** cobertura sem drenagem adequada acumula lâmina d'água = carga variável adicional que entra no cálculo estrutural (NBR 6120:2019).

---

## Fórmula Principal

```
Q (L/min) = I (mm/h) × A (m²) / 60
```

- **Q** = vazão de projeto (L/min)
- **I** = intensidade pluviométrica local (mm/h) — ⚠️ obter da equação IDF Rio-Águas para a zona do terreno
- **A** = área de contribuição (m²) — inclui área horizontal da cobertura + parcela de parede exposta

---

## Períodos de Retorno

| Tipo de Área | T recomendado |
|---|---|
| Pátios com acúmulo tolerável | T = 1 ano |
| **Coberturas/terraços residenciais** | **T = 5 anos** (padrão STTK) |
| Áreas onde transbordo é crítico | T = 25 anos |

---

## Sequência de Projeto

1. Definir i (mm/h) pela equação IDF Rio-Águas — zona do terreno
2. Calcular área de contribuição por trecho (cobertura + parcela de parede)
3. Calcular Q por trecho: Q = I × A / 60
4. Dimensionar calhas (seção, declividade mínima 0,5%)
5. Definir número e posição dos condutores verticais (DN mínimo ≈ 75mm — ⚠️ confirmar com norma)
6. Dimensionar condutores horizontais (declividade mínima 0,5%)
7. Especificar caixas de areia (obrigatórias antes do lançamento)
8. Definir e registrar ponto de lançamento no memorial

---

## Regra Fundamental — Sistema Separador Absoluto

**É proibido conectar águas pluviais à rede de esgoto sanitário** (NBR 8160 + legislação municipal RJ).

Todo condutor pluvial deve ir para: rede pública de águas pluviais, corpo receptor, infiltração no lote, jardim de chuva, ou reservatório (NBR 15527). Nunca em cano de esgoto.

---

## Armadilhas Frequentes

1. **Área de contribuição subestimada** — não incluir parcela de parede exposta
2. **Intensidade pluviométrica "média" sem conferir IDF local** — usar valor de outra cidade ou tabela genérica
3. **Calha sem declividade** — empoça mesmo sem chuva intensa
4. **Lançamento em rede de esgoto** — proibido, infração grave
5. **Ausência de caixa de areia** — obrigatória antes do lançamento
6. **Condutor vertical único para área grande** — distribuir conforme cálculo
7. **Projeto sem ART de engenheiro habilitado (CREA)**

---

## Interações STTK

| Norma/Skill | Como interage |
|---|---|
| NBR 15527:2019 | Quando projeto inclui aproveitamento de chuva: condutor vertical alimenta reservatório antes do extravasor ir para rede |
| NBR 16783 (reuso — Skill) | Sistema de reuso pode usar água pluvial como fonte alternativa |
| NBR 9575:2024 (impermeabilização — Skill) | Caimentos da cobertura impermeabilizada devem ser coordenados com calhas e ralos |
| NBR 6120:2019 (cargas — Skill Baumgart) | Lâmina d'água acumulada = carga variável adicional na laje |

---

## Obrigações ao Usar Esta Skill

1. Obter i (mm/h) da equação IDF Rio-Águas para a zona do bairro — nunca usar valor genérico sem confirmar
2. Dimensionar por trecho, não usar Q único para toda a cobertura
3. Registrar T adotado, valor de i e fonte no memorial descritivo
4. Verificar com Glaziou o destino final da água antes de fechar o projeto
5. Verificar com Kelsen/Hely se a rua tem rede pluvial separada (em bairros antigos de RJ pode ser rede unitária)
6. Sinalizar a lacuna de fonte primária em qualquer retorno a Cardozo/Wallenberg

---

## Fonte

- GreenGold Engenharia — "NBR 10844: drenagem pluvial predial" (jul/2026)
- GreenGold Engenharia — "Dimensionamento de Calhas e Condutores" (jul/2026)
- ABNT NBR 10844:1989 — norma primária (não lida — paga)
- Verificado: 10/09/2026
