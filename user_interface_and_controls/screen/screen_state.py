from common import random, pygame, sys


def draw_start_menu():
    screen.fill(black)
    
    # Title
    title = font.render("My Game", True, white)
    title_rect = title.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(title, title_rect)
    
    # Start button
    start_button = font.render("Start", True, white)
    start_button_rect = start_button.get_rect(center=(screen_width // 2, screen_height // 2))
    
    # Highlight button if mouse hovers over it
    mouse_pos = pygame.mouse.get_pos()
    if start_button_rect.collidepoint(mouse_pos):
        # Draw a rectangle around the text
        pygame.draw.rect(screen, grey, start_button_rect.inflate(20, 10))
    
    screen.blit(start_button, start_button_rect)
    
    # Visual feedback on button click (optional, handled in main loop)
    if start_button_selected:
        pygame.draw.rect(screen, grey, start_button_rect.inflate(20, 10), 3)
    
    pygame.display.flip()
    
    return start_button_rect 

def render_text_box(text, font, color, screen, x, y, box_width, box_height):
    pygame.draw.rect(screen, black, (x, y, box_width, box_height))
    pygame.draw.rect(screen, white, (x, y, box_width, box_height), 2) # Draw the border around the text box
    
    lines = text.split('\n')

    words = [word.split(' ') for word in text.splitlines()] # splits up the words within the split up lines
    space_width, space_height = font.size(' ')  # Get the size of a space character
    max_line_width = box_width - 10
    current_y = y + 5
    
    for line in lines:
        words = line.split(' ')  # Split each line into individual words
        current_line = ""  # Start with an empty line
        for word in words:
            test_line = current_line + word + ' '
            # Check the width of the line
            test_width, test_height = font.size(test_line) # Using tuple to get test_width and test_height
            
            # If the line is too wide, draw the current line and start a new one
            if test_width > max_line_width:
                screen.blit(font.render(current_line, True, color), (x + 5, current_y))
                current_y += test_height
                current_line = word + ' '
            else:
                current_line = test_line
        
        # After the loop, draw any remaining text
        if current_line:
            screen.blit(font.render(current_line, True, color), (x + 5, current_y))
            current_y += test_height  # Move down after the last line


def draw_game_over(selected_button=None):
    screen.fill(black)

    title = font.render("Game Over", True, white)
    restart_button_text = font.render("Restart", True, white)
    quit_button_text = font.render("Quit", True, white)

    title_rect = title.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    restart_button_rect = restart_button_text.get_rect(center=(screen_width // 2, screen_height // 2))
    quit_button_rect = quit_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

    # Draw title
    screen.blit(title, title_rect)

    # Draw Restart button with hover effect
    mouse_pos = pygame.mouse.get_pos()
    if restart_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, grey, restart_button_rect.inflate(20, 10))
        if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            selected_button = "restart"
    else:
        pygame.draw.rect(screen, black, restart_button_rect.inflate(20, 10), 0)
    screen.blit(restart_button_text, restart_button_rect)

    # Draw Quit button with hover effect
    if quit_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, grey, quit_button_rect.inflate(20, 10))
        if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            selected_button = "quit"
    else:
        pygame.draw.rect(screen, black, quit_button_rect.inflate(20, 10), 0)
    screen.blit(quit_button_text, quit_button_rect)

    pygame.display.flip()

    return selected_button
