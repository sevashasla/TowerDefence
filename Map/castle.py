import time
from ..Game.coordinates import Coordinates

class Castle:

    def __init__(self, castle_parameters):
        self.health = castle_parameters["health"]
        self.produce_money = castle_parameters["produce_money"]
        self.cooldown = castle_parameters["cooldown"]
        self.coordinates = Coordinates(coordinates=castle_parameters["coordinates"])
        self.width = castle_parameters["width"]
        self.height = castle_parameters["height"]
        self.last_money_income = 0

    def send_money(self) -> int:
        if time.time() - self.cooldown >= self.last_money_income:
            self.last_money_income = time.time()
            return self.produce_money
        return 0

    def belongs_to_castle(self, coordinates) -> bool:
        #####STRANGE#######
        return 0 <= coordinates.y <= self.height//20 and self.width*7//20 <= coordinates.x <= self.width*12//20


    def get_health(self) -> int:
        return self.health

    
    def decrease_health(self, damage) -> None:
        self.health -= damage
