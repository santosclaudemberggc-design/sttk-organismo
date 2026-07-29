# Estado — Kelsen (Gestor Legal)

> Arquivo de estado pessoal. Leio ao nascer (toda vez que Wallenberg me aciona), escrevo ao morrer (antes de devolver o retorno a ele).
> Memória privada minha — não repete o Registro Diário, que é o que Wallenberg leva pra Claudemberg.

**Última atualização:** 27/07/2026

---

## 1. Onde parei / em andamento

- Aprovado por Claudemberg em **13/07/2026**. Equipe: **Hely**, único Agente. Eu sou **Autonomous** desde 22/07/2026.
- Base legislativa: Recreio / Barra / Vargem Grande (AP4). Fontes em `Agentes/Hely/Fontes_Legislacao/`, índice em `_indice_fontes.md`. POPs meus em `Agentes/Hely/POPs/` (RIU-01, 02 **SUSPENSO**, 03, 04, 05) + `POP-GESTOR-LEGAL-01` na minha pasta.
- Casos-teste (fictícios): Bittencourt, Kowalski Andreatta, Petrella Wachowski, Vasconcelos, Clínica Bem-Estar Recreio, Benatti. **Nenhum cliente real ainda.**
- **Contexto que reposiciona toda a base: a Sttickler é UNIFAMILIAR** (confirmado por Claudemberg). Unifamiliar segue o **rito completo** — não existe rito de baixa complexidade (Resolução SMDEIS 27/2021 e seu decreto-âncora estão "Sem efeito"). O único tratamento diferenciado vigente é **Anexo IV no lugar do III** (Decreto 55.622/2025, Art. 10, p.ú.) — peça, não rito.

- **27/07/2026 — AUTONOMIA CONTÍNUA DE TREINO/TESTE ATIVADA.** Você é Autonomous desde 22/07/2026; agora tem estrutura de verdade pra treinar o Hely. Notion database "Treinos e Testes" criada em 27/07 — essa é sua fila. Você consulta antes de qualquer execução, vê se há treino pendente (Status = "pendente", Gestor = seu nome), abre Hely se necessário, audita, registra na Seção 0 do estado dele e atualiza Notion. Sem esperar ordem de Wallenberg — é autonomia contínua, não automática.
  - **Data source Notion:** `collection://7b0728a8-fd57-419c-8a51-d5fe3794d165`
  - **Primeiros treinos:** nenhum registrado ainda (banco vazio em 27/07). Aguardando Wallenberg designar o primeiro exame, ou você criá-lo sob demanda (novo Agente futuro, promoção de nível do Hely, etc.).

- **23/07/2026 — 1ª DRENAGEM CONTÍNUA DE PENDÊNCIAS** (regra nova do `CLAUDE.md`). Reconciliei a fila item a item contra os arquivos, classifiquei em três baldes e executei o meu. Relatório integral entregue a Wallenberg — **não repetir aqui**.
  - **A fila estava inflada: 8 de 21 itens já estavam feitos ou eram falsa escalação.** Lista que envelhece vira fila falsa, e fila falsa esconde o que é urgente de verdade.
  - **Executei (backup em `01_CEO/Decisoes_Autonomas/_backups/2026-07-23/`):**
    1. **`POP-LEGAL-02` posto em QUARENTENA** — `status:` mudado para SUSPENSO, bloco `## 0` no topo separando o que morreu (scaffolding da LC 274), o que sobrevive (LC 281, arts. 18-19) e o que precisa ser reconfirmado; 5 marcações inline nos pontos perigosos. **Suspendi antes de reescrever, de propósito:** a reescrita é produção do Hely, mas o risco de alguém abrir o arquivo e ver `status: oficial` sobre lei morta era hoje.
    2. **`POP-GESTOR-LEGAL-01` revisado** — removida a exigência inventada de A1 (3.4); acrescentados Busca Fácil como passo obrigatório (4.1), APAC/Art. 280 III (4.2) e a regra de documento em quarentena (4.3); **decididas** as duas pendências que esperavam julgamento meu: Anexo III vs. IV (3.5) e cores em obra nova (3.6).
  - **Achado meu durante a drenagem, que corrige um diagnóstico errado da própria fila:** a pendência do PDF sem acentuação mandava "embutir fonte TTF no `gerar_prancha_legal.py`". **O script não é o culpado** — `_limpa()` mapeia para **latin-1**, que contém todos os acentos do português. O ASCII veio do **dado**: `caso_prancha.json` tem **1** caractere acentuado no arquivo inteiro. Corrigir o script não resolveria nada.
  - **Levantei ao Wallenberg um risco que eu mesmo criei:** os `.pdf` gêmeos dos dois POPs que editei ficaram **desatualizados** — não tenho shell nesta execução para rodar o `md_to_pdf.py`. Quem ler o PDF do POP-LEGAL-02 **não vê a quarentena**.

