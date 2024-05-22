import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
desert_storm = (245, 245, 243)
cape_cod = (56, 64, 66)
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Pygame Template")

# Create a clock object to manage the frame ragte
clock = pygame.time.Clock()

def render():
    # Draw everything
    screen.fill(white)  # Fill the screen with white
    # (Add your drawing code here)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)


def main():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
        # (Add your game logic here)

        render()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
