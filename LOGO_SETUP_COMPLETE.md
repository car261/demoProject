# App Logo Setup - Complete Guide

## ✅ What's Been Configured

### 1. Project Structure
```
PROJECT/
├── assets/
│   └── logo/
│       └── logo.png          ← Place your logo here
├── pubspec.yaml              ← Updated with assets + launcher icons
├── lib/
│   ├── features/auth/presentation/screens/
│   │   ├── login_screen.dart    ← Shows logo
│   │   └── signup_screen.dart   ← Shows logo
│   └── shared/widgets/
│       └── app_drawer.dart      ← Shows logo in header
└── create_assets.bat         ← Run this to create folders
```

### 2. Files Modified

✅ **pubspec.yaml**
- Added `flutter_launcher_icons: ^0.13.1` dependency
- Configured assets path: `assets/logo/logo.png`
- Set up adaptive icon with black background

✅ **login_screen.dart**
- Added 100x100px logo display
- Centered at top
- Rounded corners (20px)
- Fallback icon if logo missing

✅ **signup_screen.dart**
- Same logo display as login
- Consistent styling

✅ **app_drawer.dart**
- Added 48x48px logo in drawer header
- Black background container
- Rounded corners (12px)
- Fallback icon if logo missing

## 📋 Step-by-Step Setup

### Step 1: Create Assets Folder

**Option A: Using batch file**
```bash
create_assets.bat
```

**Option B: Manual creation**
```bash
mkdir assets
mkdir assets\logo
```

### Step 2: Create Your Logo

**See:** `LOGO_DESIGN_GUIDE.md` for detailed design specs

