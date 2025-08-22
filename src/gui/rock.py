import pygame
import asyncio
import platform

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_caption("Curling Stone")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
GRAY = (100, 100, 100)
DARK_GRAY = (70, 70, 70)
LIGHT_GRAY = (180, 180, 180)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Stone dimensions
stone_width = 220
stone_height = 160
handle_width = 90
handle_height = 40

# Main loop function
def setup():
    pass

def update_loop():
    screen.fill((255, 255, 255))  # White background

    # Draw the stone body (elliptical shape)
    pygame.draw.ellipse(screen, GRAY, (90, 70, stone_width, stone_height))
    pygame.draw.rect(screen, LIGHT_GRAY, (90, 70 + stone_height/3, stone_width, stone_height/3), border_radius=20)

    # Draw the handle
    pygame.draw.polygon(screen, RED, [
        (145, 60), (255, 60), (265, 80), (245, 100), (155, 100), (135, 80)
    ])
    pygame.draw.line(screen, BLACK, (200, 100), (200, 130), 5)  # Handle support
    pygame.draw.line(screen, BLACK, (170, 80), (230, 80), 3)  # Handle curve detail

    # Add subtle edge details
    pygame.draw.ellipse(screen, DARK_GRAY, (90, 70, stone_width, 10), 2)  # Top edge
    pygame.draw.ellipse(screen, DARK_GRAY, (90, 220, stone_width, 10), 2)  # Bottom edge

    pygame.display.flip()

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / 60)  # Control frame rate

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())