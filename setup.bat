@echo off
chcp 65001 >nul
echo ============================================
echo   🤖 AUTONOMOUS BOT SETUP & DEPLOYMENT
echo ============================================
echo.
echo 🚀 Setting up autonomous daily logs bot...
echo.

cd /d "%~dp0"

echo 📋 Current directory: %cd%
echo.

echo 🧪 Testing bot locally...
python autonomous_bot.py

echo.
echo 🔧 Adding remote repository...
git remote add origin git@github.com:duyentinh188/auto-daily-logs.git

echo.
echo 📦 Adding all files...
git add .

echo.
echo 💾 Creating initial commit...
git commit -m "🤖 Initial autonomous bot setup - 100%% independent"

echo.
echo 🚀 Pushing to GitHub...
git push -u origin main

echo.
echo ============================================
echo         🎉 DEPLOYMENT COMPLETED
echo ============================================
echo.
echo ✅ Autonomous bot deployed successfully!
echo 🤖 Bot will now run automatically every day at 00:00 UTC
echo 📊 Check GitHub Actions for monitoring
echo 🔗 Repository: https://github.com/duyentinh188/auto-daily-logs
echo.
echo 🎯 Bot features:
echo   - 100%% autonomous operation
echo   - No user intervention required
echo   - GitHub Actions powered
echo   - Daily UTC scheduling
echo   - Enhanced logging and monitoring
echo.
pause