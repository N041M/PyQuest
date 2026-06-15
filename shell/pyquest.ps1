# PyQuest shortcuts for PowerShell (Windows).
#
# Lets you type `check`, `hint`, `solution`, and so on instead of the long
# `python start.py check`. PowerShell is the native shell on Windows 10/11.
#
# Use it for THIS terminal only:
#     . .\shell\pyquest.ps1
# Install it for every new terminal (adds one line to your PowerShell profile):
#     . .\shell\pyquest.ps1 ; Install-PyQuest
# Remove it again:
#     uninstall
#
# If PowerShell refuses to run this file ("running scripts is disabled"), allow
# local scripts once with:
#     Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# --- locate the PyQuest root, so the folder can live anywhere ----------------
$PyQuestRoot = Split-Path -Parent $PSScriptRoot
$PyQuestPlay = Join-Path $PyQuestRoot 'start.py'
$PyQuestMark = '# PyQuest shell shortcuts'

# --- find a Python to run (the py launcher, then python, then python3) --------
function Find-PyQuestPython {
    if (Get-Command py      -ErrorAction SilentlyContinue) { return , @('py', '-3') }
    if (Get-Command python  -ErrorAction SilentlyContinue) { return , @('python') }
    if (Get-Command python3 -ErrorAction SilentlyContinue) { return , @('python3') }
    Write-Warning 'PyQuest: no Python found on PATH. Install Python 3 from python.org.'
    return , @('python')
}
$PyQuestPython = Find-PyQuestPython
$env:PYQUEST_SHELL = '1'   # tell start.py the short commands are in use

function _pyquest {
    $py  = $PyQuestPython
    $pre = if ($py.Count -gt 1) { $py[1..($py.Count - 1)] } else { @() }
    & $py[0] @pre $PyQuestPlay @args
}

# --- the shortcuts, usable from any directory --------------------------------
function pq        { _pyquest @args }
function pyquest   { _pyquest @args }
function begin     { _pyquest begin @args }
function menu      { _pyquest menu @args }
function back      { _pyquest menu @args }
function status    { _pyquest status @args }
function help      { _pyquest help @args }
function setup     { _pyquest setup @args }
function check     { _pyquest check @args }
function hint      { _pyquest hint @args }
function solution  { _pyquest solution @args }
function map       { _pyquest map @args }
function next      { _pyquest next @args }
function goto      { _pyquest goto @args }
function load      { _pyquest load @args }
function skip      { _pyquest skip @args }
function retry     { _pyquest retry @args }
function replay    { _pyquest replay @args }
function revert    { _pyquest revert @args }
function mode      { _pyquest mode @args }
function theme     { _pyquest theme @args }
function user      { _pyquest user @args }
function users     { _pyquest user @args }

# `start` is a built-in PowerShell alias (Start-Process), so it is left alone;
# use `pq` as the umbrella command (`pq`, `pq check`, `pq reset`, ...).

# `reset` wipes ALL PyQuest progress, so confirm before doing it.
function reset {
    $ans = Read-Host 'Wipe ALL PyQuest progress, saved code and workspaces? [y/N]'
    if ($ans -match '^[yY]') { _pyquest reset } else { 'Cancelled.' }
}

# --- install / uninstall in the PowerShell profile ---------------------------
function Install-PyQuest {
    $line = ". `"$PyQuestRoot\shell\pyquest.ps1`"  $PyQuestMark"
    if (-not (Test-Path $PROFILE)) {
        New-Item -ItemType File -Path $PROFILE -Force | Out-Null
    }
    if (Select-String -Path $PROFILE -SimpleMatch $PyQuestMark -Quiet) {
        "PyQuest shortcuts are already in your profile ($PROFILE)."
    } else {
        Add-Content -Path $PROFILE -Value $line
        "Added PyQuest shortcuts to $PROFILE. Open a new PowerShell to use them everywhere."
    }
}

function uninstall {
    if (Test-Path $PROFILE) {
        (Get-Content $PROFILE) |
            Where-Object { $_ -notmatch [regex]::Escape($PyQuestMark) } |
            Set-Content $PROFILE
    }
    'pq pyquest begin menu back status help setup check hint solution map next goto load skip retry replay revert mode theme user users reset uninstall'.Split(' ') |
        ForEach-Object { Remove-Item "Function:$_" -ErrorAction SilentlyContinue }
    'Removed the PyQuest shortcuts (from your profile and this terminal).'
}

Write-Host 'PyQuest shortcuts loaded. Try:  pq   (or check, hint, map, next, ...)'
