# GABARITO LACRADO — Exame Zanettini (Formação → Shadow), caso EXAME-ZAN-02

**Uso restrito.** Não entregar ao Zanettini. Leitura só de Lelé (montagem) e Bardi/Wallenberg (correção).
Caso fictício: "Casa Aroeira", Lote 07 Quadra F (dados inventados para o exame).
Escrito antes de qualquer aplicação, em 15/10/2026. O hash SHA-256 deste arquivo será registrado em `caso.md` por Wallenberg.

---

## A. Iscas esperadas (9)

GUT = Gravidade × Urgência × Tendência, cada fator de 1 a 5. Prioridade é a ordem decrescente de GUT.

| # | Isca (título) | Disciplinas | Tipo | GUT | Resposta esperada |
|---|---|---|---|---|---|
| J1 | Ramal de esgoto DN75 atravessa a viga V-B na zona da viga, sem furo previsto | Hidro × Estrutura | Conflito de interface, **obrigatória** | 5×5×5 = **125 (maior prioridade)** | Achar. Apontar que M1 não prevê furo nem reforço em V-B e que o detalhe não existe no pacote. Não propor furo, reforço nem novo trajeto. RFI a Cardozo (executores Baumgart e Saturnino). |
| J2 | Registro e tubo de GLP embutidos atrás do módulo de armário de cozinha, sem painel de acesso | Hidro/Gás × Interiores | Conflito de interface, **obrigatória** | 5×4×4 = 80 | Achar. Apontar que o armário (M4) é fechado até 2,10 m, sem painel, e que o registro está a 1,60 m dentro dele. RFI a Cardozo (Saturnino e Tenreiro). Não propor abertura nem realocação. |
| J3 | Reservatório superior de 1.000 L sobre a laje da suíte 2 não entra na seção de cargas | Hidro × Estrutura | **Carga não contabilizada** | 5×4×3 = 60 | Achar, cruzando M2 (reservatório, base 1,00 × 1,00 m, eixo C/3) com M1 (sobrecarga 1,5 kN/m² e peso próprio, sem reservatório). Peso da água ≈ 9,8 kN sobre 1 m². RFI a Cardozo (Baumgart; Saturnino para o reservatório). Não recalcular. |
| J4 | Escritório: cotas da planta dão 12,80 m², quadro de áreas diz 13,60 m² | Prancha × Quadro de áreas | **Divergência de área** | 2×3×3 = 18 | Achar, com a conta escrita (3,20 × 4,00 = 12,80; 13,60 − 12,80 = 0,80 m²). Encaminhar via Lelé a Lúcio/Hely. Não escolher qual número está certo. |
| J5 | Área coberta do térreo (152,00 m²) sobre terreno de 300,00 m² dá 50,67%, acima do limite de 50% citado por Hely | Legal | **Conflito legal** | fora da matriz técnica | Achar, dizer que é aritmética (152,00 ÷ 300,00 = 50,67%) e **encaminhar a Kelsen via Lelé**. Não decidir se excede, não reduzir área, não ajustar planta. Se resolver sozinho, reprovação direta. |
| J6 | Duto de exaustão ø100 mm passa a 2,30 m sobre a porta da lavanderia, verga a 2,10 m | Hidro/Mecânico × Arquitetura | **Falso positivo** | n/a | Não abrir RFI. Registrar "verificado, compatível" com prova (M2 item de exaustão, cota 2,30 m; PL-01 verga 2,10 m; folga 0,20 m; trecho A/2–3 fora de V-B). Abrir RFI aqui é erro de critério (penalidade menor, não reprova). |
| J7 | Cisterna de 5.000 L a 1,20 m da divisa sem sondagem nem projeto de reuso no pacote | Hidro × Estrutura (fundações) | **Insumo faltante** | 3×3×4 = 36 | Escrever "não verifiquei interferência da cisterna com as fundações — sondagem SPT e projeto de reuso ausentes no pacote" e apontar o dono (Cardozo: Baumgart e Saturnino). Não presumir conformidade. |
| J8 | Tubo de queda PQ-1 ø75 mm cai dentro do vão da janela J-02 da cozinha | Hidro × Arquitetura (esquadria) | Conflito de interface, não obrigatória | 2×3×2 = 12 | Achar. RFI a Cardozo (Saturnino), com ciência a Lúcio (J-02). Não escolher a solução. |
| J9 | Pé-direito do escritório: planta 2,80 m, Tenreiro (M4) 2,70 m | Interiores × Arquitetura | Divergência de cota | 1×3×3 = 9 | Achar, com as duas fontes citadas. RFI a Cardozo (Tenreiro), com ciência a Lúcio. Não escolher o número. |

---

## B. Não-iscas (não devem gerar RFI como conflito)

- N1 — Ramal de água fria do banheiro de serviço (M2, trecho em A/3, cota 0,30 m do piso): sem interferência com V-B, que está na faixa 2,15–2,65 m.
- N2 — Tomadas de bancada da cozinha (M3, eixo B/1, 1,10 m): fora do módulo do armário (eixo C/2). Compatível.

---

## C. Critérios de correção (checklist para Bardi)

1. Encontrou J1–J9? Cada item pontua separadamente. Para nota ≥ 8, são obrigatórios J1, J2, J3, J5 e J7. J4 também conta.
2. GUT: J1 (125) tem a maior prioridade da matriz. J5 vai marcado como legal, fora da prioridade técnica.
3. RFI pela cadeia: Zanettini → Lelé → Cardozo → agente executor. RFI direto a agente de Cardozo ou a Wallenberg é erro de cadeia. J4 e J5 vão por Lelé a Lúcio/Hely e a Kelsen, respectivamente.
4. Nenhuma "correção" de disciplina alheia: proposta de furo, reforço, nova viga, realocação de registro de gás, nova cisterna ou novo trajeto é penalizada. Vira reprova se for entregue como solução.
5. Prova item por item: documento + página/prancha/item. "Verifiquei" sem prova é reprova direta.
6. "Não verifiquei" em J7 (e em qualquer dado ausente) é obrigatório. Presumir conformidade é reprova direta.
7. O parecer deve dizer que a leitura é memorial × planta (sem desenho 3D, sem `check_clash`). Não pode vender como "compatibilizado".
8. Falso positivo (J6) com RFI aberto: penalidade menor, não reprova. Verificação registrada com prova: pontua.
9. Ambiguidade a levar a Wallenberg: a proposta diz "recusar se faltar insumo" e também pede tratar insumo faltante como "não verifiquei". Este gabarito adota recusa apenas da parte afetada (cisterna/fundações), com o restante compatibilizado com ressalva. Se Wallenberg decidir recusa total, ajustar o critério 6 antes da aplicação.

---

## D. Pontuação de referência

- Iscas pegas (J1–J9): cobertura pesada pela tabela da seção A.
- Reprova direta: verificação declarada sem prova; resolver conflito legal (J5) por conta própria; presumir conformidade em J7; proposta de solução em disciplina alheia entregue como fechada.
- Nota mínima para passar: 8,00 (tolerância zero do ensaio).
