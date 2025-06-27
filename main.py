import time

from src.gui.ui import ScreenManager
from src.logic.game_config import GameConfig, GameState
from src.logic.game_manager import GameManager
from src.logic.timer import Timer


def menu_state():
    new_state = GameState.MENU
    while True:
        if new_state == GameState.START:
            break
    return new_state


def start_game(game_manager: GameManager):
    game_manager.start_game()
    return GameState.START


def main():
    game_config = GameConfig()
    current_state = game_config.current_state
    screen_manager = ScreenManager()
    game_manager = None

    while True:

        if current_state == GameState.MENU:
            current_state = menu_state()

        if current_state == GameState.START:
            game_manager = GameManager(game_config, scheduled_start_time=time.time())
            current_state = start_game(game_manager)
