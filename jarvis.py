import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# pipprint(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)  # Audio is content which jarvis will speak
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogning...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia... Please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube, happy watching!")

        elif 'open w3schools' in query:
            webbrowser.open("https://www.w3schools.com/")
            speak("opening w3schools, happy learning!")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("Opening stackoverflow, happy learning!")

        elif 'open geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
            speak("Opening geeksforgeeks, happy learning!")

        elif 'open news' in query:
            webbrowser.open(
                "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
            speak("Opening google news")

        elif 'open pac-man' in query:
            webbrowser.open("https://www.google.com/search?q=pacman&rlz=1C1CHZN_enIN924IN924&ei=wlaZZOeBGdP6hwP1_pPoCA&gs_ssp=eJzj4tZP1zc0MjQwNDRMMWD0YitITM5NzAMANqUFhw&oq=pac&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMg0ILhCKBRCxAxCDARBDMg0IABCKBRCxAxCDARBDMgcILhCKBRBDMgcILhCKBRBDMggILhCABBCxAzIFCAAQgAQyCwguEIAEEMcBEK8BMgsILhCABBCxAxCDATIICAAQgAQQyQMyCAgAEIAEEJIDMhsILhCKBRCxAxCDARBDEJcFENwEEN4EEOAEGAE6BwgAEIoFEEM6BQguEIAEOgoILhCKBRDUAhBDOgsIABCABBCxAxCDAUoECEEYAFAAWMEDYJoUaABwAXgAgAGuAYgB2wOSAQMwLjOYAQCgAQHAAQHaAQYIARABGBQ&sclient=gws-wiz-serp")
            speak("Opening pacman")

        elif 'open amitranet' in query:
            webbrowser.open("https://aisn.amizone.net/")
            speak("Opening amitranet")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            speak("Opening gmail")

        elif 'open lms' in query:
            webbrowser.open(
                "https://aisn.amizone.net/StudentLogin/StudentLogin")
            speak("Opening lms")

        elif 'open get hub' in query:
            webbrowser.open("https://github.com/")
            speak("Opening github")

        elif 'open chatting website' in query:
            webbrowser.open("https://dpingo.github.io/Kwitter/index.html")
            speak("Opening Kwitter")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'open  code' in query:
            codePath = "C:\\Users\\japji\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code, happy Coding!")
            os.startfile(codePath)

        elif 'open ppt' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            speak("Opening Power Point")
            os.startfile(code_path)

        elif 'open excel' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            speak("Opening Excel")
            os.startfile(code_path)

        elif 'open word' in query:
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening word")
            os.startfile(code_path)

       # elif 'email to anmol' in query:
            # try:
            #  speak("What should I say?")
            #  content = takeCommand()
            # to = "anmolkaur.kalra@ais.amity.edu"
            # sendEmail(to, content)
            # speak("Email has been sent!")

            # except Exception as e:
            # print(e)
            # speak("Apologies! I am not able send this email")
