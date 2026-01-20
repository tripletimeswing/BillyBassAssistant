import struct
import pvporcupine
import pyaudio
import os

def wakeWord():
    porcupineKey = os.getenv("PORCUPINE_KEY")

    try:
        #create wake word instant
        porcupine = pvporcupine.create(
            access_key=porcupineKey,
            #keywords=['picovoice', 'bumblebee'] or train your own keyword_paths on pico voice and name the file wakeWordPath.ppn
            keyword_paths = ["wakeWordPath.ppn"]
        )

        #create audio stream
        pa = pyaudio.PyAudio()
        chunk = porcupine.frame_length

        stream = pa.open(
            rate = porcupine.sample_rate,
            channels = 1,
            format = pyaudio.paInt16,
            input = True,
            frames_per_buffer = chunk
        )

        print("recording\n")

        detected = False

        while (detected != True):
            frames = stream.read(chunk)
            frames = struct.unpack_from("h" * chunk, frames)

            keywordIndex = porcupine.process(frames)

            if keywordIndex >= 0:
                detected = True
                print("detected")

    finally:
        if (detected == True):
            porcupine.delete()
            stream.close()
            pa.terminate()
            print("\nclosed audiostream")

    return(detected)

