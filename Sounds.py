# SOUND SETTINGS
from os import path
from settings import *
import pygame.mixer

SND_dir = path.join(path.dirname(__file__), 'SND')

# SHOOT SOUND
shootSound = pygame.mixer.Sound(path.join(SND_dir, 'sfx_laser1.ogg'))
extraShootSound = pygame.mixer.Sound(path.join(SND_dir, 'sfx_laser2.ogg'))

# METEORS DESTRACTION SOUNDS
meteorExplosionSounds = []
meteorExplosionSounds_list = [
    'explosion01.wav',
    'explosion02.wav',
    'explosion03.wav',
    'explosion04.wav'
]
for i in meteorExplosionSounds_list:
    result = pygame.mixer.Sound(path.join(SND_dir, i))
    result.set_volume(0.5)
    meteorExplosionSounds.append(result)

# MAIN SONG
pygame.mixer.music.load(path.join(SND_dir, 'Alexander Ehlers - Warped.mp3'))
pygame.mixer.music.set_volume(0.4)

# BONUS ACTIVATED SOUND
bonusUP = pygame.mixer.Sound(path.join(SND_dir, 'sfx_shieldUp.ogg'))
