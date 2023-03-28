import random

from exceptions import EnemyDown, GameOver
from settings import PLAYER_HEALTH, ENEMY_HEALTH


# Version WRW_game 3.0
class Player:
    def __init__(self, name, health=PLAYER_HEALTH, score=0):
        self.name = name
        self.health = health
        self.score = score

    def attack(self, enemy):
        # Функція для автоматичного вибору атаки гравця і захисту ворога(тестова)
        attack_choice = random.choice(["warrior", "robber", "wizard"])
        enemy_defence_choice = random.choice(["warrior", "robber", "wizard"])

        if attack_choice == "warrior" and enemy_defence_choice == "robber":
            enemy.reduce_health()
            self.score_points()
            print(f"\n{self.name} hit {enemy.name}!\n")
        elif attack_choice == "robber" and enemy_defence_choice == "wizard":
            enemy.reduce_health()
            self.score_points()
            print(f"\n{self.name} hit {enemy.name}!\n")
        elif attack_choice == "wizard" and enemy_defence_choice == "warrior":
            enemy.reduce_health()
            self.score_points()
            print(f"\n{self.name} hit {enemy.name}!\n")
        elif attack_choice == enemy_defence_choice:
            print("\nDraw!\n")
        else:
            print(f"\n{self.name}'s attack failed.\n")
        print(
            f"{self.name} health: {self.health}, {self.name} score: {self.score}. \n{enemy.name} health: {enemy.health}"
            f", {enemy.name} level: {enemy.lvl}\n")

        # attack_choice = input(f"{self.name}, select your 'ATTACK' choice (warrior, robber, wizard): ")
        # enemy_defence_choice = random.choice(["warrior", "robber", "wizard"])
        #
        # if attack_choice == "warrior" and enemy_defence_choice == "robber":
        #     enemy.reduce_health()
        #     self.score_points()
        #     print(f"\n{self.name} hit {enemy.name}!\n")
        # elif attack_choice == "robber" and enemy_defence_choice == "wizard":
        #     enemy.reduce_health()
        #     self.score_points()
        #     print(f"\n{self.name} hit {enemy.name}!\n")
        # elif attack_choice == "wizard" and enemy_defence_choice == "warrior":
        #     enemy.reduce_health()
        #     self.score_points()
        #     print(f"\n{self.name} hit {enemy.name}!\n")
        # elif attack_choice == enemy_defence_choice:
        #     print("\nDraw!\n")
        # else:
        #     print(f"\n{self.name}'s attack failed.\n")
        #     print( f"{self.name} health: {self.health}, {self.name} score: {self.score}. \n{enemy.name} health: {enemy.health},{enemy.name} level: {enemy.lvl}\n")

    def defend(self, enemy):
        # Функція для автоматичного вибору захисту гравця й атаки ворога(тестова)
        defence_choice = random.choice(["warrior", "robber", "wizard"])
        enemy_attack_choice = random.choice(["warrior", "robber", "wizard"])

        if enemy_attack_choice == "warrior" and defence_choice == "robber":
            self.reduce_health()
            print(f'\n{enemy.player} hit you!\n')
        elif enemy_attack_choice == "robber" and defence_choice == "wizard":
            self.reduce_health()
            print(f'\n{enemy.player} hit you!\n')
        elif enemy_attack_choice == "wizard" and defence_choice == "warrior":
            self.reduce_health()
            print(f'\n{enemy.player} hit you!\n')
        elif enemy_attack_choice == defence_choice:
            print("\nDraw!\n")
        else:
            print(f"\n{enemy.player}'s attack failed.\n")
        print(
            f"{self.name}'s health: {self.health}, {self.name} score: {self.score}. \n{enemy.player} health: "
            f"{enemy.health}, {enemy.player} level: {enemy.lvl}\n")

        # defence_choice = input(f"{self.name}, select your 'DEFENCE' choice (warrior, robber, wizard): ")
        # enemy_attack_choice = random.choice(["warrior", "robber", "wizard"])
        #
        # if enemy_attack_choice == "warrior" and defence_choice == "robber":
        #     self.reduce_health()
        #     print(f'\n{enemy.name} hit you!\n')
        # elif enemy_attack_choice == "robber" and defence_choice == "wizard":
        #     self.reduce_health()
        #     print(f'\n{enemy.name} hit you!\n')
        # elif enemy_attack_choice == "wizard" and defence_choice == "warrior":
        #     self.reduce_health()
        #     print(f'\n{enemy.name} hit you!\n')
        # elif enemy_attack_choice == defence_choice:
        #     print("\nDraw!\n")
        # else:
        #     print(f"\n{enemy.name}'s attack failed.\n")
        # print(
        #     f"{self.name}'s health: {self.health}, {self.name} score: {self.score}. \n{enemy.name}'s health: {enemy.health}, {enemy.name} level: {enemy.lvl}\n")

    def reduce_health(self):
        self.health -= 1
        if self.health <= 0:
            raise GameOver(self)

    def score_points(self):
        self.score += 1


class Enemy:
    def __init__(self, name, health=ENEMY_HEALTH, lvl=1):
        self.name = name
        self.health = health
        self.lvl = lvl

    def attack(self, player):
        # Функція для автоматичного вибору атаки гравця і захисту ворога(тестова)
        attack_choice = random.choice(["warrior", "robber", "wizard"])
        player_defence_choice = random.choice(["warrior", "robber", "wizard"])

        if attack_choice == "warrior" and player_defence_choice == "robber":
            player.reduce_health()
            print(f'\n{self.name} hit you!\n')
        elif attack_choice == "robber" and player_defence_choice == "wizard":
            player.reduce_health()
            print(f'\n{self.name} hit you!\n')
        elif attack_choice == "wizard" and player_defence_choice == "warrior":
            player.reduce_health()
            print(f'\n{self.name} hit you!\n')
        elif attack_choice == player_defence_choice:
            print("\nDraw!\n")
        else:
            print(f"\n{self.name}'s attack failed.\n")
        print(
            f"{self.name}'s health: {self.health}, {self.name} level: {self.lvl}. \n{player.name}'s health: "
            f"{player.health}, {player.name} score: {player.score}\n")

        # attack_choice = random.choice(["warrior", "robber", "wizard"])
        # player_defence_choice = input(f"{player.name}, select your 'DEFENCE' choice (warrior, robber, wizard): ")
        #
        # if attack_choice == "warrior" and player_defence_choice == "robber":
        #     player.reduce_health() print(f'\n{self.name} hit you!\n')
        # elif attack_choice == "robber" and player_defence_choice == "wizard":
        #     player.reduce_health() print(f'\n{self.name} hit you!\n')
        # elif attack_choice == "wizard" and player_defence_choice == "warrior":
        #     player.reduce_health() print(f'\n{self.name} hit you!\n')
        # elif attack_choice == player_defence_choice:
        #     print("\nDraw!\n")
        # else:
        #     print(f"\n{self.name}'s attack failed.\n")
        # print(
        #     f"{player.name}'s health: {player.health}, {player.name} score: {player.score}. \n{self.name}'s
        # health: {self.health}, {self.name} level: {self.lvl}\n")

    def reduce_health(self):
        self.health -= 1
        if self.health <= 0:
            raise EnemyDown(self)
