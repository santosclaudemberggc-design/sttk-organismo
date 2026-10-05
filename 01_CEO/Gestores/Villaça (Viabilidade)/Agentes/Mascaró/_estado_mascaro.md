# _estado_mascaro.md

## 1. Onde parei / Em andamento
- **Ensaio 003, Etapa 02 — v6 entregue em 05/10/2026** (`.../entrega/v6/custo_obra_mascaro_003_v6.md`; v1 a v5 intactas). Bardi reprovou a v5 (erro 2: áreas da Etapa 01 como "[DOC — Etapa 01]"; ressalva do playground). v6: [PL] na legenda e em toda área ou conclusão do Legal; nota do CUB transcrita literalmente (PDF reaberto em 05/10); alternativa ago/26 = "índice do mês anterior ao da proposta, leitura usada em alguns contratos"; Cronoshare = "página datada de 02/01/2026"; Skill v1.4; varredura de 71 itens. Extras corrigidos: somas de plataforma/elevador eram apresentadas como "preço da fonte"; "aterro de +3,20 m" (é cota de soleira); a v5 citava a Skill v1.2 com a v1.3 em vigor; fator 1,0025 é exato, não aproximação. Nenhum número mudou. Aguardo Villaça/Bardi.
- Casos anteriores (001 Recreio, 002 Barra): entregues. Histórico no git.

## 2. Pendências abertas
- [ABERTO] Sem percentual citável de acréscimo do CUB R-1 (térrea, NBR 12.721) para sobrado. Ressalva só qualitativa.
- [ABERTO] Sem fonte para acabamento "alto padrão" de mercado acima do memorial R-1 Alto.
- [ABERTO] Remuneração do construtor: uso o BDI do TCU (Acórdão 2622/2013, Edifícios 20,34/22,12/25,00%) como ordem de grandeza. É de obra pública, logo extrapolação. Falta fonte de BDI de construtora privada residencial.
- [PARCIAL] Hélice contínua: SINAPI 100651 (Ø30, R$ 139,38/m) e 100652 (Ø50, R$ 255,98/m), 07/2026, média nacional via orcamentor, consistentes com concreto. Falta preço RJ e Ø40 (100650 = 404).
- [ABERTO] Elevador/plataforma residencial: só fonte jornalística fraca (Monitor do Mercado 24/08/2026). Falta tabela de fabricante.
- [ABERTO] Tabela de Honorários CAU/BR oficial: não lida. Projetos e aprovações seguem [NC].
- [ABERTO] Curva de R$/m² de custo por faixa de área no mesmo padrão: sem fonte formal (vem do caso 002).

## 3. Aprendizados que não posso esquecer
- **Fontes que funcionam:** a página `sinduscon-rio.com.br/wp/servicos/custo-unitario-basico/` lista os PDFs do mês. O padrão de URL é `/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-<mes>-de-<ano>.pdf`, mais "Evolucao-e-composicao-..." e "Precos-medianos-...". A página `/cub` dá erro fatal. Para INCC-M, a primária é `portal.fgv.br/noticias/incc-m-<mes>-<ano>`. Brasil Indicadores e VRI têm a série mês a mês e o número-índice.
- **PDF pelo WebFetch vem binário:** usar Read no arquivo que ele salva em tool-results. Funcionou para Sinduscon e TCU.
- **Projeção de índice:** dar faixa com dois métodos (mesma janela do ano anterior × média 12m composta) e avisar do dissídio de maio (CUB-Rio MO +4,42% em mai/2026).
- **Testar consistência do preço unitário:** antes de usar um preço de agregador, conferir contra insumo da fonte primária (ex.: concreto R$ 587,50/m³ × volume por metro de estaca). Pegou o ORSE inconsistente.
- **Técnica do preço = técnica do solo:** composição SINAPI de outra técnica (escavada sem fluido) não serve para solo com NA raso. Ler a descrição antes de usar o preço.
- **Base de área (reprovação 02/10):** CUB NUNCA sobre área computável. Usar área equivalente NBR 12721 (Skill `viabilidade-cub-nbr12721-...`), faixa piso/teto, base declarada linha a linha. Checklist §2.4 completo, inclusive elevador/plataforma quando houver idoso/cadeirante no programa — ler o programa do cliente à procura de equipamento.
- **Reajuste vai até o fim do desembolso, não até o início da obra** (reprovação v2). Usar a taxa mensal implícita já adotada; piso = mês médio (linear), teto = fim da obra, salvo se houver cronograma. Itens fora do CUB também se reajustam. [ABERTO] Falta fonte lida que diga literalmente "reajuste por medição pelo INCC". A minuta da PF/PE 2018 (cl. 3.3) só sustenta o reajuste anual.
- **Proposta de construtora:** é preço (com BDI e itens fora do CUB), n = 1, não é benchmark. Conferir área contra a lei, "chave na mão" contra a lista de não inclusos, fundação contra a sondagem, reajuste e validade.
- **Ler e citar LITERALMENTE a cláusula do documento do caso antes de dizer "não declara"** (reprovação v3: afirmei 3 versões seguidas que a 5.12 não tinha mês-base, e ela tinha). Documento do caso é a fonte primária; macete/contrato público é só apoio. Separar [DOC] (o que o texto diz) de [PV] (o que eu deduzo, ex.: fim da obra = prazo de mudança).
- **Data declarada ≠ número-índice declarado** (reprovação v4). "A partir da data da proposta" não diz se o índice-base é o do mês ou do mês anterior: isso é [PV], com alternativa e efeito. Antes de entregar, varrer o arquivo inteiro atrás de [FP]/[DOC]/"declara"/"literal"/"não premissa" e conferir cada um contra a fonte; acumulado composto por mim é [ECF], mesmo com taxas [FP].
- **Todo item com valor recebe data-base e reajuste** (plataforma, demolição). FGV `incc-m-<mes>-<ano>` não traz acumulado no ano: compor com a tabela de variações mensais da própria matéria. Fator no mês médio ≠ média dos fatores: declarar a diferença com a conta, não "de segunda ordem".
- **[DOC] é só Dossiê/caso base; número ou conclusão do Legal (Etapa 01) é [PL]** (reprovação v5). Nunca esticar uma legenda para caber um rótulo, e a mesma área tem o mesmo rótulo em toda a entrega. Toda exclusão do CUB citada como [FP] leva a condição literal do PDF (ex.: playground "quando não classificado como área construída"). Soma minha de faixas da fonte é [ECF], nunca "preço da fonte". Data de página/artigo ≠ data do preço.
- Exemplo ilustrativo do cliente ou de Claudemberg não vira dado. Sempre achar e citar a minha fonte.
- 2ª via por % do VGV (TBO, 40–55% para construção) e ajuste sobre o CUB são vias diferentes. Não apresentar uma como a outra. Sinal do lado da revenda não é fonte de custo.
- R-1 da NBR 12.721 = térrea. Usar para sobrado é extrapolação declarada. "Médio-alto" não existe no CUB: interpolar entre Normal e Alto e declarar.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
