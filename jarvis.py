import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good evening')
    speak('I am Hazel....Whats up!!')


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


if __name__ == "__main__":
    wishMe()
    query = ""
    while(not("thank you" in query)):
        query = takeCommand().lower()  # to match it with our command

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
            speak('You can thank me for me to stop')
        elif 'thank you' in query:
            speak('Glad to help you....You know where to find me')
        elif 'tony stark' in query:
            speak('He is the creater of my arch nemesis')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            webbrowser.open('music.youtube.com/')
        # elif 'let\'s study' in query:                  #ERROR in this method /permission denied
        #    dir = 'D:\\study'
        #    os.open(dir,os.O_RDONLY)
        else:
            speak('Can you say that  again please')
