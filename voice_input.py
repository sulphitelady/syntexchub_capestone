import speech_recognition as sr

def get_command():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5)

            command = r.recognize_google(audio)
            return command.lower()

    except:
        # fallback to text input
        command = input("Type your command: ")
        return command.lower()