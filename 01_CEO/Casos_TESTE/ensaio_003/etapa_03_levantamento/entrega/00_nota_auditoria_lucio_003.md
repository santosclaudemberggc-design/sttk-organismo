# Nota de auditoria do Gestor — Etapa 03 (Levantamento), Ensaio Sombra 003

**Gestor:** Lúcio (Arquitetura). **Executor auditado:** Oscar. **Data:** 06/10/2026. Caso 100% fictício; nada enviado.

## Como foi feito
- Li enunciado, caso base, parecer do Hely + auditoria do Kelsen (com ERRATA 4.1) e Viabilidade aprovada (v9 Villaça, v9 Fiker, v8 Mascaró) **antes** de acionar o Oscar. Acionei em primeiro plano, com os mesmos caminhos e a mesma proibição, e li as 3 peças na íntegra depois.
- Conferi contra as Skills as citações que sustentam conclusão: COE §2 (PV ≥ 1,00 m; PVI ≥ 3,00 m), fundações M4 (atrito negativo) e R7/checklist (NBR 8036: mín. 3 furos entre 200–400 m² de projeção), rebaixamento checklist (NA máximo, flutuação com piscina vazia), decreto3046 §6 ("M1 e M2 nunca se presumem"), levantamento-DULI §3–§5. Todas conferem.
- Refiz as contas: 14,29 − 5,00 = 9,29; 40,00 − 11,00 = 29,00; 9,29 × 29,00 = 269,41; 269,41 − 228,72 = 40,69; H1: 9,29 × 16,00 = 148,64; −120,77 / −80,08 / −160,16; faixas 85,74 + 72,50 + 72,50 + 71,45 = 302,19; 302,19 + 269,41 = 571,60 (−0,20 vs 571,80, aproximação declarada); 302,19 − 142,95 = 159,24; H1 sem APP: 85,74 + 80,00 − 142,95 = 22,79; 22,79 / 6,00 = 3,80 m; 0,50 / 0,0833 = 6,00 m; 3,20 + 8,50 = 11,70. Todas fecham.

## Correções que apliquei (marcadas no próprio texto)
1. **Peça 3, linha 1:** "Área de cálculo: Legal (já decidida)" contradizia a R1 do Kelsen (efeito patrimonial; cliente decide com advogado; Legal só recomenda). Corrigido.
2. **Peça 2, §3.2:** faltava a **locação** dos 142,95 m² pedida no critério 6 (havia só aptidão e folga). Acrescentei zoneamento conceitual com duas alternativas por causa da posição desconhecida da piscina (A: fundos + lateral esq. = 143,95; B: duas laterais = 145,00), a regra de ≥ 2,00 m de lado aplicada a faixa lateral parcialmente pavimentada, e a reserva obrigatória de jardim no frontal.

## Pontos que confirmo do Oscar (sem alteração)
- 13 divergências do enunciado com as fontes, tratadas e não absorvidas (Peça 3 §2): casa "demolida" × existente a demolir; 1,60 m é do condomínio, não da lei; Art. 353 III são porções drenantes, não lote mínimo; soleira +3,20 é **prevista**, referencial não confirmado (Art. 458); NA está em 5.7, não 5.2; custo/crédito trocados; "~150 m²" de H1 sem base; afastamento lateral não diminui, a largura do lote sim; DULI é Etapa 07 (Legal), não Executivo; 5.5 × 5.9 (lago/maré) não decidido; valores do "EXEMPLO" não usados; 28,20 m² atribuídos ao muro por inferência; "árvores raramente saem" é Skill secundária.
- O levantamento 5.2 **não serve de base de DULI** (falta RN, curvas, perfil natural, PAA, passeio, postes, PVs, árvores, casa, piscina, espelho d'água): complementação T1–T17.
- Pareceres: edícula — demolição total (decisão final do cliente); piscina — não entra como premissa do EP sem levantamento e laudo; árvores — preservar, acesso depois da locação.
- Nenhuma premissa legal reinterpretada; programa não redimensionado (só testado: cabe em H0 se ≥ 62,56 m² forem de fato não computáveis; não cabe em H1, faltam 160,16 m²); nada desenhado.

## Achado meu para Wallenberg/Villaça (não muda esta etapa)
- O pré-estudo v9 (aprovado) §5 diz "crédito aprovado mantém teto R$ 3 mi"; esse valor **não está no dossiê** (caso §2 só fala em crédito condicionado à licença e teto de obra de R$ 4,2 mi). Número sem fonte numa entrega aprovada — para Villaça conferir.

## Bloqueios de ferramenta
- `mcp__vitruvius__revit_status` → `Error: No such tool available: mcp__vitruvius__revit_status`. Entrega em texto/tabela/croqui descritivo. Pendência antiga (Vitruvius nunca disponível ao Oscar em sessão de ensaio) continua aberta.

## Gabarito lacrado — declaração honesta
- Não abri, li nem citei `_gabaritos_LACRADO\` nem `parecer_bardi*.md`. **Registro:** no início, um `Glob` meu na raiz da pasta do ensaio devolveu a lista de arquivos e os **nomes** dos arquivos do gabarito apareceram no resultado. Nenhum foi aberto. Depois disso usei só leitura por caminho exato e orientei o Oscar a não usar `Glob` na pasta-base. Bardi avalia se isso tem efeito.

## Veredito do Gestor
**Pronto para correção do Bardi**, com as 2 correções acima. Análise preliminar; num caso real, Gate do Maurício antes de qualquer uso com o cliente.

— Lúcio, 06/10/2026
