import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String _baseUrl = 'http://10.0.2.2:5000'; // For Android emulator

  static Future<Map<String, dynamic>> register(
      String username, String password) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/register'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );
    return jsonDecode(response.body);
  }

  static Future<Map<String, dynamic>> login(
      String username, String password) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );
    return jsonDecode(response.body);
  }

  static Future<Map<String, dynamic>> uploadToYouTube(
      String filePath, String title, String description, String tags) async {
    var request = http.MultipartRequest('POST', Uri.parse('$_baseUrl/upload_to_youtube'));
    request.files.add(await http.MultipartFile.fromPath('video', filePath));
    request.fields['title'] = title;
    request.fields['description'] = description;
    request.fields['tags'] = tags;

    var response = await request.send();
    var responseBody = await response.stream.bytesToString();
    return jsonDecode(responseBody);
  }
}
