import os 
import shutil 
import pyttsx3

from voice.settings import BASE_DIR, PROJECT_ROOT
def tts(transcript, voicetype):
    print(BASE_DIR,'here')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    if(voicetype=='1'):      #getting details of current voice
        engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
    else:
        engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(transcript)   #plays the voice-over
    engine.save_to_file(transcript, 'speech.mp3') #save the file to speech.mp3
    engine.runAndWait()
    shutil.move(str(BASE_DIR)+"\speech.mp3",str(BASE_DIR)+"\static\speech.mp3") #moves the file
    return