@ECHO OFF
PowerShell.exe -windowstyle hidden -Command "& & env/Scripts/Activate.ps1"
PowerShell.exe -windowstyle hidden -Command "& env/Scripts/python.exe ler_horario.py"
PowerShell.exe -windowstyle hidden -Command "& env/Scripts/python.exe form.py"