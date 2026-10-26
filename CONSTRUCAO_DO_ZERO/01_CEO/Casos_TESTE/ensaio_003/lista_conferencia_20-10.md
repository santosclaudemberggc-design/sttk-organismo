# Lista de conferência — 20/10/2026 (Wallenberg)

Commit no repositório do organismo: `273710c` (78 arquivos). Ficaram de fora só os backups automáticos do Revit (`*.000N.rvt`).
**A pasta `D:\011_VITRUVIUS` não é repositório git**, então as mudanças do plugin e do MCP (itens 9 a 14) estão só no disco, sem commit.

## A. Repositório do organismo (commit 273710c)

1. `.claude/skills/oscar-revit-projetista-vitruvius/SKILL.md` e o espelho em `.agents/skills/...`, linha 153.
   Prova: `| — | quadro de áreas (TO, CA, permeabilidade) | Desde 20/10/2026 (plugin v68): `criar_quadro_areas` | Template ARQ.Sttk - 2026 já traz os 3 esquemas e as 3 tabelas com fórmula ...`
2. `CONSTRUCAO_DO_ZERO/01_CEO/Padroes_Documentos/Oscar_catalogo_vitruvius.md`, linha 97.
   Prova: `- **Quadro de áreas (20/10/2026, plugin v68):** `criar_quadro_areas` — areaLote (obrigatória), fatores (Skill quadro-de-areas-rj ...), manuais ..., baseIndices (menor/informada/medida) ...`
3. `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/ensaio_003/_estado_ensaio_003.json`:
   - linha 583, evento `quadro_areas_partido_b` (TO 40,01% / CA 0,786 / permeabilidade 44,99%, concregrama decidido por Claudemberg);
   - linha 608, `gate_decidido_por_claudemberg_20_10`: base 571,60, vão da escada fora do superior, permeabilidade de 25%;
   - linha 617, `volumetria_escolhida`: E, decidido por Claudemberg;
   - linhas 630 e 643, `exame_fase3_corrigido` (7,60, reprovado por Claudemberg) e `exame_fase3_recorrigido` (8,75, aprovado por Claudemberg);
   - linha 655, `trava_v3_etapa_5_liberada`;
   - linha 674, `"liberada": true`; linha 680, `gabarito_modelo_20_10` (SHA256 c18910c4…); linha 687, `"liberacao_20_10": "Fase 3 aprovada com 8,75 e trava da etapa 5 liberada apos conferencia visual no Revit — decidido por Claudemberg, 20/10/2026."`
4. `CONSTRUCAO_DO_ZERO/01_CEO/Casos_TESTE/ensaio_003/mapa_prontidao_etapas_04_17.md`, linha 31.
   Prova: `**Decidido por Claudemberg em 20/10/2026: Fase 3 aprovada (8,75) e trava v3 da etapa 5 liberada.** Modelo: etapa_05_estudo_preliminar/entrega_v3/EP_v3.rvt (volumetria E). Parecer: parecer_bardi_v3_correcao.md.`
5. `CONSTRUCAO_DO_ZERO/01_CEO/Rotinas_Evolucao/ensaio_sombra.md`, linha 52.
   Prova: `- **(20/10) Decidido por Claudemberg em 20/10/2026: Fase 3 aprovada com 8,75 (...) e trava v3 da etapa 5 LIBERADA após conferência visual no Revit.** Portão encerrado. ...`
6. Arquivos novos, escritos pelos agentes:
   - `etapa_05_estudo_preliminar/diagnostico_EP/volumetria_estudos_v2.md` e os modelos `EP_volumeD/E/F.rvt` (Oscar);
   - `etapa_05_estudo_preliminar/entrega_v3/`: `EP_v3.rvt`, `relatorio_oscar_v3.md` (com a seção "Correção 20/10 após reprovação") e `imagens/` (Oscar);
   - `etapa_05_estudo_preliminar/parecer_bardi_v3.md` e `parecer_bardi_v3_correcao.md` (Bardi);
   - `_gabaritos_LACRADO_bardi/ensaio_003/etapa_05_gabarito.md`, seção 7: Bardi. O lacre SHA256 `c18910c4742f6e6d7896dddeba2e7c1660ee930486a966e5d0fe708ec4a5324e` foi conferido intacto depois das duas correções.
