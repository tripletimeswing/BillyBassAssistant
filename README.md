# Billy Bass Assistant
The Billy Bass Assistant is a voice-based artificial inteligence chatbot ran on a Raspberry Pi. It transform the singing Billy Bass toy into an interactive smart assistant capable of listening, thinking, speaking and reacting by combining Pico Voice's Porcupine, Groq's LLama, and ElevenLabs text-to-speech.


https://github.com/user-attachments/assets/cf363afb-d33a-4abf-9209-668e9805cda8

# Bill of Materials
1. Raspberry Pi 4
2. Big Mouth Billy Bass toy
3. Speaker
4. 3.5mm aux cable
5. INMP441
6. 9V Battery
7. 2N2222 NPN Transistor
8. 220 Ohm Resistor
9. 10μF capacitor
10. Jumper Wires
11. Breadboard connectors

# Schematics
<img width="733" height="657" alt="BillyBassSchema" src="https://github.com/user-attachments/assets/90a88929-1741-4af9-8a34-960897c9feb1" />

# Hardware Setup
### 1
Connect the transistor and microphone module on a breadboard.
![1000005369](https://github.com/user-attachments/assets/214a0c3c-7413-4cf8-b36a-ac0ec06b46ca)

### 2
Open back of Billy Bass toy and cut and strip motor wires, test with a battery to see which wire for which motor.

### 3
Connect motor to transistor. If body motor is still working, use a dual H-bridge like l293d to use both motors. (Code is not made for 2 motors)

### 4
Connect external speaker to RPi through aux or alternatively use speaker from toy by soldering it to aux adapter.

# Raspberry Pi Setup
### 1 
Get Raspberry Pi OS. https://www.raspberrypi.com/software/
### 2
Download the files ```git clone https://github.com/tripletimeswing/BillyBassAssistant```
### 3 
Install the necessary libraries:
```pip install pvporcupine PyAudio SpeechRecognition groq elevenlabs ffmpeg-python gpiozero numpy```

If download doesn't work, create a virtual environment. https://www.raspberrypi.com/news/using-python-with-virtual-environments-the-magpi-148/
### 4
Get API keys from Pico Voice, Groq and Elevenlabs. Load keys when running the program.
### 5 
Run fishBot.py
