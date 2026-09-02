@echo off
REM Medicao real de tokens do organismo STTK.
REM Le os transcripts de sessao do Claude Code e gera token_metrics.json + RELATORIO_TOKENS.md
python "%~dp0medir_tokens.py" %*
