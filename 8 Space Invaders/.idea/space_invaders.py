import pygame
import random

pygame.init()
pygame.mixer.init()

dark_blue = (0,0,20)
grey = (127,127,127)
red = (200,0,0)
spaceship_blue = (0,170,200)

#IMAGES
img1 = pygame.image.load('first_alien.png')
img2 = pygame.image.load('second_alien.png')
img3 = pygame.image.load('third_alien.png')
img4 = pygame.image.load('special_alien_copy.png')
img5 = pygame.image.load('blue_spaceship_copy.png')

#MUSIC
game_won_sound = pygame.mixer.Sound('game_won.wav')
spaceship_shoot_sound = pygame.mixer.Sound('spaceship_shoot.wav')
special_alien_defeated_sound = pygame.mixer.Sound('shot.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')
new_game_sound = pygame.mixer.Sound('new_game.wav')
extra_life_sound = pygame.mixer.Sound('extra_life.wav')

#USEREVENTS
enemy_shooting = pygame.USEREVENT
pygame.time.set_timer(enemy_shooting,300)
special_enemy_appears = pygame.USEREVENT +1
pygame.time.set_timer(special_enemy_appears,21000)
extra_life = pygame.USEREVENT +2
pygame.time.set_timer(extra_life,30000)

#SCREEN
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Invaders')

#CAPTIONS
font_name = pygame.font.match_font('segoe print')

