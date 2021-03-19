from abc import ABC, abstractmethod
import time


# https://refactoring.guru/ru/design-patterns/factory-method/python/example

class Unit(ABC):

	@abstractmethod
	def __init__(self, spawn_point):
		pass


	def attack(self, tower):
		for towers in tower:
			if self.can_attack(tower):
				last_attack_time = time.clock()
				tower.decreaseHealth(self.damage)
				break

	def can_attack(self, tower):
		return (self.position.x - tower.position.x)**2 + (self.position.y - tower.position.y)**2 <= range_of_attack**2

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage

	@abstractmethod
	def make_step(self):
		pass

	def __del__(self):
		# Pocket.addMoney(self.bounty)
                pass


class UnitCreator(C):
		
	def __init__(self):
		pass
		
	@abstractmethod
	def create(self, *args, **kwargs) -> Unit:
		pass