7. Estados atualizados pelos próprios agentes: `_estado_hely.md`, `_estado_lucio.md`, `_estado_oscar.md`.
8. O commit também levou o que já estava pendente de antes (rotinas de 19 e 20/10, `.claude/settings.local.json` com permissões de sessão, Skills novas de escada, layout, volumetria e quadro de áreas). Nada disso foi escrito por Wallenberg nesta parte da conversa.

## B. Vitruvius (`D:\011_VITRUVIUS`, fora do git)

9. `RevitPlugin/RevitPluginApp.cs`, linha 27: `public const string BuildVersion = "2026-10-20-quadro-areas-v69";`. Instalado nas duas pastas de add-in, MD5 `9A334555603730682AB4AC0290D3E26E`.
10. `RevitPlugin/Commands/CreateAreaTableCommand.cs`:
    - linha 67, apaga áreas soltas dos 3 esquemas: `var soltas = new FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Areas)...`
    - linhas 76 e 155, garagem, varanda e marquise viram áreas próprias: `var subTO = Separadas(doc, ES_TO, regras, nTerreo, pisosEdif, TipoNome, todosOsNiveis: true);`
    - linha 106, manual de permeabilidade entra antes do IMPERMEAVEL e fica fora dele: `// manuais de PERMEABILIDADE (ex.: faixa de concregrama sem piso no modelo) entram antes`
    - linha 330, etiqueta sem linha de chamada: `var tag = doc.Create.NewAreaTag(vista, area, new UV(q.X, q.Y)); if (tag != null) tag.HasLeader = false;`
    - linha 388, base dos índices: `baseDosIndices = new { modo, m2 = Math.Round(baseM2, 2) },` com padrão "menor" e a outra base em `naOutraBase`.
11. `RevitPlugin/Utils/AreaGeometria.cs`, linhas 119 e 125: ponto mais folgado para a etiqueta. Prova: `.OrderByDescending(q => Math.Round(Folga(q, bordas), 1))` e `private static double Folga(XYZ q, List<List<XYZ>> poligonos)`.
12. `MCP_Server/src/modelagem.ts`, linha 151. Prova: `baseIndices: { type: 'string', enum: ['menor', 'informada', 'medida'], ...`. O build passou.
13. `VITRUVIUS_ERROS_RAIZ.md`, linha 262: `### E-31 · Quadro de áreas pela API (criar_quadro_areas, v65–v68)`, com 6 causas raiz e a regra.
14. `PLANO_AGENTE_GUIADO.md`, linha 96: `- **[20/10/2026] PASSOU — decidido por Claudemberg.** Exame sobre a volumetria E: 7,60 (reprovado) → correção → 8,75 (aprovado) ...`

## C. Modelo no Revit (fora do git)
15. `diagnostico_EP/EP_layout_partidoB.rvt`: áreas soltas 418454 e 418905 apagadas (antes, conferido `location: null`), quadro v68 e modelo salvo.
16. `entrega_v3/EP_v3.rvt`: quadro v69 refeito e salvo (TO 44,71% / CA 0,837 / permeabilidade 28,33%) antes da correção do Oscar. O Oscar alterou e salvou de novo às 20:56.

## Pendências registradas (não resolvidas)
- Programa com 452 m², contra ~520 (3º pavimento ou cliente; Kelsen olha o gabarito de altura).
- Vagas descobertas no afastamento lateral (Kelsen); largura interna das vagas cobertas não provada.
- Defeitos do Vitruvius: resize com falso sucesso; cota de face interna medindo eixo; piscina e deck fora da soma do lote; colisão de nome na exportação.
- Bardi: lançar `notas_assertividade.md`, `registro.json` e `_estado_bardi.md` (ele declarou que não fez).
