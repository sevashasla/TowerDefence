class Castle:

    def __init__(self, width, height, castle_parameters):
        self.health = castle_parameters["health"]
        self.produce_money = castle_parameters["produce_money"]
        self.width = width
        self.height = height


    def belongs_to_castle(self, coordinates) -> bool:
        #####STRANGE#######
        return 0 <= coordinates.y <= self.height//20 and self.width*7//20 <= coordinates.x <= self.width*12//20


    def get_health(self) -> int:
        return self.health

    
    def decrease_health(self, damage) -> None:
        self.health -= damage
