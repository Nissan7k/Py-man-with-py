from gtts import gTTS
import pygame
import os

# Set display driver for pygame to dummy
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def speak(text):
    tts = gTTS(text, lang="en")
    tts.save("speech.mp3")

    try:
        pygame.mixer.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()

        # Wait for the speech to finish
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)

        pygame.mixer.quit()  # Properly close the mixer
    except pygame.error as e:
        if "video system not initialized" not in str(e):
            print(f"Error playing sound: {e}")
