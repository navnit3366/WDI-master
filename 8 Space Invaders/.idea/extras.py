import pygame

#MOVING UP AND DOWN
lead_y_change = 0

if event.key == pygame.K_UP:
    lead_y_change = -20
    lead_x_change = 0
if event.key == pygame.K_DOWN:
    lead_y_change = 20
    lead_x_change = 0

#CAPTIONS
import time

font = pygame.font.SysFont(None, 30)

def message_on_the_screen (msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


message_on_the_screen('GAME OVER', blue)
time.sleep(2)
pygame.display.update()

#CROSSOVERS
#import random

#if bullet_position_x == lead_x and bullet_position_y == lead_y:
    #removing part of a spaceship

#DRAWING STUFF
Pix = pygame.PixelArray(gameDisplay)
Pix [10][10] = pink
pygame.display.update()

pygame.draw.lines(gameDisplay, yellow,(200,300),(400,500), 5)
pygame.draw.circle(gameDisplay, blue,(50,50),5,2)
pygame.draw.rect()
pygame.draw.polygon(gameDisplay,pink,(()))


for i in range (0,10):
    stworek = Alien11()
    stworek.center = (center_x, center_y)
    center_x += 40
    enemies.add(stworek)