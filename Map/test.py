import field
from road import Road, FieldError
from castle import Castle
from random import randint
from spawn_point import SpawnPoint


import sys
sys.path.insert(0, "../Game/")
sys.path.insert(0, "../Tower/")

from coordinates import Coordinates
from tower_factories import *
from pocket import Pocket
from coordinates import Coordinates
my_field = field.Field(0.1)

a = Coordinates([2, 5])
b = Coordinates([2, 3])

my_field.units.append(field.tower_factories.WeakUnitCreator.create(coordinates=a))

my_field.units.append(WeakUnitCreator.create(coordinates=b))

my_field.units.append(WeakUnitCreator.create(coordinates=a))

time.sleep(2)
my_field.units[2].health = -1
my_field.update()
print(my_field.units)
print(my_field.can_place_tower([150, 200]))

			# unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			# if self.can_make_step(unit, distance):
			#	directions[(3 + shift) % 4] = True
			# unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			
			# unit.speed[0], unit.speed[1] = - unit.speed[0], - unit.speed[1]
			# if self.can_make_step(unit, far_distance):
			#	directions[(shift + 2) % 4] = True
			# unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			# if self.can_make_step(unit, distance):
			#	directions[(1 + shift) % 4] = True
			# unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			


			# if self.can_make_step(unit, distance):
			#	unit.make_step()
			#	continue
			# if unit.speed[0] != 0:
			#	unit.speed[0], unit.speed[1] = unit.speed[1], -abs(unit.speed[0])
			#	if (self.can_make_step(unit, distance)):
			#		unit.make_step()
			#		continue
			# else:
			#	unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			#	distance = 75
			#	if self.can_make_step(unit, distance):
			#		unit.make_step()
			#		continue
			#	else:
			#		unit.speed[0] *= -1
			#		if (self.can_make_step(unit, distance)):
			#			unit.make_step()
			#			continue
			#	unit.speed[0], unit.speed[1] = unit.speed[1], -abs(unit.speed[0])
			#	if (self.can_make_step(unit, distance)):
			#		unit.make_step()

