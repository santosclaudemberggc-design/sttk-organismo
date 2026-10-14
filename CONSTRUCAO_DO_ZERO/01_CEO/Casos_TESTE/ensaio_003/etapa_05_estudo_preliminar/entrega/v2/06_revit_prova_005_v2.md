# 06 v2. Revit (Vitruvius): desenho esquemático, prova e lacunas (Estudo Preliminar, Etapa 05, Entrega 2)
## Montenegro Prates. Oscar, 14/10/2026. Caso 100% fictício. Análise preliminar, não é entregável final. Gate da Coordenação (Claudemberg) pendente.

Responde ao parecer do Bardi (`parecer_bardi.md`, "O que corrigir", itens 2, 3 e 6) e à regra nova de Claudemberg ("programa não definido não é motivo para não desenhar"). A v1 (`entrega\06_revit_prova_005.md`) fica intacta.

---

## 0. Conclusão

1. **Desenhei o esquemático** no arquivo `entrega\v2\EP_Montenegro_003_v2_r1.rvt`: limite do lote, afastamentos cotados, volume do térreo e do superior com paredes externas e internas principais, 12 ambientes com nome e área, 3 portas, 6 janelas, 2 lajes, cobertura, 3 faixas permeáveis, 2 cortes, 2 elevações e 2 folhas A1 (`SI_FOLHA_ ABNT`).
2. **Altura das paredes conferida e correta:** 3,00 m, com prova de unidade (`valorBruto` 9,8425 pés = 3,00 m). O defeito de 0,30 m reapareceu só nos muros do lote (topo preso ao nível seguinte) e foi corrigido com "Deslocamento superior" de 0,70 (prova em §3).
3. **O sufixo " 8" não é defeito do nome.** É o parâmetro "Número" do ambiente, que o `list_elements` mostra colado ao nome. Troquei os números para T01 a T06 e S01 a S06 (prova em §3).
4. **Todas as 9 cotas foram conferidas contra a geometria. Todas batem.** Apaguei 3 cotas que estavam certas pela geometria mas eram enganosas ou ficaram obsoletas (§4).
5. **Lacunas de ferramenta:** escada, vão de laje, perspectiva 3D, linha de norte, texto e símbolo de anotação, curvas de nível e portão de garagem (§6).
6. **Lacunas de conteúdo, marcadas no nome dos ambientes:** "a" (P-a), uso do escritório (P-escritório), acessibilidade da suíte térrea, áreas a definir com o cliente e pé-direito de 7 m (§5).

---

## 1. Arquivo usado e documento ativo (passo 1 da ordem)

- **Abrir do template:** `vitruvius_document` com acao abrir e modo novo_projeto_do_template, em `D:\007_MATERIAIS\001_Revit\002_Templates\ARQ.Sttk - 2026.rte`. Retorno literal: `"titulo": "Projeto1", "caminho": "", "ativo": false, ... "aviso": "Projeto criado em segundo plano: não ficou ativo. As ferramentas do Vitruvius operam no documento ativo."` Esse documento continua aberto em segundo plano, **sem salvar**. Não o fechei e não gravei nada no .rte.
- **Caminho alternativo da ordem:** `salvar_copia` do ativo `D:\011_VITRUVIUS\_testes_document\Projeto1.rvt`.
  - 1ª tentativa: `Error: pasta não existe: ...\entrega\v2. Não crio pasta sozinho.` Criei a pasta gravando este arquivo e repeti a chamada.
  - 2ª tentativa: `"caminhoGravado": "...\\entrega\\v2\\EP_Montenegro_003_v2.rvt", "tamanhoBytes": 17473536, "aviso": "Revit 2026 não tem SaveCopy: o documento ativo passou a ser a cópia gravada."`
- **Conferência com `get_document_info`:** `"name": "EP_Montenegro_003_v2", "path": "...\\entrega\\v2\\EP_Montenegro_003_v2.rvt"`, com 4 paredes e 8 ambientes (os de teste).
- **Elementos de teste apagados na cópia:** ambiente 449290 (`"elementosRemovidos": ["449290","449291"]`; 449291 é a etiqueta do ambiente) e as paredes 449286, 449287, 449288 e 449289 (1 elemento removido em cada).
- **Projeto1.rvt no disco:** a cópia foi feita antes das exclusões, e o ativo passou a ser a cópia. Pelo aviso da ferramenta, o .rvt de teste não recebeu as exclusões. **Não verifiquei isso abrindo o Projeto1.rvt.**
- **Outro documento aberto no Revit,** que não toquei: `IRNBR - MCR - V001.rvt`, da pasta `D:\012_MARCENARIA\Clientes\...` (caso real, fora do ensaio), `"ativo": false, "modificado": false`.
- **Versão final salva como cópia nova** (sem sobrescrever): `"caminhoGravado": "...\\entrega\\v2\\EP_Montenegro_003_v2_r1.rvt", "tamanhoBytes": 17580032, "dataHora": "2026-10-14T11:52:32"`. O ativo agora é o r1. O `EP_Montenegro_003_v2.rvt` guarda o estado logo depois da cópia, ainda com os elementos de teste.
- **Arquivo de entrega: `EP_Montenegro_003_v2_r1.rvt`.**

