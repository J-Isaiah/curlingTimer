import pygame

from src.gui.button import Button
from src.gui.text_formats import draw_header
from src.logic.game_config import GameState, GameMode


class ScreenManager:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_font = pygame.font.SysFont(None, 36, bold=True)
        self.default_background_color = (46, 52, 64)

        self.menu_buttons: dict[GameMode, Button] = {}
        self.init_menu()

    def init_menu(self):
        self.screen.fill(self.default_background_color)

        draw_header(screen=self.screen, screen_width=self.screen_width, screen_height=self.screen_height, text='Menu')
        button_height = self.screen_height // 6
        button_width = self.screen_width // 2
        spacing = self.screen_height // 20

        total_height = 2 * button_height + spacing

        start_y = (self.screen_height - total_height) // 2

        button_center_x = (self.screen_width - button_width) // 2
        y_doubles = start_y
        y_fours = y_doubles + button_height + spacing

        game_mode_fours = Button(
            rect=(button_center_x, y_doubles, button_width, button_height),
            color=(136, 192, 208), text="Fours", text_color=(236, 239, 244),
            font=self.default_font)
        game_mode_doubles = Button(
            rect=(button_center_x, y_fours, button_width, button_height),
            color=(136, 192, 208), text="Doubles",
            text_color=(236, 239, 244),
            font=self.default_font)

        self.menu_buttons[GameMode.FOURS] = game_mode_fours
        self.menu_buttons[GameMode.DOUBLES] = game_mode_doubles

    def draw_menu(self):
        for button in self.menu_buttons.values():
            button.draw(self.screen)
        pygame.display.flip()

    def init_settings(self):
        self.screen.fill(self.default_background_color)
        draw_header(self.screen, self.screen_width, self.screen_height, text="Settings")

        pygame.display.flip()
