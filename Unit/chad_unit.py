from abc import ABC, abstractmethod
from .unit import Unit

class ChadUnit(Unit):

	damage = 20
	speed_of_attack = 0.75
	range_of_attack = 75
	bounty = 20
	max_health = 10
	speed_abs = 1
	

	def __init__(self, *args, **kwargs):
		self.coordinates= kwargs['coordinates']
		self.last_attack_time = 0
		self.health = ChadUnit.max_health
		self.speed = [0, 0]
		self.set_speed_mode(0)


	def __str__(self):
		return f'"Unit_{id(self)}": {{"name": "ChadUnit", "health": {self.health},' + \
		f' "coordinates": {{"x": {self.coordinates.x}, "y": {self.coordinates.y}}} }}'