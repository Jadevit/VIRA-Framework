# vira/core/config.py

import os

# Path to GGUF model (dynamically resolved)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "VIRA-7b", "vira-q8.gguf")

# llama-cpp init parameters
INIT_PARAMS = {
    "n_ctx": 2048,
    "n_threads": 8,
    "n_batch": 512,
    "n_gpu_layers": 0,
    "verbose": False
}

# Text generation parameters
GENERATION_PARAMS = {
    "max_tokens": 512,
    "temperature": 0.8,
    "top_p": 0.9,
    "stop": ["</s>"]
}

# System prompt for VIRA's persona (placeholder version)
SYSTEM_PROMPT = (
    "[SYSTEM_PROMPT_PLACEHOLDER] "
    "Replace this with your custom identity prompt."
)