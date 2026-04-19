# FoodLens - AI Food Analysis App

A production-quality cross-platform mobile app built with Flutter that analyzes food, provides nutrition information, and offers chat-based interaction.

## Features

### 🎥 Camera-First UX
- Live camera preview as landing screen
- Instant food capture and analysis
- Gallery image selection support
- Flash control for better photos

### 🍎 Food Analysis
- Mock AI-powered food detection
- Detailed nutrition breakdown (calories, macros)
- Allergy warnings
- Personalized health suggestions

### 💬 Smart Chat
- Text and image-based conversations
- Mock AI responses about food and nutrition
- Conversation history
- Smooth message animations

### 👤 Profile Management
- Customizable profile with photo
- Name and email management
- User preferences

### 📊 Health Tracking
- Weight and height tracking
- Automatic BMI calculation
- Body type selection (Lean, Fit, Fit-Bulky, Overweight)
- Allergy management (multi-select)

### 🎨 Customizable Themes
- Light / Dark / System modes
- Two color palettes:
  - Default (Material 3)
  - Food Theme (greens and warm tones)
- Smooth theme transitions

## Tech Stack

- **Framework**: Flutter 3.0+
- **State Management**: Riverpod
- **Navigation**: go_router
- **Camera**: camera plugin
- **Image Picker**: image_picker plugin
- **Permissions**: permission_handler
- **Design**: Material 3

## Project Structure

```
lib/
├── core/
│   ├── theme/          # Material 3 themes, color schemes
│   └── router/         # go_router configuration
├── features/
│   ├── camera_screen.dart
│   ├── camera_provider.dart
│   ├── food_result_screen.dart
│   ├── food_provider.dart
│   ├── chat_screen.dart
│   ├── chat_provider.dart
│   ├── profile_screen.dart
│   ├── profile_provider.dart
│   ├── health_stats_screen.dart
│   ├── health_provider.dart
│   ├── settings_screen.dart
│   └── auth/           # Login/Signup screens
├── shared/
│   ├── widgets/        # Reusable components
│   ├── food_item.dart
│   ├── chat_message.dart
│   ├── user_profile.dart
│   └── health_stats.dart
└── main.dart
```

## Getting Started

### Prerequisites
- Flutter SDK 3.0 or higher
- Android Studio / Xcode (for mobile development)
- A physical device or emulator with camera support

### Installation

1. **Clone the repository**
   ```bash
   cd PROJECT
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Run the app**
   ```bash
   flutter run
   ```

### Platform-Specific Setup

#### Android
- Minimum SDK: 21
- Target SDK: 33
- Permissions are configured in `android/app/src/main/AndroidManifest.xml`

#### iOS
- Minimum iOS version: 12.0
- Camera and photo library permissions required
- Update `ios/Runner/Info.plist` with usage descriptions

## Usage

### Camera Screen (Landing)
- App opens directly to live camera
- Use the center button to capture food
- Gallery button (bottom-left) to select existing photos
- Flash button (bottom-right) for lighting control
- Menu button (top-left) to access drawer
- Profile button (top-right) for quick profile access

### Food Result Screen
- Top 40%: Food image preview
- Middle 50%: Nutrition information
  - Calories
  - Macronutrients (Protein, Carbs, Fat)
  - Allergy warnings
  - Health suggestions
- Bottom 10%: Chat input bar

### Chat Screen
- Text and image messaging
- Mock AI responses
- Conversation history
- Clear chat option

### Drawer Navigation
- Profile
- Health Stats
- Chat History
- Settings
- About

## Mock Data

All food analysis and chat responses are currently mock data. The app is designed to easily integrate with real AI/ML APIs:

- Replace `FoodItem.fromImage()` with actual food detection API
- Replace chat responses in `ChatNotifier` with real AI service
- Add backend integration for user data persistence

## Key Implementation Details

### State Management
- Riverpod providers for all features
- In-memory state (no database)
- Reactive UI updates

### Permissions
- Camera permission with graceful handling
- Storage/Media access for gallery
- Runtime permission requests
- Permission denial UI with retry

### Navigation
- Declarative routing with go_router
- Custom page transitions
- Hero animations for images
- Deep linking support

### Theme System
- Material 3 design throughout
- Dynamic color schemes
- System theme awareness
- Smooth theme switching

## Customization

### Adding New Food Detection
Update `lib/shared/food_item.dart`:
```dart
factory FoodItem.fromImage(String imagePath) {
  // Replace with actual API call
  return yourFoodDetectionAPI(imagePath);
}
```

### Integrating Real AI Chat
Update `lib/features/chat_provider.dart`:
```dart
void _generateMockResponse() {
  // Replace with actual AI service
  final response = await yourChatAPI(userMessage);
  // ...
}
```

### Adding Persistence
Integrate a database (SQLite, Hive, etc.) in providers:
- ProfileNotifier
- HealthNotifier
- ChatNotifier

## Future Enhancements

- [ ] Real AI/ML food detection
- [ ] Backend API integration
- [ ] User authentication (Firebase, etc.)
- [ ] Data persistence (local + cloud)
- [ ] Recipe suggestions
- [ ] Meal planning features
- [ ] Nutrition goal tracking
- [ ] Social features (share meals)

## License

This project is for educational/demonstration purposes.

## Support

For issues or questions, please refer to the Flutter documentation:
- [Flutter Docs](https://docs.flutter.dev/)
- [Riverpod](https://riverpod.dev/)
- [go_router](https://pub.dev/packages/go_router)
