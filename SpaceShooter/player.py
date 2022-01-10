import pygame
from pygame.surface import Surface
from pygame.event import Event
from pygame.rect import Rect

from .shot import Shot


class Player(object):

    def __init__(self, window_dimention: tuple[int, int]):
        self.image = pygame.image.load('./resources/player.png')
        self.rect: Rect = self.image.get_rect()
        self.window_width, self.window_height = window_dimention
        self.speed = 5
        self.exploded = False
        self.shots = []

        self.image_width, self.image_height = self.image.get_size()
        self.rect.x = int((self.window_width / 2) - (self.image_width / 2))
        self.rect.y = self.window_height - 100 - self.image_height

    def update_position_from_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.rect.y > 0:
                self.rect.y -= self.speed
                if self.rect.y < 0:
                    self.rect.y = 0

        if keys[pygame.K_DOWN]:
            if self.rect.y < self.window_height - self.image_height:
                self.rect.y += self.speed
                if self.rect.y > self.window_height - self.image_height:
                    self.rect.y = self.window_height - self.image_height

        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
                if self.rect.x < 0:
                    self.rect.x = 0

        if keys[pygame.K_RIGHT]:
            if self.rect.x < self.window_width - self.image_width:
                self.rect.x += self.speed
                if self.rect.x > self.window_width - self.image_width:
                    self.rect.x = self.window_width - self.image_width

    def handle_events(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot()

    def draw(self, display_surface: Surface):
        if self.exploded:
            return

        display_surface.blit(self.image, self.rect)

        for shot in self.shots.copy():
            shot.update()
            shot.draw(display_surface)
            if shot.rect.y < -30:
                self.shots.remove(shot)

    def shoot(self):
        if self.exploded:
            return

        origin_x = int(self.rect.x + (self.image_width / 2))
        shot = Shot((origin_x, self.rect.y))
        self.shots.append(shot)

    def shot_hit(self, shot: Shot):
        self.shots.remove(shot)

    def explode(self):
        self.exploded = True
