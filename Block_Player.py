import pygame.sprite
import Sounds
from settings import *
from Block_Bullets import Bullet
import Graphics


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Graphics.playerIMG
        self.rect = self.image.get_rect()
        # raduis for more correct collisions
        self.radius = 25
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius, width=2)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 50
        self.speedx = 0
        self.shield = 100
        self.shootDelay = 300
        self.lastShoot = pygame.time.get_ticks()
        self.lives = 1
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx

        if self.rect.right > WIDTH + self.rect.width / 2:
            self.rect.right = self.rect.width / 2
        if self.rect.left < 0 - self.rect.width / 2:
            self.rect.left = WIDTH - self.rect.width / 2

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1500:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 50

        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > 5000:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def shoot(self, all_sprites, groupOfBullets):
        now = pygame.time.get_ticks()
        if now - self.lastShoot > self.shootDelay:
            self.lastShoot = now
            if self.power == 1:
                self.shootDelay = 300
                bullet = Bullet(self.rect.centerx, self.rect.top - 5)
                all_sprites.add(bullet)
                groupOfBullets.add(bullet)
                Sounds.shootSound.play()
            elif self.power >= 2:
                self.shootDelay = 150
                extraBullet_1 = Bullet(self.rect.left, self.rect.top - 5)
                extraBullet_2 = Bullet(self.rect.right, self.rect.top - 5)
                all_sprites.add(extraBullet_1)
                all_sprites.add(extraBullet_2)
                groupOfBullets.add(extraBullet_1)
                groupOfBullets.add(extraBullet_2)
                Sounds.extraShootSound.play()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 1000)

    def powerUP(self):
        self.power +=1
        self.power_time = pygame.time.get_ticks()