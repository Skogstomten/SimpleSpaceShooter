# import pygame
# from pygame.locals import QUIT
#
# from .obstacle_manager import ObstacleManager
# from .player import Player
#
# WINDOW_DIMENTION = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 600
# COLOR_BLACK = (0, 0, 0)
# FPS = 60
#
#
# def main():
#     pygame.init()
#     running = True
#     game_over = False
#     display_surface = pygame.display.set_mode(WINDOW_DIMENTION)
#     player = Player(WINDOW_DIMENTION, display_surface)
#     clock = pygame.time.Clock()
#     obstacle_manager = ObstacleManager(display_surface, player, clock, WINDOW_DIMENTION)
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 running = False
#             player.handle_events(event)
#             obstacle_manager.handle_event(event)
#
#         display_surface.fill(COLOR_BLACK)
#         player.draw()
#         result = obstacle_manager.update()
#         player.update_position_from_input()
#         if result == 'GAME_OVER':
#             game_over = True
#             print(result)
#
#         pygame.display.flip()
#         clock.tick(FPS)
#
#
# if __name__ == '__main__':
#     main()

from .main import App

if __name__ == '__main__':
    app = App()
    app.execute()
