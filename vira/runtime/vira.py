# vira/runtime/vira.py

from llama_cpp import Llama
from vira.core.config import MODEL_PATH, INIT_PARAMS, GENERATION_PARAMS, SYSTEM_PROMPT
from vira.core.prompting import build_prompt
from vira.core.memory import conversation_history, save_conversation, trim_history
from vira.audio.tts_engine import speak  # VIRA speaks via TTS

def stream_response(llm, prompt):
    """
    Streams response tokens from the LLM and prints them in real-time.
    """
    print("VIRA: ", end='', flush=True)
    full_output = ""
    for chunk in llm(prompt, stream=True, **GENERATION_PARAMS):
        text = chunk['choices'][0]['text']
        print(text, end='', flush=True)
        full_output += text
    print()
    return full_output.strip()

def start_chat():
    """
    Main chat loop. Accepts user input, builds prompt, streams LLM response,
    speaks it aloud, and logs conversation history.
    """
    print("[+] Booting VIRA...")

    try:
        llm = Llama(model_path=MODEL_PATH, **INIT_PARAMS)
    except Exception as e:
        print(f"[!] Failed to load model: {e}")
        return

    print("[✓] VIRA is online. Type 'exit' to shut her down.")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("[-] Shutting down VIRA.")
                break

            # Build prompt from past 4 interactions
            prompt_text = SYSTEM_PROMPT + "\n\n"
            for pair in conversation_history[-4:]:
                prompt_text += build_prompt(pair["user"]) + pair["vira"] + "\n"
            prompt_text += build_prompt(user_input)

            # Generate output
            model_output = stream_response(llm, prompt_text)

            # TTS output
            speak(model_output)

            # Save and update memory
            save_conversation(user_input, model_output)
            conversation_history.append({"user": user_input, "vira": model_output})
            conversation_history[:] = trim_history(conversation_history)

        except KeyboardInterrupt:
            print("\n[-] Session interrupted.")
            break
        except Exception as e:
            print(f"[!] Runtime error: {e}")

if __name__ == "__main__":
    start_chat()