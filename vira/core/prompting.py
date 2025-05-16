# vira/core/prompting.py

def build_prompt(user_input: str) -> str:
    """
    Wraps user input in Mistral-style [INST]...[/INST] blocks.
    """
    clean_input = user_input.strip()
    return f"[INST] {clean_input} [/INST]"