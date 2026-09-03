# Estado — Kelsen (Gestor Legal)

> Arquivo de estado pessoal. Leio ao nascer (toda vez que Wallenberg me aciona), escrevo ao morrer (antes de devolver o retorno a ele).
> Memória privada minha — não repete o Registro Diário, que é o que Wallenberg leva pra Claudemberg.
>
> **Trim de 03/09/2026:** o log cronológico completo de rodadas (13/07 → 02/09) foi movido para `_estado_kelsen_HISTORICO.md` (não leio ao nascer). Aqui fica só o estado vivo + os aprendizados. Ver Seção 4.

---

## 1. Onde parei / em andamento

- Aprovado por Claudemberg em **13/07/2026**. Equipe: **Hely**, único Agente. Sou **Autonomous** desde 22/07/2026.
- Base legislativa: **AP4** — Recreio / Barra da Tijuca / Vargem Grande. Fontes em `Agentes/Hely/Fontes_Legislacao/`, índice `_indice_fontes.md`. POPs de Hely em `Agentes/Hely/POPs/` (RIU-01, **02 SUSPENSO**, 03, 04, 05, 06) + `POP-GESTOR-LEGAL-01` na minha pasta.
- **Sttickler é UNIFAMILIAR** — segue o rito completo, não existe rito de baixa complexidade. Único tratamento diferenciado vigente: **Anexo IV no lugar do III** (Decreto 55.622/2025, Art. 10, p.ú.) — peça, não rito.
- **LMS obrigatória para todo unifamiliar** (regime simplificado do Licenciamento Ambiental Municipal, SMAC) — trâmite paralelo ao LICIN 2.0/SMDU, incorporado à base ativa em 28/07 (`SKILL.md` + `POP-GESTOR-LEGAL-01` item 4.4). Exceção: Decreto 51.503/2022 Art. 27 p.ú. II/IV — terreno com APP ou área alagadiça cai no rito ordinário LMP+LMI.
- Notion "Treinos e Testes" (`collection://7b0728a8-fd57-419c-8a51-d5fe3794d165`) é minha fila de treino/exame — consulto antes de executar.

### Caso ativo — Daniel-OB (escalada crítica de Wallenberg, 02/09/2026)

Área Privativa 04, Condomínio Venice, Orla Bothânica, Recreio, matrícula 141.944, EIS-PRO-2023/08061. 5 fontes de parâmetro urbanístico divergentes. Acionei Hely; auditei o retorno contra o PDF primário `LC104_2009_PEUVargens_REVOGADA.pdf` (Arts. 76 III / 89-93 verbatim — bate 100%; NÃO reconferi eu mesma Arts. 530/536 VI/538 da LC270/2024 nem a tabela do Anexo XXI AP4 — aceitei a citação de Hely com ressalva registrada no JSON).

Achados centrais:
1. Zoneamento-base **ZRM1-B AP4** confirmado com alta confiança por 3 fontes independentes (API ArcGIS sob POP, RIU screenshot de Claudemberg id=165197, Art. 345 §4º): CAB 1,0 / CAM 1,2 / TO máx 50% / gabarito 6pav-20m (afastado) ou 4pav-14m (não afastado) / afast. frontal 3m / lote mín 360 m² / testada 10 m / SMD 20% / ICS 0,36.
2. Fonte interna RTU-ORB-001 (22/04/2026) errou **CAB (disse 0,6, é 1,0)** e afastamento frontal (disse 5m, é 3m) — armadilha "subzona de nome parecido"; usou sistema antigo (lbb.php), nunca obteve CI oficial.
3. Parâmetros ampliados da OUC Legado Olímpico (LC284/2025 Setor III-H) **provavelmente NÃO em vigor** ainda pro lote (condicionantes do Art. 21 I/III não confirmadas satisfeitas). Explica por que o RIU específico do lote mostra só os parâmetros-base da LC270/2024.
4. **Achado central:** "PEU das Vargens" da Convenção = **LC104/2009**, mesma lei citada no Contrato, **REVOGADA** pela LC270/2024 Art. 536 VI. O Art. 92 §1º (revogado, mas vigente à época do protocolo em 2023) permitia calcular ATE por **MÉDIA do grupamento inteiro** — fundamento plausível pros números diferentes da Convenção (TO 108m²/60%, ATE 204m²/CA 1,13).
5. **Pergunta aberta que decide o caso:** LC270/2024 Art. 530 dá direito a exame pela legislação anterior para requerimento protocolado antes da vigência da LC270 (2024)? O grupamento EIS-PRO-2023/08061 é de 2023. Falta: data exata de protocolo, se não caducou/foi arquivado, se "grupamento" se enquadra em "licença de construção" pro Art. 530.

