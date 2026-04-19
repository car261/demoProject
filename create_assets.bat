@echo off
echo Creating assets directory structure...

if not exist "assets" mkdir "assets"
if not exist "assets\logo" mkdir "assets\logo"

echo.
echo ✓ Assets folders created!
echo.
echo Next steps:
echo 1. Add your logo.png to assets\logo\
echo 2. Run: flutter pub get
echo 3. Run: flutter pub run flutter_launcher_icons
echo.
pause
