import pygame
import sys

from Screen import Screen
from Ball import Ball
from Player import Player
from Config import *

pygame.init()
game_display = Screen()
ball = Ball()
player_1 = Player(paddle_data_1, pygame.K_w, pygame.K_s, 'blue')
player_2 = Player(paddle_data_2, pygame.K_UP, pygame.K_DOWN, 'red')


clock = pygame.time.Clock()
while True:
    game_display.screen.blit(game_display.background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        player_1.check_push(event)
        player_2.check_push(event)

    game_display.draw(ball, game_display.screen, player_1, player_2)

    pygame.display.update()
    game_display.game_over(player_1, player_2)
    clock.tick(60)
