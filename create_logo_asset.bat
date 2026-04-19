@echo off
mkdir assets\logo 2>nul
copy "android\app\src\main\res\mipmap-xxxhdpi\ic_launcher.png" "assets\logo\logo.png"
echo Logo asset created successfully!
pause