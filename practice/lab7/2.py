import pygame 
import os
path = r'C:\Users\User\Desktop\Pragramming Principles 2\practice\lab7'
songs = [file for file in os.listdir(path) if file.endswith('.mp3')]
index = 0
pygame.init()
sc = pygame.display.set_mode((640,640))
player = pygame.image.load("player.jpg")
pygame.mixer.music.load(os.path.join(path,songs[index]))
print(songs[index])
pygame.mixer.music.play()
sc.blit(player, (0, 0))
pygame.display.update()
press = pause = False
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                press = True
        if i.type == pygame.MOUSEMOTION:
            if press and 281 < i.pos[0] < 360 and 470 < i.pos[1] < 550:
                if not pause:
                    pygame.mixer.music.pause()
                    pause = True
                    press = False
                else:
                    pygame.mixer.music.unpause()
                    pause = False
                    press = False
            if press and 220 < i.pos[0] < 265 and 490 < i.pos[1] <530:
                index = (index + 1)%len(songs)
                pygame.mixer.music.load(os.path.join(path,songs[index]))
                print(songs[index])
                pygame.mixer.music.play()
                press = False
            if press and 356 < i.pos[0] < 421 and  490 < i.pos[1] <530:
                index = (index - 1)%len(songs)
                pygame.mixer.music.load(os.path.join(path,songs[index]))
                print(songs[index])
                pygame.mixer.music.play()
                press = False
