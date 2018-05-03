import sys
import pygame
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('Hello world!', True, WHITE, BLACK)

while True:
    windowSurface.fill(BLACK)

    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    # draw the text onto the surface
    windowSurface.blit(text, textRect)

    pygame.draw.circle(windowSurface, (255,0,0), (10, 20), 30)
    pygame.draw.line(windowSurface, (0,0,255), (200, 250), (225, 300))
    pygame.draw.rect(windowSurface, (0,255,0), (150,50,100,50))

    pygame.display.update()
    for event in pygame.event.get():
        # Check to see if the "Close" button has been pressed
        if event.type == QUIT:
            pygame.quit()
            sys.exit(1)
