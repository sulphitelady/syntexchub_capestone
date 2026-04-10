import random

# Simple memory (can be expanded later)
user_name = None


def chatbot_reply(command):
    global user_name

    command = command.lower().strip()

    # ---------------------------
    # GREETINGS
    # ---------------------------
    if any(word in command for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! Ready to assist you."
        ])

    # ---------------------------
    # HOW ARE YOU
    # ---------------------------
    elif "how are you" in command:
        return "I'm doing great! Thanks for asking 😊"

    # ---------------------------
    # NAME HANDLING
    # ---------------------------
    elif "your name" in command:
        return "I am your AI Assistant built for Syntecxhub internship."

    elif "my name is" in command:
        user_name = command.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    elif "what is my name" in command:
        if user_name:
            return f"Your name is {user_name}"
        else:
            return "I don't know your name yet. Tell me by saying 'my name is ...'"

    # ---------------------------
    # HELP
    # ---------------------------
    elif "help" in command:
        return (
            "You can ask me things like:\n"
            "- Open YouTube\n"
            "- Open Google\n"
            "- Tell time\n"
            "- Search something\n"
            "- Say hello"
        )

    # ---------------------------
    # MOTIVATION
    # ---------------------------
    elif any(word in command for word in ["motivate", "inspire"]):
        return random.choice([
            "Keep going! You're doing amazing 🚀",
            "Success is built step by step.",
            "Don't stop until you're proud."
        ])

    # ---------------------------
    # DEFAULT RESPONSE
    # ---------------------------
    else:
        return "I'm not sure how to respond to that. Try asking for help."