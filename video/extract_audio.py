# 코드를 통해서 비디오 파일의 오디오만 추출
import os
import sys
from moviepy.editor import VideoFileClip


def process_video(input_video_path: str) -> None:
    output_filename, _ = os.path.splitext(input_video_path)
    output_audio_filename = output_filename + "_audio.mp3"

    clip = VideoFileClip(input_video_path)
    audio = clip.audio
    audio.write_audiofile(output_audio_filename, codec="mp3")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_audio.py <input_video_path>")
        sys.exit(1)

    process_video(sys.argv[1])
