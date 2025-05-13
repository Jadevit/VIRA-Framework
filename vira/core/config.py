# vira/core/config.py

import os

# Dynamically resolve the path to the GGUF model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "VIRA-7b", "vira-q8.gguf")

# Model load-time parameters for llama-cpp
INIT_PARAMS = {
    "n_ctx": 2048,       # Context window size
    "n_threads": 8,      # CPU threads to use
    "n_batch": 512,      # Batch size for evaluation
    "n_gpu_layers": 0,   # GPU acceleration layers (0 = CPU only)
    "verbose": False     # Set to True for debug output
}

# Generation parameters used at inference time
GENERATION_PARAMS = {
    "max_tokens": 512,       # Maximum tokens to generate
    "temperature": 0.8,      # Sampling temperature
    "top_p": 0.9,            # Nucleus sampling
    "stop": ["</s>"]         # Token(s) to end generation
}