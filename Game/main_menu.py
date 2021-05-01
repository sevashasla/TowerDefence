from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from .interface import Interface
from .levels_menu import LevelsMenu
from .rules_menu import RulesMenu

import os
import json

class MainMenu:
	def __init__(self, mode):
		current_path = os.getcwd()
		with open(os.path.join(current_path, "TowerDefence/Data/last_completed_level.json")) as f:
			last_completed_level = json.loads(os.path.join(f.read()))["last_completed_level"] + 1

		with open(os.path.join(current_path, "TowerDefence/Data/main_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.levels = LevelsMenu(mode)
		self.rules = RulesMenu(mode)

		if mode == "console":
			self.display = DisplayConsole()
			self.dispatcher = DispatcherConsole()
			self.interface = None
		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"])
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height)
			self.dispatcher = DispatcherGraphics(self.interface)
		else:
			raise ValueError("wrong type of mode")



	def start(self):
		self.display.start()
		self.dispatcher.start()

		running = True

		while running:
			for event in self.dispatcher.get_events():
				if(event[0] == "stop"):
					running = False
				elif (event[0] == "place"):
					class_of_button = event[1]
					position = event[2]
					
					print("You've click at", position)

					if class_of_button == "LevelsMenu":
						self.levels.start()
					elif class_of_button == "RulesMenu":
						self.rules.start()

			self.display.show_menu()

		self.dispatcher.finish()
		self.display.finish()
