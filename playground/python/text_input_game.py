import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Input Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up font
font = pygame.font.Font(None, 74)

# Text input variables
input_text = ''
input_active = True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    print("User input:", input_text)
                    input_text = ''  # Clear input text after pressing Enter
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Remove last character
                else:
                    input_text += event.unicode  # Add the character to input_text

    # Clear the screen
    screen.fill(BLACK)

    # Render the current input text
    text_surface = font.render(input_text, True, WHITE)
    screen.blit(text_surface, (50, 300))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
