__author__ = "Ashwin Bhat"

import item
import enemy
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
        if self.tile_type == "start":
            self.shop = None
            self.enemy = None
            self.weapon = None
            self.coin = None
        elif self.tile_type == "shop":
            self.shop = tile_data.get("items")
            self.enemy = None
            self.weapon = None
            self.coin = None
        elif self.tile_type == "weapon_drop":
            self.shop = None
            self.enemy = None
            self.weapon = tile_data.get("weapon")
            self.coin = None
        elif self.tile_type == "gold_drop":
            self.shop = None
            self.enemy = None
            self.weapon = None
            self.coin = tile_data.get("gold")
        elif self.tile_type == "enemy_room":
            self.shop = None
            self.enemy = tile_data.get("enemy")
            self.weapon = None
            self.coin = None
        elif self.tile_type == "healing_room":
            self.shop = None
            self.enemy = None
            self.weapon = None
            self.coin = None
        elif self.tile_type == "end":
            self.shop = None
            self.enemy = None
            self.weapon = None
            self.coin = None


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






