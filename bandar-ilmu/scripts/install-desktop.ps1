# Install Bandar Ilmu as a desktop app (Edge app window, works offline).
# Copies v1/ to %LOCALAPPDATA%\BandarIlmu and puts a "Bandar Ilmu" shortcut on the Desktop.
# Re-run after an update; progress is kept (it lives in Edge's storage for that file path).
#   powershell -ExecutionPolicy Bypass -File bandar-ilmu\scripts\install-desktop.ps1
$ErrorActionPreference = 'Stop'
$src  = Join-Path $PSScriptRoot '..\v1' | Resolve-Path
$dest = Join-Path $env:LOCALAPPDATA 'BandarIlmu'
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse -Force (Join-Path $src '*') $dest

$edge = @("${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
          "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw 'Microsoft Edge not found.' }

$url = 'file:///' + ((Join-Path $dest 'index.html') -replace '\\', '/')
$lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) 'Bandar Ilmu.lnk'
$sh = (New-Object -ComObject WScript.Shell).CreateShortcut($lnk)
$sh.TargetPath = $edge
$sh.Arguments = "--app=`"$url`" --start-maximized"
$sh.IconLocation = "$edge,0"
$sh.Description = 'Bandar Ilmu - bina bandar dengan matematik'
$sh.Save()
"installed: $dest"
"shortcut:  $lnk"
