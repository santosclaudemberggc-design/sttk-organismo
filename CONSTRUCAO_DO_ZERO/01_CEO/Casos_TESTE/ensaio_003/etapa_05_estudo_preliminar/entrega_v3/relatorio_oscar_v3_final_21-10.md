# Ensaio 003, Etapa 05 (EP), v3 final, 21/10/2026: RETOMADO em 21/10 após reconexão

Autor: Oscar. Destinatário: Lúcio. Ordem de Claudemberg (21/10/2026), via Wallenberg e Lúcio. Análise preliminar: não é entregável final e não passou pelo Gate.

## Entrega — Ensaio 003 — Etapa 05 (EP) v3 final
Build: 2026-10-20-quadro-areas-v69 (lido no get_revit_status)

### Gate de entrada (0.1/0.3), saída bruta
```
get_revit_status: success true | connected true | buildVersion "2026-10-20-quadro-areas-v69" | hasDocument true
 revitVersion "Autodesk Revit 2026" | documentTitle "EP_v3"
 documentPath "D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\CONSTRUCAO_DO_ZERO\01_CEO\Casos_TESTE\ensaio_003\etapa_05_estudo_preliminar\entrega_v3\EP_v3.rvt"
 isModified false | statistics {levels 4, walls 44, doors 20, windows 24, rooms 22, floors 13} | uptime 00:00:47
get_document_info: success true | name "EP_v3" | path (o mesmo acima) | version "Autodesk Revit 2026"
 statistics {levels 4, walls 44, doors 20, windows 24, rooms 22}
```
Documento ativo = EP_v3.rvt em entrega_v3. Não abri nem fechei documento. RDMOB-PBA-04 não foi tocado.
Níveis (get_levels): Terreno 324604 = 0; Páv. térreo 311 = 0,30; Páv. Superior 694 = 3,45; Cobertura 323714 = 6,60.

### (a) Árvores, 1 por vaga descoberta (Dec. 3.046 XXII, p. 4, conforme o parecer Kelsen)
Antes: `list_elements Vegetação` = total 0, listado antes de criar.
Tipo: 105491 "M_RPC Árvore - Caduca : Bordo japonês - 3,0 metros" (o único porte pequeno do projeto; espécie nativa é com Glaziou).
- 455088: criada em (13,04; 19,00). A copa (bbox y 16,758) invadia a vaga 2, então movi dy +1,5. Releitura: ponto (13,04; 20,50), bbox x 10,812–15,122, y 18,258–22,674.
- 455089: (13,04; 23,00), bbox y 20,758–25,174.
- Comentários (requestIds oscar-21-10-arv1-com/arv2-com): "ARVORE VAGA DESCOBERTA 1 (454843) Dec 3046 XXII" e "... 2 (454851) ...".
- Ficam no jardim 452447 (x 11,79–14,29; y 18–35), atrás do fim da vaga 2 (y 18). Não há lugar ao lado das vagas: a faixa toda tem 2,50 m e é a própria vaga. Na frente (y 0–6) a árvore bloquearia o acesso. Fora da vaga e da faixa de acesso. Ressalva: a bbox da família RPC tem 4,31 m de largura e passa por cima da parede da casa e do muro. É só símbolo; a copa real é de Glaziou.

