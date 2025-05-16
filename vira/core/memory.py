# vira/core/memory.py

import os

# Persistent in-memory context during runtime
conversation_history = []

def save_conversation(user_input, response):
    """
    Append a chat turn to 'chat_log.txt'.
    Ensures the logs directory exists.
    """
    os.makedirs("vira/logs", exist_ok=True)

    with open("vira/logs/chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"You: {user_input}\n")
        log_file.write(f"VIRA: {response}\n\n")

def trim_history(history, max_messages=20):
    """
    Keep only the latest `max_messages` in memory.
    """
    return history[-max_messages:]