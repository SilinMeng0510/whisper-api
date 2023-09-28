import sys
sys.path.append("/Users/silinmeng/Python_Projects/SpeechToText")

import openai
from pydub import AudioSegment
import constants

openai.api_key = constants.API_KEY

audio = AudioSegment.from_file("audio_files/audio.m4a")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000
while audio:
    first_10_minutes = audio[:ten_minutes]
    first_10_minutes.export("audio_segmented/10_minutes_chunk.mp3", format="mp3")
    audio_file= open("audio_segmented/10_minutes_chunk.mp3", "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(transcript.text + " ")
    audio = audio[ten_minutes:]