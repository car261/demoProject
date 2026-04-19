import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../shared/food_item.dart';

class FoodNotifier extends StateNotifier<FoodItem?> {
  FoodNotifier() : super(null);

  void setFood(FoodItem food) {
    state = food;
  }

  void clear() {
    state = null;
  }
}

final foodProvider = StateNotifierProvider<FoodNotifier, FoodItem?>((ref) {
  return FoodNotifier();
});
