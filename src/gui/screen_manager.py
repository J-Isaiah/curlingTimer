import pygame

from src.gui.button import Button


class ScreenManager:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_font = pygame.font.SysFont(None, 36, bold=True)

    def draw_menu(self):
        game_mode_fours = Button(rect=(100, 100, 100, 100), color=(255, 255, 255), text="Fours", text_color=(0, 0, 0),
                                 font=self.default_font)
        game_mode_fours.draw(self.screen)

        game_mode_fours.draw(self.screen)
        pygame.display.flip()
