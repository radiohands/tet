import pygame
import time
pygame.init()

screen = pygame.display.set_mode([18,21], pygame.NOFRAME)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0, 255), (9,10),4)
    pygame.draw.circle(screen,(0,255,0),(9,10),3)
    pygame.display.flip()

time.sleep(3)
pygame.quit()