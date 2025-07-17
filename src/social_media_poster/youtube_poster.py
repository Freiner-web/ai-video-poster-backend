import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# This is the name of the file that will store the user's credentials.
CREDENTIALS_PICKLE_FILE = 'youtube_credentials.pkl'

# This is the scope that we'll be requesting from the user.
# It allows us to upload videos on their behalf.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def get_youtube_service():
    """
    Authenticates with the YouTube API and returns a service object.
    """
    creds = None
    # The file youtube_credentials.pkl stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(CREDENTIALS_PICKLE_FILE):
        with open(CREDENTIALS_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(CREDENTIALS_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)

def upload_video_to_youtube(video_path, title, description, tags):
    """
    Uploads a video to YouTube.

    Args:
        video_path (str): The path to the video file.
        title (str): The title of the video.
        description (str): The description of the video.
        tags (list): A list of tags for the video.
    """
    youtube = get_youtube_service()

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '22'  # 'People & Blogs' category
        },
        'status': {
            'privacyStatus': 'private'  # or 'public' or 'unlisted'
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"Video uploaded successfully! Video ID: {response['id']}")
    return response['id']

# Example usage:
#
# from src.social_media_poster.youtube_poster import upload_video_to_youtube
#
# # This assumes you have a video file named 'output.mp4' and your
# # client_secrets.json file is set up correctly.
# upload_video_to_youtube(
#     'output.mp4',
#     'My Awesome AI-Generated Video',
#     'This video was created using AI!',
#     ['ai', 'automation', 'cool']
# )
