import sys
import os
from Display import Display

class DisplayConsole(Display):
	def __init__(self):
		super().__init__()

	def start(self):
		print("Let's stars!")

	def show(self, items):
		for item in items:
			print(item)
