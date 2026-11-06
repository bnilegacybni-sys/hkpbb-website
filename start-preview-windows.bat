@echo off
cd /d "%~dp0"
start "" http://localhost:8080
python _preview_server.py 2>nul || py _preview_server.py
pause
