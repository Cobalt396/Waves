import pygame
pygame.init()

#basic setup

window_w = 1000
window_h = 700

gameDisplay = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Waves')

clock = pygame.time.Clock()

white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)

titleBack = pygame.image.load('silverbackground.jpg')

gameBack = pygame.image.load('darkbackground.jpg')

titleArt = pygame.image.load('title.png')

startButton = pygame.image.load('start.png')
startBorder = pygame.image.load('startborder.png')

quitButton = pygame.image.load('quit.png')
quitBorder = pygame.image.load('quitborder.png')

playeronepointer = pygame.image.load('player1point.png')
playertwopointer = pygame.image.load('player2point.png')

gamegrid = pygame.image.load('grid.png')

redcastle = pygame.image.load('redcastle.png')
bluecastle = pygame.image.load('bluecastle.png')

def background(pic,x,y):
    gameDisplay.blit(pic, (x,y))

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

def pointer1(x,y):
    gameDisplay.blit(playeronepointer, (x,y))
    
def pointer2(x,y):
    gameDisplay.blit(playertwopointer, (x,y))

def grid(x,y):
    gameDisplay.blit(gamegrid, (x,y))

def redCastle(x,y):
    gameDisplay.blit(redcastle, (x,y))

def blueCastle(x,y):
    gameDisplay.blit(bluecastle, (x,y))

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

        gameDisplay.fill(black)
        
        background(titleBack,0,0)
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
    
    oneX = 50
    oneY = 50
    twoX = 950
    twoY = 50

    oneX_change = 0
    oneY_change = 0
    twoX_change = 0
    twoY_change = 0

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    oneX_change += 5
                elif event.key == pygame.K_a:
                    oneX_change += -5
                elif event.key == pygame.K_s:
                    oneY_change += 5
                elif event.key == pygame.K_w:
                    oneY_change += -5
                elif event.key == pygame.K_RIGHT:
                    twoX_change += 5
                elif event.key == pygame.K_LEFT:
                    twoX_change += -5
                elif event.key == pygame.K_DOWN:
                    twoY_change += 5
                elif event.key == pygame.K_UP:
                    twoY_change += -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a or\
                   event.key == pygame.K_s or event.key == pygame.K_w or\
                   event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or\
                   event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    oneX_change = 0
                    oneY_change = 0
                    twoX_change = 0
                    twoY_change = 0
                
        background(gameBack,0,0)
        #gameDisplay.fill(white)

        oneX += oneX_change
        oneY += oneY_change
        twoX += twoX_change
        twoY += twoY_change

        grid(250,100)

        redCastle(476,545)
        blueCastle(476,105)

        pointer1(oneX,oneY)
        pointer2(twoX,twoY)

        mouse = pygame.mouse.get_pos()
        #print(mouse)
        click = pygame.mouse.get_pressed()
        #print(click)

        pygame.display.update()
        clock.tick(60)

gameIntro()
gameLoop()






