import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down")
        return "None"
    return query

def voice_assistant():
    speak("Hello, how can I help you?")
    while True:
        query = listen().lower()
        if query == "none":
            continue
        if 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break
        elif 'hello' in query:
            speak("Hello! How are you?")
        elif 'your name' in query:
            speak("I am your voice assistant.")
        else:
            speak("I am sorry, I can't do that yet.")

if __name__ == "__main__":
    voice_assistant()
