# Render every (or selected) slide of a PPTX to PNG with the user's own PowerPoint (Windows).
# Usage:
#   powershell -ExecutionPolicy Bypass -File render_pptx.ps1 -Pptx deck.pptx -OutDir render-r1 [-Only "3,5,9"] [-Pdf deck.pdf] [-Width 1600]
# Opens the file read-only, never saves over it, quits PowerPoint only if this script started it.
param(
  [Parameter(Mandatory = $true)][string]$Pptx,
  [Parameter(Mandatory = $true)][string]$OutDir,
  [string]$Only = "",
  [string]$Pdf = "",
  [int]$Width = 1600
)
$ErrorActionPreference = 'Stop'
$Pptx = (Resolve-Path -LiteralPath $Pptx).Path
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$OutDir = (Resolve-Path -LiteralPath $OutDir).Path
$height = [int]($Width * 9 / 16)
$app = New-Object -ComObject PowerPoint.Application
$before = $app.Presentations.Count
$p = $app.Presentations.Open($Pptx, $true, $false, $false)   # ReadOnly, Untitled=false, WithWindow=false
try {
  $sel = @()
  if ($Only) { $sel = $Only.Split(',') | ForEach-Object { [int]$_.Trim() } }
  $count = 0
  for ($i = 1; $i -le $p.Slides.Count; $i++) {
    if ($sel.Count -gt 0 -and -not ($sel -contains $i)) { continue }
    $f = Join-Path $OutDir ("slide-{0:D2}.png" -f $i)
    $p.Slides.Item($i).Export($f, 'PNG', $Width, $height)
    $count++
  }
  if ($Pdf) { $p.SaveCopyAs([IO.Path]::GetFullPath($Pdf), 32) }   # 32 = ppSaveAsPDF
  "rendered=$count slides=$($p.Slides.Count) out=$OutDir"
} finally {
  $p.Close()
  if ($app.Presentations.Count -eq 0 -and $before -eq 0) { $app.Quit() }
}
