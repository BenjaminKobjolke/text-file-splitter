@echo off
echo Running application...
call venv\Scripts\activate.bat
call python main.py %*
pause
