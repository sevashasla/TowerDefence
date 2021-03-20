from random import randint

class SpawnPoint:
    

    def __init__(x_size, y_size):
        self.x_size = x.size
        self.y_size = y.size

    def wave(waves_count):
        creators = [WeakUnitCreator(), AverageUnitCreator(), ChadUnitCreator()]
        if waves_count <= 5:
            size_of_wave = randint(1, 3)
            wave = []
            for i in range(size_of_wave):
                coords = (self.y_size-1, randint(self.x_size * 9//20, self.x_size*11//20))
                unit = creator[1].create(coordinates=coords))
                wave.append(unit)
            return wave
        elif waves_count <= 15:
            size_of_wave = randint(2,7)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,1)
                coords = (self.y_size-1, randint(self.x_size * 9//20, x_size*11//20))
                unit = creators[type_of_unit].create(coordinates=coords))
                wave.append(unit)
            return wave
        else:
            size_of_wave = randint(3,10)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,2)
                coords = (self.y_size-1, randint(self.x_size * 9//20, self.x_size*11//20))
                unit = creators[type_of_unit].create(coordinates=coords))
                wave.append(unit)
            return wave
