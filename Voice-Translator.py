import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import os

translator = Translator()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="None") #In place of None, put the initials of the speech recognition language. You will be able to see your initials here https://py-googletrans.readthedocs.io/en/latest/. After that, the program will accept English and the language you entered.
            command = command.lower()
            
    except:
        pass
    return command


def run_whisper():
    command = take_command()
    print(command)
    if "None" in command or "translate" in command: #Instead of None, you can put a word that is in the language you entered on line 22.
        command = take_command()
        translation = translator.translate(command, dest="en")
        print(command, "-->", translation.text)
        talk(translation.text)
        os.system('cls')
    elif "None" in command or "end" in command: #Instead of None, you can put a word that is in the language you entered on line 22.
        os.system('cls')
        exit()

while True:
    run_whisper()
