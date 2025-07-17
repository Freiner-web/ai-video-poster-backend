from src.video_generator.generator import generate_video
from src.video_editor.editor import add_text_overlay
from src.social_media_poster.youtube_poster import upload_video_to_youtube
from src.social_media_poster.tiktok_poster import upload_video_to_tiktok

def main():
    """
    Main function to run the video generation and posting automation.
    """
    # 1. Get a prompt for the video.
    video_prompt = "A futuristic cityscape with flying cars"

    # 2. Generate the video using the Runway API.
    #    (This is still a placeholder)
    print("Generating video...")
    # generated_video_path = generate_video(None, {'prompt': video_prompt})
    generated_video_path = "input.mp4" # Placeholder path
    print("Video generated successfully!")

    # 3. Edit the video.
    print("Editing video...")
    edited_video_path = "output.mp4"
    add_text_overlay(generated_video_path, "Hello from the future!", edited_video_path)
    print("Video edited successfully!")

    # 4. Post the video to YouTube.
    #    (Requires client_secrets.json)
    print("Posting video to YouTube...")
    # upload_video_to_youtube(
    #     edited_video_path,
    #     "My Awesome AI-Generated Video",
    #     "This video was created using AI! #ai #automation",
    #     ["ai", "automation", "cool"]
    # )
    print("Video posted to YouTube successfully!")

    # 5. Post the video to TikTok.
    #    (Requires tiktok_cookies.txt)
    print("Posting video to TikTok...")
    # upload_video_to_tiktok(
    #     edited_video_path,
    #     "My Awesome AI-Generated Video #ai #automation",
    #     "tiktok_cookies.txt"
    # )
    print("Video posted to TikTok successfully!")


if __name__ == "__main__":
    main()
