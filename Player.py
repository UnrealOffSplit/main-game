#Player.py
#Devin Kamer
#4/27/17

import pygame
import os

img = pygame.image.load(os.getcwd() + "/Images/walk1.png")

class Player(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, image=img):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100

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

    def getHealth(self):
        return self.health

        
