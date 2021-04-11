class Coordinates:
	def __init__(self, x: int=None, y: int=None, coordinates: list=None):
		self.x = x
		self.y = y
		self.coordinates = coordinates

		if not self.coordinates is None:
			self.x = coordinates[0]
			self.y = coordinates[1]

	def to_tuple(self) -> tuple:
		return (self.x, self.y)


	def __str__(self) -> str:
		return str(self.x) + ' ' + str(self.y)
