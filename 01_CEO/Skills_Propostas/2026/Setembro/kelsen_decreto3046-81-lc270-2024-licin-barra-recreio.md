---
name: decreto3046-81-lc270-2024-licin-barra-recreio
description: "Base legal para licenciamento LICIN 2.0 na Barra da Tijuca e Recreio dos Bandeirantes: Decreto 3046/81 (ZE-5/Zona Plano Piloto) incorporado à LC 270/2024, e como Hely identifica os parâmetros por subzona via RIU antes de cada consulta prévia."
version: "1.1"
status: ativa-com-ressalva
created: 2026-09-21
updated: 2026-09-28
changelog:
  - "1.1 (28/09/2026, Kelsen, aprovado por Claudemberg): treino de 28/09. §2 fonte do RIU alinhada a mapas.rio.rj.gov.br; §3 menção 'ZPR – Zona de Proteção de Ruas' removida (sem fonte); §4 faixa de marinha reescrita (os 33 m são a própria faixa); §4 APP de lagoa marcada 'a confirmar' com distinção urbano/rural. Ver R10."
author: Rotina Diária Skills v3.2
gestor_validador: kelsen
agente_principal: hely
cross_disciplina:
  - oscar
fonte_primaria_lida: "parcial — Decreto 3046/81 via câmara.rj.gov.br (disponível em PDF); LC 270/2024 via legisweb.com.br (truncada no Art. 80; Art. 106 não verificado)"
metadata:
  tipo: Inteligência (Trilha A)
  norma_base: "Decreto 3046/81 (ZE-5) + LC 270/2024 Plano Diretor + LICIN 2.0 (Decreto 55.622/2025)"
  zona_geografica: "Barra da Tijuca, Recreio dos Bandeirantes, Baixada de Jacarepaguá — Rio de Janeiro"
  tags:
    - licin-barra
    - decreto3046
    - ze-5
    - zona-plano-piloto
    - parametros-urbanisticos
    - kelsen
    - hely
    - barra-tijuca
    - recreio
---

# Base Legal para Licenciamento LICIN 2.0 na Barra da Tijuca e Recreio
## Decreto 3046/81 (ZE-5) integrado à LC 270/2024

---

## POR QUE ESTA SKILL

Quando Kelsen/Hely recebe um projeto na Barra da Tijuca ou Recreio dos Bandeirantes, **a base legal aplicável é diferente do resto da cidade**. O LICIN 2.0 (Decreto 55.622/2025) usa como parâmetros urbanísticos os dados do Plano Diretor (LC 270/2024), que para a Barra/Recreio **manteve os parâmetros herdados do Decreto 3046/81** — publicado em 1981 especificamente para a Zona Especial 5 (ZE-5). Não conhecer essa cadeia legislativa = montar DULI com gabarito errado = exigência da prefeitura na análise.

---

## 1. A CADEIA LEGISLATIVA DA BARRA/RECREIO

```
Barra da Tijuca e Recreio dos Bandeirantes
        ↓
Zona Especial 5 (ZE-5) — Baixada de Jacarepaguá
        ↓
Decreto 3046/81 — parâmetros originais (1981)
        ↓
LC 270/2024 — novo Plano Diretor — incorporou ZE-5 como
"Zona do Plano Piloto" (ZPP) — parâmetros MANTIDOS
        ↓
LICIN 2.0 (Decreto 55.622/2025) — usa LC 270/2024 como base
        ↓
Resultado: para licenciamento na Barra/Recreio,
os parâmetros de referência são os do Decreto 3046/81
(agora chamado ZPP no PD de 2024)
```

**Ponto crítico:** o Decreto 3046/81 é um dos atos normativos mais complexos da cidade — tem dezenas de subzonas (A-1, A-2, A-17, A-18, A-20 etc.), cada uma com gabarito, índice de aproveitamento (IAA/CA), taxa de ocupação (TO) e afastamentos próprios. Não existe um parâmetro único "da Barra" — cada lote precisa ser localizado em sua subzona.

---

## 2. COMO IDENTIFICAR A SUBZONA DO LOTE

**Passo obrigatório antes de qualquer consulta prévia:**

1. Acessar o **RIU digital — SMU** (Relatório de Informações Urbanísticas)
   - Portal oficial da casa: `mapas.rio.rj.gov.br` (Certidão/Relatório de Informações Urbanísticas) — fonte oficial que vence qualquer fonte secundária
   - Inserir endereço completo ou matrícula do imóvel
   - O RIU retorna: zona (ZPP = ex-ZE-5), subzona, parâmetros aplicáveis

2. Verificar no RIU:
   - **Gabarito (G)**: número máximo de pavimentos
   - **Índice de Aproveitamento (IAA) / Coeficiente de Aproveitamento (CA)**: área construída ÷ área do lote
   - **Taxa de Ocupação (TO)**: projeção da edificação ÷ área do lote
   - **Afastamentos**: frontal, lateral, de fundos (metros)
   - **Testada mínima de lote**

