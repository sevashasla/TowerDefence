import time
from ..Game.coordinates import Coordinates
import functools
import sys

class Castle:

    def __init__(self, castle_parameters):
        self.health = castle_parameters["health"]
        self.produce_money = castle_parameters["produce_money"]
        self.cooldown = castle_parameters["cooldown"]
        self.coordinates = Coordinates(castle_parameters["coordinates"][0],
                                       castle_parameters["coordinates"][1])
        self.width = castle_parameters["width"]
        self.height = castle_parameters["height"]
        self.last_money_income = 0

    def send_money(self) -> int:
        if time.time() - self.cooldown >= self.last_money_income:
            self.last_money_income = time.time()
            return self.produce_money
        return 0

    @property
    def center(self):
        return Coordinates(self.coordinates.x + self.width / 2, self.coordinates.y + self.height / 2)

    def belongs_to_castle(self, coordinates) -> bool:
        return abs(coordinates.x - (self.coordinates.x + self.width / 2)) <= self.width / 2 and \
               abs(coordinates.y - (self.coordinates.y + self.height / 2)) <= self.height / 2


    def get_health(self) -> int:
        return max(self.health, 0)

    
    def decrease_health(self, damage) -> None:
        self.health -= damage

    def __str__(self):
        return f'"Castle": {{"name": "Castle", "health": {self.health}, ' + \
        f'"coordinates": {{ "x": {self.coordinates.x}, "y":{self.coordinates.y}}}}}'

    def dump(self, file=sys.stdout):
        file.write(str(self))
