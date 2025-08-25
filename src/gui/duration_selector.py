import pygame


class DurationSelector:
    def __init__(self, screen, x, y, width, height, font_size, initial_minutes=120, step=15, label="Game Duration"):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.minutes = initial_minutes
        self.step = step
        self.label = label
        self.last_checked_time = 0
        self.click_delay = 200

        self.font = pygame.font.SysFont('Segoe UI', font_size, bold=True)
        self.label_font = pygame.font.SysFont('Segoe UI', int(font_size * 0.7), bold=False)

        self.button_width = width // 6
        self.button_height = height // 2

        self.left_button = pygame.Rect(x + 10, y + (height - self.button_height) // 2,
                                       self.button_width, self.button_height)
        self.right_button = pygame.Rect(x + width - self.button_width - 10,
                                        y + (height - self.button_height) // 2,
                                        self.button_width, self.button_height)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, border_radius=8)

        label_surf = self.label_font.render(self.label, True, (236, 239, 244))
        label_pos = (self.rect.centerx - label_surf.get_width() // 2, self.rect.top - self.label_font.get_height() - 5)
        self.screen.blit(label_surf, label_pos)

        duration_text = f"{self.minutes} min"
        text_surf = self.font.render(duration_text, True, (0,0,0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.screen.blit(text_surf, text_rect)

        pygame.draw.rect(self.screen, (180, 180, 180), self.left_button, border_radius=5)
        pygame.draw.rect(self.screen, (180, 180, 180), self.right_button, border_radius=5)

        left_arrow = self.font.render("<", True, (0, 0, 0))
        right_arrow = self.font.render(">", True, (0, 0, 0))
        self.screen.blit(left_arrow, left_arrow.get_rect(center=self.left_button.center))
        self.screen.blit(right_arrow, right_arrow.get_rect(center=self.right_button.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            now = pygame.time.get_ticks()

            if now - self.last_checked_time < self.click_delay:
                return

            if self.left_button.collidepoint(event.pos):
                self.minutes = max(self.step, self.minutes - self.step)
            elif self.right_button.collidepoint(event.pos):
                self.minutes += self.step
            self.last_checked_time = now

    def get_duration_seconds(self):
        return self.minutes * 60
