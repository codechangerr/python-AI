from ctypes import oledll
import ctypes
import pyaudio
import pyttsx3
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import random as r

OlexVoice = pyttsx3.init()

rate = OlexVoice.getProperty('rate')

OlexVoice.setProperty('rate', 146)

volume = OlexVoice.getProperty('volume')

OlexVoice.setProperty('volume', 1.0)

voices = OlexVoice.getProperty('voices')
OlexVoice.setProperty('voice', voices[1].id)

OlexVoice.say("started monkey AI. use wakeword monkey")

OlexVoice.runAndWait() 

#waits for the wakeword
while True:
    def getaudio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("" + str(e))

        return said
    
    text = getaudio()

    if "monkey" in text:
        
        #will start to get audio again when the wake word is siad
        def get_command():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""

                try:
                    said = r.recognize_google(audio)
                    print(said)
                except Exception as e:
                    OlexVoice.say("sorry didnt hear or get that." + str(e))
                    OlexVoice.runAndWait()

            return said
        OlexVoice.say("ready. you may speak")
        OlexVoice.runAndWait()
        text=get_command()
        
        if 'hello' in text:
            OlexVoice.say("hello")
            OlexVoice.runAndWait()

        if 'are you always listening' in text:
            OlexVoice.say("yes")
            OlexVoice.runAndWait()
        if "who's Candice" in text:
            OlexVoice.say("candice dick fit in ur mouth")
            OlexVoice.runAndWait()
        if "I'm offended" in text:
            OlexVoice.say("shut the fuck up no one cares that your offended.")
            OlexVoice.runAndWait()
        if "can you help me with my math homework" in text:
            OlexVoice.say('no you dumb ass mother fucker do it yourself')
            OlexVoice.runAndWait()
        
        if "are you sending what I say to the government" in text:
            OlexVoice.say("no")
            OlexVoice.runAndWait()
        if "good morning" in text:
            OlexVoice.say("good morning.")
            OlexVoice.runAndWait()
        if "write this down" in text:
            OlexVoice.say("what is it you want to write down")
            OlexVoice.runAndWait()
        
            text = get_command()
            tts = gTTS(text=text, lang ="en")
            filename = 'reminders.mp3'
            tts.save(filename)
            OlexVoice.say('ok. done')
            OlexVoice.runAndWait()
            
        if "what do I have today" in text:
            os.system('reminders.mp3')

        if "search" in text:
            OlexVoice.say("ok. search what")
            OlexVoice.runAndWait()
            import wikipedia as wik
            import ctypes
            stuff = get_command()
            result = wik.summary(stuff)
            OlexVoice.say("ok here's what I found")
            OlexVoice.runAndWait()
            OlexVoice.say(result[:400])
            OlexVoice.runAndWait()
        if "911 find" in text:
            OlexVoice.say("whats the persons email you want to find")
            OlexVoice.runAndWait()
