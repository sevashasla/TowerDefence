from .command import Command

class QuitPageCommand(Command):
	def __init__(self):
		pass

	def __str__(self) -> str:
		return "Quit current page"
