#Player.py
#Devin Kamer
#4/27/17

import pygame
import os
from random import randint

img = pygame.image.load(os.getcwd() + "/Images/EnemyIdle.png")

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, image=img):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.convert()
        self.image = pygame.transform.scale(self.image, [128, 128])
        self.image.set_colorkey((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.attack = 20
        self.cooldown = 0
        self.isDead = False

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def getImage(self):
        return self.image
    
    def setImage(self, image):
        self.image = image
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def takeDamage(self, damage=0):
        self.health -= damage
        if self.health <= 0 and not self.isDead:
            image = pygame.transform.rotate(self.image, 90.0)
            self.setImage(image)
            self.isDead = True

    def getHealth(self):
        return self.health

    def performAttack(self, target):
        if randint(1, 4) != 1:
            target.takeDamage(self.attack)
        self.cooldown = 90

    def trackTarget(self, target):
        if not self.cooldown and not self.isDead:
            direction = [0, 0]
            if target.rect.x > self.rect.x + int(self.rect[2] / 2):
                direction[0] = 1
            elif target.rect.x + int(target.rect[2] / 2) < self.rect.x:
                direction[0] = -1

            if target.rect.y > self.rect.y + int(self.rect[3] / 2):
                direction[1] = 1
            elif target.rect.y + int(target.rect[3] / 2) < self.rect.y:
                direction[1] = -1

            if direction == [0, 0]:
                self.performAttack(target)
            else:
                self.update(direction[0], direction[1])
        else:
            if self.isDead:
                pass
            else:
                self.cooldown -= 1
        
        




            
            
            

        