3. **Exemplo de parâmetros típicos de subzona residencial** (Subzona A — valores referência, NÃO usar sem confirmar via RIU para o lote específico):
   - Gabarito: 2 pavimentos
   - IAA: 0,60
   - TO: 40%
   - Afastamento frontal: 10,00 m
   - Afastamentos laterais: dispensados quando frontal ≥ 10 m

**Atenção:** esses valores são EXEMPLOS de uma subzona residencial genérica do Decreto 3046/81. A Barra e Recreio têm subzonas comerciais, mistas, de uso especial (ZDE — Zona de Domínio Especial do Plano Piloto) e áreas de proteção ambiental, cada uma com parâmetros distintos. Nunca assumir parâmetro sem RIU.

---

## 3. PARÂMETROS QUE O NOVO PD (LC 270/2024) ALTEROU OU NÃO

### O que LC 270/2024 **MANTEVE** na Barra/Recreio

- Estrutura de subzonas com parâmetros diferenciados (agora ZPP)
- Gabaritos baixos nas subzonas residenciais (1–2 pavimentos típicos)
- Conceito do Plano Piloto de Lúcio Costa: baixa densidade, afastamentos generosos, ampla área verde

### O que LC 270/2024 pode ter **ALTERADO** (verificar via RIU por lote)

- Possibilidade de uso da **OODC / Outorga Onerosa** para ultrapassar o CA básico (ver Skill OODC)
- **TDC (Transferência do Direito de Construir)** pode ser disponível em alguns setores da Barra (ver Skill TDC/LICIN 2.0)
- Sobreposição de outros instrumentos da LC 270/2024 (ex.: AEIS) — conferir no RIU do lote

### O que NÃO mudou

- Restrições da APA do Recreio (Área de Proteção Ambiental) — regras ambientais sobrepostas ao zoneamento
- Recuo de praia / faixa de marinha em lotes de orla
- Proteção da Lagoa de Jacarepaguá e Lagoa da Tijuca (legislação ambiental estadual)

---

## 4. SOBREPOSIÇÕES LEGAIS NA BARRA/RECREIO — MAPA DE RISCO

