import pygame
import random

from Config import *
class Teammate:
    def __init__(self, image, color):
        self.rect = pygame.Rect(random.randint(player_size, screen_w - player_size),
                                random.randint(player_size, screen_h - player_size),
                                player_size, player_size)
        self.image = pygame.transform.scale(image, (player_size, player_size))
        self.color = color



    def draw(self, screen):
        screen.blit(self.image, self.rect)

