import pygame
import pygame_gui
from globals import *
from login_ui import LoginUI
from menu_ui import MenuUI
from story_ui import StoryUI
from combat_ui import CombatUI

class UIController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = "login"

    def run(self):
        while self.running:
            # Depending on the current screen, show the relevant UI class
            if self.current_screen == "login":
                current_ui = LoginUI()
            elif self.current_screen == "menu":
                current_ui = MenuUI()
            elif self.current_screen == "combat":
                current_ui = CombatUI()
            elif self.current_screen == "story":
                current_ui = StoryUI()
            else:
                self.running = False
                return

            # Run the UI and get the next screen
            self.current_screen = current_ui.run()  # This method returns the next screen

            # Handle quitting
            if self.current_screen == "quit":
                self.running = False

        pygame.quit()

if __name__ == "__main__":
    ui_controller = UIController()
    ui_controller.run()