| Condição do lote | Legislação adicional a verificar |
|---|---|
| Lote com testada para praia | Terreno de marinha (SPU): a faixa **é** a própria largura de 33 m, medida a partir da linha do preamar médio de 1831 — não é recuo adicional além dela (DL 9.760/1946, art. 2º — **a confirmar** em fonte primária). Parte do lote dentro da faixa exige regularização junto à SPU |
| Lote próximo a lagoa | APA Estadual + plano de manejo específico |
| Lote em área de antigas "Superquadras" | Normas específicas do Plano Piloto de Lúcio Costa — gabarito máximo fixo |
| Condomínio horizontal já aprovado (ex: Orla Bothanica) | Regramentos internos do Estatuto do Condomínio (Hely deve ler o Anexo II — Regramento Construtivo) |
| Área de preservação permanente (APP) | Lei Federal 12.651/2012 (Código Florestal), art. 4º — largura da faixa no entorno de lagoa natural **depende de zona urbana x rural** (e do tamanho do corpo d'água na zona rural); o valor de 30 m vale, em tese, só para zona urbana. **A confirmar** em fonte primária, inclusive eventual regra municipal de APP urbana posterior. Nunca aplicar 30 m sem essa conferência |

---

## 5. PROTOCOLO HELY — CHECKLIST PARA PROJETOS NA BARRA/RECREIO

**Antes de montar a DULI (LICIN 2.0):**

- [ ] Gerar RIU pelo endereço completo do lote
- [ ] Identificar subzona ZPP (ex-ZE-5) e anotar GA/IAA/TO/afastamentos
- [ ] Verificar sobreposições: faixa de marinha, APA, APP, condomínio com regramento próprio
- [ ] ⚠️ OODC — verificar disponibilidade SOMENTE APÓS Art. 106 LC 270/2024 confirmado em fonte primária (ver R1). Até lá: registrar como "a confirmar", NÃO informar cliente sobre eventual isenção
- [ ] Verificar LMS (Licença Municipal de Supressão) se houver árvores no lote — obrigatória para todo unifamiliar; em APP/área alagadiça pode tornar-se LMP+LMI (Decreto 51.503/2022 Art. 27 p.ú. II/IV)
- [ ] Se condomínio existente: ler Regramento Construtivo (Anexo do Estatuto) antes de propor implantação
- [ ] Confirmar com Lúcio/Oscar se o partido arquitetônico proposto cabe nos parâmetros levantados

---

## RESSALVAS

**R1 (CRÍTICA) — Art. 106 LC 270/2024 (isenção OODC 5 anos) NÃO CONFIRMADA:** o texto da LC 270/2024 estava disponível apenas até o Art. 80 nas fontes consultadas. A "isenção de OODC por 5 anos" mencionada em debates da Câmara Municipal não pôde ser verificada como texto aprovado do Art. 106. **Não informar cliente sobre isenção de OODC até Hely ler o Art. 106 na íntegra** (Diário Oficial ou via SMU).

**R2 — Parâmetros por subzona:** os exemplos numéricos nesta Skill (IAA 0,60, TO 40%, afastamento 10 m) são de UMA subzona residencial genérica do Decreto 3046/81. Cada lote tem sua subzona própria — NUNCA usar esses números sem confirmar via RIU.

**R3 — LC 270/2024 em implementação:** o novo Plano Diretor (jan. 2024) está em fase de regulamentação progressiva. Algumas ZPP ainda usam Decreto 3046/81 como referência direta. Hely verifica qual instrumento está sendo aceito pelo balcão digital da SMU para consulta prévia.

**R4 — Decreto 3046/81 texto integral:** disponível em PDF na Câmara Municipal (mail.camara.rj.gov.br). Para projetos com dúvida de subzona, Hely deve consultar o texto original do Decreto (disponível via WebFetch ou download direto).

**R5 CRÍTICA — LMS ausente do checklist (Kelsen, 21/09):** adicionada ao checklist acima. POP-GESTOR-LEGAL-01 item 4.4 registra LMS obrigatória para todo unifamiliar — ativo desde 28/07/2026. A Barra/Recreio com APA e lotes próximos a lagoa é o cenário de maior risco para rito LMP+LMI. Omissão corrigida nesta versão.

**R6 — Nomenclatura ZPP vs ZRM1-B (Kelsen, 21/09):** o caso ativo Daniel-OB (Recreio) usa subzona "ZRM1-B" do Decreto 3046/81. A Skill refere "ZPP" como denominação da LC 270/2024, mas não confirma se as subzonas internas (ZRM1-B, A-17 etc.) foram renomeadas ou mantidas. Hely deve confirmar via RIU se o novo PD manteve a nomenclatura de subzonas do Decreto 3046/81 antes de usar a terminologia desta Skill como definitiva.

**R7 — Lacuna Art. 106 duplicada com Skill TDC/LICIN 2.0 (Kelsen, 21/09):** a mesma dúvida sobre isenção de OODC 5 anos já consta como lacuna pendente na Skill TDC/LICIN 2.0 (16/09). A resolução deve ser centralizada naquela Skill quando Hely confirmar o Art. 106 via fonte primária — não criar dois pontos de atualização independentes para a mesma lacuna.

**R8 CRÍTICA — Checklist item OODC corrigido (Kelsen, 21/09):** o checklist original instruía "Consultar se o lote está em área de OODC disponível" sem alertar sobre o Art. 106 em aberto — contradição interna com a R1. Corrigido nesta versão para condicionar a consulta à confirmação do Art. 106.

---

**R9 — Ratificada por Claudemberg (21/09/2026):** status promovido de `proposta-com-ressalvas` para `ativa-com-ressalva` por Claudemberg em sessão manual. Todas as ressalvas acima permanecem ativas — uso pelo Hely condicionado às ressalvas R1, R5 e R8 especialmente.

**R10 — Correções do treino de 28/09/2026 (Kelsen, aprovado por Claudemberg):** (a) fonte do RIU alinhada à oficial da casa, `mapas.rio.rj.gov.br` (antes apontava `geoinfo.rio/smdu`); (b) "ZPR – Zona de Proteção de Ruas" removida — nenhuma fonte encontrada para esse instrumento; se reaparecer, só volta com artigo da LC 270/2024 citado; (c) faixa de marinha reescrita — os 33 m são a própria faixa, não recuo além dela (**a confirmar** DL 9.760/1946 em fonte primária); (d) APP de lagoa — largura depende de zona urbana x rural (Lei 12.651/2012, art. 4º), **a confirmar** em fonte primária. Registro do treino: `01_CEO/Gestores/Kelsen (Legal)/Casos_TESTE/treino_skills/2026-09-28_decreto3046-81-lc270-2024.md`.

---

## FONTES VERIFICADAS

- Prefeitura RJ — "Novo Plano Diretor propõe manutenção de parâmetros na Barra da Tijuca" [prefeitura.rio] (secundária ✓)
- Câmara Municipal RJ — "Plano Diretor prevê potenciais construtivos mantidos na Barra e parte do Recreio" [camara.rio] (secundária ✓)
- Câmara Municipal RJ — Decreto 3046/81 PDF [mail.camara.rj.gov.br] (disponível; parâmetros específicos por subzona não lidos na íntegra nesta rodada)
- LC 270/2024 via legisweb.com.br — lida parcialmente (até ~Art. 80); Art. 106 não verificado
- **LICIN 2.0 (Decreto 55.622/2025)** — referenciado, não relido nesta rodada (Skill TDC/LICIN 2.0 de 16/09 cobre detalhes)
