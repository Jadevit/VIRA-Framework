# memory.py

import os

def save_conversation(user_input, response):
    """
    Appends a conversation turn to 'chat_log.txt'.
    Ensures the log directory exists before writing.
    """
    os.makedirs("vira/logs", exist_ok=True)

    with open("vira/logs/chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"You: {user_input}\n")
        log_file.write(f"VIRA: {response}\n\n")