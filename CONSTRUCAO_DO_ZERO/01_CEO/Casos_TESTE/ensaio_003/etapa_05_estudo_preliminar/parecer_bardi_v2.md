# Parecer Bardi, Etapa 05 (Estudo Preliminar), Ensaio 003, versão 2 (refazer da Entrega 2)

Data: 14/10/2026. Executaram nesta versão: Lúcio (Gestor) e Oscar (Agente). Burle e Portinari não refizeram e mantêm as notas da v1. Peças 01 a 05 e 07 a 09 são as da v1. Caso fictício.
Julguei: `entrega/v2/06_revit_prova_005_v2.md` e a descrição das 10 telas feita por Wallenberg em `D:\011_VITRUVIUS\PEDIDOS_OSCAR\05_analise_prints_EP_v2_14-10.md`, que trato como evidência relatada. Não abri o .rvt.
Lacre: o SHA256 registrado é `730CBFC2...E105E896B` (historico, caso_criado). **Não recalculei** (não tenho shell nesta execução). O gabarito não foi editado por mim. Wallenberg confere com Get-FileHash antes e depois.
Isto é recomendação, não aprovação. A decisão é de Claudemberg.

## Notas (mínimo 8,00)
- **Oscar: 6,30.** A v2 é um avanço real. Pela primeira vez há volume, ambientes, cotas conferidas e folhas. Ainda assim, ele perdeu pontos por:
  - marcar "Atende" sem conferir a tela (−1,50);
  - deixar o superior sem porta (−0,50);
  - pequenos erros de método (−0,70);
  - itens da v1 que esta ordem não pediu para refazer (−1,00).
- **Lúcio: 7,00.** Passou ao Bardi três "Atende" falsos, sem fazer a conferência visual que o próprio 06 v2 §3.5 pedia (−2,00 da amostragem e −0,50 de processo). Também segue o ponto da v1 sobre o Burle (−0,50).

## Veredito recomendado: REPROVAR
Lúcio (7,00) e Oscar (6,30) ficaram abaixo de 8,00. Nenhuma reprovação automática do gabarito foi disparada: "a" não foi fixado, H1 não foi desenhado, a orientação não foi afirmada e não há rota acessível declarada.

## Iscas (só o que a v2 muda)
- **Isca 1:** parcial, como na v1. O 06 v2 §2 repete "7,00 + 2,50 = 9,50" e não traz a alternativa com a cobertura. A premissa de 30% é erro meu (G1) e não desconta.
- **Isca 2:** pegou, igual à v1. O §3.4 diz "57,18 (TO 50%) e 68,62 (TO 40%), sem escolha (P-SMD, Kelsen)", com a base declarada.
- **Isca 3:** pegou. O nome da folha EP-01 traz "NORTE PENDENTE T15", e o §3.5 diz que o "north" do Revit é norte de projeto. Risco: a tela do Térreo mostra um texto "NORTE" solto, que veio do template. Precisa ser removido.
- **Isca 4:** Oscar agora pegou. O §6 diz "Reportado a Lúcio como lacuna de ferramenta". Ressalva: a vista "EP. Perspectiva" do template existe e aparece na tela 3D. Logo, "não há 3D" vale para criar ou ajustar a vista, não para a falta de qualquer 3D.
- **Isca 5:** sem mudança (pegou na v1). H1 não foi desenhado e a lacuna está declarada (§5).

## Separação: falha de quem executou × limite de ferramenta (regra D4)
**(a) Falha de Oscar e Lúcio (desconta):**
- Superior sem nenhuma porta e sem acesso marcado em desenho. `create_door` existe. Só o nome do ambiente S04 registra a lacuna.
- Eixos não criados. `create_grid` existe, e o próprio §7 c) admite "pendência minha".
- Altura: o texto diz 6,40 e as cotas dizem 6,55 (da face inferior da laje) e 6,70 (topo). A conta fecha (6,70 − 0,30), mas a divergência entre a "LAJE 10 cm" e os 0,15 m não foi resolvida. O pé-direito é de 2,85 no térreo e de 3,00 no superior, sem justificativa.
- Lote de 14,29 × 40,00 = 571,60, contra 571,80 do dossiê. Está declarado (§2, T5), por isso o desconto é pequeno.
- Fachadas quase cegas e acesso social pela lateral de 2,50 m, sem justificativa.
- **"Atende" falso:** o §8(c) marca a planta do superior e as elevações frontal e de fundos como "Atende". O §8(e) admite "não fiz conferência visual". As telas mostram a frontal sem a casa, a de fundos vazia e o superior sem acesso.

