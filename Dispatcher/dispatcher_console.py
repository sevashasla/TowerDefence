import time
import sys
import os

from .dispatcher import Dispatcher
from ..Game.coordinates import Coordinates

from ..Command.stop import StopCommand
from ..Command.place_tower import PlaceTowerCommand

class DispatcherConsole(Dispatcher):
	def __init__(self):
		super().__init__()
		self.last_time_update = time.time()
		self.update_rate = 0.5

	def start(self):
		pass

	def finish(self):
		pass

	def get_events(self) -> list:
		events = []

		if (time.time() - self.last_time_update) >= self.update_rate:
			return events

		input_ = sys.stdin.readline()

		event_split = input_.split()

		if event_split[0] == "stop":
			events.append(StopCommand())

		elif event_split[0] == "c":
			pass

		elif event_split[0] == "place":
			if event_split[1] == "weak":
				class_of_tower = "WeakTower"
			elif event_split[1] == "average":
				class_of_tower = "AverageTower"
			position = Coordinates(int(event_split[2]), int(event_split[3]))
			events.append(PlaceTowerCommand(class_of_tower, position))

		else:
			raise TypeError("wrong type!")

		self.last_time_update = time.time()

		return events