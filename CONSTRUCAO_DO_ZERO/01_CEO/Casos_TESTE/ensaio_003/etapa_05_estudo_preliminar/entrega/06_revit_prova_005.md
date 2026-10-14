# 06. Revit (Vitruvius): prova de estado, desenho e bloqueios (Estudo Preliminar, Etapa 05)
## Montenegro Prates. Oscar, 14/10/2026. Caso 100% fictício.

---

## 1. Saída literal de `mcp__vitruvius__vitruvius_get_revit_status` (chamada desta execução)

```
{
  "success": true,
  "data": {
    "connected": true,
    "hasDocument": true,
    "revitVersion": "Autodesk Revit 2026",
    "documentTitle": "Projeto1",
    "documentPath": "D:\\011_VITRUVIUS\\_testes_document\\Projeto1.rvt",
    "isModified": false,
    "activeViewName": null,
    "activeViewType": null,
    "statistics": {
      "levels": 4,
      "walls": 4,
      "doors": 0,
      "windows": 0,
      "rooms": 8,
      "floors": 0
    },
    "uptime": "00:00:00",
    "uptimeSeconds": 0
  },
  "message": "Status do plugin obtido com sucesso"
}
```

**Leitura.** O plugin está conectado. O documento ativo é o arquivo de **teste** `Projeto1.rvt`, o mesmo de 13/10/2026, não um arquivo do caso Montenegro Prates. `isModified: false` no início desta execução.

---

## 2. Saída literal de `vitruvius_list_elements`

### 2.1 Categoria "Paredes" (com `fields: ["parameters"]`). Trecho literal: os 4 elementos, campos de identificação, comprimento, altura e restrições

Valores literais, mas reorganizados em uma linha por elemento. Os campos não citados estão marcados por `[...]`; a saída completa tem dezenas de parâmetros por parede. Os campos citados (inclusive os quatro de altura e restrição) foram copiados como vieram:

```
{ "success": true, "data": { "category": "Paredes", "total": 4, "count": 4, "offset": 0, "limit": 1000, "hasMore": false,
  "elements": [
    { "id": "449286", "name": "Parede padrão - 15 cm", "typeName": "Parede padrão - 15 cm", "typeId": "326842", "className": "Wall", "levelId": "324604", "area": 1.25, "length": 4,
      "parameters": { "...": "[...]", "Comprimento": 4, "Altura desconectada": 0.3, "Restrição da base": "324604", "Restrição superior": "311", "Deslocamento da base": 0, "Deslocamento superior": 0, "Delimitação de ambientes": 1 } },
    { "id": "449287", "name": "Parede padrão - 15 cm", "typeName": "Parede padrão - 15 cm", "typeId": "326842", "className": "Wall", "levelId": "324604", "area": 0.9, "length": 3,
      "parameters": { "...": "[...]", "Comprimento": 3, "Altura desconectada": 0.3, "Restrição da base": "324604", "Restrição superior": "311", "Deslocamento da base": 0, "Deslocamento superior": 0, "Delimitação de ambientes": 1 } },
    { "id": "449288", "name": "Parede padrão - 15 cm", "typeName": "Parede padrão - 15 cm", "typeId": "326842", "className": "Wall", "levelId": "324604", "area": 1.2, "length": 4,
      "parameters": { "...": "[...]", "Comprimento": 4, "Altura desconectada": 0.3, "Restrição da base": "324604", "Restrição superior": "311", "Deslocamento da base": 0, "Deslocamento superior": 0, "Delimitação de ambientes": 1 } },
    { "id": "449289", "name": "Parede padrão - 15 cm", "typeName": "Parede padrão - 15 cm", "typeId": "326842", "className": "Wall", "levelId": "324604", "area": 0.86, "length": 3,
      "parameters": { "...": "[...]", "Comprimento": 3, "Altura desconectada": 0.3, "Restrição da base": "324604", "Restrição superior": "311", "Deslocamento da base": 0, "Deslocamento superior": 0, "Delimitação de ambientes": 1 } }
  ] }, "message": "Elementos listados com sucesso" }
```

### 2.2 Categoria "Ambientes" (saída literal, todos os 8)

```
{ "success": true, "data": { "category": "Ambientes", "total": 8, "count": 8, "hasMore": false, "elements": [
  { "id": "416079", "name": "Escritório 1", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416267", "name": "cozinha 2", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416273", "name": "sala de jantar 3", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416276", "name": "sala 4", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416676", "name": "área de serviço 5", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416772", "name": "corredor 6", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "416874", "name": "Garagem 7", "levelId": "311", "className": "Room", "area": 0, "placed": false },
  { "id": "449290", "name": "TESTE OSCAR 13-10 8", "levelId": "324604", "className": "Room", "area": 10.97, "placed": true }
] }, "message": "Elementos listados com sucesso" }
```

### 2.3 Categoria "Portas" (saída literal)

```
{ "success": true, "data": { "category": "Portas", "total": 0, "count": 0, "offset": 0, "limit": 1000, "hasMore": false, "elements": [] }, "message": "Elementos listados com sucesso" }
```

### 2.4 Categoria "Janelas" (saída literal)

```
{ "success": true, "data": { "category": "Janelas", "total": 0, "count": 0, "offset": 0, "limit": 1000, "hasMore": false, "elements": [] }, "message": "Elementos listados com sucesso" }
```

---

## 3. Conferência de altura das paredes contra o pé-direito adotado

