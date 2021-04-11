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
