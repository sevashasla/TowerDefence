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

class Field:

	x_size = 500
	y_size = 500

	def __init__(self, update_rate):
		self.road = Road(self.x_size, self.y_size)
		self.castle = Castle(self.x_size, self.y_size)
		self.spawn_point = SpawnPoint(self.x_size, self.y_size)
		self.units = []
		self.towers = []
		self.waves_spawned = 0
		self.update_rate = update_rate
		self.last_update = 0.0


	def can_make_step(self, unit) -> bool:
		try:    
			new_coords_x = unit.coordinates.x + randint(2, 18) * unit.speed[0]
			new_coords_y = unit.coordinates.y + randint(2, 18) * unit.speed[1]
			new_coords = Coordinates(new_coords_x, new_coords_y)
			if self.road.belongs_to_road(new_coords):
				return self.road.pixels[new_coords.x][new_coords.y]
		except IndexError:
			return False


	def can_place_tower(self, coords) -> bool:
		# try:
		# 	if not self.road.belongs_to_road(coords) and not self.castle.belongs_to_castle(coords):
		# 		return self.cells[coords[0]][coords[1]] is None
		# except IndexError:
		# 	return False

		return True


	def place_tower(self, tower):
		if self.can_place_tower(tower.coordinates):
			self.towers.append(tower)
		else:
			raise FieldError


	def destroy (self, tower):
		self.towers.remove(tower)


	def move(self, coords_1, coords_2):
		# self.cells[coords_2[0]][coords_2[1]] = self.cells[coords_1[0]][coords_1[1]]
		# self.cells[coords_1[0]][coords_1[1]] = None
		pass


	def spawn_units(self):
		self.waves_spawned += 1
		for unit in self.spawn_point.wave(self.waves_spawned):
			unit.make_step()
			self.units.append(unit)

	def units_step(self):
		
		for unit in self.units:
			if self.can_make_step(unit):
				unit.make_step()
				continue
			if unit.speed[1] == 0:
				unit.speed[1] = -abs(unit.speed[0])
				unit.speed[0] = 0
			if self.can_make_step(unit):
				unit.make_step()
				continue
			unit.speed[0], unit.speed[1] = unit.speed[1], unit.speed[0]
			if self.can_make_step(unit):
				unit.make_step()
				continue
			unit.speed[0] *= -1
			if self.can_make_step(unit):
				unit.make_step()
				continue
			continue
			for unit in self.units:
				print(unit.__str__())
			print()

	def units_attack(self):
		for unit in self.units:
			for tower in self.towers:
				if unit.can_attack(tower):
					unit.attack(tower)	
	def towers_attack(self):
		for tower in self.towers:
			for unit in self.units:
				if tower.can_attack(unit):
					tower.attack(unit)

	def collect_garbage(self):
		for unit in units:
			if unit.health <= 0:
				Pocket.addMoney(unit.bounty)
				units.remove(unit)

	def field_update():
		current_time = time.clock()
		if current_time - self.last_update >= update_rate:
			self.units_step()
			self.towers_attack()
			self.units_attack()
			self.collect_garbage()


