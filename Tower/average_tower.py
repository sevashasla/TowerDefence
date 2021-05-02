from abc import ABC, abstractmethod
from .tower import Tower


class AverageTower(Tower):

	max_health = 50
	damage = 15
	speed_of_attack = 5
	range_of_attack = 150
	cost = 15

	def __init__(self, coordinates):
		super().__init__()
		self.coordinates = coordinates
		self.health = AverageTower.max_health
		self.last_attack_time = 0 ####chang

	def __str__(self):
		return f'"Tower_{id(self)}": {{"name": "AverageTower", "health": {self.health},' + \
		f' "coordinates": {{"x": {self.coordinates.tuple[0]}, "y": {self.coordinates.tuple[1]}}}}}'
