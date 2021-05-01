import fcntl
import sys
import os

from .dispatcher import Dispatcher
from ..Game.coordinates import Coordinates

from ..Command.stop import StopCommand
from ..Command.place_tower import PlaceTowerCommand

class DispatcherConsole(Dispatcher):
	def __init__(self):
		super().__init__()

	def start(self):
		#make non-blocking stdin
		orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
		fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)

	def finish(self):
		pass

	def read_stdin(self):
		input_ = sys.stdin.readlines()
		return input_

	def get_events(self) -> list:
		events = []
		input_ = self.read_stdin()
		if input_:
			for event in input_:
				event = event.replace("\n", "")
				event_split = event.split()

				if event_split[0] == "stop":
					events.append(StopCommand())

				elif event_split[0] == "place":
					if event_split[1] == "weak":
						class_of_tower = "WeakTower"
					elif event_split[1] == "average":
						class_of_tower = "AverageTower"
					position = Coordinates(int(event_split[2]), int(event_split[3]))
					events.append(PlaceTowerCommand(class_of_tower, position))

		return events