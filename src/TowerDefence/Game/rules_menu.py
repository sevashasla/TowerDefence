from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from .interface import Interface

import os
import json

from ..Command.forced_exit import ForcedExitCommand
from ..Command.quit_page import QuitPageCommand

class RulesMenu:
	def __init__(self, mode, game_path, other_display):
		self.game_path = game_path

		with open(os.path.join(self.game_path, "Data/rules_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		if mode == "console":
			self.display = DisplayConsole(other_display, self.game_path)
			self.dispatcher = DispatcherConsole(self.game_path)
			self.interface = None

		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"], data["text"], self.game_path)
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height, game_path, other_display)
			self.dispatcher = DispatcherGraphics(self.interface, self.game_path)
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
				if isinstance(event, ForcedExitCommand):
					self.dispatcher.finish()
					self.display.finish()
					return ForcedExitCommand()
				elif isinstance(event, QuitPageCommand):
					return QuitPageCommand()
		
