from abc import ABC, abstractmethod

# https://refactoring.guru/ru/design-patterns/factory-method/python/example

class Tower(ABC):
	@abstractmethod
	def __init__(self):
		pass

	def attack(self, enemies: list) -> list:
		for enemy in enemies:
			if(self.can_attack(enemy)):
				enemy.decrease_health(self.damage)
				break
			self.last_attack_time = 0  ####change
		return enemies

	def can_attack(self, enemy):
		return ((self.coordinates.x - enemy.coordinates.x) ** 2 + 
			(self.coordinates.y - enemy.coordinates.y) ** 2 <=  self.range_attack ** 2)

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage



class TowerCreator(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def create(self, *args, **kwargs) -> Tower:
		pass

