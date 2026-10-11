# _estado_fiker.md

## 1. Onde parei / Em andamento
- **05/10/2026: Ensaio 003, Etapa 02, v8 CONCLUÍDO** — Homogeneização regional NBR 14653-2 com fator 0,75 validado e auditado.
  - **Base de dados ampliada:** 2 vendas reais (C1, C4) + 12 ofertas (W1-W13) + ITBI agregado (1.421 transações, R$ 6.911/m²) + 15 ofertas adicionais encontradas.
  - **Fator de oferta regional:** 0,75 (intervalo 0,72–0,75). Baseado em C1/C4 vendas (R$ 13.500/m² média) ÷ W1-W13 ofertas (R$ 9.790/m² média) = 1,378. Significado: ofertas estão ~27% abaixo de vendas reais.
  - **Wallenberg apontou erro:** vendas acima de ofertas (não abaixo). Corrigido e documentado em `CORRECAO_ERRO_LOGICO_05_10.md`.
  - **Resultado j' S1/S2:** R$ 3.001.540–5.250.370 (fator 0,75). Gap condomínio/web aumenta de 16% (v6) para 48–116% (v8).
  - **Confiança:** MÉDIA. Amostra de 2 vendas é pequena, mas tipo está correto (casas de condomínio). Gap grande sinaliza prêmio real do condomínio OU erro em base de área das escrituras.
  - **Três opções para Wallenberg:** (1) usar v8 0,75 [recomendado, regional]; (2) intervalo 0,72–0,75 [transparência sobre incerteza]; (3) manter v6 0,91 [nacional, documentado].
  - **Próximos passos críticos:** validar escrituras C1/C4 (construída vs computável); se for computável, números v6 voltam a valer.
  - v6 (correção v7) + v1–v5 mantidas intactas.
  - Motivo: filtro de metragem dos anúncios estava na base computável (faixas da v1). Refeito sobre a construída de trabalho [PV], ±15% sobre os extremos (fixado por Villaça): S1/S2 425–624 (n = 7, com W8); S3 289–414 (n = 5: W10, W11, W13, W9, W5); W12 fora.
  - R$/m² recalculado sobre preço e área exatos; achei 3 divergências além das de Villaça (W3 ×0,86 9.173; W4 ×0,86 7.453; W11 ×0,91 6.165), nenhuma em extremo.
  - Resultado: faixa principal C1/C4 inalterada (S1 6,50–7,80; S2 6,79–8,14; S3 4,42–5,40 mi). Controle web S1/S2 R$ 7.091 a 11.175/m², piso do condomínio 16% acima; j' S1 3.545.500–5.811.000; S2 3.705.473–6.063.108; S3 alto padrão (W10+W13) 3.151.676–4.418.116.
  - Lacuna: lote/"Área total" de W5, W8, W9, W10, W11, W13 e pavimentos de W8/W9 não foram registrados em 02/10 (sem nova pesquisa por ordem de Villaça).
- Casos anteriores (001 Recreio, 18/09; 002 Barra, 21/09) estão encerrados. O aprendizado deles está na Seção 3.

## 2. Pendências abertas
- [ABERTO] Não consegui abrir individualmente nenhum anúncio do VivaReal/ZAP para a Rua Flávio Carvalho Molina (403/bloqueio de fetch) — a fragilidade de fonte que Villaça já tinha sinalizado continua sem solução técnica minha. Se algum dia eu tiver acesso a um MCP de scraping ou a uma chave de API de portal imobiliário, isso resolveria essa lacuna de verdade.
- [ABERTO] Minha resposta trouxe uma 3ª hipótese (efeito de tamanho dentro do mercado "normal", distinto de erro de classificação e de diferença de bairro) que Villaça não tinha levantado — fica para ele decidir se incorpora ao documento.
- [ABERTO] Caso 002 CAM (~800m²): só tenho 1 comparável individualmente confirmado (Alphaville, R$12,9mi). Precisaria de mais 1-2 comparáveis reais pra amostra mais robusta nessa metragem — VivaReal e Realiza Imóveis bloquearam o fetch (403 / página sem listagem individual), e o link do MGF de 700m² redirecionou pra busca genérica. Se Villaça quiser mais força estatística nesse cenário, vale eu tentar de novo com outro portal ou aguardar acesso a ferramenta de scraping.
- [RESOLVIDO 05/10] Ensaio 003: **v9 CONCLUÍDO** — Método NBR 14653-2 transparente com matriz tabulada.
  - v8 reprovou (falta rastreabilidade). v9 traz matriz explícita C1-C6: inclui C1/C2 (com fator 0,75)/C4; exclui C3 (terreno puro), C5 (outro condomínio, rooftop vedado), C6 (desatualizado 11/2021).
  - Fator 0,75 rastreável: C1/C4 vendas (R$ 13.500/m²) vs W1-W13 ofertas (R$ 9.790/m²) = razão 1,378 → 0,72–0,75.
  - Resultado: j' principal S1/S2 = R$ 6.500.000–7.800.000; web = R$ 3.001.540–5.250.370; gap 41–142%.
  - Método em cascata visível: triagem (tipo→data→metragem→fator→resultado).
  - Arquivo: `v9/revenda_fiker_003_v9.md`. v1–v8 mantidas.

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
- **Filtro de metragem usa a mesma base de área do avaliando** (construída × construída; Skill v1.5 §3.1/§3.2). Declarar a decisão de método errada e mantê-la reprova (reprovação da v6 do ensaio, 05/10). Tolerância padrão usada: ±15% sobre os extremos.
- **R$/m² homogeneizado = preço × fator ÷ área, arredondando só no fim**; nunca multiplicar o bruto já arredondado.
- **Na coleta, registrar todos os campos (lote/"Área total", pavimentos, padrão) de todo anúncio, inclusive os que parecem fora da faixa** — a faixa pode mudar depois.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
