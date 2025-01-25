import os
import pygame


pygame.init()

def play_song(song_index, playlist):
    pygame.mixer.music.load(playlist[song_index])
    pygame.mixer.music.play()

def get_music_files(folder_path):
     return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".mp3", ".wav"))]

def play_music():
     pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def replay_music():
    pygame.mixer.music.rewind()
    play_music()
def music():
    music_folder_path = "C:\\Users\\Dell\\Documents\\vsproject\\project Paimon\\music"
    playlist = get_music_files(music_folder_path)
    current_song_index = 0
    play_song(current_song_index, playlist)

    while True:
        state = input("Me: ")
        if state == 'next':
            current_song_index = (current_song_index + 1) % len(playlist)
            play_song(current_song_index, playlist)
        elif state == 'prev':
            current_song_index = (current_song_index - 1) % len(playlist)
            play_song(current_song_index, playlist)
        elif state == 'play':
            play_music()
        elif state == 'pause':
            pause_music()
        elif state == 'replay':
            replay_music()
        elif state == 'exit':
            pygame.mixer.music.stop()
            pygame.quit()
            break
        else:
           break

