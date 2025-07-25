import time
import math


def get_time_rounded_to_nearest_15_min() -> int:
    interval = 15 * 60
    return math.ceil(int(time.time()) / interval) * interval
