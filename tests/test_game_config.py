from src.logic.game_config import GameMode, GameConfig, GameState


def test_change_game_state():
    cfg = GameConfig()

    cfg.change_state(GameState.START)
    assert cfg.current_state == GameState.START


def test_change_game_mode():
    cfg = GameConfig()

    cfg.change_game_mode(GameMode.DOUBLES)
    assert cfg.game_mode == GameMode.DOUBLES


def test_current_state():
    cfg = GameConfig()

    assert isinstance(cfg.current_state, GameState)


def test_game_mode():
    cfg = GameConfig()

    assert isinstance(cfg.game_mode, GameMode)
