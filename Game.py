import sys
sys.path.insert(0, "../Display/")
sys.path.insert(0, "../Dispatcher/")

from Display_graphics import DisplayGraphics
from Dispatcher_graphics import DispatcherGraphics

from Display_console import DisplayConsole
from Dispatcher_console import DispatcherConsole


class Game:
	def __init__(self, mode):
		if(mode == "console"):
			self.display = DisplayConsole()
			self.dispatcher = DispatcherConsole()
		elif(mode == "graphics"):
			self.display = DisplayGraphics()
			self.dispatcher = DispatcherGraphics()
		else:
			assert "wrong type of mode"

	def start(self):
		self.display.start()
		self.dispatcher.start()

		running = True
		while running:
			for event in self.dispatcher.get_events():
				if(event[0] == "stop"):
					running = False
				elif(event[0] == "mouse_click"):
					print("You've click at", event[1])

		self.display.finish()
		self.dispatcher.finish()

	def finish(self):
		self.display.finish()
		self.dispatcher.finish()

def main():
	game = Game("graphics")
	game.start()


if __name__ == "__main__":
	main()

