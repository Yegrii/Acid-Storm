from models import Player, Enemy
from exceptions import EnemyDown, GameOver


# Version WRW_game 2.0
def play_game():
    # Функція гри
    player = Player()
    enemy = Enemy()
    while True:
        try:
            player.attack(enemy)
        except EnemyDown:
            enemy = Enemy()
            print(f"{enemy.name} is dea... Oh, no! He is rising again!")
            # Гра продовжується доки не закінчаться життя гравця
            continue
        try:
            enemy.attack(player)
        except GameOver:
            print(
                f"Sad but true... {player.name} is dead...\n{enemy.name} laughs at you and said: You just another "
                f"mortal in my game!")
            # Гра закінчується коли закінчаться життя гравця
            break


# Ініціалізація гри
if __name__ == "__main__":
    play_game()
