import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Welcome, [Username]'),
        actions: [
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () {
              // TODO: Navigate to Profile screen
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Recent Projects',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 10),
              // Placeholder for recent projects
              Container(
                height: 150,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: 5,
                  itemBuilder: (context, index) {
                    return Card(
                      child: Container(
                        width: 150,
                        child: Center(child: Text('Project ${index + 1}')),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 30),
              const Text(
                'Quick Actions',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 10),
              // Placeholder for quick actions
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () async {
                      // Pick a video file
                      // FilePickerResult? result = await FilePicker.platform.pickFiles(
                      //   type: FileType.video,
                      // );

                      // if (result != null) {
                      //   PlatformFile file = result.files.first;
                      //   print(file.name);
                      //   print(file.bytes);
                      //   print(file.size);
                      //   print(file.extension);
                      //   print(file.path);

                      //   // Upload the video to YouTube
                      //   var response = await ApiService.uploadToYouTube(
                      //     file.path!,
                      //     'My Awesome AI-Generated Video',
                      //     'This video was created using AI!',
                      //     'ai,automation,cool',
                      //   );

                      //   print(response);
                      // } else {
                      //   // User canceled the picker
                      // }
                    },
                    icon: const Icon(Icons.upload),
                    label: const Text('Upload to YouTube'),
                  ),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: const Icon(Icons.cut),
                    label: const Text('Auto-Clip'),
                  ),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: const Icon(Icons.auto_awesome),
                    label: const Text('AI Edit'),
                  ),
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: const Icon(Icons.mic),
                    label: const Text('Add Voiceover'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.folder),
            label: 'Projects',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.sync),
            label: 'Automation',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
      ),
    );
  }
}
