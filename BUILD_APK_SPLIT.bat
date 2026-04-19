@echo off
echo ========================================
echo   FoodLens - Build Split APKs
echo ========================================
echo   (Smaller file sizes per architecture)
echo.

echo [1/4] Cleaning build cache...
call flutter clean
echo.

echo [2/4] Getting dependencies...
call flutter pub get
echo.

echo [3/4] Building split APKs...
echo This may take 3-5 minutes...
call flutter build apk --split-per-abi --release
echo.

if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo   BUILD SUCCESS!
    echo ========================================
    echo.
    echo APK Files:
    echo build\app\outputs\flutter-apk\app-arm64-v8a-release.apk (RECOMMENDED)
    echo build\app\outputs\flutter-apk\app-armeabi-v7a-release.apk
    echo build\app\outputs\flutter-apk\app-x86_64-release.apk
    echo.
    echo Use app-arm64-v8a-release.apk for most modern phones
    echo.
) else (
    echo ========================================
    echo   BUILD FAILED
    echo ========================================
    echo Check errors above
)

pause
