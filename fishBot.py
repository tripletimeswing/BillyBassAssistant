#set environment
import os
from dotenv import load_dotenv
load_dotenv()

import wakeWord
import voiceRec
import textGen
import voiceGen
import wavConvert
import mouth

def chat():
    detected = wakeWord.wakeWord()
    #currently set to "Billy bass"

    while (detected == True):
        #inside loop iteration
        query = voiceRec.speechRec()
        print(query)

        try:
            if (query is not None):
                #call text
                response = textGen.textResponse(query)
                #prints fish response
                print(response)
                #call tts
                voiceGen.t2s(response)
                #convert to wav
                wavConvert.convertAudio()
                #play and control motor
                mouth.controlMouth()

        except Exception as e:
            print("error occured: ", e)
        finally:
            detected = False

while True:
    chat()
    #restart
    restart = input("\nContinue program? (y/n): ").strip().lower()
    if restart != "y":
        break #exit code