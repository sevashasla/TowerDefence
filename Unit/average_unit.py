from abc import ABC, abstractmethod
from unit import Unit, UnitCreator

#there is a lot of work to be done

class AverageUnit(Unit):

	damage = 2
	speed_of_attack = 1	
	range_of_attack = 4
	speed = 1
	step = 1
	bounty = 10
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs[spawn_point]
                last_attack_time = 0
		self.health = 5


average = AverageUnit(coordinates)
print(average.health, average.step, average.damage)
