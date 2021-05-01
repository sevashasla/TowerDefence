from .display import Display
import sys
import time

class DisplayConsole(Display):
	
	def __init__(self):
		super().__init__()
		self.last_time_update = time.time()
		self.update_rate = 3

	def start(self):
		sys.stdout.write("Let's start!\n")

	def finish(self):
		sys.stdout.write("Game is over!\n")


	def show_menu(self):
		pass

	def show(self, field, pocket):

		if((time.time() - self.last_time_update) >= self.update_rate):
			sys.stdout.flush()

			sys.stdout.write("NEW STEP\n")

			sys.stdout.write(str(pocket.get_money()) + "\n")

			for unit in field.units:
				sys.stdout.write(str(unit) + "\n")

			for tower in field.towers:
				sys.stdout.write(str(tower) + "\n")

			self.last_time_update = time.time()