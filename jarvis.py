import time
from urllib import request
import pyttsx3 as pyttsx
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import smtplib
import pyjokes
import pywhatkit
import pyautogui
import requests


engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
# engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    elif hour>=18 and hour<21:
        speak("Good Evening sir")
    else:
        speak("Welcome sir")

    speak("I am Jarvis. How can I help you?")

def takeCommand():
    #it takes microphone input and returns string output
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
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=e63c9253799c47d9908d8c8dbd47a7b9"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    for ar in articles:
        head.append(ar["title"])
    speak("Here are today's top 5 news for you sir")
    for i in range (5):
        speak(head[i])


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.connect("smtp.example.com",465)
    server.ehlo()
    server.startls()
    server.login('pulakkumarghosh2001@gmail.com', 'Pulak@2001')
    server.sendmail('pulakkumarghosh2001@gmail.com', to, content)
    server.close( )

if __name__ == '__main__':
    # speak("Rajibul is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoriding to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'play music' in query:
            cinema_dir = "E:\\Sonu Ke Titu Ki Sweety (2018) HDRip 720p Hindi H.264 ACC 2.0 - LatestHDMovies"
            cinema = os.listdir(cinema_dir)
            print(cinema)
            os.startfile(os.path.join(cinema_dir, cinema[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'email to pulak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ghoshpulak2901@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("try again")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'play' in query:
            song = query.replace('play', ' ')
            pywhatkit.playonyt(song)

        elif 'search' in query:
            search = query.replace('search', ' ')
            pywhatkit.search(search)

        elif 'quit' in query:
            speak("Thank you Sir, Have a good day...")
            exit()

        elif 'shut down' in query:
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            os.system("shutdown /r /t 5")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "news" in query:
            speak("Getting the news for you sir")
            time.sleep(1)
            speak("Just a second sir")
            time.sleep(1)
            news()
