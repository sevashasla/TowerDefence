from .display import Display
import sys
import time
import os

class DisplayConsole(Display):
	
	def __init__(self, other_display=None):
		super().__init__()
		self.last_time_update = time.time()
		self.update_rate = 2.0

		self.copy_from_other = False
		if not other_display is None:
			self.copy_from_other = True

	def start(self):
		if not self.copy_from_other:
			sys.stdout.write("Let's start!\n")

	def finish(self):
		if not self.copy_from_other:
			sys.stdout.write("Game is over!\n")

	def show_menu(self):
		pass

	def show_game(self, field, pocket):
		if (time.time() - self.last_time_update) >= self.update_rate:
			sys.stdout.flush()
			os.system("clear")

			sys.stdout.write("{\n")

			sys.stdout.write(str(field.castle) + ",\n")
			sys.stdout.write(str(pocket) + ",\n")

			for unit in field.units:
				sys.stdout.write(str(unit) + ",\n")

			for tower in field.towers:
				sys.stdout.write(str(tower) + ",\n")

			for attack in field.attacks_by_units:
				sys.stdout.write(f'{{"attack_{id(attack)}": {{ "x1": {attack[0].tuple[0]}, "y1": {attack[0].tuple[1]},' + \
					f' "x2": {attack[1].tuple[0]}, "y2": {attack[1].tuple[1]},  }} }}' + ",\n")

			for attack in field.attacks_by_towers:
				sys.stdout.write(f'{{"attack_{id(attack)}": {{ "x1": {attack[0].tuple[0]}, "y1": {attack[0].tuple[1]},' + \
					f' "x2": {attack[1].tuple[0]}, "y2": {attack[1].tuple[1]},  }} }}' + ",\n")

			sys.stdout.write("}\n")
			self.last_time_update = time.time()
