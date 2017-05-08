#Player.py
#Devin Kamer
#4/27/17

import pygame
import os

path = os.getcwd() + "/Images/Player"

class Player(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, isArthur=False):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.imagesLeft = []
        if not isArthur:
            for file in os.listdir(path + "/Biker/Idle"):
                image = pygame.image.load(path + "/Biker/Idle/" + file).convert()
                image = pygame.transform.scale(image, [128, 128])
                image.set_colorkey((255, 0, 0))
                self.images.append(image)
                image = pygame.transform.flip(image, True, False)
                self.imagesLeft.append(image)

        else:
            for file in os.listdir(path + "/Arthur/Idle"):
                image = pygame.image.load(path + "/Arthur/Idle/" + file).convert()
                image = pygame.transform.scale(image, [128, 128])
                image.set_colorkey((255, 0, 0))
                self.images.append(image)
                image = pygame.transform.flip(image, True, False)
                self.imagesLeft.append(image)
            
        self.index = 0
        self.image = self.images[self.index]
        self.imageLeft = pygame.transform.flip(self.image, True, False)
        self.imageRight = pygame.transform.flip(self.imageLeft, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.attack = 20
        self.isDead = False
        self.coolDown = 0
        self.faceRight = True

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

    def animate(self, timer):
        timer = timer % 60 + 1
        if timer / 5. == 1:
            self.index += 1
            self.index = self.index % len(self.images)
            if self.faceRight:
                self.setImage(self.images[self.index])
            else:
                self.setImage(self.imagesLeft[self.index])

    def flip(self, isRight):
        if isRight:
            self.faceRight = True
            return self.images[self.index]
        else:
            self.faceRight = False
            return self.imagesLeft[self.index]
        

        
