import pygame
from pygame.surface import Surface
from pygame.font import Font
from pygame.event import Event
from pygame.rect import Rect
from typing import Tuple


class Button:
    def __init__(
            self,
            rect: Tuple[int, int, int, int],

            font: Font,
            color: Tuple[int, int, int] = (255,255,255),
            text_color: Tuple[int, int, int] =(0, 0, 1),
            text: str = 'Text Missing',
    ) -> None:
        self.rect: Rect = pygame.Rect(rect)
        self.color: Tuple[int, int, int] = color
        self.text: str = text
        self.font: Font = font
        self.text_color: Tuple[int, int, int] = text_color

        self.text_surface: Surface = font.render(text, True, text_color)
        self.text_rect: Rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event: Event) -> bool:
        print('Mouse Button Is clicked')
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
