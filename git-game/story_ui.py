import pygame
import pygame_gui
from globals import *
pygame.init()

class StoryUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT)) # GUI Manager initialisation
        self.clock = pygame.time.Clock()

        self.dialogue = [
                "Hello.",
                "This is an example of visual novel dialogue.",
                "End."
            ]
        self.current_dialogue = 0
        
        # Defining UI elements  
        self.dialogue_box = pygame_gui.elements.UITextBox(
            html_text=self.dialogue[self.current_dialogue],  
            relative_rect=pygame.Rect((50, SCREEN_HEIGHT - 150), (SCREEN_WIDTH - 100, 120)),
            manager=self.manager,
            object_id="#dialoguebox" # For themeing in future
        )
        
        
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
                if event.type == pygame.MOUSEBUTTONDOWN: # Handling dialogue progression
                    if self.current_dialogue < len(self.dialogue) - 1:
                        self.current_dialogue += 1
                        # Update the text on the dialogue box
                        self.dialogue_box.set_text(self.dialogue[self.current_dialogue])
                    else:
                        running = False

            # Refresh and update
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))

            # Drawing a white border around the dialogue box
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 120), 3)  

            # Draw UI
            self.manager.draw_ui(self.screen)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    story_ui = StoryUI()  # Instantiate StoryUI
    story_ui.run()  # Run the StoryUI
    