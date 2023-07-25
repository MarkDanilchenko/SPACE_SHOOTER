# GRAPHICS SETTINGS
from os import path
from settings import *
import pygame.image

IMG_dir = path.join(path.dirname(__file__), 'IMG')
IMG_dir_Explosions = path.join(path.dirname(__file__), 'IMG/Explosions')
IMG_dir_Bonus = path.join(path.dirname(__file__), 'IMG/Bonus')
IMG_dir_Meteors = path.join(path.dirname(__file__), 'IMG/Meteors')

# MAIN BACKGROUND
background = pygame.image.load(path.join(IMG_dir, 'gameBackground.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

# PLAYER
playerIMG = pygame.image.load(path.join(IMG_dir, 'playerShip2_red.png'))
playerIMG = pygame.transform.scale(playerIMG, (56, 38))
playerIMG.set_colorkey((0, 0, 0))

# PLAYER'S LIVES
playerLifeIMG = pygame.image.load(path.join(IMG_dir, 'playerShip2_red.png'))
playerLifeIMG = pygame.transform.scale(playerLifeIMG, (23, 15))
playerLifeIMG.set_colorkey((0, 0, 0))

# METEORS
meteorsIMGs = []
meteorsIMGs_list = [
    'meteorBrown_med1.png',
    'meteorBrown_med3.png',
    'meteorBrown_small1.png',
    'meteorBrown_small2.png',
    'meteorBrown_tiny1.png',
    'meteorBrown_tiny2.png'
]

for i in meteorsIMGs_list:
    result = pygame.image.load(path.join(IMG_dir_Meteors, i)).convert()
    result.set_colorkey((0, 0, 0))
    meteorsIMGs.append(result)

# WEAPON AND BULLETS
bulletIMG = pygame.image.load(path.join(IMG_dir, 'laserRed01.png')).convert()
bulletIMG = pygame.transform.scale(bulletIMG, (9, 27))
bulletIMG.set_colorkey((0, 0, 0))

# EXPLOSIONS
explosionAnim = {}
explosionAnim['large'] = []
explosionAnim['small'] = []
explosionAnim['player_deathExplosion'] = []
for i in range(9):
    img = pygame.image.load(path.join(IMG_dir_Explosions, f'regularExplosion0{i}.png')).convert()
    img.set_colorkey((0, 0, 0))
    imgLarge = pygame.transform.scale(img, (75, 75))
    explosionAnim['large'].append(imgLarge)
    imgSmall = pygame.transform.scale(img, (32, 32))
    explosionAnim['small'].append(imgSmall)
    img = pygame.image.load(path.join(IMG_dir_Explosions, f'sonicExplosion0{i}.png')).convert()
    img.set_colorkey((0, 0, 0))
    explosionAnim['player_deathExplosion'].append(img)

# BONUSES
powerUP = {}
powerUP['healthShield'] = pygame.image.load(path.join(IMG_dir_Bonus, 'shield_gold.png')).convert()
powerUP['gun'] = pygame.image.load(path.join(IMG_dir_Bonus, 'gun05.png')).convert()

# CURSOR
pointer = pygame.image.load(path.join(IMG_dir, 'cursor.png')).convert()
pointer = pygame.transform.scale(pointer, (15, 16))
pointer.set_colorkey((0, 0, 0))
