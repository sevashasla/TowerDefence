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
from ..Command.forced_exit import ForcedExitCommand
from ..Command.choose_level import ChooseLevelCommand
from ..Command.quit_page import QuitPageCommand


def get_text_paths(game_path, text_name=None):
	if text_name is None:
		return os.path.join(game_path, "Data")
	else:
		return os.path.join(game_path, "Data", text_name)	


class MainMenu:
	def __init__(self, mode, game_path):
		self.game_path = game_path
		self.mode = mode


		with open(os.path.join(self.game_path, "Data/main_menu.json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]


		if mode == "console":
			self.text = []
			for cell in data["text"]:

				with open(get_text_paths(self.game_path, cell["text_path"]), 'r') as cell_file:
					self.text.append(cell_file.read())

			self.display = DisplayConsole(self.text, self.game_path)
			self.dispatcher = DispatcherConsole(self.game_path)
			self.interface = None
		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"], data["text"], game_path)
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height, game_path)
			self.dispatcher = DispatcherGraphics(self.interface, game_path)
		else:
			raise ValueError("wrong type of mode")


	def start(self):

		self.display.start()
		self.dispatcher.start()

		self.levels = LevelsMenu(self.mode, self.game_path, self.display)
		self.rules = RulesMenu(self.mode, self.game_path, self.display)
		
		running = True

		while running:
			self.display.show_menu()
			for event in self.dispatcher.get_events():
				if isinstance(event, ForcedExitCommand):
					self.dispatcher.finish()
					self.display.finish()
					return ForcedExitCommand()

				elif isinstance(event, LevelsMenuCommand):
					thrown_command = self.levels.start()
					if isinstance(thrown_command, ForcedExitCommand):
						self.dispatcher.finish()
						self.display.finish()
						return
					if isinstance(thrown_command, QuitPageCommand):
						continue

				elif isinstance(event, RulesMenuCommand):
					thrown_command = self.rules.start()
					if isinstance(thrown_command, ForcedExitCommand):
						self.dispatcher.finish()
						self.display.finish()
						return
					if isinstance(thrown_command, QuitPageCommand):
						continue

				elif isinstance(event, QuitPageCommand):
					return
		

