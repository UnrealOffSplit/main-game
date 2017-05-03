#Player.py
#Devin Kamer
#4/27/17

import pygame
import os

img = pygame.image.load(os.getcwd() + "/Images/Idle.png")

class Player(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, image=img):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.attack = 20
        self.isDead = False
        self.coolDown = 0

    def update(self, x, y):
        if not self.isDead:
            self.rect.x += x
            self.rect.y += y
        if self.coolDown:
            self.coolDown -= 1
        while self.rect.y < 300:
            self.rect.y += 1
        while self.rect.y > 700 - self.rect[3]:
            self.rect.y -= 1
            
        while self.rect.x < 0:
            self.rect.x += 1
        while self.rect.x > 1200 - self.rect[2]:
            self.rect.x -= 1

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
            img = pygame.transform.rotate(self.image, -90.0)
            self.setImage(img)
            self.isDead = True

    def getHealth(self):
        return self.health

    def performAttack(self, target):
        if not self.coolDown:
            if pygame.sprite.collide_rect(self, target):
                target.takeDamage(self.attack)
            self.coolDown = 60

        
