import 'package:flutter/material.dart';
import 'package:frontend/screens/home_screen.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
            // Replace with your desired background image
            image: NetworkImage('https://placeimg.com/640/480/tech'),
            fit: BoxFit.cover,
          ),
        ),
        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  'Sign In to NexusAI',
                  style: TextStyle(
                    fontSize: 32,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
                const SizedBox(height: 50),
                // Replace with your actual sign-in buttons
                ElevatedButton.icon(
                  onPressed: () {
                    // TODO: Implement Google Sign-In
                  },
                  icon: const Icon(Icons.g_mobiledata),
                  label: const Text('Sign in with Google'),
                  style: ElevatedButton.styleFrom(
                    minimumSize: const Size(250, 50),
                  ),
                ),
                const SizedBox(height: 20),
                ElevatedButton.icon(
                  onPressed: () {
                    // TODO: Implement Phone Number Login
                  },
                  icon: const Icon(Icons.phone),
                  label: const Text('Sign in with Phone'),
                  style: ElevatedButton.styleFrom(
                    minimumSize: const Size(250, 50),
                  ),
                ),
                const SizedBox(height: 50),
                TextButton(
                  onPressed: () {
                    Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(builder: (context) => const HomeScreen()),
                    );
                  },
                  child: const Text(
                    'Continue as Guest',
                    style: TextStyle(color: Colors.white70),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
