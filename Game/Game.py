import sys
sys.path.insert(0, "./Display/")
sys.path.insert(0, "./Dispatcher/")
sys.path.insert(0, "./Map/")
sys.path.insert(0, "./Tower/")


from Display_graphics import DisplayGraphics
from Dispatcher_graphics import DispatcherGraphics

from Display_console import DisplayConsole
from Dispatcher_console import DispatcherConsole

from field import Field
from interface import Interface

from pocket import Pocket
from coordinates import Coordinates
from tower_factories import *

# sys.intern - equate via reference?

class Game:
	def __init__(self, mode):
		self.width = 512
		self.height = 512 + 256
		self.pocket = Pocket()

		if(mode == "console"):
			self.display = DisplayConsole()
			self.dispatcher = DispatcherConsole()
			self.interface = None
		elif(mode == "graphics"):
			self.display = DisplayGraphics(self.width, self.height)
			self.dispatcher = DispatcherGraphics()
			self.interface = Interface()
		else:
			assert "wrong type of mode"

		self.field = Field()
		self.pocket = Pocket()

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
					pos = event[2]
					self.field.place_tower(creators[class_of_tower].create(pos))

					print("You've click at", pos)
			self.display.show(self.field, self.pocket)
			self.field.step()
		self.dispatcher.finish()
		self.display.finish()

	def finish(self):
		self.finish()
