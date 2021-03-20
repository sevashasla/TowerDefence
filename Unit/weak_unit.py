from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class WeakUnit(Unit):

	damage = 1
	speed_of_attack = 1	
	range_of_attack = 5
	speed = 1
        step = [1, 0]
	bounty = 5
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs['coordinates']
		last_attack_time = 0
		self.health = 3



