import sys
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

WINDOW_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BASIC_FONT = pygame.font.SysFont(None, 48)
TEXT = BASIC_FONT.render('Hello world!', True, WHITE, BLACK)

while True:
    WINDOW_SURFACE.fill(BLACK)

    text_rect = TEXT.get_rect()
    text_rect.centerx = WINDOW_SURFACE.get_rect().centerx
    text_rect.centery = WINDOW_SURFACE.get_rect().centery
    # draw the text onto the surface
    WINDOW_SURFACE.blit(TEXT, text_rect)

    pygame.draw.circle(WINDOW_SURFACE, (255, 0, 0), (10, 20), 30)
    pygame.draw.line(WINDOW_SURFACE, (0, 0, 255), (200, 250), (225, 300))
    pygame.draw.rect(WINDOW_SURFACE, (0, 255, 0), (150, 50, 100, 50))

    pygame.display.update()
    for event in pygame.event.get():
        # Check to see if the "Close" button has been pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