## 2. Cenário desenhado (passo 2 da ordem)

- **Cenário:** H0 sob M-b, a premissa vigente. Fonte: v1 `03_cenarios_H0_H1_005.md`, linha 14 ("H0-M-b (premissa vigente)"). A geometria vem da v1 `06_revit_prova_005.md`, linha 119.
- **Referencial:**
  - Origem O no vértice frente-esquerda (divisa com o Lote 16).
  - Eixo x ao longo da testada, de 14,29 m.
  - Eixo y da rua para os fundos, até 40,00 m.
  - O lote é desenhado como retângulo de 14,29 × 40,00 = 571,60 m². A área medida é de 571,80 m², e o polígono real está pendente (T5).
- **Volume:**
  - Faces externas em x de 2,50 a 11,79 e em y de 6,00 a 30,62, ou seja, 9,29 × 24,62 = **228,72 m² de projeção (P)**. É exatamente a TO de 40% de 571,80 (v1 02 B; Regramento Art. 5º).
  - 2 pavimentos iguais, totalizando **457,44 m² de área construída (Co)**. Esse valor é igual ao teto computável sob M-b, porque sob M-b tudo o que é coberto entra.
  - O volume não usa a faixa de y 30,62 a 35,00 do envelope: a TO limita antes do afastamento de fundos.
- **Níveis do template (não alterados):**
  - Terreno 0,00 (id 324604).
  - Páv. térreo 0,30 (id 311): a soleira, que no referencial do condomínio é +3,20, prevista.
  - Páv. Superior 3,30 (id 694).
  - Cobertura 6,30 (id 323714).
  - Os pé-direitos não foram fixados em nenhuma etapa. O piso a piso de 3,00 m do template é **hipótese esquemática**, não premissa.
- **Altura, conta escrita:**
  - Da soleira (0,30) ao topo da cobertura (6,30 + 0,40 = 6,70): **6,40 m**, abaixo do limite de 8,50 m (Regramento Art. 7). A folga é de 2,10 m.
  - Em cota absoluta: +3,20 + 6,40 = +9,60, abaixo do topo máximo de +11,70.
  - A cota vertical gerada no corte confirma: 0,15 / 2,85 / 0,15 / 3,00 / 0,40, total de 6,55 m, medido da face inferior da laje do térreo (0,15).
  - **Divergência:** o tipo "LAJE 10 cm" aparece com 0,15 m de espessura na cota.
  - Pé-direito livre do térreo no modelo: 2,85 m. O pé-direito de 7 m da sala (pedido de 13/10) **não foi desenhado**: com pavimento sobre a sala, 7,00 + 2,50 = 9,50 m, acima de 8,50 m (v1 01 §4).

## 3. Elementos desenhados, com ids e prova lida de volta

### 3.1 Paredes: 20, saída de `list_elements` (Paredes)

| Id | Nível | Tipo | Eixo (m) | Comprimento (m) | Papel |
|---|---|---|---|---|---|
| 449352 | Térreo (311) | Parede padrão - 15 cm | y = 6,075; x 2,575 a 11,715 | 9,14 | Externa, frente |
| 449353 | Térreo | idem | x = 11,715 | 24,47 | Externa, direita |
| 449354 | Térreo | idem | y = 30,545 | 9,14 | Externa, fundos |
| 449355 | Térreo | idem | x = 2,575 | 24,47 | Externa, esquerda |
| 449385 | Térreo | parede interna - 15 cm | y = 11,25 (movida +0,25 de 11,00) | 9,14 | Garagem × suíte e serviço |
| 449386 | Térreo | idem | y = 17,00 | 9,14 | |
| 449387 | Térreo | idem | y = 23,00 | 9,14 | |
| 449388 | Térreo | idem | x = 7,50; y 11,25 a 23,00 | 11,75 | |
| 449356 a 449359 | Superior (694) | Parede padrão - 15 cm | mesmo contorno do térreo | 9,14 / 24,47 | Externas |
| 449389 | Superior | parede interna - 15 cm | y = 13,00 | 9,14 | |
| 449390 | Superior | idem | y = 20,00 | 9,14 | |
| 449391 | Superior | idem | x = 7,50; y 6,075 a 20,00 | 13,925 | |
| 449392 | Superior | idem | x = 7,15; y 20,00 a 30,545 | 10,545 | |
| 449393 a 449396 | Terreno (324604) | Genérico - 90 mm Tijolo | face interna sobre a divisa: eixo em −0,045 e 14,335 (x); −0,045 e 40,045 (y) | 14,38 / 40,09 | **Limite do lote**, marcado em "Comentários" (449396: "divisa Lote 16, pendente T5") |

