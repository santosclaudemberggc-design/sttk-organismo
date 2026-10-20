# Taxa de Ocupação (TO) da ZPP / ZE-5 por subzona — Decreto 3.046/1981 (Cap. III) — trabalho Hely, 14/10/2026

**Item:** kelsen-f1-to-zpp-anexo-xxi-subzona-13-10-2026 (pedido de Kelsen, acionamento automático de 14/10/2026).

> Correção 20/10/2026 (Drenagem Contínua, item hely-mapa-zpp-a18-a19-19-10-2026): linha p34 corrigida de A-18 para A-19 após conferência no PDF p.34 (cabeçalho "Subzona A-19"). Backup: _backups/2026-10-20/.

## 1. Onde a TO da ZPP está escrita (duas camadas)

- **LC 270/2024, Anexo XXI, bloco AP-4, linha "ZPP"** (PDF p. 275, conferido por rasterização da página): colunas CAM, TO, lote mínimo, gabarito e afastamento frontal dizem todas **"ver Dec. nº 3046/1981"**. Não há número de TO no anexo para a ZPP. (Obs.: a extração de texto com pdftotext deu uma linha "ZPP B 2,00" que NÃO existe na imagem da página; a leitura válida é a da imagem.)
- **LC 270/2024, Art. 363 §1º III** (áreas sob o Decreto 3.046 ficam fora da regra geral de afastamento frontal) e **§5º do art. 345** ("Na ZPP, o CAM será igual ao IAA definido em cada Subzona do Decreto nº 3046/1981"). Art. 433 mantém as disposições do Decreto 3.046 na ZPP. Art. 432 fixa TO máxima de 50% para cultos religiosos com testada na Av. das Américas, Subzona A-18 (LC 270, Art. 432).
- **Decreto 3.046/1981, Cap. III (Das Subzonas)**: a TO é fixada **por subzona e, dentro da subzona, por uso** (alíneas a, b, c... de cada subzona) e às vezes por sub-área (áreas A/B/C/D do inciso I, glebas, PALs). Cap. II, Disposições Gerais, não fixa TO numérica geral; o inciso VII do Cap. II exclui varandas abertas da TO.

## 2. Fonte primária usada

- Arquivo: `Decreto3046_1981_PlanoPilotoBaixadaJacarepagua.pdf` (87 pp. do arquivo; texto extraído com `pdftotext -layout`, com contagem de páginas por form feed). Todas as linhas de TO do Cap. III (pp. 6 a 86) foram extraídas e mapeadas; o restante do Cap. III não foi lido integralmente nesta execução.
- Codificação do PDF: acentos aparecem corrompidos na extração bruta; a leitura de valores e de números foi feita com conversão latin1->UTF-8. Os números do mapa são cópia literal das linhas do texto extraído.

## 3. Lote e RIU

- **Não aplicado nesta execução.** O acionamento não identifica lote (matrícula, endereço ou coordenada). Sem lote, a subzona operativa não é determinável, e a subzona do Dec. 3.046 pode não ser a operativa para AP-4 (ver ressalva já registrada em 13/10/2026 no estado de Hely). Para parâmetro de lote: consulta ao RIU/ArcGIS (`LBB_Zoneamento_urbano_vigente`) por lote, conforme skill legal-base-legislativa-bairro.
- Subzona **A-ENS** não foi tocada: não existe no Dec. 3.046 nem na LC 270 (decisão humana, conforme instrução).

## 4. Avisos de vigência

- O próprio PDF do Decreto traz nota "(Subzona A-n revogada pela Lei Complementar 270 de 16/01/2024)" para: A-4 a A-12 (linhas 823 a 1318 do texto extraído), A-23 a A-34 (linhas 2370 a 2999 e 3111), A-38 (linha 3680), A-41 a A-45 (linhas 3888 a 4569). Não há nota de revogação para A-1 a A-3, A-13 a A-22, A-35 a A-37, A-39, A-40 e A-46 no trecho lido. Para as subzonas revogadas, a TO do decreto não deve ser usada sem checagem da LC 270 e do Anexo XXI. Atenção: a revogação consta na nota do próprio decreto; o alcance exato (parcial ou total) deve ser conferido no texto da LC 270 antes de uso em parecer.
- Subzonas com TO "decorrente do I.A.A. e do gabarito" ou "função do número de pavimentos" não têm número fixo: o valor sai da regra da própria subzona, não é número único.

