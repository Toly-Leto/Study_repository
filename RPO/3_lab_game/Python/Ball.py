import pygame
import random

class Ball:
    def __init__(self, x, y, size, initial_speed_x, initial_speed_y, screen_width, screen_height):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = initial_speed_x
        self.speed_y = initial_speed_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_tuch = None


    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1

    def check_collision(self, player1_paddle, player2_paddle):
        if self.rect.colliderect(player1_paddle.rect): self.last_tuch = 'left'
        if self.rect.colliderect(player2_paddle.rect): self.last_tuch = 'right'

        if self.rect.colliderect(player1_paddle.rect) or self.rect.colliderect(player2_paddle.rect):
            self.speed_x *= -1
            return True
        else: return False

    def check_collision_mine(self, lst_of_mines):
        for mine in lst_of_mines:
            if self.rect.colliderect(mine.rect): return mine

    def check_color_and_paddle(self, mine):
        if self.last_tuch == 'left' and mine.color == 'blue':
            return True
        if self.last_tuch == 'right' and mine.color == 'red':
            return True
        return False



    def check_point(self):

        if self.rect.left <= 0:
            return 'player_2' # Шар вышел за левую границу, значит очко набрал правый игрок
        if self.rect.right >= self.screen_width:
            return 'player_1' # Шар вышел за правую границу, значит очко набрал левый игрок
        return None

    def reset(self):
        self.rect.center = (self.screen_width / 2, self.screen_height / 2)
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

    def draw(self, surface):
        pygame.draw.ellipse(surface, 'white', self.rect)