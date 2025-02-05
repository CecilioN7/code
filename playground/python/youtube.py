import yt_dlp

def download_live_stream_and_audio(video_url):
    # Define options for downloading the best video and audio
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video + best audio
        'live_from_start': True,  # Download from the start of live stream if possible
        'noplaylist': True,  # Download only the individual video, not the playlist
        'outtmpl': '%(title)s.%(ext)s',  # Output template for merged video+audio
        'merge_output_format': 'mp4',  # Merge into MP4 format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Merge into mp4 format for video
        }]
    }

    # Define options for extracting the audio file separately
    audio_opts = {
        'format': 'bestaudio/best',  # Download the best available audio
        'outtmpl': '%(title)s_audio.%(ext)s',  # Save audio with '_audio' suffix
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Extract audio to MP3 format (or use 'm4a' for m4a format)
            'preferredquality': '192',  # Set the quality of the audio (192 kbps)
        }],
    }

    try:
        # First, download the best video and audio combined
        print("Downloading video and audio (best quality)...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Next, download and extract only the audio
        print("Extracting audio file separately...")
        with yt_dlp.YoutubeDL(audio_opts) as ydl:
            ydl.download([video_url])

        print("Download complete! Video+Audio and separate audio file saved.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ask the user for the live stream URL
    video_url = input("Enter the YouTube live stream URL: ")

    # Start downloading the video and extracting audio
    download_live_stream_and_audio(video_url)
