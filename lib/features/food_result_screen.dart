import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../shared/food_item.dart';
import 'food_provider.dart';

class FoodResultScreen extends ConsumerStatefulWidget {
  final String? imagePath;

  const FoodResultScreen({Key? key, this.imagePath}) : super(key: key);

  @override
  ConsumerState<FoodResultScreen> createState() => _FoodResultScreenState();
}

class _FoodResultScreenState extends ConsumerState<FoodResultScreen> {
  final TextEditingController _chatController = TextEditingController();

  @override
  void dispose() {
    _chatController.dispose();
    super.dispose();
  }

  void _openChat() {
    // Navigate to chat screen with image path
    context.push('/chat/default');
  }

  @override
  Widget build(BuildContext context) {
    final foodItem = widget.imagePath != null 
        ? FoodItem.fromImage(widget.imagePath!) 
        : FoodItem.mock();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Food Analysis'),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => context.pop(),
        ),
      ),
      body: Column(
        children: [
          // Image Preview (40%)
          Expanded(
            flex: 4,
            child: Hero(
              tag: 'food-image',
              child: Container(
                width: double.infinity,
                decoration: BoxDecoration(
                  color: Colors.grey[200],
                  image: widget.imagePath != null
                      ? DecorationImage(
                          image: FileImage(File(widget.imagePath!)),
                          fit: BoxFit.cover,
                        )
                      : null,
                ),
                child: widget.imagePath == null
                    ? const Center(
                        child: Icon(Icons.restaurant, size: 80, color: Colors.grey),
                      )
                    : null,
              ),
            ),
          ),

          // Food Information (50%)
          Expanded(
            flex: 5,
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Food Name
                  Text(
                    foodItem.name,
                    style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  const SizedBox(height: 20),

                  // Calories
                  _InfoCard(
                    icon: Icons.local_fire_department,
                    title: 'Calories',
                    value: '${foodItem.calories.toInt()} kcal',
                    color: Colors.orange,
                  ),
                  const SizedBox(height: 12),

                  // Macros
                  _InfoCard(
                    icon: Icons.pie_chart,
                    title: 'Macronutrients',
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _MacroChip('Protein', '${foodItem.macros.protein.toInt()}g', Colors.blue),
                        _MacroChip('Carbs', '${foodItem.macros.carbs.toInt()}g', Colors.green),
                        _MacroChip('Fat', '${foodItem.macros.fat.toInt()}g', Colors.purple),
                      ],
                    ),
                  ),
                  const SizedBox(height: 12),

                  // Allergies
                  if (foodItem.allergyWarnings.isNotEmpty)
                    _InfoCard(
                      icon: Icons.warning_amber,
                      title: 'Allergy Warnings',
                      child: Wrap(
                        spacing: 8,
                        runSpacing: 8,
                        children: foodItem.allergyWarnings
                            .map((allergy) => Chip(
                                  label: Text(allergy, style: const TextStyle(fontSize: 12)),
                                  backgroundColor: Colors.red[50],
                                  side: BorderSide(color: Colors.red[300]!),
                                ))
                            .toList(),
                      ),
                    ),
                  const SizedBox(height: 12),

                  // Health Suggestion
                  _InfoCard(
                    icon: Icons.lightbulb,
                    title: 'Health Suggestion',
                    child: Text(
                      foodItem.healthSuggestion,
                      style: const TextStyle(height: 1.5),
                    ),
                  ),
                ],
              ),
            ),
          ),

          // Chat Input (10%)
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.surface,
              border: Border(
                top: BorderSide(color: Theme.of(context).dividerColor),
              ),
            ),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _chatController,
                    decoration: const InputDecoration(
                      hintText: 'Ask about this food...',
                      contentPadding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                    ),
                    onSubmitted: (_) => _openChat(),
                  ),
                ),
                const SizedBox(width: 8),
                IconButton(
                  icon: const Icon(Icons.send),
                  onPressed: _openChat,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _InfoCard extends StatelessWidget {
  final IconData icon;
  final String title;
  final String? value;
  final Widget? child;
  final Color? color;

  const _InfoCard({
    required this.icon,
    required this.title,
    this.value,
    this.child,
    this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, size: 20, color: color ?? Theme.of(context).colorScheme.primary),
                const SizedBox(width: 8),
                Text(
                  title,
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.w600,
                      ),
                ),
              ],
            ),
            if (value != null || child != null) const SizedBox(height: 12),
            if (value != null)
              Text(
                value!,
                style: Theme.of(context).textTheme.titleLarge,
              ),
            if (child != null) child!,
          ],
        ),
      ),
    );
  }
}

class _MacroChip extends StatelessWidget {
  final String label;
  final String value;
  final Color color;

  const _MacroChip(this.label, this.value, this.color);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: color),
          ),
          child: Column(
            children: [
              Text(
                value,
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: color,
                ),
              ),
              Text(
                label,
                style: TextStyle(fontSize: 12, color: color),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
