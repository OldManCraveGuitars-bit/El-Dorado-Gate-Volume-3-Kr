param(
    [Parameter(Mandatory=$true)][string]$Xdelta,
    [Parameter(Mandatory=$true)][string]$Patch,
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$taskEngine = (Resolve-Path -LiteralPath $Xdelta).Path
$taskPatch = (Resolve-Path -LiteralPath $Patch).Path
$taskManifest = Get-Content -LiteralPath (Join-Path $taskRepo 'hashes.json') -Raw | ConvertFrom-Json
$taskEngineHash = (Get-FileHash -LiteralPath $taskEngine -Algorithm SHA256).Hash.ToLowerInvariant()
$taskPatchHash = (Get-FileHash -LiteralPath $taskPatch -Algorithm SHA256).Hash.ToLowerInvariant()
if ($taskEngineHash -ne $taskManifest.xdelta.sha256) { throw 'Verified xdelta3 3.2.1 Windows x64 binary required' }
if ($taskPatchHash -ne $taskManifest.patch.sha256) { throw 'Patch payload SHA-256 does not match hashes.json' }
& $Python -m PyInstaller --noconfirm --clean --onefile --windowed `
    --name ('El-Dorado-Gate-Volume-3-Kr-' + $taskManifest.version + '-Patcher') `
    --distpath (Join-Path $taskRepo 'dist') `
    --workpath (Join-Path $taskRepo 'build') `
    --specpath (Join-Path $taskRepo 'build') `
    --version-file (Join-Path $PSScriptRoot 'version-info.txt') `
    --add-data ((Join-Path $taskRepo 'hashes.json') + ';.') `
    --add-data ($taskPatch + ';.') `
    --add-data ((Join-Path $taskRepo 'licenses') + ';licenses') `
    --add-binary ($taskEngine + ';.') `
    (Join-Path $PSScriptRoot 'patcher.py')
if ($LASTEXITCODE -ne 0) { throw 'PyInstaller build failed' }
Write-Output 'Built a standalone EXE with the verified patch payload, engine and licenses embedded.'
