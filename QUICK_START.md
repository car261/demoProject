# FoodLens - Quick Start Guide

## ⚡ Quick Start (3 Steps)

### 1. Install Dependencies
```bash
cd c:\Users\HP\Desktop\PROJECT
flutter pub get
```

### 2. Run the App
```bash
flutter run
```

### 3. Grant Permissions
When the app launches, grant camera and storage permissions.

That's it! The app will open directly to the camera screen.

## 🎯 App Flow

```
📱 Launch App
    ↓
📷 Camera Screen (Live Preview)
    ↓ [Capture Photo]
    ↓
🍎 Food Result Screen
    ├─ See nutrition info
    ├─ View health suggestions
    └─ Start chat about food
        ↓
💬 Chat Screen
    ├─ Ask questions
    └─ Send images
```

## 🗺️ Navigation Map

- **/** → Camera (Landing Screen)
- **/result** → Food Analysis
- **/chat** → Full Chat
- **/profile** → User Profile
- **/health** → Health Stats
- **/settings** → App Settings
- **/login** → Login Screen
- **/signup** → Signup Screen

## 📋 Features to Test

### Camera Screen
- [ ] Camera preview loads
- [ ] Capture button takes photo
- [ ] Gallery button opens picker
- [ ] Flash toggle works
- [ ] Menu opens drawer
- [ ] Profile button navigates

### Food Result
- [ ] Image displays correctly
- [ ] Food name and calories shown
- [ ] Macros displayed (P/C/F)
- [ ] Allergy warnings appear
- [ ] Health suggestion shown
- [ ] Chat input opens full chat

### Chat
- [ ] Send text messages
- [ ] Messages appear in bubbles
- [ ] AI responds (mock)
- [ ] Send images from gallery
- [ ] Image chat response
- [ ] Clear chat works

### Profile
- [ ] Update name
- [ ] Update email
- [ ] Upload profile photo
- [ ] Changes save in memory

### Health Stats
- [ ] Enter weight/height
- [ ] BMI auto-calculates
- [ ] Select body type
- [ ] Toggle allergies
- [ ] UI updates reactively

### Settings
- [ ] Switch theme mode
- [ ] Change color palette
- [ ] Theme applies immediately

### Drawer
- [ ] Opens from camera
- [ ] Navigate to all sections
- [ ] About dialog shows

## 🎨 Try These

1. **Capture a photo** → See mock nutrition analysis
2. **Switch to Food Theme** → Settings → Color Palette → Food Theme
3. **Ask a food question** → Result screen → Type in chat bar
4. **Add your health stats** → Drawer → Health Stats
5. **Change your profile photo** → Drawer → Profile

## 🔍 Mock Data Examples

When you capture/select an image, you'll see one of these foods:
- Avocado Toast (280 kcal)
- Grilled Salmon (420 kcal)
- Chocolate Cake (580 kcal)
- Greek Yogurt Bowl (220 kcal)
- Quinoa Buddha Bowl (380 kcal)

Chat responses will cycle through 5 different nutritional tips!

## ⚠️ Common Issues

### Camera not working?
- Grant camera permission when prompted
- For Android: Check Settings → Apps → FoodLens → Permissions

### Theme not changing?
- Go to Settings
- Select theme mode (Light/Dark/System)
- Changes apply immediately

### Build errors?
```bash
flutter clean
flutter pub get
flutter run
```

## 📱 Recommended Test Device

- **Android**: API 21+ (Android 5.0+)
- **iOS**: iOS 12.0+
- **Physical device recommended** for camera testing

## 🎓 Development Notes

- All data is **in-memory** (no database)
- All AI responses are **mock** (no real API)
- Permissions requested at runtime
- Theme changes persist during session

## 🚀 Next Steps After Testing

1. Integrate real food detection API
2. Connect actual AI chat service
3. Add user authentication (Firebase/etc)
4. Implement data persistence
5. Add more nutrition features

---

**Ready to test!** Run `flutter run` and explore the app.
