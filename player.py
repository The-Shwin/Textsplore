import random
import collections

__author__ = "Ashwin Bhat"

class Player():
    def __init__(self, pname):
        # Here are the statistics for the player
        self.name = pname
        self.hp = 100
        self.mp = 100
        self.attributes = collections.OrderedDict()
        self.attributes["strength"] = 0
        self.attributes["vitality"] = 0
        self.attributes["dexterity"] = 0
        self.attributes["intelligence"] = 0
        self.attributes["wisdom"] = 0
        self.attributes["charisma"] = 0
        self.attributes["luck"] = 0

        # What the player has equipped
        self.armor = None
        self.weapon = None

        # Player inventory
        self.inventory = []
        self.grimoire = []

    def is_living(self):
        return self.hp > 0

    def get_status(self):
        status = ""
        if self.is_living():
            status += "You are alive. Your current health is: " + self.hp + " and your current mana is: " + self.mp + \
                      ". For some reason you haven't yet realized the quickest way to finish the game is to die."
        else:
            status += "You are dead. Good luck with that."
        return status

    def get_equipped(self):
        equip_str = ""
        if self.armor is not None:
            equip_str += self.armor.toString() + " "
        if self.weapon is not None:
            equip_str += + self.weapon.toString() + "."
        return equip_str
