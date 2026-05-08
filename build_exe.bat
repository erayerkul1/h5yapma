@echo off
REM ============================================================
REM  Load Extraction Tool — Windows EXE Build Script
REM  Gereksinim: Python 3.11+ ve pip kurulu olmalı
REM ============================================================

echo.
echo ============================================================
echo   Load Extraction Tool - EXE Build
echo ============================================================
echo.

REM Gerekli kütüphaneleri kur
echo [1/3] Gerekli kutuphaneler kuruluyor...
pip install -r requirements.txt
if errorlevel 1 (
    echo HATA: Kutuphaneler kurulamadi!
    pause
    exit /b 1
)

REM Eski build dosyalarını temizle
echo.
echo [2/3] Eski build dosyalari temizleniyor...
if exist "build" rmdir /s /q "build"
if exist "dist"  rmdir /s /q "dist"

REM PyInstaller ile exe oluştur
echo.
echo [3/3] EXE olusturuluyor (bu birkaç dakika surebilir)...
pyinstaller LoadExtractionTool.spec
if errorlevel 1 (
    echo HATA: EXE olusturulamadi!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   BASARILI! EXE dosyasi hazir:
echo   dist\LoadExtractionTool\LoadExtractionTool.exe
echo ============================================================
echo.
pause
