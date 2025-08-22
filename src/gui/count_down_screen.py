import pygame
import sys


import sys
import pygame

def end_game_screen(screen_manager, game_config=None, event=None):
    screen = screen_manager
    w, h = screen.get_size()
    u = min(w, h)

    # --- background & border ---
    screen.fill((0, 0, 0))
    border_thickness = max(2, int(u * 0.004))
    inset = max(6, int(u * 0.01))
    border_rect = pygame.Rect(inset, inset, w - 2*inset, h - 2*inset)
    pygame.draw.rect(screen, (0, 128, 255), border_rect, width=border_thickness)

    # --- text ---
    size_top = max(12, int(h * 0.18))
    size_bot = max(12, int(h * 0.25))
    font_top = pygame.font.SysFont("Courier New", size_top, bold=True)
    font_bot = pygame.font.SysFont("Courier New", size_bot, bold=True)
    white = (255, 255, 255)

    good_surf    = font_top.render("Good",    False, white)
    curling_surf = font_bot.render("Curling", False, white)

    left_margin   = int(w * 0.05)
    top_margin    = int(h * 0.08)
    bottom_margin = int(h * 0.22)  # a bit larger to make room for buttons

    x = border_rect.left + left_margin
    y_top = border_rect.top + top_margin
    y_bot = border_rect.bottom - curling_surf.get_height() - bottom_margin

    screen.blit(good_surf, (x, y_top))
    screen.blit(curling_surf, (x, y_bot))

    # --- buttons (dynamic sizes) ---
    btn_h = max(36, int(h * 0.10))
    btn_w = max(160, int(w * 0.28))
    btn_gap = int(w * 0.04)

    total_w = btn_w * 2 + btn_gap
    btn_y = border_rect.bottom - btn_h - int(h * 0.06)
    btn_x_start = (w - total_w) // 2

    new_rect  = pygame.Rect(btn_x_start, btn_y, btn_w, btn_h)
    quit_rect = pygame.Rect(btn_x_start + btn_w + btn_gap, btn_y, btn_w, btn_h)

    mouse_pos = pygame.mouse.get_pos()
    def draw_button(rect, label, hovered):
        base = (230, 230, 230) if not hovered else (255, 255, 255)
        edge = (30, 30, 30)
        pygame.draw.rect(screen, base, rect, border_radius=12)
        pygame.draw.rect(screen, edge, rect, width=2, border_radius=12)
        f = pygame.font.SysFont("Courier New", max(14, int(rect.height * 0.45)), bold=True)
        txt = f.render(label, True, (0, 0, 0))
        screen.blit(txt, txt.get_rect(center=rect.center))

    draw_button(new_rect,  "New Game", new_rect.collidepoint(mouse_pos))
    draw_button(quit_rect, "Quit",     quit_rect.collidepoint(mouse_pos))

    # --- click handling ---
    if event and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if new_rect.collidepoint(event.pos):
            return True
        if quit_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()

    return False




def setup_timer(screen, time_left: float, total_time, is_set_up_time, h, w, current_end):
    if is_set_up_time: # set up time
        screen.fill((164, 160, 112))
        bar_color=(255,255,0)
        top_text = 'Set Up Time left...'
    elif time_left <= 0: # ends game
        end_game_screen(screen)
    elif current_end >=8 or time_left <=900:
        top_text = 'Final End...'
        screen.fill((139,0,0))
        bar_color = 0,255,0
    else: # Game time
        top_text = f'End {current_end} of 8'
        screen.fill((1, 61, 1))
        bar_color=(0,255,0)


    # Bar size
    bar_w = w * 0.65
    bar_h = h * 0.14

    bar_x = (w - bar_w) / 2
    bar_y = ((h - (h // 3)) - bar_h) / 2

    progress_ratio = max(0, min(1, time_left / total_time))
    progress_width = bar_w * progress_ratio
    pygame.draw.rect(screen, (60, 60, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=10)

    pygame.draw.rect(screen, bar_color, (bar_x, bar_y, progress_width, bar_h), border_radius=10)

    font = pygame.font.SysFont(None, int(bar_h * 0.6))
    if time_left > 3600:
        time_text = f"{int((time_left // 3600))}:{int((time_left % 3600)//60):02d}:{int(time_left % 60):02d}"
    elif time_left > 60:
        time_text = f"{int(time_left // 60):02d}:{int(time_left % 60):02d}"
    else:
        time_text = f"{int(time_left)}"
    time_text = font.render(f"{time_text}s", True, (0, 0, 0))
    text_rect = time_text.get_rect(center=(w / 2, bar_y + bar_h / 2))
    screen.blit(time_text, text_rect)

def draw_headding(screen, current_end: int, is_set_up_time: bool, h: int, w: int, time_left: float):
    if is_set_up_time:
        text = "Set UP"
    elif current_end >= 8 or time_left <= 900:
        text = f"End {current_end} of 8 (Final)"
    else:
        print(current_end)
        text = f"End {current_end} of 8"

    font_size = max(18, int(h * 0.08))
    font = pygame.font.SysFont("Courier New", font_size, bold=True)

    # Render text
    text_surface = font.render(text, True, (0, 0, 0))  # black text
    text_rect = text_surface.get_rect(center=(w // 2, int(h * 0.08)))

    padding_x = int(w * 0.02)
    padding_y = int(h * 0.01)
    bg_rect = pygame.Rect(
        text_rect.left - padding_x,
        text_rect.top - padding_y,
        text_rect.width + 2 * padding_x,
        text_rect.height + 2 * padding_y
    )
    pygame.draw.rect(screen, (200, 200, 200), bg_rect, border_radius=6)
    pygame.draw.rect(screen, (50, 50, 50), bg_rect, width=2, border_radius=6)

    screen.blit(text_surface, text_rect)

def draw_play_screen(screen, current_end, is_set_up_time: bool, time_left: float, height, width, total_time):

    setup_timer(screen=screen, time_left=time_left, total_time=total_time,
                is_set_up_time=is_set_up_time, h=height, w=width, current_end=current_end)
    draw_headding(screen, current_end, is_set_up_time, height, width, time_left)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    # Start window (resizable)
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.display.set_caption("Curling Timer")

    # Initial state
    is_set_up = False
    time_left = 100
    total_time = 600
    current_end = 1

    running = True
    while running:
        # --- Handle events ---
        event = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.VIDEORESIZE:  # handle resizing
                screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            else:
                event = e

        time_left -= clock.get_time() / 1000  # subtract seconds
        if time_left < 0:
            time_left = 0

        screen_width, screen_height = screen.get_size()

        draw_play_screen(
            screen,
            current_end=current_end,
            is_set_up_time=is_set_up,
            time_left=time_left,
            height=screen_height,
            width=screen_width,
            total_time=total_time,
        )

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