### (b) Quadro (criar_quadro_areas), saída bruta
Parâmetros: areaLote 571.6, baseIndices "informada", limites {toMax 40, caMax 1.0, tpMin 25}, permeaveis "JARDIM|GRAMA", fatorConcregrama 0, fatores [GARAGEM COBERTA VAGA 1 ×0 TO; MARQUISE ×0; GARAGEM COBERTA ×0 CA].
```
areaLoteInformadaM2 571.6 | areaLoteDoModeloM2 571.6 | diferencaLoteM2 0
baseDosIndices {informada, 571.6} | naOutraBase {571.6: TO 38.33, CA 0.72, perm 32.76}
somaAreasDoLote {m2 547.1, percentual 95.71, confere "NÃO soma 100%: conferir contorno do lote e regiões"}
taxaOcupacao 38.33 atende | coeficienteAproveitamento 0.72 atende | permeabilidade 32.76 atende
TO   térreo GARAGEM COBERTA VAGA 1   13.83 ×0 = 0       (455106)
TO   térreo MARQUISE BALANCO 15 CM   13.01 ×0 = 0       (455120)
TO   térreo PROJECAO                219.11 ×1 = 219.11  (455138)
CA   térreo GARAGEM COBERTA VAGA 1   13.83 ×0 = 0       (455156)
CA   térreo GARAGEM COBERTA VAGA 2   14.19 ×0 = 0       (455163)
CA   térreo AREA CONSTRUIDA         204.93 ×1 = 204.93  (455170)
CA   sup.   MARQUISE BALANCO 15 CM   13.01 ×0 = 0       (455195)
CA   sup.   AREA CONSTRUIDA         206.45 ×1 = 206.45  (455215)
PERM Terreno JARDIM SOLO NATURAL    187.27 ×1 = 187.27  (455241)
PERM Terreno IMPERMEAVEL            359.83 ×0 = 0       (455248)
areasVazias [] | aviso "Fatores padrão (1 = conta inteira; grama 1; concregrama 0 (Rio não fixa fator); impermeável 0) até o Hely aplicar os fatores da Skill quadro de áreas RJ..."
```
- Permeabilidade: 187,27 / 571,60 = 32,76% ≥ 25%. Jardins: 452447 42,50 + 454328 85,00 + 454336 34,45 + 454823 25,32 = 187,27. As árvores não mudam área.
- **CALCADA:** os pisos 454312 (85,74, faixa frontal), 454843 (15,00) e 454851 (15,00), tipo 454293 "CALCADA ACESSO E VAGAS DESCOBERTAS .30", entram como **NÃO permeáveis, fator 0, dentro da região IMPERMEAVEL id 455248 (359,83 m²)**. Não casam com o regex "JARDIM|GRAMA". Diferente de 20/10, não usei o manual CONCREGRAMA. Foi escolha conservadora: o resultado é o mesmo (fator 0). Imagem: a faixa das vagas fica dentro do contorno roxo IMPERMEAVEL.
- Soma do lote: 547,10 + piscina 454356 17,50 + deck 454348 7,00 (furo no jardim 454336, fora de região) = 571,60 = 100%. A ferramenta continua dando 95,71%: o defeito de 20/10 persiste.
- TO 219,11 ≤ 228,64 (40%). CA (204,93 + 206,45) / 571,60 = 0,720.

### (c) Largura interna das vagas cobertas (sem cota, E-32)
Fonte: `list_elements Paredes levelId 311 fields location`. Espessura: `manage_types listar` tipo 326842 "Parede padrão - 15 cm" espessura 0.15 (as duas paredes são desse tipo).

| Item | Parede oeste | Parede leste | Eixos | Conta | Face a face |
|---|---|---|---|---|---|
| Largura das 2 vagas | 453878 x 6,55 (y 6,075–11,5), e 0,15 | 453875 x 11,715 (y 6,075–31), e 0,15 | 11,715 − 6,55 = 5,165 | 5,165 − (0,075 + 0,075) | **5,015 ≥ 5,00** |
| Profundidade | 453874 y 6,075 (frente), e 0,15 | 453879 y 11,5 (fundo), e 0,15 | 11,5 − 6,075 = 5,425 | 5,425 − 0,15 | **5,275 ≥ 5,00** |

- Por vaga, dividindo igualmente: 5,015 / 2 = 2,5075 ≥ 2,50.
- **Mas a divisão desenhada não é igual.** A linha de separação entre os ambientes não fica no meio. Áreas (get_rooms): VAGA 1 453914 = 13,06 e VAGA 2 453915 = 13,40. Pela profundidade 5,275: vaga 1 = 13,06 / 5,275 = **2,476 < 2,50**; vaga 2 = 2,540. Soma 5,016 (confere com o 5,015). Não redesenhei.
- **Proposta:** mover a linha de separação para x = 6,625 + 2,5075 = 9,1325 (as duas ficam com 2,5075). Não há sobra: a folga total é 0,015 m. Alternativa com folga: deslocar a parede 453878 para oeste (o hall perde área).
- A cota 5,02 da imagem do térreo (de 20/10) bate com a face a face 5,015, e não com eixo a eixo (5,165). A leitura do Bardi ("5,02 é eixo a eixo") não se confirma por esta conta. Lúcio decide.
- **Achado:** a parede de frente 453874 tem só a porta 453937 (entrada, 1240 × 2100). Na imagem do térreo não aparece vão de garagem na fachada da garagem (x 6,55–11,715). A entrada de carro na garagem coberta não está modelada. Não redesenhei.

