import time

import pygame

from src.gui.screen_manager import ScreenManager
from src.logic.game_config import GameConfig, GameState
from src.logic.game_manager import GameManager
from src.logic.timer import Timer


def menu_state(screen_manager):
    screen_manager.draw_menu()


def handle_menu_buttons(screen_manager, game_config, event):
    for mode, button in screen_manager.menu_buttons.items():
        if button.is_clicked(event):
            game_config.change_game_mode(mode)
            game_config.change_state(GameState.SETTINGS)

    return screen_manager, game_config


def create_setting_state(screen_manager, game_mode, game_config, event):
    screen_manager.init_and_draw_settings(game_mode)


def handle_setting_screen_buttons(screen_manager, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        screen_manager.start_selector.handle_event(event)
        screen_manager.duration_selector.handle_event(event)
        screen_manager.start_selector.draw()
        screen_manager.duration_selector.draw()


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

    setup_done = {
        GameState.MENU: False,
        GameState.SETTINGS: False,
        GameState.START: False
    }

    while running:
        # Handles Event Listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit(1)

            if setup_done[GameState.MENU]:
                screen_manager, game_config = handle_menu_buttons(screen_manager, game_config, event)
            elif setup_done[GameState.SETTINGS]:
                handle_setting_screen_buttons(screen_manager, event)
                print('unix time: ', screen_manager.start_selector.get_unix_time())

        # Handles Screen Renders
        if game_config.current_state == GameState.MENU:
            menu_state(screen_manager)
            setup_done[GameState.MENU] = True

        if game_config.current_state == GameState.SETTINGS:
            if not setup_done[game_config.current_state]:
                create_setting_state(screen_manager, game_config.game_mode, game_config, event)
                setup_done[GameState.SETTINGS] = True
            handle_setting_screen_buttons(screen_manager, event)

        if game_config.current_state == GameState.START:
            if not setup_done[GameState.START]:
                game_manager = GameManager(game_config, event, scheduled_start_time=time.time(), )
                setup_done[GameState.START] = True
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
