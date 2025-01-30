import pygame
import pygame_gui
from globals import *
pygame.init()

class CombatUI:
    def __init__(self):
        self.__screen = SCREEN
        # Initialised the Pygame GUI manager with the screen dimensions to handle all UI elements (buttons, text boxes) for the game
        self.__manager = UI_MANAGER
        self.__clock = CLOCK

        # Creating a text box to display the current dialogue, managed by the UI manager
        self.__attack_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 500), (100, 50)),
            text="Attack",
            manager=self.__manager)
        
        self.__guard_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 500), (100, 50)),
            text="Guard",
            manager=self.__manager)
        
        self.__spell_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 500), (100, 50)),
            text="Spell",
            manager=self.__manager)
        
        self.__item_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((500, 500), (100, 50)),
            text="Item",
            manager=self.__manager)

    def run(self):
        running = True
        while running:
            # This is needed because pygame_gui uses it for updating UI elements
            time_delta = self.__clock.tick(60) / 1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle GUI events
                self.__manager.process_events(event)

                # Check button clicks
                if event.type == pygame.USEREVENT:  # Handling user button interactions
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__attack_button:
                            print("Attack pressed")
                        elif event.ui_element == self.__guard_button:
                            print("Guard pressed")
                        elif event.ui_element == self.__spell_button:
                            print("Spell pressed")
                        elif event.ui_element == self.__item_button:
                            print("Item pressed")

            # Update and draw UI
            self.__manager.update(time_delta)
            self.__screen.fill((0, 0, 0))
            self.__manager.draw_ui(self.__screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    combat_ui = CombatUI()  # Instantiate CombatUI
    combat_ui.run()  # Run the CombatUI
