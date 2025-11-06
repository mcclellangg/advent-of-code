# use PowerShell instead of sh:
set shell := ["powershell.exe", "-c"]

# Run black on all practice problems: venv must be activated!
format:
    black .\2015\*
    black .\tmpl\