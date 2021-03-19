from abc import ABC, abstractmethod
from unit import Unit, UnitCreator

#there is a lot of work to be done

class ChadUnit(Unit):

	damage = 5
	speed_of_attack = 0.75	
	range_of_attack = 7
	speed = 1
	step = 1
	bounty = 15
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs[spawn_point]
                last_attack_time = 0
		self.health = 10
chad = ChadUnit(coordinates)
print(chad.health, chad.step, chad.damage)
