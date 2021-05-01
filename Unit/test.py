import unit_factories
import sys
sys.path.insert(0, "../Game/")
from coordinates import Coordinates

a = Coordinates(2, 5)

weak_creator = unit_factories.WeakUnitCreator()
weak = weak_creator.create(coordinates = a)

print('weak set at coordinates x = {}, y = {}'.format(weak.coordinates.x, weak.coordinates.y), '; health = ', weak.health, '; damage = ', weak.damage)


average_creator = unit_factories.AverageUnitCreator()
average = average_creator.create(coordinates = a)

print('average set at coordinates x = {}, y = {}'.format((average.coordinates.x, average.coordinates.y), '; health = ', average.health, '; damage = ', average.damage))

chad_creator = unit_factories.ChadUnitCreator()
chad = chad_creator.create(coordinates = a)

print('chad set at coordinates x = {}, y = {}'.format(chad.coordinates.x, chad.coordinates.y), '; health = ', chad.health, '; damage = ', chad.damage)

print(chad.update_time)
