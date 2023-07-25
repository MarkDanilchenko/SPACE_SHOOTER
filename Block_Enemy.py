import pygame.sprite
import random
import Graphics
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageORIGINAL = random.choice(Graphics.meteorsIMGs)
        self.image = self.imageORIGINAL.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        # pygame.draw.circle(self.imageORIGINAL, (255,0,0), self.rect.center, self.radius, width=2)
        self.rect.x = random.randrange(0 + self.rect.width, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(1, 2)
        self.rot = 0
        self.rotSpeed = random.randrange(-5, 5)
        self.lastUpdate = pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0 + self.rect.width, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx = -self.speedx

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > 50:
            self.lastUpdate = now
            self.rot = (self.rot + self.rotSpeed) % 360
            new_image = pygame.transform.rotate(self.imageORIGINAL, self.rot)
            oldCenter = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
