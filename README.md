# VIRA Framework

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![LLM](https://img.shields.io/badge/LLM-Mistral_7B-critical)
![TTS](https://img.shields.io/badge/TTS-Kokoro-purple)
![Offline](https://img.shields.io/badge/cloud-free-lightgrey)

**VIRA** (Virtual Intelligence, Real Autonomy) is a modular, local-first AI assistant framework designed for customization, self-hosting, and long-term development. It's built to evolve, not just respond.

The entire system was written from scratch with zero prior Python experience—not as a stunt, but because the best way to learn is to build. Every file is structured with clarity and future-proofing in mind, making VIRA a solid foundation for anyone serious about AI integration at home or beyond.

---

## Features

- **Modular Architecture** – Runtime, core logic, memory, TTS, and more are cleanly separated.
- **Local LLM Inference** – Runs quantized `.gguf` models using `llama-cpp-python`.
- **Streaming Output** – Token-by-token responses for a natural back-and-forth.
- **Text-to-Speech (TTS)** – VIRA speaks using [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M) and supports voice model swapping.
- **Custom Personalities** – Easily control tone and behavior via `config.py`.
- **Automatic Logging** – Conversations are saved to `logs/chat_log.txt`.
- **Built for Expansion** – Modules for audio, plugins, and web UI are scaffolded and ready.

---

## Voice Demos

Generate voice samples using:

```
vira/audio/demos/generate_samples.py
```
To use:

```
python3 vira/audio/demos/generate_samples.py
```

They're grouped by accent and demonstrate how expressive and natural Kokoro's voice models are—especially `af_heart`, VIRA’s default voice.

---

## Directory Structure

```
VIRA-Framework/
├── run.py                  # Entry point to launch VIRA
├── requirements.txt        # Python dependencies
├── vira/
│   ├── __init__.py
│   ├── core/               # Prompting logic, config, memory
│   ├── runtime/            # CLI launcher (vira.py)
│   ├── logs/               # Chat logs (output stored here)
│   ├── models/             # Quantized model files
│   ├── audio/              # Voice samples, TTS assets
│   │   ├── demos/          # Sampled TTS voices
│   │   └── output/         # Runtime TTS output
│   ├── skills/             # Future plugin modules
│   └── web/                # Reserved for future web interface
```

---

## Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/VIRA-Framework.git
cd VIRA-Framework
```

2. **(Optional) Create a Virtual Environment**

```bash
python3 -m venv vira-env
source vira-env/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Add Your Model**

Place your `.gguf` model in:

```bash
vira/models/
```

Update the model path in `vira/core/config.py` if needed.

---

## Usage

```bash
python3 run.py
```

This launches VIRA in CLI mode. She responds in real-time, speaks via TTS, and logs all conversations to `logs/chat_log.txt`.

---

## Customization

You can tweak VIRA's tone and behavior by editing the system prompt and generation settings in `config.py`.

You can also change her voice model by editing the default in `tts_engine.py`:
```python
speak(text, voice='af_heart')
```

Kokoro supports 20+ English voice models across accents and genders. Want her to sound British? Angry? Calm? She’ll deliver.

---

## Roadmap

- [x] Modular architecture
- [x] Local model inference
- [x] Prompt formatting
- [x] Conversation logging
- [x] TTS (text-to-speech) support
- [ ] STT (speech-to-text) input
- [ ] Memory/context system
- [ ] Web-based interface
- [ ] Plugin/skill system

---

## Author

**Jaden Pain**  
Self-taught developer, hands-on builder, and a strong believer in doing the work instead of talking about it.  
VIRA was developed in just over a week—what started as a personal challenge became a real, working system.

---

## License

MIT. Use it, remix it, improve it. Just don’t claim you built it from scratch if you didn’t.