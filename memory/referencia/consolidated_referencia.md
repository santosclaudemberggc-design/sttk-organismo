---
name: consolidated-referencia
description: "Referência Técnica STTK — RIU API, Drive, Revit/Vitruvius, LICIN 2.0, Entregáveis, CAU/CREA, NBRs, Legislação"
metadata: 
  node_type: memory
  type: reference
  scope: "Integrações Técnicas, Legislação, Capacidade Real"
  updated: 2026-07-27
  originSessionId: 5bb7d99f-8636-4ada-948a-86139f91b2df
  modified: 2026-07-27T18:52:12.223Z
---

# Sistema STTK — Referência Técnica Consolidada

## RIU API (ArcGIS) — Acesso Automático a Zoneamento

**Problema resolvido (15/07/2026):** RIU exigia clique manual. **Errado** — é API pública ArcGIS REST com CORS liberado.

### Pipeline Endereço → Parâmetros (Sem Clique)

**1. Endereço → Coordenada (SIRGAS 2000 / UTM 23S, EPSG 31983)**

```
Geocoder: Geocode_composto_SIURB (padrão oficial, validado 15/07)
URL: pgeo3.rio.rj.gov.br/arcgis/rest/services/Geocode/Geocode_composto_SIURB
Input: endereço + CEP
Output: x, y (EPSG 31983)
Interpolação: localiza número por interpolação (dezenas de metros de desvio possível)

TRAVA A — Validar Lote Real:
URL: pgeo3.rio.rj.gov.br/arcgis/rest/services/CadParcel/GeoPAL/MapServer/0
Input: coordenada (x, y, EPSG 31983)
Output: "Número de lote" (confirma se ponto cai dentro do lote)
Se ponto cair na via (0 features): refinar até lote real antes de zoneamento
```

**2. Coordenada → Pacote RIU Completo**

```
URL: pgeo3.rio.rj.gov.br/arcgis/rest/services/Urbanismo/LBB_Zoneamento_urbano_vigente/MapServer/0/query
Method: POST/GET
Params:
  f=json
  geometryType=esriGeometryPoint
  inSR=31983
  spatialRel=esriSpatialRelIntersects
  outFields=*
  returnGeometry=false
  geometry={"x":..,"y":..,"spatialReference":{"wkid":31983}}

Output (todos os campos RIU):
  - sigla (zona + subzona)
  - zona
  - subzona
  - ap (Área de Planejamento)
  - legislacao (ref. legal)
  - cab (Coeficiente Aproveitamento Básico)
  - cam (Coeficiente Aproveitamento Máximo)
  - to_ (Taxa de Ocupação)
  - lote_min (Lote mínimo)
  - testada_min (Testada mínima)
  - gab_afast (Gabarito afastado)
  - gab_n_afast (Gabarito não afastado)
  - afast_fron (Afastamento frontal)
  - ics (Índice Comércio e Serviços)
  - obs_riu (Observações)
```

**Exemplo real (15/07/2026, Recreio dos Bandeirantes, Estrada dos Bandeirantes 5000):**
- Zona: ZRM3 B
- CAB: 0,8
- CAM: 1,0
- TO: 50%
- Lote mín: 600 m²
- Testada mín: 12 m
- Gabarito 6 pav / 20m (afastado) ou 4 pav / 14m (não afastado)
- Afastamento frontal: 5 m
- ICS: 0,4

### Serviços Auxiliares (Mesmo Servidor)

```
Folder: Urbanismo/
  - IU_Zoneamento_Urbano_Limites (só zona + vigência, sem números)
  - LBB_Parametros (SMD e Q como camadas espaciais)
  - LBB_AEI / LBB_AEIS / LBB_Areas_Protegidas / LBB_APAC / LBB_APP (restrições)
  - IU_Usos_e_atividades (usos por CNAE)

Basemap/Imagem:
  - pgeo3.../Basicos (mapa base)
  - pgeo3.../Imagens (imagem aérea)
```

### Status de Confiabilidade (Crítico)

| Fonte | Confiabilidade | Razão | Uso |
|-------|---|---|---|
| **RIU oficial (mapas.rio.rj.gov.br)** | ✅ Alta | Fonte oficial, sempre em vigência | Sempre — base de verdade |
| **API ArcGIS** | ⚠️ Baixa | Erro confirmado ZRM3→ZRM2 em 15/07 | Consulta rápida + conferência por lote |
| **Compilações de terceiros** | ❌ Baixa | Podem estar desatualizadas | Indicativo apenas |

**Regra:** Sempre confirmar por lote real (GeoPAL) e fonte oficial quando crítico pra cliente.

