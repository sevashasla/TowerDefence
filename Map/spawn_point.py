from random import randint
import time
import json


from ..Unit.unit_factories import *
from ..Game.coordinates import Coordinates

class SpawnPoint:
	
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
