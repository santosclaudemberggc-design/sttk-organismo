@echo off
REM Sincronizar Painel do Fundador STTK (Windows Batch)
REM Copia o painel do repositório Git para a pasta local

setlocal enabledelayedexpansion

REM Caminhos
set REPO_PASTA=D:\sttk-organismo
set REPO_PAINEL=%REPO_PASTA%\01_CEO\Painel_Fundador\painel_fundador_sttk.html
set LOCAL_PASTA=D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador
set LOCAL_PAINEL=%LOCAL_PASTA%\painel_fundador_sttk.html

REM Data/hora para backup
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c%%a%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
set TIMESTAMP=%mydate%_%mytime%

REM Header
echo.
echo ============================================
echo Sincronizar Painel do Fundador STTK
echo %date% %time%
echo ============================================
echo.

REM Verifica arquivo origem
if not exist "%REPO_PAINEL%" (
  echo [ERRO] Arquivo de origem nao encontrado:
  echo        %REPO_PAINEL%
  echo.
  echo Certifique-se que:
  echo  - O repositorio esta em: %REPO_PASTA%
  echo  - O arquivo existe naquele caminho
  pause
  exit /b 1
)

REM Cria pasta destino se nao existir
if not exist "%LOCAL_PASTA%" (
  echo [INFO] Criando pasta: %LOCAL_PASTA%
  mkdir "%LOCAL_PASTA%"
)

REM Faz backup do arquivo anterior
if exist "%LOCAL_PAINEL%" (
  echo [INFO] Fazendo backup do arquivo anterior...
  copy "%LOCAL_PAINEL%" "%LOCAL_PASTA%\painel_fundador_sttk_backup_%TIMESTAMP%.html" >nul
  echo       Backup criado: painel_fundador_sttk_backup_%TIMESTAMP%.html
)

REM Copia arquivo
echo [INFO] Copiando arquivo atualizado...
copy "%REPO_PAINEL%" "%LOCAL_PAINEL%" >nul

if exist "%LOCAL_PAINEL%" (
  echo.
  echo [OK] Painel sincronizado com sucesso!
  echo      Destino: %LOCAL_PAINEL%
  echo.
  echo Proximas etapas:
  echo  1. Abra o arquivo no navegador: %LOCAL_PAINEL%
  echo  2. Use Ctrl+Shift+R para limpar cache
  echo  3. Painel atualizado com Semana 2 validada (45-67%%)
  echo.
) else (
  echo.
  echo [ERRO] Falha ao copiar arquivo
  exit /b 1
)

REM Pausa para ver mensagem
timeout /t 5 /nobreak

endlocal
exit /b 0
