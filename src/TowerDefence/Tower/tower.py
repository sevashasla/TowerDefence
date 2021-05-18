from abc import ABC, abstractmethod
import time
<<<<<<< HEAD:Tower/tower.py
from math import hypot

=======
import sys
>>>>>>> checkpoint_3:src/TowerDefence/Tower/tower.py

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
		cooldown = self.attack_time * self.speed_of_attack
		passed_time = time.time() - self.last_attack_time
		if passed_time >= cooldown:
			return hypot(self.coordinates.x - enemy.coordinates.x, 
				self.coordinates.y - enemy.coordinates.y) <= self.range_of_attack
		return False

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage

	def dump(self, file=sys.stdout):
		file.write(str(self))
