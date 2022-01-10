import sys

import pygame
from pygame.locals import QUIT
from pygame.surface import Surface

from .screens.screen import Screen
from .screens.start_screen import StartScreen


class App(object):
    WINDOW_WIDTH: int = 400
    WINDOW_HEIGHT: int = 600
    WINDOW_DIMENSION: tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT)

    FPS: int = 60

    _display_surface: Surface
    _screen: Screen

    def __init__(self):
        self._running = True
        self._game_over = False

    def _on_init(self) -> bool:
        try:
            pygame.init()
            pygame.font.init()
            self._display_surface = pygame.display.set_mode(self.WINDOW_DIMENSION)
            self._screen = StartScreen(self.WINDOW_DIMENSION, self.FPS)
            return True
        except Exception as err:
            print(str(err))
            return False

    def execute(self):
        if not self._on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                self._screen = self._screen.handle_event(event)
            self._screen = self._screen.update()
            self._screen = self._screen.render(self._display_surface)


# class App(object):
#     WINDOW_WIDTH: int = 400
#     WINDOW_HEIGHT: int = 600
#     WINDOW_DIMENSION: tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT)
#
#     COLOR_BLACK: tuple[int, int, int] = (0, 0, 0)
#
#     FPS: int = 60
#
#     _display_surface: Surface
#     _clock: Clock
#     _player: Player
#     _obstacle_manager: ObstacleManager
#     _background: Background
#     _running: bool
#     _game_over: bool
#     _game_over_text: Surface
#     _game_font: Font
#
#     def __init__(self):
#         self._running = True
#         self._game_over = False
#
#     def _on_init(self) -> bool:
#         try:
#             pygame.init()
#             pygame.font.init()
#             self._display_surface = pygame.display.set_mode(self.WINDOW_DIMENSION)
#             self._player = Player(self.WINDOW_DIMENSION)
#             self._clock = Clock()
#             self._obstacle_manager = ObstacleManager(
#                 self._player,
#                 self._clock,
#                 self.WINDOW_DIMENSION
#             )
#             self._background = Background(self.WINDOW_DIMENSION)
#             self._game_font = SysFont('Comic Sans MS', 30)
#             self._game_over_text = self._game_font.render('GAME OVER!', False, (255, 0, 0))
#             return True
#         except Exception as err:
#             print(str(err))
#             return False
#
#     def _on_event(self, event: Event):
#         if event.type == QUIT:
#             self._running = False
#         self._player.handle_events(event)
#         self._obstacle_manager.handle_event(event)
#
#     def _on_loop(self):
#         self._background.update()
#         self._player.update_position_from_input()
#         result = self._obstacle_manager.update()
#         if result == 'GAME_OVER':
#             self._game_over = True
#
#     def _on_render(self):
#         self._background.draw(self._display_surface)
#         self._player.draw(self._display_surface)
#         self._obstacle_manager.draw(self._display_surface)
#         if self._game_over:
#             self._display_surface.blit(
#                 self._game_over_text,
#                 (
#                     (self.WINDOW_WIDTH / 2) - (self._game_over_text.get_width() / 2),
#                     (self.WINDOW_HEIGHT / 2) - (self._game_over_text.get_height() / 2)
#                 )
#             )
#
#         pygame.display.flip()
#         self._clock.tick(self.FPS)
#
#     @staticmethod
#     def _on_cleanup():
#         pygame.quit()
#         sys.exit()
#
#     def execute(self):
#         if not self._on_init():
#             self._running = False
#
#         while self._running:
#             for event in pygame.event.get():
#                 self._on_event(event)
#             self._on_loop()
#             self._on_render()
#         self._on_cleanup()