- **24/07/2026 — Auditoria do achado de Wallenberg sobre a LC 301/2026 (rotina diária Cérebro/Criador de Skills, Funções 3+5).** Wallenberg trouxe um resumo do LegisWeb (agregador) com 3 pontos e um conflito de artigo a resolver. Não usei o resumo como fonte — reli o **PDF primário já arquivado** (`LC301_2026_AEIUPracaOnze_AlteraLC270e281.pdf`, 54 pp., verbatim) do Art. 1º ao 63 e todos os Anexos.
  - **O "conflito" Art. 40 vs. Art. 58 não existia.** Verbatim (p. 44): *"Art. 58. O art. 40 da Lei Complementar nº 281 [...] passa a vigorar com a seguinte redação [...]"* — Art. 58 é o dispositivo **da LC 301** que altera; Art. 40 é o dispositivo **da LC 281** que é alterado. O índice já registrava isso certo e completo desde 21/07/2026. A aparência de conflito veio de uma citação **abreviada minha** (balde (c) deste arquivo, que cortou "Art. 58" ao resumir) comparada contra o achado de hoje — não um erro de fato em nenhuma das duas datas. **Lição:** meu próprio resumo, mesmo dentro de casa, pode simular uma divergência que só existe entre dois graus de detalhe, não entre dois fatos.
  - **Três dispositivos novos confirmados verbatim, todos fora do escopo AP4:** Art. 35 (Anexo XXI, só Região de Planejamento 2.2 — Tijuca etc.); Art. 61 (revoga §incisos de gabarito do Art. 61 da LC 229/2021, o Art. 65-B dela, o Anexo A da LC 97/2009, e **o §1º do Art. 437 da LC 270/2024** — revogação direta, não "por decorrência"); Art. 17 §8º da LC 229/2021 (testada dupla com zoneamento distinto, parâmetro mais favorável em toda a extensão do lote).
  - **Julguei o Art. 17 §8º como mecanismo de nicho — não entra na Skill agora, decisão minha, não pendência.** Só vale em áreas receptoras de Operação Interligada em **AP 2.2 e AP 3** (nenhuma é AP4), **exclui explicitamente ZRU** (o regime que cobre a maioria dos nossos lotes unifamiliares), e pressupõe reconversão/retrofit dentro do desenho de Operação Interligada — não licenciamento residencial comum. Princípio 19 (crescimento por demanda da Skill). Registrado no índice pra não precisar repesquisar se algum dia surgir cliente de AP2.2/AP3 com lote de testada dupla.
  - **Editei, com backup em `01_CEO/Decisoes_Autonomas/_backups/2026-07-24/`:** (1) `SKILL.md` — só reforcei a linha "Janela de contrapartida com desconto" com a nota de verbatim conferido (conteúdo não mudou, já estava certo); (2) `_indice_fontes.md` — nova seção "AUDITORIA DA LC 301/2026 CONTRA O PRIMÁRIO — 24/07/2026" com os 4 pontos acima.
  - **Risco que se repete do dia 23/07:** não tenho shell nesta execução. O `_indice_fontes.pdf` (que já existe como gêmeo) e um eventual `SKILL.pdf` (que nunca existiu — não vou criar precedente novo sem decisão de Wallenberg) ficam **desatualizados** frente ao `.md`. Mesma pendência bloqueante de B1, agora estendida.

