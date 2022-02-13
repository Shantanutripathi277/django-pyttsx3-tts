import ffmpeg
import sys
import os
path = 'C:/Users/tripa/Downloads/ffmpeg-n4.4-latest-win64-gpl-4.4/bin'
os.environ['PATH'] += ';'+path
sys.path.insert(0,'C:/Users/tripa/Downloads/ffmpeg-n4.4-latest-win64-gpl-4.4/bin')
def handle_uploaded_file(f):
    with open('T:/STUDY/ME/Fosee/django/voice/static/video.mp4', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)        
    input_video= ffmpeg.input('T:/STUDY/ME/Fosee/django/voice/static/video.mp4')
    input_audio=ffmpeg.input('T:/STUDY/ME/Fosee/django/voice/static/songname.mp3')
    input_video = ffmpeg.output(input_audio.audio,input_video.video,'T:/STUDY/ME/Fosee/django/voice/static/input_video.mp4')
    ffmpeg.run(input_video)
    return



