from gtts import gTTS
import playsound3

def t2s(response):
    filename = "voice.mp3"

    def speak(text, filename):
        tts = gTTS(text= text, lang= "nl")
        tts.save(filename)

    def play(filename):
        playsound3.playsound(filename)

    def voiceGen(speech, filename):
        speak(speech, filename)
        play(filename)

    voiceGen(response, filename)