#PowerBar.py
#Devin Kamer & Tyler Whitney
#4/28/17

"""An 'Energy Meter' used to display energy or power in a visiable way"""

import pygame

class PowerBar(pygame.sprite.Sprite):

    def __init__(self, percent=0, x=0, y=0, color=(255, 0, 0), width=100, height=25):

        self.percent = 100 -percent

        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.Surface([width, height]),
                       pygame.Surface([width - (100 - percent / 100.0 * width), height])]

        self.colors = [(0, 0, 0), color]
        for i in range(2):
            self.images[i].fill(self.colors[i])

        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height



    def draw(self, screen):
        """screen is the pygame screen"""
        
        for i in self.images:
            screen.blit(i, [self.rect.x, self.rect.y])

    def setPercent(self, percent):
        self.percent = 100 -percent
        if self.percent <= 100:
            self.images[1] = pygame.Surface([self.width - (self.percent / 100.0 * self.width), self.height])
            self.images[1].fill(self.colors[1])
        else:
            self.images[1] = pygame.Surface([0, self.height])
            self.images[1].fill(self.colors[1])

        
