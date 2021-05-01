from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from .interface import Interface
from .levels_menu import LevelsMenu
from .rules_menu import RulesMenu

import os
import json

from ..Command.levels_menu import LevelsMenuCommand
from ..Command.rules_menu import RulesMenuCommand
from ..Command.stop import StopCommand
from ..Command.choose_level import ChooseLevelCommand

class MainMenu:
	def __init__(self, mode):
		current_path = os.getcwd()

		self.mode = mode

		with open(os.path.join(current_path, "TowerDefence/Data/main_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]


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

		self.levels = LevelsMenu(self.mode, self.display)
		self.rules = RulesMenu(self.mode, self.display)
		
		running = True

		while running:
			self.display.show_menu()
			for event in self.dispatcher.get_events():
				if isinstance(event, StopCommand):
					running = False

				elif isinstance(event, LevelsMenuCommand):
					running = not self.levels.start()

				elif isinstance(event, RulesMenuCommand):
					running = not self.rules.start()

		self.dispatcher.finish()
		self.display.finish()

