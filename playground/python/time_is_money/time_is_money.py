# NAME: Cecilio Navarro
# ORGN:
# FILE: time_is_money.py
# DATE: Thu Aug 15, 2024

import pygame
from datetime import datetime, timedelta

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
desert_storm = (245, 245, 243)
cape_cod = (56, 64, 66)
black = (0, 0, 0)

class Text:
    def __init__(self, text, font_path, font_size, color, center_position):
        self.font = pygame.font.Font(font_path, font_size)
        self.text = text
        self.color = color
        self.center_position = center_position
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.center_position)

    def update_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.center_position)

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)

# TextBox class remains unchanged
class TextBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = cape_cod
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = black if self.active else cape_cod

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Hourly Rate: {self.text}")
                    self.active = False  # Stop editing after pressing enter
                    start_earning_calculation()  # Start calculation when Enter is pressed
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text

# Create Text instances
hello_text = Text("Hello!", "BebasNeue-Regular.ttf", 70, cape_cod, (SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
time_text = Text("", "BebasNeue-Regular.ttf", 30, cape_cod, (SCREEN_WIDTH - 70, 30))
instruction_text = Text("Enter the dollars per hour and press Enter:", "BebasNeue-Regular.ttf", 30, cape_cod, (SCREEN_WIDTH/2, SCREEN_HEIGHT * 5/12))
total_text = Text("", "BebasNeue-Regular.ttf", 70, cape_cod, (SCREEN_WIDTH/2, SCREEN_HEIGHT * .65))
time_elapsed_text = Text("", "BebasNeue-Regular.ttf", 40, cape_cod, (SCREEN_WIDTH/2, SCREEN_HEIGHT * .80))

input_box = TextBox(300, 300, 200, 32, pygame.font.Font(None, 32))

tracking = False
start_time = None
hourly_rate = 0.00

def start_earning_calculation():
    global start_time, tracking, hourly_rate
    hourly_rate = float(input_box.get_text()) if input_box.get_text().replace('.', '', 1).isdigit() else 0.00
    start_time = datetime.now()
    tracking = True

def calculate_earnings(hourly_rate, elapsed_time):
    # Calculate earnings based on hourly rate and elapsed time in seconds
    earnings = (hourly_rate / 3600) * elapsed_time.total_seconds()
    return f"${earnings:.2f}"

def format_elapsed_time(elapsed_time):
    minutes, seconds = divmod(int(elapsed_time.total_seconds()), 60)
    return f"{minutes:02d}:{seconds:02d}"

def get_time():
    now = datetime.now().strftime("%I:%M:%S %p")
    time_text.update_text(now)

def render():
    screen.fill(desert_storm)
    if tracking:
        elapsed_time = datetime.now() - start_time
        earnings = calculate_earnings(hourly_rate, elapsed_time)
        total_text.update_text(f"Your Total: {earnings}")
        time_elapsed_text.update_text(f"Time worked so far: {format_elapsed_time(elapsed_time)}")
    total_text.draw(screen)
    time_text.draw(screen)
    hello_text.draw(screen)
    instruction_text.draw(screen)
    time_elapsed_text.draw(screen)
    input_box.draw(screen)
    pygame.display.flip()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        input_box.handle_event(event)
    
    get_time()
    render()

pygame.quit()