**Não decidi mérito nem fechei a pergunta central.** Registrado em `pendencias.json` (`kelsen-daniel-ob-legislacao-real-lote04`, crítica, `alc: humano`), relacionado a `lucio-daniel-ob-excedente-ate-cliente-aprovou` (Oscar apurou excedente de ATE ~29% no EP já assinado pelo cliente em 15/05). Recomendado a Wallenberg/Claudemberg: confirmar situação processual do EIS-PRO junto à SMDU/arquiteto parceiro antes de qualquer parecer; reavaliar o excedente do Oscar à luz da leitura "ATE por média" se o Art. 530 se confirmar aplicável. Gate do Maurício pendente — tudo é análise preliminar (Princípio 18).

### Caso EVTL Av. Projetada Canal 2 (fora do escopo das rotinas de drenagem — Wallenberg, 31/08)

PA 19170, Lote 1/Quadra 6, matrícula 21.336/9º RGI, ~10.500 m². Núcleo do parecer de pé desde 30/07: é **gleba, não lote** (LC270/2024 Arts. 289 V / 323 / 327 §2º — sem logradouro público aceito não há testada legal; um único gargalo mata prédio, casa e condomínio de lotes). B13/TRAVA C (zoneamento **ZCS E**) fechada 08/08 via RIU interativo (Claude in Chrome). B14 (transferência obrigatória — nem Quadro 24.3 >20.000m² nem Art. 305 >40.000m² cobrem ~10.500m²): busca exaurida; nota técnica bipartite `b14_nota_tecnica_lacuna_transferencia_evtl.md` pronta 27/08 (ANÁLISE PRELIMINAR — Leitura A/isenção favorecida por precedente SP Cota de Solidariedade; Leitura B/conservadora 15% por analogia). Caso conduzido pelo comercial (Maurício Fonseca, Novos Negócios) + Gate do Maurício (Costa). **Não toco.**

---

## 2. Pendências abertas

Fonte de verdade é `01_CEO/Pendencias/pendencias.json` — aqui só os ponteiros.

### Balde (a) — minha alçada
*(vazio — drenado em 23/07/2026)*

### Balde (b) — precisa do Hely produzir (Wallenberg orquestra a abertura)
- Retorno de Hely (tarefas A e B) auditado 31/08 contra o primário: **item 4 de `lucio-decisao-auditoria-oscar-11-08` FECHADO** da minha parte (li LC270/2024 pp.96-98 — Art. 278 §1º IV é a exceção textual: reforma/modificação interna sem acréscimo; qualquer coisa além disso exige DULI; COES não dispensa licenciamento; piso é LC270 Art. 278 §1º). `skill-caurj-rrt-009-2026-lacuna-numeracao` **aberto** (`alc: humano`) — Art. 8º da Res. 91/2014 **já tem §5º** (RRT Social), proposta da CEP-RJ colide com numeração vigente; devolver à Diária de Skills antes de ratificar. Monitoramento NÃO disparado.
- PDF da DP 009/2026 (domínio CAU/RRT) **pendente de indexação** em `_indice_fontes.md` — sem shell p/ regerar o `.pdf` gêmeo; entregar `.md` + `.pdf` juntos via Wallenberg.

### Balde (c) — sobe para Claudemberg
- **`b14-lacuna-substantiva-transferencia-evtl`** (`alc: humano`) — lacuna normativa real e não resolvida em substância; nota bipartite pronta, aguarda Gate do Maurício. Espera da SMDU encerrada por Claudemberg 27/08 (10 dias sem resposta). Sem mudança desde 28/08.
- **`kelsen-daniel-ob-legislacao-real-lote04`** (`alc: humano`) — ver Seção 1.
- **`drive-legal-fase2-frases-genericas`** (`alc: auto`) — redação das 5 substituições concluída (POP-ARQ-PL-01 3× + Memorial-Projeto Legal 2×: remove duplicação, corrige regência "à→ao", adiciona ressalva de fachada técnica). Wallenberg executa via Service Account **fora do modo automático** (bloqueio de permissão do modo automático, não gap de ferramenta).
- **`drive-legal-pops-copias-desatualizadas`** (`alc: auto`) — 4 cópias .md/.pdf no Drive congeladas em 2026-07-20 contradizem o repo (POP-LEGAL-02 pré-quarentena "status: oficial" sobre LC 274 morta; "POP-LEGAL-04" no Drive é o teste de escrita de 30/07, não o POP). Remover cópias (fonte única = repo local) OU sincronizar + regenerar PDFs sob POP-LEGAL-06. Wallenberg executa.
- **COES Art. 2º §7º (LC 291/2025)** — parcelamento bifamiliar meio-lote mínimo / testada 6 m: incide em **licenciamento de loteamento** (não é o que fazemos), impacto **baixo**. Sobe como oportunidade de negócio (produto novo), não risco de conformidade. Lote menor **não** aumenta coeficiente. Desde 21/07.
- **Migração de teste → produção real** (`000_CLIENTES_TESTE` no Drive). Desde 13/07.
- **POPs no Drive sem PDF** (RIU-01, 03, 04); **duas pastas distintas "GESTOR LEGAL"** no Drive. Organização. Desde 20/07.

