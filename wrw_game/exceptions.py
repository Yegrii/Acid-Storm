class EnemyDown(Exception):
    #  Ініціалізуємо клас EnemyDown
    def __init__(self, enemy):
        self.enemy = enemy

class GameOver(Exception):
    #  Ініціалізуємо клас GameOver
    def __init__(self, player):
        self.player = player