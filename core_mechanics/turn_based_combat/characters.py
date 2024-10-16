import pygame
import random

# Classes for characters
class Entity: # Playable and non playable
    def __init__(self, name, hp, mp, attack_power, shield, agility, evasion):
        self.name = name 
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack_power = attack_power
        self.shield = shield
        self.agility = agility
        self.evasion = evasion

    def take_damage(self,amount):
        self.hp -=amount
        if self.hp < 0:
            self.hp = 0 # Dont want minus health bars

    def is_dead(self):
        if self.hp == 0:
            return True
        else:
            return False

    def get_stats(self):
        return f"Name: {self.name}\nHP: {self.hp}/{self.max_hp}\nMP: {self.mp}/{self.max_mp}\nAttack: {self.attack_power}\nShield: {self.shield}"

class Character(Entity):
    def __init__(self, name, hp, mp, attack_power, shield, agility, evasion, level, crit_rate, crit_multiplier, summon):
        super().__init__(name, hp, mp, attack_power, shield, agility, evasion)
        self.level = level
        self.crit_rate = crit_rate
        self.crit_multiplier = crit_multiplier
        self.summon = summon  # Summon that can deal elemental damage 
        self.status_effects = []

    def test_for_critical(self):
        if random.randint(1,100) < self.crit_rate:
            return True
        
    def perform_attack(self, enemy): 
        damage = self.attack_power - enemy.shield
        if self.test_for_critical():
            damage *= self.crit_multiplier
            print(f"Critical hit!")
        if damage > 0:
            enemy.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack is blocked by {enemy.name}!")

    def perform_guard(self):
        shield_increase = self.max_hp * 0.3
        print(f"{self.name} guards, increasing shield by {shield_increase}.")
        self.status_effects.append("Guarded")

    def process_turn(self):
        # Check for guarded status effect and skip turn if it's there
        if "Guarded" in self.status_effects:
            print(f"{self.name} is guarding and skips this turn.")
            self.status_effects.remove("Guarded")  # Remove guard effect after skipping
            return False  # Skip the turn
        return True  # Otherwise, take a normal turn

class Enemy(Entity):
    def __init__(self, name, hp, mp, attack_power, shield, agility, evasion, exp):
        super().__init__(name, hp, mp, attack_power, shield, agility, evasion)
        self.exp = exp

    def perform_attack(self, character: Character):
        damage = self.attack_power - character.shield
        if damage > 0:
            character.take_damage(damage)
            print(f"{self.name} attacks {character.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack is blocked by {character.name}!")


class Main_Character(Character):
    def __init__(self, name, hp, mp, attack_power, shield, agility, evasion, level, crit_rate, summon):
        super().__init__(name, hp, mp, attack_power, shield, agility, evasion, level, crit_rate, summon)

    def use_item(self, item):
        print(f"{self.name} uses {item}!")
    
    def reroll_initiative(self):
        initiative = self.agility + random.randint(1, 10)
        return initiative



# Characters (WIP)

player_party = [
    Character(
        name="Naomi", 
        hp=100, 
        mp=30, 
        attack_power=15, 
        shield=5, 
        agility=10, 
        evasion=5, 
        level=1, 
        crit_rate=5,
        crit_multiplier = 30,
        summon="Fire"
    ),
    Character(
        name="March", 
        hp=100, 
        mp=30, 
        attack_power=15, 
        shield=5, 
        agility=10, 
        evasion=5, 
        level=1, 
        crit_rate=5,
        crit_multiplier = 30,
        summon="Ice"
    )
]

enemies = [
    Enemy(
        name="Goblin", 
        hp=30, 
        mp=0, 
        attack_power=8, 
        shield=2, 
        agility=6, 
        evasion=3, 
        exp=50  # Experience points granted when defeated
    ),
    Enemy(
        name="Troll", 
        hp=40, 
        mp=0, 
        attack_power=12, 
        shield=1, 
        agility=5, 
        evasion=2, 
        exp=75
    )
]
