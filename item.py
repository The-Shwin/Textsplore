__author__ = "Ashwin Bhat"

class Item():
    def __init__(self, iname, description):
        # All items have a name
        self.item_name = iname
        self.description = description
        self.attributes_adj = OrderedDict()
        self.attributes_adj["strength"] = 0
        self.attributes_adj["vitality"] = 0
        self.attributes_adj["dexterity"] = 0
        self.attributes_adj["intelligence"] = 0
        self.attributes_adj["wisdom"] = 0
        self.attributes_adj["charisma"] = 0
        self.attributes_adj["luck"] = 0

class Coin(Item):
    def __init__(self, amount):
        self.amount = amount
        super.()__init__(iname="Coin", description="A shiny gold coin. You have {} of them in your coin pouch.".format(str(self.amount)))

class Armor(Item):
    def __init__(self, iname, description):
        Item.__init__(self, iname, description)
        self.armor_val = None

    def toString(self):
        return "This is a " + self.item_name + " with an armor rating of: " + self.armor_val + " and a dexterity penalty of: " + self.dex_pen + ". " + self.description

class MageRobes(Armor):
    def __init__(self, iname):
        description = "These are mage robes. They provide some armor, but reduce dexterity. You seem quite wise wearing them."
        Armor.__init__(self, iname, description)
        self.armor_val = 75
        self.attributes_adj["dexterity"] = -1
        self.attributes_adj["wisdom"] = 1

class IronArmor(Armor):
    def __init__(self, iname):
        description = "This is iron armor. It is rather protective, but slows reduces your agility. It put some weight behind your hits."
        Armor.__init__(self, iname, description)
        self.armor_val = 100
        self.attributes_adj["dexterity"] = -2
        self.attributes_adj["strength"] = 1

class LeatherArmor(Armor):
    def __init__(self, iname):
        description = "This is leather armor. It protects a bit, but doesn't weigh you down at all. You seem cooler wearing it."
        Armor.__init__(self, iname, description)
        self.armor_val = 50
        self.attributes_adj["dexterity"] = 0
        self.attributes_adj["charisma"] = 1

class Weapon(Item):
    def __init__(self, iname, description, weapon_val):
        Item.__init__(self, iname, description)
        self.weapon_val = weapon_val

    def toString(self):
        return "This is a " + self.item_name + " with a weapon rating of: " + self.weapon_val + ". " + self.description
