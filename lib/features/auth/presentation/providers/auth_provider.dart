import 'dart:convert';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../../domain/models/user.dart';

const _authBaseUrl = String.fromEnvironment(
  'API_BASE_URL',
  defaultValue: 'http://10.0.2.2:8000',
);

class AuthState {
  final User? user;
  final String? token;
  final bool isLoading;
  final String? error;
  final bool isInitialized;

  AuthState({
    this.user,
    this.token,
    this.isLoading = false,
    this.error,
    this.isInitialized = false,
  });

  bool get isLoggedIn =>
    user != null && (token?.isNotEmpty ?? false);

  AuthState copyWith({
    User? user,
    String? token,
    bool? isLoading,
    String? error,
    bool? isInitialized,
    bool clearUser = false,
  }) {
    return AuthState(
      user: clearUser ? null : (user ?? this.user),
      token: clearUser ? null : (token ?? this.token),
      isLoading: isLoading ?? this.isLoading,
      error: error,
      isInitialized: isInitialized ?? this.isInitialized,
    );
  }
}

class AuthNotifier extends StateNotifier<AuthState> {
  AuthNotifier() : super(AuthState()) {
    _initialize();
  }

  Future<void> _initialize() async {
    final prefs = await SharedPreferences.getInstance();
    final isLoggedIn = prefs.getBool('isLoggedIn') ?? false;
    
    if (isLoggedIn) {
      final userId = prefs.getString('userId') ?? '1';
      final userName = prefs.getString('userName') ?? 'User';
      final userEmail = prefs.getString('userEmail') ?? 'user@example.com';
      final token = prefs.getString('token');
      
      final user = User(
        id: userId,
        name: userName,
        email: userEmail,
      );
      
      state = state.copyWith(user: user, token: token, isInitialized: true);
    } else {
      state = state.copyWith(isInitialized: true);
    }
  }

  Future<bool> login(String email, String password) async {
    if (email.isEmpty || password.isEmpty) {
      state = state.copyWith(error: 'Please fill in all fields');
      return false;
    }

    if (!email.contains('@')) {
      state = state.copyWith(error: 'Please enter a valid email');
      return false;
    }

    state = state.copyWith(isLoading: true, error: null);

    try {
      final response = await http
          .post(
            Uri.parse('$_authBaseUrl/auth/login'),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'email': email, 'password': password}),
          )
          .timeout(const Duration(seconds: 20));

      final decoded = jsonDecode(response.body);
      if (response.statusCode < 200 || response.statusCode >= 300 || decoded is! Map<String, dynamic>) {
        final message = decoded is Map<String, dynamic> ? (decoded['message']?.toString() ?? 'Login failed') : 'Login failed';
        state = state.copyWith(isLoading: false, error: message);
        return false;
      }

      final payload = decoded['data'];
      if (payload is! Map<String, dynamic>) {
        state = state.copyWith(isLoading: false, error: 'Invalid login response');
        return false;
      }

      final token = payload['token']?.toString();
      final userPayload = payload['user'];
      if (token == null || token.isEmpty || userPayload is! Map<String, dynamic>) {
        state = state.copyWith(isLoading: false, error: 'Invalid login response');
        return false;
      }

      final user = User(
        id: userPayload['user_id']?.toString() ?? '1',
        name: (userPayload['email']?.toString() ?? email).split('@')[0],
        email: userPayload['email']?.toString() ?? email,
      );

      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool('isLoggedIn', true);
      await prefs.setString('userId', user.id);
      await prefs.setString('userName', user.name);
      await prefs.setString('userEmail', user.email);
      await prefs.setString('token', token);

      state = state.copyWith(user: user, token: token, isLoading: false);
      return true;
    } catch (_) {
      state = state.copyWith(isLoading: false, error: 'Unable to login');
      return false;
    }
  }

  Future<bool> signup(String name, String email, String password) async {
    if (name.isEmpty || email.isEmpty || password.isEmpty) {
      state = state.copyWith(error: 'Please fill in all fields');
      return false;
    }

    if (!email.contains('@')) {
      state = state.copyWith(error: 'Please enter a valid email');
      return false;
    }

    if (password.length < 6) {
      state = state.copyWith(error: 'Password must be at least 6 characters');
      return false;
    }

    state = state.copyWith(isLoading: true, error: null);

    try {
      final response = await http
          .post(
            Uri.parse('$_authBaseUrl/auth/signup'),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({'email': email, 'password': password}),
          )
          .timeout(const Duration(seconds: 20));

      final decoded = jsonDecode(response.body);
      if (response.statusCode < 200 || response.statusCode >= 300 || decoded is! Map<String, dynamic>) {
        final message = decoded is Map<String, dynamic> ? (decoded['message']?.toString() ?? 'Signup failed') : 'Signup failed';
        state = state.copyWith(isLoading: false, error: message);
        return false;
      }

      final payload = decoded['data'];
      if (payload is! Map<String, dynamic>) {
        state = state.copyWith(isLoading: false, error: 'Invalid signup response');
        return false;
      }

      final token = payload['token']?.toString();
      final userPayload = payload['user'];
      if (token == null || token.isEmpty || userPayload is! Map<String, dynamic>) {
        state = state.copyWith(isLoading: false, error: 'Invalid signup response');
        return false;
      }

      final user = User(
        id: userPayload['user_id']?.toString() ?? '1',
        name: name,
        email: userPayload['email']?.toString() ?? email,
      );

      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool('isLoggedIn', true);
      await prefs.setString('userId', user.id);
      await prefs.setString('userName', user.name);
      await prefs.setString('userEmail', user.email);
      await prefs.setString('token', token);

      state = state.copyWith(user: user, token: token, isLoading: false);
      return true;
    } catch (_) {
      state = state.copyWith(isLoading: false, error: 'Unable to signup');
      return false;
    }
  }

  Future<void> logout() async {
    // Attempt to call backend logout (best-effort, always clear locally)
    final token = state.token;
    if (token != null && token.isNotEmpty) {
      try {
        await http
            .post(
              Uri.parse('$_authBaseUrl/auth/logout'),
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer $token',
              },
            )
            .timeout(const Duration(seconds: 5));
      } catch (_) {
        // Logout best-effort; continue with local clear
      }
    }

    // Clear local state
    final prefs = await SharedPreferences.getInstance();
    await prefs.clear();
    
    state = state.copyWith(clearUser: true);
  }
}

final authProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
  return AuthNotifier();
});
