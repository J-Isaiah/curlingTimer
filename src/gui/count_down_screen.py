import pygame
import sys

from src.logic.game_manager import GameManager


def end_game_screen(screen_manager, game_config=None, event=None):
    screen = screen_manager
    w, h = screen.get_size()
    u = min(w, h)

    screen.fill((0, 0, 0))
    border_thickness = max(2, int(u * 0.004))
    inset = max(6, int(u * 0.01))
    border_rect = pygame.Rect(inset, inset, w - 2 * inset, h - 2 * inset)
    pygame.draw.rect(screen, (0, 128, 255), border_rect, width=border_thickness)

    size_top = max(12, int(h * 0.18))
    size_bot = max(12, int(h * 0.25))
    font_top = pygame.font.SysFont("Courier New", size_top, bold=True)
    font_bot = pygame.font.SysFont("Courier New", size_bot, bold=True)
    white = (255, 255, 255)

    good_surf = font_top.render("Good", False, white)
    curling_surf = font_bot.render("Curling", False, white)

    left_margin = int(w * 0.05)
    top_margin = int(h * 0.08)
    bottom_margin = int(h * 0.22)

    x = border_rect.left + left_margin
    y_top = border_rect.top + top_margin
    y_bot = border_rect.bottom - curling_surf.get_height() - bottom_margin

    screen.blit(good_surf, (x, y_top))
    screen.blit(curling_surf, (x, y_bot))

    btn_h = max(36, int(h * 0.10))
    btn_w = max(160, int(w * 0.28))
    btn_gap = int(w * 0.04)

    total_w = btn_w * 2 + btn_gap
    btn_y = border_rect.bottom - btn_h - int(h * 0.06)
    btn_x_start = (w - total_w) // 2

    new_rect = pygame.Rect(btn_x_start, btn_y, btn_w, btn_h)
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

    draw_button(new_rect, "New Game", new_rect.collidepoint(mouse_pos))
    draw_button(quit_rect, "Quit", quit_rect.collidepoint(mouse_pos))

    if event and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if new_rect.collidepoint(event.pos):
            return True
        if quit_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()

    return False


