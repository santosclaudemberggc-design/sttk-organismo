# Anexo 03. Organograma funcional e esquemas básicos (PN-ARQ 5.2.1 a e b)
## Ensaio Sombra 003, Montenegro Prates (caso 100% FICTÍCIO). Oscar, 13/10/2026, v4

**Escopo:** relações funcionais e fluxos programáticos. **Não há posição de ambiente, adjacência espacial em planta, nem desenho.** Isso é da Etapa 05.
**Base:** NBR 6492:2021, item 5.2.1 a (organograma funcional) e b (esquemas básicos dos ambientes), conforme Skill `nbr6492-2021-memoriais-por-etapa-projeto` §2 [lido, Skill]. Texto da norma [nv].
**Gráficos em escala (5.2.1 b):** adiados para a Etapa 05, com dono Oscar e Lúcio. Aqui a caracterização vai em texto e tabela. Essa lacuna está registrada em 06.

---

## 1. Organograma funcional (5.2.1 a)

Zonas funcionais e ambientes, sem posição:

| Zona | Ambientes (ver 02) | Caráter | Acesso de quem |
|---|---|---|---|
| Social | A5 estar/jantar; A7 área gourmet | convívio, visitas | moradores, visitas |
| Íntima | A1 suíte acessível (térreo); A2 demais suítes | repouso | moradores; D. Lourdes (A1) |
| Trabalho | A3 escritório / home office | trabalho; atendimento se aprovado | moradores; clientes, se aprovado (P-escritório) |
| Lazer | A4 cinema; A11 piscina; A12 deck; A13 jardim | lazer | moradores, visitas |
| Serviço | A6 cozinha; A8 serviço com dependência; A14 edícula (se mantida) | apoio | empregados, serviço |
| Veículos | A9 garagem (4 vagas, n cobertas) | estacionamento | moradores, visitas, serviço |
| Externa | faixa frontal, faixas laterais e fundos (permeáveis) | acesso, permeabilidade | todos |

**Relação entre zonas (requisito funcional, não adjacência):** a zona de veículos é a porta de entrada para as demais; a zona íntima deve ter acesso por circulação interna; a zona de serviço tem acesso separado da social, conforme a relação abaixo. **Essa separação não é lei: é requisito do programa.** Fonte: caso §1 (pedido de serviço com dependência). Dono: Cliente.

---

## 2. Fluxos (5.2.1 a: pessoas, serviço, carro, D. Lourdes)

| Fluxo | Origem → destino | Requisito | Condição de fato (o que depende de quê) | Dono |
|---|---|---|---|---|
| **Pessoas (moradores)** | entrada social → social (A5) → cozinha (A6) e área gourmet (A7); entrada → zona íntima (A2) | acesso social separado da zona íntima e da zona de serviço | o acesso de pedestres à frente depende de locação e largura do passeio (T6, T7, dossiê; COES Art. 35 §§2º–3º [nv]) | Cliente; topógrafo (T6, T7) |
| **Pessoas (visitas)** | entrada social → social (A5); visitas à área gourmet (A7) | acesso sem passar pela zona íntima | igual ao anterior | Cliente |
| **Serviço** | acesso de serviço → cozinha (A6) → serviço com dependência (A8); edícula (A14), se mantida | acesso de serviço separado | depende de se existe passagem lateral. Lateral útil de 2,50 m (faixa de circulação, COES Art. 29 IV, p. 15 [lido]); passagem por fundos atravessa área comum (faixa verde, dossiê), não presumida | Cliente; Kelsen (fundos, condomínio) |
| **Carro** | rua (frente) → acesso de carro no frontal → garagem (A9) → entrada da casa | 4 vagas; manobra fora da via pública | depende de: n cobertas (1 a 4); manobra e acesso pela frente, entre as 3 árvores (locação T11); vaga descoberta no frontal é alternativa A, vedada no texto (status na Etapa 03 C-8) | Cliente (n); Kelsen; Gate; topógrafo (T11) |
| **Acesso de D. Lourdes** | rua → (rampa ou degrau, se houver) → entrada → suíte acessível (A1) → banheiro e área de convívio | sem escada; ligação do térreo à rua | desnível rua × soleira desconhecido (T2, T4). Rampa de veículo no frontal: ≤ 10% e ≤ 0,50 m de altura (LC 270 Art. 363 §3º, p. 130 [lido]), sem prejudicar acessibilidade. Acima de 0,50 m, sai do frontal e, se coberta, consome projeção | Cliente; topógrafo (T2, T4); EP (Etapa 05) |
| **Acesso de D. Lourdes à garagem** | garagem (A9) → entrada → A1 | sem escada entre garagem e suíte | depende de a entrada da casa ser no térreo e de o acesso de carro ser sem degrau (a definir) | Cliente; EP |

