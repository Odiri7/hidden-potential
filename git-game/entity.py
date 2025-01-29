from globals import *
import pygame as py
from abc import ABC, abstractmethod
import random

class Entity(ABC):
    def __init__(self, name: str, hp: int =10, max_hp: int=20, attack: int=5, shield: int =0, agility: int=5, evasion: int=20, guarded: bool=False, healer: bool=False):
        self.name = name
        self.__hp = hp
        self.__max_hp = max_hp
        self.__attack = attack
        self.__shield = shield
        self.__agility = agility # Does not change
        self.__evasion = evasion # Range (1-100) does not change
        self.__guarded = guarded
        self.__healer = healer # Defines role
    
    def set_hp(self, value):
        if self.get_hp() + value < self.get_max_hp():
              self.__hp = value
        else:
            self.__hp = self.get_max_hp()

    def get_hp(self):
        return self.__hp
      
    def set_max_hp(self, value):
        if value < 0:
            value = 0
        self.__max_hp += value

    def get_max_hp(self):
        return self.__max_hp
      
    def set_attack(self, value):
        if value < 0:
            value = 0
        self.__attack += value

    def get_attack(self):
        return self.__attack
      
    def get_agility(self):
        return self.__agility
      
    def get_evasion(self):
        return self.__evasion
      
    def set_shield(self, value):
        if value < 0:
            value = 0
        self.__shield += value

    def get_shield(self):
        return self.__shield
        
    def set_guarded(self, value):
        if isinstance(value, bool):
            self.__guarded = value

    def get_guarded(self):
        return self.__guarded

    def get_healer(self):
        return self.__healer
      
    def evade_chance(self):
        random_value = random.randint(1, 100)
        return random_value <= self.get_evasion()

    def deal_damage(self, target):
        shield_damage = 0
        hp_damage = 0

        if self.get_attack() < target.get_shield():
            shield_damage = self.get_attack() - target.get_shield()
        else:
            shield_damage = target.get_shield()
            hp_damage = self.get_attack() - target.get_shield()

        # Test for critical hit
        if isinstance(self, Character):  # Only characters can critical hit
            if self.critical_hit_test():
                hp_damage *= Character.crit_multiplier  # Apply critical multiplier

        return shield_damage, hp_damage
    
    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    def execute_action(self):
        pass
