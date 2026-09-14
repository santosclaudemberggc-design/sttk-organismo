---
name: nbr17076-2024-tratamento-esgoto-fossa-filtro-sumidouro
version: v1.0
status: proposta
data: 2026-09-14
tipo: Inteligência (Trilha A)
gestor_alvo: Cardozo (Complementares)
agente_principal: Saturnino (Hidrossanitário)
agentes_cross: Glaziou (drenagem próxima ao sistema), Baumgart (carga sobre cobertura/estrutura das unidades)
substitui_normas: NBR 7229:1993, NBR 13969:1997
---

# Skill: NBR 17076:2024 — Sistema de Tratamento de Esgoto de Menor Porte (Fossa, Filtro e Sumidouro)

## 1. CONTEXTO E RELEVÂNCIA

A **ABNT NBR 17076:2024** unifica e substitui dois documentos antigos (NBR 7229:1993 e NBR 13969:1997), publicando um único conjunto de requisitos para projeto de **sistemas de tratamento de esgoto sanitário de menor porte instalados no próprio terreno**, sem ligação com rede coletora pública, com contribuição diária de até **12.000 L/dia**.

**Quando aplicar no STTK:** sempre que o lote não tiver acesso à rede pública de esgoto — situação comum em terrenos rurais, loteamentos novos, condomínios afastados do sistema CEDAE/concessionária local, ou clientes que demandam sistema autônomo. Também relevante em caso de ampliações que aumentem o número de usuários além da capacidade do sistema existente.

---

## 2. MUDANÇA CRÍTICA VS. NORMAS ANTERIORES

| Aspecto | Antes (7229 + 13969) | Agora (17076:2024) |
|---------|----------------------|--------------------|
| Conexão fossa → sumidouro | Permitida diretamente | **PROIBIDA** — filtro anaeróbio obrigatório entre eles |
| Documentos de referência | Dois documentos separados | Um único documento unificado |
| Profundidade máxima do sumidouro | Não fixada expressamente | Máximo **3,5 m** |
| ART/RRT | Recomendada | **Obrigatória** (engenheiro — CREA) |

> **Regra essencial:** a sequência de tratamento é obrigatória — não há exceção para sistemas residenciais pequenos.

---

## 3. SEQUÊNCIA OBRIGATÓRIA DO SISTEMA

```
Esgoto da edificação
    ↓
[1] Pré-tratamento (caixa de gordura / separador de sólidos)
    ↓
[2] Tratamento primário — TANQUE SÉPTICO (fossa)
    ↓
[3] Tratamento secundário — FILTRO ANAERÓBIO
    ↓
[4] Disposição final — SUMIDOURO (poço absorvente) ou VALA DE INFILTRAÇÃO
```

Qualquer configuração que salte a etapa [3] está em desconformidade com a norma.

---

## 4. DIMENSIONAMENTO — TANQUE SÉPTICO (FOSSA)

### Fórmula do volume útil

```
V = 1000 + N × (q × T + K × Lf)
```

**Parâmetros:**
| Símbolo | Significado | Valor típico residencial |
|---------|-------------|--------------------------|
| V | Volume útil (litros) | — calcular |
| N | Número de usuários | conforme projeto |
| q | Contribuição de esgoto (L/usuário/dia) | 120 a 150 L/pessoa/dia (ou 80% do consumo médio histórico de água, mínimo 12 meses) |
| T | Período de detenção (dias) | ver tabela da norma |
| K | Fator de acumulação de lodo (dias) | ver tabela da norma |
| Lf | Volume de lodo fresco (L/dia) | calculado em função de q e N |

**Regras de configuração:**
- Se dividido em câmaras múltiplas, acrescenta-se **1.000 L por câmara adicional**
- Diferença de nível entrada–saída: **+10 cm** (saída mais baixa)
- Tubo-guia obrigatório para limpeza de lodo sem contato humano direto
- Mínimo 2 câmaras para sistemas com N > 5 usuários (prática recomendada)

---

## 5. DIMENSIONAMENTO — FILTRO ANAERÓBIO

| Parâmetro | Requisito mínimo |
|-----------|-----------------|
| Altura útil total (falso fundo + meio suporte) | ≥ **1,20 m** |
| Volume útil | ≥ **1.000 L** |
| Meio filtrante | pedra brita nº 4 ou meio plástico modular |
| Falso fundo | obrigatório para distribuição uniforme |

