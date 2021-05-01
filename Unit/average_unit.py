from abc import ABC, abstractmethod
from .unit import Unit

#there is a lot of work to be done

class AverageUnit(Unit):

	damage = 10
	speed_of_attack = 1	
	range_of_attack = 100
	bounty = 10

	def __init__(self, *args, **kwargs):
		self.coordinates = kwargs['coordinates']
		self.last_attack_time = 0
		self.health = 5
		self.speed_abs = 1
		self.speed = [0, 0]
		self.set_speed_mode(0)


	def __str__(self):
		return 'AverageUnit:' + '{:.>20}'.format(self.coordinates.__str__())