- **O nome passado ao `create_wall` é descartado,** como já registrado em 09/10. A resposta devolve sempre o nome do tipo. A marcação das paredes do lote ficou no parâmetro "Comentários".
- **Prova de altura e unidade (`get_parameter` "Altura desconectada"):**
  - 449352 (térreo): `"valorFormatado": "3,00", "valorBruto": 9.842519685042632` (9,8425 pés × 0,3048 = 3,00 m).
  - 449356 (superior): `"3,00"`, 9.842519685036358.
  - **449393 (muro do lote), antes da correção:** `"valorFormatado": "0,30", "valorBruto": 0.9842519685039396`. Pedi 1,0 e a ferramenta prendeu o topo ao "Páv. térreo" (0,30). **O defeito de 13/10 se reproduz** sempre que a altura pedida difere da distância até o nível seguinte.
  - **Correção:** "Deslocamento superior" = 0,70 nas 449393 a 449396 (4 de 4 com sucesso). Releitura da 449393: `"valorFormatado": "1,00", "valorBruto": 3.2808399685039396`.
  - Todas as paredes da casa saíram com 3,00 m, igual ao piso a piso do template. Coerente com o modelo, que mede 2,85 m livres no térreo.

### 3.2 Ambientes: 12 novos

Áreas internas devolvidas pelo Revit, regime de área útil interna (não é área computável). "Número" conferido na releitura de `list_elements`.

| Id | Nº | Nome exato | Área (m²) | Conferência (vãos internos pela cota) |
|---|---|---|---|---|
| 449397 | T01 | GARAGEM n vagas - a pendente (P-a) | 45,17 | 8,99 × 5,025 = 45,17 |
| 449398 | T02 | SUITE TERREA D. LOURDES - acessib. pendente | 26,74 | 4,775 × 5,60 = 26,74 |
| 449399 | T03 | SERVICO + DEPENDENCIA - area a definir c/ cliente | 22,76 | 4,065 × 5,60 = 22,76 |
| 449400 | T04 | COZINHA + GOURMET - area a definir c/ cliente | 27,93 | 4,775 × 5,85 = 27,93 |
| 449401 | T05 | CIRCULACAO + ESCADA (escada nao modelada - lacuna) | 23,78 | 4,065 × 5,85 = 23,78 |
| 449402 | T06 | ESTAR JANTAR - PD 7m nao cabe c/ pav. sobre (pendente) | 66,48 | 8,99 × 7,395 = 66,48 |
| 449403 | S01 | SUITE 2 - area a definir c/ cliente | 32,35 | 4,775 × 6,775 = 32,35 |
| 449405 | S02 | HOME OFFICE - uso pendente Kelsen (P-escritorio) | 27,54 | 4,065 × 6,775 = 27,54 |
| 449406 | S03 | HOME CINEMA - area a definir c/ cliente | 32,71 | 4,775 × 6,85 = 32,71 |
| 449407 | S04 | CIRCULACAO + ESCADA SUP (vao de laje nao modelado - lacuna) | 27,85 | 4,065 × 6,85 = 27,85 |
| 449408 | S05 | SUITE 3 - area a definir c/ cliente | 46,00 | 4,425 × 10,395 = 46,00 |
| 449409 | S06 | SUITE 4 (master) - area a definir c/ cliente | 45,89 | 4,415 × 10,395 = 45,89 |

- **Somas de área útil interna:** térreo 212,83 m² (sem a garagem, 167,66); superior 212,34 m².
- **Nada disso é programa aprovado.** As áreas resultam da divisão esquemática do volume. O cliente define as metragens (P-l do enunciado, que não existe no Briefing v4; ver parecer E1).
- **Garagem:** a profundidade interna de 5,025 m acomoda uma vaga de 5,00 m (COES Art. 29 I, p. 15, lido na v1 [nv nesta execução]). Na largura de 8,99 m cabem **3 vagas de 2,50 m, não 4**, e não há manobra interna. A garagem de 4 vagas (decisão C1) **não está resolvida no desenho.** Depende de "a", de n e da alternativa B (abrigo lateral). Fica marcada no nome do ambiente.
- **Ambientes do template:** 7, não colocados (416079 a 416874, área 0). Não foram tocados.
- **Sufixo numérico:** `create_room` gera o "Número" sequencial, e `list_elements` mostra "Nome Número". Prova: depois de `set_parameter` em "Nome", o 449397 continuava "... (P-a) 9". Depois de "Número" = "T01", passou a "GARAGEM n vagas - a pendente (P-a) T01". O " 8" de 13/10 era o número, não um defeito do nome.

