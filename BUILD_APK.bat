@echo off
echo ========================================
echo   FoodLens - Build Release APK
echo ========================================
echo.

echo [1/4] Cleaning build cache...
call flutter clean
echo.

echo [2/4] Getting dependencies...
call flutter pub get
echo.

echo [3/4] Building release APK...
echo This may take 3-5 minutes...
call flutter build apk --release
echo.

if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo   BUILD SUCCESS! 
    echo ========================================
    echo.
    echo APK Location:
    echo build\app\outputs\flutter-apk\app-release.apk
    echo.
    echo Transfer this file to your phone and install!
    echo.
) else (
    echo ========================================
    echo   BUILD FAILED
    echo ========================================
    echo Check errors above
)

pause
