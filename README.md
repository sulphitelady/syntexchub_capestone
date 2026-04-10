# 🤖 SyntexHub AI Voice Assistant

An intelligent Python-based Voice Assistant that understands speech commands, executes system tasks, and responds using Text-to-Speech (TTS).

---

## 📌 Overview

SyntexHub AI Voice Assistant is designed to simulate a basic AI assistant capable of:

- 🎤 Listening to voice commands  
- 🧠 Processing instructions intelligently  
- 💻 Executing system-level actions  
- 🔊 Responding using speech output  

It runs in a continuous loop and provides a smooth CLI-based interactive experience.

---

## ✨ Features

- 🎤 Voice Input Recognition (SpeechRecognition)
- 🧠 Command-based Processing System
- 💬 Chatbot Fallback Responses
- 🔊 Text-to-Speech (TTS) Output
- ⏰ Time & System Queries Handling
- 🌐 Web Automation (Open Google, Search, etc.)
- ❌ Exit Command Support
- 🔁 Continuous Listening Mode
- 🔐 Optional Face Authentication (OpenCV)

---

## 🛠 Tech Stack

- **Language:** Python 3.x  
- **Libraries:**
  - pyttsx3
  - SpeechRecognition
  - opencv-python
  - webbrowser
  - os

---

## 📁 Project Structure


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


---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/sulphitelady/syntexchub_capestone.git
cd SyntexHub_AI_Assistant
2. Install Dependencies
pip install -r requirements.txt

OR manually:

pip install pyttsx3 SpeechRecognition opencv-python
▶️ Run Project
python main.py
🧠 How It Works
System starts and initializes the assistant
Continuously listens for voice input
Processes command:
If recognized → executes system action
If unknown → chatbot responds
Response is converted to speech (TTS)
Loop continues until user says "exit"
💡 Example Commands
“Tell me the time”
“Open Google”
“Search on Google”
“Hello”
“Exit”
🚀 Future Improvements
🌐 GUI using Tkinter or PyQt
🤖 Integration with OpenAI / LLM
🗣️ More natural AI voice responses
🎯 Wake word detection (“Hey Assistant”)
📱 Mobile application version
👨‍💻 Author

Namra Mughal
AI & Software Development Enthusiast

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
