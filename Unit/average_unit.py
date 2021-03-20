from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class AverageUnit(Unit):

	damage = 2
	speed_of_attack = 1	
	range_of_attack = 5
	speed = [0, -1]
	step = 1
	bounty = 10
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs['coordinates']
		last_attack_time = 0
		self.health = 5



