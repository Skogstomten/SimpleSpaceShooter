import pygame
from pygame.surface import Surface
from pygame.rect import Rect


class Shot(object):
    rect: Rect

    def __init__(self, origin_pos: tuple[int, int]):
        self.origin_pos_x, self.origin_pos_y = origin_pos
        self.image = pygame.image.load('./resources/shot.png')
        self.rect = self.image.get_rect()
        self.image_width, self.image_height = self.image.get_size()
        self.rect.topleft = (self.origin_pos_x - (self.image_width / 2),
                             self.origin_pos_y - self.image_height)
        self._damage = 1

    def update(self):
        self.rect.y -= 10

    def draw(self, display_surface: Surface):
        display_surface.blit(self.image, self.rect)

    def get_damage(self) -> int:
        return self._damage
