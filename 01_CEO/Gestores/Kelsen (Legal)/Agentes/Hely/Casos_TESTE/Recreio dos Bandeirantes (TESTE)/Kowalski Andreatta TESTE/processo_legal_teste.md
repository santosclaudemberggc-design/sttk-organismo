---
status: TESTE — não é cliente real
caso: 1
data_teste: 2026-07-13
gestor: Kelsen
executor: (caso rodado antes da divisão Kelsen/Hely — Kelsen executou diretamente)
---

# ⚠️ CENÁRIO DE TESTE — NENHUM DADO AQUI É REAL

Todo conteúdo deste arquivo — requerente, imóvel, matrícula, CPF, respostas da prefeitura — é fictício, gerado pelo Pesquisador de Testes (`D:\010_PESQUISADOR DE TESTES`) para validar o Gestor Legal (Kelsen). **Nunca copiar para `000_CLIENTES` real, nem tratar como caso verdadeiro.**

Cenário-fonte: `D:\010_PESQUISADOR DE TESTES\Cenarios de Teste\Kelsen (Legal)\2026-07-13_Projeto-Legal-TESTE-Recreio.md`

## Requerente e imóvel (fictícios)
- **Requerente**: Fabiana Kowalski Andreatta (casada, comunhão parcial de bens; cônjuge Marcos Andreatta)
- **Imóvel**: Rua Claude Monet, nº 142 (fictício), Recreio dos Bandeirantes, RJ — CEP 22790-663 (rua/CEP reais, número/lote/matrícula fictícios)
- **Matrícula RGI**: 000.000-TESTE | **Área do terreno**: 450,00 m² (15,00 x 30,00 m)
- **Situação**: terreno vago (demolição já concluída)
- **Natureza da obra**: CONSTRUÇÃO NOVA — residencial multifamiliar (condomínio), térreo + 3 pav. tipo + cobertura, 8 unidades

## Projeto arquitetônico de origem
Autor: Estúdio Vetor Cárdeas Arquitetura (parceiro externo) — Arqta. Renata Souza Cárdeas, CAU A000000-0-TESTE.

## Legislação aplicável — achado do teste (não confiar em fonte secundária)
Pesquisa inicial (fonte secundária) indicou Decreto Rio nº 3.046/1981 (ZE-5). **Confirmação com fonte oficial** (`mapas.rio.rj.gov.br`, consultada por Claudemberg) trouxe o valor real: zona **ZRM3 D da AP 4**, base legal **Lei Complementar 270/2024** — CA máximo 1,0 (básico 0,8), Taxa de Ocupação máxima 50%, afastamento frontal mínimo 5 m, gabarito 4pav/14m (não afastado) ou 6pav/20m (afastado das divisas).

**Parâmetros propostos pelo Estúdio Vetor Cárdeas x limite real confirmado:**

| Parâmetro | Proposto | Limite real (LC 270/2024) | Situação |
|---|---|---|---|
| CA | 2,6 | 1,0 (básico 0,8) | **Não conforme** |
| Taxa de ocupação | 55% | 50% | **Não conforme** |
| Gabarito | 14,50 m | 14 m (não afastado) / 20 m (afastado) | Borderline — só cabe se afastado das divisas |
| Recuo frontal | 4,00 m | 5 m mínimo | **Não conforme** |

**Pendência de mérito real, não resolvida pelo teste:** estes parâmetros precisariam ser revistos com Arquitetura antes de qualquer protocolo real — o teste não simula essa correção, só confirma que o Kelsen/Hely saberiam identificar o risco.

## Anexo I — DULI (rascunho de teste)
- Tipo de licença: Construção nova, residencial multifamiliar
- Requerente: Fabiana Kowalski Andreatta (CPF/RG fictícios)
- Imóvel: Rua Claude Monet, 142, Recreio dos Bandeirantes — Matrícula 000.000-TESTE
- PRPA: Arqta. Renata Souza Cárdeas (Estúdio Vetor Cárdeas) — parceiro externo, autora do projeto arquitetônico
- Documentos anexados: Ficha de Levantamento, Estudo Preliminar v2, Anteprojeto (AP-TESTE-2026-001 a 006), Certidão de matrícula RGI, Certidão negativa de IPTU, cópias RG/CPF

## Anexo II — Declaração de Responsabilidade
Pendente de ART/RRT do Estúdio Vetor Cárdeas (não emitida no pacote de entrada) — **bloqueio antes do protocolo real**, identificado no teste.

## Anexo III — Quadro Explicativo de Áreas (construção nova)
- **Versão 1 (protocolo simulado)**: 1.240,00 m²
- **Resposta simulada da SMDU** (processo LICIN-TESTE-2026-0000123): PEDIDO DE AJUSTE — divergência entre Anexo III (1.240,00 m²) e soma das plantas de pavimento (1.198,40 m²)
- **Versão 2 (revisada, aprovada na simulação)**: 1.198,40 m²

## Emissão (simulada, 2ª submissão aprovada)
- Minuta da Licença — construção nova, residencial multifamiliar, 8 unidades
- Guia de arrecadação
- Anexo III revisado (1.198,40 m²)
- Termo de Responsabilidade

## Fluxo pós-aprovação
Não passa por Compatibilização — segue direto pra fila de espera do **Gate 16 (Liberação de Obra)**, com Habite-se (unidade nova) como fechamento futuro.

## Pendências e sinalizações (registradas no teste)
1. **PRPA**: assinatura é de direito da Arqta. Renata Souza Cárdeas (parceiro externo, autora do projeto) — não de Claudemberg.
2. **ART/RRT do Estúdio Vetor Cárdeas** ainda não emitida — bloqueio documental antes do protocolo real.
3. **Parâmetros urbanísticos** (CA, TO, recuo frontal) do Anteprojeto — não conformes com a legislação real confirmada (LC 270/2024) — precisariam de revisão com Arquitetura antes de um caso real equivalente.
4. **Lacuna de conhecimento**: base do Kelsen não tinha, antes deste teste, granularidade de índices urbanísticos por bairro/subzona — virou proposta de Skill (`01_CEO\Gestores\Kelsen (Legal)\skill_base_legislativa_bairro_proposta.html`).
