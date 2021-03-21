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
<<<<<<< HEAD
		self.image_name = "weak_unit.jpeg" #change later
=======
>>>>>>> 585b772da578a7523f92f23d20a031b3a5cb29f6


	def __str__(self):
		print('ChadUnit:' + '{:.>20}'.format(self.coordinates.__str__()))