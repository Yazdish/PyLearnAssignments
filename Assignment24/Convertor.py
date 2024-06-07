import time
from moviepy import editor

start_time = time.time()

def vid_to_aud(video, audio):
    video = editor.VideoFileClip(video)
    video.audio.write_audiofile(audio)

paths = [
    ["video/Video1.mp4", "Audio/Audio1.mp3"],
    ["video/Video2.mp4", "Audio/Audio2.mp3"],
    ["video/Video3.mp4", "Audio/Audio3.mp3"],
    ["video/Video4.mp4", "Audio/Audio4.mp3"],
    ["video/Video5.mp4", "Audio/Audio5.mp3"]
]

for file, name in paths:
    # print(file, name)
    vid_to_aud(file, name)

end_time = time.time()

print("execution time: ", end_time - start_time)