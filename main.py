import pygame
import time
import os
pygame.init()

# Resolution is 18,21 for the screen, not the board

debug = True
sX, sY = 0, 0  # Window start position (0,0 = top left)
RED, GREEN, BLUE, WHITE, BLACK, GRAY = (255,0,0), (0,255,0), (0,0,255), (0,0,0), (255,255,255), (128,128,128)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (sX,sY) # Place window at sX,sY location

if debug:
    screen = pygame.display.set_mode([18,21], pygame.NOFRAME | pygame.SCALED | pygame.RESIZABLE)
else:
    screen = pygame.display.set_mode([18,21], pygame.NOFRAME)

done = False
gameEnd = False
fps = 0
clock = pygame.time.Clock
left, right, up, down = 0, 1, 2, 3

# Define blocks
B1 = [
1,1,1,1,
0,0,0,0
]
B2 = [
1,0,0,0,
1,1,1,0
]
B3 = [
1,1,1,0,
1,0,0,0
]
B4 = [
1,1,0,0,
0,1,1,0
]
B5 = [
0,1,1,0,
1,1,0,0
]
B6 = [
1,1,0,0,
1,1,0,0
]
B7 = [
1,1,1,0,
0,1,0,0
]


def moveWindow(direction, ammount):
    print("yes")

def drawBoard():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,0,255), (0,0,18,21), 1)
    pygame.draw.rect(screen, (0,0,255), (11,0,18,8), 1)
    pygame.draw.rect(screen, (0,0,255), (11,7,7,14), 1)

def drawBlock(type, x, y, clr):
    #screen.set_at((x,y-1),clr)
    xloc = 0
    for i in type:
        if i == 1:
            if i == 3:
                y = y + 1
                x = 0
                xloc = 0
            screen.set_at((x + xloc, y), clr)
        xloc = xloc + 1


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN and gameEnd != True:
            if event.key == pygame.K_BACKSPACE:
                print("BS")
            elif event.key == pygame.K_ESCAPE:
                done = True
            elif event.key== pygame.K_LEFT:
                moveWindow(left, 1)

    #screen.fill((255,255,255))
    #pygame.draw.circle(screen,(0,0, 255), (9,10),4)
    #pygame.draw.circle(screen,(0,255,0),(9,10),3)
    drawBoard()
    drawBlock(B1, 5, 5, RED)
    pygame.display.flip()

pygame.quit()