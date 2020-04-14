__author__ = "Ashwin Bhat"

class Item():
    def __init__(self, iname):
        # All items have a name
        self.item_name = iname


class Armor(Item):
    def __init__(self, iname, armor_val):
        Item.__init__(self, iname)
        self.armor = armor_val
        
