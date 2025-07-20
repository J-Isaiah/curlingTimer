import pygame

GLOBAL_BASE_FONT = 'Segoe UI Light'
GLOBAL_HEADER_FONT = 'Segoe UI'


def draw_header(screen, screen_width, screen_height, text="Settings"):
    font_size = max(36, screen_height // 9)
    header_font = pygame.font.SysFont(GLOBAL_HEADER_FONT, font_size, bold=True)

    header_surface = header_font.render(text, True, (236, 239, 244))
    header_rect = header_surface.get_rect(center=(screen_width // 2, screen_height // 8))
    screen.blit(header_surface, header_rect)


def draw_text(
        screen,
        text: str,
        screen_width: int,
        screen_height: int,
        position_ratio: tuple[float, float],
        size_ratio: float = 1 / 24,
        color: tuple[int, int, int] = (236, 239, 244),
        bold: bool = False,
        center: bool = False,
        font_name: str = GLOBAL_BASE_FONT,
):
    font_size = max(16, int(screen_height * size_ratio))  # Minimum font size safeguard

    font = pygame.font.SysFont(None, font_size, bold=bold)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    # Calculate actual pixel position from ratios
    pos_x = int(screen_width * position_ratio[0])
    pos_y = int(screen_height * position_ratio[1])

    if center:
        text_rect.center = (pos_x, pos_y)
    else:
        text_rect.topleft = (pos_x, pos_y)

    screen.blit(text_surface, text_rect)
