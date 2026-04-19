@echo off
echo Cleaning up conflicting files...

echo Deleting old chat_screen.dart...
del /f "lib\features\chat_screen.dart" 2>nul

echo Deleting old chat_provider.dart...  
del /f "lib\features\chat_provider.dart" 2>nul

echo Creating logo directory...
mkdir assets\logo 2>nul

echo Done! Now:
echo 1. Copy your logo.png to assets\logo\logo.png
echo 2. Run: flutter clean
echo 3. Run: flutter pub get
echo 4. Run: flutter run

pause