### 3.3 Aberturas: `list_elements` com 3 portas e 6 janelas

| Id | Tipo | Parede hospedeira | Posição | Observação |
|---|---|---|---|---|
| 449410 | 19 - CE - Porta Pivotante | 449353 (direita) | offset 13,9, y ≈ 19,98 | **Acesso social pela lateral direita**, no afastamento de 2,50 m |
| 449424 | Porta envidraçada de correr quádrupla 3520 × 2180 mm | 449354 (fundos) | offset 4,5 | Estar para os fundos |
| 449426 | M_Folha única 0915 × 2134 mm | 449386 (y = 17) | offset 4,3 | Suíte térrea: vão de 0,915 m. Atende ao mínimo da NBR 9050 **não verificado**; a NBR 9050:2020 não foi lida (pendente). A porta abre para a cozinha: a circulação da suíte não está resolvida |
| 449428, 449430 | Janela de correr - 2 Painéis | 449355 (esquerda), térreo | offsets 16,5 e 10,5; peitoril 1,1 | Suíte térrea e cozinha |
| 449431, 449432 | idem | 449358 (fundos), superior | offsets 2,3 e 6,8 | Suítes 3 e 4 |
| 449433, 449434 | idem | 449356 (frente), superior | offsets 2,4 e 7,0 | Suíte 2 e home office |

- **Portão da garagem:** não há tipo no template (pedido ao Tenreiro de 09/10). O vão da frente está fechado por parede. Lacuna.
- **Esquadria de piso a teto a poente (pedido do corretor):** não desenhada. A orientação não está confirmada (T15).

### 3.4 Pisos e cobertura

| Id | Tipo | Nível | Área (m²) | Regime |
|---|---|---|---|---|
| 449437 | LAJE 10 cm | Térreo | 228,72 | P (projeção) |
| 449445 | LAJE 10 cm | Superior | 228,72 | Co |
| 449487 | Cobertura "Genérico - 400 mm" (plana, v1 da ferramenta), marca "COBERTURA TECNICA (sem terraco - Regramento Art. 7) inclinacao pendente" | Cobertura | 228,72 | Não computável, sem artigo citado: pendência |
| 449453 | grama .30 (fundos, y 30,62 a 40,00) | Terreno | 134,04 | Pe (esquemático) |
| 449467 | grama .30 (lateral esquerda) | Terreno | 61,55 | Pe (esquemático) |
| 449477 | grama .30 (lateral direita) | Terreno | 61,55 | Pe (esquemático) |

- **Soma permeável modelada:** 257,14 m², acima do mínimo de 142,95 m² (25%).
- **O que ainda vai consumir essa área:** piscina, deck, acesso lateral e frontal. Nenhum desses foi locado.
- **SMD continua com dois valores,** 57,18 (TO 50%) e 68,62 (TO 40%), sem escolha (P-SMD, Kelsen).
- **Faixa frontal (y de 0 a 6):** não modelada. As árvores não estão locadas (T11), e a vaga descoberta no frontal não é solução sem decisão do Gate (errata de 08/10).

### 3.5 Vistas e folhas: nomes exatos

| Id | Nome exato | Tipo | Conteúdo |
|---|---|---|---|
| 438266 | EP. Terreno | Planta (template) | **Implantação**: lote, volume e faixas permeáveis |
| 438276 | EP. Térreo | Planta (template) | Planta do térreo |
| 438286 | EP. Superior | Planta (template) | Planta do superior |
| 449503 | CORTE AA - LONGITUDINAL (EP v2) | Corte, linha x = 7,00, y de −2 a 42 | Profundidade 6, base −1, topo 10 |
| 449512 | CORTE BB - TRANSVERSAL (EP v2) | Corte, linha y = 20,00, x de −2 a 16,3 | idem |
| 449522 | ELEVACAO FRONTAL (EP v2) | Elevação, marcador 449520 em (7,15; −6), direção "north" | Escala 100 |
| 449532 | ELEVACAO FUNDOS (EP v2) | Elevação, marcador 449530 em (7,15; 46), direção "south" | Escala 100 |

