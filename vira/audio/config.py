# vira/audio/config.py

import os

# Path to save generated speech
AUDIO_ROOT = os.path.join(os.path.dirname(__file__), "output")

# Ensure the output folder exists
os.makedirs(AUDIO_ROOT, exist_ok=True)

# Final output path for TTS audio
OUTPUT_WAV_PATH = os.path.join(AUDIO_ROOT, "output.wav")