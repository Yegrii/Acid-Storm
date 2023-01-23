# models.py
class Player:
    def __init__(self, name="Player", health=5, score=0):
        self.name = name
        self.health = health
        self.score = score

class Enemy:
    def __init__(self, level=1, health=5, score=0):
        self.level = level
        self.health = health
        self.score = score