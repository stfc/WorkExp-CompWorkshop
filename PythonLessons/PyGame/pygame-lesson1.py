"""This file contains a simple 'Hello World' style program for PyGame."""

import sys
import pygame

# Initialize all imported pygame modules
pygame.init()

# Define colours as (R, G, B) values for later use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Define the screen size
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# Set up the surface to draw on later
WINDOW_SURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# Declare a font and string for displaying later
BASIC_FONT = pygame.font.SysFont(None, 48)
TEXT = BASIC_FONT.render('Hello world!', True, WHITE, BLACK)

while True:
    # Fill the screen to prevent any moving shapes leaving a 'trail'
    WINDOW_SURFACE.fill(BLACK)

    # Determine where to display TEXT
    text_rect = TEXT.get_rect()
    text_rect.centerx = WINDOW_SURFACE.get_rect().centerx
    text_rect.centery = WINDOW_SURFACE.get_rect().centery
    # Draw the text onto the surface
    WINDOW_SURFACE.blit(TEXT, text_rect)

    # Draw a circle, line and rectangle just to show how
    pygame.draw.circle(WINDOW_SURFACE, (255, 0, 0), (10, 20), 30)
    pygame.draw.line(WINDOW_SURFACE, (0, 0, 255), (200, 250), (225, 300))
    pygame.draw.rect(WINDOW_SURFACE, (0, 255, 0), (150, 50, 100, 50))

    # Update the screen
    pygame.display.update()

    # Check for user input
    for event in pygame.event.get():
        # Check to see if the "Close" button has been pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
