import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import espeak
espeak.init()
speaker = espeak.Espeak()
speaker.say("Hello world")
speaker.rate = 300
speaker.say("Faster hello world")