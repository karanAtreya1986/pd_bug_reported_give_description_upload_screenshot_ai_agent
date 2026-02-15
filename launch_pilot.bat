@echo off
setlocal
title Jira Ticket Pilot Launcher
:: Get current directory
set "dir=%~dp0"
cd /d "%dir%"

echo 🚀 Starting Jira Ticket Pilot Server...
start /b python server.py
echo 🌐 Opening UI in browser...
timeout /t 3 >nul
start http://localhost:5000
echo ✅ System is live!
pause
