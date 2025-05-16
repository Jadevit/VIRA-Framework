# vira/audio/tts_engine.py

from kokoro import KPipeline
from .config import OUTPUT_WAV_PATH
import torch
import soundfile as sf
import simpleaudio as sa

# Initialize Kokoro TTS pipeline
pipeline = KPipeline(lang_code='a')  # American English

def speak(text: str, voice: str = 'af_heart', speed: float = 1.0):
    """
    Generate and play speech from text using Kokoro TTS.
    Saves to 'output.wav' and plays back with simpleaudio.
    """
    if not text.strip():
        print("No text provided to TTS.")
        return

    print(f"[Kokoro] Generating audio for: {text}")

    try:
        audio_segments = [audio for _, _, audio in pipeline(text, voice=voice, speed=speed)]
        if not audio_segments:
            print("No audio segments generated.")
            return

        # Stack all waveform tensors into one
        waveform = torch.cat(audio_segments).numpy()
        sf.write(OUTPUT_WAV_PATH, waveform, 24000)

        # Play output
        try:
            wave_obj = sa.WaveObject.from_wave_file(OUTPUT_WAV_PATH)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except Exception as e:
            print(f"[!] simpleaudio playback failed: {e}")

    except Exception as e:
        print(f"[!] Kokoro TTS error: {e}")