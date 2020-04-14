import random

__author__ = "Ashwin Bhat"

class Player():
    def __init__(self, pname):
        # Here are the statistics for the player
        self.name = pname
        self.hp = 100
        self.mp = 100
        self.strength = 0
        self.vitality = 0
        self.dexterity = 0
        self.intelligence = 0
        self.perception = 0
        self.charisma = 0
        self.luck = 0

        # What the player has equipped
        self.armor_info = None
        self.armor_val = 0
        self.weapon_info = None
        self.weapon = 0

        # Player inventory
        self.inventory = []

    def is_living(self):
        return self.hp > 0

    def get_status(self):
        status = ""
        if is_living:
            status += "You are alive. Your current health is: " + self.hp + " and your current mana is: " + self.mp + ". For some reason you haven't yet realized the quickest way to finish the game is to die."

    def