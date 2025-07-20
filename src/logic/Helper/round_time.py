import time


def get_time_rounded_to_nearest_15_min() -> int:
    interval = 15 * 60
    return round(int(time.time()) / interval) * interval
