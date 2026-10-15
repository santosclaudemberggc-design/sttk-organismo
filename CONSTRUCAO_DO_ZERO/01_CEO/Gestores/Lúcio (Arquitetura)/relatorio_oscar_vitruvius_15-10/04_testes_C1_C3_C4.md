# Testes C1, C3, C4 — só leitura (Oscar, 15/10/2026)

Ordem: Lúcio, a mando de Wallenberg, com autorização de Claudemberg. Só ferramentas de leitura.

## Passo (b) — documento aberto

| Chamada | Saída colada |
|---|---|
| `vitruvius_get_revit_status` | `Error: Plugin não está conectado` |
| `vitruvius_get_document_info` | `Error: Plugin não está conectado` |

Documento aberto: **sem prova** (plugin desconectado). isModified no início: **sem prova**. isModified no fim: **sem prova** (nenhuma chamada posterior; não repeti a tentativa).

Pela regra (b), parei aqui. Não abri arquivo, não tentei reconectar, não chamei nenhuma outra ferramenta Vitruvius.

## Resultado por item

| Item | Classificação | Motivo |
|---|---|---|
| C1 cota vermelha | indeterminado | Teste não executado; sem prova. Plugin desconectado. |
| C3 pé-direito/alturas | indeterminado | Teste não executado; sem prova. O memorial do EP v2 não foi lido, porque sem a leitura do modelo não há o que comparar. |
| C4 Cobertura 6,30→6,20 | indeterminado | Teste não executado; sem prova. |

## Para refazer

1. Alguém com acesso ao Revit abre `EP_Montenegro_003_v2_r1.rvt` e confirma que o plugin está conectado. Eu não abro arquivo.
2. Repetir esta ordem do passo (b) em diante.

## Pedidos de ferramenta

Nenhum P31 criado. Estado do plugin no fim de 14/10 (meu estado §1): "O plugin ficou desconectado e o v2 não está aberto no Revit". Continua igual em 15/10.
