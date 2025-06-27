import time

from src.logic.game_config import GameConfig
from src.logic.timer import Timer


class GameManager:
    def __init__(self, config: GameConfig, scheduled_start_time: float):
        self.config = config
        self._scheduled_start_time = scheduled_start_time

        self._timer = None
        self._rock_tracker = None
        self._current_end = 1

    def start_game(self):
        self._timer = Timer(self._scheduled_start_time + 3, )

    @property
    def get_timer(self):
        return self._timer
