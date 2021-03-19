from abc import ABC, abstractmethod
from tower import Tower, TowerCreator


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


class AverageTowerCreator(TowerCreator):
	def __init__(self):
		super().__init__()

	def create(self, *args, **kwargs) -> Tower:
		return AverageTowerCreator(*args, **kwargs)
