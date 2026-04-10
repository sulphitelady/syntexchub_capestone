import webbrowser
from datetime import datetime


def handle_command(command):

    command = command.lower()

    # ---------------- TIME ----------------
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        return f"Current time is {current_time}"

    # ---------------- GOOGLE ----------------
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # ---------------- YOUTUBE ----------------
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    return None