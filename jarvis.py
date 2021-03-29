import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python.
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(str(date)+" "+str(month)+" "+str(year))

def greet():
    speak("Welcome back my lord")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning my lord")
    elif hour >=12 and hour<18:
        speak("Good afternoon my lord")
    elif hour >=18 and hour<24:
        speak("Good evening my lord")
    else:
        speak("Good night my lord")
    speak("Tnavis at your service!please tell me how can i help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
    
    except Exception as e:
        print(e)
        speak("Pardon! Say that again please ")
        return "None"
    return query

def sendEmail(to,content):
    try:
        server =smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("kingstarr1361@gmail.com","sivant9994532266")
        server.sendmail("kingstarr1361@gmail.com",to,content)
        server.close()
    except:
        speak("Sorry! mail not sent")

def screenshot():
    img=pyautogui.screenshot()
    img.save(".\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at "+usage)
    battery=str(psutil.sensors_battery().percent)
    speak("battery is at "+battery)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    greet()
    while True:
        query =takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)
        elif "send email" in query:
            speak("what should i say?")
            content = takeCommand()
            to="sivant1313@gmail.com"
            sendEmail(to, content)
            speak(content)
            speak("Email sent!")
        elif "search in chrome" in query:
            speak("what should i search?")
            path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(path).open_new_tab(search)
        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember that,"+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak(remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        elif "good job" in query:
            speak("Thank you my lord")
        elif "bye" in query:
            speak("Good bye my lord! have a great day")
            quit()