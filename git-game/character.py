from globals import *
from entity import Entity

class Character(Entity):
    # Class variable 
    crit_multiplier = 2

    def __init__(self, name: str, hp: int = 10, max_hp: int = 20, attack: int = 5, shield: int = 0, agility: int = 5, evasion: int = 5, guarded: bool = False, healer: bool = False, level: int = 1, xp:int = 0, crit_rate: int = 10):
        super().__init__(name, hp, max_hp, attack, shield, agility, evasion, guarded, healer)
        self.__level = level
        self.__xp = xp
        self.__crit_rate = crit_rate
        
    # Getters and setters
    def get_level(self):
        return self.__level
    
    def set_level(self, value):
        if value > 0:
            self.__level += value

    def get_xp(self):
        return self.__xp
    
    def set_xp(self, value):
        if value > 0:
            self.__xp += value

    def get_crit_rate(self):
        return self.__crit_rate

    # Methods

    def check_level_up(self):
        if self.get_xp >= LEVEL_UP_XP:
            self.__level_up()

    def __level_up(self):
        self.set_level(self.get_level() + 1)
        self.set_attack(self.get_attack() + (self.get_level() * 2))
        self.set_max_hp(self.get_max_hp() + 10)
        self.set_xp(0) # Reseting XP after leveling up
        self._message_display.show_message("You leveled up!")

    def deal_damage(self, target):
        if self.get_attack() < target.get_shield():
            shield_damage = self.get_attack() - target.get_shield()  # All damage absorbed by shield
            hp_damage = 0
        else:
            shield_damage = target.get_shield()  # All shield is gone
            hp_damage = self.get_attack() - target.get_shield()  # Remaining damage goes to HP

        # Test for critical hit
        if self.__critical_hit_test():
            hp_damage *= Character.crit_multiplier  # Apply critical multiplier
            self._message_display.show_message(f"{self.name} landed a critical hit!")

        target.apply_damage(shield_damage, hp_damage)

    def __critical_hit_test(self):
        return random.randint(1,100) < self.get_crit_rate()

    def take_turn(self):
        pass

    def execute_action(self):
        pass

if __name__ == "__main__":
    char1 = Character("March")
    char2= Character("Test")

    print(f"Test HP before = {char2.get_hp()}")
    print(f"Test shield before = {char2.get_shield()}")
    char1.deal_damage(char2)
    print(f"Test HP after = {char2.get_hp()}")
    print(f"Test shield after = {char2.get_shield()}")
