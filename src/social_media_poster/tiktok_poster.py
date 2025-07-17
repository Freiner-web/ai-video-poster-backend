from tiktok_uploader.upload import upload_video

def upload_video_to_tiktok(video_path, title, cookies):
    """
    Uploads a video to TikTok.

    Args:
        video_path (str): The path to the video file.
        title (str): The title of the video.
        cookies (str): The path to your TikTok cookies file.
    """
    upload_video(
        video_path,
        description=title,
        cookies=cookies,
    )
    print("Video uploaded successfully to TikTok!")

# Example usage:
#
# from src.social_media_poster.tiktok_poster import upload_video_to_tiktok
#
# # To get your TikTok cookies, you can use a browser extension like
# # "Get cookies.txt" for Chrome or "cookies.txt" for Firefox.
# # You'll need to be logged in to TikTok in your browser, then use the
# # extension to export your cookies to a file (e.g., 'tiktok_cookies.txt').
# #
# # Important: Be careful with your cookies file, as it contains your
# # session information. Do not share it with anyone.
#
# # This assumes you have a video file named 'output.mp4' and your
# # cookies file is named 'tiktok_cookies.txt'.
# upload_video_to_tiktok(
#     'output.mp4',
#     'My Awesome AI-Generated Video #ai #automation',
#     'tiktok_cookies.txt'
# )
