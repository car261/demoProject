import 'dart:convert';
import 'dart:io';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;

import '../../features/auth/presentation/providers/auth_provider.dart';
import 'response_parser.dart';

class ApiConfig {
  static String get baseUrl {
    return const String.fromEnvironment(
      'API_BASE_URL',
      defaultValue: 'http://10.0.2.2:8000',
    );
  }
}

class ApiClient {
  ApiClient(this.ref);

  final Ref ref;

  String get baseUrl => ApiConfig.baseUrl;

  Future<Map<String, dynamic>> sendChat({
    String? text,
    String? imagePath,
  }) async {
    try {
      final token = ref.read(authProvider).token;
      final hasText = text != null && text.trim().isNotEmpty;
      final hasImage = imagePath != null && imagePath.trim().isNotEmpty;

      if (!hasText && !hasImage) {
        return {'response': 'Sorry, something went wrong'};
      }

      if (token == null || token.isEmpty) {
        await ref.read(authProvider.notifier).logout();
        return {'response': 'Session expired. Please login again'};
      }

      if (hasImage) {
        final imageFile = File(imagePath!);
        if (!imageFile.existsSync()) {
          return {'response': 'Sorry, something went wrong'};
        }

        final request = http.MultipartRequest(
          'POST',
          Uri.parse('$baseUrl/chat'),
        );

        request.headers['Authorization'] = 'Bearer $token';

        if (hasText) {
          request.fields['text'] = text!.trim();
        }
        request.fields['chat_id'] = 'default';
        request.files.add(await http.MultipartFile.fromPath('image', imagePath));

        final streamed = await request.send().timeout(const Duration(seconds: 20));
        final body = await streamed.stream.bytesToString();

        if (streamed.statusCode == 401) {
          ref.read(authProvider.notifier).logout();
          return {'response': 'Session expired. Please login again'};
        }

        return safeJson(body);
      }

      final headers = <String, String>{
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $token',
      };

      final response = await http
          .post(
            Uri.parse('$baseUrl/chat'),
            headers: headers,
            body: jsonEncode({'text': text?.trim(), 'chat_id': 'default'}),
          )
          .timeout(const Duration(seconds: 20));

      if (response.statusCode == 401) {
        ref.read(authProvider.notifier).logout();
        return {'response': 'Session expired. Please login again'};
      }

      return safeJson(response.body);
    } catch (_) {
      return {'response': 'Sorry, something went wrong'};
    }
  }
}
