from pygame import Surface
from pygame.event import Event

from .screen import Screen
from ..background import Background
from ..obstacle_manager import ObstacleManager
from ..player import Player


class PlayScreen(Screen):
    _background: Background
    _player: Player
    _obstacle_manager: ObstacleManager

    def __init__(self, window_dimension: tuple[int, int], fps: int):
        super(PlayScreen, self).__init__(window_dimension, fps)
        self._background = Background(window_dimension)
        self._player = Player(window_dimension)
        self._obstacle_manager = ObstacleManager(self._player, window_dimension)

    def _handle_event(self, event: Event) -> 'Screen':
        self._player.handle_events(event)
        self._obstacle_manager.handle_event(event)
        return self

    def _update(self) -> 'Screen':
        self._background.update()
        self._player.update_position_from_input()
        result = self._obstacle_manager.update()
        if result == 'GAME_OVER':
            from .game_over_screen import GameOverScreen
            return GameOverScreen(self._window_dimension, self._fps)
        return self

    def _render(self, surface: Surface) -> 'Screen':
        self._background.draw(surface)
        self._player.draw(surface)
        self._obstacle_manager.draw(surface)
        return self
