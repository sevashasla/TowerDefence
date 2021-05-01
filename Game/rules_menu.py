from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from .interface import Interface

import os
import json

from ..Command.stop import StopCommand

class RulesMenu:
	def __init__(self, mode, other_display):
		current_path = os.getcwd()

		with open(os.path.join(current_path, "TowerDefence/Data/levels_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

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
		self.dispatcher.start()
		self.display.start()

		get_stop_command = False
		running = True

		while running:
			self.display.show_menu()
			for event in self.dispatcher.get_events():
				if isinstance(event, StopCommand):
					running = False
					get_stop_command = True

		self.dispatcher.finish()
		self.display.finish()

		return get_stop_command
