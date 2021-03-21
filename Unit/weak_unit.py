from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class WeakUnit(Unit):

	damage = 1
	speed_of_attack = 1.25
	range_of_attack = 5
	bounty = 5
	

	def __init__(self, *args, **kwargs):
		self.coordinates= kwargs['coordinates']
		self.last_attack_time = 0
		self.health = 3
		self.speed = [0, -2]
		self.image_name = "weak_unit.jpeg"

	def __str__(self):
		print('WeakUnit:' + '{:.>20}'.format(self.coordinates.__str__()))


