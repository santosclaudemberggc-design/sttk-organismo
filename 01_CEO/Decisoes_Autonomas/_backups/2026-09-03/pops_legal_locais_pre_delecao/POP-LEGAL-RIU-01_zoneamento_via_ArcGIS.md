---
pop: POP-LEGAL-RIU-01
titulo: Consulta de zoneamento urbano do Rio via ArcGIS REST oficial (RIU sem clicar no mapa)
area: Legal — base legislativa por bairro/subzona
autor: Hely (Agente executor, equipe de Kelsen)
criado: 2026-07-15
origem: Diretriz de Kelsen (aval de Wallenberg/Claudemberg, 15/07/2026); achado testado por Claudemberg
status: oficial — aprovado por Claudemberg na Reunião Semanal de 20/07/2026 (geocoder e trava de lote abaixo formalizados como padrão da Skill "Base Legislativa por Bairro/Subzona")
principios: 8 (Rastreabilidade), 9 (Padronização), 18 (Ética e conformidade)
---

# POP-LEGAL-RIU-01 — Zoneamento urbano do Rio via ArcGIS REST oficial

## 1. Objetivo e por que existe
Obter os parâmetros urbanísticos oficiais de um lote (zona, subzona, CAB, CAM, TO, lote mínimo, testada, gabarito, afastamento frontal, ICS) e as restrições sobrepostas, **partindo de um endereço**, sem depender de clicar no mapa interativo do RIU (`mapas.rio.rj.gov.br`).

O mapa RIU consome serviços **ArcGIS REST públicos** da Prefeitura em `https://pgeo3.rio.rj.gov.br/arcgis/rest/services/`, abertos por HTTP. Consultar esses serviços por coordenada devolve **o mesmo dado oficial que alimenta o RIU** — é fonte oficial, não fonte secundária.

Este POP **substitui explicitamente** os "contornos" anteriores que erravam (geocodificação por CEP centroide + consulta espacial `identify` mal configurada com `tolerance` desproporcional). Ver seção 8 (histórico) e o `_indice_fontes.md`.

## 2. Regra de ouro deste POP
**Fonte oficial vence fonte secundária, sempre.** Compilações de terceiros (sites, PDFs de terceiros, geocoders de terceiros tipo AwesomeAPI/Nominatim) são no máximo indicativo de baixa confiança. O parâmetro que entra num protocolo real vem do endpoint oficial da SMDU **e** passa pela conferência humana no RIU interativo (seção 6, TRAVA C).

## 3. Ferramentas necessárias (dependência de ambiente — registrar se faltar)
- `curl` (com `--data-urlencode` e `-G`) — presente no ambiente de teste (Git Bash, curl 8.21).
- `python` — usado só para parsear o JSON de resposta de forma legível (opcional; dá para ler o JSON cru).
- **Não exige** navegador nem clique no mapa. **Exige** rede liberada para `pgeo3.rio.rj.gov.br`.
- Se `curl` ou rede faltarem no ambiente, sinalizar a Kelsen — é dependência de ferramenta, não decidir sozinho um contorno.

## 4. Servidor e projeção
- Base: `https://pgeo3.rio.rj.gov.br/arcgis/rest/services/`
- Projeção de trabalho do zoneamento: **EPSG 31983** (SIRGAS 2000 / UTM 23S). Toda consulta de zoneamento/restrição usa `inSR=31983` e geometria com `"spatialReference":{"wkid":31983}`.
- **Reprojeção resolvida na origem:** o geocoder devolve nativamente WGS84 (wkid 4326), mas a operação `findAddressCandidates` aceita o parâmetro **`outSR=31983`** — o próprio ArcGIS reprojeta no servidor e devolve a coordenada já em 31983. **Não é preciso reprojetar manualmente.** (Fallback, caso um geocoder não aceite `outSR`: reprojetar 4326->31983 com `pyproj` antes de consultar o zoneamento. No teste real não foi necessário.)

## 5. Procedimento passo a passo

### Passo 1 — Endereço -> coordenada (geocoder oficial)
Geocoder recomendado (testado, o que melhor interpola número de porta): **`Geocode/Geocode_composto_SIURB`**. Alternativas oficiais no mesmo servidor: `Geocode/Geocode_Logradouros_WGS84`, `Geocode/Geocode_Logradouros`, e `Geocode/PAL_QD_LOTE` (geocodifica direto por PAL/Quadra/Lote quando esses dados são conhecidos).

