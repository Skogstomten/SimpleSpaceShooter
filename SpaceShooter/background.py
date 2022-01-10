import pygame
from pygame.surface import Surface


class Background(object):
    _bg_image: Surface
    _y_pos: int

    def __init__(self, window_dimension: tuple[int, int]):
        self._bg_image = pygame.transform.scale(
            pygame.image.load('./resources/bg.jpg'),
            window_dimension
        )
        self._window_height = window_dimension[1]
        self._y_pos = -1

    def update(self):
        self._y_pos += 1
        if self._y_pos >= self._window_height:
            self._y_pos = 0

    def draw(self, display_surface: Surface):
        display_surface.fill((0, 0, 0))
        display_surface.blit(self._bg_image, (0, self._y_pos))
        display_surface.blit(self._bg_image, (0, self._y_pos - self._window_height))
