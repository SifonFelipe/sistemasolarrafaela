import sys
from os import system
from pathlib import Path


def achicar_video(video_path):
    small_video_path = video_path.replace('.mp4','_small.mp4')
    cmd = f"ffmpeg -i '{video_path}' -vcodec libx264 -crf 28 -preset veryfast -acodec aac -b:a 128k '{small_video_path}'"
    system(cmd)
    system(f"rm '{video_path}'")
    system(f"mv '{small_video_path}' '{video_path}'")


def achicar_muchos(dir_path):
    for f in Path(dir_path).glob("*.*"):
        print(f)
        achicar_video(str(f))
