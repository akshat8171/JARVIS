import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as wb
import os
import smtplib
import selenium
chrome_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


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
        speak("Good Evening! ")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)        
        r.pause_threshold = 1
        r.energy_threshold=500
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language="en-in")
        query=query.lower()
        print(query)
        if( 'jarvis' in query ):
            speak("ok sir")
            print("User Said : ", query)
        else:
            speak("Say that again please")
            return("None")
    except Exception as e:
        speak("Say that again please")
        print("Say that again please...")  
        return ("None")
    return(query)
def continuecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=2000
        audio = r.listen(source)
    try:

        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        speak("ok sir")
        print(query)

    except Exception as e:
        speak("Say that again please")
        print("Say that again please...")  
        return ("None")
    return(query)
def stopcommand():
    query=""
    while("jarvis" not in query):
        print(query)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)        
            r.pause_threshold = 1
            r.energy_threshold=500
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            query=query.lower()
            print(query)
        except Exception as e:
            print('no')
            pass
    return
 

    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akshtkingggg@gmail.com', '9412316103')
    server.sendmail('akshtkingggg@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        query=query.replace("jarvis","")
        if query=="None":
            continue
        elif "hi" in query or "hello" in query:
            speak("Hello akshat")
        elif "stop" in query:
            speak("wake me up by saying  jarvis")
            stopcommand()
            speak("i am awake sir")        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'search' in query:
            query=query.replace('search','')
            query=query.replace('Jarvis','')
            query=query.replace('jarvis','')
            wb.open_new_tab('https://www.google.com/search?source=hp&ei=xhHoXNviIMjJrQHyvonQAw&q='+query)

        elif 'open' in query and 'youtube' in query:
            speak("which video you want to play")
            while(True):
                if(query=="None"):
                    continue
                else:
                    query=continuecommand().lower()
                    print(query)
                    try:
                        query=query.replace("play","")
                    except:
                        query=query
                    wb.open_new_tab("https://www.youtube.com/results?search_query="+query)
                    break
        elif 'open google' in query:
            wb.open_new_tab("http://www.google.com")

        elif 'open stackoverflow' in query:
            wb.open_new_tab("http://www.stackoverflow.com")
        elif'open codeforces' in query:
            wb.open_new_tab("http://www.codeforces.com")
        elif 'open codechef' in query:
            wb.open_new_tab("http://www.codechef.com")
        elif 'open hackerearth' in query:
            wb.open_new_tab("http://www.hackerearth.com")
        elif 'open whatsapp' in query:
            wb.open_new_tab("https://web.whatsapp.com")
            
            

        elif 'open python' in query :
            python='C:\\Users\\akshat garg\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib\\idle.pyw'
            os.startfile(python)
        elif 'close python' in query:
            os.system("TASKKILL /F /IM pythonw.exe")

            
        elif 'open spotify' in query :
            spotify='C:\\Users\\akshat garg\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(spotify)
        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM spotify.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")


        elif 'play songs' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "agarwalmuskan9808@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'shutdown' in query:
            speak("Bye bye sir")
            os.system("shutdown /s /t 1")
        elif'restart' in query:
            speak("come in a while")
            os.system("shutdown /r /t 1")
    
