from llama_cpp import Llama
from vira.core.config import MODEL_PATH, INIT_PARAMS, GENERATION_PARAMS
from vira.core.prompting import build_prompt
from vira.core.memory import save_conversation

def stream_response(llm, prompt):
    """
    Streams the model's response token-by-token to simulate real-time chat.
    Returns the full output as a string.
    """
    print("VIRA: ", end='', flush=True)
    full_output = ""
    for chunk in llm(prompt, stream=True, **GENERATION_PARAMS):
        text = chunk['choices'][0]['text']
        print(text, end='', flush=True)
        full_output += text
    print()  # newline after stream ends
    return full_output.strip()

def start_chat():
    """
    Launches VIRA's CLI interface using llama.cpp.
    Manages input loop, streaming output, session memory, and error handling.
    """
    print("[+] Booting VIRA...")

    try:
        llm = Llama(model_path=MODEL_PATH, **INIT_PARAMS)
    except Exception as e:
        print(f"[!] Failed to load model: {e}")
        return

    print("[✓] VIRA is online. Type 'exit' to shut her down.")

    conversation_history = []

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("[-] Shutting down VIRA.")
                break

            # Build prompt from recent context
            prompt_parts = conversation_history[-4:]  # max last 4 turns
            prompt_text = ""
            for pair in prompt_parts:
                prompt_text += build_prompt(pair["user"]) + pair["vira"] + "\n"

            # Add current message
            prompt_text += build_prompt(user_input)

            # Generate and stream output
            model_output = stream_response(llm, prompt_text)

            # Log to file
            save_conversation(user_input, model_output)

            # Update in-memory history
            conversation_history.append({
                "user": user_input,
                "vira": model_output
            })

        except KeyboardInterrupt:
            print("\n[-] Session interrupted.")
            break
        except Exception as e:
            print(f"[!] Runtime error: {e}")

if __name__ == "__main__":
    start_chat()