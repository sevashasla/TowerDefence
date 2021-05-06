import sys
import os
import time

from .dispatcher import Dispatcher
from ..Game.coordinates import Coordinates

from ..Command.levels_menu import LevelsMenuCommand
from ..Command.rules_menu import RulesMenuCommand
from ..Command.forced_exit import ForcedExitCommand
from ..Command.place_tower import PlaceTowerCommand
from ..Command.choose_level import ChooseLevelCommand
from ..Command.quit_page import QuitPageCommand


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

		if (time.time() - self.last_time_update) <= self.update_rate:
			return events

		input_ = sys.stdin.readline()
		event_split = input_.split()

		if event_split == []:
			pass

		elif event_split[0] == "levelmenu":
			events.append(LevelsMenuCommand())

		elif event_split[0] == "rulesmenu":
			events.append(RulesMenuCommand())

		elif event_split[0] == "quit":
			events.append(ForcedExitCommand())

		elif event_split[0] == "place":
			if event_split[1] == "weak":
				class_of_tower = "WeakTower"
			elif event_split[1] == "average":
				class_of_tower = "AverageTower"
			position = Coordinates(int(event_split[2]), int(event_split[3]))
			events.append(PlaceTowerCommand(class_of_tower, position))

		elif event_split[0] == "level":
			events.append(ChooseLevelCommand(event_split[0] + event_split[1]))

		else:
			raise TypeError("wrong type!")

		self.last_time_update = time.time()

		return events
