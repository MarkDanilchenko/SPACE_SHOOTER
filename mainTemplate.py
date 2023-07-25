import random
import pygame
from settings import *

# INITIALIZATION
# INITIALIZATION
# INITIALIZATION
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SPACE_SHOOTER')
clock = pygame.time.Clock()
import Graphics
import Sounds
import Block_Explosion
import Block_Bonus
import Block_Player
import Block_Enemy

# NEW CURSOR
# NEW CURSOR
# NEW CURSOR
pygame.mouse.set_visible(False)
pointer_rect = Graphics.pointer.get_rect()

# GAME SCORE, MAIN SONG, STATS
# GAME SCORE, MAIN SONG, STATS
# GAME SCORE, MAIN SONG, STATS
pygame.mixer.music.play(loops=-1)
gameScore = 0
gameScoreBEST = 0
fontName = pygame.font.match_font('arial', True)


def draw_text(surface, text: str, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_shieldBar(surface, x, y, pct):
    if pct < 0:
        pct = 0
    barLength = 100
    barHeight = 10
    fill = (pct / 100) * barLength
    outline_rect = pygame.Rect(x, y, barLength, barHeight)
    fill_rect = pygame.Rect(x, y, fill, barHeight)
    pygame.draw.rect(surface, (255, 0, 0), outline_rect)
    pygame.draw.rect(surface, (0, 255, 0), fill_rect)
    pygame.draw.rect(surface, (255, 255, 255), outline_rect, width=2)


def draw_lives(surface, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surface.blit(img, img_rect)


# GAME OVER
# GAME OVER
# GAME OVER
def finalScreen():
    global gameScoreBEST
    if gameScoreBEST < gameScore:
        gameScoreBEST = gameScore
    screen.blit(Graphics.background, Graphics.background_rect)
    draw_text(screen, 'SPACE_SHOOTER', 50, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, f'Best Score = {str(gameScoreBEST)}', 18, WIDTH / 2, HEIGHT * 0.35)
    draw_text(screen, 'MOVE: -LEFT|RIGHT- or -A|D-', 20, WIDTH / 2, HEIGHT * 0.5)
    draw_text(screen, 'FIRE: -SPACE|LBM-', 20, WIDTH / 2, HEIGHT * 0.6)
    draw_text(screen, 'Press any key to begin', 18, WIDTH / 2, HEIGHT * 0.8)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def createEnemy():
    enemy = Block_Enemy.Enemy()
    all_sprites.add(enemy)
    groupOfEnemies.add(enemy)


# MAIN GAME LOOP
# MAIN GAME LOOP
# MAIN GAME LOOP
game_over = True
running = True

while running:
    if game_over:
        finalScreen()
        game_over = False
        gameScore = 0

        #         SPRITES ADDING
        #         SPRITES ADDING
        #         SPRITES ADDING
        all_sprites = pygame.sprite.Group()
        groupOfEnemies = pygame.sprite.Group()
        groupOfBullets = pygame.sprite.Group()
        groupOfBonuses = pygame.sprite.Group()
        player = Block_Player.Player()
        all_sprites.add(player)
        for i in range(20):
            createEnemy()

    clock.tick(FPS)
    pointer_rect.center = pygame.mouse.get_pos()
    keystate = pygame.key.get_pressed()
    mousestate = pygame.mouse.get_pressed()

    if keystate[pygame.K_SPACE] or mousestate[0]:
        player.shoot(all_sprites, groupOfBullets)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #     SPRITES UPDATE AND COLLISIONS
    all_sprites.update()
    hits_Player_Enemy = pygame.sprite.spritecollide(player, groupOfEnemies, True, pygame.sprite.collide_circle)
    for i in hits_Player_Enemy:
        # adding enemy after self delete
        createEnemy()
        # health damage after collision with meteor
        player.shield -= i.radius * 1.2
        if player.shield <= 0:
            player_deathExplosion = Block_Explosion.Explosion(player.rect.center, 'player_deathExplosion')
            all_sprites.add(player_deathExplosion)
            player.hide()
            player.lives -= 1
            player.shield = 100
        explosion = Block_Explosion.Explosion(i.rect.center, 'small')
        all_sprites.add(explosion)

    if player.lives == 0 and not player_deathExplosion.alive():
        game_over = True

    hits_Player_Bonus = pygame.sprite.spritecollide(player, groupOfBonuses, True)
    for i in hits_Player_Bonus:
        if i.type == 'healthShield':
            player.shield += 15
            Sounds.bonusUP.play()
            if player.shield >= 100:
                player.shield = 100
        if i.type == 'gun':
            Sounds.bonusUP.play()
            player.powerUP()

    hits_Bullet_Enemy = pygame.sprite.groupcollide(groupOfEnemies, groupOfBullets, True, True)
    for i in hits_Bullet_Enemy:
        createEnemy()
        gameScore += 50 - i.radius
        explosion = Block_Explosion.Explosion(i.rect.center, 'large')
        all_sprites.add(explosion)
        (random.choice(Sounds.meteorExplosionSounds)).play()
        if random.random() > 0.97:
            bonus = Block_Bonus.Bonus(i.rect.center)
            all_sprites.add(bonus)
            groupOfBonuses.add(bonus)

    # DRAWING ALL SPRITES
    screen.fill((0, 0, 0))
    screen.blit(Graphics.background, Graphics.background_rect)
    all_sprites.draw(screen)
    draw_text(screen, f'Score {str(gameScore)}', 24, WIDTH / 2, 660)
    draw_text(screen, f'Lives {str(round(player.shield, 1))} %', 14, 60, 660)
    draw_shieldBar(screen, 10, 680, player.shield)
    draw_lives(screen, WIDTH - 150, 670, player.lives, Graphics.playerLifeIMG)
    screen.blit(Graphics.pointer, pointer_rect)

    pygame.display.flip()

pygame.quit()


