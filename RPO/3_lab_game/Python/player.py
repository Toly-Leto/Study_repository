import pygame

class Player:
    """
    Класс Player представляет ракетку, управляемую игроком.
    Отвечает за ее позицию, скорость и движение, а также за ограничение
    движения в пределах экрана.
    """
    def __init__(self, x, y, width, height, screen_height):
        # Создаем прямоугольник для ракетки
        self.rect = pygame.Rect(x, y, width, height)
        # Текущая вертикальная скорость ракетки
        self.speed = 0
        # Высота экрана для ограничения движения ракетки
        self.screen_height = screen_height

    def set_speed(self, speed):
        """
        Устанавливает вертикальную скорость ракетки.
        """
        self.speed = speed

    def move(self):
        """
        Обновляет позицию ракетки на основе ее текущей скорости.
        Ограничивает движение ракетки в пределах верхней и нижней границ экрана.
        """
        self.rect.y += self.speed

        # Ограничиваем движение ракетки в пределах экрана
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height

    def draw(self, surface):
        """
        Отрисовывает ракетку на заданной поверхности Pygame.
        """
        pygame.draw.rect(surface, 'white', self.rect)