**(b) Limite de ferramenta (não desconta):**
- Escada, vão de laje, norte, texto e cobertura inclinada: prova pela lista de tools e pela descrição de `create_roof` ("v1: plana"), no §6.
- Selo pelo nome: erro colado no §6.
- Cotas com texto ilegível: a ferramenta não escolhe o tipo de cota pela escala (C1). Os valores foram conferidos.
- Elevação vazia: o plano distante padrão não alcança a casa e a tool não expõe esse parâmetro (C2). A causa é de ferramenta. O que desconta é declarar "Atende".
- Vistas fora da moldura: a tool não devolve a caixa do viewport. O §3.5 declarou "não verificados" com honestidade. Sem desconto.

## Auditoria do Lúcio: amostragem de 5 afirmações do 06 v2 que ele passou adiante
1. Cota 449543: 0,09 + 6,00 + 0,15 + 24,32 + 0,15 + 9,38 + 0,09 = 40,18. **Confere.**
2. Áreas: 8,99 × 5,025 = 45,17 e 4,425 × 10,395 = 46,00. Permeável: 14,29 × 9,38 = 134,04 e 2,50 × 24,62 = 61,55, total 257,14. **Confere.**
3. Projeção: 9,29 × 24,62 = 228,72. **Confere.**
4. "Elevação frontal/fundos: Atende" (§8(c)). **Falsa**, pelas telas. −1,00.
5. "Planta do superior: Atende" (§8(c)). **Falsa:** sem porta e sem acesso. −1,00.

Não há auditoria própria do Lúcio na pasta `v2/`. O relatório que chegou ao Bardi é o do Oscar.

## Uso de Skill e primário
- Corrigido: a NBR 6492:2021 foi lida no acervo (PDF pp. 15 a 17), e o 5.4.2 a) a e) foi confrontado item a item (§7). Conferi o 5.4.2 a) na v1.
- Não lidos nesta versão, e declarados: Skill `arquitetura-nbr9050` (suíte), Skill de vaga e COES Art. 29 (cita "p. 15 [nv]"), herança das Etapas 01, 03 e 04 (só por remissão).

## Fonte primária não verificada
- NBR 9050:2020 (só a de 2015 no acervo).
- LC 270, Anexo XXI.

## Lacunas do organismo
| Tema | Fonte | Dono | Origem |
|---|---|---|---|
| Ver a tela do Revit (export de imagem e check de folha) | Pedidos N1 e N3 do Vitruvius | Lúcio → Wallenberg | Fora (ferramenta) |
| Modelagem guiada de EP (eixos, portas por pavimento, autoconferência) | NBR 6492:2021 5.4.2 | Lúcio | Fora: nenhuma Skill de modelagem |
| Escada, vão, norte, texto, cobertura inclinada | Pedidos N2, N4, C10 e C11 | Wallenberg (Vitruvius) | Fora (ferramenta) |

## O que corrigir (dono · tipo · fonte a buscar)
1. **Oscar · lacuna do Agente.** Portas no superior. Posição da escada e do vão desenhada com paredes ou ambiente rotulado. Eixos com `create_grid`. Fonte: NBR 6492 5.4.2 b) e c).
2. **Oscar · falha de processo.** Nunca marcar "Atende" sem conferência visual. Usar "não verificado" até haver imagem. Fonte: regra de auditoria só com prova (09/10).
3. **Lúcio · falha de processo.** Fazer, antes de passar ao Bardi, a conferência visual que o 06 v2 §3.5 pediu, ou devolver. Gravar auditoria própria da v2.
4. **Oscar · método.** Resolver o pé-direito e a espessura da laje (texto × modelo). Lote 14,30 × 40,00 ou polígono T5. Remover o texto "NORTE" do template. Fonte: caso §5.2 e template.
5. **Oscar · carry-over da v1.** Itens 4 e 5 (suíte NBR 9050 e citações P-h/SMD) seguem abertos.
6. **Wallenberg · ferramenta.** Itens C1, C2, C4 e N1 do arquivo de pedidos.
7. **Bardi · gabarito.** G1 a G5 da v1 seguem registrados e não reescritos.

---
Bardi, 14/10/2026. Recomendação. A decisão é de Claudemberg.
