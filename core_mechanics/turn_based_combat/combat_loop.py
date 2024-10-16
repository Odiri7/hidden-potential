import pygame
import random
from enemy_ai import *
from initiative_roll import *
from npc_choose_target import *
from player_turn import *
from characters import *

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

        # List to keep track of defeated enemies
        defeated_enemies = []

        for entity in turn_order:
            if isinstance(entity, Main_Character):
                player_turn(entity)

                # Check if any enemies are dead after the player's turn
                if any(enemy.is_dead() for enemy in enemies):
                    defeated_enemies.extend(enemy for enemy in enemies if enemy.is_dead())

            if isinstance(entity, Character):
                target = Character.choose_target(enemies)
                if target:
                    entity.perform_attack(target) 

            elif isinstance(entity, Enemy):
                target = Enemy.choose_target(player_party)
                if target:
                    entity.perform_attack(target) 

        # Remove defeated enemies form the enemies list
        for enemy in defeated_enemies:
            enemies.remove(enemy)

        # Update turn order for next round
        turn_order = determine_turn_order(player_party, enemies)


if __name__ == "__main__":
    
    p1 = Character(name="Human1", 
        hp=100, 
        mp=30, 
        attack_power=15, 
        shield=5, 
        agility=10, 
        evasion=5, 
        level=1, 
        crit_rate=5,
        crit_multiplier = 30,
        summon="Fire")
    p2 = Character(name="Human2", 
        hp=100, 
        mp=30, 
        attack_power=15, 
        shield=5, 
        agility=10, 
        evasion=5, 
        level=1, 
        crit_rate=5,
        crit_multiplier = 30,
        summon="Fire")


    e1 = Enemy(name="Enemy1", 
        hp=40, 
        mp=0, 
        attack_power=12, 
        shield=1, 
        agility=5, 
        evasion=2, 
        exp=75,)
    e2 = Enemy(name="Enemy2", 
        hp=40, 
        mp=0, 
        attack_power=12, 
        shield=1, 
        agility=5, 
        evasion=2, 
        exp=75,)

    player_party=[p1,p2]
    enemies =[e1,e2]

    battle_loop(player_party,enemies)