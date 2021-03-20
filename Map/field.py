from road import Road, FieldError
from castle import Castle
from random import randint
from spawn_point import SpawnPoint


class Field:

	x_size = 500
	y_size = 500
	waves_spawned = 0

	def __init__(self):
		self.cells = []
		for i in range(self.x_size):
			self.cells.append([None] * self.y_size)
		self.road = Road(self.x_size, self.y_size)
		self.castle = Castle(self.x_size, self.y_size)
		self.spawn_point = SpawnPoint(self.x_size, self.y_size)
		self.units = []
		self.towers = []


	def can_make_step(self, unit) -> bool:
		try:    
			new_coords_x = unit.position[0] + randint(5, 20) * speed[0]
			new_coords_y = unit.position[1] + randint(5, 20) * speed[1]
			if self.road.belongs_to_road((new_coords_x, new_coords_y)):
				return self.road[new_coords_x][new_coords_y]
		except IndexError:
			return False


	def can_place_tower(self, coords) -> bool:
		# try:
		# 	if not self.road.belongs_to_road(coords) and not self.castle.belongs_to_castle(coords):
		# 		return self.cells[coords[0]][coords[1]] is None
		# except IndexError:
		# 	return False



		return True


	def place_tower(self, tower, coords):
		if self.can_place_tower(coords):
			self.towers.append(tower)
		else:
			raise FieldError


	def destroy (self, coordinates):
		self.cells[coordinates[0]][coordinates[1]] = None


	def move(self, coords_1, coords_2):
		self.cells[coords_2[0]][coords_2[1]] = self.cells[coords_1[0]][coords_1[1]]
		self.cells[coords_1[0]][coords_1[1]] = None


	def spawn_units(self):
		waves_spawned += 1
		for unit in self.spawn_point.wave(waves_spawned):
			unit.make_step()
			self.units.append(unit)

	def step(self):
		pass
