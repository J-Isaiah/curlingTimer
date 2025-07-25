import time

import pygame

from src.gui.screen_manager import ScreenManager
from src.logic.game_config import GameConfig, GameState
from src.logic.game_manager import GameManager, GameManagerStates
from src.logic.timer import Timer


def menu_state(screen_manager):
    screen_manager.draw_menu()


def handle_menu_buttons(screen_manager, game_config, event):
    for mode, button in screen_manager.menu_buttons.items():
        if button.is_clicked(event):
            game_config.change_game_mode(mode)
            game_config.change_state(GameState.SETTINGS)

    return screen_manager, game_config


def create_setting_state(screen_manager, game_mode, event):
    screen_manager.init_and_draw_settings(game_mode)


def handle_setting_screen_buttons(screen_manager, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        screen_manager.start_selector.handle_event(event)
        screen_manager.duration_selector.handle_event(event)
        screen_manager.start_selector.draw()
        screen_manager.duration_selector.draw()
    return screen_manager.start_game_button.is_clicked(event)


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
        GameState.START: False,
    }

    current_game_running = False

    while running:
        # Handles Event Listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit(1)

            if not setup_done[GameState.START]:
                if setup_done[GameState.MENU]:
                    screen_manager, game_config = handle_menu_buttons(screen_manager, game_config, event)

            if game_config.current_state == GameState.SETTINGS:
                if not setup_done[game_config.current_state]:
                    create_setting_state(screen_manager, game_config.game_mode, game_config, )
                    setup_done[GameState.SETTINGS] = True
                elif setup_done[GameState.SETTINGS]:
                    game_start = handle_setting_screen_buttons(screen_manager, event)
                    print('game Start', game_start)
                    if game_start:
                        print('Game Start Button Has been Clicked' * 100)
                        game_config.change_state(GameState.START)

        # Handles Screen Renders
        if game_config.current_state == GameState.MENU:
            menu_state(screen_manager)
            setup_done[GameState.MENU] = True

        if game_config.current_state == GameState.START:
            if not setup_done[GameState.START]:
                game_manager = GameManager(game_config,
                                           scheduled_start_time=screen_manager.start_selector.get_unix_time(),
                                           game_duration=screen_manager.duration_selector.get_duration_seconds(), )
                game_manager.start_game()
                setup_done[GameState.START] = True
                screen_manager.screen.fill((0, 0, 0))  # Replace with new screen switch logic
                current_game_running = True

                game_manager.start_game()
            elif current_game_running and game_manager:
                if game_manager.get_timer.is_pre_game:
                    # Pre Game Count Down
                    print(game_manager.get_timer.get_pre_game_time())
                    print('still in if')
                else:
                    print('game Has Started')
                    remaining_game_time = game_manager.get_timer.get_remaining_game_time()
                    print('remaining game time', remaining_game_time)

                    if remaining_game_time < 0:
                        print('Should not ber her')
                        # Game End protocol
                    else:
                        # Continue game protocol
                        print('BOOL CHECK', game_manager.get_rock_tracker.is_end_over,
                              game_manager.get_rock_tracker.is_in_break())
                        print('ends', game_manager.get_rock_tracker.get_ends_left())

                        if ((
                                not game_manager.get_rock_tracker.is_end_over and not game_manager.get_rock_tracker.is_in_break())
                                and not game_manager.get_rock_tracker.end_started):
                            print('creaing new game manager rock')
                            game_manager.begin_new_end()  # if rocks remaining == 0 restart end
                            # Trigger break
                        elif not game_manager.is_break_completed():
                            print('In break loop')
                            # Break Screen
                            game_manager.handle_break()

                        elif game_manager.get_rock_tracker.get_ends_left() >= 0:
                            print('handle game time')
                            game_manager_state = game_manager.handle_end()
                            if game_manager_state == GameManagerStates.LAST_END:
                                print('we are on the last end')
                                quit()
                            # play time logic
                print('Else block end')

        # Rock update logic here
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
