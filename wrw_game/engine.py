import random
from models import Player, Enemy
from exceptions import EnemyDown, GameOver
from settings import NUM_ROUNDS


# Version WRW_game 1.1
def attack_stage(player, enemy):
    # Функція нападу гравця на ворога

    attack_choice = input("Select your attack choice (warrior, robber, wizard): ")
    enemy_defence_choice = random.choice(["warrior", "robber", "wizard"])
    if attack_choice == "warrior" and enemy_defence_choice == "robber":
        enemy.health -= 1
        player.score += 1
        if enemy.health <= 0:
            raise EnemyDown(enemy)
    elif attack_choice == "robber" and enemy_defence_choice == "wizard":
        enemy.health -= 1
        player.score += 1
        if enemy.health <= 0:
            raise EnemyDown(enemy)
    elif attack_choice == "wizard" and enemy_defence_choice == "warrior":
        enemy.health -= 1
        player.score += 1
        if enemy.health <= 0:
            raise EnemyDown(enemy)
    else:
        print("Attack failed.")
    # Додано вивід здоров'я гравця та ворога
    print(f"Player health: {player.health}, Enemy health: {enemy.health}")


def defence_stage(player, enemy):
    # Функція захисту гравця від нападу ворога

    defence_choice = input("Select your defence choice (warrior, robber, wizard): ")
    enemy_attack_choice = random.choice(["warrior", "robber", "wizard"])
    if defence_choice == "warrior" and enemy_attack_choice == "robber":
        player.health -= 1
        if player.health <= 0:
            raise GameOver(player)
    elif defence_choice == "robber" and enemy_attack_choice == "wizard":
        player.health -= 1
        if player.health <= 0:
            raise GameOver(player)
    elif defence_choice == "wizard" and enemy_attack_choice == "warrior":
        player.health -= 1
        if player.health <= 0:
            raise GameOver(player)
    else:
        print("Enemy's attack failed.")
    # Додано вивід здоров‘я гравця та ворога
    print(f"Player health: {player.health}, Enemy health: {enemy.health}")


def play_game():
    # Функція гри
    # Додано змінну NUM_ROUNDS, щоб обмежити кількість раундів

    player = Player()
    enemy = Enemy()
    for i in range(NUM_ROUNDS):
        try:
            attack_stage(player, enemy)
            defence_stage(player, enemy)
        except EnemyDown as e:
            enemy = Enemy()
            print(f"Enemy {e.enemy.name} is down.")
            break
        except GameOver as e:
            print(f"Game over. Player {e.player.name} is down.")
            break
    print(f"{player.name} has hit {enemy.name} {player.score} times and win the WRW game!!!")


# Ініціалізація гри
if __name__ == "__main__":
    play_game()