- **Altura das 4 paredes (IDs 449286, 449287, 449288, 449289): "Altura desconectada" = 0.3, restrição superior "311".** Lido como 0,30 m, o mesmo valor do defeito anotado em 13/10/2026 (registro da Etapa 04 v4, Anexo 06, B-1, e enunciado da Etapa 05, "Agentes"). Não confirmei a unidade interna do campo nesta execução; a leitura de 0,30 m segue o registro de 13/10.
- **Pé-direito adotado para o Estudo Preliminar:** não existe. Nenhuma etapa aprovada fixa o pé-direito. A conta de altura (05 E-25) depende de pé-direitos a definir (PDT, PDS, laje e cobertura, com teto de +11,70 m).
- **Resultado:** a altura das paredes **não está conforme** a qualquer pé-direito plausível do programa (2,50 m de permanência prolongada, COE Art. 12, [nv]). **Não entreguei modelo com essa altura como correto.** Não corrigi, porque o arquivo é de teste e a correção muda elementos que não são meus neste caso (ver §5).
- **Ambiente de teste:** "TESTE OSCAR 13-10 8" mantém o sufixo " 8" anotado em 13/10. Mesmo defeito, não corrigido.
- **Ambientes 416079 a 416874 (7):** não colocados (`placed: false`, área 0), herdados do template do arquivo. Não são deste caso e não foram tocados.
- **Janelas (0) e portas (0):** nenhuma abertura criada.

---

## 4. Desenhos do EP: estado "não desenhado" com motivo

| Entrega do enunciado | Estado | Motivo |
|---|---|---|
| Implantação (norte, acessos, recuos, permeável e impermeável, cotas de nível, projeção da topografia) | **Não desenhado** | Norte não medido (T15). Topografia sem curvas, RN e perfil natural (T1–T4). Divisa com o Lote 16 não locada (T5). Sem o polígono real do lote, qualquer envelope seria retangular inventado |
| Planta do pavimento térreo | **Não desenhado** | Sem metragem por ambiente (Briefing, Anexo 02 §1). Térreo depende de "a", n e da edícula, sem decisão |
| Planta do pavimento superior | **Não desenhado** | Idem, e depende de pé-direito e laje (05 E-25) |
| Corte longitudinal | **Não desenhado** | Cota de soleira só prevista (+3,20). Topo +11,70 depende de estrutura |
| Corte transversal | **Não desenhado** | Idem; a projeção natural do terreno não existe |
| Elevação frontal | **Não desenhado** | Esquadrias não definidas; varanda frontal sem decisão (05 E-17) |
| Elevação de fundos | **Não desenhado** | Lago e APP sem decisão (H0 × H1); piscina sem cota |

**Motivo central, em uma frase.** O partido e as áreas dependem de decisões ainda não tomadas (n cobertas, "a", edícula, varanda frontal, APP, SMD) e de metragens que nenhuma etapa aprovada fixou. Desenhar agora exigiria inventar áreas e alturas.

**Bloqueio de ferramenta.** Não houve bloqueio de ferramenta nesta execução. As ferramentas de leitura respondem. O bloqueio é de conteúdo: falta programa definido.

---

## 5. Descrição em texto, com cotas, do que o modelo teria de representar (sem desenho)

**Implantação (texto).** Referencial O = vértice frente-esquerda, na face do muro do Lote 16. x ao longo da testada (14,29 m de menor largura). y da rua para os fundos (40,00 m). Envelope H0: x 2,50 a 11,79; y 6,00 a 35,00 (9,29 × 29,00 = 269,41 m²). Faixa de fundos: y 35,00 a 40,00 (5,00 m). Frontal: y 0 a 6,00 (6,00 m). Linha de H1: y = 22,00 (APP de 30 m da margem; margem do lago a y ≈ 52,00). Saliência de jardineira até y = 5,60 (Dec. 3.046 XIV). Edícula: face em x = 13,49. Árvores (1 ipê e 2 amendoeiras) no frontal, locação não consta (T11).

**Cortes e cotas de altura (texto).** Soleira prevista +3,20. Topo máximo +11,70 (= 3,20 + 8,50). Térreo: piso em +3,20 (soleira = cota de implantação, Etapa 03 Peça 1 §3, [nv]). Superior: sem cota. Piscina: borda e fundo não constam; fundo 0,70 m abaixo do NA 0,90 m (05 E-18). Terreno natural e aterro: não constam (T4).

**Elevações (texto).** Fachada frontal: recuo 6,00 m do alinhamento; balanço frontal não admitido como premissa (05 E-17); esquadrias não definidas. Fachada de fundos: afastamento 5,00 m; faixa verde comum de 12 m além da divisa (dossiê 5.5); lago a 12,00 m da divisa, margem em y ≈ 52,00. Laterais: 2,50 m das divisas. Esquadria de fachada poente (corretor): sem dado de orientação.

**Quando houver Revit com a geometria certa.** Pré-requisitos: (i) polígono real do lote (T5); (ii) cota da rua e RN (T2); (iii) pé-direitos fixados (Baumgart, Oscar); (iv) decisão de n, "a", edícula e varanda frontal; (v) APP definida (H0 ou H1).

---

## 6. Itens que não fiz (e por quê)

- Não criei nenhuma parede, ambiente, porta ou janela.
- Não apaguei as 4 paredes de teste, o ambiente de teste nem os 7 ambientes do template. São de teste e não são meus neste caso. Decisão de Lúcio.
- Não consultei níveis por nome (get_levels): o nível 311 não está nomeado nesta execução.
- Não salvei o documento. `isModified` continua `false` no fim desta execução.

---

Oscar, 14/10/2026. Contagem de palavras: pendente de Wallenberg.