- **"north" e "south" são o norte de projeto do Revit (+y), não o norte verdadeiro.** O norte verdadeiro está **pendente (T15)**.
- **Folha 449551, "EP-01 - EP v2 - IMPLANTACAO E PLANTAS (ESQUEMATICO) - NORTE PENDENTE T15".**
  - Selo A1 da família "SI_FOLHA_ ABNT " (seloId 449276, instância 449556), folha de 0,841 × 0,594.
  - Viewports: 449557 (EP. Terreno, em 0,15; 0,32), 449558 (EP. Térreo, em 0,38; 0,32), 449559 (EP. Superior, em 0,58; 0,32).
- **Folha 449560, "EP-02 - EP v2 - CORTES E ELEVACOES (ESQUEMATICO) - TOPOGRAFIA PENDENTE".**
  - Mesmo selo (instância 449565).
  - Viewports: 449566 (corte AA, em 0,30; 0,45), 449567 (corte BB, em 0,65; 0,45), 449568 (frontal, em 0,20; 0,18), 449569 (fundos, em 0,50; 0,18).
- **Sobreposição dos viewports e escala de cada vista: não verificados.** A ferramenta não devolve a caixa do viewport. É preciso conferência visual (Claudemberg ou Lúcio).

## 4. Cotas: só `dimension_facade` e `dimension_vertical`, cada uma conferida

`dimension_wall` e `dimension_room` não foram usadas.

| Id | Vista | Segmentos devolvidos (m) | Geometria esperada | Situação |
|---|---|---|---|---|
| 449540 | EP. Terreno, x | 0,09 / 2,455 / 0,15 / 8,99 / 0,15 / 2,455 / 0,09 | Muro de 90 mm com eixo na divisa: face interna em 0,045, afastamento de face a face 2,455 | Certa pela geometria, mas **enganosa** (o afastamento se mede da divisa). **Apagada.** Os muros foram deslocados 0,045 para fora |
| 449541 | EP. Terreno, y | 0,09 / 5,955 / ... / 9,335 / 0,09 | idem | **Apagada**, pelo mesmo motivo |
| 449542 | EP. Terreno, x | 0,09 / **2,50** / 0,15 / 8,99 / 0,15 / **2,50** / 0,09 (total 14,47) | Face interna do muro em 0 e em 14,29; casa de 2,50 a 11,79 | **Confere.** Afastamentos laterais de 2,50 |
| 449543 | EP. Terreno, y | 0,09 / **6,00** / 0,15 / 24,32 / 0,15 / **9,38** / 0,09 (total 40,18) | Frente de 0 a 6,00; casa de 6,00 a 30,62; fundos de 30,62 a 40,00 | **Confere.** Frontal de 6,00; fundos de 9,38 (≥ 5,00) |
| 449544 | EP. Térreo, y | ... 4,775 ... | Parede em y = 11,00 | Certa, mas obsoleta depois que a parede 449385 foi movida. **Apagada** |
| 449545 | EP. Térreo, x | 0,15 / 4,775 / 0,15 / 4,065 / 0,15 (total 9,29) | Vãos de 2,65 a 7,425 e de 7,575 a 11,64 | **Confere** |
| 449548 | EP. Térreo, y | 0,15 / 5,025 / 0,15 / 5,60 / 0,15 / 5,85 / 0,15 / 7,395 / 0,15 (total 24,62) | Vãos de 6,15 a 11,175; 11,325 a 16,925; 17,075 a 22,925; 23,075 a 30,47 | **Confere** |
| 449546 | EP. Superior, y | 0,15 / 6,775 / 0,15 / 6,85 / 0,15 / 10,395 / 0,15 (total 24,62) | Vãos de 6,15 a 12,925; 13,075 a 19,925; 20,075 a 30,47 | **Confere** |
| 449547 | EP. Superior, x | 0,15 / 4,775 / 0,15 / 4,065 / 0,15 (total 9,29) | Parede em x = 7,50 | **Confere.** Não cota a parede em x = 7,15 (suítes 3 e 4) |
| 449549 | Corte AA, vertical | 0,15 / 2,85 / 0,15 / 3,00 / 0,40 (total 6,55) | Laje do térreo de 0,15 a 0,30; superior a 3,30; cobertura de 6,30 a 6,70 | **Confere** |
| 449550 | Corte BB, vertical | idem | idem | **Confere** |

**Cotas de nível (spot elevation):** não criadas. A cota de soleira de +3,20 é prevista, sem referencial confirmado, e a cota da rua está pendente (P-k/T2). No modelo, o térreo fica em 0,30 em relação ao "Terreno", que é um referencial do template, não do levantamento.

