@echo off
title Smart Exam Generator
echo Starting Smart Exam Generator...
echo.

:: Change to the directory where the batch file is located
cd /d "%~dp0"

:: Kill any existing Python processes
taskkill /F /IM python.exe /T >nul 2>&1

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH!
    echo Please install Python 3.x from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

:: Check if required packages are installed
echo Checking required packages...
python -c "import PyQt6" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyQt6...
    pip install PyQt6
)

python -c "import nltk" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing NLTK...
    pip install nltk
)

:: Download required NLTK data
echo Downloading required NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"

:: Wait a moment to ensure all processes are finished
timeout /t 2 >nul

:: Create sample content
echo Creating sample content...
python create_sample_content.py

:: Wait for sample content creation to complete
timeout /t 2 >nul

:: Run the application
echo Starting application...
python exam_generator_ui.py

if %errorlevel% neq 0 (
    echo.
    echo An error occurred while running the application.
    echo Please check if all files are in the correct location.
    pause
    exit /b 1
)

exit /b 0 