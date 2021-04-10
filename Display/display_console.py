from .display import Display
import os
import sys
import time

class DisplayConsole(Display):
	def __init__(self):
		super().__init__()
		self.last_time_update = time.time()
		self.update_rate = 3

	def start(self):
		print("Let's start!")

	def end(self):
		print("Game is over!")

	def show(self, field, pocket):

		if((time.time() - self.last_time_update) >= self.update_rate):
			sys.stdout.flush()
			print(pocket.get_money())

			for unit in field.units:
				print(unit)

			for tower in field.towers:
				print(tower)

			self.last_time_update = time.time()