import pygame
import pygame_gui
from globals import *
pygame.init()

class LoginUI:
    def __init__(self):
        self.__screen = SCREEN
        self.__manager = UI_MANAGER  # GUI Manager initialisation
        self.__clock = CLOCK

        # Defining UI elements
        self.__register_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 237), (100, 50)),
            text="Register",
            manager=self.__manager)
        
        self.__login_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((430, 307), (100, 50)),
            text="Login",
            manager=self.__manager)
        
    def run(self):
        running = True
        while running:
            time_delta = self.__clock.tick(60) / 1000.0  # Convert to milliseconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle GUI events
                self.__manager.process_events(event)

                # Check button clicks
                if event.type == pygame.USEREVENT:  # Handling user button interactions
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__login_button:
                            print("Login pressed")
                            running = False
                            return "menu"
                        if event.ui_element == self.__register_button:
                            print("Register pressed")
            
            # Update and draw UI
            self.__manager.update(time_delta)
            self.__screen.fill((0, 0, 0))
            self.__manager.draw_ui(self.__screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    login_ui = LoginUI()  # Instantiate LoginUI
    result = login_ui.run()  # Run the LoginUI
    print(f"Next screen: {result}")  # Print the result (menu or none)
