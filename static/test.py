import ffmpeg
import sys
import os
path = 'C:/Users/tripa/Downloads/ffmpeg-n4.4-latest-win64-gpl-4.4/bin'
os.environ['PATH'] += ';'+path

sys.path.insert(0,'C:/Users/tripa/Downloads/ffmpeg-n4.4-latest-win64-gpl-4.4/bin')
input_video= ffmpeg.input('video.mp4')
input_audio=ffmpeg.input('songname.mp3')
input_video = ffmpeg.output(input_audio.audio,input_video.video,'input_video.mp4')
ffmpeg.run(input_video)



