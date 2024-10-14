from common import random, pygame, sys

# Code for the battle loop
def battle_loop(player_party, enemies):
    turn_order = determine_turn_order(player_party, enemies)
    battle_loop_running = True

    while battle_loop_running:
        if all(enemy.is_dead() for enemy in enemies):
            print("Victory")
            battle_loop_running = False
            break
        if all(character.is_dead() for character in player_party):
            print("Defeat")
            battle_loop_running = False
            break

        for entity in turn_order:
            if isinstance(entity, Main_Character):
                player_turn(entity)
                if enemies[0].is_dead():
                    enemies.remove(enemies[0]) # Remove defeated enemy from the list

            if isinstance(entity, Character):
                target = choose_target(enemies)
                if target:
                    entity.perform_attack(target) 

            elif isinstance(entity, Enemy):
                target = choose_target(player_party)
                if target:
                    entity.perform_attack(target) 

        # Update turn order for next round
        turn_order = determine_turn_order(player_party, enemies)

