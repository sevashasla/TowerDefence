from abc import ABC, abstractmethod
from .unit import Unit

#there is a lot of work to be done

class WeakUnit(Unit):

	damage = 4
	speed_of_attack = 1.25
	range_of_attack = 50
	bounty = 5
	max_health = 5
	speed_abs = 2

	def __init__(self, *args, **kwargs):
		self.coordinates= kwargs['coordinates']
		self.last_attack_time = 0
		self.health = WeakUnit.max_health
		self.speed = [0, 0]
		self.set_speed_mode(0)

	def __str__(self):
		return f'"Unit_{id(self)}": {{"name": "WeakUnit", "health": {self.health},' + \
		f' "coordinates": {{"x": {self.coordinates.x}, "y": {self.coordinates.y}}} }}'


