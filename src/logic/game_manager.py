import sys
import time

from src.logic import rock_manager
from src.logic.game_config import GameConfig, GameMode, GameState
from src.logic.rock_manager import RockTracker, FoursTracker, DoublesTracker
from src.logic.timer import Timer
from enum import Enum, nonmember


class GameManagerStates(Enum):
    END_START = 'end_start'
    BREAK = 'break'
    GAME_OVER = 'game_over'
    LAST_END = 'last_end'


class GameManager:
    def __init__(self, config: GameConfig, game_duration: float = None, scheduled_start_time: float = time.time(), ):
        self.config = config
        self._scheduled_start_time = scheduled_start_time
        self.game_duration = game_duration
        self.game_status = None
        self._timer = None
        self._rock_tracker = None
        self._max_end = 8
        self._cur_game_state = nonmember
        self.break_completed = True

    def start_game(self):
        self._timer = Timer(self._scheduled_start_time + 3, game_length=self.game_duration)

        if self.config.game_mode == GameMode.FOURS:
            self._rock_tracker = FoursTracker()
        else:
            self._rock_tracker = DoublesTracker()

        self.game_status = GameState.START

    def begin_new_end(self):
        if self._rock_tracker:
            print('Rock CUrrent end', self.get_rock_tracker.get_current_end)
            self._rock_tracker.start_new_end()
            print('Rock CUrrent end', self.get_rock_tracker.get_current_end)
            self.break_completed = False

    @property
    def get_rock_tracker(self):
        return self._rock_tracker

    @property
    def get_timer(self):
        return self._timer

    def change_game_state_to_break(self):
        self._cur_game_state = GameManagerStates.BREAK

    def change_game_state_to_game_over(self):
        self._cur_game_state = GameManagerStates.GAME_OVER

    def change_game_state_to_end_start(self):
        self._cur_game_state = GameManagerStates.END_START

    def get_game_manager_state(self):
        return self._cur_game_state

    def handle_one_rock_throw(self):
        print('Handling one rock throw --------')
        rock_tracker = self.get_rock_tracker
        current_rock = rock_tracker.get_current_rock()
        print('THROWING TIME ', current_rock.time_to_throw)

        if not current_rock.time_throw_started:
            current_rock.start_rock_throw()

        if current_rock.check_rock_thrown_precent() >= 1:
            print('STARTING NEXT ROCK')
            print('throw start time', current_rock.time_throw_started)
            rock_tracker.mark_rock_as_thrown()
            return True

        print('throw precent', current_rock.check_rock_thrown_precent())
        return False

    def handle_end(self):
        one_rock_thrown = self.handle_one_rock_throw()

        if one_rock_thrown and self.get_rock_tracker.is_end_over:
            self.change_game_state_to_break()
            self.get_rock_tracker.start_end_break()
            self.break_completed = False

        if self.get_rock_tracker.is_last_end:
            self.change_game_state_to_game_over()
            if self._cur_game_state == GameManagerStates.GAME_OVER:
                return GameManagerStates.GAME_OVER
            return GameManagerStates.LAST_END

        return GameManagerStates.END_START

    def handle_break(self):
        remaining = self.get_rock_tracker.get_break_time_remaining()

        print(f"[BREAK STATE] Remaining: {remaining}, InBreak: {self.get_rock_tracker.in_end_break}")

        if remaining <= 0:
            print('Resetting rocks: break is over')
            self.change_game_state_to_end_start()
            self.get_rock_tracker.in_end_break = False
            self.break_completed = True
            self.get_rock_tracker.start_new_end()

    def is_break_completed(self):
        return self.break_completed
