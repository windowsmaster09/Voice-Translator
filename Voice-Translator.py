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
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="None")#In place of None, put the initials of the speech recognition language. You will be able to see your initials here https://py-googletrans.readthedocs.io/en/latest/. After that, the program will accept English and the language you entered.
            command = command.lower()
    except:
        command = ""
    return command

counter = 0

def run_translator():
    os.system('cls')
    global counter
    counter += 1
    f = open("chat.txt", "a+", encoding="utf-8")
    if os.path.getsize("chat.txt") > 0:
        f.write(f"\n\nTranslation {counter}\n")
    else:
        f.write(f"Translation {counter}\n")
    f.close()
    print('Do you want to translate a word or end the program?')
    talk('Do you want to translate a word or end the program?')
    f = open("chat.txt", "a+", encoding="utf-8")
    f.write("\nBot: Do you want to translate a word or end the program?")
    f.close()
    command = take_command()
    print(command)
    f = open("chat.txt", "a+", encoding="utf-8")
    f.write(f"\nUser: {command}")
    f.close()
    if "None" in command or "translate" in command:#Instead of None, you can put a word that is in the language you entered on line 22.
        print('listening...')
        talk('listening...')
        f = open("chat.txt", "a+", encoding="utf-8")
        f.write("\nBot: listening...")
        f.close()
        command = take_command()
        f = open("chat.txt", "a+", encoding="utf-8")
        f.write(f"\nUser: {command}")
        f.close()
        translation = translator.translate(command, dest="en")
        print(command, "-->", translation.text)
        talk(translation.text)
        f = open("chat.txt", "a+", encoding="utf-8")
        f.write(f"\nBot: {command} --> {translation.text}")
        f.close()
        print("Do you want to repeat or spell out?")
        talk("Do you want to repeat or spell out?")
        f = open("chat.txt", "a+", encoding="utf-8")
        f.write("\nBot: Do you want to repeat or spell out?")
        f.close()
        command = take_command()
        f = open("chat.txt", "a+", encoding="utf-8")
        f.write(f"\nUser: {command}")
        f.close()
        if "repeat" in command or "None" in command:#Instead of None, you can put a word that is in the language you entered on line 22.
            print(command)
            talk(translation.text)
        elif "spell out" in command or "None" in command:#Instead of None, you can put a word that is in the language you entered on line 22.
            print(command)
            spelled_text = ", ".join(list(translation.text))
            talk(spelled_text)
            f = open("chat.txt", "a+", encoding="utf-8")
            f.write(f"\nBot: {spelled_text}")
            f.close()
        elif "no" in command or "None" in command:#Instead of None, you can put a word that is in the language you entered on line 22.
            print(command)
            run_translator()
    elif "None" in command or "end" in command:#Instead of None, you can put a word that is in the language you entered on line 22.
        exit()

while True:
    run_translator()
