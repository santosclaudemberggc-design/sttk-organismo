# _estado_fiker.md

## 1. Onde parei / Em andamento
- **02/10/2026: Ensaio Sombra 003, Etapa 02 (Viabilidade), ENTREGUE a Villaça.** Arquivo: `01_CEO/Casos_TESTE/ensaio_003/etapa_02_viabilidade/entrega/revenda_fiker_003.md`. Aguardando auditoria de Villaça e parecer de Bardi.
  - **Planilha do corretor 5.13:** C1 e C4 aceitas (vendas, mesmo condomínio); C2 aceita só como teto (anúncio); C3, C5 e C6 rejeitadas. A média de R$ 12.833 foi declarada inválida como método.
  - **S1:** R$ 5,95 a 6,86 mi. **S2:** R$ 6,24 a 7,20 mi. Ambos a R$ 13 a 15 mil/m², confiança média-baixa.
  - **S3:** sem comparável real; interpolação declarada com ressalva forte, risco para baixo.
  - **Controle web:** Attria e VM, 6 anúncios de 430 a 520 m² a R$ 8.245 a 10.778/m², pelo menos 20% abaixo das vendas do dossiê.
- Casos anteriores (001 Recreio, 18/09; 002 Barra, 21/09) estão encerrados. O aprendizado deles está na Seção 3.

## 2. Pendências abertas
- [ABERTO] Não consegui abrir individualmente nenhum anúncio do VivaReal/ZAP para a Rua Flávio Carvalho Molina (403/bloqueio de fetch) — a fragilidade de fonte que Villaça já tinha sinalizado continua sem solução técnica minha. Se algum dia eu tiver acesso a um MCP de scraping ou a uma chave de API de portal imobiliário, isso resolveria essa lacuna de verdade.
- [ABERTO] Minha resposta trouxe uma 3ª hipótese (efeito de tamanho dentro do mercado "normal", distinto de erro de classificação e de diferença de bairro) que Villaça não tinha levantado — fica para ele decidir se incorpora ao documento.
- [ABERTO] Caso 002 CAM (~800m²): só tenho 1 comparável individualmente confirmado (Alphaville, R$12,9mi). Precisaria de mais 1-2 comparáveis reais pra amostra mais robusta nessa metragem — VivaReal e Realiza Imóveis bloquearam o fetch (403 / página sem listagem individual), e o link do MGF de 700m² redirecionou pra busca genérica. Se Villaça quiser mais força estatística nesse cenário, vale eu tentar de novo com outro portal ou aguardar acesso a ferramenta de scraping.
- [ABERTO] Ensaio 003: aguardando auditoria de Villaça e parecer de Bardi sobre `revenda_fiker_003.md`. O PDF primário do Raio-X FipeZAP do 2º trimestre de 2026 não foi aberto (deu 404 no DataZAP); usei reportagem do Portas como fonte secundária.

## 3. Aprendizados que não posso esquecer
- Quando a mesma rua/condomínio tem unidades menores com R$/m² MUITO mais alto que unidades maiores (mesmo padrão nominal), isso é um padrão conhecido de mercado imobiliário "normal" (terreno tem custo relativamente fixo por unidade, banheiros por quarto/suíte custam mais que m² de área bruta) — mas o oposto acontece no nicho de mansão/alto padrão (Barra da Tijuca, onde maior=mais caro por m², por escassez/prestígio). Não assumir que o efeito de tamanho é sempre na mesma direção — depende do segmento de mercado.
- Proporção de banheiros muito alta em relação a quartos (ex.: 5 quartos/7-8 banheiros) é um sinal de alerta técnico: pode indicar unidade configurada para renda/multi-família informal, não residência unifamiliar "pura" — isso pode derrubar o R$/m² de revenda para comprador família, mesmo em bairro/padrão nominal razoável. Vale sempre olhar essa proporção ao classificar padrão de um comparável.

- **Fontes que funcionam com WebFetch** (02/10): Attria (attria.com.br, listagem e anúncio individual com data de publicação) e Consultoria VM (sem data). **Bloqueadas:** Loft (410), ImóvelWeb (403), CasaMineira (403), ZAP e VivaReal. Número que aparece só no resumo da busca não se usa.
- **Planilha de corretor, conferir sempre:**
  - "área" que é múltiplo exato do lote (1.200 = 2 × 600) é área de terreno;
  - média simples que mistura anúncio e escritura não vale;
  - comparável com atributo vedado no condomínio-alvo (subsolo, rooftop) não vale;
  - dado com anos de idade não vale sem índice próprio de casa (o FipeZAP mede apartamento).
- **Comparável que antecede uma restrição** (ex.: APP ainda não conhecida) não serve para precificar o imóvel depois que a restrição for confirmada.
- **No Recreio, a maioria das casas em condomínio de 300 a 500 m² é triplex com terraço em lote pequeno.** Sempre marcar a diferença quando o alvo é de 2 pavimentos em lote grande.

## 4. Como escrever nele
- Substitua seções, não append.
- Apague o que virou passado.
- Aponte pra docs em vez de copiar.