- **27/07/2026 — Julgamento sobre achado de Wallenberg: Resolução SMAC 27/2020 (PGRCC) é trâmite AMBIENTAL paralelo, não o mesmo do LICIN 2.0.** Reli o Decreto 55.622/2025 inteiro (14 pp., verbatim) para responder à pergunta central. **Confirmado**: o decreto não menciona PGRCC/LMI/resíduo em nenhuma linha; sua única ponte com a SMAC é a autodeclaração de "passivo ambiental" do Anexo II item III.5, que cita a **Res. SMAC 605/2015** — resolução diferente da 27/2020. São dois trâmites: LICIN 2.0/SMDU termina em Habite-se; LAM/SMAC termina em LMI, condicionado a PGRCC quando incide. **O que não confirmei, e não presumi**: se um lote unifamiliar padrão sem os gatilhos ambientais já autodeclaráveis no Anexo II (vegetação, curso d'água, risco geológico, passivo ambiental) está mesmo sujeito ao LAM — falta a norma que define o âmbito de incidência do LAM, e o texto primário da Res. 27/2020 (o PDF oficial não abriu por encoding, só tenho via LegisWeb/secundária). **Editado com backup em `01_CEO/Decisoes_Autonomas/_backups/2026-07-27/`:** nova seção no `_indice_fontes.md` ("LICENCIAMENTO AMBIENTAL MUNICIPAL (SMAC)"); `SKILL.md` recebeu só duas edições mínimas — item na lista de restrições a checar (passo 3, "Como usar") e entrada em "Lacunas conhecidas" — **não virou armadilha fechada**, porque a aplicabilidade ao nosso escopo não está confirmada por primário. Não é urgente para caso real hoje (zero cliente ativo); vira urgente se a pendência de confirmação (Balde B) mostrar que unifamiliar sem gatilho também está sujeito.

## 2. Pendências abertas

### Balde (a) — minha alçada
*(vazio nesta data — drenado em 23/07/2026)*

### Balde (b) — precisa do Hely produzir (Wallenberg orquestra a abertura)

| # | O que o Hely tem que produzir | Desde |
|---|---|---|
| B1 | 🔴 **Regerar os `.pdf`** de `POP-LEGAL-02`, `POP-GESTOR-LEGAL-01` **e agora também `_indice_fontes.md`** (`_ferramentas/md_to_pdf.py`). Os PDFs atuais não mostram a quarentena nem a auditoria de 24/07 sobre a LC 301/2026. Usar marcador textual `[ATENÇÃO]` e `->` — o script descarta glifos sem fonte Symbol, silenciosamente. Avaliar também se `SKILL.md` (`legal-base-legislativa-bairro`) passa a ter PDF gêmeo — nunca teve um; não decidir sozinho, perguntar a Wallenberg (ele é quem define a regra de PDF). | 23-24/07 |
| B2 | 🔴 **Reescrever o POP-LEGAL-02** sobre a LC 281/2025, arts. 18-20, transcritos **verbatim** do `LC281_2025_CondicoesEspeciais_CONSOLIDADO.pdf`. Reencontrar o endereço vivo da Outorga de Alteração de Uso. **Levantar a quarentena é decisão minha**, depois de auditar contra o primário — não dele, e não por decurso de prazo. | 21/07 |
| B3 | **Acentuação da prancha:** repovoar `caso_prancha.json` com texto acentuado e regerar. **Não mexer no script** (ver seção 3). Conferir rasterizando, não pelo "rodou sem erro". | 21/07 |
| B4 | **POP-LEGAL-04 §8 (glosa "0,3 do CAM"):** arquivar o *Dicionário de Termos da LC 270/2024* e extrair o **Art. 367 verbatim**. Hipótese a testar: os dois estão certos em registros diferentes e o certo é **anotar**, não reescrever. Não alterar nada antes de eu ver o primário. | 20/07 |
| B5 | **Decreto 45.917/2019** (regulamento do COES) pela **Busca Fácil** — a premissa "esperar via oficial" venceu, a via existe desde 21/07. | 20/07 |
| B6 | **Propagar para os POPs do Hely** o que decidi no POP-GESTOR-LEGAL-01: trava de colisão de subzona entre APs no `POP-LEGAL-RIU-01` §6 e no `_indice_fontes.md`; decisões 3.5 e 3.6 no `POP-LEGAL-05` (fecha L-6 como decisão adotada, mantendo a ressalva). | 20-21/07 |
| B7 | **Mapear incidência de APAC** em Recreio/Barra/Vargem Grande (`LBB_APAC`), para saber se o Art. 280, III é hipótese real ou remota no nosso escopo. | 21/07 |
| B8 | **Varredura de decretos e resoluções** no acervo Busca Fácil. Varremos com rigor as 145 LCs; o universo de decretos/resoluções **não**. A base não está provada completa. | 21/07 |
| B9 | **Resolução SMAC 27/2020 (PGRCC) e o âmbito de incidência do Licenciamento Ambiental Municipal.** Obter o texto primário (o PDF oficial linkado não abriu por encoding — tentar Busca Fácil ou portal da SMAC); confirmar status no Busca Fácil; e, o essencial, **achar a norma que define quando uma construção está "sujeita ao Licenciamento Ambiental Municipal"** — se unifamiliar padrão sem gatilho ambiental (sem vegetação/curso d'água/risco geológico/passivo ambiental, os mesmos itens já autodeclaráveis no Anexo II do LICIN 2.0) se enquadra ou é dispensada. Não decidir aplicabilidade por presunção. Detalhe em `_indice_fontes.md`, seção de 27/07/2026. | 27/07 |

### Balde (c) — sobe para Claudemberg

| Pendência | Desde |
|---|---|
| **Exame 3 do Hely fechado: veredito PROMOVE a Autonomous (escopo cliente).** Ratificar e conciliar o registro de nível — o `CLAUDE.md` ainda diz "Formação no escopo cliente". | 23/07 |
| 🔴 **COES Art. 35 §7º (LC 283/2025): dutos no passeio obrigatórios em TODA nova edificação.** Escopo Construção do Zero exato. Custo de obra e item de projeto que **ninguém orçou**. Atravessa Legal → Complementares → proposta comercial. | 21/07 |
| **Janela comercial ABERTA até 01/12/2026, 30% à vista** (LC 281 Art. 40, redação da LC 301/2026 Art. 58). Nossa base a dava por expirada. Decisão de negócio. **Não confundir com os descontos do Art. 19, que expiraram** — hipóteses de incidência diferentes. **24/07: artigo reconferido verbatim no primário, sem ambiguidade — o que restava era só a decisão de negócio, não mais dúvida de fundamento.** | 21/07 |
| **COES Art. 2º §7º (LC 291/2025): parcelamento de lote bifamiliar com metade do lote mínimo e testada 6 m.** Minha avaliação: incide em **licenciamento de loteamento**, que não é o que fazemos — impacto **baixo** no escopo atual. Sobe como oportunidade de negócio (viabiliza produto novo), não como risco de conformidade. Não confundir com CAB/CAM: lote menor **não** aumenta coeficiente. | 21/07 |
| **Base oficial do Drive (POP-ARQ-PL-01, Memorial, Planilha) desconhece o LICIN 2.0** — não citam DULI, Decreto 55.622/2025, COES nem LC 270/2024. O POP oficial é de 05/03/2026, anterior a tudo que construímos. Documento do Drive é de Claudemberg. | 20/07 |
| **A Planilha de Enviáveis vende entregável que a prefeitura recusa** (fachadas legais; memorial "para protocolo legal"). A dúvida jurídica está **resolvida — a recusa se sustenta**. Falta corrigir os documentos, que é decisão dele. | 20/07 |
| **Os dois formulários de Legal são ilegíveis por ferramenta** (mime `google-apps.form`). Confronto campo-a-campo não executado. Precisa export manual. | 20/07 |
| **Migração de teste → produção real** (`000_CLIENTES_TESTE` no Drive). | 13/07 |
| **POPs no Drive sem PDF** (RIU-01, 03, 04); **duas pastas distintas chamadas "GESTOR LEGAL"**. Organização do Drive. | 20/07 |

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
- **A lei central pode ser 100% muda sobre um trâmite que ainda assim se aplica.** O Decreto 55.622/2025 tem zero menções a PGRCC/LMI/resíduo — isso prova que o LICIN 2.0 não absorve o Licenciamento Ambiental Municipal, não prova que o LAM não se aplica ao nosso caso. "Varredura negativa na lei X" só fecha pendência sobre o que a lei X regula; para saber se existe trâmite paralelo em outro órgão, a varredura tem que ser na norma daquele órgão, não na nossa. Mesmo padrão do achado de APAC (21/07), mas lá o gatilho já era conhecido — aqui ainda não é, e eu não fechei essa por presunção.

## 4. Como escrever neste arquivo

Antes de devolver o retorno a Wallenberg, atualize as 4 seções: substitua o que mudou, apague o que virou passado, mantenha só o que o próximo Kelsen precisa pra continuar. Não vire diário nem repita o conteúdo dos documentos — aponte pra eles. **A seção 2 se reconcilia contra os arquivos, não contra a memória** — item que já está feito sai da lista; item marcado "esperando alguém" que na verdade é meu volta pro balde (a).
