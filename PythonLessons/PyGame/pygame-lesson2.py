import pygame, sys, time, math # import pygame module and others
# import some constant vairables - like QUIT.  The import * means we don't need
# to write  pygame.locals in front of each constant variable
from pygame.locals import *

pygame.init()   # initialise pygame

# setup a clock to control frame rate
clock = pygame.time.Clock()


# set some colours - RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# setting movement variables(no. pixels)
move = 4
move2 = 3


WINDOWWIDTH = 400  # set a constant, for window width
WINDOWHEIGHT = 300  # set another constant, for window height


# pygame.display is a module in pygame
# set_mode is a method in pygamme.display
# draws a window, pixel size WINDOWWIDTH x WINDOWHEIGHT.
# (WINDOWWIDTH,WINDOWHEIGHT) = tuple.  Can't change, like a string
# don't worry about the 0,32 - just leave them as is
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)


# fills windowSurface with BLACK
windowSurface.fill(BLACK)


# draw two rectangles - one red one green
# tuple at end: x, y (of top left corner), width, height
rectangle = pygame.draw.rect(windowSurface, RED, (150, 50, 100, 50))
rectangle2 = pygame.draw.rect(windowSurface, GREEN, (0, 50, 50, 50))

# print out x coord of lhs and of rhs of the first rectangle
print(rectangle.left)
print(rectangle.right)
# print out y coord of top and bottom of the first rectangle
print(rectangle.top)
print(rectangle.bottom)


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # clear the surface by filling with black
    windowSurface.fill(BLACK)

    # check if the first rectangle is off screen?  If it is,
    # change the direction it moves in
    if (rectangle.right > WINDOWWIDTH):
        move = - move
    elif (rectangle.left <= 0):
        move = -move

    # check if rectangle2 is off screen? If it is, change the direction it
    # moves in

    if (rectangle2.right > WINDOWWIDTH):
        move2 = - move2
    elif (rectangle2.left <= 0):
        move2 = -move2

    # do rectangle and rectangle2 overlap?  If they do, change the direction they
    #  move in
    if ((rectangle2.left > rectangle.left) and (rectangle2.left < rectangle.right )) or ((rectangle2.right > rectangle.left) and (rectangle2.right < rectangle.right)):
        move = -move
        move2 = -move2

    # alter position of the rectangles - i.e. make them move
    topx = rectangle.left + move
    topx2 = rectangle2.left + move2

    # redraw rectangles
    rectangle = pygame.draw.rect(windowSurface, RED, (topx, 50, 100, 50))
    rectangle2 = pygame.draw.rect(windowSurface, GREEN, (topx2, 50, 50, 50))

    pygame.display.update()          # update the display
    clock.tick(30)  # maximum framerate of 30 fps
