import pygame

from src.gui.button import Button
from src.logic.game_config import GameState, GameMode


class ScreenManager:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_font = pygame.font.SysFont(None, 36, bold=True)

        self.menu_buttons: dict[GameMode, Button] = {}
        self.init_menu()

    def init_menu(self):
        button_height = self.screen_height // 4
        button_width = self.screen_width // 2

        button_center_x = (self.screen_width - button_width) // 2
        button_center_y = (self.screen_height - button_height) // 2

        game_mode_fours = Button(
            rect=(button_center_x, button_center_y + button_height // 2, button_width, button_height),
            color=(255, 255, 255), text="Fours", text_color=(0, 0, 0),
            font=self.default_font)
        game_mode_doubles = Button(
            rect=(button_center_x, button_center_y - button_height // 2, button_width, button_height),
            color=(255, 255, 255), text="Doubles",
            text_color=(0, 0, 0),
            font=self.default_font)

        self.menu_buttons[GameMode.FOURS] = game_mode_fours
        self.menu_buttons[GameMode.DOUBLES] = game_mode_doubles

    def draw_menu(self):
        self.screen.fill("gray")
        for button in self.menu_buttons.values():
            button.draw(self.screen)
        pygame.display.flip()
