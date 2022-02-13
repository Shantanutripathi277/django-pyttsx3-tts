import os 
import shutil 
import pyttsx3
''' TODO-
change static path to relative path
home page -routing
video player
session control
submit button sahi krni hogya
male female hogya
code saaf
css
testing
'''
def tts(transcript, voicetype):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    if(voicetype=='1'):      #getting details of current voice
        engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
    else:
        engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(transcript)
    engine.save_to_file(transcript, 'songname.mp3')
    engine.runAndWait()
    shutil.move("T:/STUDY/ME/Fosee/django/voice/songname.mp3","T:/STUDY/ME/Fosee/django/voice/static/songname.mp3")
    return