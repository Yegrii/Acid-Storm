from settings import PLAYER_HEALTH, ENEMY_HEALTH


# Version WRW_game 1.1
class Player:
    # Ініціалізація гравця
    # Додано змінну name, щоб гравець міг ввести своє ім‘я
    def __init__(self, name=input("Enter player's name: "), health=PLAYER_HEALTH, score=0):
        self.name = name
        self.health = health
        self.score = score


class Enemy:
    # Ініціалізація ворога
    def __init__(self, name=input("Enter enemy's name: "), health=ENEMY_HEALTH, score=0):
        self.name = name
        self.health = health
        self.score = score
