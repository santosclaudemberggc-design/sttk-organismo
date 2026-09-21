# _estado_fiker.md

## 1. Onde parei / Em andamento
- **21/09/2026 — Caso Sombra 002 (ENSAIO/TESTE, `01_CEO/Casos_TESTE/Barra_da_Tijuca/ensaio_002/`).** Villaça pediu estimativa de revenda para 2 cenários fictícios (CAB ~400m² e CAM ~800m², casa unifamiliar, 4 suítes, padrão médio-alto, Barra da Tijuca). Entreguei comparáveis reais para ambos os cenários, aplicando o método corrigido (tipo → padrão → metragem, sem extrapolar média de bairro). Reportei a Villaça, não editei o Pré-Estudo (quem integra é ele).
- Cenário CAB (~400m²): 3 comparáveis confirmados via MGF Imóveis (Condomínio Blue Houses 400m²/R$5,5mi; Barra de Itaúna 336m²/R$2,87mi; Mandala 556m²/R$4,8mi — este último fora da faixa, usado só como referência de tendência).
- Cenário CAM (~800m²): 1 comparável forte confirmado individualmente (Alphaville Barra, triplex 800m² útil/656m² terreno, 5 suítes, R$12,9mi, via Azuza Imóveis). Tentei confirmar um 2º comparável (MGF, mansão 700m², 5 suítes, R$6,5mi) mas o link individual redirecionou pra página de busca genérica (301) — não consegui abrir o anúncio específico, não usei o número isolado, mas registrei como sinal de mercado (mesma faixa de metragem, preço bem mais baixo que o Alphaville — provável diferença de padrão de condomínio, não erro).
- Primeira execução (18/09/2026, Caso 001 Recreio) segue registrada no aprendizado da Seção 3.

## 2. Pendências abertas
- [ABERTO] Não consegui abrir individualmente nenhum anúncio do VivaReal/ZAP para a Rua Flávio Carvalho Molina (403/bloqueio de fetch) — a fragilidade de fonte que Villaça já tinha sinalizado continua sem solução técnica minha. Se algum dia eu tiver acesso a um MCP de scraping ou a uma chave de API de portal imobiliário, isso resolveria essa lacuna de verdade.
- [ABERTO] Minha resposta trouxe uma 3ª hipótese (efeito de tamanho dentro do mercado "normal", distinto de erro de classificação e de diferença de bairro) que Villaça não tinha levantado — fica para ele decidir se incorpora ao documento.
- [ABERTO] Caso 002 CAM (~800m²): só tenho 1 comparável individualmente confirmado (Alphaville, R$12,9mi). Precisaria de mais 1-2 comparáveis reais pra amostra mais robusta nessa metragem — VivaReal e Realiza Imóveis bloquearam o fetch (403 / página sem listagem individual), e o link do MGF de 700m² redirecionou pra busca genérica. Se Villaça quiser mais força estatística nesse cenário, vale eu tentar de novo com outro portal ou aguardar acesso a ferramenta de scraping.

## 3. Aprendizados que não posso esquecer
- Quando a mesma rua/condomínio tem unidades menores com R$/m² MUITO mais alto que unidades maiores (mesmo padrão nominal), isso é um padrão conhecido de mercado imobiliário "normal" (terreno tem custo relativamente fixo por unidade, banheiros por quarto/suíte custam mais que m² de área bruta) — mas o oposto acontece no nicho de mansão/alto padrão (Barra da Tijuca, onde maior=mais caro por m², por escassez/prestígio). Não assumir que o efeito de tamanho é sempre na mesma direção — depende do segmento de mercado.
- Proporção de banheiros muito alta em relação a quartos (ex.: 5 quartos/7-8 banheiros) é um sinal de alerta técnico: pode indicar unidade configurada para renda/multi-família informal, não residência unifamiliar "pura" — isso pode derrubar o R$/m² de revenda para comprador família, mesmo em bairro/padrão nominal razoável. Vale sempre olhar essa proporção ao classificar padrão de um comparável.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
