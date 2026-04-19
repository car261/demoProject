import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/theme/app_theme.dart';
import 'core/theme/theme_provider.dart';
import 'core/router/app_router.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends ConsumerWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final router = ref.watch(routerProvider);
    final themeSettings = ref.watch(themeProvider);
    
    // Get system brightness
    final systemBrightness = MediaQuery.platformBrightnessOf(context);
    
    // Determine effective brightness
    final Brightness effectiveBrightness = themeSettings.themeMode == ThemeMode.system
        ? systemBrightness
        : (themeSettings.themeMode == ThemeMode.light ? Brightness.light : Brightness.dark);
    
    return MaterialApp.router(
      title: 'FoodLens',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light(palette: themeSettings.colorPalette),
      darkTheme: AppTheme.dark(palette: themeSettings.colorPalette),
      themeMode: themeSettings.themeMode == ThemeMode.system 
          ? ThemeMode.system 
          : (themeSettings.themeMode == ThemeMode.light ? ThemeMode.light : ThemeMode.dark),
      routerConfig: router,
    );
  }
}
