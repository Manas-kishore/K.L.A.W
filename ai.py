import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 178)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am claw. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'shut down' in query:
            speak('shutting down')
            os.system("poweroff")

        elif 'shutdown' in query:
            speak('shutting down')
            os.system("poweroff")

        elif 'close yourself' in query:
            speak('thanks for using me')
            print('Quiting...........')
            break

        elif 'how are you' in query:
            speak('i am fine! what about you, sir')
            
        elif 'introduce yourself' in query:
            speak("I am claw. A very high profiled ai voice assistant developed by Cisco a k a manas kishore")
        
        elif 'repeat' in query:
            speak('now speak')
            s = takeCommand()
            speak(s)

        elif 'ecosystem' in query:
            speak('a biological community of interacting organisms and their physical environment')        
