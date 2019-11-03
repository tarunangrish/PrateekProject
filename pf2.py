import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('nsss') #For windows use 'sap5'
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour <=17:
        speak("good Afternoon")

    elif hour>17 and hour<22:
        speak("Good Evening")
    
    else:
        speak("Good Night")
    
    speak("My name is vikram, sir. How may I help you?")
    speak("Mr. bhola what is the price of the blouse")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold =1

        audio = r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Sorry, sir. I couldn't recognize what you said.")
        return "None"
         
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    seever.login('youremail@gmail.com', 'your-password-here') # Enter your email ID and password here
    server.sendmail('youremail@gmail.com', to, content) #Enter your email ID here
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'play some music' in query:
            music_dir ='' #enter directory for music 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'note this down' in query:
            noteUp = "" #Enter the process directory for notepad here
            os.startfile(noteUp)

        elif 'send an email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = content
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry, the email couldn't be sent.")