**Nota de cômputo (D. Lourdes):** a suíte no térreo é programa, não lei. COES Art. 31 V (p. 17 [lido]) dispensa a unifamiliar das normas técnicas de acessibilidade. Lei federal e NBR 9050:2020 não lidas (P-m).

---

## 3. Matriz de relações funcionais (5.2.1 a)

Marcação: **R** = relação requerida; **D** = relação desejável; **—** = sem relação requerida. Cada célula é requisito do programa, não posição de planta.

| De \ Para | A1 suíte acessível | A2 suítes | A3 escritório | A5 estar/jantar | A6 cozinha | A7 gourmet | A8 serviço | A9 garagem | A14 edícula |
|---|---|---|---|---|---|---|---|---|---|
| **A1 suíte acessível** | — | D | — | R (acesso de D. Lourdes) | — | — | — | R (sem escada) | — |
| **A2 suítes** | D | — | — | R | — | — | — | — | — |
| **A3 escritório** | — | — | — | D | — | — | — | — | — |
| **A5 estar/jantar** | R | R | D | — | R | D | — | D | — |
| **A6 cozinha** | — | — | — | R | — | D | R (serviço) | — | D |
| **A7 gourmet** | — | — | — | D | D | — | — | — | — |
| **A8 serviço** | — | — | — | — | R | — | — | R (acesso de serviço) | R (se mantida) |
| **A9 garagem** | R (sem escada) | — | — | R | — | — | R | — | — |
| **A14 edícula** | — | — | — | — | D | — | D | — | — |

**Pendências desta matriz:** a relação entre escritório e atendimento de clientes (P-escritório) não está definida. Não há relação com entrada externa independente enquanto Kelsen não responder.

---

## 4. Esquemas básicos dos ambientes (5.2.1 b): caracterização em texto e tabela

| Ambiente | Área | Dimensões | Mobiliário (exigência) | Outras exigências | Dono |
|---|---|---|---|---|---|
| A1 suíte acessível | a definir | a definir | cama, banho acessível, circulação livre (NBR 9050:2020 [nv]) | sem degrau; térreo; sem escada | Cliente; Kelsen (P-m) |
| A2 suítes | a definir | a definir | cama, banheiro | salubridade (COES Art. 31 caput, p. 17 [lido]) | Cliente |
| A3 escritório | a definir | a definir | mesa, armário | porta própria (pedido); atendimento (P-escritório) | Cliente; Kelsen |
| A4 cinema | a definir | a definir | poltronas, tela | acústica (a definir, Cardozo/Tenreiro) | Cliente |
| A5 estar/jantar | a definir | a definir | sofá, mesa de jantar | ligado à cozinha (requisito) | Cliente |
| A6 cozinha | a definir | a definir | bancadas, equipamentos | ventilação e exaustão (COES, a definir na Etapa 05) | Cliente; Oscar |
| A7 gourmet | a definir | a definir | churrasqueira, bancada | churrasqueira integrada à fachada (COES Art. 8º §6º, p. 5 [lido]) | Cliente |
| A8 serviço com dependência | a definir | a definir | tanque, máquina, guarda-volumes, dependência | acesso separado | Cliente |
| A9 garagem | 4 vagas (n cobertas) | 2,50 × 5,00 m por vaga; manobra 2,50 × 5,00 m; circulação 2,50 m (COES Art. 29 I, II, IV, p. 15 [lido]) | — | pé-direito livre ≥ 2,20 m (COES Art. 28 II, citado pela Skill de vaga; p. 14 não lida nesta execução [nv]) | Cliente (n); Hely via Kelsen (a) |
| A10 varandas | a definir | a definir | mobiliário externo | ver 02 e corpo §4 | Kelsen; condomínio |
| A11 piscina | a definir | profundidade até 1,60 m (Regramento, dossiê) | — | fundo 0,70 m abaixo do NA (E-18); laudo | Cliente; Baumgart/Cardozo |
| A12 deck | a definir | a definir | — | impermeável | Cliente |
| A13 jardim | a definir | a definir | — | permeável; paisagismo | Cliente; Glaziou |
| A14 edícula (se mantida) | a definir | 0,80 m da divisa direita (dossiê) | — | falta 1,70 m (Regramento) e 0,70 m (COES p.u.), E-14 | Cliente; Kelsen |

---

## 5. Declaração

- Não há posição, adjacência espacial em planta, nem desenho. Esquemas em escala ficam para a Etapa 05.
- Relações e fluxos vêm dos pedidos (caso §1, §4; mensagens de 07 a 09/10) e da Etapa 03 v8 (acessos, árvores, rampa). Nada foi tirado de gabarito.
- Oscar, 13/10/2026 (v4)
