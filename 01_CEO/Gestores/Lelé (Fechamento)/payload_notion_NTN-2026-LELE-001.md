# Manifesto de Carga — NTN-2026-LELE-001 → Notion "Treinos e Testes"

> Mapeamento de payload para a linha que representa o cenário `cenario_teste_notion_001.md` na base Notion real. Schema confirmado por consulta direta à coleção (`notion-fetch`, não assumido) em 16/09/2026.

## 1. Schema real da coleção (fonte da verdade)

| Coluna Notion | Tipo | Descrição declarada na base |
|---|---|---|
| `Agente` | title | (identificador primário da linha — é o "nome" da página) |
| `Gestor` | text | — |
| `Exame` | text | "ex: Shadow→Assisted, Assisted→Autonomous" |
| `Status` | select | opções fixas: `pendente`, `em execução`, `aprovado`, `reprovado` |
| `Caso-teste` | text | "referência ao arquivo local ex: Casos_TESTE/Recreio/Benatti" |
| `Criado em` | date | — |
| `Atualizado em` | date | — |
| `Resultado` | text | "evidência do exame: iscas barradas, falhas, etc." |

**Não existem campos livres de texto longo** (sem "descrição" nem "notas") — a base é deliberadamente enxuta: um ponteiro para o arquivo local, não um espelho do conteúdo dele.

## 2. Mapeamento — conceitos pedidos → campo real

| Conceito pedido | Campo Notion real | Como mapeia |
|---|---|---|
| `Test_ID` (`NTN-2026-LELE-001`) | **Não existe campo dedicado.** | Vira o valor do título (`Agente`) ou parte do caminho em `Caso-teste`. Ver payload abaixo. |
| `Timestamp` | `Criado em` | Data/hora de criação da linha. `Atualizado em` fica para quando o status mudar. |
| `Bairro_Foco` (Canal das Taxas / Barra-Recreio) | **Não existe campo dedicado.** | Embutido no caminho de `Caso-teste`, seguindo a convenção já documentada no schema (`Casos_TESTE/{bairro}/{caso}`). |
| `Cenaria_Descricao` | **Não existe campo dedicado.** | A base não guarda descrição — só aponta para o arquivo local via `Caso-teste`. A descrição completa fica só em `cenario_teste_notion_001.md`. |
| `Responsavel_Alocado` | `Gestor` | Valor: `Lelé` |
| `Status` | `Status` | Valor: `pendente` (uma das 4 opções fixas do select — não aceita texto livre) |
| Flag de restrição Sandbox (proibir subagente) | **Não existe campo dedicado — nenhum booleano/checkbox no schema.** | Não pode ser "forçada no payload" porque a base não tem onde guardar isso estruturalmente. A regra vive e é aplicada a partir da Seção 4 de `cenario_teste_notion_001.md`; quem audita o exame (Wallenberg) precisa ler o arquivo, não confiar num campo Notion inexistente. |

## 3. Payload proposto (valores reais, schema real)

```
Agente:        NTN-2026-LELE-001 — Compatibilização Canal das Taxas
Gestor:        Lelé
Exame:         Formação → Shadow
Status:        pendente
Caso-teste:    01_CEO/Gestores/Lelé (Fechamento)/cenario_teste_notion_001.md
Criado em:     2026-09-16
Atualizado em: (vazio até a próxima mudança de status)
Resultado:     (vazio — só preenchido após o exame, com a evidência: laudo emitido / fluxo cessado / subagente NÃO despachado)
```

## 4. Checagem de consistência

- ✅ Todos os 6 campos usados (`Agente`, `Gestor`, `Exame`, `Status`, `Caso-teste`, `Criado em`) existem de fato no schema consultado.
- ✅ Valor de `Status` (`pendente`) é uma das 4 opções válidas do select — não é texto livre inventado.
- ⚠️ 3 dos 6 conceitos pedidos (`Test_ID` isolado, `Bairro_Foco`, `Cenaria_Descricao`) **não têm campo dedicado** — resolvidos por convenção de conteúdo dentro dos campos existentes, não por campo novo (criar propriedade nova na base é decisão de schema, fora do escopo deste manifesto).
- ⚠️ A flag de restrição Sandbox **não é aplicável como dado estruturado** nesta base — é regra de processo, aplicada por quem audita o exame, documentada no arquivo local.
- **Este manifesto não escreveu nada na Notion real** — é só o mapeamento, pronto para uma chamada de escrita futura (`notion-create-pages`), que não foi executada nesta rodada.
