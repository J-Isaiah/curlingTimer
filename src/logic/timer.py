import time


class Timer:
    def __init__(self, scheduled_start_time: float, game_length: float = 7200):
        self._start_time = scheduled_start_time
        self._game_end_time = self._start_time + game_length

    @property
    def is_pre_game(self) -> bool:
        return time.time() < self._start_time

    def get_pre_game_time(self) -> float:
        return max(0.0, self._start_time - time.time())

    def is_game_over(self) -> bool:
        return time.time() > self._game_end_time

    def get_remaining_game_time(self) -> float:
        if self.is_pre_game:
            print('Not Supposed to be here')
            return 0.0
        return max(0.0, self._game_end_time) - time.time()

    def get_elapsed_game_time(self) -> float:
        if self.is_pre_game:
            return 0.0
        return min(time.time() - self._start_time, self._game_end_time - self._start_time)

    def get_remaining_pre_game_time(self):
        return self._start_time - time.time() if self.is_pre_game else 0.0


if __name__ == '__main__':
    start = Timer(time.time())
    print(start.is_pre_game)
    print(start.is_game_over())
    while True:
        print(start.get_remaining_game_time())
