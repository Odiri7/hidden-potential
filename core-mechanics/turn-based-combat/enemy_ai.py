

class EnemyAI:
    def __init__(self, enemy):
        self.enemy = enemy

    def take_turn(self, player_party):
        target = self.choose_target(player_party)
        # If the target's HP is low, the enemy will focus on them
        if target.hp < target.max_hp * 0.5:
            print(f"{self.enemy.name} focuses on {target.name}!")
        else:
            print(f"{self.enemy.name} attacks {target.name}!")

        # Perform the attack on the chosen target
        self.enemy.attack(target)

    def choose_target(self, player_party):
        # AI chooses the player with the lowest HP
        return min(player_party, key=lambda character: character.hp)
