@echo off
REM Rotina Local — Otimização de Tokens STTK (Windows Batch)
REM Executa validações de Items 4-6 e sincroniza painel

setlocal enabledelayedexpansion

REM Caminhos
set REPO_PASTA=D:\sttk-organismo
set SCRIPT_PYTHON=%REPO_PASTA%\01_CEO\Painel_Fundador\rotina_otimizacao_tokens.py
set PYTHON_EXE=python

REM Header
echo.
echo ============================================
echo Rotina Local - Otimizacao de Tokens STTK
echo Validacoes Items 4-6 + Sincronizacao Painel
echo %date% %time%
echo ============================================
echo.

REM Verifica se arquivo Python existe
if not exist "%SCRIPT_PYTHON%" (
  echo [ERRO] Script Python nao encontrado:
  echo        %SCRIPT_PYTHON%
  echo.
  echo Certifique-se que:
  echo  - O repositorio esta em: %REPO_PASTA%
  echo  - O arquivo rotina_otimizacao_tokens.py existe
  pause
  exit /b 1
)

REM Verifica se Python esta instalado
%PYTHON_EXE% --version >nul 2>&1
if errorlevel 1 (
  echo [ERRO] Python nao encontrado no PATH
  echo.
  echo Instale Python ou adicione-o ao PATH do Windows
  pause
  exit /b 1
)

REM Executa rotina
echo [INFO] Executando rotina de otimizacao...
echo.

%PYTHON_EXE% "%SCRIPT_PYTHON%"

REM Verifica resultado
if errorlevel 1 (
  echo.
  echo [ERRO] Rotina falhou. Verifique os logs acima.
  pause
  exit /b 1
) else (
  echo.
  echo [OK] Rotina completada com sucesso!
  echo.
  echo Proximas etapas:
  echo  1. Abra o painel: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
  echo  2. Use Ctrl+Shift+R para limpar cache do navegador
  echo  3. Verifique os registros em: %REPO_PASTA%\03_REGISTROS_DIARIOS
  echo.
)

REM Pausa para ver mensagem
timeout /t 5 /nobreak

endlocal
exit /b 0
