from road import Road, FieldError
from castle import Castle



class Field:

	x_size = 20
	y_size = 20

	def __init__(self):
		self.cells = []
		for i in range(self.x_size):
			self.cells.append([None] * self.y_size)
		self.road = Road()
		self.castle = Castle()


	def can_make_step(self, coordinates) -> bool:
		try:
			if self.road.belongs_to_road(coordinates):
				return self.road[coordinates[0]][coordinates[1]] is None
			return False
		except IndexError:
			return False


	def can_place_tower(self, coordinates) -> bool:
		try:
			if not self.road.belongs_to_road(coordinates) and not self.castle.belongs_to_castle(coordinates):
				return self.cells[coordinates[0]][coordinates[1]] is None
		except IndexError:
			return False


	def place_tower(self, tower, coordinates):
		if self.can_place_tower(coordinates):
			self.cells[coordinates[0]][coordinates[1]] = tower
		else:
			raise FieldError


	def move(self, coords_1, coords_2):
		self.road.move(coords_1, coords_2)
		self.cells[coords_2[0]][coords_2[1]] = self.cells[coords_1[0]][coords_1[1]]
		self.cells[coords_1[0]][coords_1[1]] = None

