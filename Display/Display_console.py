from Display import Display
import os
import sys

class DisplayConsole(Display):
	def __init__(self):
		super().__init__()
		self.count = 0

	def start(self):
		print("Let's stars!")

	def end(self):
		print("Game is over!")

	def show(self, field):
		self.count += 1
		if(self.count % 100 == 0):
			os.system('clear')
			for unit in field.units:
				print(unit)

			for tower in field.towers:
				print(tower)
