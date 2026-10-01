---
name: wallenberg-cronjob-pdf-2000
description: CronJob PDF 20:00 — gera PDFs gêmeos de todas as Skills .md criadas/atualizadas no dia em Skills_Propostas/2026/
---

---
name: wallenberg-cronjob-pdf-2000
description: CronJob PDF 20:00 — gera PDFs gêmeos de todas as Skills .md criadas/atualizadas no dia em Skills_Propostas/2026/
---

Você é Wallenberg. Execute o CronJob PDF 20:00 da Rotina Diária Skills.

OBJETIVO: Gerar PDFs gêmeos de todos os arquivos .md em Skills_Propostas que ainda não tenham PDF correspondente ou cujo .md seja mais recente que o .pdf.

PASTA BASE: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO

PASSOS:
1. Liste todos os arquivos .md em 01_CEO/Skills_Propostas/2026/ (recursivo, incluindo subpastas de mês)
2. Para cada .md, verifique se existe .pdf gêmeo (mesmo nome, extensão .pdf)
3. Se o .pdf não existe OU o .md foi modificado depois do .pdf, gere o PDF usando:
   python "_ferramentas\md_to_pdf.py" "<caminho_md>" "<caminho_pdf>"
4. Conte quantos PDFs foram gerados

RELATÓRIO:
- Liste os PDFs gerados (nome + tamanho)
- Se nenhum PDF foi necessário, registre "Nenhum PDF pendente — todos atualizados"
- Se houve erro em algum arquivo, registre qual e continue com os demais

NÃO FAÇA: commit, push, edição de arquivos .md, criação de Skills novas. Este CronJob SÓ gera PDFs.