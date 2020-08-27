# The design of virtual assistant

import random
import os
import datetime, calendar

import wikipedia
import speech_recognition as sr
from gtts import gTTS
from va_utils import recordAudio, vaSpeechResponse, vaWakeUpCall, getInfoFromWikipedia
from playsound import playsound

speech_text = None

while True:
    speech_text = recordAudio()
    #print(speech_text)

    #wake_call = vaWakeUpCall(speech_text)
    #if wake_call is True:
    #    print("I am awake")

    if speech_text is not None:
        wiki_info = getInfoFromWikipedia(speech_text)
        #test_text = "This is spaaarta!"
        vaSpeechResponse(wiki_info)