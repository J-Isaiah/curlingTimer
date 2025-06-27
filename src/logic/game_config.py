# Defined States
import logging
from enum import Enum


class GameState(Enum):
    MENU = "menu"
    SETTINGS = "settings"
    START = "start"
    GAME = "game"
    END = "end"


class GameMode(Enum):
    FOURS = "fours"
    DOUBLES = "doubles"


class GameConfig:
    def __init__(self):
        self._current_state = GameState.MENU
        self._game_mode = GameMode.FOURS
        self._start_time = 0

    def change_state(self, new_state):
        if not isinstance(new_state, GameState):
            logging.warning(f'New state {new_state} is not an instance of {GameState} and instead "{type(new_state)}')
            return
        self._current_state = new_state

    def change_game_mode(self, new_settings):
        if not isinstance(new_settings, GameMode):
            logging.warning(
                f'New state {new_settings} is not an instance of {GameMode} and instead "{type(new_settings)}')
            return
        self._game_mode = new_settings

    @property
    def current_state(self):
        return self._current_state

    @property
    def game_mode(self):
        return self._game_mode
