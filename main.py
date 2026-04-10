from face_auth import authenticate_user
from voice_input import get_command
from command_handler import handle_command
from chatbot import chatbot_reply
from tts import speak


def main():
    print("==== AI Assistant Started ====")

    # ---------------------------
    # FACE AUTH
    # ---------------------------
    auth = authenticate_user()

    if not auth:
        speak("Access denied")
        print("Access Denied ❌")
        return

    speak("Access granted")
    speak("Welcome! AI Assistant is now active")

    while True:
        command = get_command()

        if not command:
            continue

        command = command.lower().strip()

        print(f"You said: {command}")

        # ---------------------------
        # EXIT
        # ---------------------------
        if "exit" in command:
            speak("Exiting AI Assistant")
            print("Exiting AI Assistant...")
            break

        # ---------------------------
        # COMMAND HANDLER
        # ---------------------------
        action_result = handle_command(command)

        if action_result:
            speak(action_result)
            continue

        # ---------------------------
        # CHATBOT
        # ---------------------------
        response = chatbot_reply(command)

        speak(response)


if __name__ == "__main__":
    main()