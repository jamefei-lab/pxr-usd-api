@echo off
setlocal
cd /d "C:\Users\jame\OneDrive - SkyVault\Documents\New project\offline_pxr_docs"
echo Serving offline pxr docs at http://127.0.0.1:8000/pxr.html
start "" "http://127.0.0.1:8000/pxr.html"
python -m http.server 8000
