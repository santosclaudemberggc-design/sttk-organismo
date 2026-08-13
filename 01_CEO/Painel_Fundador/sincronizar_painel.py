#!/usr/bin/env python3
"""
Sincronizar Painel do Fundador STTK
Copia o painel atualizado do repositório para a pasta local (Windows)
"""

import shutil
import os
from datetime import datetime
from pathlib import Path

# Caminhos
REPO_PAINEL = "/home/user/sttk-organismo/01_CEO/Painel_Fundador/painel_fundador_sttk.html"
LOCAL_PASTA = r"D:\000_ESTRUTURA DEPARTAMENTO DE PROJETO\01_CEO\Painel_Fundador"
LOCAL_PAINEL = os.path.join(LOCAL_PASTA, "painel_fundador_sttk.html")

# Backup anterior (opcional)
LOCAL_PAINEL_BACKUP = os.path.join(LOCAL_PASTA, f"painel_fundador_sttk_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")

def sincronizar():
    """Sincroniza o painel do repositório para a pasta local"""

    print(f"🔄 Sincronizando Painel do Fundador...")
    print(f"   Origem: {REPO_PAINEL}")
    print(f"   Destino: {LOCAL_PAINEL}")

    # Verifica se arquivo origem existe
    if not os.path.exists(REPO_PAINEL):
        print(f"❌ Erro: Arquivo de origem não encontrado: {REPO_PAINEL}")
        return False

    # Verifica/cria pasta destino
    if not os.path.exists(LOCAL_PASTA):
        print(f"📁 Criando pasta: {LOCAL_PASTA}")
        os.makedirs(LOCAL_PASTA, exist_ok=True)

    # Faz backup do arquivo anterior (se existir)
    if os.path.exists(LOCAL_PAINEL):
        print(f"💾 Fazendo backup: {LOCAL_PAINEL_BACKUP}")
        shutil.copy2(LOCAL_PAINEL, LOCAL_PAINEL_BACKUP)

    # Copia arquivo
    try:
        shutil.copy2(REPO_PAINEL, LOCAL_PAINEL)
        tamanho = os.path.getsize(LOCAL_PAINEL) / 1024  # KB
        print(f"✅ Painel sincronizado com sucesso ({tamanho:.1f} KB)")
        print(f"   Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        return True
    except Exception as e:
        print(f"❌ Erro ao copiar: {e}")
        return False

if __name__ == "__main__":
    sucesso = sincronizar()
    exit(0 if sucesso else 1)
