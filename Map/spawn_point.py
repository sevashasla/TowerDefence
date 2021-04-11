from random import randint
import time
<<<<<<< HEAD
<<<<<<< HEAD
import json
=======
>>>>>>> delete it later
=======
import json
>>>>>>> add files to checkpoint 2


from ..Unit.unit_factories import *
from ..Game.coordinates import Coordinates

class SpawnPoint:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
	
	creators = [WeakUnitCreator(), AverageUnitCreator(), ChadUnitCreator()]

	def __init__(self, position, wvs):
		self.x1 = position["x1"]
		self.x2 = position["x2"]
		self.y1 = position["y1"]
		self.y2 = position["y2"]
		self.last_wave = 0.0
		self.cooldown = 0
		self.waves = []
		self.timer = []
		for each in wvs:
			self.waves.append(each["wave"])
			self.timer.append(each["time"])
		self.waves.reverse()
		self.timer.reverse()


	def generate_random_coordinate(self) -> Coordinates:
		return Coordinates(randint(self.x1 + 1, self.x2 - 1), 
						   randint(self.y1 + 1, self.y2 - 1))


	def wave(self):
		units = []
		for unit_type in self.waves[-1]:
			unit = self.creators[unit_type].create(coordinates=self.generate_random_coordinate())
			units.append(unit)
		self.last_wave = time.time()
		if (len(self.timer) >= 2):
			self.cooldown = self.timer[-2] - self.timer[-1]
		else:
			self.cooldown = -1
		self.waves.pop()
		self.timer.pop()
		return units
<<<<<<< HEAD
=======
    

    def __init__(self, width, height, waves):
        self.last_wave = 0.0
        self.width = width
        self.height = height
        self.time_out = 1.5


    def wave(self, waves_count):


        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!NOW WE HAVE WAVES AND WE HAVE TO CHANGE OUT LOGIC!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        
        creators = [WeakUnitCreator(), AverageUnitCreator(), ChadUnitCreator()]
        if waves_count <= 5:
            size_of_wave = randint(1, 3)
            wave = []
            for i in range(size_of_wave):
                coords = Coordinates(randint(self.width * 9//20, self.width*11//20), randint(self.height - 30, self.height - 1))
                unit = creators[1].create(coordinates=coords)
                wave.append(unit)
            return wave
        elif waves_count <= 15:
            size_of_wave = randint(2,7)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,1)
                coords = Coordinates(randint(self.width * 9//20, self.width*11//20), randint(self.height - 30, self.height - 1))
                unit = creators[type_of_unit].create(coordinates=coords)
                wave.append(unit)
            return wave
        else:
            size_of_wave = randint(3,10)
            wave = []
            for i in range(size_of_wave):
                type_of_unit = randint(0,2)
                coords = Coordinates(randint(self.width * 9//20, self.width*11//20), randint(self.height - 30, self.height - 1))
                unit = creators[type_of_unit].create(coordinates=coords)
                wave.append(unit)
            return wave
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2
