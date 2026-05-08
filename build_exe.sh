#!/bin/bash
# ============================================================
#  Load Extraction Tool — Linux/Mac EXE Build Script
# ============================================================

set -e

echo ""
echo "============================================================"
echo "  Load Extraction Tool - Build"
echo "============================================================"
echo ""

echo "[1/3] Gerekli kutuphaneler kuruluyor..."
pip install -r requirements.txt

echo ""
echo "[2/3] Eski build dosyalari temizleniyor..."
rm -rf build dist

echo ""
echo "[3/3] Executable olusturuluyor (bu birkaç dakika surebilir)..."
pyinstaller LoadExtractionTool.spec

echo ""
echo "============================================================"
echo "  BASARILI! Uygulama hazir:"
echo "  dist/LoadExtractionTool/LoadExtractionTool"
echo "============================================================"
echo ""
