import time

import pygame

from src.gui.screen_manager import ScreenManager
from src.logic.game_config import GameConfig, GameState
from src.logic.game_manager import GameManager
from src.logic.timer import Timer


def menu_state(screen_manager):
    new_state = GameState.MENU
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                new_state = GameState.START
        screen_manager.draw_menu()
    return new_state, screen_manager


def start_game(game_manager: GameManager):
    game_manager.start_game()
    return GameState.START


def main():
    pygame.init()
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    screen.fill((46, 52, 64))

    game_config = GameConfig()
    current_state = game_config.current_state
    screen_manager = ScreenManager(screen, screen_width, screen_height)
    game_manager = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == GameState.MENU:
            current_state, screen_manager = menu_state(screen_manager)

        if current_state == GameState.START:
            game_manager = GameManager(game_config, scheduled_start_time=time.time())
            current_state = start_game(game_manager)
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
