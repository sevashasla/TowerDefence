from abc import ABC, abstractmethod
from unit import Unit

#there is a lot of work to be done

class ChadUnit(Unit):

	damage = 4
	speed_of_attack = 0.75
	range_of_attack = 5
	step = 1
	bounty = 20
		

	def __init__(self, *args, **kwargs):
		self.coordinates= kwargs['coordinates']
		self.last_attack_time = 0
		self.health = 10	
		self.speed = [0, -1]
		self.image_name = "weak_unit.jpeg" #change later


	def __str__(self):
		print('ChadUnit:' + '{:.>20}'.format(self.coordinates.__str__()))