import time
from src.logic.game_config import GameConfig
from src.logic.game_manager import GameManager
from src.logic.timer import Timer


def test_start_game_initializes_timer():
    fake_start_time = time.time()
    config = GameConfig()
    manager = GameManager(config, scheduled_start_time=fake_start_time)
    manager.start_game()

    timer = manager.get_timer
    assert isinstance(timer, Timer)
    assert abs(timer._start_time - (fake_start_time + 3)) < 0.1
