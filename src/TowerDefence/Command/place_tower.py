from .command import Command

class PlaceTowerCommand(Command):
	def __init__(self, class_of_tower: str, position):
		self.class_of_tower = class_of_tower
		self.position = position

	def __str__(self) -> str:
		return "Place " + self.class_of_tower + " at " + str(self.position)