---

## 3. Aprendizados que não posso esquecer

- **Fonte oficial vence fonte secundária.** RIU/Certidão da SMDU é palavra final.
- **Paráfrase nossa não é fonte — nem a que está no `_indice_fontes.md`.** Auditado duas vezes contra o primário e errado nas duas.
- **Granularidade é por bairro/subzona.** Código de subzona **não é único na cidade** — ler o cabeçalho do bloco de AP antes de aceitar qualquer linha do Anexo XXI.
- **Eu não executo.** Trabalho operacional vai pro Hely; eu decido, repasso contexto, audito. **E não faço o trabalho dele fingindo que ele fez** — quando a ferramenta falha, escalo o bloqueio, não fabrico o artefato.
- **Skill só vem de Wallenberg.** Lacuna eu sinalizo como proposta. **POP meu, eu mesmo corrijo** (autonomia de Gestor, 22/07/2026).
- **Conclusão marcada "RESOLVIDO" merece mais desconfiança, não menos.**
- **Erro em documento nosso não fica onde nasceu — ele se replica.** Sempre `grep` da frase errada na base inteira antes de dar a correção por concluída.
- **O elemento que reprova quase nunca é o que a pergunta destaca.**
- **Documento aprovado como oficial pode nascer errado.** POP-LEGAL-02 e 04 foram aprovados no mesmo dia e ambos tinham erro de artigo. **Aprovação não é verificação.**
- **"Exigência" que ninguém consegue citar por artigo provavelmente não existe.** O "A1 obrigatório" viveu na minha identidade e no meu POP como exigência da Prefeitura até ser varrido e não achado em lugar nenhum. Antes de barrar por regra herdada, exigir o artigo.
- **Auditar o retorno do Hely é olhar o artefato, não ler o relatório dele.**
- **Ter o texto certo da lei não é ter a lei certa.** Status jurídico e cadeia de alterações se conferem à parte, na Busca Fácil.
- **Norma pode morrer sem ninguém matá-la expressamente.** Não achar cláusula revogatória não prova que a norma antiga vive.
- **Não ler o Diário Oficial como documento único.** Delimitar o ato antes de atribuir a cláusula.
- **O Hely reporta com honestidade e pesa errado a relevância.** Minha auditoria não é procurar mentira — é reordenar prioridade.
- **Suspeitar de citação estranha, e ir ao primário.** A desconfiança pode estar certa em ser exercida e a conclusão dela ser absolver.
- **Onde eu não tenho base, eu digo.** Interpretação sobe para Claudemberg; não se resolve por escolha minha.
- **Lista de pendência envelhece igual a lei.** Em 23/07 achei 8 de 21 itens já feitos ou escalados a quem não devia. **Reconciliar antes de drenar** — senão a fila falsa esconde o urgente. E "esperando Wallenberg/Claudemberg" merece a mesma desconfiança que "RESOLVIDO": muita coisa parada ali já era minha.
- **Trava não espera produção.** Quando um documento nosso está errado e a correção depende de execução que não é minha, **suspender é ato meu e é imediato** — separar a trava da reescrita evita que o risco fique de pé esperando o conserto.
- **Diagnóstico registrado numa pendência também precisa ser auditado.** "Embutir fonte TTF no script" estava na fila havia dois dias e era **falso**: o script já emite latin-1, o ASCII vinha do JSON. Executar a pendência como escrita teria gasto trabalho sem corrigir nada.
- **Editar `.md` sem poder regerar o `.pdf` cria uma segunda verdade.** Se não dá pra atualizar o gêmeo na hora, isso é pendência **bloqueante** e tem que ser dita — não é detalhe de formatação.
- **Meu próprio resumo abreviado pode simular um conflito legal que não existe.** Em 24/07 um "conflito de artigo" (Art. 40 vs. 58) entre o achado do dia e o livro-razão de 21/07 era só diferença de nível de detalhe — os dois estavam certos, um mais completo que o outro. Antes de tratar duas citações como divergentes, voltar ao primário; não presumir que uma delas está errada só porque são citadas de formas diferentes.
- **Mecanismo real confirmado não é sinônimo de mecanismo relevante.** O Art. 17 §8º da LC 229/2021 (testada dupla, parâmetro mais favorável) é real e verbatim, mas só vale em áreas receptoras de Operação Interligada de AP2.2/AP3 e exclui ZRU — não pertence à Skill do nosso escopo (AP4, unifamiliar) enquanto não houver cliente real nessas condições. Confirmar que algo existe é etapa diferente de decidir que precisa entrar na base ativa (Princípio 19).
- **Autonomia de decisão concedida não é autonomia de execução garantida.** Em 28/07 tentei de fato executar a edição de documento do Drive (autonomia dada em 27/07) e travei: a sessão só me dá tools de leitura do Drive. Antes de marcar algo "auto" como pronto pra eu fazer sozinha, checar se a ferramenta de escrita existe na minha própria lista de tools — não presumir pela permissão.
- **A correção que o Hely fez num arquivo não garante que a mesma classe de bug não sobreviva em outro arquivo mudado na mesma rodada.** Em 28/07 ele corrigiu 4 setas unicode no `POP-GESTOR-LEGAL-01.md` mas não varreu o `POP-LEGAL-02.md` (mudado na mesma rodada) pela mesma falha — eu só achei porque rasterizei o PDF já regerado, não porque confiei no "ele já resolveu isso hoje". Auditar por arquivo, não por classe de correção já vista.
- **Quando eu edito um documento meu (POP), a obrigação de backup-antes-de-alterar é minha, igual à de qualquer Gestor** — não é privilégio só de execução do Hely.
- **Uma zona cinzenta de "obrigação vs. faculdade" não se fecha só relendo o artigo em dúvida — se fecha comparando como a MESMA norma trata os casos que ela própria qualifica como opcionais.** Em 53 artigos do Decreto 51.503/2022, só um instrumento (Art. 17, CMI) é chamado de "facultativo", e não é o que estava em dúvida. Quando a norma sabe dizer "opcional" e não disse no dispositivo em questão, isso pesa mais que eu decidir por conta própria o que "passível de" quer dizer isoladamente.
- **A pergunta do cliente quase nunca é a pergunta que decide o negócio.** No EVTL de 30/07 pediram "quantos pavimentos" em três hipóteses de produto. A resposta certa era **zero para as três**, e não por gabarito — porque o imóvel não é `lote` na acepção do `Art. 289, V` da LC 270/2024. Antes de responder o parâmetro pedido, checar se o **pressuposto** do parâmetro existe. Isso é o que me faz camada de julgamento e não repasse.
- **Escrever "≥ 2.000 m²" quando a norma diz "≥ 20.000 m²" é o erro mais fácil de cometer e o mais caro num parecer para investidor.** Aconteceu comigo, no mesmo dia, entre a 1ª e a 2ª passagem — e só apareceu porque reli o Anexo verbatim em vez de confiar na minha própria anotação de horas antes. **Minha nota recente tem o mesmo status de confiabilidade que paráfrase de terceiro** — recência dá falsa segurança. Reler o primário mesmo quando a fonte do resumo sou eu.
- **Conclusão que se sustenta por aritmética vale mais que conclusão que depende de dado não confirmado — procurar ativamente a primeira.** No EVTL: aterrar 10.500 m² com 0,50 m já dá 5.250 m³ e cruza o gatilho de 5.000 m³. **Quando duas exigências legais se travam uma na outra, essa trava é o argumento mais forte disponível** — não há dado faltante que a desfaça.
- **Dois nomes parecidos podem ser regimes de entes federativos diferentes: FMP não é APP.** FMP é estadual (INEA) e alcança canal artificial; APP do Código Florestal fala em "curso d'água natural". É juridicamente possível haver uma sem a outra. **Não tratar como sinônimo, e não estimar largura de FMP** — a LC 270/2024, Art. 459, remete ao órgão de gestão hídrica.
- **Artigo lido fora da sua Subseção mente.** O Art. 409 da LC 270/2024 parece regra geral de ZRM e é regra de RA específica (está antes da Subseção de Santa Teresa). É a armadilha do cabeçalho de AP do Anexo XXI, na mesma lei, em outro lugar. Ler para cima até achar o cabeçalho da Seção/Subseção antes de citar qualquer artigo de "condições específicas".
- **Quando falta a ferramenta, o parecer honesto vale mais que o parecer completo.** Entregar o EVTL com bairro/zona/Anexo XXI marcados NÃO CONFIRMADO, com a consulta exata que fecha cada um e o grau de confiança declarado por seção. **Para um fundo, declarar a incerteza constrói credibilidade; escondê-la destrói.**
- **Auditar sem a mesma ferramenta que o Hely usou não é auditoria vazia — é auditoria de outro tipo, e tem que declarar qual.** "Não posso confirmar tudo" não é motivo para não confirmar o que dá — e dizer com precisão qual pedaço ficou confirmado por mim e qual continua no grau que Hely declarou é mais honesto do que emprestar confiança geral pro relatório inteiro.
- **Um artigo que Hely não citou pode ser exatamente o que resolve a lacuna que ele deixou em aberto.** A lacuna de Hely não era a resposta — era a metade da pergunta.
- **Localizar arquivo pelo nome parecido não é localizar pelo conteúdo.** Em 30/07 registrei um ID de planilha só porque o título continha "Enviáveis" — era a errada. Só a leitura literal do conteúdo (`read_file_content`) confirma. Mesmo cuidado que aplico com lei, agora vale para arquivo do Drive.
- **A lei central pode ser 100% muda sobre um trâmite que ainda assim se aplica.** "Varredura negativa na lei X" só fecha pendência sobre o que a lei X regula; para saber se existe trâmite paralelo em outro órgão, a varredura tem que ser na norma daquele órgão.
- **Pendência escrita só em tabela de texto (não no `pendencias.json`) é invisível pra reconciliação automática — mesmo eu mesma esquecendo dela.** B4-B8 e B14 ficaram 19-30 dias como linha de tabela, nunca no JSON que a rotina de drenagem lê. Pendência real que sobrevive mais de uma rodada tem que virar item no JSON.
- **Bloqueio de "interface web sem API" tem solução genérica, não uma por caso.** Google Forms ilegível por mime e RIU interativo sem endpoint têm a mesma solução (Claude in Chrome lê a página renderizada). Antes de registrar um bloqueio como "sem rota", checar se um bloqueio de classe parecida já foi resolvido em outro lugar do organismo.
- **Busca exaurida sem achado fecha a TAREFA, não necessariamente a PENDÊNCIA.** Resultado negativo que toca caso real com terceiro na mesa carrega risco de mérito que não decido sozinha — vira item novo de Balde (c), não fica escondido dentro do item fechado.
- **Acionar o Hely via `Agent` não garante retorno na mesma sessão — a ausência de notificação não é "ainda processando", pode ser impedimento real.** Confirmar ausência de retorno é tão importante quanto confirmar o retorno. (Desalinhamento recorrente: a notificação de conclusão de Hely às vezes vai para Wallenberg, não para mim.)
- **Aprendizado que se repete três vezes e continua só reativo é uma lacuna de processo, não uma sequência de azar.** O bug de glifo silencioso em PDF foi corrigido 3× antes de virar POP-LEGAL-06 (07/08). Segunda ocorrência do mesmo tipo de erro = formalizar processo, não só corrigir de novo.
- **`Read` lê PDF diretamente** (extração de texto, até 20 páginas/chamada) — 2ª via independente da rasterização de Hely para auditar PDF pequeno. Ferramenta padrão minha desde 11/08.
- **O cabeçalho de `_estado_hely.md` é volátil — achado real registrado só ali, sem virar item no `pendencias.json`, desaparece na próxima sobrescrita.** Ler o estado do Hely inteiro (não só a resposta da tarefa que pedi) antes de fechar a rodada.

---

## 4. Como escrevo neste arquivo

- **Substituo seções, não faço append.** Apago o que virou passado.
- O **log cronológico de rodadas** (reconciliações, "sem execução nova", auditorias já fechadas) vai para `_estado_kelsen_HISTORICO.md` — **não leio esse arquivo ao nascer**. Aqui fica só o estado atual.
- **Reconcilio contra os arquivos** (`pendencias.json`, POPs, `_indice_fontes.md`), não contra a memória desta seção.
- Aponto para docs em vez de copiar. **Não gero PDF deste arquivo** (é arquivo de máquina, reescrito toda hora).
- Aprendizado durável entra na Seção 3 (nunca é podado). Estado que envelheceu sai da Seção 1.
