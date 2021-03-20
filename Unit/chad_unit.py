from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class ChadUnit(Unit):

	damage = 4
	speed_of_attack = 0.75
	range_of_attack = 5
	speed = [1, 0]
	step = 1
	bounty = 20
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs['coordinates']
		last_attack_time = 0
		self.health = 10