---

## Google Drive — Estrutura & Acesso

**Pasta raiz:** "Dptº de Projetos" (Sttickler)

### Subpastas Principais

```
Dptº de Projetos/
├── 000_CLIENTES/
│   ├── Bairro/
│   │   └── Cliente/
│   │       ├── Levantamento/
│   │       ├── Briefing/
│   │       ├── Estudo Preliminar/
│   │       ├── Anteprojeto/
│   │       ├── Legal/
│   │       ├── Complementares/
│   │       ├── Compatibilização/
│   │       ├── Projeto Executivo/
│   │       ├── Orçamento Executivo/
│   │       ├── Pós-Venda/
│   │       └── Arquivo/
│
├── 001_MATERIAL DE CONTROLE INTERNO/
│   ├── 001_PROCEDIMENTOS/ (POPs: Arquitetura, Legal, Complementares, Fechamento)
│   ├── 002_CERTIFICAÇÃO/ (Parceiros, Política de Precificação)
│   ├── 003_CHECKLIST/ (Validação genérica)
│   ├── 004_FORMULÁRIOS/ (Construção Nova)
│   ├── 005_PLANILHAS/ (Construção Nova)
│   ├── 006_MEMORIAIS DESCRITIVOS/ (Por Gestor)
│   └── 007_PLANILHAS DE CONTROLE/ (Entregáveis por disciplina)
│
└── 003_RELATORIOS_CONSELHO/
    └── {Ano}/{Mês}/ (Relatório Mensal de Wallenberg)
```

### Filtro de Escopo (Construção do Zero)

**Sempre que houver subpasta "Reforma", "Retrofit" ou "Home Staging", é excluída do organismo.**  
**Resto entra.**

### Acesso por Agente

| Agente | Leitura | Escrita |
|--------|---------|---------|
| **Hely** | 000_CLIENTES (pasta cliente) + 001_MATERIAL (Legal) | 000_CLIENTES (pasta cliente, seu escopo) |
| **Lúcio** (futuro) | 000_CLIENTES (pasta cliente) + 001_MATERIAL (Arquitetura) | 000_CLIENTES (pasta cliente, seu escopo) |
| **Complementares** (futuro) | 000_CLIENTES (pasta cliente) + 001_MATERIAL (Complementares) | 000_CLIENTES (pasta cliente, seu escopo) |

**Restrição:** Agente **nunca** altera compartilhamento/acesso de arquivo (proibido em qualquer circunstância).

**Cache incremental:** Usar `modifiedTime` para carregar apenas arquivos que mudaram (não toda a pasta toda vez).

---

## Vitruvius/Revit — Capacidade Real

### O Que Existe (16/07/2026)

```
MCP Oficial Autodesk: Apenas leitura (Tech Preview, deliberado pra estabelecer confiança)
Bridge Vitruvius (custom): Leitura + Escrita (testado Revit 2026)
```

### Escrita Real — Capabilities

✅ **Pode criar:**
- Nível (level)
- Parede (entre 2 pontos, em metros)
- Porta e janela (hospedadas em parede, por offset)
- Piso (contorno fechado)

✅ **Pode ler:**
- Status, model_info
- Níveis, tipos, elementos
- Ambientes (`list_rooms`)
- Detalhe de elemento

✅ **Pode editar:**
- Apagar elemento

### Coordenadas

- Sistema: metros
- X → leste / Y → norte

### GAP de Capacidade (Pendência Crítica)

❌ **Falta:** `create_room` (criar Ambiente) e `create_dimension` (cotas)

**Impacto:** Ao montar cômodo (ex: 4×3 m):
- Muros/portas/janelas/piso → automático
- Room (cálculo área, nome, acabamento no quadro) → **manual**
- Cotas alinhadas → **manual**

**Ação:** Incluir `create_room` + `create_dimension` no roadmap Vitruvius (bloqueia 100% automação de arquitetura).

### Disciplinas & Viabilidade

| Disciplina | Situação 09/07 | Por quê | Quando |
|-----------|---|---|---|
| **Compatibilização** | ✅ Pronto | Só leitura (achar interferência) | Agora |
| **Interiores** | ⚠️ Curto prazo | Pouco regulado, memorial+layout+especificação | 1-2 meses |
| **Legal** | ⚠️ Curto prazo | Compilação+checagem, não modelagem | 1-2 meses |
| **Arquitetura, Estrutura, Elétrico, Hidro, Automação, Paisagismo** | ⏳ Exige investimento | MCP terceiros (não oficial), precisa Dynamo/pyRevit | 3+ meses |

---

## LICIN 2.0 (Decreto Rio nº 55.622/2025)

