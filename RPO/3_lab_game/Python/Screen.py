import pygame

class Screen:

    def __init__(self, width, height, caption):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        self.font = pygame.font.Font(None, 100)
        self.screen_width = width
        self.screen_height = height



    def draw_elements(self, ball_obj, player1_paddle, player2_paddle, player1_points, player2_points, lst_of_mines):

        self.screen.fill('black')


        player1_score_surface = self.font.render(str(player1_points), True, "white")
        player2_score_surface = self.font.render(str(player2_points), True, "white")




        pygame.draw.aaline(self.screen, 'white', (self.screen_width / 2, 0), (self.screen_width / 2, self.screen_height))


        ball_obj.draw(self.screen)
        player1_paddle.draw(self.screen)
        player2_paddle.draw(self.screen)
        [mine.draw(self.screen) for mine in lst_of_mines]

        self.screen.blit(player1_score_surface, (self.screen_width / 4, 20))
        self.screen.blit(player2_score_surface, (3 * self.screen_width / 4, 20))



        pygame.display.update()