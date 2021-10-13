import speech_recognition as sr
import pyttsx3
import datetime

print('Loading your AI personal assistant - G One')

engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


if __name__ == '__main__':

    speak("Loading your Converter")
    wishMe()
    speak("Enter the file name where you want to enter speech")
    file_name = input("Enter the file name :-  ")
    f = open(file_name+".txt", "a+")
    r = sr.Recognizer()
    source = sr.Microphone()
    while True:
        speak("tell next line to enter or say goodbye to stop program")
        print("Listening...")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            try:
                statements = r.recognize_google(audio)
                print(f"user said:{statements}\n")

            except Exception as e:
                print(e)
                speak("Pardon me, please say that again")
                statements = None

        if statements:
            statements = statements.lower()
            if ("goodbye" in statements) or ("bye" in statements):
                speak('your Converter shutting down,Good bye')
                print('your Converter is shutting down,Good bye')
                exit(0)
            else:
                # f.write(statements)
                print(statements, file=f)
