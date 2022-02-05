import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speake3

print('Initilatization jarvis')
engine = speake3.Speake() # Initialize the speake engine")
engine.set('voice', 'en')
engine.set('speed', '170')
engine.set('pitch', '99')
engine.say("Hello world!")
engine.talkback()
