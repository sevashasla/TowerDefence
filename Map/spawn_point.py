from random import randint
import time
import json


from ..Unit.unit_factories import *
from ..Game.coordinates import Coordinates
from ..Game.rectangle import Rectangle

class SpawnPoint:
	
	creators = [WeakUnitCreator(), AverageUnitCreator(), ChadUnitCreator()]

	def __init__(self, position, wvs):
		self.places = []
		for rectangle in position:
			self.places.append(((Rectangle(rectangle)), rectangle["mode"]))


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
		place = self.places[randint(0, len(self.places) - 1)]
		point = place[0]
		mode = place[1] 
		coords = Coordinates(randint(point.x1 + 1, point.x2 - 1), 
						   	 randint(point.y1 + 1, point.y2 - 1))
		return (coords, mode)


	def spawn_wave(self):
		units = []
		for unit_type in self.waves[-1]:
			coords, speed_mode = self.generate_random_coordinate()
			unit = self.creators[unit_type].create(coordinates=coords)
			unit.set_speed_mode(speed_mode)
			units.append(unit)
		self.last_wave = time.time()
		if (len(self.timer) >= 2):
			self.cooldown = self.timer[-2] - self.timer[-1]
		else:
			self.cooldown = -1
		self.waves.pop()
		self.timer.pop()
		return units
