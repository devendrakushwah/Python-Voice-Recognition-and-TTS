import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def text_to_speech(text):
  try:
    tts=gTTS(text=text,lang='en')
    tts.save('new.mp3')
    print('Playing sound.....')
    playsound.playsound('new.mp3', True)
  except:
    print('Handle Exception')
    pass

def speech_to_text():
  
  r=sr.Recognizer()
  
  with sr.Microphone() as source:
    print('Say something')
    audio=r.listen(source)
    print('Done listening')
  try:
    s=(r.recognize_google(audio))
    print('You said -> ',s)
  except:
    print('Handle Exception')
    pass

#Driver
if __name__=='__main__':
  speech_to_text()
  text_to_speech('This is awesome')  
