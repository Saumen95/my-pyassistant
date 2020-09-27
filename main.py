import speech_recognition as sr
import webbrowser
from time import ctime
import time
import os
from gtts import gTTS
import playsound
import random



r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            speak('Sorry, dont understand')

        except sr.RequestError:
            speak('Sorry, Service is Down')

        print(f">> {voice_data.lower()}")

        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(f"kiri: {audio_string}")
    os.remove(audio_file)



def respond(voice_data):
    with sr.Microphone as source:
        audio = r.listen()
        voice_data = audio
        if 'what is your name' in voice_data:
            speak(audio)

        if 'what time is it' in voice_data:
            speak(ctime())

        if 'search' in voice_data:
            search = record_audio('what are you looking for?')
            url = 'https://www.google.com/serch?q=' + search
            webbrowser.get().open(url)
            speak('here you go' + search)

        if 'Find location' in voice_data:
            location = record_audio('where am I?')
            url = 'https://www.google.com/maps/@23.6013305,89.8411966,14z' + location
            webbrowser.get().open(url)
            speak('Here you are' + location)

        if 'exit' in voice_data:
            exit()



time.sleep(2)
speak('How Can I Help You?')
while 2:
    voice_data = record_audio()
    respond(voice_data)