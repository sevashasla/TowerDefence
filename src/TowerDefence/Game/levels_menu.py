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

def get_text_paths(game_path, text_name=None):
	if text_name is None:
		return os.path.join(game_path, "Data")
	else:
		return os.path.join(game_path, "Data", text_name)	


class LevelsMenu:
	def __init__(self, mode, game_path, other_display):
		self.game_path = game_path

		with open(os.path.join(self.game_path, "Data/levels_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			self.text = data["text"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.mode = mode

		if mode == "console":
			self.text = []
			for cell in data["text"]:

				with open(get_text_paths(self.game_path, cell["text_path"]), 'r') as cell_file:
					self.text.append(cell_file.read())

			self.display = DisplayConsole(self.text, other_display, self.game_path)
			self.dispatcher = DispatcherConsole(self.game_path)
			self.interface = None

		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"], data["text"], self.game_path)
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height, game_path, other_display)
			self.dispatcher = DispatcherGraphics(self.interface, self.game_path)
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
					game = Game(self.mode, event.level, self.game_path, self.display)
					thrown_command = game.start()
					if isinstance(thrown_command, ForcedExitCommand):
						self.display.finish()
						self.dispatcher.finish()
						return ForcedExitCommand()
					if isinstance(thrown_command, QuitPageCommand):
						continue

				if isinstance(event, QuitPageCommand):
					return QuitPageCommand()
