@echo off

call %~dp0venv\Scripts\activate

python async_parser.py

pause