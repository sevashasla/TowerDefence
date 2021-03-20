from Display import Display

class DisplayConsole(Display):
	def __init__(self):
		super().__init__()

	def start(self):
		print("Let's stars!")

	def end(self):
		print("Game is over!")

	def show(self, field):
		#don't want to print road coordinates 
		for unit in field.units:
			print(unit)

		for tower in field.towers:
			print(tower)