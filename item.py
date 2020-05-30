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

#### #### #### #### Currencies #### #### #### ####
class Coin(Item):
    def __init__(self, amount):
        self.amount = amount
        super.()__init__(iname="Coin", description="A shiny gold coin. You have {} of them in your coin pouch.".format(str(self.amount)))
#### #### #### #### Currencies #### #### #### ####


#### #### #### #### Armors #### #### #### ####
class Armor(Item):
    def __init__(self, iname, description, armor_val):
        Item.__init__(self, iname, description)
        self.armor_val = armor_val

    def toString(self):
        return "This is a " + self.item_name + " with an armor rating of: " + self.armor_val + " and a dexterity penalty of: " + self.attributes_adj["dexterity"] + ". " + self.description

class MageRobes(Armor):
    def __init__(self):
        iname = "Mage Robes"
        description = "These are mage robes. They provide some armor, but reduce dexterity. They lend you an air of wisdom."
        armor_val = 75
        Armor.__init__(self, iname, description, armor_val)
        self.attributes_adj["dexterity"] = -1
        self.attributes_adj["wisdom"] = 1

class IronArmor(Armor):
    def __init__(self):
        iname = "Iron Armor"
        description = "This is iron armor. It is rather protective, but slows reduces your agility. It puts some weight behind your hits."
        armor_val = 100
        Armor.__init__(self, iname, description, armor_val)
        self.attributes_adj["dexterity"] = -2
        self.attributes_adj["strength"] = 1

class LeatherArmor(Armor):
    def __init__(self):
        iname = "Leather Armor"
        description = "This is leather armor. It protects a bit, but doesn't weigh you down at all. You seem cooler wearing it."
        armor_val = 50
        Armor.__init__(self, iname, description, armor_val)
        self.attributes_adj["dexterity"] = 0
        self.attributes_adj["charisma"] = 1
#### #### #### #### Armors #### #### #### ####


#### #### #### #### Weapons #### #### #### ####
class Weapon(Item):
    def __init__(self, iname, description, weapon_val):
        Item.__init__(self, iname, description)
        self.weapon_val = weapon_val

    def toString(self):
        return "This is a " + self.item_name + " with a weapon rating of: " + self.weapon_val + ". " + self.description

class CommonDagger(Weapon):
    def __init__(self):
        iname = "Common Dagger"
        description = "This is a common dagger. It might help in enclosed places, but good luck piercing troll hide with this."
        weapon_val = 20
        Weapon.__init__(self, iname, description, weapon_val)

class AssassinDagger(Weapon):
    def __init__(self):
        iname = "Assassin Dagger"
        description = "This is an assassin's dagger. Historically used by the most legendary of assassins, it gives the user great ability."
        weapon_val = 130
        Weapon.__init__(self, iname, description, weapon_val)
        self.attributes_adj["dexterity"] = 3
#### #### #### #### Weapons #### #### #### ####
