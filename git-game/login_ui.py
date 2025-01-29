import pygame
import pygame_gui
from globals import *
pygame.init()

class LoginUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT)) # GUI Manager initialisation
        self.clock = pygame.time.Clock()

        # Defining UI elements
        self.register_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 237), (100, 50)),
            text="Register",
            manager=self.manager)
        
        self.login_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 307), (100, 50)),
            text="Login",
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
                        if event.ui_element == self.login_button:
                            print("Login pressed")
                            running = False
                            return "menu"
                        if event.ui_element == self.register_button:
                            print("Register pressed")
            
            # Update and draw UI
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    login_ui = LoginUI()  # Instantiate LoginUI
    result = login_ui.run()  # Run the LoginUI
    print(f"Next screen: {result}")  # Print the result (menu or none)