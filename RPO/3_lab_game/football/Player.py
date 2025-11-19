import pygame
from Config import *

class Player:
    def __init__(self, data, key_up, key_down, color):
        self.rect = pygame.Rect(*data)
        self.key_up = key_up
        self.key_down = key_down
        self.speed_y = 0
        self.score = 0
        self.color = color






    def move(self):
        self.rect.y += self.speed_y
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.y + paddle_h > screen_h: self.rect.y = screen_h - paddle_h


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


    def check_push(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -1 * speed_paddle
            if event.key == self.key_down:
                self.speed_y = speed_paddle

        if event.type == pygame.KEYUP:
            if event.key == self.key_up or event.key == self.key_down:
                self.speed_y = 0


