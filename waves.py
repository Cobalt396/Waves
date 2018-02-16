import pygame
pygame.init()

#basic setup

window_w = 1000
window_h = 700

gameDisplay = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Waves')

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

titleArt = pygame.image.load('title.png')

startButton = pygame.image.load('start.png')
startBorder = pygame.image.load('startborder.png')

quitButton = pygame.image.load('quit.png')
quitBorder = pygame.image.load('quitborder.png')

def title(x,y):
    gameDisplay.blit(titleArt, (x,y))

def startImg(x,y):
    gameDisplay.blit(startButton, (x,y))

def quitImg(x,y):
    gameDisplay.blit(quitButton, (x,y))

def startBrder(x,y):
    gameDisplay.blit(startBorder, (x,y))

def quitBrder(x,y):
    gameDisplay.blit(quitBorder, (x,y))

def gameIntro():
    title_screen = True
    while title_screen == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        click = pygame.mouse.get_pressed()
        #print(click)

        gameDisplay.fill(white)

        title(380,50)
        startImg(50,550)
        quitImg(765,550)
        
        if 50 + 185 > mouse[0] > 50 and 550 + 100 > mouse[1] > 550:
            startBrder(15,530)
            if click[0] == 1:
                title_screen = False
                
        if 765 + 185 > mouse[0] > 765 and 550 + 100 > mouse[1] > 550:
            quitBrder(755,530)
            if click[0] == 1:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)

def gameLoop():
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)

        pygame.display.update()
        clock.tick(60)

gameIntro()
gameLoop()






