# Estado — Landell (Automação+Elétrica)

> Arquivo de estado pessoal. Leio ao nascer, escrevo ao morrer.

**Última atualização:** 09/09/2026 — Exame 2 (Shadow → Assisted) executado, 2 casos-teste resolvidos e memoriais gravados. Aguardando veredito de Cardozo.

## 1. Onde parei / em andamento

**Nível:** Assisted (promovido 09/09/2026 após Exame 2 Shadow → Assisted, 2/2 aprovado por Cardozo).

**Exame 2 — Caso 1 (E1 simples, elétrica NBR 5410, residência 100m²):** revisei 6 itens de proposta preliminar terceirizada. Barrei: circuito único de iluminação para 7 ambientes (viola divisão obrigatória por cômodo/área), DR dispensado em banheiro por "quadro em ambiente seco" (DR é sobre o ambiente atendido, não o do quadro), chuveiro 5.500W dividindo circuito de 20A com TUG do banheiro (TUE precisa ser exclusivo, e 20A nem sustenta o chuveiro sozinho a 127V — IB≈43,3A), aterramento TN-C reaproveitando PEN (exige TN-S em obra nova). Aprovei LSHF em cozinha/área de serviço (reforço voluntário, não obrigatório ali, mas não contraria norma) e a divisão de TUG da cozinha em 2 circuitos por ultrapassar 1.500W. 2 pendências bloqueantes: potência do chuveiro do banheiro social (não informada) e confirmação com a Light do tipo real de fornecimento (127V vs. 220V muda o dimensionamento do circuito do chuveiro da suíte). Memorial: `Agentes/Landell/Casos/2026-09_Residencia_Vila_Isabel_Eletrica_100m2/memorial_verificacao_eletrica.md`.

**Exame 2 — Caso 2 (E2 complexo, SPDA + COSCIP/CBMERJ, condomínio 9 unidades):** revisei 6 itens. Barrei: SPDA "dispensando" NBR 5419 (é norma própria, não capítulo de aterramento da NBR 5410), aterramento único citando a "NBR 5410 revisada" como fundamento (mesma armadilha do Exame 1 — revisão não tem força normativa), estrutura metálica aparente dispensando captor Franklin e análise de risco (sem base), SPDA e detecção/alarme fundidos no mesmo memorial (são NTs distintas — 2-08 vs. 2-03). Não decidi por conta própria (fronteira reconhecida como lacuna pela própria Skill proposta): isenção A-1 aplicada a grupamento de 9 unidades — registrei como pendência bloqueante a confirmar via Kelsen/Hely, não como fato. Também não decidi titulação profissional exata (NT 1-01 não lida por completo) nem se "aspecto CAU" deve rotear para Baumgart (Estrutural/CREA) ou para Lúcio (Arquitetura/CAU) — ambos pendência. Sinalizei a Cardozo lacuna de ferramenta: não tenho Skill própria ratificada de NBR 5419 (SPDA detalhado) nem de NBR 17240 (detecção/alarme) — recomendo avaliar criação, no padrão da Skill NBR 6118 do Baumgart. Memorial: `Agentes/Landell/Casos/2026-09_Condominio_Golden_Green_SPDA_COSCIP/memorial_verificacao_spda_coscip.md`.

Nenhum caso real acionado ainda.

## 2. Pendências abertas

Nenhuma minha — Exame 2 respondido, 2/2 aprovado, promovido a Assisted. Próximo: à espera de acionamento de Cardozo com Briefing aprovado de Lúcio (produção real), ou Exame 3 (Assisted → Autonomous) quando Cardozo administrar. Recomendação de Skill dedicada NBR 5419/NBR 17240 registrada para Cardozo.

## 3. Aprendizados

- Minha função é elaborar e ajustar o projeto elétrico (NBR 5410) e de automação residencial **juntos** (disciplinas fundidas — dependência real).
- **NBR 5410:2004 (VC 2:2008) é única com força normativa hoje.** Revisão 2026 está em consulta pública, sem publicação antes fim/2026.
- **Proteção DR 30mA é obrigatória banheiro/cozinha/molhadas**, sem exceção por tensão (127V ou 220V). O risco é contato direto/indireto, não "corrente de fuga em 220V fica menor".
- **Proteção dimensionada por circuito:** IB (corrente projeto, pela potência real) ≤ In (nominal disjuntor) ≤ Iz (capacidade condutor). Não "40A para todos porque dá certo".
- Não decido o que automatizar sem instrução Cardozo — **Briefing deve listar**.
- **Potências reais são obrigatórias** para dimensionamento — não se presume.
- Não assino ART — **aponto necessidade profissional licenciado**, Cardozo registra.
- Skill Trilha A é proposta (referência); NBR 5410:2004 texto oficial é o documento de verdade. Revisar antes de cada projeto se houver publicação 2026.
- **SPDA (NBR 5419) está fora do escopo da minha Skill ativa `nbr5410-eletrica-automacao`** — a própria Skill declara isso em "O que NÃO cobre". Não tenho hoje Skill dedicada ratificada de NBR 5419 nem de NBR 17240 (detecção/alarme de incêndio). Em caso de SPDA real, sinalizar a lacuna a Cardozo antes de presumir conteúdo técnico detalhado.
- **Skill "proposta" `complementares_coscip-cbmerj-decreto42-2018-seguranca-incendio-rj.md`** ainda não ratificada — usar com ressalva de fonte secundária. Ela mesma reconhece lacuna não fechada: fronteira de isenção A-1 dentro de grupamento A-4 com mais de 6 unidades não foi apurada com rigor primário (só Hely/Kelsen fecham isso, referência: achado `b10-coscip-nt107` já fechado é só para A-1 isolado, não para A-4 >6 unidades). Nunca decidir essa fronteira sozinho — registrar como pendência.
- NBR 5410 e NBR 5419 são normas distintas (elétrica predial vs. proteção contra descargas atmosféricas) — SPDA nunca se dimensiona só pelo capítulo de aterramento da NBR 5410.

## 4. Como escrever neste arquivo

Ao encerrar a conversa, atualize as 3 seções acima. Não vire diário — substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Landell precisa pra continuar.
