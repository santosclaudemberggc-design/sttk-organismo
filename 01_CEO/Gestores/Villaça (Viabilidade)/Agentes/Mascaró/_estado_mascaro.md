# _estado_mascaro.md

## 1. Onde parei / Em andamento
- **Ensaio Sombra 003, Etapa 02 (02/10/2026):** custo de obra entregue a Villaça para auditoria em `01_CEO/Casos_TESTE/ensaio_003/etapa_02_viabilidade/entrega/custo_obra_mascaro_003.md`. Base: CUB Sinduscon-Rio Set/2026 (R-1 A 3.691,68; R-1 N 2.990,86) e INCC-M Set/2026 (12 meses: 6,61%). Parcela calculável do S1 em mai/27 ficou em R$ 2,12–2,26 mi. O resto ficou como [NC], com a fundação profunda como maior incógnita. Proposta 5.12 tratada item por item. Aguardo a auditoria de Villaça e o parecer de Bardi.
- Casos anteriores (001 Recreio, 002 Barra): entregues. Histórico no git.

## 2. Pendências abertas
- [ABERTO] Sem percentual citável de acréscimo do CUB R-1 (térrea, NBR 12.721) para sobrado. Ressalva só qualitativa.
- [ABERTO] Sem fonte para acabamento "alto padrão" de mercado acima do memorial R-1 Alto.
- [ABERTO] Remuneração do construtor: uso o BDI do TCU (Acórdão 2622/2013, Edifícios 20,34/22,12/25,00%) como ordem de grandeza. É de obra pública, logo extrapolação. Falta fonte de BDI de construtora privada residencial.
- [ABERTO] Preço de estaca hélice contínua no RJ: não obtido. ORSE-11360 (R$ 40/m) é inconsistente com o preço do concreto. SINAPI 107120/107130 é escavada sem fluido, que não serve abaixo do NA. Próxima tentativa: preço RJ da composição SINAPI de hélice contínua (caderno técnico da Caixa existe).
- [ABERTO] Tabela de Honorários CAU/BR oficial: não lida. Projetos e aprovações seguem [NC].
- [ABERTO] Curva de R$/m² de custo por faixa de área no mesmo padrão: sem fonte formal (vem do caso 002).

## 3. Aprendizados que não posso esquecer
- **Fontes que funcionam:** a página `sinduscon-rio.com.br/wp/servicos/custo-unitario-basico/` lista os PDFs do mês. O padrão de URL é `/wp/wp-content/uploads/2021/01/Custos-Unitarios-Basicos-de-Construcao-<mes>-de-<ano>.pdf`, mais "Evolucao-e-composicao-..." e "Precos-medianos-...". A página `/cub` dá erro fatal. Para INCC-M, a primária é `portal.fgv.br/noticias/incc-m-<mes>-<ano>`. Brasil Indicadores e VRI têm a série mês a mês e o número-índice.
- **PDF pelo WebFetch vem binário:** usar Read no arquivo que ele salva em tool-results. Funcionou para Sinduscon e TCU.
- **Projeção de índice:** dar faixa com dois métodos (mesma janela do ano anterior × média 12m composta) e avisar do dissídio de maio (CUB-Rio MO +4,42% em mai/2026).
- **Testar consistência do preço unitário:** antes de usar um preço de agregador, conferir contra insumo da fonte primária (ex.: concreto R$ 587,50/m³ × volume por metro de estaca). Pegou o ORSE inconsistente.
- **Técnica do preço = técnica do solo:** composição SINAPI de outra técnica (escavada sem fluido) não serve para solo com NA raso. Ler a descrição antes de usar o preço.
- **Proposta de construtora:** é preço (com BDI e itens fora do CUB), n = 1, não é benchmark. Conferir área contra a lei, "chave na mão" contra a lista de não inclusos, fundação contra a sondagem, reajuste e validade.
- Exemplo ilustrativo do cliente ou de Claudemberg não vira dado. Sempre achar e citar a minha fonte.
- 2ª via por % do VGV (TBO, 40–55% para construção) e ajuste sobre o CUB são vias diferentes. Não apresentar uma como a outra. Sinal do lado da revenda não é fonte de custo.
- R-1 da NBR 12.721 = térrea. Usar para sobrado é extrapolação declarada. "Médio-alto" não existe no CUB: interpolar entre Normal e Alto e declarar.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
