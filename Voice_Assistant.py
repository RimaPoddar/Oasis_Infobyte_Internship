import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

def recognize_speech():  
    recognizer = sr.Recognizer()  
    with sr.Microphone() as source:
        print("Listening...")   
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)  
        print(f"You said: {command}")  
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "" 
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search for" in command:
        search_query = command.replace("search for", "").strip()
        results = wikipedia.summary(search_query, sentences=2)
        speak(f"According to Wikipedia, {results}")
    else:
        speak("I am not sure how to respond to that.")  

def main():
    while True:
        command = recognize_speech()
        if command:
            respond_to_command(command)
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break


if __name__ == "__main__":
    main()
