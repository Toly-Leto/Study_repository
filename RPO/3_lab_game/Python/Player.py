import pygame

class Player:
    def __init__(self, x, y, width, height, screen_height, name):

        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 0
        self.screen_height = screen_height
        self.score = 0
        self.last_tuch = False
        self.name = name


    def set_speed(self, speed):
        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height

    def draw(self, surface):
        pygame.draw.rect(surface, self.name, self.rect)