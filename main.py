#main.py
#Devin Kamer
#4/27/17


import pygame
import Player
import Enemy
import Text
import PowerBar
import os
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
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
img = pygame.image.load(cwd + "/Images/walk1.png").convert()
img.set_colorkey(BLACK)
background = pygame.image.load(cwd + "/Images/street.png").convert()
background = pygame.transform.scale(background, size)

player = Player.Player(50, 200, img)
enemy = Enemy.Enemy(1000, 500)
xCur = 0
yCur = 0

healthText = Text.Text(str(player.getHealth()), size[0] - 50, 50)
healthBar = PowerBar.PowerBar(75, 15, 50)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xCur = -2
            elif event.key == pygame.K_RIGHT:
                xCur = 2
            elif event.key == pygame.K_UP:
                yCur = -2
            elif event.key == pygame.K_DOWN:
                yCur = 2
            elif event.key == pygame.K_SPACE:
                player.takeDamage(1)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xCur = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yCur = 0

    player.update(xCur, yCur)
    enemy.trackTarget(player)
    healthBar.setPercent(player.getHealth())
    healthText.setText(str(player.getHealth()))
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background, [0, 0])


    # --- Drawing code should go here
    screen.blit(player.getImage(), player.getPos())
    screen.blit(enemy.getImage(), enemy.getPos())
    screen.blit(healthText.getText(), healthText.getPos())
    healthBar.draw(screen)
 

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
