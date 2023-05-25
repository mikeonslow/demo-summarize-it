from deepgram import Deepgram
import json
import os

# Hosted sample file

def deepgram_transcribe(audio_file_url):
    # Initializes the Deepgram SDK
    dg_client = Deepgram(os.environ["DEEPGRAM_API_KEY"])
    source = {'url': audio_file_url}
    options = { "punctuate": True, "model": "nova", "language": "en-US" }

    print('Requesting transcript...\n')

    response = dg_client.transcription.sync_prerecorded(source, options)

    transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    print("TRANSCRIPT FROM DEEPGRAM\n")
    print(transcript)
    print("\n\n")
    return transcript
