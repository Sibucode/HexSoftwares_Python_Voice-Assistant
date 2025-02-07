
from dis import Instruction
import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
import os
import requests

listener = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

text = "Hi there! How can I help you?"
print(text)
talk(text) 


def input_instruction():
    while True:
        try:
            with sr.Microphone() as origin:
                print("Say something....")

                speech = listener.listen(origin)
                instruction = listener.recognize_google(speech)
                instruction = instruction.lower()

                print(f"You said: {instruction}")
                print()
                return instruction



        except sr.UnknownValueError:
              print("Sorry, I didn't understand that. Please try again.")
              talk("Sorry, I didn't understand that. Please try again.")
              print()

        except sr.RequestError:
            print("There was an issue with the speech recognition service. Check your connection.")
            talk("There was an issue with the speech recognition service. Check your connection.")
            return None  # Return None if there's a connection issue

        except Exception as e:
            print(f"An error occurred: {e}")
            talk("An error occurred. Please try again.")

       
        
        
          
def open_app(app_name):
    """Open specified applications."""
    apps = {
        "outlook": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
        "notepad": "notepad.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    }
    if app_name in apps:
        talk(f"Opening {app_name}")
        os.startfile(apps[app_name])
    else:
        talk(f"Sorry, I don't know how to open {app_name}")

def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why did the computer catch a cold? Because it left its Windows open!",
        "I told my computer I needed a break, and now it won't stop sending me vacation ads!",
        "Why do programmers prefer dark mode? Because the light attracts bugs!"
    ]
    joke = random.choice(jokes)
    print(joke)
    talk(joke)

def find_restaurants():
    """Opens Google Maps to show nearby restaurants."""
    talk("Looking for restaurants near you.")
    webbrowser.open("https://www.google.com/maps/search/restaurants+near+me")

def play_Tom():
   
    instruction = input_instruction()
    print(instruction)

    if "play" in instruction:
        song = instruction.replace('play', " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        print("Current time is: " + time)
        talk('current time is' + time)
        

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        talk("Today's date is: " + date)
        print("Current date is: " + date)
        
        

    elif 'how are you' in instruction:
        talk("I am fine thanks and how are you")
        


    elif 'your name' in instruction:
        talk('My name is Jabu and I am your virtual assistant, How can I help you my friend')
       



    elif "who is" in instruction or "what is" in instruction:
        try:
            human = instruction.replace('who is', "").replace('what is', "")
            info = wikipedia.summary(human, sentences=1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results for that. Please be more specific.")

    elif "open" in instruction:
        app_name = instruction.replace("open", "").strip()
        open_app(app_name)

    elif "search for" in instruction:
        query = instruction.replace("search for", "").strip()
        talk(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "joke" in instruction:
        tell_joke()

    elif "find restaurants" in instruction or "place to eat" in instruction:
        find_restaurants()

    else:
        talk("Sorry, I don't recognize that command. Please try again.")

  

    print()
        
    play_Tom()
    

    
 
       
       
play_Tom()







