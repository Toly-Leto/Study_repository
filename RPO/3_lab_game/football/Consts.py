import pygame
screen_w = 1280
screen_h = 720
background = pygame.image.load('images/background.png')
caption = "FOOTBALL GAME!"
ball_size = 50
ball_image = pygame.image.load('images/ball.png')
speed_x = 10
speed_y = 8
paddle_w = 20
paddle_h = 200
paddle_speed = 15
blue_player_image = pygame.image.load('images/blue_player.png')
red_player_image = pygame.image.load('images/red_player.png')
size_player = 200
game_over_score = 3

blue_player_data = (0, screen_h//2, paddle_w, paddle_h)
red_player_data = (screen_w -paddle_w, screen_h//2, paddle_w, paddle_h)