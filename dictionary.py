import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
        
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    
    else:
        speak('Good evening') 
    speak('I am Hazel....what are you searching for?')
def takeCommand():
    '''
    it takes microphone input from the user and returns a string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print('user said :', query)
        
    except Exception as e:
        print(e)
        print('Say that again please....')
        return "None"
    return query
    
     
if __name__ =="__main__":
    wishMe()
    print('1)Say one word to find the meaning of it\n2)say "yes" if you got what you are looking for and "no" if you didn\'t 3)say "thank you" for exiting ')
    query =""
    satisfied = ""
    while(True):
        query = takeCommand().lower() #to match it with our command
        speak(dictionary.meaning(query))
        print(dictionary.meaning(query))
        speak('did you get what you are looking for?')
        satisfied = takeCommand().lower()
        if 'yes' in satisfied:
            speak('glad i could help')
            break
        elif 'no' in satisfied:
            speak('ohhh.... I am sorry, can you repeat that')
            continue
        else:
            speak('i\'m sorry i did not get that')
            
