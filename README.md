🚀 SyntexHub AI Voice Assistant

An intelligent Python-based AI Voice Assistant that enables hands-free interaction through voice commands. It can recognize speech, execute system tasks, and respond using a natural text-to-speech engine.

📌 Overview

SyntexHub AI Voice Assistant is designed to simulate a basic AI assistant capable of:

Listening to user voice commands 🎤
Processing instructions intelligently 🧠
Executing system-level actions 💻
Responding using speech output 🔊

It provides a smooth CLI-based interactive experience with continuous listening mode.

✨ Features
🎤 Voice Input Recognition using SpeechRecognition
🧠 Command-based Processing System
💬 Chatbot Fallback Responses
🔊 Text-to-Speech (TTS) Output
⏰ Time and System Query Handling
🌐 Web Automation (Open Google, search, etc.)
❌ Exit Command Support
🔁 Continuous Listening Loop
🔐 Optional Face Authentication (OpenCV-based)
🛠 Tech Stack
Language: Python 3.x
Libraries:
pyttsx3 – Text-to-Speech engine
SpeechRecognition – Voice input processing
opencv-python – Face authentication (optional)
webbrowser – Open websites
os – System-level commands
📁 Project Structure
SyntexHub_AI_Assistant/
│
├── main.py
├── tts.py
├── voice_input.py
├── command_handler.py
├── chatbot.py
├── face_auth.py
├── actions.py
├── history.py
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/sulphitelady/syntexchub_capestone.git
cd SyntexHub_AI_Assistant
2. Install Dependencies
pip install -r requirements.txt

Or manually:

pip install pyttsx3 SpeechRecognition opencv-python
▶️ How to Run
python main.py
🧠 How It Works
The system starts and initializes the assistant
It listens for voice input continuously
Command is processed:
If recognized → system executes action
If unknown → chatbot responds
Response is spoken using TTS engine
Loop continues until "exit" is spoken
💡 Example Commands
“Tell me the time”
“Open Google”
“Search on Google”
“Hello”
“Exit”
🚀 Future Improvements
🌐 GUI interface using Tkinter / PyQt
🤖 Integration with OpenAI / LLM chatbot
🗣️ More natural voice responses
🎯 Wake word detection (“Hey Assistant”)
📱 Mobile application version
👨‍💻 Author

Namra Mughal
AI & Software Development Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
