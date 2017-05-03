#Font.py
#Devin Kamer
#4/28/17

"""Displays Text to the screen using pygame"""

import pygame
import os


class Text(pygame.sprite.Sprite):

    def __init__(self, text, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text = text
        self.textSprite = self.font.render(self.text, True, (255, 255, 255))

        self.rect = self.textSprite.get_rect()
        self.rect.x = x
        self.rect.y = y

    def setText(self, text):
        self.text = text
        self.textSprite = self.font.render(self.text, True, (255, 255, 255))

    def getText(self):
        return self.textSprite

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def getPos(self):
        return (self.rect.x, self.rect.y)

        
