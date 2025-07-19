import time

import pygame

from src.gui.screen_manager import ScreenManager
from src.logic.game_config import GameConfig, GameState
from src.logic.game_manager import GameManager
from src.logic.timer import Timer


def menu_state(screen_manager, game_config):
    new_state = GameState.MENU
    while new_state == GameState.MENU:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for mode, button in screen_manager.menu_buttons.items():
                    if button.is_clicked(event):
                        new_state = GameState.SETTINGS
                        game_config.change_game_mode(mode)
                        game_config.change_state(new_state)
        screen_manager.draw_menu()
    return screen_manager, game_config


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

    game_config = GameConfig()
    screen_manager = ScreenManager(screen, screen_width, screen_height)
    game_manager = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit(1)

        if game_config.current_state == GameState.MENU:
            screen_manager, game_config = menu_state(screen_manager, game_config)

        if game_config.current_state == GameState.START:
            game_manager = GameManager(game_config, scheduled_start_time=time.time())

        if game_config.current_state == GameState.SETTINGS:
            screen_manager.init_settings()

        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
