import webbrowser
import datetime
from tts import speak

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube")

def open_google():
    webbrowser.open("https://www.google.com")
    speak("Opening Google")

def tell_time():
    time = datetime.datetime.now().strftime("%H:%M")
    print("Current time:", time)
    speak(f"The time is {time}")

def search_google(command):
    query = command.replace("search", "")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query}")