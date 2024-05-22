from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(url, output_path):
    # Download the video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download(output_path=output_path)

    # Convert to MP3
    base, ext = os.path.splitext(downloaded_file)
    mp3_file = base + '.mp3'
    audio = AudioSegment.from_file(downloaded_file)
    audio.export(mp3_file, format='mp3')

    # Remove the original file
    os.remove(downloaded_file)

    return mp3_file

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output path (default is current directory): ") or "."
    mp3_file = download_youtube_video_as_mp3(url, output_path)
    print(f"MP3 file saved as {mp3_file}")
