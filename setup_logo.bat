@echo off
echo Creating assets\logo directory...
mkdir assets\logo 2>nul

echo.
echo Please copy your logo image to: %CD%\assets\logo\logo.png
echo.
echo Example: copy "C:\path\to\your\image.png" "assets\logo\logo.png"
echo.
pause