def caption (surf, text, color, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#VARIABLES CONSTANT FOR NOW
frames_per_second = 30

clock = pygame.time.Clock()

speed = 1 #of the aliens

#FIRST ALIEN AND HIS MOVES ♥
class Alien11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('first_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 80
        self.speedx = speed
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        self.rect.x += self.speedx
        if self.rect.right >= display_width:
            self.rect.y += 20
            self.speedx = -speed
        if self.rect.left <= 0:
            self.rect.y += 20
            self.speedx = speed

#SECOND FIRST ALIEN AND HIS MOVES ♥
class Alien12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('first_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 120
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right >= display_width:
            self.rect.y += 20
            self.speedx = -speed
        if self.rect.left <= 0:
            self.rect.y += 20
            self.speedx = speed

#SECOND ALIEN AND HIS MOVES ♥
class Alien21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('second_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 160
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right >= display_width:
            self.rect.y += 20
            self.speedx = -speed
        if self.rect.left <= 0:
            self.rect.y += 20
            self.speedx = speed

#SECOND SECOND ALIEN AND HIS MOVES ♥
class Alien22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('second_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right >= display_width:
            self.rect.y += 20
            self.speedx = -speed
        if self.rect.left <= 0:
            self.rect.y += 20
            self.speedx = speed

#THIRD ALIEN AND HIS MOVES ♥
class Alien3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('third_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 240
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right >= display_width:
            self.rect.y += 20
            self.speedx = -speed
        if self.rect.left <= 0:
            self.rect.y += 20
            self.speedx = speed

#SPACESHIP
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('blue_spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = display_width/2
        self.rect.y = display_height-40
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -6
        if keystate[pygame.K_RIGHT]:
            self.speedx = 6
        self.rect.x += self.speedx
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= display_width:
            self.rect.right = display_width

    def shoot(self):
        new_lightning = Lightning(self.rect.centerx, self.rect.top)
        lightnings.add(new_lightning)
        all_sprites.add(new_lightning)

#SPECIAL ALIEN
class SpecialAlien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('special_alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 80
        self.speedx = speed+1

    def update(self):
        self.rect.x += self.speedx

#LIGHTNINGS
class Lightning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('lightning.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()

#STARS
class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.speedy = 4

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom >= display_height:
            self.kill()

#BLOCKS
class Block(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 530

#EXTRA LIFE
class ExtraLife(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = display_width
        self.rect.y = 500
        self.speedx = -speed-1

    def update(self):
        self.rect.x += self.speedx

#GAME LOOP
gameExit = False
gameOver = False
gameWon = False
newGame = True

while not gameExit:

    if newGame == True:
        new_game_sound.play(10)
        gameDisplay.fill(dark_blue)
        caption(gameDisplay, 'Welcome to', grey, 16, display_width / 2, 100)
        caption(gameDisplay, 'SPACE INVADERS', spaceship_blue, 40, display_width / 2, 130)
        caption(gameDisplay, 'Your purpose is to defeat the enemies and save our planet!', grey, 16, display_width / 2,
                210)
        caption(gameDisplay, 'Press arrows to move and space to shoot', grey, 16, display_width / 2, 240)
        caption(gameDisplay, 'Catch hearts to get extra life and dont let the aliens come too close!', grey, 16,
                display_width / 2, 270)
        caption(gameDisplay, 'Good luck!', grey, 16, display_width / 2, 300)
        caption(gameDisplay, 'Press any key to begin', spaceship_blue, 16, display_width / 2, 470)
        coor1 = 40
        for i in range(4):
            gameDisplay.blit(img1, [coor1, 380])
            gameDisplay.blit(img2, [coor1 + 45, 380])
            gameDisplay.blit(img3, [coor1 + 90, 380])
            coor1 += 135
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(frames_per_second)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    waiting = False
                    gameExit = True
                if event.type == pygame.KEYUP:
                    waiting = False
        newGame = False
        enemies = pygame.sprite.Group()
        spaceship_group = pygame.sprite.Group()
        specials = pygame.sprite.Group()
        lightnings = pygame.sprite.Group()
        stars = pygame.sprite.Group()
        blocks = pygame.sprite.Group()
        extras = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        x1 = 0
        for i in range(0, 10):
            creature = Alien11()
            creature.rect.x += x1
            x1 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x2 = 0
        for i in range(0, 10):
            creature = Alien12()
            creature.rect.x += x2
            x2 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x3 = 0
        for i in range(0, 10):
            creature = Alien21()
            creature.rect.x += x3
            x3 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x4 = 0
        for i in range(0, 10):
            creature = Alien22()
            creature.rect.x += x4
            x4 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x5 = 0
        for i in range(0, 10):
            creature = Alien3()
            creature.rect.x += x5
            x5 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        my_spaceship = Spaceship()
        spaceship_group.add(my_spaceship)
        all_sprites.add(my_spaceship)

        x1_of_a_block = 75
        for i in range(0, 10):
            square = Block(x1_of_a_block)
            x1_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x2_of_a_block = 250
        for i in range(0, 10):
            square = Block(x2_of_a_block)
            x2_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x3_of_a_block = 425
        for i in range(0, 10):
            square = Block(x3_of_a_block)
            x3_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        lives = 3
        score = 0

    if gameOver == True:
        game_over_sound.play()
        gameDisplay.fill(dark_blue)
        caption(gameDisplay, 'Game Over', red, 50, display_width / 2, 200)
        caption(gameDisplay, 'Try again! ', grey, 20, display_width / 2, 270)
        caption(gameDisplay, 'Press C to play again or Q to quit ', grey, 20, display_width / 2, 300)
        gameDisplay.blit(img4, [180, 40])
        gameDisplay.blit(img4, [180, 400])
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(frames_per_second)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
        gameOver = False
        enemies = pygame.sprite.Group()
        spaceship_group = pygame.sprite.Group()
        specials = pygame.sprite.Group()
        lightnings = pygame.sprite.Group()
        stars = pygame.sprite.Group()
        blocks = pygame.sprite.Group()
        extras = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        x1 = 0
        for i in range(0, 10):
            creature = Alien11()
            creature.rect.x += x1
            x1 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x2 = 0
        for i in range(0, 10):
            creature = Alien12()
            creature.rect.x += x2
            x2 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x3 = 0
        for i in range(0, 10):
            creature = Alien21()
            creature.rect.x += x3
            x3 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x4 = 0
        for i in range(0, 10):
            creature = Alien22()
            creature.rect.x += x4
            x4 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x5 = 0
        for i in range(0, 10):
            creature = Alien3()
            creature.rect.x += x5
            x5 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        my_spaceship = Spaceship()
        spaceship_group.add(my_spaceship)
        all_sprites.add(my_spaceship)

        x1_of_a_block = 75
        for i in range(0, 10):
            square = Block(x1_of_a_block)
            x1_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x2_of_a_block = 250
        for i in range(0, 10):
            square = Block(x2_of_a_block)
            x2_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x3_of_a_block = 425
        for i in range(0, 10):
            square = Block(x3_of_a_block)
            x3_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        lives = 3
        score = 0

    if gameWon == True:
        game_won_sound.play()
        gameDisplay.fill(dark_blue)
        caption(gameDisplay, 'Congratulations! You won the game!', spaceship_blue, 30, display_width / 2, 200)
        caption(gameDisplay, 'Press C to play again or Q to quit ', grey, 20, display_width / 2, 270)
        gameDisplay.blit(img5, [180, 40])
        gameDisplay.blit(img5, [180, 400])
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(frames_per_second)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    waiting = False
                    gameExit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        waiting = False
                    elif event.key == pygame.K_q:
                        #pygame.quit()
                        waiting = False
                        gameExit = True
        gameWon = False
        enemies = pygame.sprite.Group()
        spaceship_group = pygame.sprite.Group()
        specials = pygame.sprite.Group()
        lightnings = pygame.sprite.Group()
        stars = pygame.sprite.Group()
        blocks = pygame.sprite.Group()
        extras = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        x1 = 0
        for i in range(0, 10):
            creature = Alien11()
            creature.rect.x += x1
            x1 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x2 = 0
        for i in range(0, 10):
            creature = Alien12()
            creature.rect.x += x2
            x2 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x3 = 0
        for i in range(0, 10):
            creature = Alien21()
            creature.rect.x += x3
            x3 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x4 = 0
        for i in range(0, 10):
            creature = Alien22()
            creature.rect.x += x4
            x4 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        x5 = 0
        for i in range(0, 10):
            creature = Alien3()
            creature.rect.x += x5
            x5 += 40
            enemies.add(creature)
            all_sprites.add(creature)

        my_spaceship = Spaceship()
        spaceship_group.add(my_spaceship)
        all_sprites.add(my_spaceship)

        x1_of_a_block = 75
        for i in range(0, 10):
            square = Block(x1_of_a_block)
            x1_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x2_of_a_block = 250
        for i in range(0, 10):
            square = Block(x2_of_a_block)
            x2_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        x3_of_a_block = 425
        for i in range(0, 10):
            square = Block(x3_of_a_block)
            x3_of_a_block += 10
            blocks.add(square)
            all_sprites.add(square)

        lives = 3
        score = 0

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_spaceship.shoot()
                spaceship_shoot_sound.play()

        elif event.type == enemy_shooting:
            if len(enemies.sprites()) != 0:
                firing_enemy = random.choice(enemies.sprites())
                new_star = Star()
                new_star.rect.x = firing_enemy.rect.x +10
                new_star.rect.y = firing_enemy.rect.y +10
                all_sprites.add(new_star)
                stars.add(new_star)
                #alien_shoot_sound.play()

        elif event.type == special_enemy_appears:
            special = SpecialAlien()
            specials.add(special)
            all_sprites.add(special)

        elif event.type == extra_life:
            heart = ExtraLife()
            extras.add(heart)
            all_sprites.add(heart)

    #ALIEN COMING TOO CLOSE
    for creature in enemies:
        if creature.rect.bottom >= 500:
            special_alien_defeated_sound.play()
            gameOver = True

    if len(enemies.sprites()) == 0:
        gameWon = True

    #COLLISIONS
    hits = pygame.sprite.groupcollide(enemies, lightnings, True, True)
    for hit in hits:
        score += 10

    hits2 = pygame.sprite.groupcollide(specials, lightnings, True, True)
    for hit in hits2:
        score += 100
        special_alien_defeated_sound.play()

    hits3 = pygame.sprite.groupcollide(stars, lightnings, True, True)
    for hit in hits3:
        score += 5

    hits4 = pygame.sprite.groupcollide(spaceship_group, stars, False, True)
    if hits4:
        lives -= 1
        special_alien_defeated_sound.play()
        my_spaceship.rect.centerx = display_width / 2
        my_spaceship.rect.y = display_height - 40
        if lives ==0:
            gameOver = True

    hits5 = pygame.sprite.groupcollide(blocks, stars, True, True)
    hits6 = pygame.sprite.groupcollide(blocks, lightnings, True, True)

    hits7 = pygame.sprite.groupcollide(extras, lightnings, True, True)
    for hit in hits7:
        extra_life_sound.play()
        lives += 1

    #UPDATING AND DRAWING ON THE DISPLAY
    if gameExit == False:
        enemies.update()
        spaceship_group.update()
        specials.update()
        lightnings.update()
        stars.update()
        blocks.update()
        extras.update()
        all_sprites.update()

        gameDisplay.fill(dark_blue)

        caption(gameDisplay, 'Score: '+str(score), grey, 20, 70, 30)
        caption(gameDisplay, 'Lives: '+str(lives), grey, 20, display_width-70, 30)

        enemies.draw(gameDisplay)
        spaceship_group.draw(gameDisplay)
        specials.draw(gameDisplay)
        lightnings.draw(gameDisplay)
        stars.draw(gameDisplay)
        blocks.draw(gameDisplay)
        extras.draw(gameDisplay)
        all_sprites.draw(gameDisplay)

        pygame.display.update()

        clock.tick(frames_per_second)

#pygame.quit()
#quit()