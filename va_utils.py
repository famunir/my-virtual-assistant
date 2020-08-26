import random
import os
import datetime, calendar

import wikipedia as wiki
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# This method wakes up the virtual assitant
def vaWakeUpCall(text_data):
    text = text_data.lower()
    wake_phrase = ["hello system"]
    if wake_phrase in text:
        return True
    else:
        return False

# This method fetches the datatime
def getDateTime():
    my_time = datetime.datetime.now()
    my_date = datetime.datetime.date()
    my_day = calendar.day_name([my_date.weekday()])
    my_month = my_time.month
    my_daynumber = my_time.day

    return None


# This method opens the microphone and records the audio
def recordAudio():
    # defining the recognizer object
    record = sr.Recognizer()

    with sr.Microphone() as speaker:
        print("Assistant: Please talk to me!")
        audio = record.listen(speaker)

    audio_data = ""

    try:
        audio_data = record.recognize_google(audio)
        print("You:" , audio_data)
    except sr.UnknownValueError():
        print("unable to understand the speaker: Unknown Error!")
    except sr.RequestError() as e:
        print(e)

    return audio_data

# This method converts the text response to speech response.
def vaSpeechResponse(text_data):
    speech = gTTS(text = text_data, lang = 'en', slow = False)
    speech.save('va_response/assistant_speech_response.mp3')
    #os.system('start va_response/assistant_speech_response.mp3')
    playsound('va_response/assistant_speech_response.mp3')