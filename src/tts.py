from gtts import gTTS
import os
from tiktokvoice import tts


# TODO: replace gTTS with TikTok standard voice

def speak(text):
    voice = 'en_us_009'
    tts(text, voice, "../assets/tts/tts.mp3", play_sound=True)
