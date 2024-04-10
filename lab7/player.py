import pygame

pygame.init()

screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music")

pygame.mixer.init()

pygame.mixer.music.load(r'D:\.vscode\.vscodepython\lab7\music\Don Toliver - Way Bigger.mp3')
pygame.mixer.music.set_volume(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                pygame.mixer.music.load(r'D:\.vscode\.vscodepython\lab7\music\Don Toliver - Way Bigger.mp3')
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                pygame.mixer.music.load(r'D:\.vscode\.vscodepython\lab7\music\Ninety_One_-_JUR_MAPELEP_76292719.mp3')
                pygame.mixer.music.play()

    pygame.display.flip()

pygame.quit()