```
curl -s -G "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Geocode/Geocode_composto_SIURB/GeocodeServer/findAddressCandidates" \
  --data-urlencode "SingleLine=Estrada dos Bandeirantes, 5000, Vargem Grande" \
  --data-urlencode "outSR=31983" \
  --data-urlencode "outFields=Addr_type" \
  --data-urlencode "maxLocations=5" \
  --data-urlencode "f=json"
```
Ler no candidato: `score`, `attributes.Addr_type`, `address` (Match_addr) e `location` (x,y em 31983).
- `Addr_type=StreetAddress` ou `PointAddress` = número foi localizado (mais forte). `StreetName` = só achou a rua, não o número (mais fraco — a coordenada é o meio do trecho).
- **Cuidado com homônimos:** se aparecerem candidatos com o mesmo nome de rua a distâncias grandes (visto no teste: "Estrada do Pontal, 4000" devolveu dois pontos a ~2,5 km), NÃO escolher pelo score sozinho — usar `CadLog/Trechos_Logradouros` para ver quantos trechos daquele nome existem e em que faixa de numeração, e resolver pela TRAVA (Passo 2) qual cai no lote do cliente.

### Passo 2 — TRAVA: confirmar que a coordenada cai num LOTE REAL do cliente (obrigatório)
O ponto do geocoder é **interpolado** e pode cair fora do lote (na via, entre lotes). Antes de ler zoneamento, refinar para o lote cadastral real via **GeoPAL, camada 0 "Número de lote"** (pontos de lote com `clnp`, `lote`, `quadra`, `x`, `y` reais):

```
curl -s -G "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/CadParcel/GeoPAL/MapServer/0/query" \
  --data-urlencode "f=json" --data-urlencode "geometryType=esriGeometryPoint" \
  --data-urlencode "inSR=31983" --data-urlencode "spatialRel=esriSpatialRelIntersects" \
  --data-urlencode "distance=50" --data-urlencode "units=esriSRUnit_Meter" \
  --data-urlencode "outFields=lote,quadra,clnp,np,x,y" --data-urlencode "returnGeometry=false" \
  --data-urlencode 'geometry={"x":658105.67,"y":7457186.26,"spatialReference":{"wkid":31983}}'
```
Escolher a feature de lote válida mais próxima (campo `x>0`) e **usar a coordenada `x`,`y` DESSE LOTE** nos passos 3 e 4 — não a coordenada crua do geocoder. Registrar `clnp/lote/quadra` do lote escolhido no arquivo do caso.

Corroboração adicional quando disponível (não é gate único, cobertura é incompleta): `CadParcel/GeoPAL/MapServer/1` (polígono PAL do loteamento — confirma "AVERBADO") e `CadParcel/IMOVEIS_TERRITORIAIS/MapServer/0` (polígono do imóvel). No teste, esses dois nem sempre têm feature no ponto — por isso a camada 0 "Número de lote" é o confirmador primário do lote.

### Passo 3 — Coordenada do lote -> pacote de zoneamento (uma consulta)
```
curl -s -G "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Urbanismo/LBB_Zoneamento_urbano_vigente/MapServer/0/query" \
  --data-urlencode "f=json" --data-urlencode "geometryType=esriGeometryPoint" \
  --data-urlencode "inSR=31983" --data-urlencode "spatialRel=esriSpatialRelIntersects" \
  --data-urlencode "outFields=*" --data-urlencode "returnGeometry=false" \
  --data-urlencode 'geometry={"x":658139.37,"y":7457206.69,"spatialReference":{"wkid":31983}}'
```
**Consulta de PONTO com geometria explícita e `inSR=31983`. NÃO usar `identify` com `tolerance`/`mapExtent`/`imageDisplay`** — é essa combinação que causou o erro histórico (seção 8). A consulta correta devolve **1 feature** para o ponto. Se devolver mais de uma, algo está errado — parar e sinalizar a Kelsen.

Campos retornados: `sigla, zona, subzona, ap, legislacao, cab, cam, to_, lote_min, testada_min, gab_afast, gab_n_afast, afast_fron, ics`. A camada é "vigente" (só o que está em vigor). No campo `legislacao`, o prefixo numérico é código interno: `6.270/2024` = LC 270/2024; `1.3046/1981` = Decreto 3.046/1981.

**Quando a própria camada não traz o número:** algumas zonas (ex.: ZPP subzona A-20) trazem os parâmetros como texto `"Ver Subzona A-20 do Dec. nº 3046/1981"` — a API está dizendo honestamente que o parâmetro numérico está na lei específica (aqui o Decreto 3.046/1981, exceção pontual já registrada no `_indice_fontes.md`). Nesse caso, buscar o número na lei, não inventar.

