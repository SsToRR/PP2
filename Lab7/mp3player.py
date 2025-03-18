import pygame
import os
import re
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame MP3 Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

music_folder = "C:/Users/Miras/Desktop/Projects/PP2/Lab7"

songs = []
current_index = 0 
is_playing = False 

def playlist_init():
    for file in os.listdir("C:/Users/Miras/Desktop/Projects/PP2/Lab7"):
        file_name = os.fsdecode(file)
        ok = re.findall("mp3$", file_name)
        if ok:
            songs.append(os.path.join(music_folder, file_name))
    if not songs:
        print("Couldn't find songs maaan...")
        exit(1)

def play_song():
    global is_playing
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()
    is_playing = True

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)  
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)  
    play_song()

def toggle_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    is_playing = not is_playing

def stop_music():
    pygame.mixer.music.stop()

def draw_screen():
    screen.fill(WHITE)

    if songs:
        song_text = f"Now Playing: {os.path.basename(songs[current_index])}"
    else:
        song_text = "No MP3 files found"

    text_surface = font.render(song_text, True, BLACK)
    screen.blit(text_surface, (20, 50))

    instructions = [
        "Controls:",
        "SPACE - Play / Pause",
        "RIGHT ARROW - Next Song",
        "LEFT ARROW - Previous Song",
        "S - Stop",
        "ESC - Exit"
    ]

    y_offset = 150
    for line in instructions:
        text_surface = small_font.render(line, True, BLUE)
        screen.blit(text_surface, (20, y_offset))
        y_offset += 40

    pygame.display.flip()

playlist_init()
play_song()

running = True
while running:
    draw_screen() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False  

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                toggle_pause()
            elif event.key == pygame.K_RIGHT: 
                next_song()
            elif event.key == pygame.K_LEFT:  
                previous_song()
            elif event.key == pygame.K_s:  
                stop_music()

pygame.quit()
