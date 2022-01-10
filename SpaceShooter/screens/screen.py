from abc import ABCMeta, abstractmethod

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.event import Event


class Screen(metaclass=ABCMeta):
    _window_dimension: tuple[int, int]
    _window_width: int
    _window_height: int
    _fps: int
    _clock: Clock

    def __init__(self,
                 window_dimension: tuple[int, int],
                 fps: int):
        self._window_dimension = window_dimension
        self._window_width, self._window_height = window_dimension
        self._fps = fps
        self._clock = Clock()

    @abstractmethod
    def _handle_event(self, event: Event) -> 'Screen':
        ...

    @abstractmethod
    def _update(self) -> 'Screen':
        ...

    @abstractmethod
    def _render(self, surface: Surface) -> 'Screen':
        ...

    def handle_event(self, event: Event) -> 'Screen':
        return self._handle_event(event)

    def update(self) -> 'Screen':
        return self._update()

    def render(self, surface: Surface) -> 'Screen':
        screen = self._render(surface)
        pygame.display.update()
        self._clock.tick(self._fps)
        return screen
