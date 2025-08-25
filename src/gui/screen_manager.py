import pygame

from src.gui.button import Button
from src.gui.text_formats import draw_header, draw_text
from src.logic.Helper.round_time import get_time_rounded_to_nearest_15_min
from src.gui.duration_selector import DurationSelector
from src.logic.game_config import GameMode
from src.gui.time_selector import TimeSelector


class ScreenManager:
    def __init__(self, screen, screen_width, screen_height):
        self.start_game_button = None
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_font = pygame.font.SysFont('Segoe UI', max(36, screen_height // 24), bold=True)
        self.default_background_color = (0,0,0)
        self.start_selector = None
        self.duration_selector = None

        self.menu_buttons: dict[GameMode, Button] = {}
        self.init_menu()

    def init_menu(self):
        self.screen.fill(self.default_background_color)

        draw_header(screen=self.screen, screen_width=self.screen_width, screen_height=self.screen_height, text='Menu')

        button_height = self.screen_height // 6
        button_width = self.screen_width // 2
        spacing = self.screen_height // 10

        total_height = 2 * button_height + spacing

        start_y = (self.screen_height - total_height) // 2

        button_center_x = (self.screen_width - button_width) // 2
        y_doubles = start_y
        y_fours = y_doubles + button_height + spacing

        game_mode_fours = Button(
            rect=(button_center_x, y_doubles, button_width, button_height),
            text="Fours",
            font=self.default_font)
        game_mode_doubles = Button(
            rect=(button_center_x, y_fours, button_width, button_height),
            text="Doubles",
            font=self.default_font)
        self.menu_buttons[GameMode.DOUBLES] = game_mode_doubles
        self.menu_buttons[GameMode.FOURS] = game_mode_fours

    def draw_menu(self):
        for button in self.menu_buttons.values():
            button.draw(self.screen)
        pygame.display.flip()
        pygame.event.clear()

    def init_and_draw_settings(self, game_mode: GameMode, ):
        button_height = self.screen_height // 16
        button_width = self.screen_width // 8
        total_height = 2 * button_height
        start_y = (self.screen_height - total_height) // 1
        button_center_x = (self.screen_width - button_width) // 2

        self.screen.fill(self.default_background_color)
        draw_header(self.screen, self.screen_width, self.screen_height, text="Settings")

        draw_text(self.screen, f'Game Mode: {game_mode.value.capitalize()}', self.screen_width, self.screen_height,
                  size_ratio=1 / 12,
                  position_ratio=(.5, .3), center=True, )
        now = get_time_rounded_to_nearest_15_min()

        w, h = self.screen_width // 2, self.screen_height // 10
        font_size = h // 2

        self.start_selector = TimeSelector(self.screen, self.screen_width // 4, int(self.screen_height * 0.42),
                                           w, h, font_size, now, label="Game Start Time", )
        if game_mode == GameMode.FOURS:
            initial_game_duration = 120
        else:
            initial_game_duration = 90

        self.duration_selector = DurationSelector(self.screen, self.screen_width // 4, int(self.screen_height * 0.62),
                                                  w, h, font_size, initial_minutes=initial_game_duration,
                                                  label="Game Duration")

        self.start_game_button = Button(rect=(button_center_x, start_y, button_width, button_height),
                                        font=self.default_font,
                                        text='Start Game')
        self.start_game_button.draw(self.screen)
        self.start_selector.draw()
        self.duration_selector.draw()
        pygame.display.flip()
