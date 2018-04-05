import pygame, sys, time, math, random
from pygame.locals import *

WINDOWHEIGHT = 400
WINDOWWIDTH = 400

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

ANGLE = 45
POWER = 20
GRAVITY = 2

pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

box = pygame.Rect(5, 300, 30, 30)
box2 = pygame.Rect(250, 100, 30, 30)

mainClock = pygame.time.Clock()

fired = False

def reset():
    global box
    global fired
    global yv
    global xv
    
    box = pygame.Rect(5, 300, 30, 30)
    fired = False
    
    radangle = ANGLE*math.pi/180
    yv = -POWER*math.cos(radangle)
    xv = POWER*math.sin(radangle)

def checkEvents():
    global fired
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and not fired:
                fired = True

def draw():
    windowSurface.fill(BLACK)
    pygame.draw.rect(windowSurface, RED, box)
    pygame.draw.rect(windowSurface, GREEN, box2)
    pygame.display.update()
    mainClock.tick(30)

def runGame():
    global yv
    global xv
    
    if fired:
        yv = yv + GRAVITY
        box.top = box.top + yv
        box.left = box.left + xv

def checkWinOrLose():
    if box.centerx > WINDOWWIDTH:
        print("Missed!")
        reset()
    if box.centery > WINDOWHEIGHT:
        print("Missed!")
        reset()
    if box.colliderect(box2):
        print("Hit! You win")
        reset()

reset()
while True:
    checkEvents()
    runGame()
    checkWinOrLose()
    draw()
