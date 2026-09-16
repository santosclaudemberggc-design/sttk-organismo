<#
.SYNOPSIS
    Acrescenta uma linha de evento estruturado (JSON compacto) a um arquivo .jsonl,
    seguro para escrita concorrente entre processos paralelos no Windows.

.DESCRIPTION
    Usa classes nativas do .NET ([System.IO.FileStream] + [System.IO.FileShare]::ReadWrite)
    em vez de Add-Content/Out-File, para blindar contra IO.IOException de file-lock quando
    mais de um processo tenta acrescentar ao mesmo log ao mesmo tempo. Cada linha gravada é
    um objeto JSON de uma só linha (JSON Lines), UTF-8 sem BOM.

.PARAMETER LogPath
    Caminho do arquivo .jsonl de destino (ex: 01_CEO/Painel_Fundador/feed.jsonl).

.PARAMETER D
    Data do evento, formato "DD/MM".

.PARAMETER Et
    Tipo do evento: decisao | promocao | agente | skill | sistema | correcao | marco | capacidade.

.PARAMETER T
    Título curto do evento.

.PARAMETER Who
    Quem executou/decidiu.

.PARAMETER P
    Frase descritiva do que aconteceu.

.PARAMETER Rec
    Opcional. Referência/âncora de recomendação (campo "rec" usado em parte do histórico).

.EXAMPLE
    .\Append-STTKLog.ps1 -LogPath "01_CEO\Painel_Fundador\feed.jsonl" `
        -D "16/09" -Et "sistema" -T "Exemplo" -Who "Wallenberg" -P "Descrição do evento."
#>
param(
    [Parameter(Mandatory = $true)][string]$LogPath,
    [Parameter(Mandatory = $true)][string]$D,
    [Parameter(Mandatory = $true)][string]$Et,
    [Parameter(Mandatory = $true)][string]$T,
    [Parameter(Mandatory = $true)][string]$Who,
    [Parameter(Mandatory = $true)][string]$P,
    [Parameter(Mandatory = $false)][string]$Rec
)

$ErrorActionPreference = 'Stop'

# Monta o objeto do evento preservando a ordem de campos do schema histórico (d, et, t, who, p[, rec])
$eventObject = [ordered]@{
    d   = $D
    et  = $Et
    t   = $T
    who = $Who
    p   = $P
}
if ($PSBoundParameters.ContainsKey('Rec') -and -not [string]::IsNullOrEmpty($Rec)) {
    $eventObject['rec'] = $Rec
}

$json = $eventObject | ConvertTo-Json -Compress -Depth 4
$line = $json + "`n"

# UTF-8 SEM assinatura (sem BOM) — o construtor com $false desliga a BOM
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$bytes = $utf8NoBom.GetBytes($line)

# Retry com FileShare.ReadWrite: tolera outro processo com o arquivo aberto ao mesmo tempo
# (leitura do Painel via fetch(), ou outro Append-STTKLog.ps1 rodando em paralelo).
$maxRetries = 8
$retryDelayMs = 150
$attempt = 0
$success = $false
$lastError = $null

while (-not $success -and $attempt -lt $maxRetries) {
    $attempt++
    $stream = $null
    try {
        $stream = New-Object System.IO.FileStream(
            $LogPath,
            [System.IO.FileMode]::Append,
            [System.IO.FileAccess]::Write,
            [System.IO.FileShare]::ReadWrite
        )
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Flush()
        $success = $true
    }
    catch [System.IO.IOException] {
        $lastError = $_
        Start-Sleep -Milliseconds $retryDelayMs
    }
    finally {
        if ($stream) { $stream.Dispose() }
    }
}

if (-not $success) {
    throw "Append-STTKLog: falha ao gravar em '$LogPath' apos $maxRetries tentativas. Ultimo erro: $lastError"
}

Write-Output "OK: evento gravado em $LogPath"
