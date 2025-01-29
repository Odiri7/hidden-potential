import pygame
import pygame_gui
from globals import *
pygame.init()

class MenuUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT)) # GUI Manager initialisation
        self.clock = pygame.time.Clock()

        # Defining UI elements
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 237), (100, 50)),
            text="Start",
            manager=self.manager)
        
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 307), (100, 50)),
            text="Quit",
            manager=self.manager)
        
    def run(self):
        running = True
        while running:
            time_delta = self.clock.tick(60) / 1000.0 # Convert to milliseconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle GUI events
                self.manager.process_events(event)

                # Check button clicks
                if event.type == pygame.USEREVENT: # Handling user button interactions
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.start_button:
                            print("Start pressed")
                            return "story"
                        if event.ui_element == self.quit_button:
                            running = False
            
            # Update and draw UI
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    menu_ui = MenuUI()  # Instantiate MenuUI
    result = menu_ui.run()  # Run the MenuUI
    print(f"Next screen: {result}")  # Print the result (story or none)