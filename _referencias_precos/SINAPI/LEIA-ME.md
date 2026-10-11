# SINAPI — planilhas oficiais da Caixa

Cada pasta guarda **um mês de referência**, com a data em que foi baixado: `AAAA-MM_baixado-AAAA-MM-DD/`.
A ferramenta `_ferramentas/sinapi_consulta.py` sempre lê a pasta mais recente.

## Como atualizar (todo mês, ou antes de fechar um orçamento)
1. A página oficial é caixa.gov.br/sinapi → Relatórios Mensais → "Relatórios a partir de 2025"
   (lista em `caixa.gov.br/site/Paginas/downloads.aspx#categoria_888`).
2. Baixe o `SINAPI-AAAA-MM-formato-xlsx.zip` mais recente. Se houver `_Retificacao`, use ela.
   O download direto por script cai num laço de redirecionamento; funciona com curl guardando cookie (`-c`/`-b`).
3. Crie a pasta nova com o mês e a data do download, e extraia o zip ali. **Não apague as pastas antigas**:
   um orçamento já entregue cita o mês que usou.
4. Teste: `python _ferramentas/sinapi_consulta.py 97631`. Em 09/2026, o RJ sem desoneração dava R$ 17,59.

## Onde ver os valores
O arquivo `SINAPI_Referência_AAAA_MM.xlsx` tem estas abas: CSD (composições sem desoneração), CCD (com desoneração),
ISD/ICD (insumos). Cada estado tem uma coluna de custo e uma de %AS. O %AS é a parte do custo que veio
de preço de São Paulo, por falta de preço no estado. Se o %AS for alto, diga isso no orçamento.

## Mês atual
- 09/2026, emitido pela Caixa em 09/10/2026, baixado em 11/10/2026.
