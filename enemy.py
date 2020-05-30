__author__ = "Ashwin Bhat"

class Enemy:
    def __init__(self, name, description, hp, mp, attributes):
        self.name = name
        self.description = description
        self.hp = hp
        self.mp = mp
        self.attributes = attributes

class Troll(Enemy):
    def __init__(self):
        Enemy().__init__(name = "Troll", description = "This is a troll. They tend to smell.", hp = 50, mp = 0, attributes =
                        {"strength":3, "vitality":3, "dexterity":1, "intelligence":0, "wisdom":0, "charisma":0, "luck":0})

class Imp(Enemy):
    def __init__(self):
        Enemy().__init__(name = "Imp", description = "This is an imp. They are quite pesky.", hp = 20, mp = 0, attributes =
                        {"strength":1, "vitality":1, "dexterity":4, "intelligence":2, "wisdom":1, "charisma":0, "luck":1})
