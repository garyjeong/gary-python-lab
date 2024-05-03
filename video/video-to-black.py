# 코드를 통해서 비디오를 검정 화면 처리
import os
import sys
from moviepy.editor import VideoFileClip, ColorClip


def process_video(input_video_path: str) -> None:
    output_filename, _ = os.path.splitext(input_video_path)
    output_filename = output_filename + "_convert.mp4"

    clip = VideoFileClip(input_video_path)
    black_clip = ColorClip(size=clip.size, color=(0, 0, 0), duration=clip.duration)
    black_clip = black_clip.set_audio(clip.audio)
    black_clip.write_videofile(output_filename, codec="mpeg4")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python video-to-black.py <input_video_path>")
        sys.exit(1)

    input_video_path = sys.argv[1]
    process_video(input_video_path)
