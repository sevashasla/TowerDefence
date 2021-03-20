from abc import ABC, abstractmethod
from tower import Tower


class AverageTower(Tower):
	def __init__(self, coordinates):
		super().__init__()
		self.coordinates = coordinates
		self.health = 20
		self.range_attack = 10
		self.damage = 7
		self.speed_of_attack = 5
		self.cost = 15
		self.last_attack_time = 0 ####change
		self.image_name = "weak_tower.jpg" ####change

	def __str__(self):
		return "AverageTower " + str(self.coordinates) + ", health = " + str(self.health)
