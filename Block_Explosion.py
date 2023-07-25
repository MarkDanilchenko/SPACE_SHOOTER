import pygame.sprite
import Graphics


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = Graphics.explosionAnim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.frameRate = 35

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(Graphics.explosionAnim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = Graphics.explosionAnim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center