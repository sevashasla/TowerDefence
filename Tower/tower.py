from abc import ABC, abstractmethod
import time
from math import hypot


class Tower(ABC):

	update_time = 0.1
	attack_time = 1.0
	shape = (40, 30)

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def __str__(self):
		pass


	def attack(self, enemy):
		if self.can_attack(enemy):
			self.last_attack_time = time.time()
			enemy.decrease_health(self.damage)

	def can_attack(self, enemy) -> bool:
		if time.time() - self.last_attack_time >= self.attack_time * self.speed_of_attack:
			return hypot(self.coordinates.x - enemy.coordinates.x, 
				self.coordinates.y - enemy.coordinates.y) <= self.range_of_attack
		return False

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage


