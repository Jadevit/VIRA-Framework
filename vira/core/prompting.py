# prompting.py

def build_prompt(user_input: str) -> str:
    """
    Wraps user input in Mistral-Instruct format.
    Example: [INST] Hello VIRA [/INST]
    """
    clean_input = user_input.strip()
    return f"[INST] {clean_input} [/INST]"