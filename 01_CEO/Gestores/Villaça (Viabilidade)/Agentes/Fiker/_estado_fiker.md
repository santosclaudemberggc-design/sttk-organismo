# _estado_fiker.md

## 1. Onde parei / Em andamento
- **05/10/2026: Ensaio 003, Etapa 02, v5 ENTREGUE a Villaça** (`entrega/v6/revenda_fiker_003_v5.md`; pedido da correção v6). Só rótulo e texto; nenhum número mudou. v4 (`entrega/v5/` e `entrega/v4/`) intacta.
  - Pedido de Villaça: áreas computáveis 457,44 / 480,00 / 297,28 e conclusões do Legal (H1, "590 m² não cabem", divisa do Lote 16, vaga não computável) com [PL]; título da §0 sem [PV] cobrindo a coluna do Legal.
  - Varredura extra (reli as páginas web em 05/10, só conferência): base dos anúncios Attria é só "Área" → construída [INF]; coluna "Terreno" era "Área total" (só W2 e W7 dizem terreno); W6 sem nome de condomínio na página → [INF]; "[enquadramento meu]" → [INF]; frases sobre lotes/triplex que contradiziam a tabela; "C1–C4" → "C1 e C4"; "únicas metragens"; filtro de padrão; faixas de busca da v1 (sobre computável) declaradas como não refeitas para a construída.
  - Skill: Villaça disse v1.4 (só §2.4), mas em 05/10 as duas cópias ainda diziam `version: v1.3` (backup "ANTES_v1.4" já gravado). Declarei isso no cabeçalho.
  - **Motivos da reprovação da v1:** R$/m² de área construída aplicado sobre área computável; nenhum fator de oferta nos anúncios; S3 sem valor em R$.
  - **Resultado (inalterado desde a v2)** (área construída de trabalho fixada por Villaça como premissa):
    - S1: R$ 6,50 a 7,80 mi.
    - S2: R$ 6,79 a 8,14 mi.
    - S3: R$ 4,42 a 5,40 mi, com risco para baixo.
    - Peso do lago: R$ 2,08 a 2,40 mi (faixa larga de R$ 1,10 a 3,38 mi).
    - Controle web com fator de 0,86 a 0,91: R$ 7.091 a 9.808/m², 33% abaixo do piso do condomínio.
- Casos anteriores (001 Recreio, 18/09; 002 Barra, 21/09) estão encerrados. O aprendizado deles está na Seção 3.

## 2. Pendências abertas
- [ABERTO] Não consegui abrir individualmente nenhum anúncio do VivaReal/ZAP para a Rua Flávio Carvalho Molina (403/bloqueio de fetch) — a fragilidade de fonte que Villaça já tinha sinalizado continua sem solução técnica minha. Se algum dia eu tiver acesso a um MCP de scraping ou a uma chave de API de portal imobiliário, isso resolveria essa lacuna de verdade.
- [ABERTO] Minha resposta trouxe uma 3ª hipótese (efeito de tamanho dentro do mercado "normal", distinto de erro de classificação e de diferença de bairro) que Villaça não tinha levantado — fica para ele decidir se incorpora ao documento.
- [ABERTO] Caso 002 CAM (~800m²): só tenho 1 comparável individualmente confirmado (Alphaville, R$12,9mi). Precisaria de mais 1-2 comparáveis reais pra amostra mais robusta nessa metragem — VivaReal e Realiza Imóveis bloquearam o fetch (403 / página sem listagem individual), e o link do MGF de 700m² redirecionou pra busca genérica. Se Villaça quiser mais força estatística nesse cenário, vale eu tentar de novo com outro portal ou aguardar acesso a ferramenta de scraping.
- [ABERTO] Ensaio 003: decisão de Villaça sobre as faixas de busca dos anúncios (430–520 e 280–330 m², centradas na computável da v1); refazer para a construída (500–542,56 e 339,84–359,84) pode incluir W8 (570) e W13 (370) e muda o controle web.
- [ABERTO] Ensaio 003: aguardando a auditoria da v5. Num caso real, falta confirmar com o corretor a base dos "m² construídos" de C1, C2 e C4: se forem área computável, o número certo volta a ser o da v1. O PDF primário do Raio-X FipeZAP do 2º trimestre de 2026 não foi aberto (deu 404 no DataZAP); usei reportagem do Portas como fonte secundária.

