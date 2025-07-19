import pygame


def draw_header(screen, screen_width, screen_height, text="Settings"):
    font_size = max(36, screen_height // 9)
    header_font = pygame.font.SysFont('Segoe UI', font_size, bold=True)

    header_surface = header_font.render(text, True, (236, 239, 244))
    header_rect = header_surface.get_rect(center=(screen_width // 2, screen_height // 8))
    screen.blit(header_surface, header_rect)
