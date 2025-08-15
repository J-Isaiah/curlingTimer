import pygame
import sys


def setup_timer(screen, time_left, total_time, is_set_up_time, h, w):
    if is_set_up_time:
        # Background color for setup time
        screen.fill((164, 160, 112))

        # Bar size
        bar_w = w * 0.65
        bar_h = h * 0.14

        # Bar position (centered)
        bar_x = (w - bar_w) / 2
        bar_y = ((h-(h//3)) - bar_h) / 2

        # Calculate progress
        progress_ratio = max(0, min(1, time_left / total_time))
        progress_width = bar_w * progress_ratio

        # Draw background bar
        pygame.draw.rect(screen, (60, 60, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=10)

        # Draw progress
        pygame.draw.rect(screen, (200, 50, 50), (bar_x, bar_y, progress_width, bar_h), border_radius=10)

        # Draw time text
        font = pygame.font.SysFont(None, int(bar_h * 0.6))
        if time_left > 60:
            time_text = f"{int(time_left // 60 ):02d}:{int(time_left % 60):02d}"
        else:
            time_text = f"{int(time_left)}"
        time_text = font.render(f"{time_text}s", True, (255, 255, 255))
        text_rect = time_text.get_rect(center=(w / 2, bar_y + bar_h / 2))
        screen.blit(time_text, text_rect)


def draw_play_screen(screen, current_end, is_set_up_time: bool, time_left_in_set_up, height, width):
    if is_set_up_time:
        setup_timer(screen=screen, time_left=time_left_in_set_up, total_time=600,
                    is_set_up_time=is_set_up_time, h=height, w=width)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    is_set_up = True
    time_left = 600

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update timer
        time_left -= clock.get_time() / 1000  # subtract seconds
        if time_left < 0:
            time_left = 0

        draw_play_screen(screen, 3, is_set_up, time_left_in_set_up=time_left,
                         height=screen_height, width=screen_width)

        pygame.display.flip()
        clock.tick(30)
