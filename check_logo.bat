@echo off
echo ================================
echo FoodLens Logo Setup Checker
echo ================================
echo.

REM Check if assets folder exists
if exist "assets" (
    echo [OK] assets folder exists
) else (
    echo [!] assets folder missing - Run create_assets.bat
    goto :end
)

REM Check if logo folder exists
if exist "assets\logo" (
    echo [OK] assets\logo folder exists
) else (
    echo [!] assets\logo folder missing - Run create_assets.bat
    goto :end
)

REM Check if logo.png exists
if exist "assets\logo\logo.png" (
    echo [OK] logo.png found!
    echo.
    echo Your logo is ready! Next steps:
    echo 1. flutter pub get
    echo 2. flutter pub run flutter_launcher_icons
    echo 3. flutter run
) else (
    echo [!] logo.png not found
    echo.
    echo Please add your logo file to: assets\logo\logo.png
    echo.
    echo See LOGO_DESIGN_GUIDE.md for how to create the logo
)

:end
echo.
echo ================================
pause
