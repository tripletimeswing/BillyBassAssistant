import ffmpeg

def convertAudio():
    (
        ffmpeg
        .input("voice.mp3")
        .output("voice.wav")
        .overwrite_output()
        .run()
    )
    print("\nconverted")