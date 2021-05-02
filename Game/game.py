from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from ..Map.field import Field
from .interface import Interface

from .pocket import Pocket
from .coordinates import Coordinates
from .errors import *	
from ..Tower.tower_factories import *
import os
import json

from ..Command.stop import StopCommand
from ..Command.place_tower import PlaceTowerCommand


class Game:
	def __init__(self, mode, level, other_display):
		current_path = os.getcwd()

		with open(os.path.join(current_path, "TowerDefence/Data/" + level + ".json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.pocket = Pocket()

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
		self.field = Field(data)
		self.pocket = Pocket()
		self.error_catcher = ErrorCatcher()

	def start(self):
		self.display.start()
		self.dispatcher.start()

		get_stop_command = False
		running = True
		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}

		while running:
			self.display.show_game(self.field, self.pocket)
			
			for event in self.dispatcher.get_events():
				if isinstance(event, StopCommand):
					running = False
					get_stop_command = True

				elif isinstance(event, PlaceTowerCommand):
					class_of_tower = event.class_of_tower
					position = event.position
					try:
						self.field.place_tower(creators[class_of_tower].create(position))
					except FieldError:
						self.display.has_FieldError = True
						self.display.error_catcher.search_for_errors('FieldError')
					except MoneyError:
						self.display.has_MoneyError = True
						self.display.error_catcher.search_for_errors('MoneyError')
			
			try:
				self.field.update()
				if self.display.error_catcher.CastleError_count == 1:
					break
			except CastleError:
				self.display.has_CastleError = True
				self.display.error_catcher.search_for_errors('CastleError')
				
		self.dispatcher.finish()
		self.display.finish()

		return get_stop_command
