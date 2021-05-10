from .command import Command

class ChooseLevelCommand(Command):
	def __init__(self, level: str):
		self.level = level
		
	def __str__(self) -> str:
		return "ChooseLevel " + self.level