### Passo 4 — Restrições sobrepostas (obrigatório — o zoneamento-base NÃO basta)
Rodar a MESMA consulta de ponto (coordenada do lote) contra TODAS estas camadas e reportar o que incidir:
`Urbanismo/LBB_AEI`, `Urbanismo/LBB_AEIS`, `Urbanismo/LBB_Areas_Protegidas`, `Urbanismo/LBB_APAC`, `Urbanismo/LBB_APP` (cada uma em `/MapServer/0/query`).
Auxiliares úteis: `Urbanismo/IU_Zoneamento_Urbano_Limites`, `Urbanismo/LBB_Parametros`, `Urbanismo/IU_Usos_e_atividades` (código de zona usado pelo Decreto 56.561/2025 para uso/atividade por CNAE). Restrições de proteção também existem no próprio zoneamento-base (ex.: ZPP), então cruzar os dois.

## 6. AS TRÊS TRAVAS (passos obrigatórios, não opcionais)
> **TRAVA A — o erro nunca foi "ler o mapa", foi apontar o LOTE ERRADO.** A coordenada usada no zoneamento tem que cair DENTRO do lote do cliente. É obrigatório refinar o ponto do geocoder para o lote cadastral real via GeoPAL "Número de lote" (Passo 2). Nunca consultar zoneamento na coordenada crua de CEP/centroide.
>
> **TRAVA B — homônimos de rua.** Se o nome da rua existir em mais de um ponto da cidade, cruzar com `CadLog/Trechos_Logradouros` e resolver pelo lote (TRAVA A) qual é o do cliente — nunca pelo score do geocoder isolado.
>
> **TRAVA C — conferência humana CONTINUA, agora como SEGURANÇA (dupla checagem), não como fonte única.** Antes de qualquer protocolo real, o parâmetro obtido aqui é conferido contra o RIU interativo oficial no lote específico (Princípio 18). Hely não acessa o mapa interativo direto — quando a confirmação visual for necessária, sinalizar a Kelsen/Claudemberg para conferir no mapa. A API dá o dado; a conferência humana fecha.
>
> **TRAVA D — colisão de subzona entre Áreas de Planejamento, propagada do `POP-GESTOR-LEGAL-01` (checagem B, item 4) em 08/08/2026.** O mesmo código de subzona existe em APs diferentes com valores diferentes (ex.: "ZRM3 D" existe na AP2, com CAM 3,5/TO 70/8pav-25m, **e** na AP4, com CAM 1,00/TO 50/6pav-20m afastado/4pav-14m não afastado). Antes de aceitar a linha do Anexo XXI lida no Passo 3 (seção 5), **conferir que o cabeçalho do bloco de Área de Planejamento é o da AP do lote** — não basta o código da subzona bater. **Near-miss real em 20/07/2026:** parâmetro de lote da Zona Sul quase aplicado a uma casa no Recreio. O campo `ap` retornado pela consulta de ponto (seção 5, Passo 3) já identifica a AP correta — usar esse campo para escolher o bloco certo do Anexo XXI, nunca localizar a subzona por busca textual isolada (`grep` devolve a primeira ocorrência, que pode ser de outra AP).

## 6.1. FALLBACK DA TRAVA A — quando a unidade está dentro de uma GLEBA-MÃE (loteamento fechado / condomínio fechado)
> **Aprovado por Claudemberg na Reunião Semanal de 20/07/2026**, a partir do achado documentado desde o caso Vasconcelos. Este fallback é uma extensão específica da TRAVA A (seção 6) — não a substitui, e **não dispensa a TRAVA C** (ver Resultado, abaixo).

**Por que existe:** o cadastro municipal (GeoPAL) enxerga a **gleba-mãe** do loteamento/condomínio fechado, não a unidade interna individual que o cliente comprou. Em loteamento fechado, os lotes internos são autônomos (matrícula própria), mas o GeoPAL pode não ter cadastrado a subdivisão — só a gleba. Isso é diferente de condomínio fechado, onde a unidade é fração ideal e **nunca** tem CLNP próprio por natureza (não é caso de fallback, é a regra — ver Lacunas, seção 10). Este fallback trata do caso intermediário: loteamento fechado onde o lote é autônomo de direito, mas o GeoPAL ainda não devolve feature própria pra ele.

