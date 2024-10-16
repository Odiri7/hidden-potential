import pygame
import random
from combat_loop import *
from initiative_roll import *
from npc_choose_target import *
from characters import *
from enemy_ai import *

def player_turn(character):
    action = input("Choose an action: 1. Attack 2. Use Item 3. Guard ")
    if action == '1':
        target = choose_target(enemies)
        character.perform_attack(target)
    elif action == '2':
        item = choose_item()  # (WIP) function to let the player select an item
        character.use_item(item)
    elif action == '3':
        character.perform_guard()  
