import pygame
from Consts import *

class Player:
    def __init__(self, data, color, key_up, key_down):
        self.rect = pygame.Rect(*data)
        self.key_up = key_up
        self.key_down = key_down
        self.color = color
        self.speed_y = 0
        self.score = 0


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.y += self.speed_y
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > screen_h: self.rect.bottom = screen_h

    def check_push(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -1 *  paddle_speed
            if event.key == self.key_down:
                self.speed_y = paddle_speed

        if event.type == pygame.KEYUP:
            if event.key == self.key_up or event.key == self.key_down:
                self.speed_y = 0