### Processo de Licenciamento

1. **Requerimento:**
   - DULI (Documento Único de Licenciamento Integrado, Anexo I)
   - Declaração de responsabilidade (Anexo II)

2. **Análise técnica:**
   - SMDU confere conformidade
   - Prazo: 30 dias

3. **Emissão:**
   - Minuta da Licença
   - Guia de arrecadação
   - Quadro Explicativo de Áreas (Anexo III ou IV)
   - Termo de Responsabilidade

4. **Antes da obra:**
   - Declaração de Compatibilidade (Anexo V)

5. **Depois da obra:**
   - Habite-se (unidade nova)
   - Aceitação de Obras (modificação)

**Laço iterativo:** Se prefeitura recusa/pede ajuste → correção + reenvio até aprovar.

### PRPA (Profissional Responsável Projeto Arquitetônico)

Quem assina = **quem produziu o Anteprojeto**:
- Claudemberg (CAU 2026) se Agente interno produziu
- Arquiteto parceiro externo se ele produziu

Hely **prepara** o processo, não decide quem assina.

### Anexos Obrigatórios

- **Anexo I:** DULI (modelo fixo)
- **Anexo II:** Declaração de Responsabilidade (texto padrão)
- **Anexo III (ou IV):** Quadro Explicativo de Áreas
  - Anexo III: residencial multifamiliar, uso exclusivo, comercial
  - Anexo IV: residencial uni/bifamiliar
  - Escolha é função do tipo de ocupação

### Quadro de Áreas Obrigatório

(Conforme Anexo III/IV)

```
PAVIMENTO | DESCRICAO | AREA (m2) | OBS
Subsolo   | Garagem   | PENDENTE  | (se houver)
Térreo    | Recepção  | PENDENTE  |
Pav 1     | Escritórios| PENDENTE |
...
---
TOTAL BRUTO | | XXX |
ATE (Área Total Edificada) | | PENDENTE | (=total bruto se sem subsolo aflorado)
Máximo legal (CAM × terreno) | | XXX |
TO máxima (%) | | PENDENTE | (precisa área projeção)
Vagas estacionamento | | PENDENTE | (análise PGV/CET-Rio)
```

---

## Legislação Municipal — Hierarquia & Fontes

### Base Legal Vigente

| Documento | Emissão | Conteúdo | Fonte Confiável |
|-----------|---------|----------|---|
| **LC 270/2024** | 2024 | Plano Diretor + LUOS (uso do solo, coeficientes, gabarito) | SMDU, mapas.rio |
| **LC 274/2024** | 2024 | Alterações LUOS | SMDU, mapas.rio |
| **LC 284/2025** | 2025 | Operação Urbana Consociada (Parque Legado Olímpico) | SMDU, mapas.rio |
| **LC 198/2019** | 2019 | COES (Código de Obras) | SMDU, mapas.rio |
| **Decreto 56.561/2025** | 2025 | Usos por CNAE e zona | SMDU, mapas.rio |
| **Decreto 55.622/2025** | 2025 | LICIN 2.0 (processo de licenciamento) | SMDU, portal.rio |
| **Decreto 23.235/2003** | 2003 | Licença de demolição | SMDU |

### Decretos Setoriais (Por Bairro/Região)

| Decreto | Bairro/Zona | Conteúdo |
|---------|---|---|
| **3.046/1981** | Recreio (ZPP) | Zona de Proteção do Parque Natural |
| Diversos | Zona de Interesse | Proteção de patrimônio, APA, etc |

**Regra:** Sempre verificar se existe decreto específico pra subzona/bairro (não assume genérico).

### Órgãos & Resoluções

| Órgão | Resolução | Conteúdo |
|-------|-----------|----------|
| **CAU/BR** | Nº 21/2012 | Atribuições do arquiteto (RRT, disciplinas) |
| **CAU/BR** | Nº 51/2013+ | Resoluções técnicas atualizadas |
| **CREA/RJ** | Variadas | Atribuições do engenheiro (ART) |

### NBRs & Normas

| Norma | Conteúdo | Crítico |
|-------|----------|--------|
| **NBR 9050:2020** | Acessibilidade | Elevadores, rampas, portas |
| **NBR 6122** | Fundações rasas | Sapata, bloco, radier (CAU cobre assinatura) |
| **NBR 5410** | Instalações elétricas | Padrão residencial |
| **NBR 16783** | Reuso de água | Sistemas de captação pluvial |
| **ABNT NBR 20250** | Sustentabilidade | Selos verdes |

---

## Entregáveis por Etapa (Arquitetura)

