@echo off
chcp 65001 >nul
echo ============================================
echo        🤖 AUTONOMOUS BOT TEST
echo ============================================
echo.
echo 🧪 Testing autonomous bot locally...
echo.

cd /d "%~dp0"

python autonomous_bot.py

echo.
echo ============================================
echo           TEST COMPLETED
echo ============================================
echo.
pause