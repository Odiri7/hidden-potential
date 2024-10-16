import pygame
import random
from combat_loop import *
from enemy_ai import *
from npc_choose_target import *
from player_turn import *
from characters import *

def determine_turn_order(player_party, enemies):
    turn_order = []
    for entity in player_party + enemies:  # Combine both lists
        initiative = entity.agility + random.randint(1, 10)  # Initiative based on agility and randomness
        turn_order.append((entity, initiative)) 

    turn_order = sorted(turn_order, key=lambda x: x[1], reverse=True) # Using built in sorting for better performance

    # Check if the main character wants to reroll
    main_character = player_party[0]  # Assuming the first character is the main character
    main_character_initiative = None
    for (character, initiative) in turn_order:
        if character.name == main_character.name: # Compare by name
            main_character_initiative = initiative
            break
    
    print(f"Current initiative for {main_character.name}: {main_character_initiative}")
    
    # Let's say you check if they want to reroll based on their initiative
    reroll_choice = input("Do you want to reroll your initiative? (yes/no): ").strip().lower()
    if reroll_choice == 'yes':
        new_initiative = main_character.reroll_initiative()
        turn_order[0] = (main_character, new_initiative)  # Update their position with the new initiative
        turn_order = sorted(turn_order, key=lambda x: x[1], reverse=True)  # Re-sort the turn order after the reroll
    
    return [entity for entity in turn_order]

if __name__ == "__main__":
    class Test:
        def __init__(self, name, agility):
            self.name = name
            self.agility = agility
            
        def reroll_initiative(self):
            initiative = self.agility + random.randint(1, 10)
            return initiative
        
        def __repr__(self):
            return f"{self.name}"

    p1 = Test("Human1", 5)
    p2 = Test("Human2", 5)
    p3 = Test("Human3", 10)
    p4 = Test("Human4", 30)

    e1 = Test("Enemy1", 10)
    e2 = Test("Enemy2", 15)
    e3 = Test("Enemy3", 5)

    player_party=[p1,p2,p3,p4]
    enemies =[e1,e2,e3]
    print(determine_turn_order(player_party, enemies))