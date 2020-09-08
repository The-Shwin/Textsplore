__author__ = "Ashwin Bhat"

import item
import enemy
import player
import json
import collections


class MapTile:
    def __init__(self, tile_data):
        dims = tile_data.get("coordinates").split()
        self.x = dims[0]
        self.y = dims[1]
        self.text = tile_data.get("intro_text")
        self.tile_type = tile_data.get("tile_type")
        self.move_set = collections.Set(tile_data.get("movement").split())


class WeaponTile(MapTile):
    def __init__(self, tile_data):
        self.weapon = tile_data.get("weapon")
        super().__init__(tile_data)

    def equip_weapon(self, player):
        # Puts old weapon in inventory and equips new one
        player.inventory.append(player.weapon)
        player.weapon = self.weapon

    def add_weapon(self, player):
        # Puts new weapon in inventory
        player.inventory.append(self.weapon)

    def player_change(self, player, equip):
        if equip:
            self.equip_weapon(player)
        else:
            self.add_weapon(player)


class CoinTile(MapTile):
    def __init__(self, tile_data):
        self.coin = tile_data.get("gold")
        super().__init__(tile_data)






# This class will be used to generate the world from json that's get passed in.
class MapMaker:
    def __init__(self, map_file_path):
        with open(map_file_path) as f:
            data = json.load(f)
            self.world_name = data.get("world_name")
            dims = data.get("total_dimensions").split()
            self.x_dim = dims[0]
            self.y_dim = dims[1]
            self.map = data.get("tiles")






