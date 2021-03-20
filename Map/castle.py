class Castle:

    def __init__(self):
        self.health = 100
        self.produce_money = 1


    def belongs_to_castle(self, coordinates):
        return 0 <= coordinates[0] <= 1 and 7<= coordinates[1] <= 12


    def get_health(self):
        return self.health

    
    def decrease_health(self, damage):
        self.health -= damage
