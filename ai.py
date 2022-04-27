import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui

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

    speak("I am KLAW. Please tell me how may I help you")       

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail', 'your pass')
    server.sendmail('your mail', to, content)
    server.close()

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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")


        elif 'email to bill' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyzemail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 

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
        
        elif 'school site' in query:
            webbrowser.open('your school site')
        
        elif 'old songs' in query:
            speak('opening')
            print('opening...')
            webbrowser.open('https://www.youtube.com/results?search_query=old+songs')
            
        elif 'introduce yourself' in query:
            speak("I am KLAW. A very high profiled ai voice assistant developed by Cisco a k a manas kishore")
        
        elif 'repeat' in query:
            speak('now speak')
            s = takeCommand()
            speak(s)

        

        