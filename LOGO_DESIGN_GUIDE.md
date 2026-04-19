# FoodLens App Logo Design Specification

## Logo Concept: "AI Food Scanner"

### Design Description

**Icon Symbol:** A combination of a camera aperture and a plate/food icon
- **Outer ring:** Camera aperture segments (6-8 segments)
- **Inner circle:** Simplified plate or fork-knife crossed
- **Center dot:** Small circle (representing focus/scan point)

### Style Guide

**Colors:**
- Background: `#000000` (Pure Black)
- Icon: `#FFFFFF` (Pure White)

**Shape:**
- Square canvas: 1024x1024px (for app icon)
- Rounded corners: 20% radius for modern look
- Icon occupies 60-70% of canvas

**Style:**
- Minimal and flat
- No gradients or shadows
- Clean geometric shapes
- 2-3 pixel stroke width
- Centered composition

### Icon Variations

#### Option 1: Camera Aperture + Plate
```
┌─────────────────────┐
│                     │
│    ◢ ◣   ◥ ◤       │ ← Aperture segments
│   ◣   ○   ◤        │ ← Center focus
│    ◥ ◤   ◢ ◣       │
│                     │
└─────────────────────┘
```

#### Option 2: Fork + Knife + Camera
```
┌─────────────────────┐
│                     │
│      ┃  ┃          │ ← Fork & Knife
│      ┃  ┃          │
│    ╱─○─○─╲         │ ← Camera lens
│   │  ●  │          │ ← Focus dot
│    ╲─────╱         │
│                     │
└─────────────────────┘
```

#### Option 3: Simple Plate with Scan Lines (RECOMMENDED)
```
┌─────────────────────┐
│                     │
│    ─────────        │ ← Scan lines
│   (         )       │ ← Plate circle
│    ─────────        │ ← Scan lines
│        ●            │ ← Center point
│                     │
└─────────────────────┘
```

## File Structure

```
assets/
└── logo/
    ├── logo.png           ← Main logo (1024x1024)
    ├── logo_512.png       ← Medium size
    ├── logo_256.png       ← Small size
    └── logo_adaptive.png  ← Adaptive icon foreground
```

## Where to Create the Logo

### Option 1: Using Free Online Tools (Easiest)

1. **Canva** (Free)
   - Go to: https://www.canva.com
   - Create custom size: 1024x1024
   - Set background: Black (#000000)
   - Add shapes/icons in white
   - Download as PNG

2. **Figma** (Free)
   - Go to: https://www.figma.com
   - Create frame: 1024x1024
   - Use shape tools to design
   - Export as PNG @ 2x

3. **Photopea** (Free Photoshop alternative)
   - Go to: https://www.photopea.com
   - Create new image: 1024x1024
   - Black background
   - White shapes/text
   - Export as PNG

### Option 2: Using AI Image Generators

**Prompt for DALL-E / Midjourney / Stable Diffusion:**
```
A minimal flat app icon logo on pure black background (#000000), 
white (#FFFFFF) icon only, featuring a camera aperture combined 
with a food plate symbol, geometric shapes, centered composition, 
modern minimalist style, no text, no gradients, high contrast
```

### Option 3: Simple Text-Based Placeholder

For now, you can use a simple text logo:
- Black background
- White text "FL" (for FoodLens)
- Large bold font
- Centered

## Implementation Steps

1. **Create the logo image** using one of the methods above
2. **Save as PNG** with transparent or black background
3. **Place in:** `assets/logo/logo.png`
4. **Update** `pubspec.yaml` with assets configuration
5. **Run** `flutter pub get`
6. **Generate app icons** with flutter_launcher_icons
7. **Update UI** to display logo

## Sizing Reference

### In-App Usage
- **Login Screen:** 100-120px
- **Drawer Header:** 48-64px
- **Splash Screen:** 150-200px

### App Icon
- **Android:** 512x512 (will be resized)
- **iOS:** 1024x1024 (will be resized)
- **Adaptive:** Foreground + background layers

## Color Codes (for designers)

```css
Background: #000000
Icon: #FFFFFF
Accent (optional): #4CAF50 (green for food theme)
```

## Design Principles

✅ **DO:**
- Keep it simple and recognizable
- Use geometric shapes
- Ensure good contrast
- Make it scalable
- Center the composition
- Use even pixel values

❌ **DON'T:**
- Use gradients
- Add text/labels
- Make it too detailed
- Use complex illustrations
- Add shadows or effects
- Use photos/realistic images

## Quick Creation Guide (5 minutes)

### Using Canva:

1. Create 1024x1024 canvas
2. Set background to black
3. Add a white circle (represents plate)
4. Add 2-3 horizontal white lines across circle (scan lines)
5. Add small white dot in center
6. Download as PNG
7. Save to `assets/logo/logo.png`

### Using PowerPoint/Google Slides:

1. Create blank slide
2. Insert shapes: circles, lines
3. Color them white on black background
4. Right-click → Save as image
5. Resize to 1024x1024 in any image editor
6. Save to `assets/logo/logo.png`

## After Creating the Logo

Run these commands:
```bash
flutter pub get
flutter pub run flutter_launcher_icons
flutter clean
flutter build apk --release
```

Your logo will appear:
- ✅ As app icon on device
- ✅ On login screen
- ✅ In drawer header
- ✅ All properly sized and positioned

---

**Need help creating the logo?** Let me know and I can provide more specific guidance or alternative approaches!