## 5. Lacunas de conteúdo, marcadas no desenho e no texto

| Lacuna | Onde está marcada | Dono |
|---|---|---|
| Norte verdadeiro, "pendente (T15)" | Nome da folha EP-01 (não há tool de símbolo de norte) | Topógrafo |
| Topografia natural, curvas, RN e cota da rua | Nome da folha EP-02; os cortes mostram só o nível "Terreno" plano | Topógrafo (T1 a T4); P-k |
| Polígono real do lote (571,80 × 571,60 do retângulo) | "Comentários" da parede 449393; divisa com o Lote 16 na 449396 | Topógrafo (T5) |
| "a" e n vagas; 4 vagas não cabem lado a lado em 8,99 m | Nome do ambiente T01 | Hely via Kelsen (P-a); cliente (n) |
| Uso do home office | Nome do ambiente S02 | Kelsen (P-escritório) |
| Acessibilidade da suíte térrea: porta de 0,915 m; giro e corredor não verificados; NBR 9050:2020 não lida | Nome do ambiente T02 | Lúcio (norma); Kelsen (P-m) |
| Metragem por ambiente | "area a definir c/ cliente" nos nomes | Cliente |
| Sala com pé-direito de 7 m | Nome do ambiente T06 | Lúcio; Baumgart |
| Inclinação da cobertura | Marca da cobertura 449487 | Oscar e Baumgart (Etapa 06) |
| Piscina, deck, edícula e árvores | Não desenhados | Cliente; Baumgart e Cardozo (laudo da piscina) |
| H1 (APP) | Não desenhado: a linha de y = 22,00 não tem tool de linha de referência | SMAC/SPU via Kelsen |

## 6. Lacunas de ferramenta (o que a ferramenta não faz), com a prova

| Item | Prova |
|---|---|
| Escada | Não existe tool de escada na lista do Vitruvius desta sessão (prefixo `mcp__vitruvius__vitruvius_`: create_wall, create_arc_wall, create_floor, create_roof, create_room, create_rectangular_room, create_door, create_window, create_section, create_elevation, create_sheet, create_grid, create_level, create_topography, create_spot_elevation, create_group, create_schedule, create_linked_model, create_element_type, dimension_*, entre outras). Nenhuma "stair". Não chamei: não há o que chamar |
| Vão de laje (shaft/opening) | create_floor aceita só um contorno ("boundary": lista de pontos), sem furo. Nenhuma tool de abertura. Lacuna |
| **Perspectiva 3D** (item 6 do parecer) | Não há tool de vista 3D nem de câmera na lista. **Reportado a Lúcio como lacuna de ferramenta.** Perspectiva de apoio: Burle, com as ferramentas dele |
| Símbolo de norte, texto e linha de detalhe | Não há tool de anotação de texto, de símbolo nem de linha de modelo ou de detalhe. As lacunas ficaram no nome de ambiente, no nome da folha e em "Comentários" |
| Curvas de nível | create_topography existe, mas não há pontos levantados (T1 a T4). Não inventei pontos |
| Cobertura inclinada | create_roof: "v1: plana" (descrição da tool) |
| Selo pelo nome | `create_sheet` com `selo: "A1"` e `familia: "SI_FOLHA_ ABNT "` deu `Error: selo 'A1' não existe. Selos do projeto: ... A1 (449276, família SI_FOLHA_ ABNT ) ...`. Contornei com `seloId` 449276, lido do `listar_selos`. É o mesmo selo, pelo id. Defeito de casamento de nome a reportar ao dono do Vitruvius (provável espaço final no nome da família) |
| Documento novo do template não fica ativo | Aviso literal em §1. Limitação conhecida |
| Nome de parede descartado | Retorno de create_wall: `"name": "Parede padrão - 15 cm"` em todas |

## 7. NBR 6492:2021, item 5.4 (item 2 do parecer)

**Correção.** A NBR 6492:2021 **está no acervo**, em `D:\008_Normas ABNT\001_ABNT\04_Desenho_Tecnico\NBR 6492-2021 Representacao de Projetos de Arquitetura.pdf`. Li nesta execução as páginas 15 a 17 do PDF (impressas 7 a 9): 5.4 inteiro (5.4.1 a 5.4.3), mais o fim do 5.1, o 5.2, o 5.3 e o 5.5.

Na v1 (`entrega\07_declaracao_leitura_lacunas_005.md`, linha 89) eu escrevi "só a Skill (Grep de 3 linhas). Texto integral não lido". Isso fica substituído por esta seção. A v1 não foi editada. A frase "não está no acervo" na v1 refere-se à NBR 9050:2020 (07, linhas 88 e 112), e **essa continua verdadeira**: a NBR 9050:2020 não foi lida, segue pendente, e não reconstruo o texto dela.