**Quick Requirements:**
- Size: 1024x1024 pixels (minimum)
- Background: Pure black (#000000)
- Icon: Pure white (#FFFFFF)
- Format: PNG with transparency or solid background
- Style: Minimal, flat, no gradients

**Recommended Tools:**
1. **Canva** (easiest) - https://canva.com
2. **Figma** (professional) - https://figma.com
3. **Photopea** (free Photoshop) - https://photopea.com

**AI Generation Prompt:**
```
Minimal flat app icon logo, black background (#000000), 
white food scanner icon, camera aperture + plate symbol, 
geometric shapes, centered, no text, 1024x1024
```

### Step 3: Save Logo

1. Export/download your logo as PNG
2. Name it exactly: `logo.png`
3. Place it in: `assets/logo/logo.png`

**File location:**
```
C:\Users\HP\Desktop\PROJECT\assets\logo\logo.png
```

### Step 4: Install Dependencies

```bash
flutter pub get
```

This will:
- Download flutter_launcher_icons package
- Register the logo asset
- Prepare for icon generation

### Step 5: Generate App Icons

```bash
flutter pub run flutter_launcher_icons
```

This will automatically create:
- Android app icons (all sizes)
- Adaptive icons (foreground + background)
- Proper manifest entries

**Output:**
```
✓ Creating icons for Android
✓ Generated adaptive icon
✓ Updated AndroidManifest.xml
```

### Step 6: Verify Logo Display

**Run the app:**
```bash
flutter run
```

**Check these screens:**
1. ✅ Login screen - Logo at top (100px)
2. ✅ Signup screen - Logo at top (100px)
3. ✅ Drawer - Logo in header (48px)

**Verify app icon:**
- Check app drawer on device
- Should show your custom logo

### Step 7: Build APK

```bash
BUILD_APK.bat
```

or

```bash
flutter build apk --release
```

## 🎨 Logo Design Specifications

### Dimensions
```
Login/Signup: 100x100 px
Drawer:       48x48 px
App Icon:     512x512 px (will be auto-resized)
```

### Colors
```css
Background: #000000 (black)
Icon:       #FFFFFF (white)
Border:     Rounded, 20px radius (login), 12px (drawer)
```

### Style
- ✅ Minimal and flat
- ✅ Food-related icon
- ✅ Geometric shapes
- ✅ High contrast
- ❌ No gradients
- ❌ No text
- ❌ No complex details

## 🔧 Troubleshooting

### Problem: "Unable to load asset"

**Solution:**
```bash
flutter clean
flutter pub get
flutter run
```

### Problem: Logo not showing

**Check:**
1. File exists: `assets/logo/logo.png`
2. File name is exact: `logo.png` (lowercase)
3. Ran `flutter pub get`
4. Restarted app

**Fallback:**
- App will show fork/knife icon if logo missing
- This is intentional - app won't crash

### Problem: Icon generation failed

**Solution:**
```bash
flutter pub upgrade flutter_launcher_icons
flutter pub run flutter_launcher_icons
```

### Problem: App icon not updated on device

**Solution:**
1. Uninstall old app completely
2. Rebuild: `flutter clean && flutter build apk`
3. Reinstall APK
4. May need device restart

## 📐 Logo Design Templates

### Simple Placeholder (5 minutes)

**Using PowerPoint/Google Slides:**
1. Create 1024x1024 slide
2. Fill background black
3. Add white circle (plate)
4. Add 3 horizontal white lines (scan lines)
5. Export as PNG
6. Save to `assets/logo/logo.png`

### Professional Design (30 minutes)

**Using Canva:**
1. Go to Canva.com
2. Custom size: 1024x1024
3. Background: Black (#000000)
4. Add elements:
   - Circle (plate outline)
   - Camera icon or aperture
   - Fork/knife symbols
5. Color: White (#FFFFFF)
6. Download PNG
7. Save to `assets/logo/logo.png`

## 🚀 Quick Start Commands

```bash
# 1. Create folders
create_assets.bat

# 2. Add your logo.png to assets/logo/

# 3. Install packages
flutter pub get

# 4. Generate app icons
flutter pub run flutter_launcher_icons

# 5. Run app
flutter run

# 6. Build APK
BUILD_APK.bat
```

## 📱 Where Logo Appears

### In-App
- ✅ Login screen (top, large)
- ✅ Signup screen (top, large)
- ✅ Drawer header (small)

### System
- ✅ App icon on home screen
- ✅ App drawer
- ✅ Recent apps
- ✅ Notifications (if implemented)

## 🎯 Logo Design Ideas

### Option 1: Camera + Plate
```
Black background
White camera aperture (circle with segments)
White plate in center
Simple and recognizable
```

### Option 2: Fork + Lens
```
Black background
White crossed fork and knife
White camera lens circle around them
Professional look
```

### Option 3: Scan Lines + Food (EASIEST)
```
Black background
White circle (plate)
2-3 white horizontal lines (scan effect)
White dot in center
Minimal, modern, quick to create
```

## 📦 Assets Folder Structure

```
assets/
└── logo/
    ├── logo.png              ← Main logo (required)
    └── (other sizes)         ← Optional variations
```

**Only one file required:** `logo.png`

All other sizes are auto-generated by flutter_launcher_icons.

## ✨ Final Checklist

Before building final APK:

- [ ] Logo file exists: `assets/logo/logo.png`
- [ ] Logo is 1024x1024 or larger
- [ ] Logo has black background
- [ ] Logo has white icon
- [ ] Ran `flutter pub get`
- [ ] Ran `flutter pub run flutter_launcher_icons`
- [ ] Logo displays on login screen
- [ ] Logo displays on signup screen
- [ ] Logo displays in drawer
- [ ] App icon shows on device
- [ ] No "asset not found" errors

## 🆘 Need Help?

1. See `LOGO_DESIGN_GUIDE.md` for design specs
2. Use fallback icon (fork/knife) until logo is ready
3. App works without logo - it's visual only
4. Logo can be added/updated later without code changes

---

**Your logo setup is complete!** 🎉

Just add `logo.png` to `assets/logo/` and run the commands above.
