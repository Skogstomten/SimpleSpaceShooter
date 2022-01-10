import pygame
from pygame.surface import Surface
from pygame.event import Event

from .player import Player
from .obstacles import Asteroid

SPAWN_EVENT = 6001
SPAWN_TIME = 3000


class ObstacleManager(object):
    def __init__(
            self,
            player: Player,
            window_dimensions: tuple[int, int]
    ):
        self.player = player
        self.window_dimensions = window_dimensions
        self.obstacles = []
        self.collision_counter = 0

        pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)

    def update(self) -> None | str:
        if self.player.exploded:
            return

        for obstacle in self.obstacles.copy():
            obstacle.update()

            if self.player.rect.colliderect(obstacle.rect):
                self.player.explode()
                obstacle.explode()
                self.collision_counter += 1
                print("Collision " + str(self.collision_counter))
                self.obstacles.remove(obstacle)
                return 'GAME_OVER'

            for shot in self.player.shots:
                if shot.rect.colliderect(obstacle.rect):
                    self.player.shot_hit(shot)
                    obstacle.damage(shot.get_damage())

            if obstacle.rect.y > self.window_dimensions[1] + 20:
                self.obstacles.remove(obstacle)

            if obstacle.is_destroyed():
                obstacle.explode()
                self.obstacles.remove(obstacle)

    def draw(self, display_surface: Surface):
        for obstacle in self.obstacles:
            obstacle.draw(display_surface)

    def handle_event(self, event: Event):
        if event.type == SPAWN_EVENT:
            self.obstacles.append(Asteroid(self.window_dimensions))
            pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