### Condição de gatilho
Aplicar este fallback quando, no Passo 2 da seção 5 (TRAVA A, consulta a `CadParcel/GeoPAL/MapServer/0/query`), ocorrer qualquer um destes:
- A consulta não retorna **nenhuma feature** de lote na coordenada/raio da unidade do cliente; ou
- A consulta retorna uma feature, mas ela corresponde à **gleba inteira** do loteamento (CLNP genérico da gleba, sem `lote`/`quadra` compatível com a unidade específica que o cliente informou); ou
- O cliente/caso já indica de origem que se trata de loteamento fechado ou condomínio fechado (contrato, matrícula, ou informação do próprio cliente) — nesse caso, rodar a TRAVA A normal primeiro; se ela não autoconfirmar a unidade, seguir para este fallback.

**Se a TRAVA A normal (Passo 2, seção 5) já devolveu CLNP próprio e compatível com a unidade do cliente, este fallback não se aplica — segue o caminho padrão da seção 5/6.**

### Passo 1 do fallback — confirmar a PAL da gleba
Consultar o polígono PAL (Projeto Aprovado de Loteamento) na camada `CadParcel/GeoPAL/MapServer/1`, na mesma coordenada usada no geocoder (Passo 1, seção 5), para confirmar que a gleba está **"AVERBADA"** e obter o número/identificação do PAL que rege aquele loteamento fechado:

```
curl -s -G "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/CadParcel/GeoPAL/MapServer/1/query" \
  --data-urlencode "f=json" --data-urlencode "geometryType=esriGeometryPoint" \
  --data-urlencode "inSR=31983" --data-urlencode "spatialRel=esriSpatialRelIntersects" \
  --data-urlencode "outFields=*" --data-urlencode "returnGeometry=false" \
  --data-urlencode 'geometry={"x":<x_da_coordenada>,"y":<y_da_coordenada>,"spatialReference":{"wkid":31983}}'
```
Ler no retorno o campo de situação/status do PAL (ex.: `situacao`, `status`, ou equivalente conforme os campos daquele serviço) e o número/identificação do PAL. **Se não vier feature nenhuma, ou o status não for "AVERBADO", o fallback não pode prosseguir** — registrar e escalar conforme o item 6 abaixo (vai direto pra TRAVA C sem alternativa).

### Passo 2 do fallback — planta do condomínio/loteamento averbada em cartório
A API pública **não tem** a subdivisão interna do loteamento (a gleba é uma feature única no GeoPAL) — este passo **não é consulta automática**, é verificação documental:
- Verificar se a **planta do loteamento averbada em cartório** (mostra a numeração interna das unidades/lotes dentro da gleba) já está na pasta do caso no Drive (`000_CLIENTES > Bairro > Cliente > etapa Legal`, ou a pasta de caso-teste equivalente enquanto em fase de teste).
- **Se o documento já estiver disponível**, seguir para o Passo 3.
- **Se o documento NÃO estiver disponível**, Hely **não presume nem inventa** o número/posição da unidade dentro da gleba. Parar aqui e **sinalizar a Kelsen** que falta a planta averbada — é lacuna documental, não decisão de execução (Princípio 18).

### Passo 3 do fallback — cruzamento
Com a planta averbada em mãos, conferir:
1. Se o número/identificação da unidade do cliente (conforme contrato/matrícula/informação do cliente) **bate** com a numeração mostrada na planta averbada; **e**
2. Se essa planta está **dentro do perímetro do PAL** confirmado como "AVERBADO" no Passo 1 (mesma gleba, mesmo loteamento).

Se os dois baterem, a unidade está confirmada dentro da gleba. Os parâmetros urbanísticos a usar são os da zona/subzona da gleba (obtidos normalmente via Passo 3 da seção 5, na coordenada da gleba confirmada no Passo 1 deste fallback) — **salvo se o PAL tiver parâmetros urbanísticos específicos próprios**, o que é uma questão distinta, já registrada como pauta separada para o Maurício (não tratada neste POP).

### Resultado
Se os Passos 1 a 3 do fallback baterem, este fallback **substitui a necessidade de cair direto na TRAVA C só porque a TRAVA A automática não autoconfirmou** — ou seja, evita escalar por conferência humana manual unicamente por essa causa, quando a cadeia PAL averbado + planta averbada + cruzamento de numeração já dá confirmação suficiente da unidade dentro da gleba.

**Isto não dispensa a TRAVA C.** Exatamente como no caminho normal (seção 6), a conferência humana no RIU interativo **continua obrigatória** antes de qualquer protocolo real (Princípio 18) — este fallback é substituto de "cair direto e sem alternativa" na TRAVA C só por falha automática da TRAVA A, não é substituto da TRAVA C em si.

