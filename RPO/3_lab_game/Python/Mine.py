import pygame
import random

class Mine:
    def __init__(self, x, y, width, height, color='red'):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color


    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)