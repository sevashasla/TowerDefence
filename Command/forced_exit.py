from .command import Command

class ForcedExitCommand(Command):
	def __init__(self):
		pass

	def __str__(self) -> str:
		return "Stop"
