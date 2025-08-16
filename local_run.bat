@echo off

echo =================================================
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
  pause
)

echo =================================================
echo http://localhost:8000
uvicorn app:app --reload
