from abc import ABC, abstractmethod
from unit import Unit, UnitCreator

#there is a lot of work to be done

class WeakUnit(Unit):

	damage = 1
	speed_of_attack = 1	
	range_of_attack = 5
	speed = 1
	step = 1
	bounty = 5
		

	def __init__(self, *args, **kwargs):
		self.position = kwargs[spawn_point]
		last_attack_time = 0
		self.health = 3


weak = WeakUnit(3, 6)
print(weak.health, weak.step, weak.damage)
