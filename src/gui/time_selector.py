import pygame
from datetime import datetime, timedelta


class TimeSelector:
    def __init__(self, screen, x, y, width, height, font_size, initial_unix_time, label="Time", step_minutes=15):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.unix_time = initial_unix_time
        self.label = label
        self.step = step_minutes * 60  # Convert to seconds
        self.last_clicked_time = 0
        self.click_delay = 150

        self.font = pygame.font.SysFont('Segoe UI', font_size, bold=True)
        self.label_font = pygame.font.SysFont('Segoe UI', int(font_size * 0.7), bold=False)

        # Button size is proportional
        self.button_width = width // 6
        self.button_height = height // 2

        self.left_button = pygame.Rect(x + 10, y + (height - self.button_height) // 2,
                                       self.button_width, self.button_height)
        self.right_button = pygame.Rect(x + width - self.button_width - 10,
                                        y + (height - self.button_height) // 2,
                                        self.button_width, self.button_height)

    def draw(self):
        # Draw container
        pygame.draw.rect(self.screen, (136, 192, 208), self.rect, border_radius=8)

        # Draw label
        label_surf = self.label_font.render(self.label, True, (236, 239, 244), )
        label_pos = (self.rect.centerx - label_surf.get_width() // 2, self.rect.top - self.label_font.get_height() - 5)
        self.screen.blit(label_surf, label_pos)

        # Draw time
        time_text = self._format_time()
        time_surf = self.font.render(time_text, True, (236, 239, 244), )
        time_rect = time_surf.get_rect(center=self.rect.center)
        self.screen.blit(time_surf, time_rect)

        # Draw buttons
        pygame.draw.rect(self.screen, (180, 180, 180), self.left_button, border_radius=5)
        pygame.draw.rect(self.screen, (180, 180, 180), self.right_button, border_radius=5)

        left_arrow = self.font.render("<", True, (0, 0, 0))
        right_arrow = self.font.render(">", True, (0, 0, 0))
        self.screen.blit(left_arrow, left_arrow.get_rect(center=self.left_button.center))
        self.screen.blit(right_arrow, right_arrow.get_rect(center=self.right_button.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            now = pygame.time.get_ticks()

            if now - self.last_clicked_time < self.click_delay:  # handles the dealay for a more controled click
                return
            if self.left_button.collidepoint(event.pos):
                print('left button clicked')
                self.unix_time -= self.step
                print(self.unix_time)
            elif self.right_button.collidepoint(event.pos):
                print('right button clicked')
                self.unix_time += self.step
            self.last_clicked_time = now

    def get_unix_time(self):
        print('returning unix time')
        return self.unix_time

    def _format_time(self):
        dt = datetime.fromtimestamp(self.unix_time)
        hour = dt.hour
        minute = dt.minute
        ampm = 'AM' if hour < 12 else 'PM'
        hour = hour % 12
        hour = 12 if hour == 0 else hour
        return f"{hour}:{minute:02d} {ampm}"
