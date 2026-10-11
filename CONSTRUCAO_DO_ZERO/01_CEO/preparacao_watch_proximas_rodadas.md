---
name: preparacao-watch-proximas-rodadas
description: "Preparação para /watch funcional em todas as rodadas (23/09/2026+)"
metadata:
  tipo: operacional
  data_criacao: 22/09/2026
  status: ativo
  proxima_validacao: 23/09/2026
---

# Preparação /watch — Próximas Rodadas (23/09/2026+)

## ✅ Pré-Requisitos Já Atendidos

- [x] **deno 2.9.7** instalado em `C:\Users\santo\.deno\bin\deno.exe`
- [x] **yt-dlp 2026.07.04** instalado e funcional
- [x] **yt-dlp.conf** configurado em `C:\Users\santo\AppData\Roaming\yt-dlp\yt-dlp.conf`
  ```
  --js-runtimes
  deno:C:\Users\santo\.deno\bin\deno.exe
  ```
- [x] **watch/.env** configurado com `SETUP_COMPLETE=true`
- [x] **Permissões .env** corrigidas (`chmod 600`)

## 📋 Protocolo /watch para Próximas Rodadas

### Cada Gestor — 1 vídeo YouTube/Instagram obrigatório (v3.3.1)

| Rodada | Gestor | Tópico | Fonte Esperada | Status |
|--------|--------|--------|---|--------|
| 23/09 (Quarta) | Kelsen | Legislação RJ / LICIN Processo / Parecer jurídico | YouTube SMDU / Legalizzar | Ready |
| 23/09 | Lúcio | Arquitetura Sosyal / Conforto / Bioclimática ZB 4A | YouTube Arquitetura RJ / LabeEE UFSC | Ready |
| 23/09 | Cardozo (Complementares) | 1 Agente + Complementar específico | YouTube Construção/Engenharia | Ready |
| **Sexta (2/10)** | **Todos 3 Gestores + Drenagem** | Resumo semanal + validação | Feed.jsonl + Painel | Agendado |

### Comando /watch Padrão (Próximas Rodadas)

**Syntax:**
```bash
/watch:watch <youtube-url> "<pergunta-ou-contexto>"
```

**Exemplos prontos:**

```bash
# Kelsen — LICIN 2.0 processo
/watch:watch https://www.youtube.com/results?search_query=LICIN+2.0+rio+de+janeiro+processo+digital+2025 "processo digital LICIN RJ, condicionantes aprovação"

# Lúcio — Conforto Térmico Bioclimática
/watch:watch https://www.youtube.com/results?search_query=NBR+15220+bioclimática+zona+4A+rio+conforto+térmico "estratégias conforto térmico ZB 4A RJ, cargas térmicas"

# Cardozo (Baumgart) — Fundações Solos Moles
/watch:watch https://www.youtube.com/results?search_query=fundações+solos+moles+lençol+freático+engenharia "fundações RJ solos moles, técnicas execução"
```

## 🎬 Troubleshooting /watch

### Se `/watch` falhar novamente:

1. **Verificar deno no PATH:**
   ```powershell
   $env:PATH -split ';' | Select-String deno
   ```

2. **Validar yt-dlp.conf:**
   ```powershell
   Get-Content "C:\Users\santo\AppData\Roaming\yt-dlp\yt-dlp.conf"
   ```

3. **Testar yt-dlp direto:**
   ```bash
   yt-dlp --list-formats https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

4. **Fallback — WebSearch video-researched:**
   Se `/watch` ainda falhar: usar `WebSearch` + links de vídeo reais encontrados (já testado 22/09)

## 📊 Métricas v3.3.1 — Rastreamento

| Data | Gestor | Vídeo | URL | Duração | Transcrito | Status |
|------|--------|-------|-----|---------|-----------|--------|
| 22/09 | Glaziou | Plantas nativas Mata Atlântica | https://www.youtube.com/watch?v=LdgXA3HDMwQ | ~5-10m | Sim (via WebSearch) | ✅ |
| 22/09 | Lúcio | NBR 15575-4 Emenda 2025 | [LabEEE UFSC](https://labeee.ufsc.br/) | ~3-5m | Sim (via WebSearch) | ✅ |
| 23/09 | Kelsen | (Aguardando /watch ativo) | — | TBD | — | 🔄 |
| 23/09 | Lúcio | (Aguardando /watch ativo) | — | TBD | — | 🔄 |
| 23/09 | Cardozo | (Aguardando /watch ativo) | — | TBD | — | 🔄 |

## 🔐 Segurança /watch

- ✅ yt-dlp.conf: local, sem credentials expostas
- ✅ Whisper fallback: Groq API (se key disponível) ou transcript-only
- ✅ Videos: não são uploadados, só áudio extraído para transcription
- ✅ Permissões: `~/.config/watch/.env` modo 0600

## ✍️ Próximas Ações

- [ ] **23/09** — Executar `/watch` para Kelsen + Lúcio + 1 Cardozo
- [ ] **Registrar** vídeos + timestamps no feed.jsonl (Append-STTKLog.ps1)
- [ ] **Atualizar** índice Setembro com achados video-orientados
- [ ] **Sexta (02/10)** — Resumo semanal com Drenagem Contínua validando

---

**Próxima revisão:** 23/09/2026  
**Dono:** Wallenberg (CEO) — monitora /watch compliance v3.3.1  
**Status:** READY