### (d) Faixa lateral e acesso das vagas descobertas (COES Art. 29 II e IV, conforme o parecer Kelsen)
- Face leste da casa = eixo 453875 x 11,715 + 0,075 = 11,79. Muro leste 449287, eixo x 14,335, tipo "Genérico - 90 mm" → face interna 14,335 − 0,045 = 14,29. **Faixa = 14,29 − 11,79 = 2,50 m.** As lajes 454775/454783 e a marquise 454246 vão até x 11,79: nada avança sobre a faixa.
- Vagas: 454843 x 11,79–14,29, y 6–12; 454851 y 12–18 (2,50 × 6,00 cada, paralelas em fila).
- **Acesso (IV, 2,50 m):** pela faixa frontal 454312 (y 0–6) na mesma largura de 2,50 (x 11,79–14,29). A largura dá exatamente 2,50.
- **Pendências de geometria (não são parecer legal):**
  - O muro frontal 449286 (y −0,045, x −0,045–14,335) não tem portão. `get_doors wallId 449286` = []. O acesso pela rua não está modelado.
  - As vagas ficam em fila: a vaga 2 só sai se a vaga 1 sair (vaga presa).
  - **Manobra (II):** não há área de 2,50 × 5,00 além da própria faixa. A única área livre é o trecho frontal y 0–6, que é afastamento frontal. Se o trecho frontal serve de manobra, quem diz é Kelsen.

### Imagens conferidas (§6), todas abertas com Read nesta execução
Pasta `D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\CONSTRUCAO_DO_ZERO\01_CEO\Casos_TESTE\ensaio_003\etapa_05_estudo_preliminar\entrega_v3\imagens\v3_final_21-10\`
- `vitruvius_20261021_141817 - Planta de piso - EP- Terreno.png`: as 2 árvores aparecem no jardim leste logo depois da VAGA DESCOBERTA 2, sem cair sobre o piso das vagas. A cota vertical "40,00" encosta na 2ª árvore (limpeza pendente). Também se veem a faixa de 2,50 e o muro frontal contínuo.
- `vitruvius_20261021_141825 - Planta de área (PERMEABILIDADE) - PLANTA DE PERMEABILIDADE.png`: dois contornos, "JARDIM SOLO NATURAL 187 m²" e "IMPERMEAVEL 360 m²". As vagas e a calçada frontal ficam no impermeável, e piscina + deck ficam fora das duas regiões (defeito da soma).
- `vitruvius_20261021_141833 - Planta de piso - EP- Térreo.png`: a garagem tem VAGA 1 (44) e VAGA 2 (45), e a linha de separação fica à esquerda do meio. Aparecem as cotas 5,02 e 5,43 e as árvores no lado leste. Não aparece vão de garagem na fachada. Rótulos BANHO DEPENDENCIA × SERVICO sobrepostos.
Perspectiva: não há ferramenta para criar ou ajustar vista 3D. A "EP. Perspectiva" não foi exportada nesta execução (fora da ordem).

### Salvar
`document salvar` (requestId oscar-21-10-v3final-salvar): caminho ...\entrega_v3\EP_v3.rvt, tinhaAlteracoes true, 18710528 bytes, dataHora 2026-10-21T14:18:45, modificadoDepois false. get_revit_status depois: isModified **false**.

Defeitos encontrados (§8): soma do lote 95,71% (piscina/deck fora de região), sem código, já reportado em 20/10. Família RPC com bbox maior que a copa (informativo).
Pendências: separação das vagas cobertas (2,476 na vaga 1); vão da garagem; portão no muro frontal; manobra/vaga presa (Kelsen); espécie nativa das árvores (Glaziou); cota 40,00 sobre a árvore; aceite do condomínio (Regramento Art. 9º).
Status: PARCIAL

---

## Histórico: bloqueio da 1ª tentativa (21/10, antes da reconexão)
- `vitruvius_get_revit_status` → `Error: Plugin não está conectado`
- `vitruvius_document acao=listar_abertos` → `Error: Plugin não está conectado`
- `vitruvius_get_document_info` → `Error: Plugin não está conectado`
Nada foi feito naquela tentativa: o EP_v3 não foi aberto nem alterado e o RDMOB não foi tocado. Status naquela hora: NÃO FEITO.
