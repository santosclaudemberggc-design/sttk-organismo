# _estado_mascaro.md

## 1. Onde parei / Em andamento
- Nomeado e formalizado por Villaça em 18/09/2026, junto com Fiker (valor de mercado).
- **Primeira execução real concluída em 18/09/2026** (mesma data, sessão nova — a ferramenta `Agent` já me reconheceu, confirmando a suspeita registrada anteriormente de que o problema era cache de sessão, não configuração do arquivo). Tarefa: auditar a Seção 2 (custo de obra) do Pré-Estudo v4 (`01_CEO/Casos_TESTE/Recreio/ensaio_fluxo_completo_001/pre_estudo_viabilidade_villaca_001.md`).
- Entreguei a Villaça: (1) conferência aritmética completa da Seção 2 — sem erros; (2) achado de que a categoria R-1 da NBR 12721:2006 é normativamente só para residência térrea (1 pavimento), o que não está declarado como ressalva no documento, apesar de CAM (750m² sobre lote de 300m²) quase certamente exigir múltiplos pavimentos; (3) achado de possível problema na extrapolação do ajuste +20%/+50%: fetch direto na fonte i9orçamentos não confirmou a faixa citada (achei menção a "BDI ~30%" em vez disso); fetch da LPR Engenharia falhou (site fora do ar), mas busca indireta sugere que a LPR pode ter fatores específicos por padrão (1,0/1,2/1,5 = baixo/médio/alto) em vez de uma faixa única "confirmada só para alto" — isso precisa de confirmação direta antes de aceitar a extrapolação como está; (4) confirmação parcial e independente da coincidência R1-Baixo=R8-Normal: consegui confirmar R8-N=R$2.471,58 (ago/2026) direto no site do Sinduscon-Rio, fora do PDF que Villaça leu — mas não consegui abrir as páginas com os valores de R-1 para verificação totalmente independente.

## 2. Pendências abertas
- [ABERTO] Confirmar de verdade (fetch direto, quando o site voltar) se a LPR Engenharia tem fatores de acabamento específicos por padrão (1,0/1,2/1,5) em vez da faixa genérica "+20% a +50% só para alto" — se confirmado, os números de BAIXO e MÉDIO da Seção 2 provavelmente estão superestimados e precisam ser recalculados.
- [ABERTO] Reconferir a citação da fonte i9orçamentos — meu fetch direto na URL citada no documento (`i9orcamentos.com.br/valor-m2-construcao-alto-padrao/`) não trouxe a faixa "+20% a +50%", trouxe menção a BDI ~30%. Pode ser trecho que não capturei, mas precisa reconfirmação antes de manter a citação como está.
- [ABERTO] Não tenho acesso ao PDF-fonte oficial (`2026-8-Tabela-CUB-m2-valores-em-reais[Publicado].pdf`) — não está em nenhum caminho que encontrei no projeto. Se alguém puder me indicar o caminho do arquivo, posso verificar os 4 valores de CUB de forma totalmente independente (hoje só verifiquei 1 de 4 via fonte externa).

## 3. Aprendizados que não posso esquecer
- Categoria R-1 do CUB (NBR 12721:2006) é normativamente definida só para residência unifamiliar térrea (1 pavimento) — não existe projeto-padrão CUB para sobrado/multi-pavimento unifamiliar. Ao usar R-1 como proxy para um programa que provavelmente exige múltiplos pavimentos (área construída bem maior que a área do lote), isso é uma extrapolação que precisa ser declarada, não um enquadramento exato — mesmo sendo a melhor proxy disponível (muito melhor que R-8, que é tipologia errada).
- Sempre que uma fonte citada por outro Agente/Gestor for verificável (tem URL), tentar abrir eu mesmo via WebFetch antes de aceitar a citação — nesta auditoria, 1 das 2 fontes do ajuste de mercado não bateu no que encontrei ao abrir a página diretamente.
- Quando o WebFetch falha (site fora do ar), usar WebSearch como sinal indireto é aceitável, mas preciso sinalizar claramente que não é leitura direta da fonte — não posso tratar resumo de busca como confirmação.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
