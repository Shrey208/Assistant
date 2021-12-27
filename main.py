import os
import smtplib
import pyttsx3 
import datetime
import wikipedia  
import webbrowser
import speech_recognition as sr  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Shreyansh how are you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Shreyansh how are you")
    else:
        speak("Good Evening! Shreyansh how are you")
    speak("I am friday. Please tell me how may I help you")
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
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shreyanshgupta208@gmail.com', 'your-password')
    server.sendmail('shreyanshgupta208@gmail.com', to, content)
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
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'exit' in query:
            quit()
        elif 'email to Shreyansh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shreyanshgupta208@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")