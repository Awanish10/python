
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('Initilatization jarvis')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set properties _before_ you add things to say
engine.setProperty('rate', 170)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

engine.setProperty('voice', 'english_rp+f3') 

engine.say(''' hey darling how. are you ''')
i=1
for voice in voices:
    print(i)
    i=i+1
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    
#rint(voices)
engine.runAndWait()
#engine.say(" hey adarsh ")
#engine.runAndWait()



