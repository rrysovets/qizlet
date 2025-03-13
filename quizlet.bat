@echo off
cd /d "%~dp0qizlet"
start "" cmd /c "python manage.py runserver"
timeout /t 2 >nul
start http://127.0.0.1:8000