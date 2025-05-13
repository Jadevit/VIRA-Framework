# VIRA Framework

**VIRA** (Virtual Intelligence, Real Autonomy) is a modular, local-first AI assistant framework designed for customization, self-hosting, and long-term development. It's built to evolve, not just respond.

The entire system was written from scratch with zero prior Python experience—not as a stunt, but because the best way to learn is to build. Every file is structured with clarity and future-proofing in mind, making VIRA a solid foundation for anyone serious about AI integration at home or beyond.

---

## Features

- **Modular Architecture** – Runtime, core logic, memory, TTS, and more are cleanly separated.
- **Local LLM Inference** – Runs quantized `.gguf` models using `llama-cpp-python`.
- **Streaming Output** – Token-by-token responses for a natural back-and-forth.
- **Custom Personalities** – Easily control tone and behavior via `config.py`.
- **Automatic Logging** – Conversations are saved to `logs/chat_log.txt`.
- **Built for Expansion** – Modules for audio, plugins, and web UI are scaffolded and ready.

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
│   ├── skills/             # Future plugin modules
│   └── web/                # Reserved for future web interface
```

---

## Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/Jadevit/VIRA-Framework.git
cd VIRA-Framework
```
2. (Optional) Create a Virtual Environment



```bash
python3 -m venv vira-env
source vira-env/bin/activate
```
3. Install Dependencies


```bash
pip install -r requirements.txt
```
4. Add Your Model



Place your .gguf model in:

```bash
vira/models/
```
Update the model path in vira/core/config.py if needed.


---

Usage

```bash
python3 run.py
```
This launches VIRA in CLI mode. She responds in real-time and logs everything to logs/chat_log.txt.


---

Customization

You can tweak VIRA's tone and behavior by editing the prompt format or generation parameters in config.py. Whether you want her dry and precise, expressive, or laid-back—it’s entirely up to you.


---

Roadmap

[x] Modular architecture

[x] Local model inference

[x] Prompt formatting

[x] Conversation logging

[ ] TTS (text-to-speech) support

[ ] STT (speech-to-text) input

[ ] Memory/context system

[ ] Web-based interface

[ ] Plugin/skill system



---

Author

Jaden Pain
Self-taught developer.

VIRA was developed in just over a week—what started as a personal challenge became a real, working system.


---

License

MIT. Use it, remix it, improve it. Just don’t claim you built it from scratch if you didn’t.
