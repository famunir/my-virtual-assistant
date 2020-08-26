# The design of virtual assistant

import random
import os
import datetime, calendar

import wikipedia as wiki
import speech_recognition as sr
from gtts import gTTS
from va_utils import recordAudio, vaSpeechResponse
from playsound import playsound

recordAudio()
test_text = "This is spaaarta!"
vaSpeechResponse(test_text)