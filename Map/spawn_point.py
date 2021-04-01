from random import randint
import time


from ..Unit.unit_factories import *
from ..Game.coordinates import Coordinates

class SpawnPoint:
    

    def __init__(self, x_size, y_size):
        self.last_wave = 0.0
        self.x_size = x_size
        self.y_size = y_size
        self.time_out = 1.5

    def wave(self, waves_count):
        creators = [WeakUnitCreator(), AverageUnitCreator(), ChadUnitCreator()]
        if waves_count <= 5:
            size_of_wave = randint(1, 3)
            wave = []
            for i in range(size_of_wave):
                coords = Coordinates(randint(self.x_size * 9//20, self.x_size*11//20), randint(self.y_size - 30, self.y_size - 1))
                unit = creators[1].create(coordinates=coords)
                wave.append(unit)
            return wave
        elif waves_count <= 15:
            size_of_wave = randint(2,7)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,1)
                coords = Coordinates(randint(self.x_size * 9//20, self.x_size*11//20), randint(self.y_size - 30, self.y_size - 1))
                unit = creators[type_of_unit].create(coordinates=coords)
                wave.append(unit)
            return wave
        else:
            size_of_wave = randint(3,10)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,2)
                coords = Coordinates(randint(self.x_size * 9//20, self.x_size*11//20), randint(self.y_size - 30, self.y_size - 1))
                unit = creators[type_of_unit].create(coordinates=coords)
                wave.append(unit)
            return wave