**Planilha oficial:** `007_PLANILHAS DE CONTROLE` (Drive 001_MATERIAL)

### Estudo Preliminar
- Plantas baixas conceituais
- Cortes conceituais
- Eleição e implantação
- Renders / vídeo / apresentação **(mandatório de Lúcio)**
- Relatório de estudo

### Anteprojeto
- Plantas de nível (cotadas)
- Cortes executivos
- Fachadas (proporção real)
- Perspectiva 3D
- Especificação de materiais
- Renders / vídeo **(mandatório)**

### Projeto Legal (Hely)
- Plantas legais (cotadas, conforme exigência do LICIN)
- Implantação legal
- Planta de situação
- Cortes legais
- Fachadas legais
- Quadro de áreas (Anexo III/IV)
- Memorial descritivo
- RRT(s)

### Projeto Executivo
- Plantas de detalhamento (1:50, 1:25)
- Especificação executiva por ambiente
- Detalhes construtivos
- Cronograma de execução

---

## CAU/CREA — Atribuições Técnicas (Confirmado 10/07/2026)

### CAU (Claudemberg 2026)

**Resolução CAU/BR nº 21/2012:**

✅ **Pode assinar RRT:**
- Projeto Legal (Licenciamento)
- Projeto Estrutural (concreto, metal, madeira) — **exceto fundação profunda** (estaca)
- Projeto Elétrico predial de **baixa tensão** — padrão residencial, não alta tensão
- Projeto Hidrossanitário (água, esgoto, águas pluviais, gás canalizado)

❌ **Não pode assinar:**
- Fundação profunda (estaca) — exige CREA
- Fora de padrão residencial — exige CREA
- Projeto de interiores (não exige assinatura)

### CREA (Externo)

Necessário pra:
- Fundação profunda
- Projetos fora do padrão residencial
- Disciplinas especializadas (telemetria, sistema de prevenção incêndio, etc)

---

## Índice Comércio e Serviços (ICS) — Correção de Rótulo

**Corrigido em 20/07/2026:** ICS = **Índice de Comércio e Serviços**, não "Compensação Social".

**Aplicação:** Em zonas comerciais/mistas, pode haver exigência de área de uso comercial/serviço (% do total).

**Exemplo:** ZRM2, ICS 0,3 do CAM = se CAM 1,0, então mín 30% de comercial/serviço naquela zona específica.

**Exceção:** Uso exclusivo de saúde (CNAE 86.3) pode ter isenção dependendo de lei específica (ex: LC 270/2024, Art. 367 §1 I).

---

## Outorga Onerosa (Contrapartida CAB→CAM)

**Lei:** LC 270/2024, LC 274/2024, LC 281/2025 Art. 18

**Fórmula:**
```
Faixa de contrapartida = (CAM - CAB) × Área terreno

Exemplo: CAB 0,6, CAM 1,0, terreno 500 m²
Faixa = (1,0 - 0,6) × 500 = 200 m² adicional pagável

Preço: Fixo por m² (atualizado anualmente)
Validade: Temporária (ano fiscal)
```

**Implicação:** Pode permitir aumentar do CAB pro CAM, mas **não além do CAM** (contrapartida tem limite).

---

## Demolição & Processo Bifásico

**Corrigido em 20/07/2026:**

| Tipo | Processo | Licença |
|------|----------|---------|
| **Demolição parcial** | Modificação única | LICIN 2.0 Modificação (Anexo IV) |
| **Demolição total + construção nova** | ❌ **NÃO confirmado em LICIN 2.0** | ? |

**Pendência Hely:** Não claro se tramita em **um DULI único** ou em **dois processos** (licença demolição prévia + LICIN obra nova).

Portal Carioca Digital trata "licença de demolição" como serviço próprio + documentação (fotos, ART/RRT destruição, certidão matricula).

**Prática:** Sinalizar a Kelsen quando caso real for demolição total — não presuma nenhum dos dois caminhos.

---

## Planilha de Enviáveis — Confirmação

(De `007_PLANILHAS DE CONTROLE`)

**Confirmado 21/07/2026:** Entregável mandatório de Lúcio em Estudo Preliminar + Anteprojeto:
- ✅ Renders
- ✅ Vídeo
- ✅ Apresentação

Não é opcional; é linha da planilha oficial.

---

## Vigência e Atualização

**Feedback crítico:** Sempre atualizar legislação ao usar.

**Regra:** Substituir desatualizado pelo mais atual. Checar data de vigência antes de usar qualquer norma/parâmetro.

**Fonte de verdade:** mapas.rio.rj.gov.br é sempre mais atual que compilações externas ou cópias locais.

