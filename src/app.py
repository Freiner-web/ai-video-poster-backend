from flask import Flask
from src import auth

app = Flask(__name__)

# Register authentication routes
auth.register_routes(app)

from flask import request, jsonify
from src.social_media_poster import youtube_poster
import os

@app.route('/upload_to_youtube', methods=['POST'])
def upload_to_youtube():
    if 'video' not in request.files:
        return jsonify({'message': 'No video file provided'}), 400

    video_file = request.files['video']
    title = request.form.get('title', 'My Awesome AI-Generated Video')
    description = request.form.get('description', 'This video was created using AI!')
    tags = request.form.get('tags', 'ai,automation,cool').split(',')

    # Save the video file temporarily
    video_path = os.path.join('uploads', video_file.filename)
    video_file.save(video_path)

    try:
        video_id = youtube_poster.upload_video_to_youtube(
            video_path,
            title,
            description,
            tags
        )
        return jsonify({'message': 'Video uploaded successfully', 'video_id': video_id}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to upload video to YouTube', 'error': str(e)}), 500
    finally:
        # Clean up the temporary video file
        if os.path.exists(video_path):
            os.remove(video_path)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
