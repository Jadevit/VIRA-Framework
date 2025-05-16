import os
import torch
import soundfile as sf
from kokoro import KPipeline

# === CONFIG ===
AMERICAN_VOICES = [
    # Female
    'af_alloy', 'af_aoede', 'af_bella', 'af_heart', 'af_jessica',
    'af_kore', 'af_nicole', 'af_nova', 'af_river', 'af_sarah', 'af_sky',
    # Male
    'am_adam', 'am_echo', 'am_eric', 'am_fenrir', 'am_liam',
    'am_michael', 'am_onyx', 'am_puck'
]

BRITISH_VOICES = [
    # Female
    'bf_alice', 'bf_emma', 'bf_isabella', 'bf_lily',
    # Male
    'bm_daniel', 'bm_fable', 'bm_george', 'bm_lewis'
]

TEST_TEXT = (
    "My name is Vira. I'm your AI assistant, designed to help you build, break, and rebuild your world. "
    "If you're hearing this, you're probably testing voice models again, aren't you?"
)

BASE_DIR = os.path.dirname(__file__)
OUTPUT_PATHS = {
    'american': os.path.join(BASE_DIR, "american"),
    'british': os.path.join(BASE_DIR, "british")
}

pipeline = KPipeline(lang_code='a')  # American English base

# === HELPER ===
def generate_voice_sample(voice_name, target_dir):
    print(f"[+] Generating: {voice_name}")

    try:
        os.makedirs(target_dir, exist_ok=True)
        audio_segments = [audio for _, _, audio in pipeline(TEST_TEXT, voice=voice_name)]

        if not audio_segments:
            print(f"[!] No audio segments returned for {voice_name}")
            return

        waveform = torch.cat(audio_segments).numpy()
        waveform = waveform / max(abs(waveform)) * 0.95  # Normalize

        output_path = os.path.join(target_dir, f"{voice_name}.wav")
        sf.write(output_path, waveform, 24000)
        print(f"    Saved to {output_path}")

    except Exception as e:
        print(f"[!] Error generating {voice_name}: {e}")

# === MAIN ===
if __name__ == "__main__":
    print("[*] Generating American English voices...")
    for voice in AMERICAN_VOICES:
        generate_voice_sample(voice, OUTPUT_PATHS['american'])

    print("\n[*] Generating British English voices...")
    for voice in BRITISH_VOICES:
        generate_voice_sample(voice, OUTPUT_PATHS['british'])

    print("\n[✓] All samples generated.")