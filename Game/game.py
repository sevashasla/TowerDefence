from ..Display.display_graphics import DisplayGraphics
from ..Dispatcher.dispatcher_graphics import DispatcherGraphics

from ..Display.display_console import DisplayConsole
from ..Dispatcher.dispatcher_console import DispatcherConsole

from ..Map.field import Field
from .interface import Interface

from .pocket import Pocket
from .coordinates import Coordinates
<<<<<<< HEAD
<<<<<<< HEAD
from .errors import *	
=======
>>>>>>> delete it later
=======
from .errors import *	
>>>>>>> add files to checkpoint 2
from ..Tower.tower_factories import *
import os
import json

class Game:
	def __init__(self, mode):
		current_path = os.getcwd()
		with open(os.path.join(current_path, "TowerDefence/Data/last_completed_level.json")) as f:
			level = json.loads(os.path.join(f.read()))["last_completed_level"] + 1

		with open(os.path.join(current_path, "TowerDefence/Data/level" + str(level) + ".json")) as f:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
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
<<<<<<< HEAD
=======
			data = json.loads(f.read())
			interface_width = data["interface"]["width"]
			interface_height = data["interface"]["height"]
			self.width = data["shape"]["width"]
			self.height = data["shape"]["height"]

		self.pocket = Pocket()

		if(mode == "console"):
			self.display = DisplayConsole()
			self.dispatcher = DispatcherConsole()
			self.interface = None
		elif(mode == "graphics"):
			self.interface = Interface(self.width, self.height, interface_width, interface_height)
			self.display = DisplayGraphics(self.interface, max(self.width, interface_width), self.height + interface_height)
			self.dispatcher = DispatcherGraphics(self.interface)
		else:
			assert "wrong type of mode"

		self.field = Field(data)
		self.pocket = Pocket()
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2

	def start(self):
		self.display.start()
		self.dispatcher.start()

		running = True
<<<<<<< HEAD
<<<<<<< HEAD
		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}
=======


		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}
		
>>>>>>> delete it later
=======
		creators = {"WeakTower": WeakTowerCreator(), "AverageTower": AverageTowerCreator()}
>>>>>>> add files to checkpoint 2

		while running:
			for event in self.dispatcher.get_events():
				if(event[0] == "stop"):
					running = False
				elif (event[0] == "place"):
					class_of_tower = event[1]
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
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
<<<<<<< HEAD
=======
					pos = event[2]
					self.field.place_tower(creators[class_of_tower].create(pos))

					print("You've click at", pos)
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2

			self.display.show(self.field, self.pocket)
			self.field.update()
		self.dispatcher.finish()
		self.display.finish()
<<<<<<< HEAD
<<<<<<< HEAD
=======

	def finish(self):
		self.finish()
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2
