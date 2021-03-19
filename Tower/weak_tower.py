from abc import ABC, abstractmethod
from tower import Tower, TowerCreator


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


class WeakTowerCreator(TowerCreator):
	def __init__(self):
		super().__init__()

	def create(self, *args, **kwargs) -> Tower:
		return WeakTower(*args, **kwargs)
