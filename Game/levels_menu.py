from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from .interface import Interface
from .game import Game

import os
import json

from ..Command.forced_exit import ForcedExitCommand
from ..Command.choose_level import ChooseLevelCommand
from ..Command.quit_page import QuitPageCommand

class LevelsMenu:
	def __init__(self, mode, other_display):
		current_path = os.getcwd()

		with open(os.path.join(current_path, "TowerDefence/Data/levels_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.mode = mode

		if mode == "console":
			self.display = DisplayConsole(other_display)
			self.dispatcher = DispatcherConsole()
			self.interface = None

		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"])
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height, other_display)
			self.dispatcher = DispatcherGraphics(self.interface)
		else:
			raise ValueError("wrong type of mode")

	def start(self):
		self.display.start()
		self.dispatcher.start()

		get_stop_command = False
		running = True
		
		while running:
			self.display.show_menu()
			for event in self.dispatcher.get_events():
				if isinstance(event, ForcedExitCommand):
					running = False
					get_stop_command = True
					return ForcedExitCommand()

				elif isinstance(event, ChooseLevelCommand):
					game = Game(self.mode, event.level, self.display)
					thrown_command = game.start()
					if isinstance(thrown_command, ForcedExitCommand):
						self.display.finish()
						self.dispatcher.finish()
						return ForcedExitCommand()
					if isinstance(thrown_command, QuitPageCommand):
						continue

				if isinstance(event, QuitPageCommand):
					return QuitPageCommand()
