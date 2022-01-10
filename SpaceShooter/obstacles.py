import random

import pygame
from pygame.surface import Surface
from pygame.rect import Rect


class Obstacle(object):

    def __init__(
            self,
            window_dimension: tuple[int, int],
            health: int
    ):
        self.window_dimension = window_dimension
        self.health = health
        self.image: Surface = pygame.image.load('./resources/asteroid.png')
        self.rect: Rect = self.image.get_rect()
        self.rect.topleft = (
            random.randint(0, self.window_dimension[0] - self.image.get_width()),
            0 - self.image.get_height()
        )
        self.direction = random.randint(-10, 10)
        self.speed = random.randint(2, 10)

    def update(self):
        self.rect.x += self.direction
        self.rect.y += self.speed
        if self.rect.x < 0 or self.rect.x > self.window_dimension[0] - self.image.get_width():
            self.direction *= -1

    def draw(self, display_surface: Surface):
        display_surface.blit(self.image, self.rect)

    def damage(self, damage: int):
        self.health -= damage

    def explode(self):
        pass

    def is_destroyed(self):
        return self.health <= 0


class Asteroid(Obstacle):
    def __init__(
            self,
            window_dimension: tuple[int, int],
    ):
        super(Asteroid, self).__init__(window_dimension, 2)
