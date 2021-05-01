from .command import Command

class StopCommand(Command):
	def __init__(self):
		pass

	def __str__(self) -> str:
		return "Stop"