### Escalonamento — se o fallback também não confirmar
Se qualquer um destes ocorrer, **não inventar contorno** — escalar direto para a TRAVA C sem alternativa, e sinalizar a Kelsen com o motivo específico:
- A planta averbada em cartório não está disponível na pasta do caso (e o cliente/Kelsen não a forneceu); ou
- A numeração da unidade não bate com a planta averbada; ou
- O PAL não confirma status "AVERBADO" (ou não há feature de PAL naquela coordenada).

### Exemplo hipotético (consistente com a seção 9 — a confirmar com caso real quando surgir)
- Cliente informa unidade "Lote 34" dentro de um loteamento fechado em Vargem Grande.
- Passo 2 (seção 5, TRAVA A normal): GeoPAL camada 0 devolve uma única feature na área — CLNP da **gleba inteira**, sem `lote=34` correspondente. Gatilho do fallback confirmado.
- Passo 1 do fallback: GeoPAL camada 1 (PAL) devolve polígono com status "AVERBADO" e número de PAL identificado.
- Passo 2 do fallback: planta averbada já está na pasta do caso no Drive (enviada pelo cliente no onboarding).
- Passo 3 do fallback: "Lote 34" consta na planta averbada, dentro do perímetro do PAL confirmado. Cruzamento bate.
- Resultado: unidade confirmada dentro da gleba — zoneamento lido na coordenada da gleba (Passo 3, seção 5) — segue para TRAVA C (conferência humana no RIU) antes de qualquer protocolo real, como de praxe.

## 6.2. VALIDADE DA CAPTURA — LIMITE DE 30 DIAS + RECONFIRMAÇÃO NO DIA DO PROTOCOLO
> **Aprovado por Claudemberg em 20/07/2026** (valor cravado em 15/07/2026, formalizado aqui em 20/07/2026).

- Qualquer parâmetro capturado por este POP (zoneamento, restrições sobrepostas) **vale por 30 dias corridos** a partir da data da consulta. Passado esse prazo, a consulta tem que ser refeita antes de qualquer uso em caso real — não reaproveitar captura vencida.
- **Mesmo dentro dos 30 dias**, os parâmetros de conformidade dura (CAB, CAM, TO, gabarito, afastamentos, uso) precisam ser **reconfirmados no dia do protocolo real**, sempre — não é opcional, mesmo que a captura ainda esteja "dentro do prazo". Motivo: a fonte é um sistema vivo da prefeitura, pode mudar antes da validade de 30 dias vencer.
- Registrar no arquivo do caso: data da captura original, data da reconfirmação no dia do protocolo, e se houve alguma divergência entre as duas (se houver, a mais recente vence — Princípio 18).

## 7. Regra de configuração que neutraliza as causas-raiz do erro histórico
- Consulta de **ponto único** com `geometryType=esriGeometryPoint` + `inSR=31983` + `geometry` explícita. **Sem** `tolerance` em pixel, **sem** `mapExtent`/`imageDisplay`. (Neutraliza a causa-raiz "b" — consulta espacial mal configurada.)
- Conferir que a feature retornada é a do lote confirmado no GeoPAL (TRAVA A). Se vier mais de uma feature, parar. (Neutraliza a causa-raiz "c" — atribuição de feature errada.)
- Registrar SEMPRE, no arquivo do caso: coordenada literal do lote, `clnp/lote/quadra`, e os parâmetros exatos da requisição (Princípio 8).

## 8. Histórico do erro que este POP corrige (não apagar — Princípio 8)
Em 14/07/2026 uma consulta a esta API (caso Rua Escritor Elie Wiesel / CL 476218, Recreio) registrou **ZRM3 O** — errado. O real, confirmado no RIU oficial em 15/07/2026, é **ZRM2 G** (diferença de zona-mãe inteira). Causa-raiz reconstituída: geocodificação por CEP centroide + `identify` com `tolerance` desproporcional ao `mapExtent`, que "explode" a busca para um raio de vários km e devolve uma zona distante como se fosse a do lote. Este POP elimina os dois vetores (geocoder oficial + trava por lote; consulta de ponto sem tolerance). A API foi **religada condicionalmente** sob este pipeline — ver `_indice_fontes.md`.

## 9. Exemplos reais testados (15/07/2026) — não teóricos

