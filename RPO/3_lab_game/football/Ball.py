import pygame
import random


from Config import *
from Teammate import Teammate

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(screen_w//2, screen_h//2, ball_size, ball_size)
        self.lst_of_players = []
        self.last_tuch = None
        self.image = pygame.transform.scale(ball_image, (ball_size, ball_size))
        self.speed_x = speed_x
        self.speed_y = speed_y


    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refraction(self):

        if self.rect.y + ball_size > screen_h: self.speed_y *= -1
        if self.rect.y < 0: self.speed_y *= -1

    def start_position(self):
        self.rect.x = screen_w//2
        self.rect.y = screen_h//2
        self.speed_x = random.choice([-1, 1]) * speed_x
        self.speed_y = random.choice([-1, 1]) * speed_y


    def check_colisions(self, player_1, player_2):
        if self.rect.x + ball_size > screen_w:
            player_1.score += 1
            self.start_position()
            self.lst_of_players = []

        if self.rect.x <0:
            player_2.score += 1
            self.start_position()
            self.lst_of_players = []

        if self.rect.colliderect(player_1.rect):
            self.speed_x *= -1
            self.last_tuch = player_1.color
            new_teammate = Teammate(blue_player, 'blue')
            self.lst_of_players.append(new_teammate)

        if self.rect.colliderect(player_2.rect):
            self.speed_x *= -1
            self.last_tuch = player_2.color
            new_teammate = Teammate(red_player, 'red')
            self.lst_of_players.append(new_teammate)


    def check_colis_players(self, player_1, player_2):
        for player in self.lst_of_players:
            if self.rect.colliderect(player.rect) and player.color != self.last_tuch:
                self.speed_x += random.choice([4, -4, 8, -8, 0])
                self.speed_x *= -1
                self.last_tuch = player.color
                self.lst_of_players.remove(player)


