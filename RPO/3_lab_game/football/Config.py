import pygame

screen_h = 720
screen_w = 1280
caption = "PONG GAME!"
ball_size = 30
background = pygame.image.load('images/background.png')
ball_image = pygame.image.load('images/ball.png')
speed_x = 10
speed_y = 8
paddle_w = 20
paddle_h = 200
speed_paddle = 20
blue_player = pygame.image.load('images/blue_player.png')
red_player = pygame.image.load('images/red_player.png')
player_size = 150
game_over_score = 3





paddle_data_1 = (0, (paddle_h + paddle_h)//2, paddle_w, paddle_h)
paddle_data_2 = (screen_w - paddle_w, (paddle_h + paddle_h)//2, paddle_w, paddle_h)
