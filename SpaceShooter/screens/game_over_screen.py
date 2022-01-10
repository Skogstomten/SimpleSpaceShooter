from pygame import KEYDOWN, K_RETURN
from pygame.surface import Surface
from pygame.event import Event
from pygame.font import SysFont

from .screen import Screen
from ..background import Background


class GameOverScreen(Screen):
    _background: Background
    _game_over_text: Surface
    _game_over_text_pos: tuple
    _info_text: Surface
    _info_text_pos: tuple

    def __init__(self, window_dimension: tuple[int, int], fps: int):
        super().__init__(window_dimension, fps)
        self._background = Background(window_dimension)
        font = SysFont('Comic Sans MS', 30)
        self._game_over_text = font.render('GAME OVER!', False, (255, 0, 0))
        self._game_over_text_pos = (
            (self._window_width / 2) - (self._game_over_text.get_width() / 2),
            (self._window_height / 2) - (self._game_over_text.get_height() / 2)
        )
        self._info_text = font.render("Press 'Return' to restart", False, (255, 0, 0))
        self._info_text_pos = (
            (self._window_width / 2) - (self._info_text.get_width() / 2),
            self._game_over_text_pos[1] + self._game_over_text.get_height() + 3
        )

    def _handle_event(self, event: Event) -> 'Screen':
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                from .play_screen import PlayScreen
                return PlayScreen(self._window_dimension, self._fps)
        return self

    def _update(self) -> 'Screen':
        self._background.update()
        return self

    def _render(self, surface: Surface) -> 'Screen':
        self._background.draw(surface)
        surface.blit(self._game_over_text, self._game_over_text_pos)
        surface.blit(self._info_text, self._info_text_pos)
        return self
