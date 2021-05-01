from abc import ABC, abstractmethod
from .unit import Unit

#there is a lot of work to be done

class WeakUnit(Unit):

	damage = 4
	speed_of_attack = 1.25
	range_of_attack = 50
	bounty = 5
	

	def __init__(self, *args, **kwargs):
		self.coordinates= kwargs['coordinates']
		self.last_attack_time = 0
		self.health = 3
		self.speed_abs = 2
		self.speed = [0, 0]
		self.set_speed_mode(0)

	def __str__(self):
		return 'WeakUnit:' + '{:.>20}'.format(self.coordinates.__str__())


