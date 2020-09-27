import speech_recognition as sr
import webbrowser
from time import ctime
import time
import os
from gtts import gTTS
import playsound
import random

r = sr.Recognizer()


def record_audio():
    with sr.Microphone as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('Sorry, dont understand')

        except sr.RequestError:
            print('Sorry, Service is Down')

        return voice_data

def respond(voice_data):
    if 'What is your name' in voice_data:
        i = input()
        print('My name is' + i)

    if 'What Time is it' in voice_data:
        print(ctime())

    if 'search' in voice_data:
        search = record_audio('What are you searching for?')
        url = 'https://www.google.com/?q=' + search
        webbrowser.get().open(url)
        print('here you go'+ search)

    if 'Find Location' in voice_data:
        location = record_audio('Where am I?')
        url = 'https://www.google.com/maps/@23.6013305,89.8411966,14z/places' + location
        webbrowser.get().open(url)
        print('You are here'+ location)

    if 'exit' in voice_data:
        exit()


time.sleep(2)
print('How Can I Help You?')
while 2:
    voice_data = record_audio()
    respond(voice_data)