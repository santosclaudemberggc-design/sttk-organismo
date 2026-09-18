# _estado_fiker.md

## 1. Onde parei / Em andamento
- **Primeira execução real aconteceu em 18/09/2026** (sessão nova — a ferramenta `Agent` já me reconheceu, confirmando que a limitação anterior era só de cache de sessão). Villaça me acionou para revisar a Seção 3.2 do Pré-Estudo (`01_CEO/Casos_TESTE/Recreio/ensaio_fluxo_completo_001/pre_estudo_viabilidade_villaca_001.md`), especificamente a inversão MÉDIO < BAIXO no cenário CAM (750m²). Entreguei parecer técnico completo (não editei o documento — quem integra é Villaça).
- Busquei (WebSearch/WebFetch) mais comparáveis na mesma rua (Flávio Carvalho Molina, Recreio) para engordar a amostra do MÉDIO/CAM. Achei 2 listagens adicionais na mesma rua fora da metragem-alvo (507m² e 450m², ambas com R$/m² bem mais alto que os 2 comparáveis de 659m² já usados) — dado diagnóstico relevante, não comparável direto. Tentei confirmar um comparável de 700m² (L2R Imóveis, R$3.800.000) mas o WebFetch não retornou a página específica (só a home da imobiliária) — não consegui confirmar detalhes, não usei o número.

## 2. Pendências abertas
- [ABERTO] Não consegui abrir individualmente nenhum anúncio do VivaReal/ZAP para a Rua Flávio Carvalho Molina (403/bloqueio de fetch) — a fragilidade de fonte que Villaça já tinha sinalizado continua sem solução técnica minha. Se algum dia eu tiver acesso a um MCP de scraping ou a uma chave de API de portal imobiliário, isso resolveria essa lacuna de verdade.
- [ABERTO] Minha resposta trouxe uma 3ª hipótese (efeito de tamanho dentro do mercado "normal", distinto de erro de classificação e de diferença de bairro) que Villaça não tinha levantado — fica para ele decidir se incorpora ao documento.

## 3. Aprendizados que não posso esquecer
- Quando a mesma rua/condomínio tem unidades menores com R$/m² MUITO mais alto que unidades maiores (mesmo padrão nominal), isso é um padrão conhecido de mercado imobiliário "normal" (terreno tem custo relativamente fixo por unidade, banheiros por quarto/suíte custam mais que m² de área bruta) — mas o oposto acontece no nicho de mansão/alto padrão (Barra da Tijuca, onde maior=mais caro por m², por escassez/prestígio). Não assumir que o efeito de tamanho é sempre na mesma direção — depende do segmento de mercado.
- Proporção de banheiros muito alta em relação a quartos (ex.: 5 quartos/7-8 banheiros) é um sinal de alerta técnico: pode indicar unidade configurada para renda/multi-família informal, não residência unifamiliar "pura" — isso pode derrubar o R$/m² de revenda para comprador família, mesmo em bairro/padrão nominal razoável. Vale sempre olhar essa proporção ao classificar padrão de um comparável.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
