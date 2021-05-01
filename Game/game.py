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

class Game:
	def __init__(self, mode, level):
		current_path = os.getcwd()
		# with open(os.path.join(current_path, "TowerDefence/Data/last_completed_level.json")) as f:
		# 	level = json.loads(os.path.join(f.read()))["last_completed_level"] + 1

		with open(os.path.join(current_path, "TowerDefence/Data/" + level + ".json")) as f:
			data = json.loads(os.path.join(f.read()))
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]

		self.pocket = Pocket()

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
		self.field = Field(data)
		self.pocket = Pocket()
		self.error_catcher = ErrorCatcher()

	def start(self):
		self.display.start()
		self.dispatcher.start()

		running = True
		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}

		while running:
			for event in self.dispatcher.get_events():
				if(event[0] == "stop"):
					running = False
				elif (event[0] == "place"):
					class_of_tower = event[1]
					position = event[2]
					try:
						self.field.place_tower(creators[class_of_tower].create(position))
					except FieldError:
						self.display.has_FieldError = True
						self.display.error_catcher.search_for_errors('FieldError')
					except MoneyError:
						self.display.has_MoneyError = True
						self.display.error_catcher.search_for_errors('MoneyError')

					print("You've click at", position)

			self.display.show_game(self.field, self.pocket)
			
			try:
				self.field.update()
			except CastleError:
				self.display.has_CastleError = True
				self.display.error_catcher.search_for_errors('CastleError')
		self.dispatcher.finish()
		self.display.finish()
