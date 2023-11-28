import pygame
import time

pygame.init()

pink = (255,92,96)
yellow = (255,170,0)
blue = (113,170,219)

#SCREEN
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Invaders')

#VARIABLES CONSTANT FOR NOW
block_size = 20
frames_per_second = 10

clock = pygame.time.Clock()

#CAPTIONS
font = pygame.font.SysFont(None, 30)

def message_on_the_screen (msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


#EVENTS
def gameLoop():
    gameExit = False
    gameOver = False

    #VARIABLES THAT MAY REALLY CHANGE
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(pink)
            message_on_the_screen('Press C to play again or Q to quit', blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0

            #TO CHANGE
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
                gameOver = True
                #it cannot move further (how?)

        lead_x += lead_x_change
        gameDisplay.fill(pink)
        pygame.draw.rect(gameDisplay, yellow, [lead_x,lead_y,block_size,block_size])
        pygame.display.update()

        clock.tick(frames_per_second)

    pygame.quit()
    quit()

gameLoop()