from exceptions import EnemyDown, GameOver
from models import Player, Enemy
from settings import ENEMY_HEALTH
from top_score import write_score_to_file, get_top_players, get_top_enemies

# Version WRW_game 3.0

# Функція для імені гравця
def get_player_name():
    return input("Enter player's name: ")


# Функція для імені ворога
def get_enemy_name():
    return input("Enter enemy's name: ")


# Функція гри
def play_game():
    player_name = get_player_name()
    enemy_name = get_enemy_name()
    player = Player(name=player_name)
    enemy = Enemy(name=enemy_name)
    while True:
        try:
            player.attack(enemy)
        except EnemyDown:
            # Після смерті ворога створюємо нового ворога у якого здоров‘я
            # дорівнює базовому здоров‘ю + його рівень
            enemy = Enemy(enemy.name, ENEMY_HEALTH + enemy.lvl, enemy.lvl + 1)

            # Збільшуємо здоров‘я гравця на 3 HP
            # Збільшуємо рахунок гравця на 1, тому що при відпрацюванні except EnemyDown бал не збільшувався,
            # тож я додав це напряму в except EnemyDown
            player.health += 3
            player.score += 1
            print(f"\n{enemy.name} is dea... Oh, no, wait...! He is rising again! And becomes more POWERFUL!!!")
            print(
                f"\nNew {enemy.name}'s health is: {enemy.health}, {player.name} takes medicine and raises his health "
                f"level by +3HP: {player.health}, {player.name} score: {player.score}")
            continue
        try:
            enemy.attack(player)
        except GameOver:
            print(
                f"\nSad but true... {player.name} is dead...\n{enemy.name} laughs at you and said: You just another "
                f"mortal in my game!")

            # Виводимо результати гри
            print(f"\n{player.name} score: {player.score}; {enemy.name} level: {enemy.lvl}")

            # Викликаємо функцію для запису результатів гри
            write_score_to_file(player.name, enemy.name, player.score, enemy.lvl)

            # Викликаємо функції для виводу топ 10 гравців та топ 3 ворогів
            top_players = get_top_players()
            top_enemies = get_top_enemies()

            print("\n--- Top 10 players ---")
            for i, (name, score) in enumerate(top_players):
                print(f"{i + 1}. {name}: {score}")

            print("\n--- Top 3 enemies ---")
            for i, (name, level) in enumerate(top_enemies):
                print(f"{i + 1}. {name}: {level}")

            break


# Ініціалізація гри
if __name__ == '__main__':
    play_game()
