from common import random, pygame, sys


def determine_turn_order(player_party, enemies):
    turn_order = []
    for entity in player_party + enemies:  # Combine both lists
        initiative = entity.agility + random.randint(1, 10)  # Initiative based on agility and randomness
        turn_order.append((entity, initiative)) 

    turn_order = sorted(turn_order, key=lambda x: x[1], reverse=True) # Using built in sorting for better performance

    # Check if the main character wants to reroll
    main_character = player_party[0]  # Assuming the first character is the main character
    main_character_initiative = turn_order[0][1]  # Get their current initiative
    print(f"Current initiative for {main_character.name}: {main_character_initiative}")

    # Let's say you check if they want to reroll based on their initiative
    reroll_choice = input("Do you want to reroll your initiative? (yes/no): ").strip().lower()
    if reroll_choice == 'yes':
        new_initiative = main_character.reroll_initiative()
        turn_order[0] = (main_character, new_initiative)  # Update their position with the new initiative
        turn_order = sorted(turn_order, key=lambda x: x[1], reverse=True)  # Re-sort the turn order after the reroll
    
    return [entity for entity in turn_order]

#turn_order = determine_turn_order(player_party, enemies)
#print("Turn Order:")
#for entity in turn_order:
 #   print(entity)
