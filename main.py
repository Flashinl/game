import pygame
import sys
import os
from components.ships import Ship, SHIP_STATS
from components.projectiles import Cannonball
from utils.helpers import draw_health_bar, draw_text
from components.game_state import GameState

# --- Game Constants ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WATER_BLUE = (20, 50, 120)

# --- Main Game Function ---
def main():
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Naval Battle Royale")
    clock = pygame.time.Clock()

    # Create game state
    game_state = GameState(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    game_state.setup_game()  # Initial game setup

    # Start background music
    try:
        pygame.mixer.music.load(os.path.join('assets', 'background_music.ogg'))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
    except Exception as e:
        print(f"Error loading music: {e}")

    # Game loop
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Process inputs
        game_state.handle_input()

        # Update game state
        if not game_state.game_over:
            game_state.update()

        # Render
        game_state.render(screen)

        # Flip display
        pygame.display.flip()

    # Clean up
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
