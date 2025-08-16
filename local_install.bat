@echo off

echo Creating virtual environment...
python -m venv .venv
echo.

echo =================================================
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
  pause
)

echo =================================================
echo Installing required packages...
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo.

pause
