#GPIOPins: IN1 = 27

import pyaudio
import wave
import numpy
from gpiozero import OutputDevice
from time import sleep

def controlMouth():
    mouth = OutputDevice(27)

    #sound
    chunk = 256
    threshold = 800 #adjust based on device

    #open wav
    wf = wave.open("voice.wav", "rb")

    #create audio stream
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    #read and process per chunk
    data = wf.readframes(chunk)

    while len(data) > 0:
        #play
        stream.write(data)

        #convert to float for overflow error
        rawWave = numpy.frombuffer(data, dtype=numpy.int16).astype(numpy.float32)
        #get amplitude w RMS
        amplitude = numpy.sqrt(numpy.mean(rawWave**2))

        #control mouth based on amplitude threshold
        if amplitude > threshold:
            mouth.on()
        else:
            mouth.off()

        #next chunk
        data = wf.readframes(chunk)
    
    mouth.close()
    stream.stop_stream()
    stream.close()
    pa.terminate()