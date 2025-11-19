import sys
import pygame

from Config import *

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.font = pygame.font.Font(None, 150)
        pygame.display.set_caption(caption)
        self.background = pygame.transform.scale(background, (screen_w, screen_h))


    def draw_players(self, lst_of_players):
        for player in lst_of_players:
            self.screen.blit(player.image, player.rect)


    def draw(self, ball, screen, player_1, player_2):
        pygame.draw.aaline(self.screen, 'white', (screen_w / 2, 0), (screen_w / 2, screen_h))
        ball.refraction()
        ball.move()
        ball.draw(screen)

        ball.check_colisions(player_1, player_2)
        player_1.move()
        player_2.move()

        player_1.draw(screen)
        player_2.draw(screen)
        self.draw_players(ball.lst_of_players)

        player1_score_surface = self.font.render(str(player_1.score), True, 'black')
        player2_score_surface = self.font.render(str(player_2.score), True, 'black')

        self.screen.blit(player1_score_surface, (screen_w / 4, 20))
        self.screen.blit(player2_score_surface, (3 * screen_w / 4, 20))

        ball.check_colis_players(player_1, player_2)

    def game_over(self, red_player, blue_player):
        if red_player.score == game_over_score or blue_player.score == game_over_score:
            text_game_over = f'{['RED', 'BLUE'][red_player.score == game_over_score]} PLAYER WON'
            font = pygame.font.Font(None, 150)
            text_surface = font.render(text_game_over, True, ['RED', 'BLUE'][red_player.score == game_over_score])
            text_rect = text_surface.get_rect()
            text_rect.center = (screen_w // 2, screen_h // 2)
            self.screen.blit(text_surface, text_rect)

            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()

