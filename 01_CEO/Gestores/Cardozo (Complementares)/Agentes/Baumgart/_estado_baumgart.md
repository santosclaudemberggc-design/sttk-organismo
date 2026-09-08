# Estado — Baumgart (Estrutural)

> Arquivo de estado pessoal. Leio ao nascer, escrevo ao morrer.

**Última atualização:** 08/09/2026 — 2º caso real do dia (fundação profunda, edifício Ipanema/esquina) verificado e gravado em .md. Nível: **Shadow** — Exame 1 já tinha sido APROVADO por Cardozo em 01/09/2026 (100%), conferido no veredito real (`Casos_TESTE/Exame1_Baumgart_TESTE/veredito_cardozo.md`); a versão anterior deste estado dizia "ainda sem resultado" por não ter checado esse arquivo — corrigido.

## 1. Onde parei / em andamento

**Caso real "Ipanema esquina"** (08/09/2026): edifício residencial 6 pav + 2 subsolos, lote de esquina encravado entre 2 prédios de fundação desconhecida, hélice contínua Ø50cm, carga crítica 2.200 kN. Resultado: **NÃO LIBERADA para detalhamento executivo** — memorial completo gravado em `01_CEO/Gestores/Cardozo (Complementares)/Agentes/Baumgart/Casos/2026-09_Edificio_Ipanema_Esquina_Fundacao_Profunda/memorial_verificacao_fundacao_profunda.md`, com 10 pendências bloqueantes (CAA, sondagem completa, método de correlação p/ capacidade de carga, prova de carga indevidamente dispensada, Anexo J x N trocado, subpressão/rebaixamento não tratados apesar do NA a 1,5m, contenção dos subsolos fora do escopo 6122, vistoria cautelar dos vizinhos, ATP, ART). Pontos que reconheci como conformes (não inventei problema): CC3 já correta, escolha de hélice contínua adequada ao lote encravado, consumo de cimento 400kg/m³ excede o mínimo de 350 da Emenda 1.

**Caso real "P4 Botafogo"** (08/09/2026, 1º caso do dia): Cardozo acionou para verificar sapata isolada 1,5×1,5m, prof. 1,2m, proposta por Oscar/geotécnico parceiro para pilar P4 (canto, 850 kN ELU), lote 400 m² à beira da Baía de Guanabara. Resultado: **NÃO LIBERADA para detalhamento executivo** — 6 pendências bloqueantes reportadas a Cardozo em texto:
1. Sondagem insuficiente (1 furo só; norma pede mín. 2 p/ lote ≤1200m²) e sem perfil NSPT de 0–3m (a sapata assenta a 1,2m, dentro do trecho não caracterizado — o NSPT=14 informado é da camada a partir de 3m, não da cota de apoio).
2. Capacidade de carga por NSPT/10 direto rejeitada (erro comum já catalogado na Skill 6122 — falta correlação reconhecida tipo Aoki-Velloso/Décourt-Quaresma ou via Su/Terzaghi para solo coesivo).
3. CAA-I "afastada do mar" contradiz o próprio Briefing ("à beira da Baía de Guanabara") e viola o protocolo — CAA é insumo obrigatório do contratante, engenheiro não arbitra.
4. Consumo de cimento 300 kg/m³ alegado como "novo mínimo da Emenda 1" está errado — a Emenda 1/2022 reduziu de 400 para **350** kg/m³, não 300.
5. Falta carga de serviço/característica (só veio ELU) — necessária para checar tensão admissível (grandeza de serviço) e para ELS; comparação direta ELU vs. admissível é metodologicamente inválida.
6. Recalque diferencial (ELS) não verificado — crítico em argila.
Cálculo-sanidade feito com os próprios números propostos (mesmo rejeitados): sapata 1,5×1,5m (2,25 m²) fica abaixo até do necessário estimado (~4,4 m², lado ~2,1m) — ou seja, mesmo aceitando os dados como estão, a geometria proposta não fecha.

Aguardando: retorno de Cardozo/geotécnico parceiro com sondagem complementar, CAA formal do cliente, e carga de serviço da superestrutura.

## 2. Pendências abertas

- [PENDENTE] Retorno do caso "Ipanema esquina" com as 10 pendências do memorial resolvidas (CAA, sondagem completa, prova de carga, contenção, ATP etc.) para reabrir a verificação e liberar o executivo.
- [PENDENTE] Retorno do caso "P4 Botafogo" com os 6 itens corrigidos, para reabrir a verificação.
- [PENDENTE] Skills NBR 6122 (fundações) e NBR 6120 (cargas) seguem como Skills Propostas, fora de `.claude/skills/` — sinalizar a Cardozo para cobrar instalação (a de 6122 já consta "ratificada 07/09" no índice, mas não foi instalada).

## 3. Aprendizados

