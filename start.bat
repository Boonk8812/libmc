@echo off
cls
echo Starting libmc...
PATH_TO_PYTHON="C:\Program Files\Python39\python.exe" # Update this with your own path
"%PATH_TO_PYTHON%" libmc.py %*
pause
