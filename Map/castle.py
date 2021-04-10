import time
from ..Game.coordinates import Coordinates

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

    def belongs_to_castle(self, coordinates) -> bool:
        return abs(coordinates.x - (self.coordinates.x + self.width / 2)) <= self.width / 2 and \
               abs(coordinates.y - (self.coordinates.y + self.height / 2)) <= self.height / 2


    def get_health(self) -> int:
        return self.health

    
    def decrease_health(self, damage) -> None:
        self.health -= damage
