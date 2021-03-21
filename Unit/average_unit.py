from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class AverageUnit(Unit):

	damage = 2
	speed_of_attack = 1	
	range_of_attack = 5
	step = 1
	bounty = 10
		

	def __init__(self, *args, **kwargs):
		self.coordinates = kwargs['coordinates']
		self.last_attack_time = 0
		self.health = 5
		self.speed = [0, -1]


	def __str__(self):
		print('AverageUnit:' + '{:.>20}'.format(self.coordinates.__str__()))