def setup_timer(screen, time_left: float, total_time, is_set_up_time, h, w, current_end=None,
                is_break_time=None, game_manager=None):
    print('Is game comming to an end check', game_manager.get_rock_tracker.is_last_end,
          game_manager.get_rock_tracker.get_rocks_left_in_end, game_manager.get_rock_tracker.get_rocks_left_in_end <= 0)
    if is_set_up_time:  # set up time
        screen.fill((164, 160, 112))

    elif time_left <= 0 or current_end <= 0 or (
            game_manager.get_rock_tracker.is_last_end and game_manager.get_rock_tracker.get_rocks_left_in_end <= 0):  # ends game
        print('ending Game')
        end_game_screen(screen)
        return True
    elif is_break_time:
        screen.fill((77, 77, 77))
    elif current_end >= 8 or time_left <= game_manager.get_rock_tracker.last_end_time:
        if time_left <= game_manager.get_rock_tracker.last_end_time:
            game_manager.get_rock_tracker.is_last_end = True
        screen.fill((135, 0, 0))
    else:  # Game time
        screen.fill((87, 183, 87))
    bar_color = (0, 255, 251)

    bar_w = w * 0.65
    bar_h = h * 0.14

    bar_x = (w - bar_w) / 2
    bar_y = ((h - (h // 3)) - bar_h) / 2

    progress_ratio = max(0, min(1, time_left / total_time))
    progress_width = bar_w * progress_ratio
    pygame.draw.rect(screen, (60, 60, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=10)
    fill_x = bar_x + (bar_w - progress_width)
    pygame.draw.rect(screen, bar_color, (fill_x, bar_y, progress_width, bar_h), border_radius=10)

    font = pygame.font.SysFont(None, int(bar_h * 1.2))
    if time_left > 3600:
        time_text = f"{int((time_left // 3600))}:{int((time_left % 3600) // 60):02d}:{int(time_left % 60):02d}"
    elif time_left > 60:
        time_text = f"{int(time_left // 60):02d}:{int(time_left % 60):02d}"
    else:
        time_text = f"{int(time_left)}"
    time_text = font.render(f"{time_text}s", True, (0, 0, 0))
    text_rect = time_text.get_rect(center=(w / 2, bar_y + bar_h / 2))
    screen.blit(time_text, text_rect)
    return False


def draw_headding(screen, current_end: int, is_set_up_time: bool, h: int, w: int, time_left: float,
                  is_break_time=None, break_time_left=None):
    if is_set_up_time:
        text = "Set UP"
    elif is_break_time:
        text = f"End Starts in {int(break_time_left)}"
    elif current_end >= 8 or time_left <= 900:
        text = f"End {current_end} of 8 (Final)"
    else:
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


def draw_rocks(screen, current_end: int, is_set_up_time: bool, h: int, w: int,
               time_left, is_break_time, break_time_left, gm: GameManager):
    # --- Rock box ---
    box_top = int(h * 0.45)
    box_bottom = int(h * 0.98)
    box_height = box_bottom - box_top
    box_width = w * 0.95

    cols = gm.get_rock_tracker.get_total_rocks_per_end // 2
    rows = 2
    gap_ratio = 0.05

    stone_size_x = box_width / (cols + (cols - 1) * gap_ratio)
    stone_size_y = box_height / (rows + (rows - 1) * gap_ratio)
    stone_size = int(min(stone_size_x, stone_size_y))
    gap = int(stone_size * gap_ratio)

    total_w = cols * stone_size + (cols - 1) * gap
    total_h = rows * stone_size + (rows - 1) * gap
    start_x = (w - total_w) // 2
    start_y = box_top + (box_height - total_h) // 2

    red_png = pygame.image.load("yellow_rock.png").convert_alpha()
    yellow_png = pygame.image.load("red_rock.png").convert_alpha()
    red_stone = pygame.transform.smoothscale(red_png, (stone_size, stone_size))
    yellow_stone = pygame.transform.smoothscale(yellow_png, (stone_size, stone_size))

    try:
        rocks_left = gm.get_rock_tracker.get_rocks_left_in_end
        percent_thrown = gm.get_rock_tracker.get_current_rock().check_rock_thrown_precent()
        current_rock_idx = gm.get_rock_tracker.current_rock
    except Exception:
        return

    max_rocks = cols * rows
    rocks_thrown = max_rocks - rocks_left

    rock_index = 0
    for col in range(cols):
        for row in range(rows):  # row 0 = red, row 1 = yellow
            x = start_x + col * (stone_size + gap)
            y = start_y + row * (stone_size + gap)

            if rock_index >= rocks_thrown:
                stone_surf = red_stone if row == 0 else yellow_stone

                if rock_index == current_rock_idx:
                    # Eating effect: 0 = full, 1 = gone
                    visible_w = int(stone_size * (1 - percent_thrown))
                    if visible_w > 0:
                        # Clip from the right side instead of left
                        clip_rect = pygame.Rect(stone_size - visible_w, 0, visible_w, stone_size)
                        screen.blit(stone_surf, (x + (stone_size - visible_w), y), area=clip_rect)

                else:
                    screen.blit(stone_surf, (x, y))

            rock_index += 1


def draw_play_screen(screen, current_end, is_set_up_time: bool, game_manager, time_left: float, height, width,
                     total_time, is_break_time=None, break_time_left=None):
    game_over = setup_timer(screen=screen, time_left=time_left, total_time=total_time,
                            is_set_up_time=is_set_up_time, h=height, w=width, current_end=current_end,
                            is_break_time=is_break_time,
                            game_manager=game_manager)
    draw_headding(screen, current_end, is_set_up_time, height, width, time_left, is_break_time, break_time_left)
    draw_rocks(screen, current_end, is_set_up_time, height, width, time_left, is_break_time, break_time_left,
               game_manager)

    return game_over
