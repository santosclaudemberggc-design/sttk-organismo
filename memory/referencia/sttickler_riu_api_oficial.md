---
name: sttickler_riu_api_oficial
description: Endpoints oficiais ArcGIS que leem zoneamento+parâmetros do RIU por coordenada (resolve o ponto fraco do Hely)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 24d9ef72-4792-4c6f-9897-f58654189f89
---

Resolve o ponto fraco do RIU do [[sttickler_licin_licenciamento_rj]] / Hely: a crença de que "o RIU exige clique e é inacessível a ferramenta" está errada. O mapa `mapas.rio.rj.gov.br/lbb.php` é uma app Esri (ArcGIS JS 4.28) que consome serviços **ArcGIS REST públicos, abertos por HTTP com CORS liberado**, em `https://pgeo3.rio.rj.gov.br/arcgis/rest/services/`. Descoberto e testado em 15/07/2026.

**Pipeline oficial endereço → parâmetros do RIU, sem clique:**

1. **Endereço → coordenada** (SIRGAS 2000 / UTM 23S, EPSG **31983**): geocoder oficial que funcionou na execução real do Hely (15/07/2026) foi **`Geocode/Geocode_composto_SIURB`** (aceita `outSR=31983`, reprojeta WGS84→31983 no servidor) — NÃO `Urbanismo/geoRuas`. Ele localiza o número por **interpolação**, então o ponto pode cair dezenas de metros do lote (39 m e 76 m nos testes reais). Por isso a validação por lote abaixo é OBRIGATÓRIA, não opcional. Foi coordenada errada (CEP centroide) que causou o erro original.
   **TRAVA de lote:** confirmar que o ponto cai dentro do lote do cliente refinando pela camada `CadParcel/GeoPAL/MapServer/0` ("Número de lote"). Se o ponto interpolado cair na via (0 features de imóvel), refinar até o lote real antes de consultar o zoneamento.
   **Config da consulta espacial (fixa as 2 causas-raiz do erro):** ponto único com `inSR=31983`, SEM `tolerance` nem `mapExtent`.

2. **Coordenada → pacote RIU completo** (uma única consulta): 
   `https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Urbanismo/LBB_Zoneamento_urbano_vigente/MapServer/0/query`
   Params: `f=json&geometryType=esriGeometryPoint&inSR=31983&spatialRel=esriSpatialRelIntersects&outFields=*&returnGeometry=false&geometry={"x":..,"y":..,"spatialReference":{"wkid":31983}}`
   Retorna todos os campos do RIU: `sigla, zona, subzona, ap, legislacao, cab, cam, to_, lote_min, testada_min, gab_afast, gab_n_afast, afast_fron, ics, obs_riu`. Camada "vigente" (só o que está em vigor). Teste real: ponto x=657364.35 y=7454433.40 → ZRM3 D, CAB 0,8, CAM 1,0, TO 50, lote_min 600, testada_min 12, gab 6pav/20m (afast)/4pav/14m (não afast), afast_frontal 5, ICS 0,4, leg 6.270/2024.

**Serviços auxiliares no mesmo servidor** (folder `Urbanismo`): `IU_Zoneamento_Urbano_Limites` (só zona+vigência, sem números), `LBB_Parametros` (SMD e Q como camadas espaciais), `LBB_AEI`/`LBB_AEIS`/`LBB_Areas_Protegidas`/`LBB_APAC`/`LBB_APP` (restrições sobrepostas — checar todas por coordenada, o zoneamento base não basta), `IU_Usos_e_atividades`. Basemap/imagem em `pgeo3.../Basicos` e `.../Imagens`.

**Consequência:** o acesso ao RIU passou de "muleta / conferência humana obrigatória" para "automático + conferência humana como segurança". IMPLEMENTADO por Kelsen→Hely em 15/07/2026: POP `POP-LEGAL-RIU-01_zoneamento_via_ArcGIS.md` na pasta do Hely, com travas A (lote real), B (ruas homônimas), C (conferência humana vira dupla checagem). Validado end-to-end em 2 endereços reais (Estrada dos Bandeirantes 5000 Vargem Grande → ZRM3 B + incidência de AEI e APA do Sertão Carioca; Rua Albano de Carvalho 100 Recreio → ZPP A-20, Decreto 3.046/1981). Fonte oficial vence — confirmar que a coordenada bate no lote continua sendo a trava. **DECIDIDO por Claudemberg na Reunião Semanal de 20/07/2026 (oficial):** `Geocode_composto_SIURB` é o geocoder padrão e `GeoPAL/0` o confirmador de lote padrão, dentro da Skill de base legislativa por bairro/subzona (Kelsen).
