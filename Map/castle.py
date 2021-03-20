class Castle:

    def __init__(self, x_size, y_size):
        self.health = 100
        self.produce_money = 1
        self.x_size = x_size
        self.y_size = y_size


    def belongs_to_castle(self, coordinates):
        return 0 <= coordinates[1] <= self.y_size//20 and self.x_size*7//20 <= coordinates[0] <= self.x_size*12//20


    def get_health(self):
        return self.health

    
    def decrease_health(self, damage):
        self.health -= damage