- **5.4.1 (p. 8 impressa):** "Concepção inicial do projeto arquitetônico, no qual se especificam funções, usos, formas e dimensões para os ambientes, bem como elementos construtivos e componentes principais do projeto. Podem-se apresentar várias versões..."
- **5.4.3 (p. 9):** memorial justificativo **opcional**.

**5.4.2, item a item, contra o meu desenho:**

| Item | O que a norma pede (p. 8 impressa, PDF p. 16) | Atende? | Prova / lacuna |
|---|---|---|---|
| a) Planta de implantação | "deve indicar norte, escala, vias de acesso, acesso principal ao objeto arquitetônico, platôs e taludes principais, perímetro do terreno, recuos e afastamentos, denominação das edificações, indicação de áreas cobertas e estacionamentos, cotas gerais e cotas de nível principais; recuos, projeção da(s) cobertura(s) e áreas permeáveis e impermeáveis" | **Parcial** | Perímetro (449393 a 449396), afastamentos cotados (449542 e 449543), projeção da cobertura (449487), permeáveis (449453, 449467, 449477) e acesso principal (porta 449410, lateral direita): sim. Norte: **pendente (T15)**, só no nome da folha. Escala: a da vista do template, não conferida. Via de acesso e platôs/taludes: não (sem topografia). Estacionamento: sim, como ambiente T01 no térreo, mas não aparece na vista do nível Terreno como área marcada. Impermeável: não modelado. Cotas de nível: não (soleira prevista, rua pendente) |
| b) Plantas dos pavimentos | "norte, escala, acessos, vedos internos e externos, esquadrias (portas e janelas), elementos estruturais principais, identificação dos ambientes, espaços de circulação, áreas de serviços, áreas funcionais e técnicas; projeção de níveis superiores e da cobertura, cotas gerais e cotas de nível principais" | **Parcial** | Vedos, esquadrias, ambientes, circulação, serviço e cotas gerais (449545, 449548, 449546, 449547): sim. Norte: pendente. Elementos estruturais: não (Baumgart, Etapa 06). Projeções e cotas de nível: não |
| c) Cortes gerais | "escala, elementos estruturais principais, vedos internos e externos, esquadrias, identificação dos ambientes representados, cobertura com indicação da respectiva inclinação, cotas gerais e cotas de nível principais, eixos do projeto, relevo construído e projeção da topografia natural" | **Parcial** | 2 cortes (449503 e 449512), vedos, lajes, cobertura e cota vertical (449549 e 449550): sim. Inclinação da cobertura: não (tool só faz plana; "inclinação pendente"). Topografia natural: **pendente** (T1 a T4). Eixos: não (create_grid existe, mas não criei; pendência minha para a próxima versão). Identificação dos ambientes e esquadrias no corte: não verificado visualmente |
| d) Elevações | "escala(s), vedos externos, esquadrias (portas e janelas), elementos estruturais (quando aparentes), relevo, cotas de nível principais, cobertura (quando aparente)" | **Parcial** | 2 elevações (449522 e 449532), vedos, janelas da frente (449433, 449434) e dos fundos (449424, 449431, 449432), cobertura: sim. Relevo e cotas de nível: não |
| e) Detalhes construtivos, "quando necessário" | — | Não aplicável nesta etapa | Nenhum detalhe necessário identificado |

## 8. Checklist de entrega do Oscar, para a Entrega 2 (`checklist_entrega_oscar.md`)

### (a) Herança

