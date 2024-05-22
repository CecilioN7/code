import pygame
from datetime import datetime, timedelta

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

desert_storm = (245, 245, 243)
cape_cod = (56, 64, 66)

font_path = "BebasNeue-Regular.ttf"
font = pygame.font.Font(font_path, 74)
text = font.render(f"Current time:", True, cape_cod)
text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


def get_time():
    global text, text_rect
    # now = datetime.now()
    now = datetime.now().strftime("%I:%M:%S %p")
    text = font.render(f"Current time: {now}", True, cape_cod)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))



def render():
    screen.fill(desert_storm)

    screen.blit(text, text_rect)

    pygame.display.flip()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    get_time()
    render()

pygame.quit()