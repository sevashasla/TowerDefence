import fcntl
import sys
import os

from .dispatcher import Dispatcher
from ..Game.coordinates import Coordinates

from ..Command.levels_menu import LevelsMenuCommand
from ..Command.rules_menu import RulesMenuCommand
from ..Command.stop import StopCommand
from ..Command.place_tower import PlaceTowerCommand
from ..Command.choose_level import ChooseLevelCommand

class DispatcherConsole(Dispatcher):
	def __init__(self):
		super().__init__()

	def start(self):

		#make non-blocking stdin
		orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
		fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)
		sys.stdout.write("I am ready to check your signals\n")

	def finish(self):
		pass

	def get_events(self) -> list:
		events = []
		input_ = sys.stdin.readlines()
		if input_:
			for event in input_:
				event = event.replace("\n", "")
				event_split = event.split()
				if event_split[0] == "levelmenu":
					events.append(LevelsMenuCommand())

				elif event_split[0] == "rulesmenu":
					events.append(RulesMenuCommand())

				elif event_split[0] == "stop":
					events.append(StopCommand())

				elif event_split[0] == "place":
					if event_split[1] == "weak":
						class_of_tower = "WeakTower"
					elif event_split[1] == "average":
						class_of_tower = "AverageTower"
					position = Coordinates(int(event_split[2]), int(event_split[3]))
					events.append(PlaceTowerCommand(class_of_tower, position))

				elif event_split[0] == "level":
					events.append(ChooseLevelCommand(event_split[0] + event_split[1]))

		return events