### Exemplo A — happy path numérico completo + restrições incidentes
- Endereço: **Estrada dos Bandeirantes, 5000, Vargem Grande**
- Geocode (`Geocode_composto_SIURB`, `outSR=31983`): score 96,33, `Addr_type=StreetAddress`, match "5000 Estrada dos Bandeirantes" -> ponto interpolado **x=658105.67 y=7457186.26**.
- TRAVA GeoPAL (raio 50 m): lote **11**, quadra **IV**, **CLNP 02433113867**, np 13867 -> coordenada do lote real **x=658139.37 y=7457206.69** (39,4 m do ponto interpolado — o refino importou).
- Zoneamento @ lote: **ZRM3 B** (AP4, lei 270/2024) — CAB 0,8; CAM 1,5; TO 50; lote_min 360; testada 10; gab_afast 6pav/20m; gab_n_afast "-"; afast_frontal 5; ICS 0,6.
- Restrições sobrepostas: **LBB_AEI INCIDE** — AEIA "Ambiental de Vargem Grande, Vargem Pequena e parte do Recreio/Camorim" (Leis 48.990/2021; 49.405/2021; 49.697/2021); **LBB_Areas_Protegidas INCIDE** — **APA do Sertão Carioca** (Leis 50.411/2022; 49.695/2021). AEIS, APAC, APP não incidem. *Prova concreta de que o zoneamento-base não basta.*

### Exemplo B — TRAVA pegando ponto fora do lote + deferência honesta à lei específica
- Endereço: **Rua Albano de Carvalho, 100, Recreio dos Bandeirantes**
- Geocode: score 99,5, `Addr_type=StreetAddress` -> ponto interpolado x=656277.77 y=7453276.62. `IMOVEIS_TERRITORIAIS` nesse ponto: **0 features** (interpolação caiu fora do polígono de lote — a TRAVA A justifica-se aqui).
- TRAVA GeoPAL (raio 40 m): lote **22**, quadra **14**, **CLNP 10421600085** -> coordenada do lote **x=656325.95 y=7453333.96**.
- Zoneamento (nos DOIS pontos, interpolado e lote — concordaram): **ZPP (A-20)**, AP4, legislação "Decreto 3.046/1981; LC 270/2024". Parâmetros retornados como texto **"Ver Subzona A-20 do Dec. nº 3046/1981"** — a API remete à lei específica; o número sai da leitura do decreto, não da API. Nenhuma restrição adicional (AEI/AEIS/Áreas Protegidas/APAC/APP) incidente — a proteção já está na própria zona-base ZPP.

### Âncora — reprodução do teste do Claudemberg
- Coordenada x=657364.35 y=7454433.40 (31983) -> **ZRM3 D**, CAB 0,8, CAM 1,0, TO 50, lote_min 600, testada 12, gab 6pav/20m (afast)/4pav/14m (não afast), afast_frontal 5, ICS 0,4, lei 270/2024 — **bateu 100% com o RIU oficial**. Isto ancora que o endpoint REST = a fonte que alimenta o RIU.

## 10. Lacunas conhecidas (sinalizadas a Kelsen)
- **Precisão do geocoder:** localiza o número quando `Addr_type=StreetAddress/PointAddress`, mas por **interpolação** — o ponto pode ficar dezenas de metros do lote (39 m e 76 m nos testes). Por isso a TRAVA A (refino por lote) é obrigatória, não opcional. Quando só devolve `StreetName`, é o meio do trecho — mais fraco ainda.
- **Cobertura incompleta** de `IMOVEIS_TERRITORIAIS` e do polígono `PAL` — nem todo lote tem feature nessas camadas; o confirmador primário é a camada 0 "Número de lote" do GeoPAL.
- **Loteamento fechado / condomínio fechado — gleba-mãe sem CLNP próprio da unidade:** quando a TRAVA A (Passo 2, seção 5) não autoconfirma porque o GeoPAL só enxerga a gleba-mãe, usar o fallback da seção 6.1 (PAL averbado + planta de cartório + cruzamento) antes de escalar. Em **condomínio fechado** a unidade é fração ideal e **nunca** terá CLNP próprio — não é uma falha a corrigir, é a natureza do regime; o fallback da 6.1 só resolve o caso de loteamento fechado com lote autônomo de direito mas ainda não refletido no GeoPAL.
- **Dependência de ferramenta:** exige `curl` + rede para `pgeo3.rio.rj.gov.br`. Se faltar, sinalizar — não improvisar contorno.
- **A API não substitui o RIU assinado** para protocolo: a conferência humana (TRAVA C) continua obrigatória (Princípio 18).