O filtro anaeróbio reduz a carga orgânica do efluente antes da disposição final, aumentando a vida útil do sumidouro e protegendo o lençol freático.

---

## 6. DIMENSIONAMENTO — SUMIDOURO (POÇO ABSORVENTE)

| Parâmetro | Requisito |
|-----------|-----------|
| Profundidade máxima | **3,5 m** |
| Número mínimo de poços | **2 poços a 100%** de capacidade cada (ou **3 poços a 50%**) |
| Operação | **Alternância obrigatória** — nunca usar os dois ao mesmo tempo continuamente |
| Distância entre poços (centro a centro) | ≥ **3,0 m** (ou diâmetro do maior quando variam) |
| Teste de percolação | **Obrigatório** antes do projeto — taxa de aplicação depende do solo |
| Distância mínima do nível máximo do lençol freático | ≥ **1,5 m** (base do sumidouro) |

**Quando não usar sumidouro:**
- Solo impermeável (argila pura, rocha): usar vala de infiltração ou ETE
- Lençol freático a menos de 3,0 m da superfície do terreno
- Terreno em encosta com risco de contaminação de nascentes

---

## 7. DISTÂNCIAS MÍNIMAS DO SISTEMA AO RESTANTE DO LOTE

| De / Para | Distância mínima |
|-----------|-----------------|
| Fundação de edificações | 1,5 m |
| Limite do lote | 1,5 m |
| Drenos e valos de drenagem | 1,5 m |
| Árvores | 3,0 m |
| Poços de abastecimento de água | 15,0 m |
| Corpos d'água (rios, lagoas) | ver legislação ambiental local |

---

## 8. LIMITES DE APLICAÇÃO

- **Máximo:** 12.000 L/dia de esgoto (contribuição diária total)
- Acima disso: obrigatório dimensionamento como Estação de Tratamento de Esgoto (ETE) — escapa do escopo desta norma
- Para condomínios maiores: somar contribuições de todas as unidades + áreas comuns

---

## 9. RESPONSABILIDADE TÉCNICA

- **ART (CREA) obrigatória** para o projeto — engenheiro civil ou sanitarista
- Para arquitetos: se o projeto hidrossanitário incluir sistema de tratamento, o Saturnino deve sinalizar ao arquiteto parceiro que a assinatura de ART de engenheiro é necessária além do projeto arquitetônico

---

## 10. INTERFACE COM OUTROS AGENTES STTK

| Agente | Interface |
|--------|-----------|
| **Saturnino** | Dimensionamento completo — fossa, filtro, sumidouro, layout no terreno |
| **Glaziou** | Drenagem pluvial do jardim não pode cruzar o sistema de tratamento; árvores a ≥ 3,0 m das unidades |
| **Baumgart** | Se a fossa for sob estrutura (garagem, calçada): carga acidental sobre a tampa e impermeabilização da laje de cobertura das unidades |

---

## 11. RESSALVAS E LIMITAÇÕES DESTA SKILL

⚠️ **Fontes secundárias:** o texto integral da NBR 17076:2024 (ABNT, pago) não foi lido diretamente. Os dados foram extraídos de fontes técnicas especializadas (GreenGold Engenharia, Projetista Pleno, Vallero Engenharia) com alta consistência entre si. Os parâmetros numéricos das tabelas (T, K, Lf detalhados) estão na norma original — Saturnino deve confirmar diretamente na ABNT ao dimensionar em caso real.

⚠️ **NBR 7229 e 13969 revogadas:** qualquer projeto que ainda use essas normas como referência está desatualizado. Esta norma 17076:2024 é a referência vigente.

---

## 12. QUANDO USAR ESTA SKILL

- Cliente em terreno sem rede de esgoto pública (urbano periférico ou rural)
- Projeto novo ou ampliação que aumente N de usuários
- Condomínio em área onde a concessionária não tem rede disponível
- Verificação de sistema existente (conformidade com norma vigente)

---

**Skill proposta em:** 14/09/2026  
**Proposta por:** Rotina Diária Skills v2.8 (segunda-feira)  
**Validação pendente:** Cardozo (Gestor Complementares)
