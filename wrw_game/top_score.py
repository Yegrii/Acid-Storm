import os

# Отримання абсолютного шляху до файлу score.txt (у PyCharm все працювало без проблем,
# але в VS Code не відкривався файл score.txt, тому я додав абсолютний шлях)
score_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'score.txt')


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