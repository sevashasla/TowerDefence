from abc import ABC, abstractmethod
import time


# https://refactoring.guru/ru/design-patterns/factory-method/python/example

class Unit(ABC):

	update_time = 0.1
	attack_time = 1.0

	@abstractmethod
	def __init__(self, spawn_point, update_time):
		pass


	def attack(self, tower):
		for towers in tower:
			if self.can_attack(tower):
				self.last_attack_time = time.clock()
				tower.decreaseHealth(self.damage)
				break

	def can_attack(self, tower) -> bool:
		if time.time() - self.last_attack_time >= self.attack_time * self.speed_of_attack:
			return (self.coordinates.x - tower.coordinates.x)**2 + (self.coordinates.y - tower.coordinates.y)**2 <= self.range_of_attack**2
		return False

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage


	def make_step(self):
		self.coordinates.x += self.speed[0]
		self.coordinates.y += self.speed[1]

	def __del__(self):
		# Pocket.addMoney(self.bounty)
		pass
		
	@abstractmethod
	def __str__(self) -> str:
		pass


class UnitCreator(ABC):
		
	def __init__(self):
		pass
		
	@abstractmethod
	def create(self, *args, **kwargs) -> Unit:
		pass

