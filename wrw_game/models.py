from settings import PLAYER_HEALTH, ENEMY_HEALTH
# Version WRW_game 1.0
class Player:
    # Ініціалізація гравця
    def __init__(self, name="Player", health=PLAYER_HEALTH, score=0):
        self.name = name
        self.health = health
        self.score = score

class Enemy:
    # Ініціалізація ворога
    def __init__(self, level=1, health=ENEMY_HEALTH, score=0):
        self.level = level
        self.health = health
        self.score = score

