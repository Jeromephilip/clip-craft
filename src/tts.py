from gtts import gTTS
import os

# TODO: replace gTTS with TikTok standard voice

def speak(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("../assets/tts/tts.mp3")
