import pyttsx3

import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia

engine = pyttsx3.init()
engine.say("Welcome Friends on new page! This is JARVIS, AI Assistant.")
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("This is JARVIS! Your AI Assistant.")
##############################################################


## Time Function in Python
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)


time()


###############################################################
###Date Function
def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)


date()


############################################################################
## Greetings
def wishme():
    speak("Welcome back: Hopefully you are good.")
    speak("the current time is:")
    time()
    speak("the today date is:")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 1200:
        speak("Good morning: How is the morning?")
    elif hour >= 1200 and hour < 1800:
        speak("Good afternoon: Enjoying the day")
    elif hour >= 1800 and hour < 2400:
        speak("Good evening")
    else:
        speak("Good night")
    speak("JARVIS at your service; please tell me how can I help you")


wishme()


##################################################################################
### Take command from user voice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "None"
    return query


#####################################################################
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "offline" in query:
            quit()
####################################################################
