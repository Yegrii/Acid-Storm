import random
from settings import PLAYER_HEALTH, ENEMY_HEALTH
from exceptions import EnemyDown, GameOver


# Version WRW_game 2.0
class Player:
    def __init__(self, name=input("Enter enemy's name: "), health=PLAYER_HEALTH):
        self.name = name
        self.health = health

    def attack(self, enemy):
        attack_choice = input("Select your attack choice (warrior, robber, wizard): ")
        enemy_defence_choice = random.choice(["warrior", "robber", "wizard"])
        if attack_choice == "warrior" and enemy_defence_choice == "robber":
            enemy.reduce_health()
        elif attack_choice == "robber" and enemy_defence_choice == "wizard":
            enemy.reduce_health()
        elif attack_choice == "wizard" and enemy_defence_choice == "warrior":
            enemy.reduce_health()
        else:
            print("Attack failed.")
        print(f"Player health: {self.health}, Enemy health: {enemy.health}")

    def defend(self, enemy):
        defence_choice = input("Select your defence choice (warrior, robber, wizard): ")
        enemy_attack_choice = random.choice(["warrior", "robber", "wizard"])
        if defence_choice == "warrior" and enemy_attack_choice == "robber":
            self.reduce_health()
        elif defence_choice == "robber" and enemy_attack_choice == "wizard":
            self.reduce_health()
        elif defence_choice == "wizard" and enemy_attack_choice == "warrior":
            self.reduce_health()
        else:
            print("Enemy's attack failed.")
        print(f"Player health: {self.health}, Enemy health: {enemy.health}")

    def reduce_health(self):
        self.health -= 1
        if self.health <= 0:
            raise GameOver(self)


class Enemy:
    def __init__(self, name=input("Enter enemy's name: "), health=ENEMY_HEALTH, score=0):
        self.name = name
        self.health = health

    def attack(self, player):
        attack_choice = random.choice(["warrior", "robber", "wizard"])
        player_defence_choice = input("Select your defence choice (warrior, robber, wizard): ")
        if attack_choice == "warrior" and player_defence_choice == "robber":
            player.reduce_health()
        elif attack_choice == "robber" and player_defence_choice == "wizard":
            player.reduce_health()
        elif attack_choice == "wizard" and player_defence_choice == "warrior":
            player.reduce_health()
        else:
            print("Enemy's attack failed.")
        print(f"Player health: {player.health}, Enemy health: {self.health}")

    def reduce_health(self):
        self.health -= 1
        if self.health <= 0:
            raise EnemyDown(self)
