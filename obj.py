import settings
import pygame
import random
from pygame import transform

##------settengs----------
W, H = settings.W, settings.H
size = settings.size
fps = settings.FPS
hp = settings.hp
hp_0 = settings.hp


class Cannon(pygame.sprite.Sprite):
    def __init__(self, can_count, coords, *group):
        """Аргументы: coords - коордiнаты на поле"""
        super().__init__(*group)
        self.image = pygame.image.load("textures/cannon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.coords = coords
        self.speed = 3.
        self.hp = settings.hp
        self.rect.x, self.rect.y = coords


    def damag(self, b=100):
        self.hp = self.hp - int(b / 10)
        if hp <= 0:
            self.death()

    def death(self):
        pass

    def hp_blit(self, screen):
        step = 20
        pygame.draw.rect(screen, (64, 128, 200),
                         (W - 2 * step, step, step, step * 5), 2)
        pygame.draw.rect(screen, (64, 128, 255),
                         (W - 2 * step, step + hp_0 - hp, step, hp))

    def update(self, m_pos, keys, objs,
               *args):
        """задел на будущее"""
        if keys[pygame.K_LEFT]:
            self.rect = self.rect.move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect = self.rect.move(self.speed, 0)
        if keys[pygame.K_UP]:
            self.rect = self.rect.move(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect = self.rect.move(0, self.speed)
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if self.rect.x < 0:
            self.x = W
        if self.rect.x > W:
            self.x = 0
        if self.rect.y < 0:
            self.y = H
        if self.rect.y > H:
            self.y = 0


class Bomb(pygame.sprite.Sprite):
    image = pygame.image.load("textures/bomb.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.hp = random.randint(0, 100)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - 200)
        self.rect.y = random.randrange(40)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.image.load("textures/explo.jpg")
            self.image = pygame.transform.scale(self.image, (70, 70))
            clock = pygame.time.Clock
            self.hp = self.hp - 10
            if self.hp < 30:
                self.kill()
