from field import Field

my_field = Field()

for i in range(25):
    my_field.spawn_units()
for unit in my_field.units:
    print(unit.__str__())
print()

for i in range(500):
    my_field.step()




print(my_field.can_place_tower([150, 200]))
