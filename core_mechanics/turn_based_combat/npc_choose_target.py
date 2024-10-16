import pygame
import random
from combat_loop import *
from enemy_ai import *
from initiative_roll import *
from player_turn import *
from characters import *

def npc_choose_target(targets):
    
    # Filter out dead targets
    alive_targets = [target for target in targets if not target.is_dead()]

    # Randomly select a target from the alive ones
    selected_target = random.choice(alive_targets)
    print(f"Target selected: {selected_target.name}")
    return selected_target
