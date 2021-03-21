from abc import ABC, abstractmethod
from tower import Tower


class WeakTower(Tower):
	def __init__(self, coordinates):
		super().__init__()
		self.coordinates = coordinates
		self.health = 10
		self.range_attack = 5
		self.damage = 3
		self.speed_of_attack = 1
		self.cost = 5
		self.last_attack_time = 0 

	def __str__(self):
		return "weak tower " + str(self.coordinates) + ", health = " + str(self.health)