## 5. Mapa de TO por subzona, uso e página (PDF)

Formato: subzona | página do PDF | uso/área (cabeçalho da alínea) | linha de TO como escrita no Decreto. Gerado por extração automática; a leitura integral do Cap. III está nas mesmas páginas. Os valores de TO devem ser citados com a alínea e a página, nunca como TO única da ZPP.

```
-|p2|-|da A.T.E., na área útil mínima das unidades e na taxa de ocupação, devendo, contudo, atender
-|p3|-|áreas computadas no cálculo da A.T.E. e da taxa de ocupação.
-|p3|-|taxa de ocupação.
-|p3|-|necessidades específicas de funcionamento da indústria, mantidos o I.A.A., a taxa de ocupação
A-1|p6|a) Uso Residencial Uni e Multifamiliar|- Taxa de ocupação: 50% (cinqüenta por cento)
A-1|p7|b) Uso multifamiliar para lotes com testada para a Avenida S|- Taxa de ocupação: decorrente do I.A.A. e do gabarito adotados, com máximo de 50%
A-1|p7|b) Uso Comercial|- Taxa de ocupação; 50% (cinqüenta por cento)
A-1|p7|b) Uso Comercial|- Taxa de ocupação 50% (cinqüenta por cento)
A-1|p8|b) Uso Comercial|- Taxa de ocupação: 50% (cinqüenta por cento) no pavimento térreo (plataforma), destinado a
A-1|p8|e) Hostel|- Taxa de ocupação: 50%;
A-2|p9|a) Nos lotes oriundos de parcelamento obedecendo aos critéri|- Taxa de ocupação: 40% (quarenta por cento)
A-2|p9|a) Nos lotes oriundos de parcelamento obedecendo aos critéri|- Taxa de ocupação: 30% (trinta por cento)
A-2|p9|a) Nos lotes oriundos de parcelamento obedecendo aos critéri|- Taxa de ocupação 30% (trinta por cento)
A-2|p9|b) Nos lotes com testada para a Avenida Sernambetiba cuja pr|-Taxa de ocupação: decorrente do I.A.A. e do gabarito adotados, com máximo de 30% (trinta
A-2|p10|b) Nos lotes com testada para a Avenida Sernambetiba cuja pr|- Taxa de ocupação: 50% (cinqüenta por cento) no pavimento térreo (plataforma), destinado a
A-2|p10|c) Nos lotes que não tenham testada para a Avenida Sernambet|- Taxa de ocupação: 40% (quarenta por cento)
A-2|p10|c) Nos lotes que não tenham testada para a Avenida Sernambet|- Taxa de ocupação: 30% (trinta por cento)
A-2|p11|e) Nos lotes oriundos do projeto do Centro da Barra, visados|- Taxa de ocupação: 30% (trinta por cento)
A-2|p11|e) Nos lotes oriundos do projeto do Centro da Barra, visados|- Taxa de ocupação: 50% (cinqüenta por cento) no pavimento térreo (plataforma), destinado a
A-2|p12|e) Nos lotes oriundos do projeto do Centro da Barra, visados|- Taxa de ocupação: 30% (trinta por cento)
A-2|p12|e) Nos lotes oriundos do projeto do Centro da Barra, visados|- Taxa de ocupação: 50%;
A-3|p13|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-3|p13|b) Hotel e Hotel-Residência|- Taxa de ocupação: 30% (trinta por cento) no pavimento térreo (plataforma) destinado a
A-3|p13|c) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-3|p13|d) Hostel|- Taxa de ocupação: 50%;
A-3|p14|a) Uso Residencial Uni e Multifamiliar|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-3|p14|b) Uso Comercial|- Taxa de ocupação: 50% (cinqüenta por cento)
A-5|p15|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-5|p15|b) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-5|p15|b) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-6|p16|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-6|p16|b) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-8|p17|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-8|p18|b) Uso Residencial Multifamiliar|- Taxa de ocupação: 20% (vinte por cento)
A-8|p18|b) Uso Comercial|- Taxa de ocupação: 20% (vinte por cento)
A-9|p19|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-9|p19|b) Uso Residencial Multifamiliar|- Taxa de ocupação: 20% (vinte por cento)
A-9|p19|c) Uso Comercial|- Taxa de ocupação: 20% (vinte por cento)
A-10|p20|a) Nos lotes da área A descrita no inciso I:|- Taxa de ocupação: 50% (cinqüenta por cento)
A-10|p21|b) Nos lotes da área B descrita no inciso I:|- Taxa de ocupação - 50% (cinqüenta por cento)
A-10|p21|b) Nos lotes da área B descrita no inciso I:|- Taxa de ocupação - 40% (quarenta por cento)
A-10|p21|c) Nos lotes da área C descrita no inciso I:|- Taxa de ocupação: 40% (quarenta por cento)
A-10|p22|c) Nos lotes da área C descrita no inciso I:|- Taxa de ocupação: 30% (trinta por cento)
A-12|p23|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-12|p23|b) Uso Residencial Multifamiliar|- Taxa de ocupação: 20% (vinte por cento)
A-13|p24|a) Nos lotes com testada para a Avenida das Américas e para |- Taxa de ocupação: 30% (trinta por cento).
A-13|p24|b) Nos lotes com testada para a Via Parque da Lagoa da Tijuc|- Taxa de ocupação: 30% (trinta por cento)
A-13|p24|b) Nos lotes com testada para a Via Parque da Lagoa da Tijuc|- Taxa de ocupação: 40% (quarenta por cento)
A-13|p25|c) Para as glebas Saco Grande e Saquinho da Tijuca|- Taxa de Ocupação: 40% (quarenta por cento)
A-13|p25|c) Para as glebas Saco Grande e Saquinho da Tijuca|- Taxa de ocupação: 25% (vinte e cinco por cento)
A-13|p25|c) Para as glebas Saco Grande e Saquinho da Tijuca|- Taxa de ocupação: 40% (quarenta por cento)
A-14|p26|-|- Taxa de ocupação: 30% (trinta por cento)
A-15|p26|d) complexo hospitalar, geriátrico e esportivo-recreativo - |- Taxa de ocupação: 25% (vinte e cinco por cento).
A-15|p27|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-15|p27|b) Uso Residencial Multifamiliar|- Taxa de ocupação: 25% (vinte e cinco por cento)
A-15|p27|c) Uso Comercial|- Taxa de ocupação: 40% (quarenta por cento)
A-15|p28|d) complexo hospitalar, geriátrico e esportivo-recreativo - |- Taxa de ocupação: 25% (vinte e cinco por cento);
A-16|p29|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-16|p29|b) Uso Residencial Multifamiliar|- Taxa de ocupação: 25% (vinte e cinco por cento)
A-16|p29|c) Uso Comercial|- Taxa de ocupação: 40% (quarenta por cento)
A-17|p31|a) Nos lotes especiais já urbanizados de acordo com o Projet|- Taxa de Ocupação: 40% (quarenta por cento)
A-17|p31|b) Nos lotes resultantes de parcelamento anterior ao Plano P|- Taxa de ocupação: 10% (dez por cento)
A-17|p31|d) Uso Comercial|- Taxa de ocupação: 20% (vinte por cento)
A-17|p31|e) Uso Especial de Interesse Social|taxa de ocupação utilizados, com predominância horizontal, até o máximo de 8 (oito)
A-17|p31|e) Uso Especial de Interesse Social|- Taxa de Ocupação: 20% (vinte por cento)
A-18|p33|a) Uso Residencial Unifamiliar|- Taxa de ocupação: 40% (quarenta por cento)
A-18|p33|c) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-18|p33|c) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-18|p33|c) Uso Comercial|- Taxa de Ocupação:16% (dezesseis por cento)
A-19|p34|a) Serão permitidas apenas edificações destinadas às seguint|- Taxa de Ocupação: 10% (dez por cento)
A-20|p35|a) Uso Residencial, Uni e Multifamiliar|- Taxa de ocupação: 50% (cinqüenta por cento)
A-20|p36|b) Uso Multifamiliar para lotes com testada para a Avenida S|- Taxa de Ocupação: decorrente do I.A.A. e do gabarito adotados, com máximo de 50%
A-20|p36|c) Uso Comercial|- Taxa de ocupação: 50% (cinqüenta por cento)
A-20|p36|c) Uso Comercial|- Taxa de ocupação: 50% (cinqüenta por cento)
A-20|p36|c) Uso Comercial|- Taxa de ocupação 50% (cinqüenta por cento) no pavimento térreo (plataforma), destinado a
A-20|p37|e) Hostel:|- Taxa de ocupação: 50%;
A-21|p38|a) No Centro de Sernambetiba:|- Taxa de ocupação máxima: 50%;
A-21|p38|a) No Centro de Sernambetiba:|- taxa de ocupação máxima: 75% para o embasamento e 40% para a lâmina
A-21|p39|a) No Centro de Sernambetiba:|- taxa de ocupação máxima: 85% para o embasamento e 35% para a lâmina
A-21|p40|a) No Centro de Sernambetiba:|- Taxa de Ocupação máxima:75% para o embasamento e 40% para a lâmina
A-21|p40|a) No Centro de Sernambetiba:|- taxa de ocupação: 30%
A-21|p40|a) No Centro de Sernambetiba:|- taxa de ocupação: 50%
A-21|p41|b) Na área denominada Gleba Finch (traçado original conforme|- Taxa de ocupação: 50% (cinqüenta por cento) da área do lote
A-21|p42|b) Na área denominada Gleba Finch (traçado original conforme|- Taxa de ocupação: 50% (cinqüenta por cento)
A-21|p42|b) Na área denominada Gleba Finch (traçado original conforme|- Taxa de ocupação: 50% (cinqüenta por cento), no pavimento térreo (plataforma), destinado a
A-21|p42|c) Hostel:|- Taxa de ocupação: 50%;
A-22|p43|a) Nos lotes da área A descrita no inciso I:|- Taxa de ocupação: 30% (trinta por cento)
A-22|p43|a) Nos lotes da área A descrita no inciso I:|- Taxa de ocupação: 30% (trinta por cento)
A-22|p43|b) Nos lotes da área B descrita no inciso I:|- Taxa de ocupação: 10% (dez por cento)
A-22|p44|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-22|p44|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-23|p44|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 30% (trinta por cento)
A-23|p45|b) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-24|p46|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-24|p46|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-24|p46|b) Nos lotes da área B descrita no inciso I:|- Taxa de ocupação: 10% (dez por cento)
A-24|p46|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-24|p47|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-25|p47|a) Nos lotes da área A descrita no inciso I:|- Taxa de ocupação: 30% (trinta por cento)
A-25|p48|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por centro)
A-25|p48|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-25|p48|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-26|p49|a) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-26|p49|b) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-27|p50|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-27|p50|b) Uso Multifamiliar|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-27|p50|c) Uso Comercial|- Taxa de ocupação: 30% (trinta por cento)
A-27|p51|d) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-28|p51|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-28|p52|a) Uso Residencial Unifamiliar|- Taxa de Ocupação : 50% (cinqüenta por cento)
A-29|p53|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-29|p53|b) Uso Residencial Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-30|p54|a) Uso Residência Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-30|p54|b) Uso Residencial Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-31|p56|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-31|p56|b) Uso Residencial Multifamiliar|- Taxa de ocupação: função do número de pavimentos:
A-31|p57|c) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-31|p57|d) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-33|p59|e) Hotel|- Taxa de Ocupação: 40% (quarenta por cento)
A-33|p59|b) Uso Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-33|p59|c) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-33|p59|d) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-33|p59|e) Hotel|- taxa de ocupação: cinquenta por cento no pavimento térreo (plataforma),destinado a serviços
A-33|p60|e) Hostel:|- Taxa de ocupação: 50%;
A-35|p61|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-35|p61|b) Uso Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-35|p61|c) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-35|p62|d) Uso Industrial|- Taxa de ocupação: 40% (quarenta por cento)
A-36|p62|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-36|p63|b) Uso Residencial Multifamiliar|- Taxa de Ocupação: função do número de pavimentos: até 6 (seis) pavimentos - 50%
A-36|p63|c) uso comercial, cultural, serviços e turístico:|- taxa de ocupação: trinta por cento
A-36|p63|c) uso comercial, cultural, serviços e turístico:|- taxa de ocupação: 30 % (trinta por cento)
A-36|p63|d) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-36|p64|e) Hotel|- taxa de ocupação: cinquenta por cento no pavimento térreo (plataforma), destinada a serviços
A-36|p64|e) Hotel|- Taxa de ocupação: 50%;
A-37|p66|b) Intensidade de Uso|- Taxa de ocupação: 30% (trinta por cento)
A-37|p67|e) Estacionamento|Taxa de Ocupação: 40% (quarenta por cento)
A-38|p69|a) No Loteamento Gardênia Azul|- Taxa de Ocupação: 50% (cinquenta por cento)
A-38|p69|b) Nos lotes não pertencentes ao Gardênia Azul|- Taxa de Ocupação: 40% (quarenta por cento)
A-38|p69|b) Nos lotes não pertencentes ao Gardênia Azul|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-38|p70|b) Nos lotes não pertencentes ao Gardênia Azul|- Taxa de Ocupação: 40% (quarenta por cento)
A-38|p70|b) Nos lotes não pertencentes ao Gardênia Azul|- Taxa de Ocupação: 40% (quarenta por cento)
A-39|p71|b) Na área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-39|p71|b) Uso Residencial Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-39|p71|c) Uso Comercial|- Taxa de ocupação: 20% (vinte por cento)
A-40|p72|-|- Taxa de Ocupação: 10% (dez por cento)
A-41|p73|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 40% (quarenta por cento)
A-41|p73|a) Uso Residencial Unifamiliar|- Taxa de Ocupação: 10% (dez por cento)
A-41|p74|b) Uso Residencial Multifamiliar|- Taxa de Ocupação: 20% (vinte por cento)
A-41|p74|c) Uso Comercial|- Taxa de Ocupação: 30% (trinta por cento)
A-41|p74|d) Uso Industrial|- Taxa de Ocupação: 40% (quarenta por cento)
A-42|p75|a) Uso Industrial|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-43|p76|a) Nos lotes constantes do PAL nº 32.744, os critérios deter|- Taxa de Ocupação: 26% (vinte e seis por cento).
A-44|p79|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-44|p79|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-44|p79|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-44|p79|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-44|p80|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 50% (cinqüenta por cento)
A-44|p80|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 25% (vinte e cinco por cento)
A-44|p80|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 35% (trinta e cinco por cento)
A-44|p81|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 50% (cinquenta por cento)
A-44|p81|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 40% (quarenta por cento)
A-44|p81|c) Nos lotes da área C descrita no inciso I:|- Taxa de Ocupação: 50% (cinquenta por cento)
A-44|p81|c) Nos lotes da área C descrita no inciso I:|- Taxa de Ocupação: 50% (cinquenta por cento)
A-44|p81|c) Nos lotes da área C descrita no inciso I:|- Taxa de Ocupação: 35% (trinta e cinco por cento)
A-44|p82|c) Nos lotes da área C descrita no inciso I:|- Taxa de Ocupação: 50% (cinquenta por cento)
A-44|p82|c) Nos lotes da área C descrita no inciso I:|- Taxa de Ocupação: 40% (quarenta por cento)
A-44|p82|d) Nos lotes da área D descrita no inciso I:|- Taxa de Ocupação: 40% (quarenta por cento)
A-44|p82|d) Nos lotes da área D descrita no inciso I:|- Taxa de Ocupação: 20% (vinte por cento)
A-44|p83|d) Nos lotes da área D descrita no inciso I:|- Taxa de Ocupação: 40% (quarenta por cento)
A-45|p83|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-45|p84|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: (soma da projeção das edificações) - 30% (trinta por cento) da área do
A-45|p84|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-45|p84|b) Nos lotes da área B descrita no inciso I:|- Taxa de ocupação: 10% (dez por cento)
A-45|p84|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: (soma da projeção das edificações ) - 10% (dez por cento) da área dos
A-46|p85|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: 30% (trinta por cento)
A-46|p85|a) Nos lotes da área A descrita no inciso I:|- Taxa de Ocupação: (soma da projeção das edificações) - 30% (trinta por cento) da área do
A-46|p86|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: 10% (dez por cento)
A-46|p86|b) Nos lotes da área B descrita no inciso I:|- Taxa de Ocupação: (soma da projeção das edificações) - 10% (dez por cento) da área dos
```

