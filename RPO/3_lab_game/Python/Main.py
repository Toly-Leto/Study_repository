import pygame
import sys
import random

from Ball import Ball
from Player import Player
from Screen import Screen
from Mine import Mine

screen_width = 1280
screen_height = 720
pygame.init()
game_display = Screen(screen_width, screen_height, "Paddle Game! Laba_#_3")


ball_size = 30
initial_ball_speed_x = 8 * random.choice([-1, 1])
initial_ball_speed_y = 6 * random.choice([-1, 1])
ball_obj = Ball(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2,
                ball_size, initial_ball_speed_x, initial_ball_speed_y, screen_width, screen_height)



paddle_width = 20
paddle_height = 150
player1_paddle = Player(0, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height, screen_height, 'red')
player2_paddle = Player(screen_width - paddle_width, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height,
                        screen_height, 'blue')


player1_points = 0
player2_points = 0

lst_of_mines = []
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_paddle.set_speed(-15)
            if event.key == pygame.K_DOWN:
                player2_paddle.set_speed(15)
            if event.key == pygame.K_w:
                player1_paddle.set_speed(-15)
            if event.key == pygame.K_s:
                player1_paddle.set_speed(15)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_paddle.set_speed(0)
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_paddle.set_speed(0)


    ball_obj.move()
    player1_paddle.move()
    player2_paddle.move()


    if  ball_obj.check_collision(player1_paddle, player2_paddle):

        new_mine = Mine(random.randint(30, 1200), random.randint(30, 700), 30, 30, ['blue', 'red'][ball_obj.last_tuch == 'left'])
        lst_of_mines.append(new_mine)


    if ball_obj.check_collision_mine(lst_of_mines) and ball_obj.check_color_and_paddle(ball_obj.check_collision_mine(lst_of_mines)):
        player1_points += ball_obj.last_tuch == 'right'
        player2_points += ball_obj.last_tuch == 'left'
        ball_obj.last_tuch = None
        lst_of_mines = []
        ball_obj.reset()




    winner_side = ball_obj.check_point()
    if winner_side == 'player_1':
        player1_points += 1
        lst_of_mines = []

        ball_obj.reset()
    elif winner_side == 'player_2':
        player2_points += 1
        lst_of_mines = []
        ball_obj.reset()

    game_display.draw_elements(ball_obj, player1_paddle, player2_paddle, player1_points, player2_points, lst_of_mines)

    clock.tick(60)


