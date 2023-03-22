from exceptions import EnemyDown, GameOver
from models import Player, Enemy
from settings import ENEMY_HEALTH
import os

# Version WRW_game 3.0

# Отримання абсолютного шляху до файлу score.txt (у PyCharm вcе працювало без проблем,
# але в VS Code не відкривався файл score.txt, тому я додав абсолютний шлях)
score_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'score.txt')


# Функція для імені гравця
def get_player_name():
    return input("Enter player's name: ")


# Функція для імені ворога
def get_enemy_name():
    return input("Enter enemy's name: ")


# Функція для запису результатів гри
def write_score_to_file(player_name, enemy_name, player_score, enemy_level):
    with open(score_file_path, 'a') as file:
        file.write(f'Player: {player_name} score: {player_score} Enemy: {enemy_name} level: {enemy_level}\n')


# Функція, щоб отримати топ 10 гравців
def get_top_players():
    with open(score_file_path, 'r') as f:
        lines = f.readlines()
        players = [(line.split()[1], int(line.split()[3])) for line in lines]
        players.sort(key=lambda x: x[1], reverse=True)
        return players[:10]


# Функція, щоб отримати топ 3 ворогів
def get_top_enemies():
    with open(score_file_path, 'r') as f:
        lines = f.readlines()
        enemies = [(line.split()[5], int(line.split()[7])) for line in lines]
        enemies.sort(key=lambda x: x[1], reverse=True)
        return enemies[:3]


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
