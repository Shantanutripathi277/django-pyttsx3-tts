import ffmpeg
import sys
import os
from voice.settings import BASE_DIR
path = os.path.join(BASE_DIR,'ffmpeg-n4.4-latest-win64-gpl-4.4','bin')
print(os.path.join(BASE_DIR,'static'))
os.environ['PATH'] += ';'+path
sys.path.insert(0,os.path.join(BASE_DIR,'ffmpeg-n4.4-latest-win64-gpl-4.4','bin'))
def handle_uploaded_file(f,title):
    with open(os.path.join(BASE_DIR,'static','video.mp4'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)        
    input_video= ffmpeg.input(os.path.join(BASE_DIR,'static','video.mp4'))
    input_audio=ffmpeg.input(os.path.join(BASE_DIR,'static','speech.mp3'))
    input_video = ffmpeg.output(input_audio.audio,input_video.video,os.path.join(BASE_DIR,'static',title,)+'.mp4')
    ffmpeg.run(input_video)
    return
