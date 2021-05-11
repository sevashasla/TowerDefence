from abc import ABC, abstractmethod
import time
import sys


class Unit(ABC):
	update_time = 0.1
	attack_time = 1.0
	shape = (40, 30)

	@abstractmethod
	def __init__(self, spawn_point, update_time):
		pass

	def attack(self, tower):
		if self.can_attack(tower):
			self.last_attack_time = time.time()
			tower.decrease_health(self.damage)

	def can_attack(self, tower) -> bool:
		if time.time() - self.last_attack_time >= self.attack_time * self.speed_of_attack:
			return ((self.coordinates.x - tower.coordinates.x)**2 + 
					(self.coordinates.y - tower.coordinates.y)**2 <= 
					 self.range_of_attack**2)
		return False

	def get_health(self):
		return self.health

	def decrease_health(self, damage):
		self.health -= damage


	def make_step(self):
		self.coordinates.x += self.speed[0]
		self.coordinates.y += self.speed[1]

	def set_speed_mode(self, mode):
		if mode == 0:
			self.speed = [0, -self.speed_abs]
		if mode == 1:
			self.speed = [self.speed_abs, 0]
		if mode == 2:
			self.speed = [0, self.speed_abs]
		if mode == 3:
			self.speed = [-self.speed_abs, 0]

	def get_speed_mode(self):
		return ((self.speed[1] < 0) * 0 + 
				(self.speed[0] > 0) * 1 +
				(self.speed[1] > 0) * 2 +
				(self.speed[0] < 0) * 3)

	@abstractmethod
	def __str__(self) -> str:
		pass

	def dump(self, file=sys.stdout):
		file.write(str(self))


class UnitCreator(ABC):
		
	def __init__(self):
		pass
		
	@abstractmethod
	def create(self, *args, **kwargs) -> Unit:
		pass

