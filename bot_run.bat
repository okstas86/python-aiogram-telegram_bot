@echo off

call %~dp0Italian_pizza_bot\venv\Scripts\activate

cd %~dp0Italian_pizza_bot

set TOKEN=

python main.py
pause