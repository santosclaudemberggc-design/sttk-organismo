---
name: sttickler_marco_vitruvius
description: "MARCO ATINGIDO em 29/07/2026 — Vitruvius confirmado por Claudemberg como capacidade oficial (escrita real no Revit, não só leitura)"
metadata:
  type: project
---

Definido por Claudemberg em 20/07/2026, durante o detalhamento do Lúcio (Gestor Arquitetura, ver [[sttickler_ceo_wallenberg]]). **Marco atingido em 29/07/2026.**

**O que aconteceu:** Wallenberg testou a ponte Vitruvius ao vivo com Claudemberg — `revit_status`/`get_model_info` confirmaram conexão real (Revit 2026, build 26.0.10.8); um teste de escrita controlado num arquivo de teste dedicado ("Projeto2", aberto por Claudemberg para o teste) criou uma parede real (`create_wall`, confirmada via `list_elements`) e apagou em seguida (`delete_element`), devolvendo o arquivo ao estado original. Claudemberg then autorizou: **"pode virar capacidade agora"**.

**O que isso muda:** o Coordenador de Projeto Arquitetônico de Lúcio deixa de "só coordena o arquiteto parceiro" e passa a **produzir diretamente no Revit** como capacidade oficial. O mesmo vale para o futuro Agente Estrutural do Gestor Complementares (rascunho "Cardozo") e qualquer outro Agente cuja disciplina o Vitruvius alcance.

**Capacidade real confirmada em 29/07/2026 (ver [[sttickler_revit_capacidade]] para a lista completa):** o toolset saiu de "criar parede/piso/sala/porta/janela/nível" (estado de 16/07) para um conjunto muito mais completo — inclui Ambientes de verdade (`create_room`, `create_rectangular_room`, separadores de ambiente integrado), cotagem oficial pra prancha de prefeitura (`dimension_facade`), cotagem de ambiente e de parede, elevações (fachada e interna), cortes, folhas/pranchas (`create_sheet`), tabelas/quadro de áreas (`create_schedule`), posicionar vista em prancha, mover/redimensionar/trocar tipo, parâmetros em lote. O gap de 16/07 (sem Room, sem cota) **está fechado**.

**O que NÃO muda (limite permanente, não é sobre capacidade técnica):** a exigência de RRT/ART por profissional licenciado continua — ver [[sttickler_revit_capacidade]], seção "Limite permanente". Produzir o desenho não substitui a revisão/assinatura humana.

**Como aplicar agora:** atualizar a identidade de qualquer Gestor/Agente cuja capacidade dependia deste marco (feito em `lucio.md` e no rascunho do Cardozo em 29/07/2026) — não precisa mais tratar "produção direta no Revit" como capacidade futura condicionada. Continua valendo: cada Agente que for de fato produzir precisa ser testado num caso real antes de ir a cliente (mesmo rigor já aplicado a Hely).
