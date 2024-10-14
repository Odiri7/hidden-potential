pygame.init()


screen_width = 960
screen_height = 544

# Game state to determine if game is running
game_state = "start_menu"

# Colours
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)

# Create the clock to set the fps
clock = pygame.time.Clock()

# Set window
screen = pygame.display.set_mode((screen_width, screen_height))

# Change name of a window
pygame.display.set_caption("Potential")


# Text
font = pygame.font.Font("NEA\ProgramFiles\03 Story and Dialogue System\Font\Lato-Regular.ttf", 32)


start_button_selected = False 
# Game loop
running = True
while running:
    screen.fill(black)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "start_menu":
                start_button_rect = draw_start_menu()
                if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    start_button_selected = True
                    game_state = "visual_novel"
                    pygame.time.delay(200)

    if game_state == "start_menu":
        start_button_rect = draw_start_menu()
    elif game_state == "visual_novel":
        text_box_height = 150
        render_text_box(narrative_text, font, white, screen, 50, screen_height - text_box_height - 50, screen_width - 100, text_box_height)
        pygame.display.flip()
        if keys[pygame.K_SPACE]:  # Progress with the spacebar
            pygame.time.delay(200)
            game_state = "battle"
    elif game_state == "battle":
        battle_loop(player_party, enemies) # Start the battle loop
        game_state = "game_over"
    elif game_state == "game_over":
        draw_game_over()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
