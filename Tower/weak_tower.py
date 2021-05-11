from abc import ABC, abstractmethod
from .tower import Tower


class WeakTower(Tower):

	max_health = 30
	damage = 5
	speed_of_attack = 1
	range_of_attack = 75
	cost = 5

	def __init__(self, coordinates):
		super().__init__()
		self.coordinates = coordinates
		self.health = WeakTower.max_health
		self.last_attack_time = 0

	def __str__(self):
		return f'"Tower_{id(self)}": {{"name": "WeakTower", "health": {self.health},' + \
		f' "coordinates": {{"x": {self.coordinates.tuple[0]}, "y": {self.coordinates.tuple[1]}}}}}'
