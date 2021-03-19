import unit_factories

weak_creator = unit_factories.WeakUnitCreator()
weak = weak_creator.create(coordinates = [2, 5])

print('weak set at coordinates x = {}, y = {}'.format(weak.position[0], weak.position[1]), '; health = ', weak.health, '; damage = ', weak.damage)


average_creator = unit_factories.AverageUnitCreator()
average = average_creator.create(coordinates = [0, -3])

print('average set at coordinates x = {}, y = {}'.format(average.position[0], average.position[1]), '; health = ', average.health, '; damage = ', average.damage)

chad_creator = unit_factories.ChadUnitCreator()
chad = chad_creator.create(coordinates = [7, 3])

print('chad set at coordinates x = {}, y = {}'.format(chad.position[0], chad.position[1]), '; health = ', chad.health, '; damage = ', chad.damage)
