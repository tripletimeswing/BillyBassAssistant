import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, save

def t2s(response):
    elabsKey = os.getenv("ELEVENLABS_KEY")
    audioFile = "voice.mp3"
    # Initialize client
    client = ElevenLabs(api_key=elabsKey)

    # Generate speech
    audio = client.text_to_speech.convert(
        text= response,
        voice_id="pqHfZKP75CvOlQylNhV4",
        model_id="eleven_flash_v2_5",
        output_format="mp3_44100_128",
    )

    # Save to file
    save(audio, audioFile)