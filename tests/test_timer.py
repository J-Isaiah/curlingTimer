from src.logic.timer import Timer
import time


def test_is_pre_game_returns_true_when_start_time_is_future():
    timer = Timer(time.time() + 5)
    assert timer.is_pre_game()


def test_is_pre_game_returns_false_when_start_time_is_past():
    timer = Timer(time.time() - 5)
    assert not timer.is_pre_game()


def test_get_pre_game_time():
    future = time.time() + 5
    timer = Timer(future)
    remaining = timer.get_pre_game_time()
    assert 4.0 <= remaining <= 5.0


def test_is_game_returns_true_when_game_is_over():
    timer = Timer(time.time() - 50, game_length=5)

    assert timer.is_game_over()


def test_get_remaining_game_time_returns_zero_when_pre_game():
    timer = Timer(time.time() - 10, game_length=5)

    assert timer.get_remaining_game_time() == 0


def test_get_remaining_game_time_returns_remaining_time():
    timer = Timer(time.time() + 90, game_length=100)

    assert timer.get_remaining_game_time() < 90


def test_get_elapsed_game_time():
    timer = Timer(time.time(), game_length=100)

    assert timer.get_elapsed_game_time() < 2


def test_is_game_over_returns_false_during_game():
    timer = Timer(time.time() - 5, game_length=20)
    assert not timer.is_game_over()


def test_get_elapsed_game_time_caps_at_game_length():
    timer = Timer(time.time() - 100, game_length=90)
    assert timer.get_elapsed_game_time() == 90


def test_get_remaining_game_time_right_after_start():
    timer = Timer(time.time() - 0.01, game_length=5)
    assert 4.9 <= timer.get_remaining_game_time() <= 5.0
