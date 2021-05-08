import speech_recognition as sr
import pyttsx3
assistant = sr.Recognizer()
engine = pyttsx3.init()
def talk():
    engine.say("Welcome")
    engine.say("How may I help you")
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            voice = assistant.listen(source)
            command = assistant.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
def run_redeemer():
    command = take_command()
    if "play" in speak.split()[:1]:
        print("Playing")
talk()
take_command()
