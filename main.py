#main.py
#Devin Kamer
#4/27/17


import pygame
import Player
import Enemy
import Text
import PowerBar
import os
from random import randint
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1200, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Main Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main variables
cwd = os.getcwd()
isArthur = False

#25% Chance to be Arthur
if randint(1, 5) != 1:
    gameMusic = pygame.mixer.music.load(cwd + "/Music/Main theme.wav")
    enemy = Enemy.Enemy(1000, 500)

else:
    gameMusic = pygame.mixer.music.load(cwd + "/Music/Coconuts.wav")
    enemyImg = pygame.image.load(cwd + "/Images/Enemy/BlackKnight/Idle/blackKnight.png").convert()
    enemyImg = pygame.transform.scale(enemyImg, [128, 128])
    enemyImg.set_colorkey(BLUE)
    enemy = Enemy.Enemy(1000, 500, enemyImg)
    isArthur = True



background = pygame.image.load(cwd + "/Images/street.png").convert()
background = pygame.transform.scale(background, size)
gameOver = pygame.image.load(cwd + "/Images/GameOver.png").convert()
gameOver = pygame.transform.scale(gameOver, size)
win = pygame.image.load(cwd + "/Images/YouWin.png").convert()
win = pygame.transform.scale(win, size)

player = Player.Player(50, 200, isArthur)
xCur = 0
yCur = 0

healthText = Text.Text(str(player.getHealth()), size[0] - 50, 50)

healthBar = PowerBar.PowerBar(75, 15, 50)

globalTimer = 0


#Audio
pygame.mixer.music.play()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    playerAttack = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xCur = -2
                player.setImage(player.flip(False))
            elif event.key == pygame.K_RIGHT:
                xCur = 2
                player.setImage(player.flip(True))
            elif event.key == pygame.K_UP:
                yCur = -2
            elif event.key == pygame.K_DOWN:
                yCur = 2
            elif event.key == pygame.K_SPACE:
                playerAttack = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xCur = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yCur = 0

    if playerAttack:
        player.performAttack(enemy)
        playerAttack = False
    player.update(xCur, yCur)
    enemy.trackTarget(player)
    healthBar.setPercent(player.getHealth())
    healthText.setText(str(enemy.getHealth()))

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()

    player.animate(globalTimer)
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background, [0, 0])


    # --- Drawing code should go here
    if not player.isDead and not enemy.isDead:
        screen.blit(player.getImage(), player.getPos())
        screen.blit(enemy.getImage(), enemy.getPos())
        screen.blit(healthText.getText(), healthText.getPos())
        healthBar.draw(screen)
    else:
        if player.isDead:
            screen.blit(gameOver, [0, 0])
        else:
            screen.blit(win, [0, 0])
        
 
    globalTimer += 1
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
