import pygame
import pygame_gui
from globals import *

class CombatUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		# Initialised the Pygame GUI manager with the screen dimensions to handle all UI elements (buttons, text boxes) for the game
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Creating a text box to display the current dialogue, managed by the UI manager
        self.attack_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 500), (100, 50)),
            text="Attack",
            manager=self.manager)
        
        self.guard_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 500), (100, 50)),
            text="Guard",
            manager=self.manager)
        
        self.spell_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 500), (100, 50)),
            text="Spell",
            manager=self.manager)
        
        self.item_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((500, 500), (100, 50)),
            text="Item",
            manager=self.manager)

    def run(self):
        running = True
        while running:
			# This is needed because pygame_gui uses it for updating UI elements
            time_delta = self.clock.tick(60) / 1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle GUI events
                self.manager.process_events(event)

                # Check button clicks
                if event.type == pygame.USEREVENT: # Handling user button interactions
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.attack_button:
                            print("Attack pressed")
                        elif event.ui_element == self.guard_button:
                            print("Guard pressed")
                        elif event.ui_element == self.spell_button:
                            print("Spell pressed")
                        elif event.ui_element == self.item_button:
                            print("Item pressed")

            # Update and draw UI
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    combat_ui = CombatUI()  # Instantiate CombatUI
    combat_ui.run()  # Run the CombatUI
    