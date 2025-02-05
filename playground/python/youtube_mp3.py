import os
from pytube import YouTube
from pydub import AudioSegment

def download_video_as_mp3(url, output_path='.'):
    try:
        # Download the video
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(output_path=output_path)
        
        # Convert to mp3 using pydub
        print(f"Converting {downloaded_file} to MP3...")
        audio = AudioSegment.from_file(downloaded_file)
        mp3_filename = os.path.splitext(downloaded_file)[0] + '.mp3'
        audio.export(mp3_filename, format="mp3")
        
        # Optionally, remove the original video file after conversion
        os.remove(downloaded_file)
        
        print(f"Download complete: {mp3_filename}")
        return mp3_filename
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the output directory (leave blank for current directory): ") or '.'
    download_video_as_mp3(video_url, output_directory)
