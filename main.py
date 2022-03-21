import pygame
import random
import obj
from obj import *
import settings
from pygame.sprite import Group
##------settings----------
W, H = settings.W, settings.H
size = settings.size
fps = settings.FPS
hp = settings.hp
cannon_count = settings.cannon_count
##------pydame------------
pygame.init()
screen = pygame.display.set_mode((W, H))
all_objs = pygame.sprite.Group()
bombs = pygame.sprite.Group()
cannon = Cannon(cannon_count, (W/2, H), all_objs)

run = True
clock = pygame.time.Clock()
cloc1 = pygame.time.Clock()
while run:
    circ = random.randint(0, 100)
    if circ >= 99:
        Bomb(bombs)

    screen.fill((255, 255, 255))
    cannon.hp_blit(screen)

    events = [event for event in pygame.event.get()]
    all_objs.draw(screen)

    m_pos = pygame.mouse.get_pos()
    x = 0
    for event in events:
        i = event
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    all_objs.update(m_pos, keys, all_objs)


    pygame.display.flip()
    clock.tick(60)