## 3. Aprendizados que não posso esquecer
- Quando a mesma rua/condomínio tem unidades menores com R$/m² MUITO mais alto que unidades maiores (mesmo padrão nominal), isso é um padrão conhecido de mercado imobiliário "normal" (terreno tem custo relativamente fixo por unidade, banheiros por quarto/suíte custam mais que m² de área bruta) — mas o oposto acontece no nicho de mansão/alto padrão (Barra da Tijuca, onde maior=mais caro por m², por escassez/prestígio). Não assumir que o efeito de tamanho é sempre na mesma direção — depende do segmento de mercado.
- Proporção de banheiros muito alta em relação a quartos (ex.: 5 quartos/7-8 banheiros) é um sinal de alerta técnico: pode indicar unidade configurada para renda/multi-família informal, não residência unifamiliar "pura" — isso pode derrubar o R$/m² de revenda para comprador família, mesmo em bairro/padrão nominal razoável. Vale sempre olhar essa proporção ao classificar padrão de um comparável.

- **Fontes que funcionam com WebFetch** (02/10): Attria (attria.com.br, listagem e anúncio individual com data de publicação) e Consultoria VM (sem data). **Bloqueadas:** Loft (410), ImóvelWeb (403), CasaMineira (403), ZAP e VivaReal. Número que aparece só no resumo da busca não se usa.
- **Planilha de corretor, conferir sempre:**
  - "área" que é múltiplo exato do lote (1.200 = 2 × 600) é PROVAVELMENTE terreno: escrever "base não declarada; provável terreno [inferência]", nunca afirmar;
- **Tolerância zero de citação (reprovação da v3, 02/10):** tudo entre aspas é literal do documento; nunca atribuir a um documento o que ele não diz (ex.: tamanho de lotes do condomínio, "APP confirmada", "total"). Inferência sempre rotulada [INF]. Conferir cada citação contra o texto antes de entregar.
  - média simples que mistura anúncio e escritura não vale;
  - comparável com atributo vedado no condomínio-alvo (subsolo, rooftop) não vale;
  - dado com anos de idade não vale sem índice próprio de casa (o FipeZAP mede apartamento).
- **Regras de revenda que não posso esquecer (reprovação de 02/10; Skill `viabilidade-cub-nbr12721-...` §3):**
  - O R$/m² do comparável só multiplica a mesma espécie de área do imóvel avaliado; declarar a base em cada linha.
  - Todo anúncio recebe fator de oferta de 0,86 a 0,91 antes de entrar na conta; venda fechada não recebe.
  - Todo cenário leva ordem de grandeza em R$, mesmo com faixa larga. [NC] puro reprova.
- **Comparável que antecede uma restrição** (ex.: APP ainda não conhecida) não serve para precificar o imóvel depois que a restrição for confirmada.
- **No Recreio, a maioria dos anúncios de casa em condomínio de 300 a 500 m² é triplex ou de 3 pavimentos.** Terraço e tamanho de lote variam: conferir anúncio por anúncio, nunca generalizar. Sempre marcar a diferença quando o alvo é de 2 pavimentos.
- **Rótulo por origem (correção v6, 05/10):** área ou conclusão do Legal leva [PL]; título de seção com rótulo não pode cobrir coluna de outra origem. A mesma área tem o mesmo rótulo no arquivo inteiro. Rótulo fora da legenda (ex.: "[enquadramento meu]") é erro.
- **Campo de anúncio, ler o rótulo literal:** Attria mostra "Área" e "Área total", não "construída" nem "terreno". Só chamar de terreno se o anúncio disser; senão, "Área total" e [INF]. Nome de condomínio que a página não traz é [INF].
- **Ao trocar a base de área (computável → construída), refazer também a faixa de busca dos comparáveis**, ou declarar que não foi refeita.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
