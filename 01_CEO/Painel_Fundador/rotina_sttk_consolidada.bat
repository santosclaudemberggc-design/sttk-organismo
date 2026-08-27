@echo off
REM Rotina STTK Consolidada (Windows Batch)
REM Orquestra Items 4-8 em uma única execução
REM Substitui todas as 5 rotinas cloud individuais

setlocal enabledelayedexpansion

REM Caminhos
set REPO_PASTA=D:\sttk-organismo
set SCRIPT_PYTHON=%REPO_PASTA%\01_CEO\Painel_Fundador\rotina_sttk_consolidada.py
set PYTHON_EXE=python

REM Header
echo.
echo ============================================
echo Rotina STTK Consolidada — Items 4-8
echo Local (sem nuvem)
echo %date% %time%
echo ============================================
echo.

REM Verifica arquivo Python
if not exist "%SCRIPT_PYTHON%" (
  echo [ERRO] Script Python nao encontrado:
  echo        %SCRIPT_PYTHON%
  echo.
  echo Certifique-se que:
  echo  - O repositorio esta em: %REPO_PASTA%
  echo  - O arquivo rotina_sttk_consolidada.py existe
  pause
  exit /b 1
)

REM Verifica Python instalado
%PYTHON_EXE% --version >nul 2>&1
if errorlevel 1 (
  echo [ERRO] Python nao encontrado no PATH
  echo.
  echo Instale Python 3.8+ ou adicione ao PATH do Windows
  pause
  exit /b 1
)

REM Executa rotina
echo [INFO] Executando rotina STTK consolidada...
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
  echo [OK] Rotina STTK consolidada completada!
  echo.
  echo Proximas etapas:
  echo  1. Abra o painel: D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador\painel_fundador_sttk.html
  echo  2. Use Ctrl+Shift+R para limpar cache
  echo  3. Verifique registros: %REPO_PASTA%\03_REGISTROS_DIARIOS
  echo.
)

REM Pausa para ver resultado
timeout /t 5 /nobreak

endlocal
exit /b 0
