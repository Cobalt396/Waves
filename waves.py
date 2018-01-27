import pygame


#basic setup
pygame.init()

window_w = 1000
window_h = 700

gameDisplay = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Waves')

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

startButton = pygame.image.load('wavesbrd.png')

title_screen = True

while title_screen == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)
    gameDisplay.blit(startButton, (50, 25))

    pygame.display.update()
    clock.tick(60)