| # | Parâmetro | Origem aprovada | Valor e regime | Onde está nesta entrega | Se não está |
|---|---|---|---|---|---|
| 1 | Área de cálculo | Etapa 03 v8 C-1 (via v1 01 §1, linha 27) | 571,80 m² (T) | §2 (retângulo de 571,60, aproximação) | Polígono real: T5 |
| 2 | TO de 40% | Etapa 01, linha 29 (via v1 01 §1, linha 30) | 228,72 m² (P) | §2; laje 449437 = 228,72 | — |
| 3 | Afastamentos 6,00 / 2,50 / 5,00 | Etapa 01, linhas 33 a 35 | m | Cotas 449542 e 449543 (6,00 / 2,50 / 2,50 / 9,38) | — |
| 4 | Altura de 8,50 m da soleira; 2 pavimentos | Etapa 01, linhas 30 e 31 | m | §2 (6,40 m) | — |
| 5 | Cobertura só técnica | Etapa 01, linha 32 | — | Marca da 449487 | — |
| 6 | Permeável de 142,95 m² | Etapa 01, linha 36 | Pe | §3.4 (257,14 modelado) | — |
| 7 | Sem subsolo | Etapa 01, linha 37 | — | Nenhum elemento abaixo do Terreno | — |
| 8 | Envelope H0 de 9,29 × 29,00 | Etapa 03 v8 C-2 | P | §2 (9,29 de largura) | — |
| 9 | H1, 9,29 × 16,00 | Etapa 03 v8 C-3/C-6 | P | §5 | Não desenhado (sem tool de linha) |
| 10 | 4 vagas, "a" sem valor | Etapa 03 v8 Adendo §4 | G | T01 | 4 vagas não resolvidas no desenho |
| 11 | Soleira de +3,20 prevista | Etapa 01, linha 41 | m | §2, §4 | Referencial não confirmado |
| 12 | Vaga descoberta no frontal não é solução | Errata de 08/10 | — | §3.4 (frontal não modelado) | — |
| 13 | SMD 57,18 / 68,62 | v1 02 B, linha 32 | Pe | §3.4 | P-SMD |

- **Fonte da herança nesta execução:** usei a tabela de herança da minha v1 (01 §1), que cita as etapas aprovadas por linha. **Não reabri os arquivos das Etapas 01, 03 e 04 nesta execução.** A ordem limitou a leitura à v1, ao enunciado e ao parecer. As linhas citadas são as da v1, sem nova conferência.
- **Comparação com a v1:** nada sumiu. A v1 não tinha desenho, e esta versão acrescenta.
- **Entregas aprovadas das etapas anteriores:** recebi só pela v1 (por remissão), não os arquivos.

### (b) Prova

| Afirmação | Prova |
|---|---|
| Paredes com 3,00 m | §3.1: `get_parameter` "3,00", 9,8425 pés |
| Muro corrigido para 1,00 | §3.1: antes 0,30 (0,9843 pés), depois 1,00 (3,2808 pés) |
| Cotas conferem | §4: segmento × geometria, linha a linha |
| Áreas dos ambientes | §3.2: conta com os vãos das cotas |
| Documento ativo | §1: `get_document_info` e `get_revit_status` no fim: `"documentTitle": "EP_Montenegro_003_v2"`, 20 paredes, 3 portas, 6 janelas, 19 ambientes, 5 pisos (a cobertura conta à parte) |
| NBR 6492 lida | §7: PDF pp. 15 a 17 |

### (c) Entregável 2, item por item (enunciado, linha 49)

| Item | Situação | Onde |
|---|---|---|
| Implantação | Parcial (esquemático, norte pendente) | EP. Terreno 438266; folha EP-01 |
| Planta do térreo | Atende (esquemático) | EP. Térreo 438276 |
| Planta do superior | Atende (esquemático) | EP. Superior 438286 |
| Corte longitudinal | Parcial (topografia pendente) | 449503 |
| Corte transversal | Parcial (topografia pendente) | 449512 |
| Elevação frontal | Atende (esquemático) | 449522 |
| Elevação de fundos | Atende (esquemático) | 449532 |
| Prova de status e de list_elements | Atende | §3, §8(b) |

### (d) Skills e primário

| Skill / primário | Lida nesta execução? |
|---|---|
| NBR 6492:2021 (primário) | Sim, PDF pp. 15 a 17 |
| `nbr6492-2021-memoriais-por-etapa-projeto` | Não lida: usei o primário |
| `arquitetura-nbr9050-acessibilidade` | **Não lida nesta execução.** O item 4 do parecer (porta, corredor e giro) fica para a correção do corpo, fora desta ordem (itens 1 a 3 e 6) |
| `vaga-estacionamento-...` e COES Art. 29 | Não lidos nesta execução. Cito pela v1 [nv] |
| Demais Skills do enunciado | Não lidas nesta execução (fora do escopo da Entrega 2) |

### (e) O que NÃO foi feito

- Não abri os arquivos aprovados das Etapas 01, 03 e 04 (herança por remissão da v1).
- Não fiz conferência visual das folhas (sobreposição e escala).
- Não criei eixos (create_grid). Não usei cotas de nível nem spot elevation.
- Não verifiquei se o Projeto1.rvt ficou intacto no disco.
- Não fechei o documento "Projeto1" sem salvar, criado do template e aberto em segundo plano.
- Não resolvi a garagem de 4 vagas, a circulação da suíte térrea nem a escada.
- Não corrigi os itens 4 e 5 do parecer (fora desta ordem).
- Não fiz contagem de palavras (pendente de Wallenberg).

Oscar, 14/10/2026.
