from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from ..Display.error_catcher_console import ErrorCatcherConsole
from ..Display.error_catcher_graphics import ErrorCatcherGraphics

from ..Map.field import Field
from .interface import Interface

from .pocket import Pocket
from .coordinates import Coordinates
from .errors import *	
from ..Tower.tower_factories import *
import os
import json

from ..Command.forced_exit import ForcedExitCommand
from ..Command.quit_page import QuitPageCommand
from ..Command.place_tower import PlaceTowerCommand


class Game:
	def __init__(self, mode, level, game_path, other_display):
		self.game_path = game_path

		with open(os.path.join(self.game_path, "Data/" + level + ".json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.pocket = Pocket()

		if mode == "console":
			self.display = DisplayConsole(self.game_path, other_display)
			self.dispatcher = DispatcherConsole(self.game_path)
			self.interface = None
			self.error_catcher = ErrorCatcherConsole()
		elif mode == "graphics":
			self.interface = Interface(self.width, self.height, data["interface"], data["buttons"], [], self.game_path)
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height, self.game_path, other_display)
			self.dispatcher = DispatcherGraphics(self.interface, self.game_path)
			self.error_catcher = ErrorCatcherGraphics()
		else:
			raise ValueError("wrong type of mode")
		self.field = Field(data)
		self.pocket = Pocket()


	def start(self):
		self.display.start()
		self.dispatcher.start()

		get_stop_command = False
		running = True
		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}

		while running:
			self.display.show_game(self.field, self.pocket, self.error_catcher)
			
			for event in self.dispatcher.get_events():
				if isinstance(event, ForcedExitCommand):
					# running = False
					# get_stop_command = Tr

					self.dispatcher.finish()
					self.display.finish()
					return ForcedExitCommand()

				if isinstance(event, QuitPageCommand):
					return

				elif isinstance(event, PlaceTowerCommand):
					class_of_tower = event.class_of_tower
					position = event.position
					try:
						self.field.place_tower(creators[class_of_tower].create(position))
					except FieldError:
						self.error_catcher.has_FieldError = True
						self.error_catcher.search_for_errors('FieldError')
					except MoneyError:
						self.error_catcher.has_MoneyError = True
						self.error_catcher.search_for_errors('MoneyError')
			
			try:
				self.field.update()
				if self.error_catcher.CastleError_count == 1:
					return QuitPageCommand()
				if self.error_catcher.WinError_count == 1:
					return QuitPageCommand()
			except CastleError:
				self.error_catcher.has_CastleError = True
				self.error_catcher.search_for_errors('CastleError')
			except WinError:
				self.error_catcher.has_WinError = True
				self.error_catcher.search_for_errors('WinError')
