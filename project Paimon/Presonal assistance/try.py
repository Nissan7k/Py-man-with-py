
import pyttsx3

def speak(text, speed=1.0):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the voice property to a female voice, if available
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

    # Set the speed property
    engine.setProperty('rate', speed * 130)  # Adjust as needed for desired speed

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
