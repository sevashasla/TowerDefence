import functools
<<<<<<< HEAD:Game/coordinates.py
from dataclasses import dataclass

@dataclass
=======


>>>>>>> checkpoint_3:src/TowerDefence/Game/coordinates.py
class Coordinates:

	x: int
	y: int

	def __init__(self, x: int=None, y: int=None, coordinates: list=None):
		self.x = x
		self.y = y
		self.coordinates = coordinates

		if not self.coordinates is None:
			self.x = coordinates[0]
			self.y = coordinates[1]

	@property
	def tuple(self) -> tuple:
		return (self.x, self.y)


	def __str__(self) -> str:
		return str(self.x) + ' ' + str(self.y)
