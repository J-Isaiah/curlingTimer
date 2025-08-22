import time


class Rock:
    def __init__(self, seconds_to_throw):
        self.time_to_throw: int = seconds_to_throw
        self.time_throw_started = 0
        self._thrown: bool = False
        self.percent_thrown: float = .00

    def mark_rock_as_thrown(self):
        self._thrown = True

    def reset_rock_status(self):
        self._thrown = False
        self.percent_thrown = .00
        self.time_throw_started = 0

    def start_rock_throw(self):
        self.time_throw_started = time.time()

    def check_rock_thrown_precent(self):
        if self.time_throw_started == 0:
            return 0.0  # Throw hasn't started

        elapsed_time = time.time() - self.time_throw_started
        self.percent_thrown = min(elapsed_time / self.time_to_throw, 1.0)
        return self.percent_thrown

    @property
    def is_thrown(self):
        return self._thrown


class RockTracker:
    def __init__(self, total_rocks, end_break: int):
        self._end_break = end_break
        self.break_end_time = 0
        self.end_break_start_time = 0
        self._full_ends_left = 8
        self._current_end = 0
        self._total_rocks_per_end = total_rocks
        self.rocks_remaining_in_the_end = self._total_rocks_per_end
        self.current_rock = 0
        self._displayed_rocks = []
        self.time_mapping = []
        self.current_end_break = 0
        self.in_end_break = False
        self.end_started = False
        self.is_first_end = True
        self.is_last_end = False

    def start_new_end(self):

        print('starting new end')
        self.rocks_remaining_in_the_end = self._total_rocks_per_end
        self.current_rock = 0
        if len(self._displayed_rocks) == 0:
            for throw_time in self.time_mapping:
                self._displayed_rocks.append(Rock(throw_time))
                self._displayed_rocks.append(Rock(throw_time))
        else:
            for rock in self._displayed_rocks:
                print('resetting rocks')
                rock.reset_rock_status()
        self.end_started = True
        self.in_end_break = False
        if self.is_first_end:  # Shitty fix for double call issue
            self.is_first_end = False
            return
        self._current_end += 1
        self._full_ends_left -= 1

    def mark_rock_as_thrown(self):
        if self.current_rock < self._total_rocks_per_end:
            self._displayed_rocks[self.current_rock].mark_rock_as_thrown()
            self.rocks_remaining_in_the_end -= 1
            self.current_rock += 1
            return True
        return False

    @property
    def is_end_over(self):
        return self.rocks_remaining_in_the_end == 0

    @property
    def get_rocks_left_in_end(self):
        return self.rocks_remaining_in_the_end

    def start_end_break(self):
        self.in_end_break = True
        self.break_end_time = time.time() + self._end_break

    def is_in_break(self):
        return time.time() <= self.break_end_time

    def get_break_time_remaining(self):
        return max(self.break_end_time - time.time(), 0)

    def get_current_rock(self):
        return self._displayed_rocks[self.current_rock] if self._displayed_rocks else None

    def get_ends_left(self):
        return self._full_ends_left

    def is_last_end(self):
        return True if (self._full_ends_left == 1) else False

    @property
    def get_current_end(self):
        return self._current_end
    @property
    def get_total_rocks_per_end(self):
        return self._total_rocks_per_end


class DoublesTracker(RockTracker):
    def __init__(self):
        super().__init__(total_rocks=10, end_break=10)
        self.time_mapping = [55, 55, 60, 60, 65]
        print('DOUBLES TRACKER CREATED ')


class FoursTracker(RockTracker):
    def __init__(self):
        super(FoursTracker, self).__init__(total_rocks=16, end_break=5)
        self.time_mapping = [45, 45, 45, 50, 55, 60, 65, 65]
        print('FOURSE TRACKER CREATED ')
