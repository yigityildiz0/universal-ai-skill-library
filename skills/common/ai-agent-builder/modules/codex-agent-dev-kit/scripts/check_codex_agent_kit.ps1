param(
    [string]$SkillPath,
    [string]$PluginPath,
    [string]$MarketplacePath
)

$ErrorActionPreference = "Stop"
$failed = $false

function Test-RequiredPath {
    param(
        [string]$Path,
        [string]$Label
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Output "MISSING: $Label -> $Path"
        $script:failed = $true
        return
    }

    Write-Output "OK: $Label -> $Path"
}

if ($SkillPath) {
    Test-RequiredPath (Join-Path $SkillPath "SKILL.md") "skill manifest"
    Test-RequiredPath (Join-Path $SkillPath "agents\openai.yaml") "skill UI metadata"
}

if ($PluginPath) {
    Test-RequiredPath (Join-Path $PluginPath ".codex-plugin\plugin.json") "plugin manifest"

    $manifestPath = Join-Path $PluginPath ".codex-plugin\plugin.json"
    if (Test-Path -LiteralPath $manifestPath) {
        $manifest = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
        $folderName = Split-Path -Leaf $PluginPath
        if ($manifest.name -ne $folderName) {
            Write-Output "MISMATCH: plugin manifest name '$($manifest.name)' != folder '$folderName'"
            $failed = $true
        } else {
            Write-Output "OK: plugin name matches folder"
        }
    }
}

if ($MarketplacePath) {
    Test-RequiredPath $MarketplacePath "marketplace"
    if (Test-Path -LiteralPath $MarketplacePath) {
        $null = Get-Content -Raw -LiteralPath $MarketplacePath | ConvertFrom-Json
        Write-Output "OK: marketplace JSON parses"
    }
}

if ($failed) {
    exit 1
}

exit 0