- Minha função é elaborar e ajustar o projeto estrutural (memória de cálculo, especificação de fundações, aço e concreto) conforme o Briefing que Cardozo me passa.
- Sigo NBR 6118:2026 (Emenda 1), classes CC1/CC2/CC3.
- Não decido o tipo de estrutura — o Briefing define, Cardozo valida antes de me acionar.
- RRT exige profissional licenciado: aponto a necessidade, não assino.
- Se o Briefing não especificar tipo de fundação ou estrutura, sinalizarei a lacuna a Cardozo antes de executar qualquer coisa.
- **CC3 tem gatilhos objetivos além de nº de pavimentos:** subsolo, marquise, protensão, >5 pav, reforma com remoção de pilar (Skill Trilha A §1). Na dúvida, prevalece a mais conservadora (Skill complementares item 1). CC3 ⇒ ATP obrigatória, sem dispensa.
- **CAA é dado de entrada inicial e obrigatório do contratante** (Skill Trilha A §3). Nunca adotar fck/cobrimento "padrão" sem CAA; nunca aceitar "ajusta depois". Lote perto da orla ⇒ exposição marinha provável (CAA III/IV), mas quem classifica é o contratante.
- **NBR 6118:2014 nunca é aceitável.** Transição só cobre 6118:2023, janela de 180 dias após 11/03/2026 (≈ 07/09/2026).
- **Skill Trilha A é PROPOSTA**, baseada em blogs, não no texto oficial ABNT. Para CC3/marquise, exigir texto normativo oficial antes do dimensionamento definitivo.
- **Marquise/balanço:** armadura inferior de segurança obrigatória (Skill Trilha A §4). **Piso acessível:** verificar frequência natural ≥ 3 Hz (§5).
- Pedido de "acelerar rebaixando norma/classe" se recusa citando Princípios 3 (qualidade > velocidade), 18 (conformidade), 8 (rastreabilidade — adiantamento verbal de terceiro não é insumo).
- Divergência de nomenclatura da sigla ATP: Skills dizem "Avaliação Técnica de Projeto"; frontmatter do Agente diz "Ação de Projeto Típica". Sinalizado a Cardozo.
- **Skills de NBR 6122 e NBR 6120 existem como Skills Propostas** em `01_CEO/Skills_Propostas/2026/Setembro/` (ainda não em `.claude/skills/`, diferente da 6118) — mesmo assim usei como Trilha A, sinalizando que os valores vêm de fonte secundária.
- **Tensão admissível (NSPT/10 ou qualquer correlação) é grandeza de SERVIÇO** — nunca comparar direto contra carga ELU (fatorada). Se só vier ELU, sinalizar a falta da carga característica/quase-permanente antes de checar capacidade ou recalque.
- **CAA nunca se arbitra por "parece razoável pra região"** — sempre cruzar a justificativa dada contra a própria descrição do lote no Briefing (ex.: "afastada do mar" x "à beira da baía" é contradição que salta aos olhos sem precisar do texto oficial da norma).
- **Emenda 1/2022 da NBR 6122 reduziu cimento mínimo para 350 kg/m³ (não 300)** — checar sempre o valor exato citado por terceiros contra a Skill antes de aceitar "conforme a norma".
- Mesmo com pendências bloqueantes, vale rodar um cálculo-sanidade com os números propostos (mesmo os rejeitados) para mostrar a ordem de grandeza do erro — ajuda Cardozo a decidir se é ajuste fino ou redesenho.
- **Correção sobre "não gravar .md":** a regra genérica do harness é para não substituir a resposta final por um arquivo de relatório — mas meu entregável de função (definido no meu próprio perfil) É o memorial em `.md` com tabelas, para Cardozo consolidar no Drive. Solução: fazer as duas coisas — gravar o `.md` em `Agentes/Baumgart/Casos/<caso>/` E devolver o conteúdo completo também na resposta final. Não tratar a regra genérica como proibição do entregável do meu próprio escopo.
- **Anexo J (hélice contínua, agregado 9,5–25,0mm) x Anexo N (escavada com fluido estabilizante, agregado 4,75–12,5mm), Emenda 1/2022:** checar sempre se o agregado citado bate com o método construtivo declarado — já vi um Briefing citar o anexo errado.
- Diâmetro/carga de estaca isolada não dá pra aprovar sem: (a) perfil de sondagem completo, (b) método de correlação nomeado, (c) prova de carga — principalmente perto de vizinhos com fundação desconhecida ou quando a camada resistente só aparece muito profunda (aqui, 22m).
- "Concretagem sob pressão resolve o lençol alto" é verdade só para a integridade do fuste da estaca — não resolve subpressão na laje de subsolo, rebaixamento e risco a vizinhos. Não aceitar isso como fechamento do assunto NA.

## 4. Como escrever neste arquivo

Ao encerrar a conversa, atualize as 3 seções acima. Não vire diário — substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Baumgart precisa pra continuar.
