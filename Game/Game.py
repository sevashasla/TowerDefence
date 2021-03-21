import sys
sys.path.insert(0, "../Display/")
sys.path.insert(0, "../Dispatcher/")
sys.path.insert(0, "../Map/")
sys.path.insert(0, "../Tower/")

from Display_graphics import DisplayGraphics
from Dispatcher_graphics import DispatcherGraphics

from Display_console import DisplayConsole
from Dispatcher_console import DispatcherConsole

from field import Field

from pocket import Pocket
from coordinates import Coordinates
from tower_factories import *
# https://stackoverflow.com/questions/40336960/creating-rect-buttons-with-pygame
# sys.intern - equate via reference?

class Game:
	def __init__(self, mode):
		self.width = 500
		self.height = 500
		if(mode == "console"):
			self.display = DisplayConsole()
			self.dispatcher = DispatcherConsole()
		elif(mode == "graphics"):
			self.display = DisplayGraphics()
			self.dispatcher = DispatcherGraphics()
		else:
			assert "wrong type of mode"

		self.field = Field()
		self.pocket = Pocket()

	def start(self):
		self.display.start()
		self.dispatcher.start()

		running = True


		creator = WeakTowerCreator() #change later
		

		while running:
			for event in self.dispatcher.get_events():
				if(event[0] == "stop"):
					running = False
				elif(event[0] == "mouse_click"):
					pos = event[1]
					
					self.field.place_tower(creator.create(pos))

					print("You've click at", pos)
			self.display.show(self.field)
			self.field.step()
		self.dispatcher.finish()
		self.display.finish()

	def finish(self):
		self.finish()

def main():
	game = Game("graphics")
	game.start()


if __name__ == "__main__":
	main()

