from pygame import Surface
from pygame import KEYDOWN, K_SPACE
from pygame.event import Event
from pygame.font import SysFont

from .screen import Screen
from .play_screen import PlayScreen
from ..background import Background


class StartScreen(Screen):
    _background: Background
    _text: Surface

    def __init__(self, window_dimension: tuple[int, int], fps: int):
        super(StartScreen, self).__init__(window_dimension, fps)
        self._background = Background(window_dimension)
        font = SysFont('Comic Sans MS', 30)
        self._text = font.render("Press 'SPACE' to start!", False, (255, 0, 0))

    def _handle_event(self, event: Event) -> 'Screen':
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                return PlayScreen(self._window_dimension, self._fps)
        return self

    def _update(self) -> 'Screen':
        self._background.update()
        return self

    def _render(self, surface: Surface) -> 'Screen':
        self._background.draw(surface)
        surface.blit(self._text, (
            (self._window_width / 2) - (self._text.get_width() / 2),
            (self._window_height / 2) - (self._text.get_height() / 2)
        ))
        return self
