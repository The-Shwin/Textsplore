__author__ = "Ashwin Bhat"

class Item():
    def __init__(self, iname, description):
        # All items have a name
        self.item_name = iname
        self.description = description


class Armor(Item):
    def __init__(self, iname, description, armor_val):
        Item.__init__(self, iname, description)
        self.armor_val = armor_val

    def toString(self):
        return "This is a " + self.item_name + " with an armor rating of: " + self.armor_val + " and a dexterity penalty of: " + self.dex_pen + ". " + self.description

class Weapon(Item):
    def __init__(self, iname, description, weapon_val):
        Item.__init__(self, iname, description)
        self.weapon_val = weapon_val

    def toString(self):
        return "This is a " + self.item_name + " with a weapon rating of: " + self.weapon_val + ". " + self.description
