import 'dart:convert';

Map<String, dynamic> safeJson(String raw) {
  try {
    final decoded = jsonDecode(raw);
    if (decoded is Map<String, dynamic>) {
      return decoded;
    }
  } catch (_) {
    // Return a safe fallback below.
  }
  return {'response': 'Sorry, something went wrong'};
}

String extractReply(Map<String, dynamic> data) {
  final answers = data['answers'];
  if (answers != null) {
    if (answers is String && answers.trim().isNotEmpty) {
      return answers;
    }
    final asText = answers.toString();
    if (asText.isNotEmpty) {
      return asText;
    }
  }

  final response = data['response'];
  if (response is String && response.trim().isNotEmpty) {
    return response;
  }

  final payload = data['data'];
  if (payload is Map<String, dynamic>) {
    final nestedAnswers = payload['answers'];
    if (nestedAnswers != null) {
      final asText = nestedAnswers.toString();
      if (asText.isNotEmpty) {
        return asText;
      }
    }

    final nestedResponse = payload['response'];
    if (nestedResponse is String && nestedResponse.trim().isNotEmpty) {
      return nestedResponse;
    }
  }

  return 'Sorry, something went wrong';
}
