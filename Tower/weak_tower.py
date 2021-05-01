from abc import ABC, abstractmethod
from .tower import Tower


class WeakTower(Tower):
	def __init__(self, coordinates):
		super().__init__()
		self.coordinates = coordinates
		self.health = 30
		self.range_of_attack = 50
		self.damage = 10
		self.speed_of_attack = 1
		self.cost = 5
		self.last_attack_time = 0

	def __str__(self):
		return f'"Tower_{id(self)}": {{"name": "WeakTower", "health": {self.health},' + \
		f' "coordinates": {{"x": {self.coordinates.tuple[0]}, "y": {self.coordinates.tuple[1]}}}}}'
