🤖 AI Voice Assistant
📌 Project Name

SyntexHub AI Voice Assistant

🚀 Project Description

This is a Python-based AI Voice Assistant that can take voice commands from the user, process them, and respond using speech output. It supports basic system commands, chatbot responses, and voice interaction using text-to-speech technology.

The assistant works in a continuous loop and provides an interactive CLI-based experience.

✨ Features
🎤 Voice input recognition
🧠 Command-based processing system
💬 Chatbot fallback responses
🔊 Text-to-Speech (TTS) voice output
⏰ Time query support
🌐 Open websites like Google
❌ Exit command handling
🔐 Optional face authentication module
🔁 Continuous listening loop

🛠 Technologies Used
Python 3.x
pyttsx3 (Text-to-Speech)
SpeechRecognition (Voice Input)
OpenCV (if face authentication is used)
OS / Webbrowser module (system commands)
Custom Python modules

Project structure
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
├── README.md

▶️ How to Run
1. Install dependencies
pip install pyttsx3 speechrecognition opencv-python
2. Run the project
python main.py

🎯 How It Works
The system starts and optionally performs face authentication.
It listens to the user’s voice command.
The command is processed:
If it matches a system command → executes action
If not → chatbot responds
The response is spoken using TTS.
The system continues in a loop until “exit” is spoken.

📌 Example Commands
“tell me the time”
“open google”
“search google”
“exit”
“hello”

📈 Future Improvements
GUI interface (Tkinter)
Advanced AI chatbot integration (ChatGPT API)
Better natural voice responses
Wake word detection (“Hey Assistant”)
Mobile app version

👨‍💻 Author

Namra Mughal
AI & Software Development Enthusiast